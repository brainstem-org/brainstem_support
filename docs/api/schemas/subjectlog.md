---
layout: default
title: SubjectLog
parent: Schemas
grand_parent: API
nav_order: 8
---

# SubjectLog schemas
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## How to use this page

- Use this page when calling `/api/private/modules/subjectlog/`.
- Set `type` to one schema name from the list below.
- Send `details` that matches that schema exactly.
- Schema controls shape of per-log-type observations and metrics.

## Quick type map

| Type value | Schema version | Required fields | Schema shape |
|:-----------|:---------------|:----------------|:-------------|
| `FoodConsumption` | `1.1.0` | `foodAmount` | `object` |
| `FoodDeprivation` | `1.0.0` | `responsiblePerson` | `object` |
| `GenericObservation` | `1.0.0` | `observation`, `observationType` | `object` |
| `Genotyping` | `1.0.0` | `result`, `sample` | `object` |
| `Habituation` | `1.0.0` | none | `object` |
| `Handling` | `1.0.0` | none | `object` |
| `HargreavesTest` | `1.1.0` | `latency`, `responseScore`, `stimulusLocation` | `object` |
| `Housing` | `1.0.0` | none | `object` |
| `TrainingSession` | `1.0.0` | none | `object` |
| `VonFreyTest` | `1.1.0` | `responseScore`, `stimulusForce`, `stimulusLocation` | `object` |
| `WaterConsumption` | `1.1.0` | `waterAmount` | `object` |
| `WaterDeprivation` | `1.0.0` | `responsiblePerson` | `object` |
| `Weighing` | `1.1.0` | `weight` | `object` |
| `Wellness` | `1.0.0` | `wellness` | `object` |

## Examples

### SubjectLog payload fragment
```json
{
  "type": "FoodConsumption",
  "details": {
    "foodAmount": {
      "unit": "g",
      "value": 0
    }
  }
}
```

## Request pattern
```json
{
  "type": "FoodConsumption",
  "details": {
    "foodAmount": {
      "unit": "g",
      "value": 0
    }
  }
}
```

## Schema reference

