---
layout: default
title: Public schemas
parent: API
nav_order: 9
---
# Public schemas
{: .no_toc}

Every type-specific JSON payload in BrainSTEM is validated against a JSON schema, and every version of every schema is published at a permanent URL. Records store the version they were validated against, exports carry it, and NWB files written by [brainstem-nwb](/tools/brainstem-nwb/) cite the URL, so a payload can always be interpreted, years later, without a BrainSTEM account.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## URLs

| URL | Content | Caching |
|---|---|---|
| `https://www.brainstem.org/schemas/` | index: every family and its types | 1 hour |
| `https://www.brainstem.org/schemas/<Family>/<Type>.json` | the **current** version of a type (what the web forms use), with a `Link: <versioned URL>; rel="canonical"` header | 5 minutes |
| `https://www.brainstem.org/schemas/<Family>/<Type>/` | the published version numbers and the current one | 1 hour |
| `https://www.brainstem.org/schemas/<Family>/<Type>/<version>.json` | one exact version, for example `.../Procedure/VirusInjection/3.0.0.json` | released versions: 1 year, immutable |

No authentication is needed, responses allow cross-origin requests, and the body is the JSON Schema (draft 7) with an `$id` set to its versioned URL. Families and types use the codes shown on the [schema pages](/api/schemas/), for example `Procedure`, `DataAcquisition`, `Coordinates`, `MaterialUsage`, `SpecimenProcedure`.

```bash
curl https://www.brainstem.org/schemas/Procedure/VirusInjection/
# {"family": "Procedure", "type": "VirusInjection", "current": "3.0.0", "versions": ["1.0.0", "1.1.0", "2.0.0", "3.0.0"]}

curl https://www.brainstem.org/schemas/Procedure/VirusInjection/3.0.0.json
```

## Versioning

Each schema carries a `schemaVersion` that follows semantic versioning over the stored data:

| Change | Bump | Example |
|---|---|---|
| Labels, help texts, ordering | patch (`1.0.1`) | a clearer tooltip |
| New optional fields or options | minor (`1.1.0`) | a new unit, a new enum value |
| Previously valid data no longer validates | major (`2.0.0`) | a field renamed or removed, an option made required, enum codes changed |

Rules you can rely on:

- A released version **never changes**. The server keeps a content fingerprint of every published version and refuses edits to it.
- Records store the version they were validated against in a field next to the payload: `type_schema_version` for `details`, `coordinates_schema_version` for coordinates, `details_schema_version` for material usages and stages. Exports include these fields.
- When a major version changes the shape of stored data, BrainSTEM migrates existing records to the new shape and updates their stored version; older versions stay published because exports and NWB files may cite them.
- Types that are retired keep serving their archived versions.
- The change history of every type is kept centrally and the version list endpoint shows which versions exist. The [schema pages](/api/schemas/) on this site show the current version of each type.

## Experimental families

A few schema families are still being refined before their first stable release. Their schemas may change in place without a version bump, and their versions are served with a short cache time. The [schema index](/api/schemas/) marks them as experimental; at the time of writing these are `SpecimenProcedure` and `SpecimenProcedureStage`.

## Using schemas in your own tools

- Validate a payload before sending it: fetch the current schema of the type and run any draft 7 validator over `details`.
- Interpret an exported record: read its `*_schema_version`, fetch `https://www.brainstem.org/schemas/<Family>/<Type>/<version>.json`, and use the `title`, `options.enum_titles` and `options.infoText` of each property for display.
- Quantities are objects `{"value": <number>, "unit": "<code>"}`; the unit codes are the enum of the property's unit definition.
- The [MCP server](/api/mcp/) exposes the same schemas to AI assistants through its `get_schema` tool, and the [agent reference](/api/reference/) links every type to its exact version.

## Terms of use

The schemas are public so that you, your API clients and agents can read and work with BrainSTEM data, but they are not open source. You may read, cache and quote them to validate and write BrainSTEM records, cite a schema by its versioned URL in exports, data papers and repository metadata, and build tools that talk to a BrainSTEM server. Copying the schemas or their vocabularies into another product or standard, mirroring or redistributing the schema tree, or relicensing them needs BrainSTEM's written permission. Every response names the terms in a `Link: rel="license"` header, and every schema served carries a one-line notice in `$comment`. The full terms are at <https://www.brainstem.org/reference/license.md>.
