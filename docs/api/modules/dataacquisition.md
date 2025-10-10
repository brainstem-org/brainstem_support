---
layout: default
title: Data acquisition
parent: Modules
grand_parent: API
nav_order: 3
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
| `notes` | string [max length: 500] |
| `session` | related session ID formatted as a string **[required]** |
| `procedures` | list of related procedure IDs formatted as strings |
| `equipment` | list of related equipment IDs formatted as strings |
| `details` | JSON object mapped to the internal `type_json` field. *See accepted schemas below* |
| `image` | URL string pointing to an uploaded image (read-only) |
| `order` | optional positive integer controlling display order within a session |


## Types of data acquisition


A detailed list of the available `type` options and accepted schemas for the `details` field can be found in the [Data acquisition schemas documentation](/api/schemas/dataacquisition).







## List view
- **Allowed portals:** public, private
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
        'notes': 'main arena cameras',
        'session': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
        'procedures': ['087b71c4-6785-437c-b8ef-e35a82a8463e'],
        'equipment': ['2f68c9ad-9b4e-49b3-947a-47a4feae0d70'],
        'type': 'BehavioralTracking',
        'details': {
            'fileName': 'session1_tracking.mp4',
            'format': 'mp4',
            'compression': 'h264',
            'frameRate': 60,
            'nFrames': 54000,
            'verticalResolution': 1080,
            'horizontalResolution': 1920
        },
        'image': 'https://images.brainstem.org/tracking.png',
        'order': 0
    },
    {
        'id': '6b7d3eb1-0360-4c40-944b-83e285f8f8a7',
        'notes': 'acute probe recording',
        'session': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
        'procedures': ['dedef2d7-00ae-4967-8e93-a9d65a20dfce'],
        'equipment': ['5b032f95-3f5b-4a27-9680-5f8f671dba22'],
        'type': 'ExtracellularEphys',
        'details': {
            'fileName': 'session1_probe.dat',
            'format': 'binary',
            'type': 'int16',
            'nChannels': 64,
            'sr': 30000,
            'nSamples': 180000000,
            'electrodeGroups': [
                {'channels': [0, 2, 4], 'label': 'anterior'}
            ],
            'channelTags': [
                {'tag': 'good', 'channels': [0, 2], 'groups': [0]}
            ]
        },
        'image': None,
        'order': 1
    }
]}
```


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/modules/dataacquisition
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model(
    "dataacquisition",
    data={
        "type": "ExtracellularEphys",
        "session": "1f7f103b-e949-405a-9b01-ddda3b2f10cf",
        "procedures": ["087b71c4-6785-437c-b8ef-e35a82a8463e"],
        "equipment": ["5b032f95-3f5b-4a27-9680-5f8f671dba22"],
        "notes": "acute probe recording",
        "details": {
            "fileName": "session1_probe.dat",
            "format": "binary",
            "type": "int16",
            "nChannels": 64,
            "sr": 30000,
            "nSamples": 180000000,
            "electrodeGroups": [
                {"channels": [0, 2, 4], "label": "anterior"},
                {"channels": [1, 3, 5], "label": "posterior"}
            ],
            "channelTags": [
                {"tag": "artifact", "channels": [1, 5], "groups": [1]},
                {"tag": "good", "channels": [0, 2], "groups": [0]}
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
    'notes': 'acute probe recording',
    'session': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
    'procedures': ['087b71c4-6785-437c-b8ef-e35a82a8463e'],
    'equipment': ['5b032f95-3f5b-4a27-9680-5f8f671dba22'],
    'type': 'ExtracellularEphys',
    'details': {
        'fileName': 'session1_probe.dat',
        'format': 'binary',
        'type': 'int16',
        'nChannels': 64,
        'sr': 30000,
        'nSamples': 180000000,
        'electrodeGroups': [
            {'channels': [0, 2, 4], 'label': 'anterior'},
            {'channels': [1, 3, 5], 'label': 'posterior'}
        ],
        'channelTags': [
            {'tag': 'artifact', 'channels': [1, 5], 'groups': [1]},
            {'tag': 'good', 'channels': [0, 2], 'groups': [0]}
        ]
    },
    'image': None,
    'order': 0
}}
```

## Detail
- **Allowed portals:** public, private
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
    'notes': 'acute probe recording',
    'session': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
    'procedures': ['087b71c4-6785-437c-b8ef-e35a82a8463e'],
    'equipment': ['5b032f95-3f5b-4a27-9680-5f8f671dba22'],
    'type': 'ExtracellularEphys',
    'details': {
        'fileName': 'session1_probe.dat',
        'format': 'binary',
        'type': 'int16',
        'nChannels': 64,
        'sr': 30000,
        'nSamples': 180000000,
        'electrodeGroups': [
            {'channels': [0, 2, 4], 'label': 'anterior'},
            {'channels': [1, 3, 5], 'label': 'posterior'}
        ],
        'channelTags': [
            {'tag': 'artifact', 'channels': [1, 5], 'groups': [1]},
            {'tag': 'good', 'channels': [0, 2], 'groups': [0]}
        ]
    },
    'image': None,
    'order': 0
}}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/dataacquisition/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model(
    "dataacquisition",
    id="b0e4ed13-f2f1-4845-8772-24978539d0bd",
    data={"notes": "re-run with higher gain", "equipment": ["5b032f95-3f5b-4a27-9680-5f8f671dba22"]}
)
```

### Response example
{: .no_toc}

```
{'dataacquisition': {
    'id': 'b0e4ed13-f2f1-4845-8772-24978539d0bd',
    'notes': 're-run with higher gain',
    'session': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
    'procedures': ['087b71c4-6785-437c-b8ef-e35a82a8463e'],
    'equipment': ['5b032f95-3f5b-4a27-9680-5f8f671dba22'],
    'type': 'ExtracellularEphys',
    'details': {
        'fileName': 'session1_probe.dat',
        'format': 'binary',
        'type': 'int16',
        'nChannels': 64,
        'sr': 30000,
        'nSamples': 180000000,
        'electrodeGroups': [
            {'channels': [0, 2, 4], 'label': 'anterior'},
            {'channels': [1, 3, 5], 'label': 'posterior'}
        ],
        'channelTags': [
            {'tag': 'artifact', 'channels': [1, 5], 'groups': [1]},
            {'tag': 'good', 'channels': [0, 2], 'groups': [0]}
        ]
    },
    'image': None,
    'order': 0
}}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/modules/dataacquisition/<id\>/
- **Data:** None
- **Responses:** `204` OK; `400` Bad request; `403` Not allowed; `404` Not found

`400` is returned when the data acquisition is still referenced by an epoch in the same session.


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("dataacquisition", id="b0e4ed13-f2f1-4845-8772-24978539d0bd")
``` 
