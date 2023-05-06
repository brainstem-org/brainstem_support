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
| `description` | string [max length: 500] |
| `action` | related action ID formatted as a string **[required]** |
| `dataset` | related dataset ID formatted as a string **[required]** |
| `hardware_device` | related hardware device ID formatted as a string |
| `type_json` | JSON object. *See accepted schemas below* |


These are the available `type` options for Manipulation:
- `ElectromagneticFieldStimulation`
- `ElectricalStimulation`
- `LiquidPerturbation`
- `Microperfusion`
- `OptogeneticalStimulation`
- `PharmacologicalInhalation`
- `PharmacologicalInjection`
- `PharmacologicalSuperfusion`
- `SoundStimulation`
- `ThermalPerturbation`
- `TranscranialElectricalStimulation`
- `UltraSoundStimulation`

A detailed list of the accepted schemas for the `type_json` field, related to each `type`, can be found in



## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/manipulation
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'manipulation')
```

### Response example
{: .no_toc}

```
{'manipulations': [
    {
        'id': '63a9caa1-620e-4ac5-8bf2-c2525a4b9e89',
        'type': 'ElectricalStimulation',
        'description': None,
        'action': '43bd31cd-7122-42b8-b82e-b391fdfdad9e',
        'hardware_device': None,
        'dataset': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
        'type_json': {
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
        'description': None,
        'action': '64b6ae70-d07f-4fbc-ac04-cdfcfe27936f',
        'hardware_device': 'b2e44346-70e0-4c19-8d50-3b0f3a7021b0',
        'dataset': 'ef7ae22f-143a-4a5e-adf6-1c623531dd63',
        'type_json': {
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
resp = save_model(settings, "manipulation",  data={
    'type': 'LiquidPerturbation',
    'dataset': '1a827c68-19b4-4cec-8ae5-e13c8f1de900',
    'action': '61da7e53-1066-42de-a1a2-3db96bb7cba2',
    'hardware_device': 'b2e44346-70e0-4c19-8d50-3b0f3a7021b0',
    'description': 'some text',
    'type_json': {
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
    'description': 'some text',
    'action': '61da7e53-1066-42de-a1a2-3db96bb7cba2',
    'hardware_device': 'b2e44346-70e0-4c19-8d50-3b0f3a7021b0',
    'dataset': '1a827c68-19b4-4cec-8ae5-e13c8f1de900',
    'type_json': {
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
resp = load_model(settings, 'manipulation', id='d05f56c6-9aea-4c38-a1cb-8680e015cad0')
```

### Response example
{: .no_toc}

```
{'manipulation': {
    'id': 'd05f56c6-9aea-4c38-a1cb-8680e015cad0',
    'type': 'LiquidPerturbation',
    'description': 'some text',
    'action': '61da7e53-1066-42de-a1a2-3db96bb7cba2',
    'hardware_device': 'b2e44346-70e0-4c19-8d50-3b0f3a7021b0',
    'dataset': '1a827c68-19b4-4cec-8ae5-e13c8f1de900',
    'type_json': {
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
resp = save_model(settings, "manipulation", id="d05f56c6-9aea-4c38-a1cb-8680e015cad0", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'manipulation': {
    'id': 'd05f56c6-9aea-4c38-a1cb-8680e015cad0',
    'type': 'LiquidPerturbation',
    'description': 'new text',
    'action': '61da7e53-1066-42de-a1a2-3db96bb7cba2',
    'hardware_device': 'b2e44346-70e0-4c19-8d50-3b0f3a7021b0',
    'dataset': '1a827c68-19b4-4cec-8ae5-e13c8f1de900',
    'type_json': {
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
resp = delete_model(settings, "manipulation", id="d05f56c6-9aea-4c38-a1cb-8680e015cad0")
``` 
