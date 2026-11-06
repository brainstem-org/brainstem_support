---
layout: default
title: MATLAB API tool
parent: Tools
nav_order: 1
---
# MATLAB API tool
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Overview

The BrainSTEM MATLAB API tool (`brainstem_matlab_api_tools`) is a thin client for the [REST API](/api/). The `BrainstemClient` class holds your token and server URL; the `brainstem.*` package functions behind it can also be called directly. Requests and responses keep the shapes the API defines, so every [resource page](/api/stem/) applies directly.

> **Repository and tutorial:** [brainstem-org/brainstem_matlab_api_tools](https://github.com/brainstem-org/brainstem_matlab_api_tools). The repository includes `brainstem_api_tutorial.m` with runnable sections.

Version 2.1 addresses every resource of the current data model, including specimen sets, specimens, specimen procedures, experimental interfaces, material usages, procedure episodes, anatomical regions and templates, and adds exports, the agent reference and anonymous public reads. Those features need a BrainSTEM server of the current release; older servers answer `404` for them. The toolbox uses base MATLAB only (`webread`, `webwrite`, `jsondecode`).

## Installation

Clone the repository and add its root folder to your path:

```matlab
addpath('/path/to/brainstem_matlab_api_tools')
```

Only the root folder is needed. MATLAB discovers the `+brainstem` package and the `BrainstemClient` class itself; do not add `+brainstem/` to the path.

## Authentication

BrainSTEM enforces two-factor authentication (2FA). The client signs you in through the browser, so your password is never typed into MATLAB. See [API authentication](/api/#authentication) for the full flow.

### Token from the environment (scripts, HPC)
{: .no_toc}

Create a token on your [token page](https://www.brainstem.org/private/users/tokens/) and set it once:

```matlab
setenv('BRAINSTEM_API_TOKEN', '<token>')
client = BrainstemClient();                     % picks it up automatically

client = BrainstemClient('token', '<token>');   % or pass it directly
```

For how long a token stays valid, see [API authentication](/api/#authentication). The client warns when fewer than 15 days remain.

### Interactive sign-in (desktop MATLAB)
{: .no_toc}

Without a token in the environment or in the cache, `BrainstemClient()` starts the device flow: it opens the approval page in your browser (and prints the URL in case the browser does not open), and waits until you approve. The token is cached in your MATLAB preferences folder and reused in later sessions. Only a `401` response triggers a new sign-in.

```matlab
client = BrainstemClient();     % opens the browser approval page
client.logout();                % forget the cached token for this server
```

### Public data without an account
{: .no_toc}

```matlab
client = BrainstemClient('anonymous', true);
projects = client.load('project', 'portal', 'public', 'load_all', true);
```

### Another server
{: .no_toc}

```matlab
client = BrainstemClient('url', 'http://127.0.0.1:8000/');   % or setenv('BRAINSTEM_API_URL', ...)
```

## Loading records

`client.load(model, ...)` returns the decoded response. List responses hold a struct array under the plural response key of the resource (`sessions`, `data_acquisitions`, `consumable_stocks`, ...) and a `meta` struct with `page`, `per_page`, `total_results` and `total_pages`.

```matlab
out = client.load('session');                        % first page, 100 records
disp(out.meta.total_results)

out = client.load('session', 'id', '<session-id>');  % one record: out.session
out = client.load('session', 'load_all', true);      % every page
```

Lists of procedures, specimen procedures, sessions and breedings hold performed entries only. Filter on `status` to get planned or cancelled ones, for example `'filter', {'status', 'planned'}` (see [Planned records](/api/#planned-records)).

The `<session-id>`, `<project-id>` and similar placeholders on this page stand for entry ids. Open the entry in the web interface and copy the id from the address bar or the **API** button ([Finding an ID](/webinterface/import-tool/#finding-an-id)), or read it from a `load` result.

### Query options
{: .no_toc}

| Option | Meaning |
|---|---|
| `'filter', {field, value, ...}` | pairs of filter key and value, e.g. `{'name.icontains', 'Rat'}`; a relation by id is `{'projects', '<project-id>'}` |
| `'sort', {'-date_time'}` | sort fields, `-` for descending |
| `'include', {'projects', 'behaviors'}` | sideload related records (sent as `include[]=<name>.*`) |
| `'limit', n` | page size, 1 to 500 (default 100) |
| `'offset', n` | a multiple of the page size |
| `'load_all', true` | follow every page and merge the results |
| `'portal', 'public'` | the public portal (default `'private'`) |
| `'app', 'resources'` | the app of a model without a convenience loader; usually inferred |

```matlab
out = client.load('session', ...
    'filter',  {'name.icontains', 'Rat', 'projects', '<project-id>'}, ...
    'sort',    {'-date_time'}, ...
    'include', {'projects', 'dataacquisition'});

out = client.load('dataacquisition', 'filter', {'type.in', 'ExtracellularEphys'});
out = client.load('procedure', 'filter', {'target_regions.acronym', 'CA1'});   % nestable relation
out = client.load('subject', 'filter', {'tags.name', 'control'});              % tags by name
```

The operators are listed on the [API page](/api/#query-parameters). A relation can be followed into the related record only when it is nestable (marked on each resource page). Included records are sideloaded next to the main list, and only the records you can read are included.

### Convenience loaders
{: .no_toc}

Loaders set default includes and accept named filters as name-value pairs. All of them also take `portal`, `filter`, `sort`, `include`, `limit`, `offset` and `load_all`.

| Method | Named filters | Default includes |
|--------|---------------|------------------|
| `load_project` | `name`, `description`, `sessions`, `subjects`, `tags` | sessions, subjects, collections, cohorts |
| `load_subject` | `name`, `description`, `projects`, `strain`, `sex`, `tags` | procedures, subjectlogs |
| `load_session` | `name`, `description`, `projects`, `datastorage`, `tags` | dataacquisition, behaviors, manipulations, epochs |
| `load_collection` | `name`, `description`, `tags` | sessions |
| `load_cohort` | `name`, `description`, `tags` | subjects |
| `load_behavior`, `load_dataacquisition`, `load_manipulation` | `session` | |
| `load_procedure` | `subject` | |
| `load_subjectlog` | `subject`, `type`, `description` | |
| `load_procedurelog` | `procedure` | |
| `load_equipment` | `name`, `setup` | |
| `load_consumablestock` | `inventory` | |

`name` and `description` are case-insensitive substring matches; `tags` filters by tag name.

```matlab
sessions  = client.load_session('name', 'Rat', 'load_all', true);
subjects  = client.load_subject('sex', 'M', 'projects', '<project-id>');
behaviors = client.load_behavior('session', '<session-id>');

% models without a loader
consumables   = client.load('consumable');
specimen_sets = client.load('specimenset', 'filter', {'projects', '<project-id>'}, 'load_all', true);
```

## Creating records

`client.save(data, model)` sends a `POST` when the struct has no `id`. Use the required fields of the [resource page](/api/stem/session/); the response holds the record under its singular key.

```matlab
s = struct();
s.name = 'Example session';
s.projects = {'<project-id>'};
s.session_type = 'subject';
s.subjects = {'<subject-id>'};
s.date_time = '2026-03-02T10:00:00Z';

created = client.save(s, 'session');
session_id = created.session.id;
```

Type-specific records take `type` and `details`; the fields of each type are on the [schema pages](/api/schemas/):

```matlab
d = struct();
d.session = session_id;
d.type = 'ExtracellularEphys';
d.experimental_interfaces = {'<experimental-interface-id>'};
d.details = struct('nChannels', 64, 'sr', struct('value', 30000, 'unit', 'Hz'));
client.save(d, 'dataacquisition');
```

Validation errors are raised as `BrainSTEM:save` with the field messages from the server.

## Updating records

Pass a struct with an `id`. The default method is `PUT`, which expects the complete record; fields you leave out are kept, not cleared. Use `'method', 'patch'` to send only the fields you change.

```matlab
p = struct('id', '<session-id>', 'description', 'updated');
client.save(p, 'session', 'method', 'patch');
```

List fields replace the whole list. Reload the record without `include` first, then send the complete list:

```matlab
s = client.load('session', 'id', '<session-id>'); s = s.session;
s.projects{end+1} = '<other-project-id>';
client.save(struct('id', s.id, 'projects', {s.projects}), 'session', 'method', 'patch');
```

Records loaded with `include` carry a `brainstem_included` field; saving such a list raises a `BrainSTEM:save:partialList` warning because it may hold only the records you can read.

## Deleting records

```matlab
client.delete('<session-id>', 'session');
```

## Exporting projects and sessions

`export_project` and `export_session` return the [export document](/api/export/) (format 2.1) decoded with `jsondecode`. Large projects exceed the server's direct request limit; use a background job.

```matlab
export = client.export_project('<project-id>');
export.export_info.record_count

export = client.export_project('<project-id>', 'background', true);   % queued and polled
session_export = client.export_session('<session-id>');

% keep the original JSON, for example for brainstem-nwb
client.export_project('<project-id>', 'file', 'project-export.json.gz');
```

`jsondecode` sanitizes field names, so `records.stem_project` stands for `"stem.project"`; use the `'file'` option when another tool needs the original keys. Exports are limited to 30 per hour.

## The agent reference

The server's own description of its API, written for AI agents and tool authors ([Agent reference](/api/reference/)):

```matlab
disp(client.agent_reference('index.md'))
disp(client.agent_reference('resources/session.md'))
```

## Errors

Errors carry identifiers you can catch: `BrainSTEM:load`, `BrainSTEM:save`, `BrainSTEM:delete`, `BrainSTEM:export`, `BrainSTEM:auth`, `BrainSTEM:agentReference`, and `BrainSTEM:deviceAuthExpired`, `BrainSTEM:deviceAuthDenied`, `BrainSTEM:deviceAuthTimeout` for the sign-in. Server validation errors are flattened to `field: message | field2: message`. Using the deprecated `brainregion` model warns with `BrainSTEM:deprecatedModel` and routes to `anatomicalregion`.

## Troubleshooting

- **401 Unauthorized**: the client signs you in again automatically; otherwise call `client.logout()` and create a new client, or create a token on your [token page](https://www.brainstem.org/private/users/tokens/).
- **403 Forbidden**: your role on the project or lab resource does not allow the action. See [permissions](/datamodel/permissions/).
- **404 Not Found**: the record does not exist, is not visible to you, or the server does not have the resource yet.
- **400 Bad request**: the message names the fields; compare with the resource and schema pages.
- **Offset errors**: `offset` must be a multiple of `limit`; use `load_all` to avoid manual paging.

The toolbox ships tests: `runtests('brainstem.BrainstemTests', 'Tag', 'offline')` runs without network access.

## Next steps

- Follow an end-to-end example in the [Electrophysiology workflow](/tutorials/electrophysiology-workflow/) tutorial.
- Convert exports to NWB with [brainstem-nwb](/tools/brainstem-nwb/).
- See the [Python API tool](/tools/python-api-tool/) for the same operations in Python.
