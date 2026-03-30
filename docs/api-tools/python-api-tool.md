---
layout: default
title: Python API tool
parent: API tools
nav_order: 2
---
# Python API tool
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Overview

The BrainSTEM Python API tool (`brainstem_python_api_tools`) provides a thin wrapper around the REST endpoints documented in the [STEM API reference]({{ "/api/stem/" | absolute_url }}). This page mirrors the structure of those docs while expanding on hands-on usage. Every snippet below has been tested against the public API; replace placeholders (for example, IDs) with values you can access in your own account.

> **Repository & notebooks:** Source code and examples live in [brainstem-org/brainstem_python_api_tools](https://github.com/brainstem-org/brainstem_python_api_tools). The repository includes the `brainstem_api_tutorial.ipynb` notebook and `brainstem_api_tutorial.py` script that mirror this guide with runnable cells.

## Installation

Install the published package from PyPI (recommended) or clone the GitHub repository.

```bash
pip install brainstem_python_api_tools
```

```bash
git clone https://github.com/brainstem-org/brainstem_python_api_tools.git
```

## Authentication

BrainSTEM enforces two-factor authentication (2FA). To ensure 2FA is always respected, authentication uses a **browser-based device authorization flow** — your password is never sent to a script or CLI tool.

### First run — browser flow (default)

```python
from brainstem_api_tools import BrainstemClient

# Opens a browser window for secure login (2FA is enforced).
# The token is cached at ~/.config/brainstem/token and reused automatically.
client = BrainstemClient()
```

On the first run a browser window opens automatically. If you are already logged in to BrainSTEM, you only need to click **Approve**. The issued token is stored with owner-read-only permissions (`0600`) and reused on subsequent runs without another browser prompt.

### Headless environments (no browser)

For servers or Docker containers where no browser is available, pass `headless=True`. The CLI prints a short URL and user code instead of opening a browser:

```python
client = BrainstemClient(headless=True)
# Prints: Open https://www.brainstem.org/account/authorize/ and enter: WXYZ-1234
```

Navigate to that URL on any device, enter the code, and approve — the script receives the token automatically.

### Pass a token directly

If you have already created a Personal Access Token at [brainstem.org/private/users/tokens/](https://www.brainstem.org/private/users/tokens/), you can pass it directly and skip the browser flow entirely. Tokens are valid for 1 year (sliding, auto-refresh).

```python
client = BrainstemClient(token="YOUR_PERSONAL_ACCESS_TOKEN")
```

For scripts and automation it is recommended to read the token from an environment variable rather than hardcoding it:

```python
import os
from brainstem_api_tools import BrainstemClient

client = BrainstemClient(token=os.environ["BRAINSTEM_TOKEN"])
```

### Connect to a different server

```python
# Local development instance
client = BrainstemClient(url="http://127.0.0.1:8000/")
```

If you receive a `401 Unauthorized` response, re-authenticate by running `brainstem login` in the CLI (see [CLI](#command-line-interface)) or create a new token at [brainstem.org/private/users/tokens/](https://www.brainstem.org/private/users/tokens/).

## Quick start

Load records using the private portal (default) or specify the public portal for open datasets. Response payloads follow the schema described in the [STEM API reference]({{ "/api/stem/" | absolute_url }}).

```python
public_projects = client.load("project", portal="public").json()

projects = public_projects.get('projects', [])
print(f"Loaded {len(projects)} public projects")
if projects:
    print(projects[0]["name"])
```

Private data uses the default portal. Ensure the authenticated user has the necessary permissions, as outlined in the API docs.

```python
private_sessions = client.load("session").json()

sessions = private_sessions.get('sessions', [])
if sessions:
    print(sessions[0]["name"])
```

## Filtering requests

Filters map directly onto the query parameters documented in the STEM API. Common case-insensitive modifiers include `.icontains`, `.iexact`, `.startswith`, and `.endswith`.

```python
filtered = client.load(
    "project",
    portal="public",
    filters={"name.icontains": "visual"}
).json()["projects"]

print(f"Matches: {len(filtered)}")
```

Multiple filters apply AND logic.

```python
filtered = client.load(
    "project",
    portal="public",
    filters={
        "name.icontains": "allen",
        "description.icontains": "neuropixels"
    }
).json()["projects"]

print(f"Matches: {len(filtered)}")
```

## Sorting results

Provide field names in `sort`. Prefix a field with `-` for descending order, mirroring the API convention.

```python
# Sort projects alphabetically by name
alpha_projects = client.load(
    "project",
    portal="public",
    sort=['name']
).json()

# Sort in descending order
reverse_alpha = client.load(
    "project",
    portal="public",
    sort=['-name']
).json()
```

## Pagination

Results are paged. Use `limit` and `offset` for manual pagination, or pass `load_all=True` to fetch every page automatically.

```python
# Manual — second page of 20
page2 = client.load("session", limit=20, offset=20).json()

# Auto-paginate — returns a merged dict with all records
all_sessions = client.load("session", load_all=True)
print(f"Total sessions: {len(all_sessions['sessions'])}")
```

## Convenience loaders

Convenience loaders set sensible `include` defaults and expose named keyword arguments for the most common filters.

| Method | Default includes | Named filter kwargs |
|--------|-----------------|---------------------|
| `load_project` | sessions, subjects, collections, cohorts | `name`, `tags` |
| `load_subject` | procedures, subjectlogs | `name`, `projects`, `sex`, `strain`, `tags` |
| `load_session` | dataacquisition, behaviors, manipulations, epochs | `name`, `projects`, `datastorage`, `tags` |
| `load_collection` | sessions | `name`, `tags` |
| `load_cohort` | subjects | `name`, `tags` |
| `load_behavior` | — | `session`, `tags` |
| `load_dataacquisition` | — | `session`, `tags` |
| `load_manipulation` | — | `session`, `tags` |
| `load_procedure` | — | `subject`, `tags` |

```python
# Load all sessions whose name contains "Rat", with related data
sessions = client.load_session(name='Rat', load_all=True)

# Load subjects by sex and project
subjects = client.load_subject(sex='M', projects='<project-uuid>', load_all=True)

# Load behaviors scoped to a session
behaviors = client.load_behavior(session='<session-uuid>', load_all=True)

# Convenience loaders also accept filters= and include= overrides
sessions = client.load_session(
    name='Rat',
    include=['projects'],
    filters={'description.icontains': 'hippocampus'},
    load_all=True,
)
```

## Creating records

Write operations require contributor permissions on the target project. Use `save` with the required fields documented in the relevant API page.

**Important**: The `projects` field must be a list (array) of project UUIDs, not a single string.

```python
payload = {
    "name": "Example Session",
    "projects": ["your-project-uuid"],
    "description": "Created via API tool"
}

created = client.save("session", data=payload).json()

if 'session' in created:
    session_id = created["session"]["id"]
    print(f"Created session with ID: {session_id}")
else:
    print(f"Error: {created}")
```

## Updating records

Pass the record UUID as `id` to perform a partial update (PATCH). Only the fields you supply are changed.

```python
updated = client.save(
    'session',
    id='your-session-uuid',
    data={'description': 'Updated via API'}
).json()

print("Session updated successfully")
```

## Deleting records

Use `delete` with the record UUID. A successful delete returns status code `204 No Content`.

```python
response = client.delete("session", id="your-session-uuid")
if response.status_code == 204:
    print("Session deleted")
```

## Command-line interface

After installation a `brainstem` command is available in your shell.

### Authentication

```bash
# Authenticate (opens browser) and cache token
brainstem login

# Headless — prints URL + code instead of opening browser
brainstem login --headless

# Connect to a local dev server
brainstem login --url http://127.0.0.1:8000/

# Remove cached token
brainstem logout
```

### Loading data

```bash
# Load all sessions (private portal)
brainstem load session

# Filter, sort and embed related data
brainstem load session --filters name.icontains=Rat --sort -name --include projects

# Load a single record by UUID
brainstem load session --id <uuid>

# Manual pagination
brainstem load session --limit 20 --offset 20

# Public portal
brainstem load project --portal public
```

### Creating and updating records

```bash
# Create a new session
brainstem save session --data '{"name":"New session","projects":["<uuid>"]}'

# Update an existing record (partial update)
brainstem save session --id <uuid> --data '{"description":"updated"}'
```

### Deleting records

```bash
brainstem delete session --id <uuid>
```

All subcommands accept `--token`, `--headless`, and `--url` to override defaults.

## Troubleshooting

- **401 Unauthorized**: Run `brainstem login` or create a new Personal Access Token at [brainstem.org/private/users/tokens/](https://www.brainstem.org/private/users/tokens/).
- **403 Forbidden**: Verify you have the necessary permissions (see the permission tables in the STEM API docs).
- **Token file location**: `~/.config/brainstem/token` — stored with `0600` permissions. Never commit this file to version control.
- **404 Not Found**: Make sure the ID exists and is within the selected portal.
- **Validation errors (400)**: Match the required fields and value formats listed in the model-specific documentation.

For a notebook-style walk-through, open `brainstem_api_tutorial.ipynb` in the API tools repository.

## Next Steps

- **Complete Experimental Workflows**: Review the [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow) or [Two-Photon Imaging Workflow]({{site.baseurl}}/tutorials/two-photon-imaging-workflow) tutorials to see how API data fits into complete experimental documentation
- **Data Storage Integration**: Learn about [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage) to optimize your API-based analysis workflows with proper data organization
- **MATLAB Integration**: If you work in mixed programming environments, check out the [MATLAB API tool tutorial]({{site.baseurl}}/api-tools/matlab-api-tool) for cross-platform data access patterns
