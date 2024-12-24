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
| `notes` | string [max length: 500] |
| `session` | related session ID formatted as a string **[required]** |
| `procedures` | list of related procedures IDs formatted as strings **[required]** |
| `hardwaredevice` | related hardware device ID formatted as a string |
| `details` | JSON object. *See accepted schemas below* |


## Types of data acquisition


### Audio and Behavior Tracking
- `Audio`: Audio
- `BehavioralTracking`: Behavioral Tracking

### Electrophysiology
- `Electroencephalography`: Electroencephalography (EEG)
- `Electroneurogram`: Electroneurogram (ENG)
- `ExtracellularEphys`: Extracellular Electrophysiology
- `IntracellularEphys`:Intracellular Electrophysiology

### Optical Imaging
- `FiberPhotometry`: Fiber Photometry
- `Miniscope`: Miniscope Microscopy
- `ConfocalMicroscopy`: Confocal Microscopy
- `LightFieldMicroscopy`: Light Field Microscopy
- `SinglePhotonMicroscopy`: Single-Photon Microscopy
- `TwoPhotonMicroscopy`: Two-Photon Microscopy
- `ThreePhotonMicroscopy`: Three-Photon Microscopy

### Magnetic and Functional Imaging
- `MagneticResonanceImaging`: Magnetic Resonance Imaging (MRI)
- `FunctionalMagneticResonanceImaging`: Functional Magnetic Resonance Imaging (fMRI)
- `Magnetoencephalography`: Magnetoencephalography (MEG)

### Tomography and Ultrasound
- `ComputedTomography`: Computed Tomography (CT)
- `PositronEmissionTomography`: Positron Emission Tomography (PET)
- `SinglePhotonEmissionComputedTomography`: Single-Photon Emission Computed Tomography (SPECT)
- `FunctionalUltrasoundImaging`: Functional Ultrasound Imaging (fUS)

### General and Time-Series Data
- `GeneralTimeSeries`: General time-series


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
        'notes': None,
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
        'notes': None,
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
    "notes": "some text",
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
    'notes': 'some text',
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
    'notes': 'some text',
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
resp = client.save_model("dataacquisition", id="b0e4ed13-f2f1-4845-8772-24978539d0bd", data={"notes": "new text"})
```

### Response example
{: .no_toc}

```
{'dataacquisition': {
    'id': 'b0e4ed13-f2f1-4845-8772-24978539d0bd',
    'notes': 'new text',
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
