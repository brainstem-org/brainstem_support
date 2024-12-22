---
layout: default
title: Data acquisition
parent: Modules
grand_parent: API
nav_order: 2
---

# Data acquisition API endpoint
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
| `session` | related session ID formatted as a string **[required]** |
| `procedures` | list of related procedures IDs formatted as strings **[required]** |
| `hardwaredevice` | related hardware device ID formatted as a string |
| `details` | JSON object. *See accepted schemas below* |


These are the available `type` options for Data acquisition:
- `Audio`
- `BehavioralTracking`
- `Electroneurogram`
- `Extracellular`
- `GeneralTimeSeries`
- `Intracellular`

A detailed list of the accepted schemas for the `details` field, related to each `type`, can be found in


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/dataacquisition
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('dataacquisition')
```

### Response example
{: .no_toc}

```
{'dataacquisition': [
    {
        'id': 'b3a6f43b-63f9-41cf-8fc2-5303e958d521',
        'description': None,
        'hardwaredevice': None,
        'procedures': ['087b71c4-6785-437c-b8ef-e35a82a8463e'],
        'session': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
        'type': 'BehavioralTracking',
        'details': {
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
        'hardwaredevice': None,
        'procedures': ['dedef2d7-00ae-4967-8e93-a9d65a20dfce'],
        'session': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
        'type': 'Extracellular',
        'details': {
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
- **URL:** https://www.brainstem.org/api/private/modules/dataacquisition
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("dataacquisition",  data={
    "type": "Extracellular",
    "procedures": ["087b71c4-6785-437c-b8ef-e35a82a8463e"],
    "session": "1f7f103b-e949-405a-9b01-ddda3b2f10cf",
    "description": "some text",
    "details": {
            "type": "int16",
            "nChannels": 32,
            "sr": 1250,
            "nSamples": 3000,
            "electrodeGroups": [
                    {
                        "channels": "0,2",
                        "label": "group1"
                    },
                    {
                        "channels": "1,3,5",
                        "label": "group2"
                    }
                ],
            "channelTags": [
                    {
                        "tag": "tag2",
                        "channels": "1,3,5",
                        "electrodeGroups": "group2"
                    },
                    {
                        "tag": "tag1",
                        "channels": "0,2",
                        "electrodeGroups": "group1"
                    }
                ]
        }
    }
)
```

### Response example
{: .no_toc}

```
{'dataacquisition': {
    'id': 'b0e4ed13-f2f1-4845-8772-24978539d0bd',
    'description': 'some text',
    'hardwaredevice': None,
    'procedures': ['087b71c4-6785-437c-b8ef-e35a82a8463e'],
    'session': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
    'type': 'Extracellular',
    'details': {
            'type': 'int16',
            'nChannels': 32,
            'sr': 1250,
            'nSamples': 3000,
            'electrodeGroups': [
                    {
                        "channels": "0,2",
                        "label": "group1"
                    },
                    {
                        "channels": "1,3,5",
                        "label": "group2"
                    }
                ],
            'channelTags': [
                    {
                        "tag": "tag2",
                        "channels": "1,3,5",
                        "electrodeGroups": "group2"
                    },
                    {
                        "tag": "tag1",
                        "channels": "0,2",
                        "electrodeGroups": "group1"
                    }
                ]
        }
    }
}
```

## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/dataacquisition/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('dataacquisition', id='b0e4ed13-f2f1-4845-8772-24978539d0bd')
```

### Response example
{: .no_toc}

```
{'dataacquisition': {
    'id': 'b0e4ed13-f2f1-4845-8772-24978539d0bd',
    'description': 'some text',
    'hardwaredevice': None,
    'procedures': ['087b71c4-6785-437c-b8ef-e35a82a8463e'],
    'session': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
    'type': 'Extracellular',
    'details': {
            'type': 'int16',
            'nChannels': 32,
            'sr': 1250,
            'nSamples': 3000,
            'electrodeGroups': [
                    {
                        "channels": "0,2",
                        "label": "group1"
                    },
                    {
                        "channels": "1,3,5",
                        "label": "group2"
                    }
                ],
            'channelTags': [
                    {
                        "tag": "tag2",
                        "channels": "1,3,5",
                        "electrodeGroups": "group2"
                    },
                    {
                        "tag": "tag1",
                        "channels": "0,2",
                        "electrodeGroups": "group1"
                    }
                ]
        }
    }
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/dataacquisition/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("dataacquisition", id="b0e4ed13-f2f1-4845-8772-24978539d0bd", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'dataacquisition': {
    'id': 'b0e4ed13-f2f1-4845-8772-24978539d0bd',
    'description': 'new text',
    'hardwaredevice': None,
    'procedures': ['087b71c4-6785-437c-b8ef-e35a82a8463e'],
    'session': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
    'type': 'Extracellular',
    'details': {
            'type': 'int16',
            'nChannels': 32,
            'sr': 1250,
            'nSamples': 3000,
            'electrodeGroups': [
                    {
                        "channels": "0,2",
                        "label": "group1"
                    },
                    {
                        "channels": "1,3,5",
                        "label": "group2"
                    }
                ],
            'channelTags': [
                    {
                        "tag": "tag2",
                        "channels": "1,3,5",
                        "electrodeGroups": "group2"
                    },
                    {
                        "tag": "tag1",
                        "channels": "0,2",
                        "electrodeGroups": "group1"
                    }
                ]
        }
    }
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/modules/dataacquisition/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("dataacquisition", id="b0e4ed13-f2f1-4845-8772-24978539d0bd")
``` 
