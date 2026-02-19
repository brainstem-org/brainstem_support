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
| `type_schema_version` | string schema version for `details` |
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
{'data_acquisitions': [
    {
        'id': '00000000-0000-0000-0000-000000000000',
        'notes': 'main arena cameras',
        'session': '00000000-0000-0000-0000-000000000000',
        'procedures': ['00000000-0000-0000-0000-000000000000'],
        'equipment': ['00000000-0000-0000-0000-000000000000'],
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
        'type_schema_version': '0.0.0',
        'image': 'https://images.brainstem.org/tracking.png',
        'order': 0
    },
    {
        'id': '00000000-0000-0000-0000-000000000000',
        'notes': 'acute probe recording',
        'session': '00000000-0000-0000-0000-000000000000',
        'procedures': ['00000000-0000-0000-0000-000000000000'],
        'equipment': ['00000000-0000-0000-0000-000000000000'],
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
        'type_schema_version': '0.0.0',
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
        "session": "00000000-0000-0000-0000-000000000000",
        "procedures": ["00000000-0000-0000-0000-000000000000"],
        "equipment": ["00000000-0000-0000-0000-000000000000"],
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
{'data_acquisition': {
    'id': '00000000-0000-0000-0000-000000000000',
    'notes': 'acute probe recording',
    'session': '00000000-0000-0000-0000-000000000000',
    'procedures': ['00000000-0000-0000-0000-000000000000'],
    'equipment': ['00000000-0000-0000-0000-000000000000'],
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
    'type_schema_version': '0.0.0',
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
resp = client.load_model('dataacquisition', id='00000000-0000-0000-0000-000000000000')
```

### Response example
{: .no_toc}

```
{'data_acquisition': {
    'id': '00000000-0000-0000-0000-000000000000',
    'notes': 'acute probe recording',
    'session': '00000000-0000-0000-0000-000000000000',
    'procedures': ['00000000-0000-0000-0000-000000000000'],
    'equipment': ['00000000-0000-0000-0000-000000000000'],
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
    'type_schema_version': '0.0.0',
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
    id="00000000-0000-0000-0000-000000000000",
    data={"notes": "re-run with higher gain", "equipment": ["00000000-0000-0000-0000-000000000000"]}
)
```

### Response example
{: .no_toc}

```
{'data_acquisition': {
    'id': '00000000-0000-0000-0000-000000000000',
    'notes': 're-run with higher gain',
    'session': '00000000-0000-0000-0000-000000000000',
    'procedures': ['00000000-0000-0000-0000-000000000000'],
    'equipment': ['00000000-0000-0000-0000-000000000000'],
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
    'type_schema_version': '0.0.0',
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
resp = client.delete_model("dataacquisition", id="00000000-0000-0000-0000-000000000000")
``` 
