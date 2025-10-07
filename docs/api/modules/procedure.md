---
layout: default
title: Procedure
parent: Modules
grand_parent: API
nav_order: 6
---

# Procedure API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `type` | string **[required]**. *See options below* |
| `notes` | string [max length: 500] |
| `subject` | related subject ID formatted as a string **[required]** |
| `date_time` | string containing date and time (ISO 8601) |
| `consumablestock` | related consumable stock ID formatted as a string |
| `equipment` | list of related equipment IDs formatted as strings |
| `brain_region` | related brain region ID formatted as a string |
| `details` | JSON object mapped to the internal `type_json` field. *See accepted schemas below* |
| `coordinates_system` | string **[required]**. *See options below* |
| `coordinates_details` | JSON object mapped to the internal `coordinates_json` field. *See accepted schemas below* |

## Types of procedure

A detailed list of the available `type` options and accepted schemas for the `details` and `coordinates_details` fields can be found in the [Procedure schemas documentation](/api/schemas/procedure) and [Coordinates schemas documentation](/api/schemas/coordinates).




## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/procedure
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('procedure')
```

### Response example
{: .no_toc}

```
{'procedures': [
    {
        'id': 'f79d84c8-6bec-40e3-b18a-5b25e57f4a09',
        'type': 'SiliconProbeImplant',
        'notes': 'acute implant',
        'subject': '0f87c229-6769-4854-83a5-c71e154246b8',
        'date_time': '2024-03-12T09:00:00Z',
        'consumablestock': 'a5f29099-2758-4163-a8e4-e5e2898e57b2',
        'equipment': ['5b032f95-3f5b-4a27-9680-5f8f671dba22'],
        'details': {
            'probeId': 'SP-64A',
            'sterilizationMethod': 'Ethylene Oxide'
        },
        'brain_region': '15f9aef5-2d46-4ff2-a0db-ac6be759c05c',
        'coordinates_system': 'Stereotaxic_BregmaAbsolute',
        'coordinates_details': {
            'apCoordinate': -2.5,
            'mlCoordinate': 1.5,
            'dvCoordinate': -1.0,
            'apAngle': 0.0,
            'mlAngle': 10.0,
            'dvAngle': 0.0
        }
    },
    {
        'id': 'a18dd2b1-6393-468c-9424-1bc77b9e4976',
        'type': 'OpticFiberImplant',
        'notes': 'bilateral implant',
        'subject': '0f87c229-6769-4854-83a5-c71e154246b8',
        'date_time': None,
        'consumablestock': None,
        'equipment': [],
        'details': {
            'fiberTipShape': 'flat',
            'fiberId': 'OF-L-2024-07',
            'sterilizationMethod': 'Autoclave'
        },
        'brain_region': '15f9aef5-2d46-4ff2-a0db-ac6be759c05c',
        'coordinates_system': 'Stereotaxic_BregmaBrainSurface',
        'coordinates_details': {
            'apCoordinate': -2.8,
            'mlCoordinate': 1.2,
            'surfaceDepth': -0.5,
            'apAngle': 0.0,
            'mlAngle': 5.0
        }
    }
]}
```


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/modules/procedure
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model(
    "procedure",
    data={
        "type": "OpticFiberImplant",
        "subject": "0f87c229-6769-4854-83a5-c71e154246b8",
        "consumablestock": "a5f29099-2758-4163-a8e4-e5e2898e57b2",
        "equipment": ["5b032f95-3f5b-4a27-9680-5f8f671dba22"],
        "notes": "bilateral implant",
        "details": {"fiberTipShape": "flat", "fiberId": "OF-L-2024-07", "sterilizationMethod": "Autoclave"},
        "coordinates_system": "Stereotaxic_BregmaAbsolute",
        "coordinates_details": {
            "apCoordinate": -2.8,
            "mlCoordinate": 1.2,
            "dvCoordinate": -2.5,
            "apAngle": 0.0,
            "mlAngle": 5.0,
            "dvAngle": 0.0
        }
    }
)
```

### Response example
{: .no_toc}

```
{'procedure': {
    'id': 'd37c9255-d5ae-47d9-b6e1-4ec760c200fb',
    'type': 'OpticFiberImplant',
    'notes': 'bilateral implant',
    'subject': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'consumablestock': 'a5f29099-2758-4163-a8e4-e5e2898e57b2',
    'equipment': ['5b032f95-3f5b-4a27-9680-5f8f671dba22'],
    'details': {'fiberTipShape': 'flat', 'fiberId': 'OF-L-2024-07', 'sterilizationMethod': 'Autoclave'},
    'brain_region': None,
    'coordinates_system': 'Stereotaxic_BregmaAbsolute',
    'coordinates_details': {
        "apCoordinate": -2.8,
        "mlCoordinate": 1.2,
        "dvCoordinate": -2.5,
        "apAngle": 0.0,
        "mlAngle": 5.0,
        "dvAngle": 0.0
    }
}}
```



## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/procedure/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('procedure', id='d37c9255-d5ae-47d9-b6e1-4ec760c200fb')
```

### Response example
{: .no_toc}

```
{'procedure': {
    'id': 'd37c9255-d5ae-47d9-b6e1-4ec760c200fb',
    'type': 'OpticFiberImplant',
    'notes': 'bilateral implant',
    'subject': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'consumablestock': 'a5f29099-2758-4163-a8e4-e5e2898e57b2',
    'equipment': ['5b032f95-3f5b-4a27-9680-5f8f671dba22'],
    'details': {'fiberTipShape': 'flat', 'fiberId': 'OF-L-2024-07', 'sterilizationMethod': 'Autoclave'},
    'brain_region': None,
    'coordinates_system': 'Stereotaxic_BregmaAbsolute',
    'coordinates_details': {
        "apCoordinate": -2.8,
        "mlCoordinate": 1.2,
        "dvCoordinate": -2.5,
        "apAngle": 0.0,
        "mlAngle": 5.0,
        "dvAngle": 0.0
    }
}}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/procedure/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model(
    "procedure",
    id="d37c9255-d5ae-47d9-b6e1-4ec760c200fb",
    data={"notes": "implant tightened"}
)
```

### Response example
{: .no_toc}

```
{'procedure': {
    'id': 'd37c9255-d5ae-47d9-b6e1-4ec760c200fb',
    'type': 'OpticFiberImplant',
    'notes': 'implant tightened',
    'subject': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'consumablestock': 'a5f29099-2758-4163-a8e4-e5e2898e57b2',
    'equipment': ['5b032f95-3f5b-4a27-9680-5f8f671dba22'],
    'details': {'fiberTipShape': 'flat', 'fiberId': 'OF-L-2024-07', 'sterilizationMethod': 'Autoclave'},
    'brain_region': None,
    'coordinates_system': 'Stereotaxic_BregmaAbsolute',
    'coordinates_details': {
        "apCoordinate": -2.8,
        "mlCoordinate": 1.2,
        "dvCoordinate": -2.5,
        "apAngle": 0.0,
        "mlAngle": 5.0,
        "dvAngle": 0.0
    }
}}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/modules/procedure/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("procedure", id="d37c9255-d5ae-47d9-b6e1-4ec760c200fb")
```
