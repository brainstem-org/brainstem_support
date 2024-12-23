---
layout: default
title: Manipulation
parent: Modules
grand_parent: API
nav_order: 4
---

# Manipulation API endpoint
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
| `procedures` | list of related procedure IDs formatted as a string **[required]** |
| `session` | related session ID formatted as a string **[required]** |
| `hardwaredevice` | related hardware device ID formatted as a string |
| `details` | JSON object. *See accepted schemas below* |


## Types of manipulation

{% include manipulation_types.md %}

## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/manipulation
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('manipulation')
```

### Response example
{: .no_toc}

```
{'manipulations': [
    {
        'id': '63a9caa1-620e-4ac5-8bf2-c2525a4b9e89',
        'type': 'ElectricalStimulation',
        'notes': None,
        'procedures': ['43bd31cd-7122-42b8-b82e-b391fdfdad9e'],
        'hardwaredevice': None,
        'session': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
        'details': {
            'amplitude': '0',
            'duration': '0',
            'dutyCycle': '0',
            'repetitions': '0',
            'injectionPolarity': '',
            'fatalOutcome': True,
            'closedLoop': False
        }
    },
    {
        'id': '1102d210-362e-4b8e-b434-8d3b60c7d535',
        'type': 'LiquidPerturbation',
        'notes': None,
        'procedures': ['64b6ae70-d07f-4fbc-ac04-cdfcfe27936f'],
        'hardwaredevice': 'b2e44346-70e0-4c19-8d50-3b0f3a7021b0',
        'session': 'ef7ae22f-143a-4a5e-adf6-1c623531dd63',
        'details': {
            'liquidAgent': '1',
            'concentration': 2,
            'volume': 2,
            'repetitions': 3,
            'flowRate': 5,
            'fatalOutcome': False,
            'closedLoop': True
        }
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/modules/manipulation
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("manipulation",  data={
    'type': 'LiquidPerturbation',
    'session': '1a827c68-19b4-4cec-8ae5-e13c8f1de900',
    'procedures': ['61da7e53-1066-42de-a1a2-3db96bb7cba2'],
    'hardwaredevice': 'b2e44346-70e0-4c19-8d50-3b0f3a7021b0',
    'notes': 'some text',
    'details': {
            'liquidAgent': 'Water',
            'concentration': 7,
            'volume': 2,
            'repetitions': 30,
            'flowRate': 12,
            'fatalOutcome': False,
            'closedLoop': True
        }
    })
```

### Response example
{: .no_toc}

```
{'manipulation': {
    'id': 'd05f56c6-9aea-4c38-a1cb-8680e015cad0',
    'type': 'LiquidPerturbation',
    'notes': 'some text',
    'procedures': ['61da7e53-1066-42de-a1a2-3db96bb7cba2'],
    'hardwaredevice': 'b2e44346-70e0-4c19-8d50-3b0f3a7021b0',
    'session': '1a827c68-19b4-4cec-8ae5-e13c8f1de900',
    'details': {
        'liquidAgent': 'Water',
        'concentration': 7,
        'volume': 2,
        'repetitions': 30,
        'flowRate': 12,
        'fatalOutcome': False,
        'closedLoop': True
    }
}}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/manipulation/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('manipulation', id='d05f56c6-9aea-4c38-a1cb-8680e015cad0')
```

### Response example
{: .no_toc}

```
{'manipulation': {
    'id': 'd05f56c6-9aea-4c38-a1cb-8680e015cad0',
    'type': 'LiquidPerturbation',
    'notes': 'some text',
    'procedures': ['61da7e53-1066-42de-a1a2-3db96bb7cba2'],
    'hardwaredevice': 'b2e44346-70e0-4c19-8d50-3b0f3a7021b0',
    'session': '1a827c68-19b4-4cec-8ae5-e13c8f1de900',
    'details': {
        'liquidAgent': 'Water',
        'concentration': 7,
        'volume': 2,
        'repetitions': 30,
        'flowRate': 12,
        'fatalOutcome': False,
        'closedLoop': True
    }
}}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/manipulation/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("manipulation", id="d05f56c6-9aea-4c38-a1cb-8680e015cad0", data={"notes": "new text"})
```

### Response example
{: .no_toc}

```
{'manipulation': {
    'id': 'd05f56c6-9aea-4c38-a1cb-8680e015cad0',
    'type': 'LiquidPerturbation',
    'notes': 'new text',
    'procedures': ['61da7e53-1066-42de-a1a2-3db96bb7cba2'],
    'hardwaredevice': 'b2e44346-70e0-4c19-8d50-3b0f3a7021b0',
    'session': '1a827c68-19b4-4cec-8ae5-e13c8f1de900',
    'details': {
        'liquidAgent': 'Water',
        'concentration': 7,
        'volume': 2,
        'repetitions': 30,
        'flowRate': 12,
        'fatalOutcome': False,
        'closedLoop': True
    }
}}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/modules/manipulation/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("manipulation", id="d05f56c6-9aea-4c38-a1cb-8680e015cad0")
``` 
