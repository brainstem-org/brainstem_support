# Authoring guide for the BrainSTEM support site

This guide says what each kind of page on support.brainstem.org must contain, which pages are generated and
which are written by hand, and how the site is kept in step with the BrainSTEM server. Read it before adding
or changing a page. It follows the same standard as BrainSTEM's own help modals
(`docs/AGENTS/help-modal-review-and-authoring.md` in the BrainSTEM repository): a page describes what the
software does, verified against the implementation, in the user's vocabulary.

## Principles

- **Describe what the software does.** Every claim is verified against the server's generated reference
  (`/reference/`), the schemas (`/schemas/`) or the BrainSTEM code. When the implementation and the intended
  behaviour disagree, do not document the intention as fact: describe what reliably holds and report the
  discrepancy to the BrainSTEM team.
- **Generate what can be generated.** Field lists, choices, permissions, endpoints, schema types and their
  properties change with every release. They are rendered from the server's reference documents by
  `scripts/build_reference_docs.py`, never typed by hand. Hand-written pages carry the explanations a
  generator cannot write: what a record is for, how to choose between neighbours, workflows, consequences.
- **User vocabulary.** Say "entry", "procedure", "specimen set"; keep "model", "record", "foreign key" and
  "JSON object" for the API pages. Quote user-facing labels exactly, in bold.
- **Short sentences, scannable structure.** One idea per sentence. Headings that name the task or the concept.
  Tables for options and fields, lists for steps. Callouts (`{: .note }`, `{: .important }`, `{: .warning }`)
  only for consequences the reader must not miss.
- **Link, do not repeat.** Each fact lives on one page; other pages link to it. A data-model page links to its
  API page and schema page; a tutorial links to the data-model pages of the records it creates.
- **No invented numbers or screenshots.** Counts ("366 probe designs") are stated "at the time of writing".
  Reference only images that exist under `docs/assets/images/`. Screenshots are produced by
  `scripts/screenshots.py` from the demo dataset (see *Screenshots and illustrations* below), never pasted by hand.
- **Nothing administrative.** Admin groups, the super-user portal, admin-only exports and other administrative
  surfaces are not documented on the public site. The server's reference leaves them out (whatever the
  interactive diagram hides is absent from `/reference/`), so the generator has nothing to filter; hand-written
  pages describe only what a user sees, such as "your institution can require two-factor sign-in".

## Page kinds and their contract

### Data model pages (`docs/datamodel/<app>/<model>.md`, hand-written)

Audience: a researcher deciding what to record where. Required sections, in this order:

1. **Front matter**: `title` (plural, e.g. "Subjects"), `parent` / `grand_parent`, `nav_order`.
2. **Introduction**: what one entry represents, what it is *not* (the neighbouring concepts it is confused with),
   how it relates to its parent and children, with links. Two to four short paragraphs.
3. **Diagram**: `{% include datamodel_embed.html model="<app>.<model>" %}` right after the introduction. It
   embeds the interactive data model focused on this model with its direct connections, as the Graph tab of
   BrainSTEM's help dialogs does. The model id is the node id of `docs/assets/datamodel/graph.json`.
4. **Fields**: a table of every user-facing field of the add and change forms, labelled as the form labels
   them, with **required** marked, the type or limits, the choices with their meanings, and an example. Not the
   bookkeeping fields (ids, timestamps, schema versions).
5. **JSON fields with a schema** (a schema that does not depend on a type: project, session, subject, setup,
   data storage, species, strain, behavioral paradigm): no section of their own. The field's row in the Fields
   table says what each entry holds (its parts, which are required, the choices) and ends with a link to the
   latest schema, `[Schema](https://www.brainstem.org/schemas/<Family>/<Type>.json)`. These families get no
   schema page; the API flavour is appended to the model's API page under "JSON field schemas".
6. **Types** (typed models only): the groups and types in dropdown order, linking to the schema page for the
   type-specific fields; what lifecycle consequence a type has (for example "creates an experimental interface").