### `FoodConsumption`
- **Schema title:** Food Consumption log
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/SubjectLog/FoodConsumption.json`
- **Schema shape:** `object`
- **Required fields:** `foodAmount`

Example payload for this type:
```json
{
  "foodAmount": {
    "unit": "g",
    "value": 0
  }
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `foodAmount` | `object(value:number, unit:enum[kg, g, mg, µg])` | yes | format="numberUnit"; default={"unit": "g"} |

### `FoodDeprivation`
- **Schema title:** Food deprivation log
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/SubjectLog/FoodDeprivation.json`
- **Schema shape:** `object`
- **Required fields:** `responsiblePerson`

Example payload for this type:
```json
{
  "responsiblePerson": "example"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `protocol` | `string` | no | — |
| `responsiblePerson` | `string` | yes | — |

### `GenericObservation`
- **Schema title:** Generic Observation
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/SubjectLog/GenericObservation.json`
- **Schema shape:** `object`
- **Required fields:** `observation`, `observationType`

Example payload for this type:
```json
{
  "observation": "example",
  "observationType": "Pain score"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `observation` | `string` | yes | — |
| `observationType` | `string` | yes | enum=["Pain score", "Grooming", "Exploration", "Freezing", "Facial expression", "Unusual behavior", "Other"] |
| `repetitions` | `integer` | no | minimum=1; default=1 |

### `Genotyping`
- **Schema title:** Genotyping
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/SubjectLog/Genotyping.json`
- **Schema shape:** `object`
- **Required fields:** `result`, `sample`

Example payload for this type:
```json
{
  "result": "example",
  "sample": "example"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `assayPanel` | `string` | no | — |
| `lociResults` | `array` | no | format="table" |
| `qcConfidence` | `string` | no | enum=["high", "medium", "low", "ambiguous", "failed"] |
| `result` | `string` | yes | — |
| `sample` | `string` | yes | — |

### `Habituation`
- **Schema title:** Habituation log
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/SubjectLog/Habituation.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "habituationMethod": "example"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `habituationMethod` | `string` | no | — |

### `Handling`
- **Schema title:** Handling log
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/SubjectLog/Handling.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "handlingMethod": "example"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `handlingMethod` | `string` | no | — |

### `HargreavesTest`
- **Schema title:** Hargreaves Thermal sensitivity test
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/SubjectLog/HargreavesTest.json`
- **Schema shape:** `object`
- **Required fields:** `latency`, `responseScore`, `stimulusLocation`

Example payload for this type:
```json
{
  "latency": {
    "unit": "s",
    "value": 0
  },
  "responseScore": 0,
  "stimulusLocation": "Left hind paw"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `cutoffLatency` | `object(value:number, unit:enum[µs, ms, s, min, h])` | no | format="numberUnit"; default={"unit": "s"} |
| `latency` | `object(value:number, unit:enum[µs, ms, s, min, h])` | yes | format="numberUnit"; default={"unit": "s"} |
| `repetitions` | `integer` | no | minimum=1; default=3 |
| `responseScore` | `integer` | yes | enum=[0, 1, 2, 3]; minimum=0; maximum=3 |
| `stimulusLocation` | `string` | yes | enum=["Left hind paw", "Right hind paw", "Left forepaw", "Right forepaw", "Face (left)", "Face (right)", "Tail", "Other"] |

### `Housing`
- **Schema title:** Housing log
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/SubjectLog/Housing.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "location": "example",
  "cageId": "example",
  "cageType": "example",
  "lightCycle": "example"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `cageId` | `string` | no | — |
| `cageType` | `string` | no | — |
| `enrichment` | `string` | no | — |
| `lightCycle` | `string` | no | — |
| `location` | `string` | no | — |

### `TrainingSession`
- **Schema title:** Training session log
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/SubjectLog/TrainingSession.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "task": "example",
  "setup": "example",
  "reinforcementType": "example",
  "performance": "example"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `performance` | `string` | no | — |
| `reinforcementType` | `string` | no | — |
| `setup` | `string` | no | — |
| `task` | `string` | no | — |

### `VonFreyTest`
- **Schema title:** Von Frey Mechanical sensitivity test
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/SubjectLog/VonFreyTest.json`
- **Schema shape:** `object`
- **Required fields:** `responseScore`, `stimulusForce`, `stimulusLocation`

Example payload for this type:
```json
{
  "responseScore": 0,
  "stimulusForce": {
    "unit": "g",
    "value": 0
  },
  "stimulusLocation": "Left hind paw"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `repetitions` | `integer` | no | minimum=1; default=10 |
| `responseScore` | `integer` | yes | enum=[0, 1, 2, 3]; minimum=0; maximum=3 |
| `stimulusForce` | `object(value:number, unit:enum[mg, g, kg])` | yes | format="numberUnit"; default={"unit": "g"} |
| `stimulusLocation` | `string` | yes | enum=["Left hind paw", "Right hind paw", "Left forepaw", "Right forepaw", "Face (left)", "Face (right)", "Tail", "Other"] |

### `WaterConsumption`
- **Schema title:** Water consumption log
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/SubjectLog/WaterConsumption.json`
- **Schema shape:** `object`
- **Required fields:** `waterAmount`

Example payload for this type:
```json
{
  "waterAmount": {
    "unit": "mL",
    "value": 0
  }
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `waterAmount` | `object(value:number, unit:enum[L, mL, µL, nL, pL])` | yes | format="numberUnit"; default={"unit": "mL"} |

### `WaterDeprivation`
- **Schema title:** Water deprivation log
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/SubjectLog/WaterDeprivation.json`
- **Schema shape:** `object`
- **Required fields:** `responsiblePerson`

Example payload for this type:
```json
{
  "responsiblePerson": "example"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `protocol` | `string` | no | — |
| `responsiblePerson` | `string` | yes | — |

### `Weighing`
- **Schema title:** Weighing log
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/SubjectLog/Weighing.json`
- **Schema shape:** `object`
- **Required fields:** `weight`

Example payload for this type:
```json
{
  "weight": {
    "unit": "g",
    "value": 0
  }
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `weight` | `object(value:number, unit:enum[kg, g, mg, µg])` | yes | format="numberUnit"; default={"unit": "g"} |

### `Wellness`
- **Schema title:** Wellness log
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/SubjectLog/Wellness.json`
- **Schema shape:** `object`
- **Required fields:** `wellness`

Example payload for this type:
```json
{
  "wellness": "example"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `wellness` | `string` | yes | — |
