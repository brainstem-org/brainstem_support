---
layout: default
title: Schemas
parent: API
nav_order: 8
has_children: true
has_toc: false
---

# Schemas

Use this section when an endpoint asks for `type`/`details` or `coordinates_system`/`coordinates_details`.

## How schemas relate to API calls
- A module endpoint validates the JSON fragment in `details` (or `coordinates_details`) against a schema chosen by `type` (or `coordinates_system`).
- If fields do not match the selected schema, the API returns `400 Bad request` with validation errors.
- Always send the selector and payload pair together in create/update calls.

## Schema groups

| Group | Used by endpoint(s) | Selector field | Payload field |
|:------|:--------------------|:---------------|:--------------|
| [Coordinates](/api/schemas/coordinates/) | `/api/private/modules/procedure/` | `coordinates_system` | `coordinates_details` |
| [ConsumableStock](/api/schemas/consumablestock/) | `/api/private/modules/consumablestock/` | `type` | `details` |
| [DataAcquisition](/api/schemas/dataacquisition/) | `/api/private/modules/dataacquisition/` | `type` | `details` |
| [Equipment](/api/schemas/equipment/) | `/api/private/modules/equipment/` | `type` | `details` |
| [Manipulation](/api/schemas/manipulation/) | `/api/private/modules/manipulation/` | `type` | `details` |
| [Procedure](/api/schemas/procedure/) | `/api/private/modules/procedure/` | `type` | `details` |
| [ProcedureLog](/api/schemas/procedurelog/) | `/api/private/modules/procedurelog/` | `type` | `details` |
| [SubjectLog](/api/schemas/subjectlog/) | `/api/private/modules/subjectlog/` | `type` | `details` |

## Validation troubleshooting
- `type` or `coordinates_system` not recognized: use one value from the target schema page quick map.
- Missing required field: add all fields listed under `Required fields` for that schema.
- Wrong nested shape: check whether field expects scalar (`string`, `number`) vs object (`value` + `unit`) or array rows.
- Unit mismatch: use one of the unit enum values documented in constraints.
