---
layout: default
title: MATLAB API tool
parent: API tools
nav_order: 1
---
# MATLAB API tool
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Overview

The BrainSTEM MATLAB API tool (`brainstem_matlab_api_tools`) provides a thin wrapper around the REST endpoints documented in the [STEM API reference]({{ "/api/stem/" | absolute_url }}). This page mirrors the structure of those docs while expanding on hands-on usage. Every snippet below has been tested against the public API; replace placeholders (for example, IDs) with values available to your account.

The `BrainstemClient` class is the recommended entry point. It holds the authentication token and base URL for all subsequent calls, and supports both interactive browser-based login and direct token injection for scripts and HPC workflows.

> **Repository & tutorial:** Source code and examples live in [brainstem-org/brainstem_matlab_api_tools](https://github.com/brainstem-org/brainstem_matlab_api_tools). The repository includes the `brainstem_api_tutorial.m` script that mirrors this guide with runnable sections.

## Installation

Clone the MATLAB helper package and add the root folder to your MATLAB path:

```matlab
git clone https://github.com/brainstem-org/brainstem_matlab_api_tools.git
addpath('/path/to/brainstem_matlab_api_tools')
```

Only the root folder needs to be added. MATLAB automatically discovers the `+brainstem` package folder and the `BrainstemClient` class. Do not add `+brainstem/` itself to the path.

## Authentication

BrainSTEM enforces two-factor authentication (2FA). To ensure 2FA is always respected, authentication uses a **browser-based device authorization flow** — your password is never sent to a script.

### Recommended: Personal Access Token (scripts, HPC, automation)

Create a token at [brainstem.org/private/users/tokens/](https://www.brainstem.org/private/users/tokens/). Tokens are valid for 1 year (sliding, auto-refresh).

```matlab
% Option A: environment variable (set once per shell/session)
setenv('BRAINSTEM_TOKEN', '<your_token>')
client = BrainstemClient();   % picks it up automatically

% Option B: pass directly
client = BrainstemClient('token', '<your_token>');
```

### Interactive login (device flow, desktop MATLAB)

When neither argument is supplied and the `BRAINSTEM_TOKEN` environment variable is not set, `BrainstemClient` opens a browser window automatically. If you are already logged in to BrainSTEM, simply click **Approve** in the browser. The token is cached and reused in future sessions.

```matlab
client = BrainstemClient();   % opens browser login page
```

If the browser cannot be opened (headless environment), MATLAB prints a short code and URL to enter on any other device.

Re-run `BrainstemClient()` or call `brainstem.get_token()` directly if you see HTTP 401 responses.

## Loading data

`client.load` retrieves records from any BrainSTEM endpoint. All arguments map directly onto their HTTP counterparts.

```matlab
out = client.load('session');
disp(numel(out.sessions))
```

Load a single record by UUID:

```matlab
out = client.load('session', 'id', 'c5547922-c973-4ad7-96d3-72789f140024');
```

Auto-paginate to retrieve all records across multiple pages:

```matlab
out = client.load('session', 'load_all', true);
```

### Convenience loaders

Convenience loaders include the correct `app` and default `include` lists for common models:

| Method | Default includes | Named filter kwargs |
|--------|-----------------|---------------------|
| `load_project` | sessions, subjects, collections, cohorts | `name`, `id`, `tags` |
| `load_subject` | procedures, subjectlogs | `name`, `id`, `sex`, `strain`, `tags` |
| `load_session` | dataacquisition, behaviors, manipulations, epochs | `name`, `id`, `projects`, `tags` |
| `load_collection` | sessions | `name`, `id`, `tags` |
| `load_cohort` | subjects | `name`, `id`, `tags` |
| `load_behavior` | — | `session`, `id`, `tags` |
| `load_dataacquisition` | — | `session`, `id`, `tags` |
| `load_manipulation` | — | `session`, `id`, `tags` |
| `load_procedure` | — | `subject`, `id`, `tags` |

```matlab
project = client.load_project('name', 'Allen Institute: Visual Coding – Neuropixels');
subject = client.load_subject('name', 'Mouse');
session = client.load_session('name', 'Example Session');
```

## Filtering

Filters accept cell arrays of key–value pairs. The modifier syntax (`.icontains`, `.iexact`, etc.) matches the API documentation.

```matlab
filtered = client.load('project', ...
    'filter', {'name.icontains', 'Allen'});

disp(numel(filtered.projects))
```

Multiple filter conditions can be specified as pairs in the same cell array:

```matlab
filtered = client.load('session', ...
    'filter', {'name.icontains', 'Rat', 'description.icontains', 'demo'});
```

The convenience loaders also support shorthand filter parameters:

```matlab
% Filter projects by name and tags
project = client.load_project('name', 'Allen', 'tags', '1');

% Filter subjects by name and sex
subject = client.load_subject('name', 'Mouse', 'sex', 'M');
```

## Sorting

Pass a cell array of field names in `sort`. Prefix with `-` for descending order.

```matlab
descending_sessions = client.load('session', 'sort', {'-start_time'});
```

## Including related records

Request related models in a single call by supplying `include`. Each entry automatically expands to `<name>.*`, mirroring the REST include syntax.

```matlab
with_related = client.load('session', ...
    'include', {'projects', 'datastorage', 'dataacquisition'});

project_names = arrayfun(@(p) p.name, with_related.projects, 'UniformOutput', false);
```

## Creating records

Use `client.save` with the required fields from the STEM API reference. The example below assumes you have contributor access to the project ID provided. Note that `tags` is a required field and can be set to an empty array if no tags are needed.

```matlab
payload = struct();
payload.name = 'Example Session';
payload.description = 'Created via MATLAB API tool';
payload.projects = {'your-project-uuid'};
payload.tags = [];

created = client.save(payload, 'session');
session_id = created.session.id;
```

## Updating records

Pass a struct with an `id` field and any fields to change. Use `'method', 'patch'` for a partial update (only the supplied fields are modified).

```matlab
update_data = struct( ...
    'id', 'your-session-uuid', ...
    'description', 'Updated via MATLAB API tool', ...
    'tags', []);

updated = client.save(update_data, 'session', 'method', 'patch');
```

## Deleting records

```matlab
client.delete('your-session-uuid', 'session');
```

## Troubleshooting

- **401 Unauthorized**: Regenerate your token with `brainstem.get_token()` or create a new Personal Access Token at [brainstem.org/private/users/tokens/](https://www.brainstem.org/private/users/tokens/).
- **403 Forbidden**: Check that your user or group has the required permissions listed in the STEM API documentation.
- **404 Not Found**: Confirm the record exists in the selected portal (public/private).
- **Validation errors (400)**: Ensure your payload matches the field definitions in the API reference. Remember that `tags` is a required field for sessions (can be an empty array).

The repository ships with `brainstem_api_tutorial.m`, a tutorial script demonstrating common workflows.

## Next Steps

- **Complete Experimental Documentation**: Review the [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow) or [Two-Photon Imaging Workflow]({{site.baseurl}}/tutorials/two-photon-imaging-workflow) tutorials to understand how API data access fits into complete experimental workflows
- **Cross-Platform Integration**: If you work in mixed programming environments, explore the [Python API tool tutorial]({{site.baseurl}}/api-tools/python-api-tool) for complementary examples
- **Data Management**: Learn about [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage) to keep file locations synchronized with metadata returned by the API
