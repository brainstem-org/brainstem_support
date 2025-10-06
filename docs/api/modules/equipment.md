---
layout: default
title: Equipment
parent: Modules
grand_parent: API
nav_order: 4
---

# Equipment API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `name` | descriptive name for the equipment |
| `type` | string **[required]**. *See options below* |
| `notes` | string [max length: 500] |
| `setup` | related experimental setup ID formatted as a string **[required]** |
| `date_time` | string containing date and time (ISO 8601) |
| `consumable` | related consumable ID formatted as a string |
| `hardwaredevice` | related hardware device ID formatted as a string |
| `details` | JSON object mapped to the internal `type_json` field. *See accepted schemas below* |
| `coordinates_system` | string **[required]**. *See options below* |
| `coordinates_details` | JSON object mapped to the internal `coordinates_json` field. *See accepted schemas below* |

Most equipment schemas currently expose no additional fields, so the API may return an empty `{}` for `details` unless new properties are defined.


## Types of equipment

A detailed list of the available `type` options and accepted schemas for the `details` and `coordinates_details` fields can be found in the [Equipment schemas documentation](/api/schemas/equipment) and [Coordinates schemas documentation](/api/schemas/coordinates).




## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/equipment
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('equipment')
```

### Response example
{: .no_toc}

```
{'equipment': [
    {
        'id': 'f79d84c8-6bec-40e3-b18a-5b25e57f4a09',
        'name': 'Headstage amplifier',
        'type': 'Amplifier',
        'notes': '32-channel preamp',
        'setup': '0f87c229-6769-4854-83a5-c71e154246b8',
        'date_time': '2024-03-05T10:00:00Z',
        'consumable': None,
        'hardwaredevice': 'c18df269-5d38-4f3d-9509-1431d0f5d4ff',
        'details': {},
        'coordinates_system': 'External_XYZ_Absolute',
        'coordinates_details': {
            'x': 0.0,
            'y': 0.0,
            'z': 0.0,
            'xAngle': 0.0,
            'yAngle': 0.0,
            'zAngle': 0.0
        }
    },
    {
        'id': 'a18dd2b1-6393-468c-9424-1bc77b9e4976',
        'name': 'Two-photon rig',
        'type': 'TwoPhotonMicroscope',
        'notes': 'Imaging setup',
        'setup': '0f87c229-6769-4854-83a5-c71e154246b8',
        'date_time': None,
        'consumable': None,
        'hardwaredevice': None,
        'details': {},
        'coordinates_system': 'External_XYZ_Absolute',
        'coordinates_details': {
            'x': 120.0,
            'y': 45.0,
            'z': 0.0,
            'xAngle': 0.0,
            'yAngle': 0.0,
            'zAngle': 0.0
        }
    }
]}
```


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/modules/equipment
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model(
    "equipment",
    data={
        "name": "Fiber photometry console",
        "type": "FiberPhotometrySystem",
        "setup": "0f87c229-6769-4854-83a5-c71e154246b8",
        "hardwaredevice": "c18df269-5d38-4f3d-9509-1431d0f5d4ff",
        "notes": "Main recording rig",
        "details": {},
        "coordinates_system": "External_XYZ_Absolute",
        "coordinates_details": {
            "x": 1.0,
            "y": 2.0,
            "z": 3.0,
            "xAngle": 4.0,
            "yAngle": 5.0,
            "zAngle": 6.0
        }
    }
)
```

### Response example
{: .no_toc}

```
{'equipment': {
    'id': 'd37c9255-d5ae-47d9-b6e1-4ec760c200fb',
    'name': 'Fiber photometry console',
    'type': 'FiberPhotometrySystem',
    'notes': 'Main recording rig',
    'setup': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'consumable': None,
    'hardwaredevice': 'c18df269-5d38-4f3d-9509-1431d0f5d4ff',
    'details': {},
    'coordinates_system': 'External_XYZ_Absolute',
    'coordinates_details': {
        'x': 1.0,
        'y': 2.0,
        'z': 3.0,
        'xAngle': 4.0,
        'yAngle': 5.0,
        'zAngle': 6.0
    }
}}
```


## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/equipment/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('equipment', id='d37c9255-d5ae-47d9-b6e1-4ec760c200fb')
```

### Response example
{: .no_toc}

```
{'equipment': {
    'id': 'd37c9255-d5ae-47d9-b6e1-4ec760c200fb',
    'name': 'Fiber photometry console',
    'type': 'FiberPhotometrySystem',
    'notes': 'Main recording rig',
    'setup': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'consumable': None,
    'hardwaredevice': 'c18df269-5d38-4f3d-9509-1431d0f5d4ff',
    'details': {},
    'coordinates_system': 'External_XYZ_Absolute',
    'coordinates_details': {
        'x': 1.0,
        'y': 2.0,
        'z': 3.0,
        'xAngle': 4.0,
        'yAngle': 5.0,
        'zAngle': 6.0
    }
}}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/equipment/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model(
    "equipment",
    id="d37c9255-d5ae-47d9-b6e1-4ec760c200fb",
    data={"notes": "Updated calibration complete"}
)
```

### Response example
{: .no_toc}

```
{'equipment': {
    'id': 'd37c9255-d5ae-47d9-b6e1-4ec760c200fb',
    'name': 'Fiber photometry console',
    'type': 'FiberPhotometrySystem',
    'notes': 'Updated calibration complete',
    'setup': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'consumable': None,
    'hardwaredevice': 'c18df269-5d38-4f3d-9509-1431d0f5d4ff',
    'details': {},
    'coordinates_system': 'External_XYZ_Absolute',
    'coordinates_details': {
        'x': 1.0,
        'y': 2.0,
        'z': 3.0,
        'xAngle': 4.0,
        'yAngle': 5.0,
        'zAngle': 6.0
    }
}}
```

## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/modules/equipment/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("equipment", id="d37c9255-d5ae-47d9-b6e1-4ec760c200fb")
```
