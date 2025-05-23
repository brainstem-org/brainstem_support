---
layout: default
title: Behavioral paradigm
parent: Personal attributes
grand_parent: API
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
| `id` | UUID identificator formatted as a string |
| `name` | string **[required]** [max length: 50] |
| `description` | string [max length: 500] |
| `task` | string [max length: 100] |
| `reward` | string [max length: 100] |
| `sensory_stimulus_type` | related sensory stimulus type ID formatted as a string |
| `setup_type` | related environment type ID formatted as a string **[required]** |
| `is_public` | boolean |

## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/personal_attributes/behavioralparadigm
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('behavioralparadigm')
```

### Response example
{: .no_toc}

```
{'behavioralparadigms': [
    {
        'id': 'febe36f7-4769-496d-bb91-6a8443214b94',
        'name': 'AlternationRunning',
        'description': '12',
        'task': "run",
        'reward': None,
        'setup_type': '531b2a21-ab1f-4aa8-8eaf-905421168d6b',
        'sensory_stimulus_type': None
    },
    {
        'id': 'f7bc834e-761c-4147-a3d4-da52293a565c',
        'name': 'ContinuousRunning',
        'description': '',
        'task': "run",
        'reward': None,
        'setup_type': '8e9c4d33-f59c-45ca-8e43-f01789f20332',
        'sensory_stimulus_type': 'b1912fcf-14dd-4b3b-b779-2d076df50150'
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/personal_attributes/behavioralparadigm
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("behavioralparadigm",  data=
    {
        'name': 'PlayMarioKart',
        'task': "Play Mario Kart on GameCube",
        'setup_type': '8e9c4d33-f59c-45ca-8e43-f01789f20332',
    }
)
```

### Response example
{: .no_toc}

```
{'behavioralparadigm': {
    'id': '22ae80be-e030-4cee-9cd5-b94ac2edc7f8',
    'name': 'PlayMarioKart',
    'description': '',
    'task': 'Play Mario Kart on GameCube',
    'reward': None,
    'setup_type': '8e9c4d33-f59c-45ca-8e43-f01789f20332',
    'sensory_stimulus_type': None}
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/personal_attributes/behavioralparadigm/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('behavioralparadigm', id='22ae80be-e030-4cee-9cd5-b94ac2edc7f8')
```

### Response example
{: .no_toc}

```
{'behavioralparadigm': {
    'id': '22ae80be-e030-4cee-9cd5-b94ac2edc7f8',
    'name': 'PlayMarioKart',
    'description': '',
    'task': 'Play Mario Kart on GameCube',
    'reward': None,
    'setup_type': '8e9c4d33-f59c-45ca-8e43-f01789f20332',
    'sensory_stimulus_type': None}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/personal_attributes/behavioralparadigm/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("behavioralparadigm", id="22ae80be-e030-4cee-9cd5-b94ac2edc7f8", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'behavioralparadigm': {
    'id': '22ae80be-e030-4cee-9cd5-b94ac2edc7f8',
    'name': 'PlayMarioKart',
    'description': 'new text',
    'task': 'Play Mario Kart on GameCube',
    'reward': None,
    'setup_type': '8e9c4d33-f59c-45ca-8e43-f01789f20332',
    'sensory_stimulus_type': None}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/personal_attributes/behavioralparadigm/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("behavioralparadigm", id="22ae80be-e030-4cee-9cd5-b94ac2edc7f8")
``` 