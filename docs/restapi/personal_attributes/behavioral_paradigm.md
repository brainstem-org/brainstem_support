---
layout: default
title: Behavioral paradigm
parent: Personal attributes
grand_parent: REST API
nav_order: 5
---

# Behavioral paradigm API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}


## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | string with UUID identificator |
| `name` | string **[required]** |
| `description` | string |
| `task` | string |
| `reward` | string |
| `sensory_stimulus_type` | string with the related sensory stimulus type ID |
| `environment_type` | string with the related environment type ID **[required]** |
| `authgroups` | list of strings representing the related groups IDs **[required]** |


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/personal_attributes/behavioralparadigm
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'behavioralparadigm')
```

### Response example
{: .no_toc}

```
{'behavioral_paradigms': [
    {
        'id': 'febe36f7-4769-496d-bb91-6a8443214b94',
        'name': 'AlternationRunning',
        'description': '12',
        'task': "run",
        'reward': None,
        'environment_type': '531b2a21-ab1f-4aa8-8eaf-905421168d6b',
        'sensory_stimulus_type': None,
        'authgroups': [10]
    },
    {
        'id': 'f7bc834e-761c-4147-a3d4-da52293a565c',
        'name': 'ContinuousRunning',
        'description': '',
        'task': "run",
        'reward': None,
        'environment_type': '8e9c4d33-f59c-45ca-8e43-f01789f20332',
        'sensory_stimulus_type': 'b1912fcf-14dd-4b3b-b779-2d076df50150',
        'authgroups': [8]
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** http://brainstem.org/rest/private/personal_attributes/behavioralparadigm
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "behavioralparadigm",  data=
    {
        'name': 'PlayMarioKart',
        'task': "Play Mario Kart on GameCube",
        'environment_type': '8e9c4d33-f59c-45ca-8e43-f01789f20332',
        'authgroups': [8]
    }
)
```

### Response example
{: .no_toc}

```
{'behavioral_paradigm': {
    'id': '22ae80be-e030-4cee-9cd5-b94ac2edc7f8',
    'name': 'PlayMarioKart',
    'description': '',
    'task': 'Play Mario Kart on GameCube',
    'reward': None,
    'environment_type': '8e9c4d33-f59c-45ca-8e43-f01789f20332',
    'sensory_stimulus_type': None,
    'authgroups': [8]}
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/personal_attributes/behavioralparadigm/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'behavioralparadigm', id='22ae80be-e030-4cee-9cd5-b94ac2edc7f8')
```

### Response example
{: .no_toc}

```
{'behavioral_paradigm': {
    'id': '22ae80be-e030-4cee-9cd5-b94ac2edc7f8',
    'name': 'PlayMarioKart',
    'description': '',
    'task': 'Play Mario Kart on GameCube',
    'reward': None,
    'environment_type': '8e9c4d33-f59c-45ca-8e43-f01789f20332',
    'sensory_stimulus_type': None,
    'authgroups': [8]}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/personal_attributes/behavioralparadigm/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "behavioralparadigm", id="22ae80be-e030-4cee-9cd5-b94ac2edc7f8", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'behavioral_paradigm': {
    'id': '22ae80be-e030-4cee-9cd5-b94ac2edc7f8',
    'name': 'PlayMarioKart',
    'description': 'new text',
    'task': 'Play Mario Kart on GameCube',
    'reward': None,
    'environment_type': '8e9c4d33-f59c-45ca-8e43-f01789f20332',
    'sensory_stimulus_type': None,
    'authgroups': [8]}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** http://brainstem.org/rest/private/personal_attributes/behavioralparadigm/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = delete_model(settings, "behavioralparadigm", id="22ae80be-e030-4cee-9cd5-b94ac2edc7f8")
``` 