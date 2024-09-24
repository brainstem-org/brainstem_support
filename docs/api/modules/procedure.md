---
layout: default
title: Procedure
parent: Modules
grand_parent: API
nav_order: 1
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
| `description` | string [max length: 500] |
| `subject` | related subject ID formatted as a string **[required]** |
| `date_time` | string containing date (e.g. "2023-03-22") |
| `consumable` | related consumable ID formatted as a string |
| `hardwaredevice` | related hardware device ID formatted as a string |
| `brain_region` | related brain region ID formatted as a string |
| `details` | JSON object. *See accepted schemas below* |
| `coordinates_system` | string **[required]**. *See options below* |
| `coordinates_details` | JSON object. *See accepted schemas below* |


These are the available `type` options for Procedure:
- `OpticFiberImplant`
- `SingleWireElectrode`
- `SiliconProbeImplant`
- `TetrodeWireElectrode`
- `VirusInjection`

A detailed list of the accepted schemas for the `details` field, related to each `type`, can be found in the [procedure schemas page]({{"/api/schemas/procedures/"|absolute_url}}).


These are the available `coordinates_system` options for Procedure:
- `External_XYZ_Absolute`
- `Stereotaxic_BregmaAbsolute`
- `Stereotaxic_BregmaBrainSurface`
- `Stereotaxic_LambdaAbsolute`
- `Stereotaxic_LambdaBrainSurface`
- `Stereotaxic_XYZ_Absolute`
- `Stereotaxic_XY_Surface`

A detailed list of the accepted schemas for the `coordinates_details` field, related to each `coordinates_system`, can be found in the [Coordinates schemas page]({{"api/schemas/coordinates/"|absolute_url}}).


## List view
- **Allowed portals:** public, private, super
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
        'type': 'TetrodeWireElectrode',
        'description': 'First implant',
        'subject': '0f87c229-6769-4854-83a5-c71e154246b8',
        'date_time': None,
        'consumable': 'a5f29099-2758-4163-a8e4-e5e2898e57b2',
        'hardwaredevice': None,
        'details': {
            'tetrodeCount': 1,
            'nWiresTetrode': 4,
            'wireDiameter': 33.9,
            'wireMaterial': 'tunsgten'
        },
        'brain_region': '15f9aef5-2d46-4ff2-a0db-ac6be759c05c',
        'coordinates_system': 'Stereotaxic_BregmaAbsolute',
        'coordinates_details': {
            'apCoordinate': 1.0
        }
    },
    {
        'id': 'a18dd2b1-6393-468c-9424-1bc77b9e4976',
        'type': 'TetrodeWireElectrode',
        'description': 'Second implant',
        'subject': '0f87c229-6769-4854-83a5-c71e154246b8',
        'date_time': None,
        'consumable': None,
        'hardwaredevice': None,
        'details': {
            'tetrodeCount': 1,
            'nWiresTetrode': 4,
            'wireDiameter': 33.9,
            'wireMaterial': 'tunsgten'
        },
        'brain_region': '15f9aef5-2d46-4ff2-a0db-ac6be759c05c',
        'coordinates_system': 'Stereotaxic_BregmaAbsolute',
        'coordinates_details': {
            'apCoordinate': 1.0,
            'mlCoordinate': 0.0,
            'dvAngle': 2.0
        }
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/modules/procedure
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("procedure",  data={
    "type": "OpticFiberImplant",
    "subject": "0f87c229-6769-4854-83a5-c71e154246b8",
    "description": "some text",
    "details": {"fiberTipShape": "flat"},
    "coordinates_system": "Stereotaxic_BregmaAbsolute",
    "coordinates_details": {
                "apCoordinate": 1.0,
                "mlCoordinate": 2.0,
                "dvCoordinate": 3.0,
                "apAngle": 4.0,
                "mlAngle": 5.0,
                "dvAngle": 6.0
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
    'description': 'some text',
    'subject': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'consumable': None,
    'hardwaredevice': None,
    'details': {'fiberTipShape': 'flat'},
    'brain_region': None,
    'coordinates_system': 'Stereotaxic_BregmaAbsolute',
    'coordinates_details': {
                "apCoordinate": 1.0,
                "mlCoordinate": 2.0,
                "dvCoordinate": 3.0,
                "apAngle": 4.0,
                "mlAngle": 5.0,
                "dvAngle": 6.0
            }
    }
}
```



## Detail
- **Allowed portals:** public, private, super
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
    'description': 'some text',
    'subject': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'consumable': None,
    'hardwaredevice': None,
    'details': {'fiberTipShape': 'flat'},
    'brain_region': None,
    'coordinates_system': 'Stereotaxic_BregmaAbsolute',
    'coordinates_details': : {
                "apCoordinate": 1.0,
                "mlCoordinate": 2.0,
                "dvCoordinate": 3.0,
                "apAngle": 4.0,
                "mlAngle": 5.0,
                "dvAngle": 6.0
            }
    }
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/procedure/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("procedure", id="d37c9255-d5ae-47d9-b6e1-4ec760c200fb", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'procedure': {
    'id': 'd37c9255-d5ae-47d9-b6e1-4ec760c200fb',
    'type': 'OpticFiberImplant',
    'description': 'new text',
    'subject': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'consumable': None,
    'hardwaredevice': None,
    'details': {'fiberTipShape': 'flat'},
    'brain_region': None,
    'coordinates_system': 'Stereotaxic_BregmaAbsolute',
    'coordinates_details': : {
                "apCoordinate": 1.0,
                "mlCoordinate": 2.0,
                "dvCoordinate": 3.0,
                "apAngle": 4.0,
                "mlAngle": 5.0,
                "dvAngle": 6.0
            }
    }
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/modules/procedure/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("procedure", id="d37c9255-d5ae-47d9-b6e1-4ec760c200fb")
```