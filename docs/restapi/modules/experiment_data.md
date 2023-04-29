---
layout: default
title: Experiment Data
parent: Modules
grand_parent: REST API
nav_order: 3
---

# Experiment Data API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | string with UUID identificator |
| `type` | string **[required]**. *See options below* |
| `description` | string |
| `dataset` | string with the related dataset ID **[required]** |
| `actions` | list of strings representing the related actions IDs **[required]** |
| `hardware_device` | string with the related hardware device ID |
| `type_json` | JSON object. *See accepted schemas below* |


These are the available `type` options for Experiment Data:
- `Audio`
- `BehavioralTracking`
- `Electroneurogram`
- `Extracellular`
- `GeneralTimeSeries`
- `Intracellular`

A detailed list of the accepted schemas for the `type_json` field, related to each `type`, can be found in


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/modules/experimentdata
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'experimentdata')
```

### Response example
{: .no_toc}

```
{'experiment_data': [
    {
        'id': 'b3a6f43b-63f9-41cf-8fc2-5303e958d521',
        'description': None,
        'hardware_device': None,
        'actions': ['087b71c4-6785-437c-b8ef-e35a82a8463e'],
        'dataset': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
        'type': 'BehavioralTracking',
        'type_json': {
            'fileName': 'myfile.txt',
            'format': '111',
            'frameRate': 0,
            'nFrames': 222,
            'horizontalResolution': 0
        }
    },
    {
        'id': '6b7d3eb1-0360-4c40-944b-83e285f8f8a7',
        'description': None,
        'hardware_device': None,
        'actions': ['dedef2d7-00ae-4967-8e93-a9d65a20dfce'],
        'dataset': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
        'type': 'Extracellular',
        'type_json': {
            'type': 'int16',
            'nChannels': 45,
            'sr': 20000.0,
            'nSamples': 122,
            'electrodeGroups': [],
            'channelTags': []
        }
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** http://brainstem.org/rest/private/modules/experimentdata
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "experimentdata",  data={
    "type": "Extracellular",
    "actions": ["087b71c4-6785-437c-b8ef-e35a82a8463e"],
    "dataset": "1f7f103b-e949-405a-9b01-ddda3b2f10cf",
    "description": "some text",
    "type_json": {
            "type": "int16",
            "nChannels": 32,
            "sr": 1250,
            "nSamples": 3000,
            "electrodeGroups": [],
            "channelTags": []
        }
    }
)
```

### Response example
{: .no_toc}

```
{'experiment_data': {
    'id': 'b0e4ed13-f2f1-4845-8772-24978539d0bd',
    'description': 'some text',
    'hardware_device': None,
    'actions': ['087b71c4-6785-437c-b8ef-e35a82a8463e'],
    'dataset': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
    'type': 'Extracellular',
    'type_json': {
            'type': 'int16',
            'nChannels': 32,
            'sr': 1250,
            'nSamples': 3000,
            'electrodeGroups': [],
            'channelTags': []
        }
    }
}
```

## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/modules/experimentdata/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'experimentdata', id='b0e4ed13-f2f1-4845-8772-24978539d0bd')
```

### Response example
{: .no_toc}

```
{'experiment_data': {
    'id': 'b0e4ed13-f2f1-4845-8772-24978539d0bd',
    'description': 'some text',
    'hardware_device': None,
    'actions': ['087b71c4-6785-437c-b8ef-e35a82a8463e'],
    'dataset': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
    'type': 'Extracellular',
    'type_json': {
            'type': 'int16',
            'nChannels': 32,
            'sr': 1250,
            'nSamples': 3000,
            'electrodeGroups': [],
            'channelTags': []
        }
    }
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/modules/experimentdata/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "experimentdata", id="b0e4ed13-f2f1-4845-8772-24978539d0bd", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'experiment_data': {
    'id': 'b0e4ed13-f2f1-4845-8772-24978539d0bd',
    'description': 'new text',
    'hardware_device': None,
    'actions': ['087b71c4-6785-437c-b8ef-e35a82a8463e'],
    'dataset': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
    'type': 'Extracellular',
    'type_json': {
            'type': 'int16',
            'nChannels': 32,
            'sr': 1250,
            'nSamples': 3000,
            'electrodeGroups': [],
            'channelTags': []
        }
    }
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** http://brainstem.org/rest/private/modules/experimentdata/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = delete_model(settings, "experimentdata", id="b0e4ed13-f2f1-4845-8772-24978539d0bd")
``` 
