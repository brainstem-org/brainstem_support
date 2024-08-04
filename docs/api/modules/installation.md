---
layout: default
title: Installation
parent: Modules
grand_parent: API
nav_order: 1
---

# Installation API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `experimentalsetup` | related experimental setup ID formatted as a string **[required]** |
| `type` | string **[required]**. *See options below* |
| `description` | string [max length: 500] |
| `date_time` | string containing date (e.g. "2023-03-22") |
| `consumable` | related consumable ID formatted as a string |
| `hardwaredevice` | related hardware device ID formatted as a string |
| `coordinates_system` | string **[required]**. *See options below* |
| `coordinates_details` | JSON object. *See accepted schemas below* |


These are the available `type` options for Installation:
- `CameraInstallation`
- `InfraredCamera`
- `Microphone`
- `PressureSensor`
- `Thermostat`


A detailed list of the accepted schemas for the `details` field, related to each `type`, can be found in the [installation schemas page]({{"/api/schemas/installations/"|absolute_url}}).


These are the available `coordinates_system` options for Installation:
- `External_XYZ_Absolute`

A detailed list of the accepted schemas for the `coordinates_details` field, related to each `coordinates_system`, can be found in the [Coordinates schemas page]({{"api/schemas/coordinates/"|absolute_url}}).


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/installation
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('installation')
```

### Response example
{: .no_toc}

```
{'installations': [
    {
        'id': 'f79d84c8-6bec-40e3-b18a-5b25e57f4a09',
        'type': 'TetrodeWireElectrode',
        'description': 'First implant',
        'experimentalsetup': '0f87c229-6769-4854-83a5-c71e154246b8',
        'date_time': None,
        'consumable': 'a5f29099-2758-4163-a8e4-e5e2898e57b2',
        'hardwaredevice': None,
        'details': {
            'tetrodeCount': 1,
            'nWiresTetrode': 4,
            'wireDiameter': 33.9,
            'wireMaterial': 'tunsgten'
        },
        'coordinates_system': 'External_XYZ_Absolute',
        'coordinates_details': {
            'apCoordinate': 1.0
        }
    },
    {
        'id': 'a18dd2b1-6393-468c-9424-1bc77b9e4976',
        'type': 'TetrodeWireElectrode',
        'description': 'Second implant',
        'experimentalsetup': '0f87c229-6769-4854-83a5-c71e154246b8',
        'date_time': None,
        'consumable': None,
        'hardwaredevice': None,
        'details': {
            'tetrodeCount': 1,
            'nWiresTetrode': 4,
            'wireDiameter': 33.9,
            'wireMaterial': 'tunsgten'
        },
        'coordinates_system': 'External_XYZ_Absolute',
        'coordinates_details': {
            'x': 1.0,
            'y': 0.0,
            'xAngle': 2.0
        }
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/modules/installation
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("installation",  data={
    "type": "OpticFiberImplant",
    "experimentalsetup": "0f87c229-6769-4854-83a5-c71e154246b8",
    "description": "some text",
    "details": {"fiberTipShape": "flat"},
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
{'installation': {
    'id': 'd37c9255-d5ae-47d9-b6e1-4ec760c200fb',
    'type': 'OpticFiberImplant',
    'description': 'some text',
    'experimentalsetup': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'consumable': None,
    'hardwaredevice': None,
    'details': {'fiberTipShape': 'flat'},
    'coordinates_system': 'External_XYZ_Absolute',
    'coordinates_details': {
                "x": 1.0,
                "y": 2.0,
                "z": 3.0,
                "xAngle": 4.0,
                "yAngle": 5.0,
                "zAngle": 6.0
            }
    }
}
```


## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/installation/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('installation', id='d37c9255-d5ae-47d9-b6e1-4ec760c200fb')
```

### Response example
{: .no_toc}

```
{'installation': {
    'id': 'd37c9255-d5ae-47d9-b6e1-4ec760c200fb',
    'type': 'OpticFiberImplant',
    'description': 'some text',
    'experimentalsetup': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'consumable': None,
    'hardwaredevice': None,
    'details': {'fiberTipShape': 'flat'},
    'coordinates_system': 'External_XYZ_Absolute',
    'coordinates_details': : {
                "x": 1.0,
                "y": 2.0,
                "z": 3.0,
                "xAngle": 4.0,
                "yAngle": 5.0,
                "zAngle": 6.0
            }
    }
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/installation/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("installation", id="d37c9255-d5ae-47d9-b6e1-4ec760c200fb", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'installation': {
    'id': 'd37c9255-d5ae-47d9-b6e1-4ec760c200fb',
    'type': 'OpticFiberImplant',
    'description': 'new text',
    'experimentalsetup': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'consumable': None,
    'hardwaredevice': None,
    'details': {'fiberTipShape': 'flat'},
    'coordinates_system': 'External_XYZ_Absolute',
    'coordinates_details': : {
                "x": 1.0,
                "y": 2.0,
                "z": 3.0,
                "xAngle": 4.0,
                "yAngle": 5.0,
                "zAngle": 6.0
            }
    }
}
```

## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/modules/installation/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("installation", id="d37c9255-d5ae-47d9-b6e1-4ec760c200fb")
```