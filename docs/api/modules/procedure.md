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
| `licenses` | list of related license IDs formatted as strings |
| `details` | JSON object mapped to the internal `type_json` field. *See accepted schemas below* |
| `type_schema_version` | string schema version for `details` |
| `coordinates_system` | string **[required]**. *See options below* |
| `coordinates_details` | JSON object mapped to the internal `coordinates_json` field. *See accepted schemas below* |
| `coordinates_schema_version` | string schema version for `coordinates_details` |
| `created_at` | string containing creation date and time (ISO 8601, read-only) |
| `updated_at` | string containing last update date and time (ISO 8601, read-only) |

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
        'id': '00000000-0000-0000-0000-000000000000',
        'type': 'SiliconProbeImplant',
        'notes': 'acute implant',
        'subject': '00000000-0000-0000-0000-000000000000',
        'date_time': '2024-03-12T09:00:00Z',
        'consumablestock': '00000000-0000-0000-0000-000000000000',
        'equipment': ['00000000-0000-0000-0000-000000000000'],
        'licenses': ['00000000-0000-0000-0000-000000000000'],
        'details': {
            'probeId': 'SP-64A',
            'sterilizationMethod': 'Ethylene Oxide'
        },
        'type_schema_version': '0.0.0',
        'brain_region': '00000000-0000-0000-0000-000000000000',
        'coordinates_system': 'Stereotaxic_BregmaAbsolute',
        'coordinates_details': {
            'apCoordinate': -2.5,
            'mlCoordinate': 1.5,
            'dvCoordinate': -1.0,
            'apAngle': 0.0,
            'mlAngle': 10.0,
            'dvAngle': 0.0
        },
        'coordinates_schema_version': '0.0.0',
        'created_at': '2024-03-12T09:00:00Z',
        'updated_at': '2024-03-12T09:00:00Z'
    },
    {
        'id': '00000000-0000-0000-0000-000000000000',
        'type': 'OpticFiberImplant',
        'notes': 'bilateral implant',
        'subject': '00000000-0000-0000-0000-000000000000',
        'date_time': None,
        'consumablestock': None,
        'equipment': [],
        'licenses': [],
        'details': {
            'fiberTipShape': 'flat',
            'fiberId': 'OF-L-2024-07',
            'sterilizationMethod': 'Autoclave'
        },
        'type_schema_version': '0.0.0',
        'brain_region': '00000000-0000-0000-0000-000000000000',
        'coordinates_system': 'Stereotaxic_BregmaBrainSurface',
        'coordinates_details': {
            'apCoordinate': -2.8,
            'mlCoordinate': 1.2,
            'surfaceDepth': -0.5,
            'apAngle': 0.0,
            'mlAngle': 5.0
        },
        'coordinates_schema_version': '0.0.0',
        'created_at': '2024-03-12T09:05:00Z',
        'updated_at': '2024-03-12T09:05:00Z'
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
        "subject": "00000000-0000-0000-0000-000000000000",
        "consumablestock": "00000000-0000-0000-0000-000000000000",
        "equipment": ["00000000-0000-0000-0000-000000000000"],
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
    'id': '00000000-0000-0000-0000-000000000000',
    'type': 'OpticFiberImplant',
    'notes': 'bilateral implant',
    'subject': '00000000-0000-0000-0000-000000000000',
    'date_time': None,
    'consumablestock': '00000000-0000-0000-0000-000000000000',
    'equipment': ['00000000-0000-0000-0000-000000000000'],
    'licenses': [],
    'details': {'fiberTipShape': 'flat', 'fiberId': 'OF-L-2024-07', 'sterilizationMethod': 'Autoclave'},
    'type_schema_version': '0.0.0',
    'brain_region': None,
    'coordinates_system': 'Stereotaxic_BregmaAbsolute',
    'coordinates_details': {
        "apCoordinate": -2.8,
        "mlCoordinate": 1.2,
        "dvCoordinate": -2.5,
        "apAngle": 0.0,
        "mlAngle": 5.0,
        "dvAngle": 0.0
    },
    'coordinates_schema_version': '0.0.0',
    'created_at': '2024-03-12T09:00:00Z',
    'updated_at': '2024-03-12T09:00:00Z'
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
resp = client.load_model('procedure', id='00000000-0000-0000-0000-000000000000')
```

### Response example
{: .no_toc}

```
{'procedure': {
    'id': '00000000-0000-0000-0000-000000000000',
    'type': 'OpticFiberImplant',
    'notes': 'bilateral implant',
    'subject': '00000000-0000-0000-0000-000000000000',
    'date_time': None,
    'consumablestock': '00000000-0000-0000-0000-000000000000',
    'equipment': ['00000000-0000-0000-0000-000000000000'],
    'licenses': [],
    'details': {'fiberTipShape': 'flat', 'fiberId': 'OF-L-2024-07', 'sterilizationMethod': 'Autoclave'},
    'type_schema_version': '0.0.0',
    'brain_region': None,
    'coordinates_system': 'Stereotaxic_BregmaAbsolute',
    'coordinates_details': {
        "apCoordinate": -2.8,
        "mlCoordinate": 1.2,
        "dvCoordinate": -2.5,
        "apAngle": 0.0,
        "mlAngle": 5.0,
        "dvAngle": 0.0
    },
    'coordinates_schema_version': '0.0.0',
    'created_at': '2024-03-12T09:00:00Z',
    'updated_at': '2024-03-12T09:00:00Z'
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
    id="00000000-0000-0000-0000-000000000000",
    data={"notes": "implant tightened"}
)
```

### Response example
{: .no_toc}

```
{'procedure': {
    'id': '00000000-0000-0000-0000-000000000000',
    'type': 'OpticFiberImplant',
    'notes': 'implant tightened',
    'subject': '00000000-0000-0000-0000-000000000000',
    'date_time': None,
    'consumablestock': '00000000-0000-0000-0000-000000000000',
    'equipment': ['00000000-0000-0000-0000-000000000000'],
    'licenses': [],
    'details': {'fiberTipShape': 'flat', 'fiberId': 'OF-L-2024-07', 'sterilizationMethod': 'Autoclave'},
    'type_schema_version': '0.0.0',
    'brain_region': None,
    'coordinates_system': 'Stereotaxic_BregmaAbsolute',
    'coordinates_details': {
        "apCoordinate": -2.8,
        "mlCoordinate": 1.2,
        "dvCoordinate": -2.5,
        "apAngle": 0.0,
        "mlAngle": 5.0,
        "dvAngle": 0.0
    },
    'coordinates_schema_version': '0.0.0',
    'created_at': '2024-03-12T09:00:00Z',
    'updated_at': '2024-03-12T09:05:00Z'
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
resp = client.delete_model("procedure", id="00000000-0000-0000-0000-000000000000")
```
