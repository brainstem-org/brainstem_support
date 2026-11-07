#!/usr/bin/env python3
"""Build the generated reference pages of the support site from the BrainSTEM agent reference.

BrainSTEM serves a code-generated description of its REST API and JSON schemas at ``/reference/``
(``data/api_surface.json``, ``data/schemas.json``, ``data/relationships.json``, ``data/model_summaries.json``,
``data/manifest.json``). The same documents are written to disk by
``python manage.py export_agent_reference --out <dir>`` in the BrainSTEM repository. This script turns them into
Jekyll pages for the support site, so the API and schema documentation always matches the server.

Usage::

    # From an export directory (the <dir> passed to export_agent_reference, or a copy of /reference/data/):
    python scripts/build_reference_docs.py --reference /path/to/export

    # Or let the script run the export from a BrainSTEM checkout (its virtualenv must be set up):
    python scripts/build_reference_docs.py --brainstem /path/to/brainstem

    # Or fetch the documents from a running server:
    python scripts/build_reference_docs.py --server https://www.brainstem.org

    # Only fetch the interactive data model into docs/assets/datamodel/ (what the Pages deploy runs; the
    # data model is not committed):
    python scripts/build_reference_docs.py --server https://www.brainstem.org --assets-only

Generated pages carry a marker comment and are rewritten on every run. A page may keep hand-written text: anything
outside the ``<!-- generated:start -->`` / ``<!-- generated:end -->`` markers is preserved, so an introduction with
figures (for example the coordinate-system conventions) survives a rebuild.

Hand-written introductions for the data-model schema pages live in ``docs/_preambles/schemas/<family>.md`` and are
inserted after the table of contents (Jekyll ignores underscore directories).

Pages written:

- ``docs/api/<app>/<resource>.md`` – one page per REST resource (fields, endpoints, permissions, examples).
- ``docs/api/<app>.md`` – the resource index of each app.
- ``docs/api/schemas.md`` and ``docs/api/schemas/<family>.md`` – JSON schema families for API users.
- ``docs/api/relationships.md`` – how resources connect, as query routes.
- ``docs/datamodel/schemas.md`` and ``docs/datamodel/schemas/<family>.md`` – the same schema families, described
  for people who fill in the web forms.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"
SERVER = "https://www.brainstem.org"
START = "<!-- generated:start -->"
END = "<!-- generated:end -->"
DOCUMENTS = ("manifest", "api_surface", "schemas", "relationships", "model_summaries", "knowledge")

APP_TITLES = {
    "stem": "STEM",
    "modules": "Modules",
    "personal_attributes": "Personal Attributes",
    "resources": "Resources",
    "taxonomies": "Taxonomies",
    "dissemination": "Dissemination",
    "users": "Users",
}
APP_ORDER = ["stem", "modules", "personal_attributes", "resources", "taxonomies", "dissemination", "users"]
APP_INTROS = {
    "stem": (
        "The STEM app holds the core records of a study: projects, the subjects and specimen sets studied in "
        "them, the sessions in which data was recorded, and the cohorts, collections, breedings and epochs that "
        "organize them. Permissions for every other record derive from these."
    ),
    "modules": (
        "The Modules app holds what was done and recorded: procedures and specimen procedures with their material "
        "usages and procedure episodes, the experimental interfaces they create (implants, windows, fibers), data "
        "acquisition, manipulations and behaviors in sessions, logs followed over time, equipment, consumable "
        "stock, and reusable templates for each of them."
    ),
    "personal_attributes": (
        "Personal attributes are the lab's own resources: setups, inventories, behavioral assays, data storage, "
        "licenses and protocols. They are shared with groups rather than projects, and each has invitation "
        "endpoints for members and groups."
    ),
    "resources": (
        "Resources are the shared catalog used by every lab: consumables (probe designs, virus constructs, "
        "reagents), hardware devices and suppliers. Changes by users without approval rights become approval "
        "requests."
    ),
    "taxonomies": (
        "Taxonomies are the shared controlled vocabularies: species, strains, anatomical regions and their atlas "
        "references, coordinate transforms, behavioral categories and paradigms, setup types and regulatory "
        "authorities. Changes by users without approval rights become approval requests."
    ),
    "dissemination": (
        "Dissemination records the research output linked to projects: publications and the journals they "
        "appear in."
    ),
    "users": (
        "The Users app exposes accounts, groups, laboratories and the invitation and request records that "
        "manage membership."
    ),
}
SUPPORTING_SUFFIXES = ("approval", "membershipinvitation", "membershiprequest")
LINK_TABLES = {
    "cohortsubject",
    "collectionsession",
    "sessiondatastorage",
    "dataacquisitioninterface",
    "manipulationinterface",
    "episodepersonnel",
    "pendinginvitation",
}
# Hand-picked order of the main resources inside each app; the rest follow alphabetically.
PREFERRED_ORDER = {
    "stem": ["project", "subject", "session", "specimenset", "specimen", "cohort", "collection", "breeding", "epoch"],
    "modules": [
        "procedure", "procedureepisode", "procedurelog", "subjectlog", "specimenprocedure", "specimenlog",
        "experimentalinterface", "materialusage", "dataacquisition", "manipulation", "behavior", "equipment",
        "consumablestock", "proceduretemplate", "procedureepisodetemplate", "specimenproceduretemplate",
        "experimentalinterfacetemplate", "materialusagetemplate", "dataacquisitiontemplate", "manipulationtemplate",
    ],
    "personal_attributes": ["setup", "inventory", "behavioralassay", "datastorage", "license", "protocol"],
    "resources": ["consumable", "hardwaredevice", "supplier"],
    "taxonomies": [
        "species", "strain", "anatomicalregion", "anatomicalreference", "coordinatetransform", "behavioralcategory",
        "behavioralparadigm", "setuptype", "regulatoryauthority",
    ],
    "dissemination": ["publication", "journal"],
    "users": ["user", "group", "laboratory"],
}
# Families whose schemas belong to one model's own JSON fields (additional fields, repositories, external
# identifiers, specifications) rather than selecting a type (``selects_type: false`` in the reference). They get
# no page of their own: the model page describes each field in its hand-written Fields table, with a link to the
# latest schema, and the API flavour is appended to the model's API resource page. This maps each such family to
# its resource; a family the reference marks that is missing here maps to the resource of the same name.
INLINE_FAMILIES = {
    "Project": "project",
    "Session": "session",
    "Subject": "subject",
    "Setup": "setup",
    "DataStorage": "datastorage",
    "Species": "species",
    "Strain": "strain",
    "BehavioralParadigm": "behavioralparadigm",
}
FAMILY_INTROS = {
    "Coordinates": (
        "Coordinate systems describe where a procedure, an experimental interface or a piece of equipment is "
        "placed. Each system is a schema; the record stores the system code and the values in the frame it "
        "defines."
    ),
    "Procedure": "Type-specific details of in-vivo procedures performed on a subject.",
    "SpecimenProcedure": "Type-specific details of ex-vivo processing steps performed on a specimen set.",
    "SpecimenProcedureStage": (
        "Detail schemas for the stages of a procedure or specimen procedure: a phase several materials take part "
        "in together, such as the induction of an anesthetic or one bath of a staining protocol."
    ),
    "MaterialUsage": (
        "Detail schemas for material usage rows: one material in one role, as prepared or applied in a procedure, "
        "specimen procedure or experimental interface. The role (type) selects the schema."
    ),
    "ExperimentalInterface": (
        "Type-specific details of experimental interfaces: the point where hardware meets the animal or tissue, "
        "such as an implanted probe, a cranial window or an optic fiber."
    ),
    "DataAcquisition": "Type-specific details of the data recorded in a session.",
    "Manipulation": "Type-specific details of manipulations applied during a session.",
    "Equipment": "Type-specific details of equipment installed in a setup.",
    "HardwareDevice": "Type-specific details of hardware devices in the shared catalog.",
    "Consumable": "Type-specific details of consumables in the shared catalog, such as probe designs and virus constructs.",
    "ConsumableStock": "Type-specific details of a lab's own stock of a consumable.",
    "SubjectLog": "Entry schemas for subject logs: measurements and observations followed over time for one subject.",
    "ProcedureLog": "Entry schemas for procedure logs: measurements followed over time for one procedure.",
    "SpecimenLog": "Entry schemas for specimen logs: measurements followed over time for one specimen set.",
    "SpecimenSet": "Type-specific details of specimen sets: tissue or cultures prepared together.",
    "Specimen": "Type-specific details of individual specimens: one slice, section, well or organoid of a set.",
    "Project": "Schemas for the additional fields and repository links of a project.",
    "Session": "Schemas for the additional fields and repository links of a session.",
    "Subject": "Schemas for the additional fields of a subject.",
    "Setup": "Schema for the specifications of a setup.",
    "DataStorage": "Schemas for the data organization and access protocols of a data storage.",
    "Species": "Schema for the external identifiers of a species.",
    "Strain": "Schema for the external identifiers of a strain.",
    "BehavioralParadigm": "Schema for the external identifiers of a behavioral paradigm.",
}
# Families whose schemas describe the web form only (no REST selector/payload pair) still get pages.
PLACEHOLDER = {
    "uuid": "<id>",
    "string": "text",
    "date": "2024-03-22",
    "datetime": "2024-03-22T10:30:00Z",
    "duration": "01:00:00",
    "boolean": True,
    "number": 1,
    "json": {},
    "list": [],
}


# --------------------------------------------------------------------------------------------------------------
# Loading
# --------------------------------------------------------------------------------------------------------------


class Source:
    """The reference documents, read from an export directory or from a server's /reference/."""

    def __init__(self, base_dir: Path | None = None, server: str | None = None, temp: bool = False):
        self.base_dir, self.server, self.temp = base_dir, (server.rstrip("/") if server else None), temp

    def read(self, path: str) -> bytes:
        """``path`` is relative to the export root: ``manifest.json``, ``renderer/dom-utils.js``, ..."""
        if self.base_dir is not None:
            return (self.base_dir / path).read_bytes()
        prefix = "renderer/" if path.startswith("renderer/") else "data/"
        url = f"{self.server}/reference/{prefix}{path[9:] if prefix == 'renderer/' else path}"
        # /reference/ has its own throttle (600 requests a minute per IP by default), and the interactive
        # data model is some 450 files: wait as long as the server asks and try again.
        for attempt in range(30):
            try:
                with urllib.request.urlopen(url) as response:  # noqa: S310
                    return response.read()
            except urllib.error.HTTPError as error:
                if error.code != 429 or attempt == 29:
                    raise
                wait = min(int(error.headers.get("Retry-After") or 10), 120)
                print(f"throttled by {self.server}; waiting {wait} s", flush=True)
                time.sleep(wait)

    def json(self, path: str):
        return json.loads(self.read(path).decode("utf-8"))

    def close(self):
        if self.temp and self.base_dir:
            shutil.rmtree(self.base_dir, ignore_errors=True)


