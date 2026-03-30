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
| `behavioral_paradigm` | related behavioral paradigm ID formatted as a string **[required]** |
| `licenses` | list of related license IDs |
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
resp = client.load('behavioralassay')
```

### Response example
{: .no_toc}

```
{'behavioralassays': [
    {
        'id': '<id>',
        'name': 'AlternationRunning',
        'description': 'Alternating running task',
        'setup_type': '<setup_type-id>',
        'behavioral_paradigm': '<behavioral_paradigm-id>',
        'licenses': [],
        'is_public': False
    },
    {
        'id': '<id>',
        'name': 'ContinuousRunning',
        'description': 'Continuous running task',
        'setup_type': '<setup_type-id>',
        'behavioral_paradigm': '<behavioral_paradigm-id>',
        'licenses': [],
        'is_public': True
    }
]}
```

Public list responses also include a `meta` object (pagination/filter metadata).


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/personal_attributes/behavioralassay
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Additional notes:** both `setup_type` and `behavioral_paradigm` are required for create requests.


### Use example (using Python API)
{: .no_toc}

```
resp = client.save("behavioralassay",  data=
    {
        'name': 'PlayMarioKart',
        'description': 'Play Mario Kart on GameCube',
        'setup_type': '<setup_type-id>',
        'behavioral_paradigm': '<behavioral_paradigm-id>',
        'licenses': [],
    }
)
```

### Response example
{: .no_toc}

```
{'behavioralassay': {
    'id': '<id>',
    'name': 'PlayMarioKart',
    'description': 'Play Mario Kart on GameCube',
    'setup_type': '<setup_type-id>',
    'behavioral_paradigm': '<behavioral_paradigm-id>',
    'licenses': [],
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
resp = client.load('behavioralassay', id='<id>')
```

### Response example
{: .no_toc}

```
{'behavioralassay': {
    'id': '<id>',
    'name': 'PlayMarioKart',
    'description': 'Play Mario Kart on GameCube',
    'setup_type': '<setup_type-id>',
    'behavioral_paradigm': '<behavioral_paradigm-id>',
    'licenses': [],
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
resp = client.save("behavioralassay", id="<id>", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'behavioralassay': {
    'id': '<id>',
    'name': 'PlayMarioKart',
    'description': 'new text',
    'setup_type': '<setup_type-id>',
    'behavioral_paradigm': '<behavioral_paradigm-id>',
    'licenses': [],
    'is_public': False}
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
resp = client.delete("behavioralassay", id="<id>")
``` 
