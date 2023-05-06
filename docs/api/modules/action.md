---
layout: default
title: Action
parent: Modules
grand_parent: API
nav_order: 1
---

# Action API endpoint
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
| `hardware_device` | related hardware device ID formatted as a string |
| `brain_region` | related brain region ID formatted as a string |
| `type_json` | JSON object. *See accepted schemas below* |
| `coordinates` | string **[required]**. *See options below* |
| `coordinates_json` | JSON object. *See accepted schemas below* |


These are the available `type` options for Action:
- `OpticFiberImplant`
- `SingleWireElectrode`
- `SiliconProbeImplant`
- `TetrodeWireElectrode`
- `VirusInjection`

A detailed list of the accepted schemas for the `type_json` field, related to each `type`, can be found in


These are the available `coordinates` options for Action:
- `External_XYZ_Absolute`
- `Stereotaxic_BregmaAbsolute`
- `Stereotaxic_BregmaBrainSurface`
- `Stereotaxic_LambdaAbsolute`
- `Stereotaxic_LambdaBrainSurface`
- `Stereotaxic_XYZ_Absolute`
- `Stereotaxic_XY_Surface`

A detailed list of the accepted schemas for the `coordinates_json` field, related to each `coordinates`, can be found in


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/action
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'action')
```

### Response example
{: .no_toc}

```
{'actions': [
    {
        'id': 'f79d84c8-6bec-40e3-b18a-5b25e57f4a09',
        'type': 'TetrodeWireElectrode',
        'description': 'First implant',
        'subject': '0f87c229-6769-4854-83a5-c71e154246b8',
        'date_time': None,
        'consumable': 'a5f29099-2758-4163-a8e4-e5e2898e57b2',
        'hardware_device': None,
        'type_json': {
            'tetrodeCount': 1,
            'nWiresTetrode': 4,
            'wireDiameter': 33.9,
            'wireMaterial': 'tunsgten'
        },
        'brain_region': '15f9aef5-2d46-4ff2-a0db-ac6be759c05c',
        'coordinates': 'Stereotaxic_BregmaAbsolute',
        'coordinates_json': {
            'apCoordinates': 1.0
        }
    },
    {
        'id': 'a18dd2b1-6393-468c-9424-1bc77b9e4976',
        'type': 'TetrodeWireElectrode',
        'description': 'Second implant',
        'subject': '0f87c229-6769-4854-83a5-c71e154246b8',
        'date_time': None,
        'consumable': None,
        'hardware_device': None,
        'type_json': {
            'tetrodeCount': 1,
            'nWiresTetrode': 4,
            'wireDiameter': 33.9,
            'wireMaterial': 'tunsgten'
        },
        'brain_region': '15f9aef5-2d46-4ff2-a0db-ac6be759c05c',
        'coordinates': 'Stereotaxic_BregmaAbsolute',
        'coordinates_json': {
            'apCoordinates': 1.0,
            'mlCoordinates': 0.0,
            'dvAngle': 2.0
        }
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/modules/action
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "action",  data={
    "type": "OpticFiberImplant",
    "subject": "0f87c229-6769-4854-83a5-c71e154246b8",
    "description": "some text",
    "type_json": {"fiberTipShape": "flat"},
    "coordinates": "Stereotaxic_BregmaAbsolute",
    "coordinates_json": {"apCoordinates": 1.0}})
```

### Response example
{: .no_toc}

```
{'action': {
    'id': 'd37c9255-d5ae-47d9-b6e1-4ec760c200fb',
    'type': 'OpticFiberImplant',
    'description': 'some text',
    'subject': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'consumable': None,
    'hardware_device': None,
    'type_json': {'fiberTipShape': 'flat'},
    'brain_region': None,
    'coordinates': 'Stereotaxic_BregmaAbsolute',
    'coordinates_json': {'apCoordinates': 1.0}}
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/action/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'action', id='d37c9255-d5ae-47d9-b6e1-4ec760c200fb')
```

### Response example
{: .no_toc}

```
{'action': {
    'id': 'd37c9255-d5ae-47d9-b6e1-4ec760c200fb',
    'type': 'OpticFiberImplant',
    'description': 'some text',
    'subject': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'consumable': None,
    'hardware_device': None,
    'type_json': {'fiberTipShape': 'flat'},
    'brain_region': None,
    'coordinates': 'Stereotaxic_BregmaAbsolute',
    'coordinates_json': {'apCoordinates': 1.0}}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/action/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "action", id="d37c9255-d5ae-47d9-b6e1-4ec760c200fb", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'action': {
    'id': 'd37c9255-d5ae-47d9-b6e1-4ec760c200fb',
    'type': 'OpticFiberImplant',
    'description': 'new text',
    'subject': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'consumable': None,
    'hardware_device': None,
    'type_json': {'fiberTipShape': 'flat'},
    'brain_region': None,
    'coordinates': 'Stereotaxic_BregmaAbsolute',
    'coordinates_json': {'apCoordinates': 1.0}}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/modules/action/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = delete_model(settings, "action", id="d37c9255-d5ae-47d9-b6e1-4ec760c200fb")
```