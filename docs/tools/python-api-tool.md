---
layout: default
title: Python API tool
parent: Tools
nav_order: 2
---
# Python API tool
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Overview

The BrainSTEM Python API tool (`brainstem_python_api_tools`, import name `brainstem_api_tools`) is a thin client for the [REST API](/api/). It handles sign-in, paging and URL building, and leaves the request and response shapes exactly as the API defines them, so every [resource page](/api/stem/) applies directly. The package also installs the `brainstem` command line.

> **Repository and tutorial:** [brainstem-org/brainstem_python_api_tools](https://github.com/brainstem-org/brainstem_python_api_tools). The repository includes `brainstem_api_tutorial.ipynb` and `brainstem_api_tutorial.py` with runnable examples.

Version 2.1 addresses every resource of the current data model, including specimen sets, specimens, specimen procedures, experimental interfaces, material usages, procedure episodes, anatomical regions and templates, and adds exports, the agent reference and anonymous public reads. Those features need a BrainSTEM server of the current release; older servers answer `404` for them. Check your version with `python -c "import brainstem_api_tools; print(brainstem_api_tools.__version__)"`.

## Installation

```bash
pip install brainstem_python_api_tools
```

Python 3.8 or newer; the only dependency is `requests`.

## Authentication

BrainSTEM enforces two-factor authentication (2FA). The client signs you in through the browser, so your password is never typed into a script. See [API authentication](/api/#authentication) for the full flow.

### First run: browser sign-in
{: .no_toc}

```python
from brainstem_api_tools import BrainstemClient

client = BrainstemClient()   # opens a browser window the first time
```

If you are already logged in to BrainSTEM, click **Approve**. The token is cached at `~/.config/brainstem/token` with owner-only permissions (`0600`) and reused on later runs.

### Headless environments
{: .no_toc}

On a server or in a container without a browser:

```python
client = BrainstemClient(headless=True)
# prints the approval URL and a short code to enter on any device
```

### Token from the environment
{: .no_toc}

Create a token on your [token page](https://www.brainstem.org/private/users/tokens/) and export it once:

```bash
export BRAINSTEM_API_TOKEN="<token>"
```

`BrainstemClient()` picks it up automatically. You can also pass it explicitly with `BrainstemClient(token="<token>")`. For how long a token stays valid, see [API authentication](/api/#authentication).

### Public data without an account
{: .no_toc}

```python
client = BrainstemClient(anonymous=True)
projects = client.load("project", portal="public", load_all=True)
```

### Another server
{: .no_toc}

```python
client = BrainstemClient(url="http://127.0.0.1:8000/")   # or set BRAINSTEM_API_URL
```

The client can be used as a context manager (`with BrainstemClient() as client:`), sends every request with a 30-second timeout, and retries transient `502`, `503` and `504` responses three times.

## Loading records

`load` returns the `requests.Response`; call `.json()` to get the body. With `load_all=True` it follows every page and returns one merged dictionary.

```python
# one page (100 records by default)
sessions = client.load("session").json()["sessions"]

# one record
session = client.load("session", id="<session-id>").json()["session"]

# every record
all_sessions = client.load("session", load_all=True)["sessions"]

# public portal
public_projects = client.load("project", portal="public").json()["projects"]
```

List responses carry `meta` with `page`, `per_page`, `total_results` and `total_pages`.

Lists of procedures, specimen procedures, sessions and breedings hold performed entries only. Filter on `status` to get planned or cancelled ones, for example `filters={"status": "planned"}` or `filters={"status.in": ["planned", "performed"]}` (see [Planned records](/api/#planned-records)).

The `<session-id>`, `<project-id>` and similar placeholders on this page stand for entry ids. Open the entry in the web interface and copy the id from the address bar or the **API** button ([Finding an ID](/webinterface/import-tool/#finding-an-id)), or read it from a `load` result.

### Filtering
{: .no_toc}

Filters are passed without braces and map directly onto the [API filter syntax](/api/#query-parameters):

```python
client.load("session", filters={"name.icontains": "rat"})
client.load("session", filters={"projects": "<project-id>"})          # relation by id
client.load("dataacquisition", filters={"type.in": ["ExtracellularEphys", "TwoPhotonMicroscopy"]})
client.load("procedure", filters={"target_regions.acronym": "CA1"})   # nestable relation
client.load("subject", filters={"tags.name": "control"})              # tags by name
```

Several filters combine with AND. The operators are listed on the [API page](/api/#query-parameters); a relation can be followed into the related record only when it is nestable (marked on each resource page).

### Sorting and including
{: .no_toc}

```python
client.load("session", sort=["-date_time", "name"])
client.load("session", include=["projects", "dataacquisition"])   # sent as include[]=projects.*
```

Included records are sideloaded next to the main list under their own key (`projects`, `data_acquisitions`), and only records you can read are included.

### Paging
{: .no_toc}

```python
page2 = client.load("session", limit=20, offset=20).json()   # offset must be a multiple of limit
print(page2["meta"])  # {'page': 2, 'per_page': 20, 'total_results': ..., 'total_pages': ...}
```

`limit` is at most 500. `load_all=True` merges every page and de-duplicates sideloaded records by id.

### Convenience loaders
{: .no_toc}

Loaders set sensible default includes and accept named filters. All of them also take `portal`, `id`, `filters`, `sort`, `include`, `limit`, `offset` and `load_all`.

| Method | Named filters | Default includes |
|--------|---------------|------------------|
| `load_project` | `name`, `sessions`, `subjects`, `tags` | sessions, subjects, collections, cohorts |
| `load_subject` | `name`, `projects`, `strain`, `sex`, `tags` | procedures, subjectlogs |
| `load_session` | `name`, `projects`, `datastorage`, `tags` | dataacquisition, behaviors, manipulations, epochs |
| `load_collection` | `name`, `tags` | sessions |
| `load_cohort` | `name`, `tags` | subjects |
| `load_behavior`, `load_dataacquisition`, `load_manipulation` | `session` | |
| `load_procedure`, `load_subjectlog` | `subject` | |
| `load_procedurelog` | `procedure` | |
| `load_equipment` | `name`, `setup` | |
| `load_consumablestock` | `inventory` | |
| `load_behavioralassay`, `load_datastorage`, `load_setup`, `load_hardwaredevice`, `load_publication`, `load_laboratory` | `name` | |
| `load_species` | `name`, `popular_name` | |
| `load_strain` | `name`, `species`, `popular_name` | |
| `load_anatomicalregion` | `name`, `acronym`, `reference` (atlas id) | |
| `load_anatomicalregion_descendants(id)` | | the regions below a region |

`name` filters are case-insensitive substring matches; `tags` filters by tag name.

```python
sessions = client.load_session(name="Rat", load_all=True)
subjects = client.load_subject(sex="M", projects="<project-id>", load_all=True)

mice = client.load_species(popular_name="mouse").json()
ca1 = client.load_anatomicalregion(acronym="CA1").json()["anatomical_regions"][0]
subregions = client.load_anatomicalregion_descendants(ca1["id"]).json()["anatomical_regions"]
```

Models without a loader are reached with `load`:

```python
specimen_sets = client.load("specimenset", filters={"projects": "<project-id>"}, load_all=True)
interfaces = client.load("experimentalinterface", filters={"subject": "<subject-id>"}, load_all=True)
```

## Creating records

`save` without `id` sends a `POST`. Use the required fields of the [resource page](/api/stem/session/); the response holds the record under its singular key.

```python
created = client.save("session", data={
    "name": "Example session",
    "projects": ["<project-id>"],
    "session_type": "subject",
    "subjects": ["<subject-id>"],
    "date_time": "2026-03-02T10:00:00Z",
}).json()
session_id = created["session"]["id"]
```

Type-specific records take `type` and `details`; the fields of each type are on the [schema pages](/api/schemas/):

```python
client.save("dataacquisition", data={
    "session": session_id,
    "type": "ExtracellularEphys",
    "experimental_interfaces": ["<experimental-interface-id>"],
    "details": {"nChannels": 64, "sr": {"value": 30000, "unit": "Hz"}},
})
```

Always check `response.ok` or `status_code`; a `400` body names the invalid fields.

## Updating records

`save` with `id` sends a `PATCH`: only the fields you send change. There is no full-replace mode.

```python
client.save("session", id="<session-id>", data={"description": "updated"})
```

List fields replace the whole list. Read the record without `include` first, then send the complete list:

```python
session = client.load("session", id="<session-id>").json()["session"]
client.save("session", id="<session-id>",
            data={"projects": session["projects"] + ["<other-project-id>"]})
```

## Deleting records

```python
response = client.delete("session", id="<session-id>")
assert response.status_code == 204
```

## Exporting projects and sessions

`export_project` and `export_session` return the [export document](/api/export/) (format 2.1) as a dictionary. Large projects exceed the server's direct request limit; use a background job.

```python
export = client.export_project("<project-id>")
print(export["export_info"]["record_count"], export["export_info"]["counts"])
for record in export["records"]["stem.session"]:
    print(record["pk"], record["fields"]["name"])

export = client.export_session("<session-id>")                    # one session and everything it touches
export = client.export_project("<project-id>", background=True)   # queued on the server, polled until ready
```

Export errors raise `ExportError`; an invalid token raises `AuthenticationError`. Exports are limited to 30 per hour.

## The agent reference

The server's own description of its API, written for AI agents and tool authors ([Agent reference](/api/reference/)):

```python
print(client.agent_reference())                            # index
print(client.agent_reference("resources/session.md"))      # one resource
print(client.agent_reference("guides/query-planning.md"))  # a guide
```

## Command line interface

The package installs the `brainstem` command. `--token` and `--url` default to `BRAINSTEM_API_TOKEN` and `BRAINSTEM_API_URL`.

```bash
brainstem login                      # browser sign-in; caches the token, never prints it
brainstem login --headless           # prints URL and code instead
brainstem logout                     # removes the cached token

brainstem load session
brainstem load session --filters name.icontains=Rat --sort -name --include projects
brainstem load session --id "<session-id>"
brainstem load session --per-page 20 --page 2
brainstem load session --all         # every page, one merged JSON object
brainstem load project --portal public

brainstem save session --data '{"name": "New session", "projects": ["<project-id>"], "session_type": "subject", "subjects": ["<subject-id>"]}'
brainstem save session --id "<session-id>" --data '{"description": "updated"}'
brainstem delete session --id "<session-id>"

brainstem reference rules.md         # a page of the agent reference, no login needed
```

`brainstem load --help` lists every model name the client knows.

## Errors

- `AuthenticationError`: the device flow failed or the token is invalid or expired. Run `brainstem login` or create a new token.
- `ExportError`: an export was refused or the server does not support exports.
- `ValueError`: unknown model, invalid portal, bad paging arguments or a missing id.
- `FutureWarning`: a deprecated name was used, for example `brainregion` instead of `anatomicalregion`.

{: .note }
Plain `load`, `save` and `delete` return the response without raising on `4xx` or `5xx`. A failed save or delete looks like any other call until you check `status_code`, or call `raise_for_status()`.

## Troubleshooting

- **401 Unauthorized**: run `brainstem login` or create a new token on your [token page](https://www.brainstem.org/private/users/tokens/).
- **403 Forbidden**: your role on the project or lab resource does not allow the action. See [permissions](/datamodel/permissions/).
- **404 Not Found**: the record does not exist, is not visible to you, or the server does not have the resource yet.
- **400 Bad request**: the body names the fields; compare with the resource and schema pages. For filters, `Invalid nested filter field` means the relation is not nestable.
- **Unknown model**: upgrade to version 2.1 or newer for the specimen-era resources.

## Next steps

- Follow an end-to-end example in the [Electrophysiology workflow](/tutorials/electrophysiology-workflow/) tutorial.
- Convert exports to NWB with [brainstem-nwb](/tools/brainstem-nwb/).
- Let an AI agent drive the client with the [agent skills](/tools/agent-skills/).