7. **Model-specific sections**: lifecycle and status, materials and stages, templates, automatic behaviour,
   what becomes immutable, delete behaviour.
8. **Permissions**: the real anchor the entry inherits from, in one or two sentences, linking to the permissions page.
9. **API access**: one sentence linking to the generated API page.

Sources of truth: the generated reference page of the resource (`/reference/resources/<resource>.md`), the model
summary, and the BrainSTEM forms. When fields change on the server, the generated API page changes automatically;
the hand-written Fields table must be updated in the same pull request (the sync workflow's description reminds you).

### Schema pages (`docs/datamodel/schemas/<family>.md` and `docs/api/schemas/<family>.md`, generated)

One page per type-dependent schema family in each section (procedures, interfaces, data acquisition, materials,
logs, equipment, consumables, coordinates and so on). The data-model flavour lists every type with its fields as
the form labels them (title, kind, options with their labels, units) and the materials and stages the type takes.
The API flavour lists the type codes, versions, published schema URLs, property paths with codes, allowed related
types, material policies and an illustrative payload. Both are rendered from `data/schemas.json`.

Families with a single schema, or whose schemas do not depend on a type (`selects_type: false` in the reference;
`INLINE_FAMILIES` in the script for older servers), get no page: the model page describes them in its hand-written Fields table with a link to the latest
schema, and their API flavour is appended to the model's API resource page.

Hand-written introductions go in `docs/_preambles/schemas/<family>.md` (inserted after the table of contents of
the data-model flavour; the coordinate-system conventions live there). The introductions of the type groups and of the
types themselves go in `docs/_preambles/schemas/types/<family>.md`, one `## group: <group name>` or `## <TypeCode>`
section each. A type's own schema description, when the schema has one, takes precedence. Those files are the
stopgap until the descriptions live in BrainSTEM's schemas and type registry, so move a text there when you can
and delete it here. On families with groups, the table of contents is built from the same file: each group with
its introduction and its types. The Schemas page and the side menu order the families by area (`SCHEMA_AREAS` in
the script). Anything else typed into a generated page
is lost at the next run unless it is outside the `<!-- generated:start -->` / `<!-- generated:end -->` markers.

### API endpoint pages (`docs/api/<app>/<resource>.md`, generated)

One page per REST resource, rendered from `data/api_surface.json` and `data/relationships.json`: description and
model summary; endpoints per portal, response keys, permission chain, uniqueness, schema payload fields, delete
behaviour, form-only inputs; the field table (type, write mode, required, notes, choices); list, add, detail,
change and delete sections with Python and MATLAB examples and example JSON; custom actions; a link to the
data-model page. The app index pages (`docs/api/<app>.md`) are generated too; their introductions are the
`APP_INTROS` dictionary in the script. Templates, approvals, invitations and requests, and link tables leave
their app in the side menu and sit under the generated group pages `docs/api/{templates,approvals,invitations,links}.md`
(`NAV_GROUPS` in the script); their URLs stay under `docs/api/<app>/`.

Hand-written API pages (`docs/api.md`, `export.md`, `public-schemas.md`, `reference.md`, `mcp.md`) explain the
cross-cutting mechanics: authentication, query syntax, writing rules, errors, rate limits, exports, schema
versioning, the agent reference and the MCP server. Verify them against `/reference/guides/*.md` and
`/reference/query-syntax.md` at each release.

### Feature pages (`docs/webinterface/*.md`, hand-written)

Audience: a user at the screen. Each page covers one surface or feature and answers: where it is (menu, button,
URL), what it does, every option with its exact label, the rules a user runs into (limits, validation, what
persists), and what happens next. Structure: short introduction, table of contents, one H2 per task or control
group, tables for options, a "Related" list at the end. Keep implementation detail out; name no files or classes.

The four everyday screens (dashboard, forms, list view, single entry view) sit directly under *Web interface*;
every other page belongs to one of the groups *Import and export*, *Account and security*, *Assistants and
references* or *Managing entries* (`parent: <group>`, `grand_parent: Web interface`). A new page joins the group
that matches its task, or a new group when none fits; the group page lists its children in one line each.

### Tutorials (`docs/tutorials/*.md`, hand-written)

Audience: a user following along. A tutorial has a goal stated in the first paragraph, prerequisites, numbered
steps with the exact labels to click and values to enter, callouts for consequences, and "Next steps" linking to
the data-model and feature pages. A tutorial never duplicates a field reference; it links to it.

### Tool pages (`docs/tools/*.md`, hand-written)

One page per tool (Python, MATLAB, web API tool, agent skills, NWB converter, NWB extension): what it is for,
version and server requirements, installation, authentication, the operations with short verbatim examples from
the tool's README, errors, troubleshooting, related pages. Verify against the tool repository's README and
CHANGELOG; copy signatures exactly.

### Home and section indexes

`docs/index.md` and the section indexes (`datamodel.md`, `webinterface.md`, `api.md`, `tools.md`,
`tutorials.md`) list their children with one line each and nothing that is explained on a child page.

## Screenshots and illustrations

A page asks for a screenshot with an HTML comment on its own line, `<!-- screenshot: <slug> | <what to capture> -->`;
`scripts/screenshots.py` lists one capture target per slug (page, clicks, dialog) and writes
`docs/assets/images/screenshots/<slug>.png` from a BrainSTEM instance that holds the demo dataset
(`manage.py generate_demo_project --user-email <demo user>`), logged in as that user. The pages then embed the
image as `![caption]({{site.baseurl}}/assets/images/screenshots/<slug>.png)` followed by `{: .screenshot }` and
the caption in italics. Rerun the script after a release so every picture shows the current interface; add a
target to `TARGETS` (or an alias in `ALIASES`) for every new slug. It needs Playwright, the server URL and the
demo credentials in the environment (`BRAINSTEM_URL`, `BRAINSTEM_SCREENSHOT_USER`, `BRAINSTEM_SCREENSHOT_PASSWORD`,
and `BRAINSTEM_CHECKOUT` when the demo user has two-factor authentication).

Several states of one control go in a slide strip, `{% include slides.html slides="slug|caption;;slug|caption" %}`
(the list view's dialogs, the materials editor, planning). Sequences a reader follows go in a walkthrough,
`{% include walkthrough.html slug="..." caption="..." %}`: a short silent WebM loop recorded by the same script
(`WALKTHROUGHS` in `scripts/screenshots.py`; `python scripts/screenshots.py walkthroughs` re-records them), kept to
one step of a tutorial each, next to a still for readers who skim.

The landing page shows each key feature in the web interface, `{% include tour.html %}` above the feature list:
one short clip per feature (complete records, collaboration and compliance, shared resources, open science,
programmable and AI ready, integrations). The feature list right after the include, marked `{: .tour-features }`,
is the only chapter navigation: clicking a feature plays its clip, and the playing one's number is filled in. The
tour opens neutrally on a welcome card about BrainSTEM as a whole (`TOUR_INTRO`, written to `intro` in
`docs/_data/tour.yml`) and goes straight into the first feature; the interactive data model is too detailed for the
tour and stays on the data model pages. A chapter opens on a title card (number, title and the chapter's one-line `text`), and every later shot on a card naming
it (its caption), each shown long enough to read and faded slowly in and out; the player then plays the chapter and
waits at its end for the arrow (Back and Replay too). The progress bar has a segment per shot and the caption under
the video follows the shots. So a chapter tells one story, each shot leading to the next (a procedure filled in, then
its coordinates in the atlas), and captions say what a shot means, not what the pointer does. A chapter is two or three shots, one idea each, and shows the
interface being used rather than still pages: a pointer glides to every control it uses and ripples where it clicks,
data is entered one field at a time (`type`, `pick`, `select2`), lists open as they would for a reader, and the
camera glides (`move`) to the next part of the same page instead of cutting. A shot opens already framed on what it
is about (a `frame` step; never zoom in from the whole page), and changing page crossfades. Across, the camera
widens to the whole card, panel, dialog or table around the target, so the screen's edges never cut through a
neighbouring field. A `mark` outlines one element at a time with a short tag beside it (above, below, beside a table
cell or inside a wide form row), never over it, and replaces the previous mark. The captions are not drawn into the
clips: each `frame` (or captioned `move`) sentence becomes a timed cue in `docs/_data/tour.yml`; keep them to one
short line. The recording only shows: the browser refuses every request that would change a record (forms autosave
as fields change), and a Select2 list is closed with Escape only where its highlighted option is the current value,
since closing picks it. The clips are recorded from Chrome's screencast at a 1200 by 750 viewport, twice the pixel
density and the navigation sidebar collapsed, and scaled to 1280 pixels wide, not with Playwright's video recorder,
which is too lossy for zoomed text. `TOUR` in `scripts/screenshots.py` defines the chapters;
`python scripts/screenshots.py tour` records them to `docs/assets/images/walkthroughs/tour/` (a clip and a poster
each) and writes the chapter list with its cues to `docs/_data/tour.yml`, and
`python scripts/screenshots.py tour:programmable` re-records one chapter. Keep the chapters in the order of the
feature list on `docs/index.md`. Cutting the clips needs an ffmpeg with VP8; the script finds Playwright's own when
there is none on the path. The assistant shot stops before the search on servers whose assistant cannot answer yet;
the search steps are in the chapter as a comment.

Drawings are generated, never edited by hand:

- `scripts/render_diagrams.py` draws the conceptual figures in `docs/assets/images/diagrams/` (the material
  chain, procedure → interface → session, specimen lineage, templates, stages, the epoch timeline, the two
  session kinds, the data-model overview, the landing-page picture, the behavior and setup tracks, the setup
  hub (where setups and equipment are used) and the parts of a session (behavior, data acquisition, manipulation and
  epochs); the last three are drawn once per page that shows them, with that page's model solid), and the reader aids: where to record what, the planning states, the public-sharing scope, the
  setup type categories and the export-to-NWB pipeline. Edit the figure's function and rerun it,
  for example `python scripts/render_diagrams.py session-kinds`.
- `scripts/render_example_figure.py` draws the worked example on the data model page (`data-model-example.svg`,
  one ephys session in a rat as table cards).

A page shows a drawing as an image linked to itself, so a click opens it full screen:
`[![<alt text>]({{site.baseurl}}/assets/images/diagrams/<name>.svg)]({{site.baseurl}}/assets/images/diagrams/<name>.svg)`.

Both take their colours from `scripts/diagram_style.py`, which copies the app colours of the interactive data
model (the `--dm-group-*` tokens of `data-model-diagram.css`): STEM data purple, Modules teal, Personal
attributes blue, Resources brown, Taxonomies olive, Dissemination rose, Users indigo. A model has its app's colour
in every drawing. The data-model overview draws every model solid, as the interactive view does; the other
drawings draw their main records solid and supporting models as a faint tint with a coloured outline. When
BrainSTEM changes an app colour, change it in `diagram_style.py` and rerun both scripts.

## Generated content and how it stays current

| Content | Source on the server | Script | Output |
|---|---|---|---|
| API resource pages, app indexes | `/reference/data/api_surface.json`, `relationships.json`, `model_summaries.json` | `scripts/build_reference_docs.py` | `docs/api/<app>/*.md`, `docs/api/<app>.md`, `docs/api/relationships.md` |
| Schema pages, both flavours, relations | `/reference/data/schemas.json` | `scripts/build_reference_docs.py` | `docs/api/schemas/*.md`, `docs/datamodel/schemas/*.md` |
| Interactive data model | `/reference/data/datamodel_graph.json`, `datamodel_types.json` and the per-type files, `/reference/renderer/*` | `scripts/build_reference_docs.py` (same run; `--no-assets` skips it, `--assets-only` does only this) | `docs/assets/datamodel/` (`graph.json`, `types/`, `vendor/`), ignored by git and fetched by `.github/workflows/pages.yml` at every build |

The interactive data model is shown on the data model page and the permissions page through
`docs/_includes/datamodel_switch.html`: an *Overview* view and an *Interactive* view. The Overview is the diagram
itself without its tools (`explorer.html?toolbar=0`, the renderer's `toolbar: false`, fitted whole and sized to
its content), unless the include is
given an `image`: the data model page shows `data-model-overview.svg`, drawn by `scripts/render_diagrams.py`,
which must be updated when models are added or move between apps. The Interactive view is the full explorer (the explorer, with
`query="view=permissions"` on the permissions page), with Expand and full-screen controls above the view. It is
also on every model page
through `datamodel_embed.html` (`explorer.html?embed=1&compact=1&focus=<app>.<model>`; the explorer mounts previews with
`minFitScale: 0.45` and sizes the frame from the renderer's `onFit` report). Every embed has an **Expand**
button that opens the model with its neighbours isolated in a page overlay (`datamodel_overlay.html`), and a
**Full model** button that opens the whole model there, focused on the model. `explorer.html` loads
Bootstrap 5.3.8 from cdnjs, the version BrainSTEM bundles, because the diagram's tooltips are Bootstrap tooltips;
raise that version when BrainSTEM does. It accepts the same view parameters as BrainSTEM's own data model page (`focus`, `field`, `view`, `permissions`, `layout`,
`show`, `isolate`, `depth`, `path`, `expand`).

Commands:

```bash
# from the production server (what the GitHub Actions workflow runs weekly)
python scripts/build_reference_docs.py --server https://www.brainstem.org --clean

# from a BrainSTEM checkout, before a release that is not deployed yet
/path/to/brainstem/.venv/bin/python manage.py export_agent_reference --out /tmp/reference   # in the checkout
python scripts/build_reference_docs.py --reference /tmp/reference --clean
# (or --brainstem /path/to/brainstem to run that export for you)
```

The workflow `.github/workflows/sync-reference.yml` regenerates the pages from the production server every
Monday and on demand, and opens a pull request when anything changed. Review the diff: it shows exactly which
fields, choices, types and versions moved, and therefore which hand-written pages need the same change. The
server's `data/manifest.json` carries `format_version`, `data_model` and `server_commit`; the generated pages
record the commit in their marker comment.

The interactive data model is not committed. BrainSTEM's schemas and renderer code stay out of this MIT-licensed
repository, so the copy is never stale. `.github/workflows/pages.yml` builds and deploys the site on every
push to `main` and daily, and first runs `build_reference_docs.py --assets-only` against the server in the
repository variable `BRAINSTEM_SERVER` (default production). That step needs reference format 1.2 (the `datamodel` section of
`manifest.json`) and fails the deploy, leaving the live site as it was, when the server does not publish it. The
server allows 600 requests a minute to `/reference/` (its own throttle scope), so the fetch takes about a minute;
when throttled, the generator waits as long as the server's `Retry-After` header says. Locally, run the same command (or `--brainstem` /
`--reference`) before `jekyll serve`.

## Release checklist

1. Export the reference from the release candidate (`--brainstem`) or the deployed server (`--server`) and
   regenerate; commit the generated pages.
2. Merge the documentation only once the release is deployed: the Pages build fetches the interactive data
   model from production. Redraw `data-model-overview.svg` (`scripts/render_diagrams.py`) if core models changed.
3. Walk the server's `rules.md`, `guides/*.md` and the release notes for changed behaviour; update the
   hand-written API, data-model, feature and tutorial pages that describe it.
4. Compare each data-model Fields table with its generated API page (same field set, same requirements).
5. Build the site locally (`cd docs && bundle exec jekyll build`) and check for broken internal links.
6. Update the tool pages from the tools' CHANGELOGs.

## Review checklist for a page

- [ ] The page kind's required sections are present and in order.
- [ ] Every label, field, choice, limit and route was verified against the reference or the code.
- [ ] Nothing described is only intended behaviour.
- [ ] Terminology is the user's; database vocabulary stays on API pages.
- [ ] Each fact lives on one page; others link to it.
- [ ] Links resolve to pages that exist on this branch.
- [ ] Generated pages were not edited inside their markers.
