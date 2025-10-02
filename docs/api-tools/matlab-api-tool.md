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

## Installation

Clone the MATLAB helper package and add it to your MATLAB path:

```matlab
git clone https://github.com/brainstem-org/brainstem_matlab_api_tools.git
addpath(genpath('brainstem_matlab_api_tools'))
```

## Authentication

Run `get_token` once to create and store an authentication token. Subsequent API calls reuse the cached credentials.

```matlab
get_token
```

Tokens expire periodically; re-run `get_token` if you see HTTP 401 responses.

## Loading data

`load_model` mirrors the REST endpoints documented under [STEM API]({{ "/api/stem/" | absolute_url }}). All arguments map directly onto their HTTP counterparts, and the helper infers the correct `app` when you omit it.

```matlab
sessions = load_model('model', 'session');
disp(numel(sessions.sessions))
```

Convenience wrappers include the correct `app` and default `include` lists for common models:

- `load_project`: includes `sessions`, `subjects`, `collections`, `cohorts`
- `load_subject`: includes `procedures`, `subjectlogs`
- `load_session`: includes `dataacquisition`, `behaviors`, `manipulations`, `epochs`

They expose a small set of shorthand arguments (for example, `name`, `projects`, `tags`) that expand into the appropriate filter entries internally.

```matlab
project = load_project('name', 'Allen Institute: Visual Coding – Neuropixels');
subject = load_subject('name', 'Mouse');
session = load_session('name', 'Example Session');
```

## Filtering

Filters accept cell arrays of key–value pairs. The modifier syntax (`.icontains`, `.iexact`, etc.) matches the API documentation.

```matlab
filtered = load_model(
    'model', 'project', ...
    'filter', {'name.icontains', 'Allen'});

disp(numel(filtered.projects))
```

Multiple filter conditions can be specified as pairs in the same cell array:

```matlab
filtered = load_model(
    'model', 'session', ...
    'filter', {'name.icontains', 'Rat', 'description.icontains', 'demo'});
```

## Sorting

Pass a cell array of field names in `sort`. Prefix with `-` for descending order.

```matlab
descending_sessions = load_model(
    'model', 'session', ...
    'sort', {'-start_time'});
```

## Including related records

Request related models (for example, `projects`, `datastorage`, `dataacquisition`) in a single call by supplying `include`. Each entry automatically expands to `<name>.*`, mirroring the REST include syntax.

```matlab
with_related = load_model(
    'model', 'session', ...
    'include', {'projects', 'datastorage', 'dataacquisition'});

project_names = arrayfun(@(p) p.name, with_related.projects, 'UniformOutput', false);
```

## Creating records

Use `save_model` with the required fields from the STEM API reference. The example below assumes you have contributor access to the project ID provided. Note that `tags` is a required field and can be set to an empty array if no tags are needed.

```matlab
payload = struct();
payload.name = 'Example Session';
payload.description = 'Created via MATLAB API tool';
payload.projects = {'your-project-uuid'};
payload.tags = [];

created = save_model('model', 'session', 'data', payload);
session_id = created.session.id;
```

## Updating records

Update existing records by placing the record ID inside the payload struct. `save_model` detects the `id` field, switches to `PUT`, and replaces the stored record with the data you supply. Remember to include the `tags` field even when updating.

```matlab
update_data = struct(
    'id', 'your-session-uuid', ...
    'description', 'Updated via MATLAB API tool', ...
    'tags', []);

updated = save_model(
    'model', 'session', ...
    'data', update_data);
```

## Troubleshooting

- **401 Unauthorized**: Regenerate your token with `get_token`.
- **403 Forbidden**: Check that your user or group has the required permissions listed in the STEM API documentation.
- **404 Not Found**: Confirm the record exists in the selected portal (public/private).
- **Validation errors (400)**: Ensure your payload matches the field definitions in the API reference. Remember that `tags` is a required field for sessions (can be an empty array).
- **Delete operations**: The MATLAB helpers focus on read and write actions. Use the Python client or direct REST calls if you need to delete records.

The repository ships with `brainstem_api_tutorial.m`, a tutorial script demonstrating common workflows.

## Next Steps

- **Complete Experimental Documentation**: Review the [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow) or [Two-Photon Imaging Workflow]({{site.baseurl}}/tutorials/two-photon-imaging-workflow) tutorials to understand how API data access fits into complete experimental workflows
- **Cross-Platform Integration**: If you work in mixed programming environments, explore the [Python API tool tutorial]({{site.baseurl}}/tutorials/python-api-tool) for complementary examples
- **Data Management**: Learn about [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage) to keep file locations synchronized with metadata returned by the API
