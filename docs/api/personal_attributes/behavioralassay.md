---
layout: default
title: Behavioral Assay
parent: Personal attributes
grand_parent: API
nav_order: 1
---

# Behavioral Assay API endpoint
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
| `setup_type` | related environment type ID formatted as a string **[required]** |
| `is_public` | boolean |

## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/personal_attributes/behavioralassay
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('behavioralassay')
```

### Response example
{: .no_toc}

```
{'behavioralassays': [
    {
        'id': 'febe36f7-4769-496d-bb91-6a8443214b94',
        'name': 'AlternationRunning',
        'description': 'Alternating running task',
        'setup_type': '531b2a21-ab1f-4aa8-8eaf-905421168d6b',
        'is_public': False
    },
    {
        'id': 'f7bc834e-761c-4147-a3d4-da52293a565c',
        'name': 'ContinuousRunning',
        'description': 'Continuous running task',
        'setup_type': '8e9c4d33-f59c-45ca-8e43-f01789f20332',
        'is_public': True
    }
]}
```


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/personal_attributes/behavioralassay
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("behavioralassay",  data=
    {
        'name': 'PlayMarioKart',
        'description': 'Play Mario Kart on GameCube',
        'setup_type': '8e9c4d33-f59c-45ca-8e43-f01789f20332',
    }
)
```

### Response example
{: .no_toc}

```
{'behavioralassay': {
    'id': '22ae80be-e030-4cee-9cd5-b94ac2edc7f8',
    'name': 'PlayMarioKart',
    'description': 'Play Mario Kart on GameCube',
    'setup_type': '8e9c4d33-f59c-45ca-8e43-f01789f20332',
    'is_public': False}
}
```



## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/personal_attributes/behavioralassay/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('behavioralassay', id='22ae80be-e030-4cee-9cd5-b94ac2edc7f8')
```

### Response example
{: .no_toc}

```
{'behavioralassay': {
    'id': '22ae80be-e030-4cee-9cd5-b94ac2edc7f8',
    'name': 'PlayMarioKart',
    'description': 'Play Mario Kart on GameCube',
    'setup_type': '8e9c4d33-f59c-45ca-8e43-f01789f20332',
    'is_public': False}
}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/personal_attributes/behavioralassay/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("behavioralassay", id="22ae80be-e030-4cee-9cd5-b94ac2edc7f8", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'behavioralassay': {
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
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/personal_attributes/behavioralassay/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("behavioralassay", id="22ae80be-e030-4cee-9cd5-b94ac2edc7f8")
``` 