def load_reference(args, names=DOCUMENTS) -> tuple[dict, Source]:
    """Return the reference documents ``names`` as ``{name: document}`` and the source they came from."""
    if args.reference:
        source = Source(base_dir=Path(args.reference))
    elif args.brainstem:
        repo = Path(args.brainstem)
        python = repo / ".venv" / "bin" / "python"
        if not python.exists():
            python = Path(sys.executable)
        out = Path(tempfile.mkdtemp(prefix="brainstem-reference-"))
        subprocess.run(
            [str(python), "manage.py", "export_agent_reference", "--out", str(out)], cwd=repo, check=True,
        )
        source = Source(base_dir=out, temp=True)
    else:
        source = Source(server=args.server)
    return {name: source.json(f"{name}.json") for name in names}, source


def copy_datamodel_assets(source: Source, manifest: dict, out: Path, required: bool = False):
    """Copy the interactive data model (graph, per-type summaries, renderer) next to ``explorer.html``.

    Needs reference format 1.2 (the ``datamodel`` section of the manifest); on an older server the local copy is
    left as it is, or, when ``required``, the run fails so that a deploy never ships the site without it."""
    datamodel = manifest.get("datamodel")
    if not datamodel:
        message = f"interactive data model not published (reference format {manifest.get('format_version')})"
        if required:
            raise SystemExit(message)
        print(f"{message}; kept as is")
        return
    out.mkdir(parents=True, exist_ok=True)
    graph = source.json(datamodel.get("graph", "datamodel_graph.json"))
    (out / "graph.json").write_text(json.dumps(graph, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    index = source.json(datamodel.get("types", "datamodel_types.json"))
    pattern = index.get("path", "datamodel_types/{group}/{type}.json")
    types_dir = out / "types"
    shutil.rmtree(types_dir, ignore_errors=True)
    for entry in index.get("types", []):
        target = types_dir / entry["group"] / f"{entry['type']}.json"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source.read(pattern.replace("{group}", entry["group"]).replace("{type}", entry["type"])))
    renderer = datamodel.get("renderer", {})
    vendor = out / "vendor"
    vendor.mkdir(exist_ok=True)
    for entry in renderer.get("files", []):
        data = source.read(entry["path"])
        if entry.get("sha256") and hashlib.sha256(data).hexdigest() != entry["sha256"]:
            raise ValueError(f"{entry['path']}: checksum does not match the manifest")
        (vendor / Path(entry["path"]).name).write_bytes(data)
    summary = {
        "exported_from": source.server or "export_agent_reference",
        "server_commit": manifest.get("server_commit"),
        "format_version": manifest.get("format_version"),
        "graph_version": datamodel.get("graph_version", graph.get("version")),
        "renderer_version": renderer.get("version"),
        "models": len(graph.get("nodes", [])),
        "relations": len(graph.get("edges", [])),
        "types": len(index.get("types", [])),
    }
    (out / "manifest.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(
        f"copied the interactive data model: {summary['models']} models, {summary['relations']} relations, "
        f"{summary['types']} type summaries, renderer {summary['renderer_version']}"
    )


# --------------------------------------------------------------------------------------------------------------
# Writing
# --------------------------------------------------------------------------------------------------------------


def write_page(path: Path, front_matter: dict | None, body: str, commit: str):
    """Write ``body`` between the generated markers, keeping any hand-written text around them.

    ``front_matter`` is ``None`` for include snippets (``docs/_includes/...``), which carry no front matter."""
    header = ""
    if front_matter is not None:
        header = "\n".join(["---"] + [f"{key}: {value}" for key, value in front_matter.items()] + ["---", ""])
    marker = (
        f"<!-- Generated by scripts/build_reference_docs.py from the BrainSTEM reference "
        f"(server {commit[:12] or 'unknown'}). Edit the text outside the markers only. -->"
    )
    generated = f"{START}\n{marker}\n{{% raw %}}\n{body.rstrip()}\n{{% endraw %}}\n{END}\n"
    if path.exists():
        text = path.read_text(encoding="utf-8")
        if START in text and END in text:
            before = text[: text.index(START)]
            after = text[text.index(END) + len(END):]
            # The front matter is generated too (titles, nav placement); hand text between it and the marker stays.
            if header and before.startswith("---\n") and "\n---\n" in before[4:]:
                before = header + before[before.index("\n---\n", 4) + len("\n---\n"):]
            # Hand text after the END marker keeps one blank line before it; without this, every run added one.
            after = after.lstrip("\n")
            path.write_text(before + generated + ("\n" + after if after else ""), encoding="utf-8")
            return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text((header + "\n" if header else "") + generated, encoding="utf-8")


# Wording of server docstrings that reaches the pages; fixed here until the server text is corrected.
TEXT_FIXES = [("invigations", "invitations"), (" n the group", " in the group"), ("Cosumable", "Consumable")]


def fix_text(text: str | None) -> str:
    text = text or ""
    for old, new in TEXT_FIXES:
        text = text.replace(old, new)
    return text


def describe(resource: dict) -> str:
    """One sentence for index tables; the label when the server gives no description."""
    text = fix_text(resource.get("description")).strip()
    return text if text else f"{resource['label']} records."


def md_cell(text) -> str:
    if text is None:
        return ""
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def code(text) -> str:
    return f"`{text}`"


def humanize(name: str) -> str:
    return name.replace("_", " ").capitalize()


def slug(resource: str) -> str:
    return resource.lower()


# --------------------------------------------------------------------------------------------------------------
# API resource pages
# --------------------------------------------------------------------------------------------------------------


def is_supporting(resource: str) -> bool:
    return resource in LINK_TABLES or resource.endswith(SUPPORTING_SUFFIXES)


# Supporting resources leave their app's place in the side menu and are grouped under API instead: one group
# page each, the resource pages beneath it (their URLs stay under docs/api/<app>/).
NAV_GROUPS = [
    {
        "key": "templates", "title": "Templates", "nav_order": 12,
        "match": lambda r: r.endswith("template"),
        "intro": (
            "Templates prefill a new record of their kind: a procedure template carries the type, the type-specific "
            "fields and the material rows a lab repeats, and applying it copies them into a new procedure. Each "
            "template resource mirrors the record it is for and is shared through its projects."
        ),
    },
    {
        "key": "approvals", "title": "Approvals", "nav_order": 13,
        "match": lambda r: r.endswith("approval"),
        "intro": (
            "Shared catalogs and taxonomies are changed through approval requests: a submission creates a request "
            "that the admin team of that domain accepts, merges, sends back or rejects. These resources list and "
            "manage the requests; the accepted entries appear in the catalog resource itself."
        ),
    },
    {
        "key": "invitations", "title": "Invitations and requests", "nav_order": 14,
        "match": lambda r: "invitation" in r or r.endswith("membershiprequest"),
        "intro": (
            "Membership is managed through invitations and requests: an invitation offers a user or a group a role "
            "on a project, a group or a personal attribute, a request asks to join a group, and a pending invitation "
            "holds an invitation for an email address that has no account yet."
        ),
    },
    {
        "key": "links", "title": "Link tables", "nav_order": 15,
        "match": lambda r: r in LINK_TABLES,
        "intro": (
            "Link tables hold a many-to-many relation with its own fields, such as the subjects of a cohort or the "
            "interfaces a data acquisition used. Most of them are written through the records they connect; the "
            "resources here read and, where allowed, edit the rows directly."
        ),
    },
]


def nav_group(resource: str) -> dict | None:
    for group in NAV_GROUPS:
        if group["match"](resource):
            return group
    return None


def render_group_index(group: dict, members: list[dict], ctx: dict) -> str:
    lines = [f"# {group['title']} API endpoints", "{: .no_toc}", "", group["intro"], ""]
    lines.append("| Resource | App | What it is |")
    lines.append("|:---------|:----|:-----------|")
    for r in members:
        summary = describe(r).split(". ")[0].rstrip(".")
        lines.append(f"| [`{r['resource']}`]({page_path(r)}) | {APP_TITLES.get(r['app'], r['app'])} | {md_cell(summary)} |")
    lines.append("")
    return "\n".join(lines)


def resource_order(app: str, resources: list[dict]) -> list[dict]:
    preferred = PREFERRED_ORDER.get(app, [])

    def key(r):
        name = r["resource"]
        if name in preferred:
            return (0, preferred.index(name), name)
        if is_supporting(name):
            return (2, 0, name)
        return (1, 0, name)

    return sorted(resources, key=key)


def page_path(resource: dict) -> str:
    return f"/api/{resource['app']}/{slug(resource['resource'])}/"


def field_type_text(field: dict, by_model: dict) -> str:
    kind = field["kind"]
    if kind in ("relation", "relation_many"):
        target = by_model.get(field.get("target"))
        many = kind == "relation_many"
        if target:
            link = f"[`{target['resource']}`]({page_path(target)})"
        else:
            link = code(field.get("target", "?"))
        return f"{'list of ' if many else ''}{link} id{'s' if many else ''}"
    if kind == "choice":
        return "choice"
    if kind == "uuid":
        return "UUID string"
    if kind == "list":
        return "list of strings"
    if kind == "json":
        return "JSON object"
    if kind == "computed":
        return "computed"
    return kind


INLINE_CHOICES = 12  # longer choice lists go in a list under the field table


def field_description(field: dict, by_model: dict, version_fields: set, selectors: dict) -> str:
    """The Description cell of the two-column field table: type, flags, limits, then the server's help text.
    ``selectors`` maps a field that selects a schema type to its family, whose page lists the choices."""
    if field["name"] in selectors:
        family = selectors[field["name"]]
        text = f"one of the [{family} types](/api/schemas/{family.lower()}/)"
    elif field["kind"] == "choice" and field.get("choices") and len(field["choices"]) <= INLINE_CHOICES:
        text = "one of " + ", ".join(code(c) for c in field["choices"])
    elif field["kind"] == "choice" and field.get("choices"):
        text = "choice (see the list below)"
    else:
        text = field_type_text(field, by_model)
    if field["name"] in version_fields:
        text += " **[set by the server]**"
    elif field["write"] in ("read_only", "not_in_form"):
        text += " **[read-only]**"
    elif field["write"] == "write_only":
        text += " **[write-only]**"
    if field["required_on_create"] and field["name"] not in version_fields:
        text += " **[required]**"
    details = []
    if field.get("max_length"):
        details.append(f"max {field['max_length']} characters")
    if field.get("nullable"):
        details.append("nullable")
    if field.get("nestable"):
        details.append("nestable")
    if field.get("filter_by"):
        details.append(f"filter with `filter{{{field['filter_by']}}}=<name>`")
    if details:
        text += "; " + "; ".join(details)
    if field.get("help"):
        text += ". " + field["help"]
    return md_cell(text)


def example_value(field: dict, resource: dict):
    kind = field["kind"]
    name = field["name"]
    if kind == "uuid":
        return "<id>"
    if kind == "relation":
        return f"<{field.get('target', 'related').split('.')[-1]}-id>"
    if kind == "relation_many":
        return [f"<{field.get('target', 'related').split('.')[-1]}-id>"]
    if kind == "choice":
        choices = field.get("choices") or []
        if name == "status":
            # A performed (active, available) record: planned ones are not listed by default.
            for preferred in ("performed", "active", "available"):
                if preferred in choices:
                    return preferred
        return choices[0] if choices else ""
    if name == "name":
        return f"{resource['label']} 1"
    if name in ("details", "details_json", "coordinates_details", "coordinates_json", "type_json"):
        return {"...": "see the schema of the selected type"}
    if name == "tags":
        return []
    if kind == "string" and name.endswith("_schema_version"):
        return "set by the server"
    if kind == "string":
        return ""
    return PLACEHOLDER.get(kind, None)


def example_record(resource: dict) -> dict:
    record = {}
    for field in resource["fields"]:
        if field["write"] == "write_only":
            continue
        record[field["name"]] = example_value(field, resource)
    return record


NO_CREATE = {"user"}  # accounts are created by signing up, not through the API

# Fields the server requires only for some values of another field, which api_surface.json does not mark. The
# create examples pick the first choice (a subject session, an interface on a subject, a material from the
# inventory), so they add what that choice requires.
CONDITIONAL_CREATE = {
    "session": {"subjects": ["<subject-id>"]},
    "experimentalinterface": {"subject": "<subject-id>"},
    "materialusage": {"procedure": "<procedure-id>", "consumable_stock": "<consumablestock-id>"},
    "materialusagetemplate": {"source": "catalog", "consumable": "<consumable-id>"},
}


# The type an example uses when the selected main type does not say which ones it accepts.
DEFAULT_TYPES = {"Coordinates": "Stereotaxic_BregmaBrainSurface"}


def selected_type(family: dict, other_fields: list[str]) -> dict | None:
    """The first current type of a family that accepts related types for every other selector of the resource
    (a procedure type with coordinate systems, say), else the first current type."""
    types = [t for t in family.get("types", []) if not t.get("legacy")]
    for t in types:
        related = {r["field"]: r["types"] for r in t.get("related_types") or []}
        if all(related.get(f) for f in other_fields):
            return t
    return types[0] if types else None


def example_create(resource: dict, ctx: dict | None = None) -> dict:
    """A minimal create payload: the required fields, with real type codes where a field selects a schema."""
    families = (ctx or {}).get("families", {})
    selectors = {p["selector_field"]: p for p in resource.get("json_payloads", [])}
    version_fields = {p["version_field"] for p in resource.get("json_payloads", [])}
    names = {f["name"] for f in resource["fields"]} | {e["name"] for e in resource.get("form_only_fields", [])}
    # The main selector (usually `type`) decides which values the others may take.
    main = next(iter(selectors), None)
    chosen = selected_type(families.get(selectors[main]["schema_group"], {}), [s for s in selectors if s != main]) \
        if main else None
    related = {r["field"]: r["types"] for r in (chosen or {}).get("related_types") or []}
    payload = {}
    for field in resource["fields"]:
        if field["write"] not in ("form", "custom") or field["name"] in version_fields:
            continue
        if field["required_on_create"] or field["name"] in ("type", "details", "details_json"):
            if field["name"] == main:
                payload[field["name"]] = chosen["type"] if chosen else ""
            elif field["name"] in selectors and related.get(field["name"]):
                payload[field["name"]] = related[field["name"]][0]
            elif field["name"] in selectors:
                family_name = selectors[field["name"]]["schema_group"]
                types = [t["type"] for t in families.get(family_name, {}).get("types", []) if not t.get("legacy")]
                default = DEFAULT_TYPES.get(family_name)
                payload[field["name"]] = default if default in types else (types[0] if types else "")
            else:
                value = example_value(field, resource)
                payload[field["name"]] = f"<{field['name']}>" if value == "" else value
    for selector, p in selectors.items():
        if selector in payload and p["payload_field"] not in payload:
            payload[p["payload_field"]] = {"...": f"the fields of the selected {p['schema_group']} type"}
    for extra in resource.get("form_only_fields", []):
        if extra.get("required_on_create"):
            choices = extra.get("choices")
            if choices:
                payload[extra["name"]] = choices[0]
            elif extra["name"].endswith("s"):
                # A list of related ids, such as experimental_interfaces.
                payload[extra["name"]] = [f"<{extra['name'][:-1].replace('_', '')}-id>"]
            else:
                payload[extra["name"]] = f"<{extra['name']}>"
    for key, value in CONDITIONAL_CREATE.get(resource["resource"], {}).items():
        if key in names:
            payload[key] = value
    return payload


def py_literal(value) -> str:
    """A Python literal for an example payload: like JSON, but with True, False and None."""
    if isinstance(value, bool):
        return "True" if value else "False"
    if value is None:
        return "None"
    if isinstance(value, dict):
        return "{" + ", ".join(f"{json.dumps(k)}: {py_literal(v)}" for k, v in value.items()) + "}"
    if isinstance(value, list):
        return "[" + ", ".join(py_literal(v) for v in value) + "]"
    return json.dumps(value, ensure_ascii=False)


def example_change(resource: dict) -> dict:
    """One writable field with a changed value, for the Change example."""
    for field in resource["fields"]:
        if field["write"] == "form" and field["kind"] == "string" and field["name"] == "name":
            return {"name": f"{resource['label']} 1 (renamed)"}
    for field in resource["fields"]:
        if field["write"] == "form" and field["kind"] in ("string", "boolean", "number", "date", "datetime"):
            value = example_value(field, resource)
            return {field["name"]: value if value != "" else "new value"}
    for field in resource["fields"]:
        if field["write"] == "form":
            return {field["name"]: example_value(field, resource)}
    return {}


def matlab_struct(payload: dict) -> str:
    """A MATLAB struct(...) literal for a small payload."""
    parts = []
    for key, value in payload.items():
        if isinstance(value, list):
            inner = ", ".join(f"'{v}'" for v in value)
            parts.append(f"'{key}', {{{{{inner}}}}}")
        elif isinstance(value, dict):
            parts.append(f"'{key}', struct()")
        elif isinstance(value, bool):
            parts.append(f"'{key}', {'true' if value else 'false'}")
        elif isinstance(value, (int, float)):
            parts.append(f"'{key}', {value}")
        else:
            parts.append(f"'{key}', '{value}'")
    return "struct(" + ", ".join(parts) + ")"


def json_block(value) -> str:
    return "```json\n" + json.dumps(value, indent=4, ensure_ascii=False) + "\n```"


def deleting_text(resource: dict, edges: list[dict], by_resource: dict) -> str | None:
    groups: dict[str, set] = {}
    for edge in edges:
        if edge["target"] == resource["resource"] and edge.get("on_delete") and edge["source"] != resource["resource"]:
            groups.setdefault(edge["on_delete"], set()).add(edge["source"])
    parts = []

    def links(names):
        return ", ".join(f"[`{n}`]({page_path(by_resource[n])})" for n in sorted(names) if n in by_resource)

    if groups.get("CASCADE"):
        parts.append(f"also deletes the linked {links(groups['CASCADE'])} records")
    if groups.get("PROTECT"):
        parts.append(f"refused (400) while {links(groups['PROTECT'])} records point to it")
    if groups.get("SET_NULL"):
        parts.append(f"clears the link on {links(groups['SET_NULL'])} records")
    return "; ".join(parts) if parts else None


def permission_text(resource: dict, by_model: dict, by_resource: dict) -> str:
    perm = resource.get("permission_path")
    if not perm:
        return "see the [permissions page](/datamodel/permissions/)"
    path = perm.get("path", "")
    if path == "object permissions":
        return "object permissions on the record itself (member / manager / owner roles)"
    anchor = perm.get("anchor")
    anchor_res = by_model.get(anchor)
    chain = " → ".join(code(hop) for hop in path.split(" | ")[0].split(".")) if path else ""
    text = f"inherited through {chain}" if chain else "inherited"
    if "|" in path:
        alternatives = " or ".join(code(p) for p in path.split(" | "))
        text = f"inherited through {alternatives}"
    if anchor_res:
        text += f" (from [`{anchor_res['resource']}`]({page_path(anchor_res)}))"
    return text


def render_resource_page(resource: dict, ctx: dict) -> str:
    by_model, by_resource, edges = ctx["by_model"], ctx["by_resource"], ctx["edges"]
    name = resource["resource"]
    label = resource["label"]
    private = resource["paths"].get("private")
    public = resource["paths"].get("public")
    lines = [f"# {label} API endpoint", "{: .no_toc}", ""]
    lines.append(fix_text(resource["description"]))
    lines += ["", "## Table of contents", "{: .no_toc .text-delta }", "", "1. TOC", "{:toc}", ""]

    # Endpoints block
    lines.append("## Endpoints")
    lines.append("")
    if private:
        lines.append(f"- **Private portal:** `{SERVER}{private}` (needs a token; one record: append `<id>/`)")
    if public:
        lines.append(f"- **Public portal:** `{SERVER}{public}` (read-only, public projects, no token)")
    else:
        lines.append("- **Public portal:** not available")
    lines.append(
        f"- **Response keys:** `{resource['response_key']}` (detail, create, update), "
        f"`{resource['response_key_plural']}` (list)"
    )
    lines.append(f"- **Permissions:** {permission_text(resource, by_model, by_resource)}")
    for uniq in resource.get("uniqueness", []):
        fields = ", ".join(code(f) for f in uniq["fields"])
        if uniq["scope"] == "global":
            lines.append(f"- **Uniqueness:** {fields} unique across BrainSTEM")
        else:
            lines.append(f"- **Uniqueness:** {fields} unique together")
    names = {f["name"] for f in resource["fields"]}
    for payload in resource.get("json_payloads", []):
        family = payload["schema_group"]
        send = payload["payload_field"]
        read = send[:-5] if send.endswith("_json") and send[:-5] in names and send not in names else send
        where = f"send its fields in `{send}`" + (f" (responses return them as `{read}`)" if read != send else "")
        lines.append(
            f"- **Schema payload:** `{payload['selector_field']}` selects a "
            f"[{family} type](/api/schemas/{family.lower()}/); {where}. "
            f"`{payload['version_field']}` is set by the server; do not send it."
        )
    type_family = resource.get("type_family")
    if type_family and not resource.get("json_payloads"):
        family = type_family["schema_group"]
        lines.append(
            f"- **Entry schemas:** `{type_family['field']}` selects a [{family} type](/api/schemas/{family.lower()}/); "
            f"each log entry is validated against it."
        )
    deleting = deleting_text(resource, edges, by_resource)
    if deleting:
        lines.append(f"- **Deleting:** {deleting}")
    if resource.get("form_only_fields"):
        lines.append("")
        lines.append("Form-only inputs (sent on create or update, not returned in responses):")
        lines.append("")
        for extra in resource["form_only_fields"]:
            req = " **[required]**" if extra.get("required_on_create") else ""
            choices = f" Choices: {', '.join(code(c) for c in extra['choices'])}." if extra.get("choices") else ""
            help_text = f" {extra['help']}" if extra.get("help") else ""
            lines.append(f"- `{extra['name']}`{req}.{choices}{help_text}")
    lines.append("")

    # Fields table
    lines.append("## Fields")
    lines.append("")
    lines.append(
        "**[required]** fields must be sent on create; **[read-only]** fields are returned but cannot be set. "
        "A *nestable* relation can be traversed in filters (`filter{field.other}`) and sideloaded with "
        "`include[]=field.*`; other relations can only be compared with ids (`filter{field}=<id>`). "
        "See the [query syntax](/api/#query-parameters)."
    )
    lines.append("")
    lines.append("| Field | Description |")
    lines.append("|:------|:------------|")
    version_fields = {p["version_field"] for p in resource.get("json_payloads", [])}
    selectors = {p["selector_field"]: p["schema_group"] for p in resource.get("json_payloads", [])}
    if type_family:
        selectors.setdefault(type_family["field"], type_family["schema_group"])
    choice_rows = []
    for field in resource["fields"]:
        if field["name"] not in selectors and field.get("choices") and len(field["choices"]) > INLINE_CHOICES:
            choice_rows.append((field["name"], field["choices"]))
        lines.append(f"| `{field['name']}` | {field_description(field, by_model, version_fields, selectors)} |")
    if choice_rows:
        lines.append("")
        for field_name, choices in choice_rows:
            lines.append(f"- `{field_name}` choices: {', '.join(code(c) for c in choices)}")
    if resource.get("ordered_fields"):
        lines.append("")
        lines.append(
            f"Ordered lists: {', '.join(code(f) for f in resource['ordered_fields'])} keep the order in which the "
            "ids are sent."
        )
    lines.append("")

    # Operations
    singular = resource["response_key"]
    plural = resource["response_key_plural"]
    record = example_record(resource)
    portals = ", ".join(resource["portals"])
    lines.append("## List")
    lines.append(f"- **Allowed portals:** {portals}")
    lines.append("- **Request method:** GET")
    lines.append(f"- **URL:** `{SERVER}{private or public}`")
    lines.append("- **Responses:** `200` OK; `401` Not authenticated; `403` Not allowed")
    lines.append("")
    lines.append("### Use example (Python API tool)")
    lines.append("{: .no_toc}")
    lines.append("")
    lines.append("```python")
    lines.append(f"resp = client.load('{name}', load_all=True)")
    lines.append(f"records = resp['{plural}']")
    lines.append("```")
    lines.append("")
    lines.append("### Use example (MATLAB API tool)")
    lines.append("{: .no_toc}")
    lines.append("")
    lines.append("```matlab")
    lines.append(f"resp = client.load('{name}', 'load_all', true);")
    lines.append(f"records = resp.{plural};")
    lines.append("```")
    lines.append("")
    lines.append("### Response example")
    lines.append("{: .no_toc}")
    lines.append("")
    lines.append(json_block({
        plural: [record],
        "meta": {"page": 1, "per_page": 100, "total_results": 1, "total_pages": 1},
    }))
    lines.append("")

    writable = any(f["write"] in ("form", "custom") for f in resource["fields"]) and "private" in resource["portals"]
    creatable = writable and resource.get("write_path") != "custom" and name not in NO_CREATE
    if creatable:
        lines.append("## Add")
        lines.append("- **Allowed portals:** private")
        lines.append("- **Request method:** POST")
        lines.append(f"- **URL:** `{SERVER}{private}`")
        lines.append("- **Data:** JSON object with at least the required fields")
        lines.append("- **Responses:** `201` Created; `400` Bad request (validation errors per field); `403` Not allowed")
        lines.append("")
        lines.append("### Use example (Python API tool)")
        lines.append("{: .no_toc}")
        lines.append("")
        create = example_create(resource, ctx)
        lines.append("```python")
        lines.append(f"resp = client.save('{name}', data={py_literal(create)})")
        lines.append(f"record = resp.json()['{singular}']")
        lines.append("```")
        lines.append("")
        lines.append("### Use example (MATLAB API tool)")
        lines.append("{: .no_toc}")
        lines.append("")
        lines.append("```matlab")
        note = "  % struct() stands for the fields of the selected type" if any(isinstance(v, dict) for v in create.values()) else ""
        lines.append(f"created = client.save({matlab_struct(create)}, '{name}');{note}")
        lines.append(f"record = created.{singular};")
        lines.append("```")
        lines.append("")

    lines.append("## Detail")
    lines.append(f"- **Allowed portals:** {portals}")
    lines.append("- **Request method:** GET")
    lines.append(f"- **URL:** `{SERVER}{private or public}<id>/`")
    lines.append("- **Responses:** `200` OK; `403` Not allowed; `404` Not found")
    lines.append("")
    lines.append("### Use example (Python API tool)")
    lines.append("{: .no_toc}")
    lines.append("")
    lines.append("```python")
    lines.append(f"resp = client.load('{name}', id='<id>')")
    lines.append(f"record = resp.json()['{singular}']")
    lines.append("```")
    lines.append("")
    lines.append("### Use example (MATLAB API tool)")
    lines.append("{: .no_toc}")
    lines.append("")
    lines.append("```matlab")
    lines.append(f"out = client.load('{name}', 'id', '<id>');")
    lines.append(f"record = out.{singular};")
    lines.append("```")
    lines.append("")
    lines.append("### Response example")
    lines.append("{: .no_toc}")
    lines.append("")
    lines.append(json_block({singular: record}))
    lines.append("")

    if writable and resource.get("write_path") != "custom":
        change = example_change(resource)
        lines.append("## Change")
        lines.append("- **Allowed portals:** private")
        lines.append("- **Request method:** PATCH")
        lines.append(f"- **URL:** `{SERVER}{private}<id>/`")
        lines.append(
            "- **Data:** JSON object with the fields to change. Lists (`projects`, `tags`, ...) and JSON payloads "
            "(`details`, coordinates) are replaced as a whole: read the record first and send the full list or object."
        )
        lines.append("- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found")
        lines.append("")
        lines.append("### Use example (Python API tool)")
        lines.append("{: .no_toc}")
        lines.append("")
        lines.append("```python")
        lines.append(f"resp = client.save('{name}', id='<id>', data={py_literal(change)})")
        lines.append("```")
        lines.append("")
        lines.append("### Use example (MATLAB API tool)")
        lines.append("{: .no_toc}")
        lines.append("")
        lines.append("```matlab")
        lines.append(f"client.save({matlab_struct({'id': '<id>', **change})}, '{name}', 'method', 'patch');")
        lines.append("```")
        lines.append("")
    if creatable:
        lines.append("## Delete")
        lines.append("- **Allowed portals:** private")
        lines.append("- **Request method:** DELETE")
        lines.append(f"- **URL:** `{SERVER}{private}<id>/`")
        lines.append(
            "- **Responses:** `204` Deleted; `400` Still referenced by other records; `403` Not allowed; "
            "`404` Not found"
        )
        lines.append("")
        lines.append("### Use example (Python API tool)")
        lines.append("{: .no_toc}")
        lines.append("")
        lines.append("```python")
        lines.append(f"resp = client.delete('{name}', id='<id>')")
        lines.append("```")
        lines.append("")
        lines.append("### Use example (MATLAB API tool)")
        lines.append("{: .no_toc}")
        lines.append("")
        lines.append("```matlab")
        lines.append(f"client.delete('<id>', '{name}');")
        lines.append("```")
        lines.append("")
    if resource.get("write_path") == "custom":
        lines.append("## Writing")
        lines.append("")
        lines.append(
            "This resource is maintained by BrainSTEM administrators or system processes and is read-only "
            "through the REST API."
        )
        lines.append("")

    if resource.get("actions"):
        lines.append("## Custom actions")
        lines.append("")
        lines.append("| Action | Request |")
        lines.append("|:-------|:--------|")
        for action in resource["actions"]:
            base = (private or public).rstrip("/")
            # Route regexes such as (?P<job_id>[0-9a-fA-F-]{36}) read as <job_id>.
            path = re.sub(r"\(\?P<(\w+)>[^)]*\)", r"<\1>", action["url_path"])
            url = f"{base}/<id>/{path}/" if action["detail"] else f"{base}/{path}/"
            lines.append(f"| `{action['name']}` | {', '.join(action['methods'])} `{url}` |")
        lines.append("")
        notes = ACTION_NOTES.get(name) or ACTION_NOTES.get("_default_" + "_".join(
            sorted(a["name"] for a in resource["actions"])
        ))
        if notes:
            lines.append(notes)
            lines.append("")

    inline = inline_family_for(name, ctx)
    if inline:
        lines += render_inline_family_api(inline, resource, ctx)

    # Data model link
    datamodel = ctx["datamodel_pages"].get(name)
    if datamodel:
        lines.append("## Data model")
        lines.append("")
        lines.append(
            f"The fields are described for the web forms on the [{label} data model page]({datamodel})."
        )
        lines.append("")
    return "\n".join(lines)


ACTION_NOTES = {
    "procedure": (
        "`materials` returns the ordered material usage rows of the procedure; `PUT` replaces them as a whole "
        "(a stale list is refused with 409). `apply-material-template` copies the rows of a material usage "
        "template onto the procedure. `material-options` lists the material roles and allowed sources of a "
        "procedure type (`?type=<Type>`). `coordinate-preview` renders the saved or posted coordinates in the "
        "atlas of the subject's species."
    ),
    "specimenprocedure": (
        "`materials` returns the ordered material usage rows of the specimen procedure; `PUT` replaces them as a "
        "whole. `apply-material-template` copies the rows of a material usage template. `material-options` lists "
        "the material roles and allowed sources of a type (`?type=<Type>`)."
    ),
    "experimentalinterface": (
        "`materials` returns the ordered material usage rows that describe what the interface is made of; `PUT` "
        "replaces them as a whole. `apply-material-template` copies the rows of a material usage template. "
        "`material-options` lists the material roles and allowed sources of an interface type (`?type=<Type>`)."
    ),
    "procedurelog": (
        "Log entries are edited through the actions: `add_entry` appends an entry validated against the log type's "
        "schema, `change_entry` replaces one entry and `remove_entry` deletes it. Each takes the entry in the "
        "request body."
    ),
    "subjectlog": (
        "Log entries are edited through the actions: `add_entry` appends an entry validated against the log type's "
        "schema, `change_entry` replaces one entry and `remove_entry` deletes it."
    ),
    "project": (
        "`export` returns the project as versioned JSON (see [Exports](/api/export/)); `POST` starts a background "
        "export job, `export-jobs` lists your jobs for the project and `export-jobs/<job_id>/download/` fetches "
        "the finished file."
    ),
    "session": (
        "`export` returns the session with everything it touches as versioned JSON (see [Exports](/api/export/)); "
        "`POST` starts a background export job."
    ),
    "anatomicalregion": (
        "`descendants` returns the regions below a region in its atlas hierarchy."
    ),
}
ACTION_NOTES["_default_accept_approval_cancel_approval_changes_required_approval_hold_for_merge_approval"
             "_hold_for_rejection_approval_merge_approval_reject_approval"] = (
    "Approval requests are reviewed by the admin team of the taxonomy or resource. The actions move a request "
    "through its lifecycle: `accept`, `reject`, `require_changes`, `hold_for_merge`, `merge` (merge into an "
    "existing record given by `merge_to_id`) and `cancel` (by the submitter)."
)


def render_app_index(app: str, resources: list[dict], ctx: dict) -> str:
    lines = [f"# {APP_TITLES[app]} API endpoints", "{: .no_toc}", "", APP_INTROS.get(app, ""), ""]
    main = [r for r in resources if not is_supporting(r["resource"])]
    supporting = [r for r in resources if is_supporting(r["resource"])]
    lines.append("## Resources")
    lines.append("")
    lines.append("| Resource | What it is | Portals |")
    lines.append("|:---------|:-----------|:--------|")
    for r in main:
        lines.append(
            f"| [`{r['resource']}`]({page_path(r)}) | {md_cell(describe(r))} | {', '.join(r['portals'])} |"
        )
    if supporting:
        lines.append("")
        lines.append("## Supporting endpoints")
        lines.append("")
        lines.append(
            "Approval requests, membership invitations and link tables. Most workflows never call these directly; "
            "the main resources create and resolve them."
        )
        lines.append("")
        lines.append("| Resource | What it is | Portals |")
        lines.append("|:---------|:-----------|:--------|")
        for r in supporting:
            lines.append(
                f"| [`{r['resource']}`]({page_path(r)}) | {md_cell(describe(r))} | {', '.join(r['portals'])} |"
            )
    lines.append("")
    lines.append(
        f"All endpoints follow `{SERVER}/api/{{portal}}/{app}/{{resource}}/` and support the common "
        "[query parameters](/api/#query-parameters)."
    )
    return "\n".join(lines)


# --------------------------------------------------------------------------------------------------------------
# Schema pages
# --------------------------------------------------------------------------------------------------------------


def shape_text(prop: dict) -> str:
    shape = prop["shape"]
    names = {
        "numberUnit": "quantity with unit",
        "array_of_strings": "multi-select",
        "array_of_objects": "table of rows",
        "array_of_integers": "list of integers",
        "enum": "choice",
        "ratio": "ratio",
        "integer": "integer",
        "number": "number",
        "boolean": "yes/no",
        "string": "text",
        "object": "object",
    }
    text = names.get(shape, shape)
    if prop.get("format") == "textarea":
        text = "text (multi-line)"
    return text


def allowed_values_api(prop: dict) -> str:
    parts = []
    if prop.get("enum"):
        parts.append("one of " + ", ".join(code(e["code"]) for e in prop["enum"]))
    if prop.get("units"):
        parts.append("units " + ", ".join(code(u) for u in prop["units"]))
    bounds = []
    if "minimum" in prop:
        bounds.append(f"≥ {prop['minimum']}")
    if "exclusiveMinimum" in prop:
        bounds.append(f"> {prop['exclusiveMinimum']}")
    if "maximum" in prop:
        bounds.append(f"≤ {prop['maximum']}")
    if bounds:
        parts.append(" and ".join(bounds))
    if prop.get("default") is not None:
        parts.append(f"default `{json.dumps(prop['default'], ensure_ascii=False)}`")
    if prop.get("format") and prop["format"] not in ("text", "textarea", "checkbox"):
        parts.append(f"format {prop['format']}")
    if prop.get("hidden"):
        parts.append("hidden legacy field")
    return "; ".join(parts)


def allowed_values_human(prop: dict) -> str:
    parts = []
    if prop.get("enum"):
        titles = [e.get("title") or e["code"] for e in prop["enum"]]
        parts.append("Options: " + ", ".join(titles))
    if prop.get("units"):
        parts.append("Units: " + ", ".join(prop["units"]))
    bounds = []
    if "minimum" in prop:
        bounds.append(f"≥ {prop['minimum']}")
    if "exclusiveMinimum" in prop:
        bounds.append(f"> {prop['exclusiveMinimum']}")
    if "maximum" in prop:
        bounds.append(f"≤ {prop['maximum']}")
    if bounds:
        parts.append("Range: " + " and ".join(bounds))
    return ". ".join(parts)


def example_payload(type_entry: dict) -> dict | list:
    """An illustrative payload: every required property plus the first few optional ones."""
    props = type_entry["properties"]
    top = [p for p in props if "[]" not in p["path"] and "." not in p["path"]]
    chosen = [p for p in top if p["required"]] + [p for p in top if not p["required"]][:2]
    payload = {}
    for prop in chosen:
        payload[prop["path"]] = example_property(prop, props)
    if type_entry["shape"] == "array":
        return [payload] if payload else []
    return payload


def example_property(prop: dict, props: list[dict]):
    shape = prop["shape"]
    if shape == "enum":
        return prop["enum"][0]["code"] if prop.get("enum") else "code"
    if shape == "numberUnit":
        unit = (prop.get("default") or {}).get("unit") or (prop.get("units") or ["unit"])[0]
        return {"value": 1, "unit": unit}
    if shape == "array_of_strings":
        return [prop["enum"][0]["code"]] if prop.get("enum") else ["text"]
    if shape == "array_of_integers":
        return [1, 2]
    if shape == "integer":
        return prop.get("default", 1) if isinstance(prop.get("default"), int) else 1
    if shape == "number":
        return 1.0
    if shape == "boolean":
        return bool(prop.get("default", True))
    if shape == "ratio":
        return {"numerator": 1, "denominator": 10}
    if shape == "array_of_objects":
        prefix = prop["path"] + "[]."
        row = {
            p["path"][len(prefix):]: example_property(p, props)
            for p in props
            if p["path"].startswith(prefix) and "[]" not in p["path"][len(prefix):] and p["required"]
        }
        return [row]
    if shape == "object":
        prefix = prop["path"] + "."
        return {
            p["path"][len(prefix):]: example_property(p, props)
            for p in props
            if p["path"].startswith(prefix) and "." not in p["path"][len(prefix):]
        }
    return "text"


# The schema families on the Schemas page and in the side menu, by area of the data model.
SCHEMA_AREAS = [
    ("Subjects and in-vivo procedures",
     "What is done to a subject and what is logged about it over time.",
     ["Procedure", "SpecimenProcedureStage", "ProcedureLog", "SubjectLog"]),
    ("Specimens and ex-vivo processing",
     "Ex-vivo material, its processing and its logs.",
     ["SpecimenSet", "Specimen", "SpecimenProcedure", "SpecimenLog"]),
    ("Interfaces, recordings and manipulations",
     "Where hardware meets the animal or tissue, what was recorded through it and what was delivered, and the "
     "coordinate systems that place them.",
     ["ExperimentalInterface", "DataAcquisition", "Manipulation", "Coordinates"]),
    ("Materials",
     "The shared catalog of consumables, a lab's stock of them, and the material rows of procedures and interfaces.",
     ["Consumable", "ConsumableStock", "MaterialUsage"]),
    ("Equipment and devices",
     "The shared catalog of hardware devices and the equipment installed in a lab's setups.",
     ["HardwareDevice", "Equipment"]),
]


def family_nav_order(families: list[dict]) -> list[str]:
    """Family names in the order of SCHEMA_AREAS, then any family the areas do not name."""
    named = [n for _, _, names in SCHEMA_AREAS for n in names]
    present = [f["family"] for f in families if f["family"] not in INLINE_FAMILIES]
    return [n for n in named if n in present] + [n for n in present if n not in named]


def type_intros(family_name: str) -> tuple[dict[str, str], dict[str, str]]:
    """Hand-written introductions for a family's groups and types, from
    docs/_preambles/schemas/types/<family>.md ("## group: <name>" and "## <TypeCode>" sections). They are used
    where the schema itself has no description; the proper home of a type description is its schema."""
    path = DOCS / "_preambles" / "schemas" / "types" / f"{family_name.lower()}.md"
    groups: dict[str, str] = {}
    types: dict[str, str] = {}
    if not path.exists():
        return groups, types
    key = None
    buffer: list[str] = []

    def flush():
        if key is None:
            return
        text = " ".join(line.strip() for line in buffer if line.strip())
        if key.startswith("group:"):
            groups[key[6:].strip()] = text
        else:
            types[key] = text

    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            flush()
            key, buffer = line[3:].strip(), []
        elif key is not None and not line.startswith("<!--"):
            buffer.append(line)
    flush()
    return groups, types


def text_anchor(text: str) -> str:
    """The heading id kramdown generates for a heading text."""
    text = re.sub(r"[^a-z0-9 -]", "", text.lower()).replace(" ", "-")
    return re.sub(r"^[^a-z]+", "", text) or "section"


def group_descriptions(family: dict) -> dict[str, str]:
    """The family's groups in reading order with their descriptions: the server's (schemas.json `groups`, reference
    format 1.3), then any group only the hand-written introductions file names."""
    groups = {g["name"]: g.get("description") or "" for g in family.get("groups") or []}
    for name, text in type_intros(family["family"])[0].items():
        if not groups.get(name):
            groups[name] = text
    return groups


def grouped_types(family: dict) -> list[tuple[str | None, list[dict]]]:
    """The family's types by group: groups in the order of the family's introductions file (the order a reader
    meets them), then in order of appearance; types without a group last."""
    order: list[str | None] = []
    groups: dict[str | None, list[dict]] = {}
    for t in family["types"]:
        group = t.get("group")
        if group not in groups:
            groups[group] = []
            order.append(group)
        groups[group].append(t)
    preferred = list(group_descriptions(family))
    order.sort(key=lambda g: (g is None, preferred.index(g) if g in preferred else len(preferred)))
    return [(g, groups[g]) for g in order]


def family_users(family_name: str, resources: list[dict]) -> list[tuple[dict, dict]]:
    users = []
    for r in resources:
        for payload in r.get("json_payloads", []):
            if payload["schema_group"] == family_name:
                users.append((r, payload))
        tf = r.get("type_family")
        if tf and tf["schema_group"] == family_name and not r.get("json_payloads"):
            users.append((r, {"selector_field": tf["field"], "payload_field": "entries"}))
    return users


def type_anchor(type_entry: dict) -> str:
    """The heading id kramdown generates: lowercase, drop everything but letters, digits, spaces and hyphens,
    spaces to hyphens (so "AP/ML/DV" becomes "apmldv" and "2.0" becomes "20")."""
    return text_anchor(type_entry.get("label") or type_entry["title"])


def render_schema_family_api(family: dict, ctx: dict) -> str:
    name = family["family"]
    resources = ctx["resources"]
    lines = [f"# {name} schemas", "{: .no_toc}", ""]
    lines.append(FAMILY_INTROS.get(name, f"Type-specific JSON schemas of the {name} family."))
    lines.append("")
    if family.get("development"):
        lines.append("{: .warning }")
        lines.append(
            "> This family is **experimental**: its schemas may change shape between releases without a version "
            "bump. Treat writes to these types as experimental."
        )
        lines.append("")
    lines += ["## Table of contents", "{: .no_toc .text-delta }", "", "1. TOC", "{:toc}", ""]
    lines.append("## How to use this family")
    lines.append("")
    users = family_users(name, resources)
    if users:
        for r, payload in users:
            if payload["payload_field"] == "entries":
                lines.append(
                    f"- [`{r['resource']}`]({page_path(r)}): `{payload['selector_field']}` selects the type; each "
                    "log entry added through the entry actions is validated against it."
                )
            else:
                lines.append(
                    f"- [`{r['resource']}`]({page_path(r)}): set `{payload['selector_field']}` to a type code below "
                    f"and send its properties in `{payload['payload_field']}`."
                )
    else:
        lines.append(
            "- These schemas describe JSON fields of the web forms (additional fields, repository links, "
            "specifications). The REST API returns the stored JSON as is."
        )
    lines.append(
        f"- Every version is published at `{SERVER}/schemas/{name}/<Type>/<version>.json` and never changes; "
        f"`{SERVER}/schemas/{name}/<Type>.json` is the current version and `{SERVER}/schemas/{name}/<Type>/` "
        "lists the versions. See [Public schemas](/api/public-schemas/)."
    )
    lines.append(
        "- Quantities are objects `{\"value\": <number>, \"unit\": \"<code>\"}`. Property paths with `[]` are "
        "inside a repeatable list of rows. The server sets the schema version field itself."
    )
    lines.append("")
    lines.append("## Quick type map")
    lines.append("")
    has_groups = any(t.get("group") for t in family["types"])
    header = "| Type code | Title |" + (" Group |" if has_groups else "") + " Version | Required properties | Schema |"
    sep = "|:----------|:------|" + (":------|" if has_groups else "") + ":--------|:--------------------|:-------|"
    lines.append(header)
    lines.append(sep)
    for t in family["types"]:
        required = ", ".join(code(r) for r in t["required"]) or "none"
        flags = []
        if t.get("legacy"):
            flags.append("legacy")
        if t.get("unregistered"):
            flags.append("form only")
        title = t.get("label") or t["title"]
        if flags:
            title += f" ({', '.join(flags)})"
        row = f"| [`{t['type']}`](#{type_anchor(t)}) | {md_cell(title)} |"
        if has_groups:
            row += f" {md_cell(t.get('group') or '')} |"
        row += f" {t['schema_version']} | {required} | [{t['schema_version']}.json]({SERVER}{t['url']}) |"
        lines.append(row)
    lines.append("")
    for group, types in grouped_types(family):
        if group:
            lines.append(f"## {group}")
            lines.append("")
        for t in types:
            lines += render_type_api(t, family, ctx)
    return "\n".join(lines)


def property_description(p: dict) -> str:
    """The Description cell of the two-column property table on API resource pages."""
    text = shape_text(p) + (" **[required]**" if p["required"] else "")
    if p.get("title") and p["title"].lower() != p["path"].rsplit(".", 1)[-1].lower():
        text = f"{p['title']}: {text}"
    allowed = allowed_values_api(p)
    if allowed:
        text += "; " + allowed
    if p.get("description"):
        text += ". " + p["description"]
    return md_cell(text)


def render_type_api(t: dict, family: dict, ctx: dict, level: str | None = None, compact: bool = False) -> list[str]:
    """``compact``: a two-column property table, for the JSON field schemas of an API resource page."""
    label = t.get("label") or t["title"]
    heading = level or ("###" if t.get("group") else "##")
    lines = [f"{heading} {label}", ""]
    meta = [f"type code `{t['type']}`", f"version {t['schema_version']}", f"[schema]({SERVER}{t['url']})"]
    if t.get("legacy"):
        meta.append("legacy: readable on old records, not selectable for new ones")
    lines.append("- " + " · ".join(meta))
    if t.get("description"):
        lines.append("")
        lines.append(t["description"])
    lines.append("")
    if t["properties"] and compact:
        lines.append("| Property | Description |")
        lines.append("|:---------|:------------|")
        for p in t["properties"]:
            lines.append(f"| `{p['path']}` | {property_description(p)} |")
    elif t["properties"]:
        lines.append("| Property | Title | Shape | Required | Allowed values | Meaning |")
        lines.append("|:---------|:------|:------|:---------|:---------------|:--------|")
        for p in t["properties"]:
            lines.append(
                f"| `{p['path']}` | {md_cell(p['title'])} | {shape_text(p)} | {'yes' if p['required'] else ''} | "
                f"{md_cell(allowed_values_api(p))} | {md_cell(p.get('description', ''))} |"
            )
    else:
        lines.append(
            "This type has no type-specific properties: send an empty object. Everything meaningful is recorded on "
            "the record itself or on its material usage rows."
        )
    lines.append("")
    payload = example_payload(t)
    if payload:
        lines.append("Illustrative payload:")
        lines.append("")
        lines.append(json_block(payload))
        lines.append("")
    for related in t.get("related_types", []):
        fam = related["family"]
        if related["types"]:
            target_family = ctx["families"].get(fam, {})
            links = []
            for code_ in related["types"]:
                entry = next((x for x in target_family.get("types", []) if x["type"] == code_), None)
                anchor = type_anchor(entry) if entry else code_.lower().replace("_", "-")
                links.append(f"[`{code_}`](/api/schemas/{fam.lower()}/#{anchor})")
            links = ", ".join(links)
        else:
            links = "none"
        rule = "other values are refused (400)" if related.get("enforced") else "the web form offers only these"
        lines.append(f"- `{related['field']}` accepts {fam} types: {links}; {rule}.")
    if t.get("unused_form_fields"):
        lines.append(
            "- Fields hidden by the web form for this type (leave empty): "
            + ", ".join(code(f) for f in t["unused_form_fields"]) + "."
        )
    policy = t.get("material_policy")
    if policy and policy.get("materials"):
        lines.append("")
        lines.append("Materials (material usage rows) allowed on this type:")
        lines.append("")
        lines.append("| Role (`type`) | Required | Max | From stock types | From catalog types | Manual | Complete when |")
        lines.append("|:--------------|:---------|:----|:-----------------|:-------------------|:-------|:--------------|")
        for m in policy["materials"]:
            stock = ", ".join(code(s["code"]) for s in m.get("stock_types", [])) or ""
            catalog = ", ".join(code(s["code"]) for s in m.get("catalog_types", [])) or ""
            lines.append(
                f"| `{m['code']}` ({md_cell(m['title'])}) | {'yes' if m['required'] else ''} | "
                f"{m['max_items'] if m.get('max_items') else ''} | {stock} | {catalog} | "
                f"{'yes' if m.get('manual_source') else ''} | {md_cell(', '.join(m.get('completion', [])))} |"
            )
        if policy.get("stages"):
            lines.append("")
            lines.append("Stages:")
            lines.append("")
            for s in policy["stages"]:
                detail = s.get("details_schema") or s.get("schema")
                detail_text = f", details schema `{detail}`" if detail else ", no detail schema"
                rep = "; repeatable" if s.get("repeatable") else ""
                lines.append(f"- `{s['code']}` ({s.get('title') or s['code']}){detail_text}{rep}")
    lines.append("")
    return lines


def render_schema_family_human(family: dict, ctx: dict) -> str:
    name = family["family"]
    label = FAMILY_HUMAN_TITLES.get(name, f"{name} types")
    lines = [f"# {label}", "{: .no_toc}", ""]
    lines.append(FAMILY_INTROS.get(name, f"Type-specific fields of the {name} family."))
    lines.append("")
    if family.get("development"):
        lines.append("{: .warning }")
        lines.append("> This family is still being refined and its fields may change between releases.")
        lines.append("")
    intros = type_intros(name)[1]
    group_intros = group_descriptions(family)
    sections = grouped_types(family)
    has_groups = any(group for group, _ in sections)
    lines += ["## Table of contents", "{: .no_toc .text-delta }", ""]
    if has_groups:
        # A hand-built table of contents: each group with what it covers and its types.
        for group, types in sections:
            links = " · ".join(f"[{t.get('label') or t['title']}](#{type_anchor(t)})" for t in types)
            if group:
                about = f": {group_intros[group]}" if group_intros.get(group) else ""
                lines.append(f"- **[{group}](#{text_anchor(group)})**{about}<br>{links}")
            else:
                lines.append(f"- **Other types**<br>{links}")
        lines.append("")
    else:
        lines += ['{::options toc_levels="2..2" /}', "1. TOC", "{:toc}", ""]
    preamble = DOCS / "_preambles" / "schemas" / f"{name.lower()}.md"
    if preamble.exists():
        lines.append(preamble.read_text(encoding="utf-8").strip())
        lines.append("")
    for group, types in sections:
        if group:
            lines.append(f"## {group}")
            lines.append("")
            if group_intros.get(group):
                lines.append(group_intros[group])
                lines.append("")
        elif has_groups:
            lines.append("## Other types")
            lines.append("")
        for t in types:
            lines += render_type_human(t, family, ctx, level="###" if has_groups else None, intro=intros.get(t["type"]))
    lines.append("## API access")
    lines.append("")
    lines.append(
        f"The same types are documented for API users, with property codes, versions and payload examples, on the "
        f"[{name} schemas API page](/api/schemas/{name.lower()}/)."
    )
    return "\n".join(lines)


FAMILY_HUMAN_TITLES = {
    "Coordinates": "Coordinate systems",
    "Procedure": "Procedure types",
    "SpecimenProcedure": "Specimen procedure types",
    "SpecimenProcedureStage": "Procedure stage types",
    "MaterialUsage": "Material usage types",
    "ExperimentalInterface": "Experimental interface types",
    "DataAcquisition": "Data acquisition types",
    "Manipulation": "Manipulation types",
    "Equipment": "Equipment types",
    "HardwareDevice": "Hardware device types",
    "Consumable": "Consumable types",
    "ConsumableStock": "Consumable stock types",
    "SubjectLog": "Subject log types",
    "ProcedureLog": "Procedure log types",
    "SpecimenLog": "Specimen log types",
    "SpecimenSet": "Specimen set types",
    "Specimen": "Specimen types",
    "Project": "Project schemas",
    "Session": "Session schemas",
    "Subject": "Subject schemas",
    "Setup": "Setup schemas",
    "DataStorage": "Data storage schemas",
    "Species": "Species schemas",
    "Strain": "Strain schemas",
    "BehavioralParadigm": "Behavioral paradigm schemas",
}


def render_type_human(t: dict, family: dict, ctx: dict, level: str | None = None, intro: str | None = None) -> list[str]:
    label = t.get("label") or t["title"]
    heading = level or ("###" if t.get("group") else "##")
    lines = [f"{heading} {label}", ""]
    # The schema's own description, else the hand-written introduction (docs/_preambles/schemas/types/).
    if t.get("description") or intro:
        lines.append(t.get("description") or intro)
        lines.append("")
    if t.get("legacy"):
        lines.append("{: .note }")
        lines.append("> Legacy type: kept for existing records, not offered for new ones.")
        lines.append("")
    if t["properties"]:
        lines.append("| Field | Description |")
        lines.append("|:------|:------------|")
        for p in t["properties"]:
            desc = []
            req = "**Required.** " if p["required"] else ""
            desc.append(f"{req}{shape_text(p).capitalize()}.")
            if p.get("description"):
                desc.append(p["description"])
            allowed = allowed_values_human(p)
            if allowed:
                desc.append(allowed + ".")
            title = p["title"]
            if "[]" in p["path"]:
                parent = p["path"].split("[]")[0]
                parent_title = next((q["title"] for q in t["properties"] if q["path"] == parent), parent)
                title = f"{parent_title} › {title}"
            elif "." in p["path"]:
                parent = p["path"].rsplit(".", 1)[0]
                parent_title = next((q["title"] for q in t["properties"] if q["path"] == parent), parent)
                title = f"{parent_title} › {title}"
            lines.append(f"| `{md_cell(title)}` | {md_cell(' '.join(desc))} |")
    else:
        lines.append(
            "This type has no type-specific fields. The record's own fields and its material rows describe it."
        )
    lines.append("")
    policy = t.get("material_policy")
    if policy and policy.get("materials"):
        lines.append("Materials that can be recorded on this type:")
        lines.append("")
        lines.append("| Material role | Required | Taken from | Complete when |")
        lines.append("|:--------------|:---------|:-----------|:--------------|")
        for m in policy["materials"]:
            sources = []
            if m.get("stock_types"):
                sources.append("stock: " + ", ".join(s["label"] for s in m["stock_types"]))
            if m.get("catalog_types"):
                sources.append("catalog: " + ", ".join(s["label"] for s in m["catalog_types"]))
            if m.get("manual_source"):
                sources.append("manual entry")
            lines.append(
                f"| {md_cell(m['title'])} | {'yes' if m['required'] else ''} | {md_cell('; '.join(sources))} | "
                f"{md_cell(', '.join(m.get('completion', [])))} |"
            )
        if policy.get("stages"):
            lines.append("")
            lines.append("Stages: " + ", ".join(s.get("title") or s["code"] for s in policy["stages"]) + ".")
        lines.append("")
    for related in t.get("related_types", []):
        if related["field"] in ("coordinates_system", "coordinates") and related["types"]:
            titles = []
            coords = ctx["families"].get("Coordinates", {})
            for code_ in related["types"]:
                entry = next((x for x in coords.get("types", []) if x["type"] == code_), None)
                titles.append(entry["title"] if entry else code_)
            lines.append("Coordinate systems offered for this type: " + "; ".join(titles) + ".")
            lines.append("")
        elif related["field"] in ("interfaces",) and related["types"]:
            lines.append(
                "Experimental interface types that can be linked: " + ", ".join(related["types"]) + "."
            )
            lines.append("")
        elif related["field"] == "consumable" and related["types"]:
            lines.append("Consumable types that can be selected: " + ", ".join(related["types"]) + ".")
            lines.append("")
    return lines


def inline_types(family: dict) -> list[dict]:
    """The types of an inline family worth documenting: validation-only helpers carry no properties."""
    return [t for t in family["types"] if t["properties"] or t.get("shape") not in ("empty", None)]


def render_inline_family_api(family: dict, resource: dict, ctx: dict) -> list[str]:
    """The API flavour of an inline family, appended to its model's API resource page."""
    name = family["family"]
    lines = ["## JSON field schemas", ""]
    lines.append(
        f"{FAMILY_INTROS.get(name, '')} The REST API returns these JSON fields as stored and validates writes "
        f"against the schemas below. Every version is published at `{SERVER}/schemas/{name}/<Type>/<version>.json` "
        f"and never changes; see [Public schemas](/api/public-schemas/)."
    )
    lines.append("")
    # Each type's heading (in the table of contents) carries its code, version and schema link, so there is no
    # overview table.
    for t in inline_types(family):
        lines += render_type_api(t, family, ctx, level="###", compact=True)
    return lines


def inline_family_for(resource_name: str, ctx: dict) -> dict | None:
    for family_name, res in INLINE_FAMILIES.items():
        if res == resource_name and family_name in ctx["families"]:
            return ctx["families"][family_name]
    return None


def render_schema_index(families: list[dict], ctx: dict, for_api: bool) -> str:
    resources = ctx["resources"]
    if for_api:
        lines = ["# Schemas", "{: .no_toc}", ""]
        lines.append(
            "Some resources carry a type-specific JSON payload validated against the JSON schema of the selected "
            "type. The selector field (usually `type`) picks the type; the payload field holds its properties. "
            "If the payload does not match the schema the API returns `400 Bad request` with the validation errors."
        )
        lines.append("")
        lines.append(
            f"Every schema version is published at `{SERVER}/schemas/<Family>/<Type>/<version>.json` and never "
            "changes; see [Public schemas](/api/public-schemas/) for the URL layout and version history."
        )
        lines.append("")
        lines.append("| Family | Types | Used by (selector → payload) | Status |")
        lines.append("|:-------|:------|:-----------------------------|:-------|")
        for family in families:
            name = family["family"]
            if name in INLINE_FAMILIES:
                continue
            users = family_users(name, resources)
            used = ", ".join(
                f"[`{r['resource']}`]({page_path(r)}): `{p['selector_field']}` → `{p['payload_field']}`"
                for r, p in users
            ) or "web forms only"
            status = "experimental" if family.get("development") else "stable"
            lines.append(
                f"| [{name}](/api/schemas/{name.lower()}/) | {len(family['types'])} | {used} | {status} |"
            )
        lines.append("")
        inline_links = []
        for family in families:
            name = family["family"]
            target = ctx["by_resource"].get(INLINE_FAMILIES.get(name, ""))
            if name in INLINE_FAMILIES and target:
                inline_links.append(f"[`{target['resource']}`]({page_path(target)}#json-field-schemas)")
        if inline_links:
            lines.append(
                "Some resources also validate one of their own JSON fields (additional fields, repository links, "
                "external identifiers, specifications) against a schema that does not depend on a type. Those "
                "schemas are documented on the resource's page: " + ", ".join(inline_links) + "."
            )
            lines.append("")
        lines.append("## Validation troubleshooting")
        lines.append("")
        lines.append("- `type` not recognized: use one type code from the family's quick type map.")
        lines.append("- Missing required property: add every property listed as required for that type.")
        lines.append(
            "- Wrong shape: quantities are objects with `value` and `unit`; multi-selects are lists of codes; "
            "tables are lists of row objects."
        )
        lines.append("- Unit or option not accepted: use one of the codes listed under *Allowed values*.")
        lines.append("- Unknown property: schemas reject properties they do not declare.")
        return "\n".join(lines)
    lines = ["# Schemas", "{: .no_toc}", ""]
    lines.append(
        "Schemas define the type-specific fields of BrainSTEM's modular records. When you pick a type in a form "
        "(a procedure type, a data acquisition type, a consumable type, a coordinate system) the form shows the "
        "fields of that type's schema, and the values are validated against it. Every schema is versioned and "
        "published, so exports can cite the exact version a record was validated against."
    )
    lines.append("")
    by_name = {f["family"]: f for f in families}
    nav = family_nav_order(families)
    areas = [(title, intro, [n for n in names if n in nav]) for title, intro, names in SCHEMA_AREAS]
    rest = [n for n in nav if not any(n in names for _, _, names in SCHEMA_AREAS)]
    if rest:
        areas.append(("Other schema families", "", rest))
    for title, intro, names in areas:
        if not names:
            continue
        lines.append(f"## {title}")
        lines.append("")
        if intro:
            lines.append(intro)
            lines.append("")
        lines.append("| Schema family | Types | Where it is used |")
        lines.append("|:--------------|:------|:-----------------|")
        for name in names:
            family = by_name[name]
            users = family_users(name, resources)
            used = ", ".join(sorted({r["label"] for r, _ in users})) or FAMILY_FORM_USE.get(name, "web forms")
            lines.append(
                f"| [{FAMILY_HUMAN_TITLES.get(name, name)}](/datamodel/schemas/{name.lower()}/) | "
                f"{len(family['types'])} | {md_cell(used)} |"
            )
        lines.append("")
    lines.append("## Structured fields and relations")
    lines.append("")
    inline_pages = []
    for family in families:
        name = family["family"]
        page = ctx["datamodel_pages"].get(INLINE_FAMILIES.get(name, ""))
        if name in INLINE_FAMILIES and page:
            label = next((r["label"] for r in resources if r["resource"] == INLINE_FAMILIES[name]), name)
            inline_pages.append(f"[{label}]({page}#fields)")
    if inline_pages:
        lines.append(
            "A few records also have structured fields (additional fields, repository links, external identifiers, "
            "specifications) whose rows follow a schema that does not depend on a type. They are described in the "
            "Fields table of the record, with a link to the schema: " + ", ".join(inline_pages) + "."
        )
        lines.append("")
    lines.append(
        "The [Relations](/datamodel/schemas/relations/) page lists which types can be combined: which interface "
        "types a data acquisition type accepts, which coordinate systems a procedure type offers, and which "
        "catalog types a stock type draws from."
    )
    return "\n".join(lines)


FAMILY_FORM_USE = {
    "Project": "Project form (additional fields, repositories)",
    "Session": "Session form (additional fields, repositories)",
    "Subject": "Subject form (additional fields)",
    "Setup": "Setup form (specifications)",
    "DataStorage": "Data storage form",
    "Species": "Species form (external identifiers)",
    "Strain": "Strain form (external identifiers)",
    "BehavioralParadigm": "Behavioral paradigm form (external identifiers)",
    "SubjectLog": "Subject log entries",
    "ProcedureLog": "Procedure log entries",
    "SpecimenLog": "Specimen log entries",
    "SpecimenProcedureStage": "Procedure and specimen procedure stages",
}


def render_relations(families: list[dict], ctx: dict) -> str:
    lines = ["# Relations", "{: .no_toc}", ""]
    lines.append(
        "Relations define which items you can select in one record based on the type of another. When you choose "
        "a type, related selectors are narrowed to the choices that make sense for it. *Enforced* relations are "
        "also checked by the server; *form only* relations narrow the web form but the API accepts any value."
    )
    lines += ["", "## Table of contents", "{: .no_toc .text-delta }", "", "1. TOC", "{:toc}", ""]
    by_family = {f["family"]: f for f in families}
    sections = [
        ("DataAcquisition", "interfaces", "Data acquisition types → experimental interface types"),
        ("Manipulation", "interfaces", "Manipulation types → experimental interface types"),
        ("ConsumableStock", "consumable", "Consumable stock types → consumable (catalog) types"),
        ("Equipment", "consumable", "Equipment types → consumable types"),
        ("Procedure", "coordinates_system", "Procedure types → coordinate systems"),
        ("Equipment", "coordinates_system", "Equipment types → coordinate systems"),
    ]
    for family_name, field, title in sections:
        family = by_family.get(family_name)
        if not family:
            continue
        rows = []
        for t in family["types"]:
            for related in t.get("related_types", []):
                if related["field"] == field:
                    rows.append((t, related))
        if not rows:
            continue
        lines.append(f"## {title}")
        lines.append("")
        enforced = any(r.get("enforced") for _, r in rows)
        lines.append(f"{'Enforced by the server.' if enforced else 'Form only.'}")
        lines.append("")
        lines.append(f"| {family_name} type | Allowed {rows[0][1]['family']} types |")
        lines.append("|:-----|:-----|")
        for t, related in rows:
            target_family = by_family.get(related["family"], {})
            titles = []
            for code_ in related["types"]:
                entry = next((x for x in target_family.get("types", []) if x["type"] == code_), None)
                titles.append(entry.get("label") or entry["title"] if entry else code_)
            lines.append(f"| {md_cell(t.get('label') or t['title'])} | {md_cell(', '.join(titles) or 'none')} |")
        lines.append("")
    return "\n".join(lines)


def render_relationships(relationships: dict, ctx: dict) -> str:
    by_resource = ctx["by_resource"]
    lines = ["# Relationships", "{: .no_toc}", ""]
    lines.append(
        "How resources connect, as the queries that follow each link. A *forward* step reads ids on the record "
        "you already have; a *reverse* step asks the next resource for records pointing back. Collect ids, "
        "de-duplicate them and pass them on with `filter{<field>.in}`."
    )
    lines += ["", "## Table of contents", "{: .no_toc .text-delta }", "", "1. TOC", "{:toc}", ""]
    lines.append("## Single-hop routes")
    lines.append("")
    lines.append("| From → to | How |")
    lines.append("|:----------|:----|")
    for name, hops in relationships["routes"].items():
        if len(hops) != 1:
            continue
        src, dst = name.split(">")
        hop = hops[0]
        if src not in by_resource or dst not in by_resource:
            continue
        if hop["direction"] == "reverse":
            target = by_resource[hop["resource"]]
            how = f"`GET {target['paths'].get('private') or target['paths'].get('public')}?filter{{{hop['field']}.in}}=<ids>`"
        else:
            many = any(
                f["name"] == hop["field"] and f["kind"] == "relation_many" for f in by_resource[src]["fields"]
            )
            how = f"read `{hop['field']}` on each `{src}` record ({'list of ids' if many else 'one id'})"
        lines.append(f"| [`{src}`]({page_path(by_resource[src])}) → [`{dst}`]({page_path(by_resource[dst])}) | {how} |")
    lines.append("")
    multi = {k: v for k, v in relationships["routes"].items() if len(v) > 1}
    if multi:
        lines.append("## Multi-hop routes")
        lines.append("")
        for name, hops in multi.items():
            src, dst = name.split(">")
            steps = " → ".join(f"`{h['resource']}.{h['field']}` ({h['direction']})" for h in hops)
            lines.append(f"- **{src} → {dst}**: {steps}")
        lines.append("")
    if relationships.get("unions"):
        lines.append("## Questions with several branches")
        lines.append("")
        for name, union in relationships["unions"].items():
            src, dst = name.split(">")
            lines.append(f"### {src} → {dst}")
            lines.append("{: .no_toc}")
            lines.append("")
            if union.get("note"):
                lines.append(union["note"])
                lines.append("")
            for branch in union.get("branches", []):
                lines.append("- " + " → ".join(f"`{step}`" for step in branch))
            lines.append("")
    lines.append("## Delete behaviour")
    lines.append("")
    lines.append(
        "What happens to a record when a record it points to is deleted: *cascade* deletes it too, *protect* "
        "refuses the deletion while it exists, *set null* clears the link."
    )
    lines.append("")
    lines.append("| Record | Field | Points to | On delete |")
    lines.append("|:-------|:------|:----------|:----------|")
    for edge in relationships["edges"]:
        if not edge.get("on_delete"):
            continue
        if edge["source"] not in by_resource or edge["target"] not in by_resource:
            continue
        lines.append(
            f"| [`{edge['source']}`]({page_path(by_resource[edge['source']])}) | `{edge['field']}` | "
            f"[`{edge['target']}`]({page_path(by_resource[edge['target']])}) | "
            f"{edge['on_delete'].replace('_', ' ').lower()} |"
        )
    return "\n".join(lines)


# --------------------------------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------------------------------


def datamodel_pages() -> dict[str, str]:
    """Map resource name → URL of its hand-written data model page, when one exists."""
    pages = {}
    for path in (DOCS / "datamodel").rglob("*.md"):
        if path.parent.name == "schemas" or path.name in ("schemas.md",):
            continue
        name = path.stem.lower()
        rel = path.relative_to(DOCS).with_suffix("")
        pages[name] = "/" + str(rel) + "/"
    # Historical page names that differ from the resource name.
    aliases = {"anatomicalregion": "brainregion"}
    for resource, page in aliases.items():
        if page in pages and resource not in pages:
            pages[resource] = pages[page]
    return pages


def main():
    global DOCS
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--reference", help="directory holding the exported reference documents (*.json)")
    source.add_argument("--brainstem", help="BrainSTEM repository to export the reference from")
    source.add_argument("--server", default=SERVER, help="server to fetch /reference/data/*.json from")
    parser.add_argument("--docs", default=str(DOCS), help="docs directory of the support site")
    parser.add_argument("--clean", action="store_true", help="remove generated pages that no longer have a source")
    assets = parser.add_mutually_exclusive_group()
    assets.add_argument("--no-assets", action="store_true",
                        help="do not refresh the interactive data model under docs/assets/datamodel/")
    assets.add_argument("--assets-only", action="store_true",
                        help="only fetch the interactive data model (fails if the server does not publish it)")
    args = parser.parse_args()

    DOCS = Path(args.docs)
    if args.assets_only:
        try:
            documents, source = load_reference(args, ("manifest",))
        except urllib.error.URLError as error:
            raise SystemExit(f"{args.server}/reference/ is not available ({error}); the interactive data model "
                             "can only be fetched from a server that publishes it") from None
        copy_datamodel_assets(source, documents["manifest"], DOCS / "assets" / "datamodel", required=True)
        source.close()
        return
    documents, source = load_reference(args)
    surface = documents["api_surface"]
    schemas = documents["schemas"]
    relationships = documents["relationships"]
    summaries = documents["model_summaries"]
    commit = documents["manifest"].get("server_commit", "")

    resources = surface["resources"]
    by_model = {r["model"]: r for r in resources}
    by_resource = {r["resource"]: r for r in resources}
    families = schemas["families"]
    # The reference says which families are field schemas; the dictionary only maps them to their resource.
    if any("selects_type" in f for f in families):
        for family in families:
            if family.get("selects_type") is False and family["family"] not in INLINE_FAMILIES:
                INLINE_FAMILIES[family["family"]] = family["family"].lower()
        for name in [n for n in INLINE_FAMILIES if any(f["family"] == n and f.get("selects_type") for f in families)]:
            del INLINE_FAMILIES[name]
    ctx = {
        "resources": resources,
        "by_model": by_model,
        "by_resource": by_resource,
        "edges": relationships["edges"],
        "summaries": {k.lower(): v for k, v in summaries.items()} | summaries,
        "schema_families": {f["family"]: f for f in families},
        "families": {f["family"]: f for f in families},
        "datamodel_pages": datamodel_pages(),
    }

    written = []

    # API resource pages and app indexes.
    grouped: dict[str, list[dict]] = {}
    for app_index, app in enumerate(APP_ORDER, start=1):
        app_resources = resource_order(app, [r for r in resources if r["app"] == app])
        if not app_resources:
            continue
        index_path = DOCS / "api" / f"{app}.md"
        write_page(
            index_path,
            {"layout": "default", "title": APP_TITLES[app], "parent": "API", "has_children": "true",
             "nav_order": app_index, "has_toc": "false"},
            render_app_index(app, app_resources, ctx),
            commit,
        )
        written.append(index_path)
        order = 0
        for resource in app_resources:
            path = DOCS / "api" / app / f"{slug(resource['resource'])}.md"
            group = nav_group(resource["resource"])
            if group:
                grouped.setdefault(group["key"], []).append(resource)
                front = {"layout": "default", "title": resource["label"], "parent": group["title"],
                         "grand_parent": "API", "nav_order": len(grouped[group["key"]])}
            else:
                order += 1
                front = {"layout": "default", "title": resource["label"], "parent": APP_TITLES[app],
                         "grand_parent": "API", "nav_order": order}
            write_page(path, front, render_resource_page(resource, ctx), commit)
            written.append(path)
    for group in NAV_GROUPS:
        members = grouped.get(group["key"], [])
        if not members:
            continue
        index_path = DOCS / "api" / f"{group['key']}.md"
        write_page(
            index_path,
            {"layout": "default", "title": group["title"], "parent": "API", "has_children": "true",
             "nav_order": group["nav_order"], "has_toc": "false"},
            render_group_index(group, members, ctx),
            commit,
        )
        written.append(index_path)

    # Schema pages (API and data model flavours).
    api_schemas_index = DOCS / "api" / "schemas.md"
    write_page(
        api_schemas_index,
        {"layout": "default", "title": "Schemas", "parent": "API", "nav_order": 20, "has_children": "true",
         "has_toc": "false"},
        render_schema_index(families, ctx, for_api=True),
        commit,
    )
    written.append(api_schemas_index)
    dm_schemas_index = DOCS / "datamodel" / "schemas.md"
    write_page(
        dm_schemas_index,
        {"layout": "default", "title": "Schemas", "parent": "Data model", "has_children": "true", "nav_order": 14,
         "has_toc": "false"},
        render_schema_index(families, ctx, for_api=False),
        commit,
    )
    written.append(dm_schemas_index)
    nav = family_nav_order(families)
    for family in families:
        name = family["family"]
        if name in INLINE_FAMILIES:
            continue
        order = nav.index(name) + 1
        api_path = DOCS / "api" / "schemas" / f"{name.lower()}.md"
        write_page(
            api_path,
            {"layout": "default", "title": name, "parent": "Schemas", "grand_parent": "API", "nav_order": order},
            render_schema_family_api(family, ctx),
            commit,
        )
        written.append(api_path)
        dm_path = DOCS / "datamodel" / "schemas" / f"{name.lower()}.md"
        write_page(
            dm_path,
            {"layout": "default", "title": FAMILY_HUMAN_TITLES.get(name, name), "parent": "Schemas",
             "grand_parent": "Data model", "nav_order": order},
            render_schema_family_human(family, ctx),
            commit,
        )
        written.append(dm_path)
    relations_path = DOCS / "datamodel" / "schemas" / "relations.md"
    write_page(
        relations_path,
        {"layout": "default", "title": "Relations", "parent": "Schemas", "grand_parent": "Data model",
         "nav_order": len(families) + 1},
        render_relations(families, ctx),
        commit,
    )
    written.append(relations_path)
    relationships_path = DOCS / "api" / "relationships.md"
    write_page(
        relationships_path,
        {"layout": "default", "title": "Relationships", "parent": "API", "nav_order": 21},
        render_relationships(relationships, ctx),
        commit,
    )
    written.append(relationships_path)

    if args.clean:
        generated_dirs = [DOCS / "api" / app for app in APP_ORDER] + [
            DOCS / "api" / "schemas", DOCS / "datamodel" / "schemas", DOCS / "_includes" / "schemas",
        ]
        for directory in generated_dirs:
            if not directory.exists():
                continue
            for path in directory.glob("*.md"):
                if path not in written and START in path.read_text(encoding="utf-8"):
                    path.unlink()
                    print(f"removed stale {path.relative_to(DOCS)}")
    print(f"wrote {len(written)} pages (server {commit[:12] or 'unknown'})")
    if not args.no_assets:
        copy_datamodel_assets(source, documents["manifest"], DOCS / "assets" / "datamodel")
    source.close()


if __name__ == "__main__":
    main()
