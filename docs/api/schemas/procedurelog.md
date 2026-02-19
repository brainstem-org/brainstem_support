---
layout: default
title: ProcedureLog
parent: Schemas
grand_parent: API
nav_order: 7
---

# ProcedureLog schemas
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## How to use this page

- Use this page when calling `/api/private/modules/procedurelog/`.
- Set `type` to one schema name from the list below.
- Send `details` that matches that schema exactly.
- Schema controls shape of per-log-type measurements.

## Quick type map

| Type value | Schema version | Required fields | Schema shape |
|:-----------|:---------------|:----------------|:-------------|
| `Impedances` | `1.0.1` | `impedances` | `object` |
| `LinearDisplacement` | `1.1.0` | `displacement` | `object` |
| `Tetrodes4` | `1.1.0` | none | `object` |
| `Tetrodes8` | `1.1.0` | none | `object` |

## Examples

### ProcedureLog payload fragment
```json
{
  "type": "Impedances",
  "details": {
    "impedances": []
  }
}
```

## Request pattern
```json
{
  "type": "Impedances",
  "details": {
    "impedances": []
  }
}
```

## Schema reference

### `Impedances`
- **Schema title:** Impedances
- **Schema version:** `1.0.1`
- **Source:** `brainstem/schemas/ProcedureLog/Impedances.json`
- **Schema shape:** `object`
- **Required fields:** `impedances`

Example payload for this type:
```json
{
  "impedances": []
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `channels` | `array` | no | — |
| `impedances` | `array` | yes | minItems=1 |
| `phases` | `array` | no | — |

### `LinearDisplacement`
- **Schema title:** Linear displacement
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/ProcedureLog/LinearDisplacement.json`
- **Schema shape:** `object`
- **Required fields:** `displacement`

Example payload for this type:
```json
{
  "displacement": {
    "unit": "µm",
    "value": 0
  }
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `displacement` | `object(value:number, unit:enum[nm, µm, mm, cm, m])` | yes | format="numberUnit"; default={"unit": "µm"} |

### `Tetrodes4`
- **Schema title:** Tetrode log (4 tetrodes)
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/ProcedureLog/Tetrodes4.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "tetrode_1": {
    "unit": "µm",
    "value": 0
  },
  "tetrode_2": {
    "unit": "µm",
    "value": 0
  },
  "tetrode_3": {
    "unit": "µm",
    "value": 0
  },
  "tetrode_4": {
    "unit": "µm",
    "value": 0
  }
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `tetrode_1` | `object(value:number, unit:enum[nm, µm, mm, cm, m])` | no | format="numberUnit"; default={"unit": "µm"} |
| `tetrode_2` | `object(value:number, unit:enum[nm, µm, mm, cm, m])` | no | format="numberUnit"; default={"unit": "µm"} |
| `tetrode_3` | `object(value:number, unit:enum[nm, µm, mm, cm, m])` | no | format="numberUnit"; default={"unit": "µm"} |
| `tetrode_4` | `object(value:number, unit:enum[nm, µm, mm, cm, m])` | no | format="numberUnit"; default={"unit": "µm"} |

### `Tetrodes8`
- **Schema title:** Tetrode log (8 tetrodes)
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/ProcedureLog/Tetrodes8.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "tetrode_1": {
    "unit": "µm",
    "value": 0
  },
  "tetrode_2": {
    "unit": "µm",
    "value": 0
  },
  "tetrode_3": {
    "unit": "µm",
    "value": 0
  },
  "tetrode_4": {
    "unit": "µm",
    "value": 0
  }
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `tetrode_1` | `object(value:number, unit:enum[nm, µm, mm, cm, m])` | no | format="numberUnit"; default={"unit": "µm"} |
| `tetrode_2` | `object(value:number, unit:enum[nm, µm, mm, cm, m])` | no | format="numberUnit"; default={"unit": "µm"} |
| `tetrode_3` | `object(value:number, unit:enum[nm, µm, mm, cm, m])` | no | format="numberUnit"; default={"unit": "µm"} |
| `tetrode_4` | `object(value:number, unit:enum[nm, µm, mm, cm, m])` | no | format="numberUnit"; default={"unit": "µm"} |
| `tetrode_5` | `object(value:number, unit:enum[nm, µm, mm, cm, m])` | no | format="numberUnit"; default={"unit": "µm"} |
| `tetrode_6` | `object(value:number, unit:enum[nm, µm, mm, cm, m])` | no | format="numberUnit"; default={"unit": "µm"} |
| `tetrode_7` | `object(value:number, unit:enum[nm, µm, mm, cm, m])` | no | format="numberUnit"; default={"unit": "µm"} |
| `tetrode_8` | `object(value:number, unit:enum[nm, µm, mm, cm, m])` | no | format="numberUnit"; default={"unit": "µm"} |
