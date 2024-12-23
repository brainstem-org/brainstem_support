---
layout: default
title: Consumable stock
parent: Modules
grand_parent: API
nav_order: 3
---

# Consumable stock API endpoint
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
| `inventory` | related inventory ID formatted as a string **[required]** |
| `acquisition_date` | string containing date (e.g. "2023-03-22") |
| `expiration_date` | string containing date (e.g. "2023-03-22") |
| `storage_location` | string describing where the location of the consumable [max length: 100] |
| `storage_conditions` | string describing the conditions the consumable string [max length: 100] |
| `intended_use` | string [max length: 100] |
| `cost` | string [max length: 100] |
| `consumable` | related consumable ID formatted as a string |
| `details` | JSON object. *See accepted schemas below* |


## Types of consumable stock

{% include consumablestock_types.md %}


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/consumablestock
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('consumablestock')
```

### Response example
{: .no_toc}

```
{'consumablestock': [
    {
        'id': 'f79d84c8-6bec-40e3-b18a-5b25e57f4a09',
        'type': 'TetrodeWireElectrode',
        'notes': 'First implant',
        'setup': '0f87c229-6769-4854-83a5-c71e154246b8',
        'date_time': None,
        'consumable': 'a5f29099-2758-4163-a8e4-e5e2898e57b2',
        'hardwaredevice': None,
        'details': {
            'tetrodeCount': 1,
            'nWiresTetrode': 4,
            'wireDiameter': 33.9,
            'wireMaterial': 'tunsgten'
        }
    },
    {
        'id': 'a18dd2b1-6393-468c-9424-1bc77b9e4976',
        'type': 'TetrodeWireElectrode',
        'notes': 'Second implant',
        'setup': '0f87c229-6769-4854-83a5-c71e154246b8',
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
- **URL:** https://www.brainstem.org/api/private/modules/consumablestock
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("consumablestock",  data={
    "type": "OpticFiberImplant",
    "setup": "0f87c229-6769-4854-83a5-c71e154246b8",
    "notes": "some text",
    "details": {"fiberTipShape": "flat"}
)
```

### Response example
{: .no_toc}

```
{'consumablestock': {
    'id': 'd37c9255-d5ae-47d9-b6e1-4ec760c200fb',
    'type': 'OpticFiberImplant',
    'notes': 'some text',
    'setup': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'consumable': None,
    'hardwaredevice': None,
    'details': {'fiberTipShape': 'flat'}
}
```


## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/consumablestock/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('consumablestock', id='d37c9255-d5ae-47d9-b6e1-4ec760c200fb')
```

### Response example
{: .no_toc}

```
{'consumablestock': {
    'id': 'd37c9255-d5ae-47d9-b6e1-4ec760c200fb',
    'type': 'OpticFiberImplant',
    'notes': 'some text',
    'setup': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'consumable': None,
    'hardwaredevice': None,
    'details': {'fiberTipShape': 'flat'}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/consumablestock/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("consumablestock", id="d37c9255-d5ae-47d9-b6e1-4ec760c200fb", data={"notes": "new text"})
```

### Response example
{: .no_toc}

```
{'consumablestock': {
    'id': 'd37c9255-d5ae-47d9-b6e1-4ec760c200fb',
    'type': 'OpticFiberImplant',
    'notes': 'new text',
    'setup': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'consumable': None,
    'hardwaredevice': None,
    'details': {'fiberTipShape': 'flat'}
}
```

## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/modules/consumablestock/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("consumablestock", id="d37c9255-d5ae-47d9-b6e1-4ec760c200fb")
```