---
layout: default
title: Coordinates
parent: Schemas
grand_parent: API
nav_order: 1
---

# Coordinates schemas
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## How to use this page

- Use this page when calling `/api/private/modules/procedure/`.
- Set `coordinates_system` to one schema name from the list below.
- Send `coordinates_details` that matches that schema exactly.
- Also used by `/api/private/modules/equipment/` for equipment location/orientation data.

## Quick type map

| Type value | Schema version | Required fields | Schema shape |
|:-----------|:---------------|:----------------|:-------------|
| `CCF_XYZ_Absolute` | `1.1.0` | none | `object` |
| `External_XYZ_Absolute` | `1.1.0` | none | `object` |
| `Stereotaxic_BregmaAbsolute` | `1.1.0` | none | `object` |
| `Stereotaxic_BregmaBrainSurface` | `1.1.0` | none | `object` |
| `Stereotaxic_LambdaAbsolute` | `1.1.0` | none | `object` |
| `Stereotaxic_LambdaBrainSurface` | `1.1.0` | none | `object` |

## Examples

### Coordinates payload fragment
```json
{
  "coordinates_system": "CCF_XYZ_Absolute",
  "coordinates_details": {
    "x": {
      "unit": "mm",
      "value": 0
    },
    "xAngle": {
      "unit": "°",
      "value": 0
    },
    "y": {
      "unit": "mm",
      "value": 0
    },
    "yAngle": {
      "unit": "°",
      "value": 0
    }
  }
}
```

## Request pattern
```json
{
  "coordinates_system": "CCF_XYZ_Absolute",
  "coordinates_details": {
    "x": {
      "unit": "mm",
      "value": 0
    },
    "xAngle": {
      "unit": "°",
      "value": 0
    },
    "y": {
      "unit": "mm",
      "value": 0
    },
    "yAngle": {
      "unit": "°",
      "value": 0
    }
  }
}
```

## Schema reference

### `CCF_XYZ_Absolute`
- **Schema title:** Common Coordinate Framework XYZ Absolute Coordinates
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Coordinates/CCF_XYZ_Absolute.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "x": {
    "unit": "mm",
    "value": 0
  },
  "xAngle": {
    "unit": "°",
    "value": 0
  },
  "y": {
    "unit": "mm",
    "value": 0
  },
  "yAngle": {
    "unit": "°",
    "value": 0
  }
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `x` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "mm"} |
| `xAngle` | `object(value:number, unit:enum[°])` | no | format="numberUnit"; default={"unit": "°"} |
| `y` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "mm"} |
| `yAngle` | `object(value:number, unit:enum[°])` | no | format="numberUnit"; default={"unit": "°"} |
| `z` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "mm"} |
| `zAngle` | `object(value:number, unit:enum[°])` | no | format="numberUnit"; default={"unit": "°"} |

### `External_XYZ_Absolute`
- **Schema title:** External XYZ Coordinates with Angles
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Coordinates/External_XYZ_Absolute.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "x": {
    "unit": "m",
    "value": 0
  },
  "xAngle": {
    "unit": "°",
    "value": 0
  },
  "y": {
    "unit": "m",
    "value": 0
  },
  "yAngle": {
    "unit": "°",
    "value": 0
  }
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `x` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "m"} |
| `xAngle` | `object(value:number, unit:enum[°])` | no | format="numberUnit"; default={"unit": "°"} |
| `y` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "m"} |
| `yAngle` | `object(value:number, unit:enum[°])` | no | format="numberUnit"; default={"unit": "°"} |
| `z` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "m"} |
| `zAngle` | `object(value:number, unit:enum[°])` | no | format="numberUnit"; default={"unit": "°"} |

### `Stereotaxic_BregmaAbsolute`
- **Schema title:** Stereotaxic Bregma-Based Absolute Coordinates
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Coordinates/Stereotaxic_BregmaAbsolute.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "apCoordinate": {
    "unit": "mm",
    "value": 0
  },
  "apAngle": {
    "unit": "°",
    "value": 0
  },
  "mlCoordinate": {
    "unit": "mm",
    "value": 0
  },
  "mlAngle": {
    "unit": "°",
    "value": 0
  }
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `apAngle` | `object(value:number, unit:enum[°])` | no | format="numberUnit"; default={"unit": "°"} |
| `apCoordinate` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "mm"} |
| `dvAngle` | `object(value:number, unit:enum[°])` | no | format="numberUnit"; default={"unit": "°"} |
| `dvCoordinate` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "mm"} |
| `mlAngle` | `object(value:number, unit:enum[°])` | no | format="numberUnit"; default={"unit": "°"} |
| `mlCoordinate` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "mm"} |

### `Stereotaxic_BregmaBrainSurface`
- **Schema title:** Stereotaxic Bregma-Based Surface Coordinates with Depth
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Coordinates/Stereotaxic_BregmaBrainSurface.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "apCoordinate": {
    "unit": "mm",
    "value": 0
  },
  "apAngle": {
    "unit": "°",
    "value": 0
  },
  "mlCoordinate": {
    "unit": "mm",
    "value": 0
  },
  "mlAngle": {
    "unit": "°",
    "value": 0
  }
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `apAngle` | `object(value:number, unit:enum[°])` | no | format="numberUnit"; default={"unit": "°"} |
| `apCoordinate` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "mm"} |
| `depth` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "mm"} |
| `mlAngle` | `object(value:number, unit:enum[°])` | no | format="numberUnit"; default={"unit": "°"} |
| `mlCoordinate` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "mm"} |
| `rotation` | `object(value:number, unit:enum[°])` | no | format="numberUnit"; default={"unit": "°"} |

### `Stereotaxic_LambdaAbsolute`
- **Schema title:** Stereotaxic Lambda-Based Absolute Coordinates
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Coordinates/Stereotaxic_LambdaAbsolute.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "apCoordinate": {
    "unit": "mm",
    "value": 0
  },
  "apAngle": {
    "unit": "°",
    "value": 0
  },
  "mlCoordinate": {
    "unit": "mm",
    "value": 0
  },
  "mlAngle": {
    "unit": "°",
    "value": 0
  }
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `apAngle` | `object(value:number, unit:enum[°])` | no | format="numberUnit"; default={"unit": "°"} |
| `apCoordinate` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "mm"} |
| `dvAngle` | `object(value:number, unit:enum[°])` | no | format="numberUnit"; default={"unit": "°"} |
| `dvCoordinate` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "mm"} |
| `mlAngle` | `object(value:number, unit:enum[°])` | no | format="numberUnit"; default={"unit": "°"} |
| `mlCoordinate` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "mm"} |

### `Stereotaxic_LambdaBrainSurface`
- **Schema title:** Stereotaxic Lambda-Based Surface Coordinates with Depth
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Coordinates/Stereotaxic_LambdaBrainSurface.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "apCoordinate": {
    "unit": "mm",
    "value": 0
  },
  "apAngle": {
    "unit": "°",
    "value": 0
  },
  "mlCoordinate": {
    "unit": "mm",
    "value": 0
  },
  "mlAngle": {
    "unit": "°",
    "value": 0
  }
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `apAngle` | `object(value:number, unit:enum[°])` | no | format="numberUnit"; default={"unit": "°"} |
| `apCoordinate` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "mm"} |
| `depth` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "mm"} |
| `mlAngle` | `object(value:number, unit:enum[°])` | no | format="numberUnit"; default={"unit": "°"} |
| `mlCoordinate` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "mm"} |
| `rotation` | `object(value:number, unit:enum[°])` | no | format="numberUnit"; default={"unit": "°"} |
