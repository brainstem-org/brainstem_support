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

## Installation

Install the published package from PyPI (recommended) or clone the GitHub repository.

```bash
pip install brainstem_python_api_tools
```

```bash
git clone https://github.com/brainstem-org/brainstem_python_api_tools.git
```

## Authentication

Initializing `BrainstemClient` prompts for your BrainSTEM email and password unless you supply a saved token. Tokens are stored locally in the API tool cache and reused automatically.

```python
from brainstem_api_tools import BrainstemClient

# Prompts for credentials the first time and caches a token
client = BrainstemClient()
```

```python
# Use a saved token instead of prompting for credentials
token = "YOUR_TOKEN"
client = BrainstemClient(token=token)

# Or load a token from a .env file (keep .env gitignored)
from dotenv import load_dotenv
import os
from brainstem_api_tools import BrainstemClient

load_dotenv()
client = BrainstemClient(token=os.getenv("BRAINSTEM_API_TOKEN"))
```

If you receive a `401 Unauthorized` response, run `BrainstemClient()` again to refresh the cached token or pass a newly generated token explicitly.

## Quick start

Load projects using the private portal (default) or specify the public portal for open datasets. Response payloads follow the schema described in `docs/api/stem/project.md`.

```python
public_projects = client.load_model("project", portal="public").json()

projects = public_projects.get('projects', [])
print(f"Loaded {len(projects)} public projects")
if projects:
    print(projects[0]["name"])
```

Private data uses the default portal. Ensure the authenticated user has the necessary permissions, as outlined in the API docs.

```python
private_sessions = client.load_model("session").json()

sessions = private_sessions.get('sessions', [])
if sessions:
    print(sessions[0]["name"])
```

## Filtering requests

Filters map directly onto the query parameters documented in the STEM API. Common case-insensitive modifiers include `.icontains`, `.iexact`, `.istartswith`, and `.iendswith`.

```python
filtered = client.load_model(
    "project",
    portal="public",
    filters={"name.icontains": "visual"}
).json()["projects"]

print(f"Matches: {len(filtered)}")
```

Multiple filters apply AND logic.

```python
filtered = client.load_model(
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
alpha_projects = client.load_model(
    "project",
    portal="public",
    sort=['name']  # Ascending alphabetical order
).json()

print("Alphabetically sorted projects:")
for i, project in enumerate(alpha_projects.get('projects', [])[:3]):
    print(f"{i+1}. {project.get('name')}")

# Sort projects reverse-alphabetically by name
reverse_alpha = client.load_model(
    "project",
    portal="public",
    sort=['-name']  # Descending alphabetical order
).json()

print("Reverse alphabetically sorted projects:")
for i, project in enumerate(reverse_alpha.get('projects', [])[:3]):
    print(f"{i+1}. {project.get('name')}")
```

## Creating records

Write operations require contributor permissions on the target project or resource. Use `save_model` with the required fields documented in the relevant API page (for example, `docs/api/stem/session.md`).

**Important**: The `projects` field must be a list (array) of project IDs, not a single string.

```python
payload = {
    "name": "Example Session",
    "projects": ["your-project-uuid"],  # Must be a list, not a string!
    "description": "Created via API tool"
}

created = client.save_model("session", data=payload).json()

if 'session' in created:
    session_id = created["session"]["id"]
    print(f"Created session with ID: {session_id}")
else:
    print(f"Error creating session: {created}")
```

## Updating records

Fetch the target record, modify the fields you want to change, and resubmit the partial payload.

```python
# First load a session you have permission to modify
filtered_session = client.load_model(
    'session', 
    filters={'name.iexact': 'your session'}
).json()

# Update the description
filtered_session['description'] = 'Updated via API'

# Pass the whole filtered_session object to save_model
updated_session = client.save_model(
    'session', 
    id=filtered_session['sessions'][0]['id'], 
    data=filtered_session
).json()

print("Session updated successfully")
```

## Deleting records

Use `delete_model` with the record ID. A successful delete returns status code `204 No Content`.

```python
response = client.delete_model("session", id="your-session-uuid")
if response.status_code == 204:
    print("Session deleted")
```

## Troubleshooting

- **401 Unauthorized**: Re-run `BrainstemClient()` to generate a fresh token or confirm credentials.
- **403 Forbidden**: Verify you have the necessary permissions (see the permission tables in the STEM API docs).
- **404 Not Found**: Make sure the ID exists and is within the selected portal.
- **Validation errors (400)**: Match the required fields and value formats listed in the model-specific documentation.

For a notebook-style walk-through, open `brainstem_api_tutorial.ipynb` in the API tools repository.

## Next Steps

- **Complete Experimental Workflows**: Review the [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow) or [Two-Photon Imaging Workflow]({{site.baseurl}}/tutorials/two-photon-imaging-workflow) tutorials to see how API data fits into complete experimental documentation
- **Data Storage Integration**: Learn about [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage) to optimize your API-based analysis workflows with proper data organization
- **MATLAB Integration**: If you work in mixed programming environments, check out the [MATLAB API tool tutorial]({{site.baseurl}}/tutorials/matlab-api-tool) for cross-platform data access patterns
