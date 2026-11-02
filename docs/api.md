---
layout: default
title: API
nav_order: 4
has_children: true
has_toc: false
---
# API
{: .no_toc}
The BrainSTEM REST API gives programmatic access to the complete data model: every record you can see in the web interface can be read, created, changed and deleted through HTTPS endpoints that return JSON. [API tools](/tools/) exist for Python and MATLAB, AI assistants can connect through the [MCP server](/api/mcp/) or the [agent skills](/tools/agent-skills/), and the server describes itself in a machine-readable [reference](/api/reference/) that is generated from its code.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Authentication

BrainSTEM uses **Personal Access Tokens** (PATs) for API authentication. Because BrainSTEM enforces two-factor authentication (2FA), tokens are issued through the browser only: your password is never typed into a script or a command line tool.

| Token type | Lifetime | How to obtain | Best for |
|------------|----------|---------------|----------|
| **Personal Access Token** | One year, sliding: each use extends it by a year | Web UI, or the device authorization flow built into the Python and MATLAB tools | Scripts, integrations, CLI tools, AI assistants |

A user can hold up to 10 active tokens. Each token has a name, records when and from where it was last used, and can be revoked at any time. Revocation takes effect immediately.

### Option 1: Create a token in the web UI
{: .no_toc}

Open your [API token management page](https://www.brainstem.org/private/users/tokens/) (Profile → **Security & access** → **API tokens**), click **Create New Personal Access Token**, enter a descriptive name such as "Analysis pipeline" and confirm. You are asked to confirm your password and 2FA code first. Copy the token right away; it is shown only once.

Use it as a bearer token:

```bash
curl -H "Authorization: Bearer YOUR_PERSONAL_TOKEN" \
     https://www.brainstem.org/api/private/stem/project/
```

{: .important }
> Personal access tokens are shown only once when created. Save them in a secure location, for example in the `BRAINSTEM_API_TOKEN` environment variable that all BrainSTEM tools read.

### Option 2: Device authorization flow
{: .no_toc}

The Python and MATLAB tools and the `brainstem` command line sign you in through the browser. The tool asks the server for a device session, opens the approval page, and polls until you approve. The approval page requires your normal login including 2FA.

```
# Step 1 — the tool starts a device session (no authentication)
POST /api/auth/device/        body: {"client_name": "my-script"}
→ {"session_id": "...", "device_code": "...", "user_code": "WXYZ-1234",
   "verification_uri": "https://www.brainstem.org/account/authorize/",
   "verification_uri_complete": "https://www.brainstem.org/account/authorize/?session=...",
   "expires_in": 900, "interval": 5}

# Step 2 — you approve in the browser (with 2FA)

# Step 3 — the tool polls until approved
POST /api/auth/device/token/  body: {"device_code": "..."}
→ {"status": "authorization_pending"}            ← keep polling every 5 s
→ {"status": "success", "token": "...", "token_id": 42, "token_name": "my-script 2026-03-29 14:30:10"}
```

In a headless environment (a server or a container without a browser) the tool prints the `verification_uri` and the short `user_code`; open the URL on any device, enter the code and approve.

All poll responses return HTTP 200 with a status in the body:

```json
{"status": "authorization_pending"}   // keep polling
{"status": "success", "token": "..."}  // done; the token is returned exactly once
{"error": "access_denied"}            // you clicked Deny
{"error": "expired_token"}            // the 15-minute window elapsed; start again
{"error": "already_used"}             // the token was already collected
```

A token obtained this way appears on your token page with the client name and a timestamp, and can be revoked like any other.

### Checking a token
{: .no_toc}

`GET /api/auth/token/info/` with the bearer header returns the token's user, type, issue and expiry times. It answers `401` when the token is invalid or revoked.

### Authentication in the Python and MATLAB tools
{: .no_toc}

- **Python:** `BrainstemClient()` reads `BRAINSTEM_API_TOKEN`, then a cached token, and otherwise opens the browser; `BrainstemClient(headless=True)` prints the code instead. See the [Python API tool](/tools/python-api-tool/).
- **MATLAB:** `BrainstemClient()` reads `BRAINSTEM_API_TOKEN`, then a cached token, and otherwise opens the browser. See the [MATLAB API tool](/tools/matlab-api-tool/).
- **Web API tool:** uses your browser session; no token needed. See the [Web API tool](/tools/web-api-tool/).
- **MCP and agent skills:** configure the bearer header once; see [MCP server](/api/mcp/) and [Agent skills](/tools/agent-skills/).

Both clients and the NWB exporter also read `BRAINSTEM_API_URL` to talk to another server than `https://www.brainstem.org`.

### Security best practices
{: .no_toc}

- Never type your password into a script. Use the device flow or create a token in the web UI.
- Keep tokens out of version control, logs and shared notebooks.
- Give each script or machine its own named token so you can revoke one without touching the others.
- Delete unused tokens on your [token management page](https://www.brainstem.org/private/users/tokens/).

## Endpoint structure

All record endpoints follow one pattern:

```
https://www.brainstem.org/api/{portal}/{app}/{resource}/
https://www.brainstem.org/api/{portal}/{app}/{resource}/{id}/
```

{: .note }
> **portal**: `private` (records you can read, needs a token) or `public` (records of public projects, read-only, no token).
>
> **app**: `stem`, `modules`, `personal_attributes`, `resources`, `taxonomies`, `dissemination` or `users`.
>
> **resource**: the lower-case model name, for example `session`, `procedure`, `specimenset`, `experimentalinterface` or `anatomicalregion`.
>
> **id**: the UUID of one record.

Examples:

```
https://www.brainstem.org/api/private/stem/session/
https://www.brainstem.org/api/private/stem/session/<id>/
https://www.brainstem.org/api/private/modules/procedure/
https://www.brainstem.org/api/public/stem/project/
```

{: .warning }
> `taxonomies/brainregion` is a deprecated alias of `taxonomies/anatomicalregion`. Use the new name.

## Available endpoints

Every resource has its own page with its fields, write rules, permissions and examples. The pages are generated from the server code, so they match the current release.

### Core records
{: .no_toc}
- **[STEM](/api/stem/)**: projects, subjects, sessions, specimen sets and specimens, cohorts, collections, breedings and epochs.
- **[Modules](/api/modules/)**: procedures, procedure episodes and logs, specimen procedures and logs, experimental interfaces, material usages, data acquisition, manipulations, behaviors, equipment, consumable stock, and the templates for each of them.
- **[Personal attributes](/api/personal_attributes/)**: setups, inventories, behavioral assays, data storage, licenses and protocols.

### Shared catalog, taxonomies and dissemination
{: .no_toc}
- **[Resources](/api/resources/)**: consumables, hardware devices and suppliers.
- **[Taxonomies](/api/taxonomies/)**: species, strains, anatomical regions and atlas references, coordinate transforms, behavioral categories and paradigms, setup types and regulatory authorities.
- **[Dissemination](/api/dissemination/)**: publications and journals.

### Collaboration
{: .no_toc}
- **[Users](/api/users/)**: users, groups and laboratories.

### Supporting endpoints
{: .no_toc}
- **[Templates](/api/templates/)**: the templates that prefill procedures, episodes, interfaces, material rows, data acquisitions and manipulations.
- **[Approvals](/api/approvals/)**: the approval requests behind submissions to the shared catalogs and taxonomies.
- **[Invitations and requests](/api/invitations/)**: membership invitations to projects, groups and personal attributes, join requests and pending invitations.
- **[Link tables](/api/links/)**: the many-to-many rows with fields of their own, such as cohort subjects and the interfaces of a data acquisition.

### Technical reference
{: .no_toc}
- **[Schemas](/api/schemas/)**: the type-specific JSON payloads (`type` + `details`, coordinate systems) and their versions.
- **[Relationships](/api/relationships/)**: how resources connect, as the queries that follow each link.
- **[Exports](/api/export/)**: a project or a session as one versioned JSON document.
- **[Public schemas](/api/public-schemas/)**: the permanent URLs of every schema version.
- **[Agent reference](/api/reference/)**: the server's own machine-readable description of its API.
- **[MCP server](/api/mcp/)**: access to the data model and your records for AI applications such as Claude Code and Cursor.

## Public vs private portals

### Private portal
{: .no_toc}
- **Access**: a Personal Access Token, or your browser session in the [Web API tool](/tools/web-api-tool/).
- **Content**: records of the projects you are a member of and the lab resources shared with your groups.
- **Operations**: read, create, change and delete, according to your role on each record.

### Public portal
{: .no_toc}
- **Access**: open, no token.
- **Content**: records of projects that their owners made public, and lab resources made public individually.
- **Operations**: read only. An empty public result says nothing about private data.

```
https://www.brainstem.org/api/public/stem/session/
```

## HTTP methods

- **GET**: retrieve a list or one record.
- **POST**: create a record.
- **PATCH**: change the fields you send (recommended for updates).
- **PUT**: replace a record completely.
- **DELETE**: delete a record.

## Responses

A list response is an object with the plural response key of the resource and a `meta` object:

```json
{
    "sessions": [ ... ],
    "meta": {"page": 1, "per_page": 100, "total_results": 231, "total_pages": 3}
}
```

A detail, create or update response uses the singular key: `{"session": {...}}`. The keys are listed on each resource page and do not always match the resource name (`data_acquisition`, `consumable_stock`, `anatomical_region`).

Relations are returned as ids. Dates are ISO 8601 strings. Type-specific details are JSON objects validated against the [schema](/api/schemas/) of the selected type.

## Query parameters

### Filtering
{: .no_toc}

```
/?filter{<field>}=<value>
/?filter{<field>.<operator>}=<value>
/?filter{<field>.<related field>}=<value>      (nestable relations only)
```

Operators: `in`, `any`, `all`, `icontains`, `contains`, `startswith`, `istartswith`, `endswith`, `iendswith`, `iexact`, `eq`, `gt`, `gte`, `lt`, `lte`, `range`, `isnull`, `year`, `month`, `day`, `week_day`. No operator means exact match. Repeat the parameter for `in`:

```
/?filter{type.in}=ExtracellularEphys&filter{type.in}=TwoPhotonMicroscopy
```

A filter can follow a relation into the related record only when that relation is **nestable**, that is, when the server lets a query step through it into the related record's fields (marked "nestable" in the field table of each resource page). Any other relation can only be the last segment and is compared with ids:

| Query | Works? |
|---|---|
| `procedure/?filter{subject}=<uuid>` | yes, `subject` is the last segment |
| `procedure/?filter{target_regions.acronym}=CA1` | yes, `target_regions` is nestable |
| `session/?filter{subjects.species}=<uuid>` | yes, `subjects` is nestable |
| `procedure/?filter{equipment.name}=Rig` | no, `equipment` is not nestable; look the equipment up first and filter with `filter{equipment.in}=<ids>` |

Tags are filtered by name: `filter{tags.name}=control` (also `.in` and `.icontains`); records return tags as names. Type-specific `details` cannot be filtered on the server.

### Sorting
{: .no_toc}

```
/?sort[]=name
/?sort[]=-date_time
/?sort[]=-date_time&sort[]=name
```

### Including related records
{: .no_toc}

```
/?include[]=projects.*
/?include[]=dataacquisition.*&include[]=subjects.*
```

Included records are returned next to the main list, under their own plural key ("sideloaded"), not nested inside each record. Only nestable relations can be included; on any other relation `include[]` is ignored and you get ids only. Only records you can read are included, and the relation's id list in that response then shows only those. Read a record without `include[]` before replacing one of its lists. `exclude[]=<field>` drops a field from the response.

### Pagination
{: .no_toc}

Lists are paged with `page` and `per_page`:

- **Default page size**: 100 records
- **Maximum page size**: 500 (larger values are reduced; `meta.per_page` reports the size used)
- `limit` and `offset` are accepted as aliases when `offset` is a multiple of `limit`; other offsets return `400`
- `exclude_count=1` skips the total count for faster responses

```
/?per_page=50&page=3
/?limit=50&offset=100      # the same page
```

Follow `page` up to `meta.total_pages`, or use `load_all` in the Python and MATLAB tools.

### Planned records
{: .no_toc}

Procedures, specimen procedures, sessions and breedings carry a `status` of `planned`, `performed` or `cancelled`. Listings return performed records only unless you add `include_planned=true` or filter on `status` explicitly. The public portal never returns planned records.

### Combining parameters
{: .no_toc}

```
/?filter{projects}=<id>&sort[]=-date_time&include[]=subjects.*&per_page=200
```

## Writing records

- Create with **POST**, update with **PATCH** (send only the fields you change).
- Required fields are listed on each resource page. The server validates with the same rules as the web forms and answers `400` with `{"field": ["message"]}`.
- **Lists replace**: sending `projects`, `subjects`, `equipment`, `target_regions` or `tags` replaces the whole list. Read the record first, change the list, send the full list.
- **JSON payloads replace**: `details` and the coordinate payloads are replaced as a whole. Read, merge, send the full object.
- **Type and payload go together**: `type` picks a schema type and the payload must match it. The resource page names the payload field to send (for example `details` on procedures, `details_json` on material usages). The server sets every `*_schema_version` field itself; do not send one.
- Some records need **form-only inputs** that are not returned in responses, for example `source` on a material usage (inventory, catalog or manual). They are listed under "Form-only inputs" on the resource page.
- Writes to shared taxonomies and catalog resources by users without approval rights create an **approval request** instead of the record.
- Deleting a record that other records still reference returns `400` ("still referenced by ...").

## Other endpoints

| Endpoint | Purpose |
|---|---|
| `GET /api/private/recent-activity/` | What changed lately in records you can read. Parameters `limit` (max 200), `actor_filter`, `action_filter`, `model_type`, `search`, `date_from`, `date_to`, `ownership`, `active_projects_only`. |
| `GET/POST .../stem/project/<id>/export/`, `.../stem/session/<id>/export/` | Project and session exports; see [Exports](/api/export/). |
| `GET .../taxonomies/anatomicalregion/<id>/descendants/` | The regions below a region in its atlas. |
| `GET/PUT .../procedure/<id>/materials/` (also specimen procedures and interfaces) | Read or replace the ordered material usage rows of a record. |
| `POST /api/auth/device/`, `POST /api/auth/device/token/`, `GET /api/auth/token/info/` | Device authorization flow and token information. |
| `GET /reference/`, `GET /schemas/` | The [agent reference](/api/reference/) and the [public schemas](/api/public-schemas/); no token needed. |
| `POST /mcp/` | The [MCP server](/api/mcp/). |

## Error handling

| Status | Meaning | What to do |
|---|---|---|
| `200` / `201` / `204` | success / created / deleted | |
| `400` `{"field": [...]}` | validation failed | fix the named fields |
| `400` `["Invalid nested filter field: x"]` | a filter followed a relation that is not nestable | filter by ids instead |
| `401` | token missing, invalid, expired or revoked | sign in again or create a new token |
| `403` | no permission for this record or action | ask a project manager for the role you need |
| `404` | no such record, or not visible to you | the record may exist in a project you cannot read |
| `409` | stale write (material lists) or export job not ready | re-read and retry, or wait |
| `429` | rate limited | wait and retry; do not loop |

## Rate limits

| Scope | Limit |
|---|---|
| Anonymous requests (public portal) | 60 per minute per IP |
| [Agent reference](/api/reference/) (`/reference/`) and [public schemas](/api/public-schemas/) (`/schemas/`) | 600 per minute per IP, each |
| Authenticated requests | 300 per minute per user |
| Device flow | 10 session starts and 30 polls per minute |
| Exports (direct and background jobs together) | 30 per hour per user |
| MCP messages | 300 per minute |

Requests over the limit receive `429` with a `Retry-After` header.
