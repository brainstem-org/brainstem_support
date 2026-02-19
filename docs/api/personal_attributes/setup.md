---
layout: default
title: Setup
parent: Personal attributes
grand_parent: API
nav_order: 4
---

# Setup API endpoint
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
| `location` | string describing the location of the setup |
| `description` | string [max length: 500]|
| `setup_type` | related environment type ID formatted as a string **[required]** |
| `specifications` | JSON array describing setup specifications |
| `is_public` | boolean |
| `image` | image URL or null |


## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/personal_attributes/setup
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('setup')
```

### Response example
{: .no_toc}

```
{'setups': [
    {
        'id': '58e0003d-16c2-4264-913d-288463c0356d',
        'name': 'Head-fixed wheel',
        'location': 'Lab Room 101',
        'description': '',
        'setup_type': '78dc6c02-dcb0-4a31-a035-a358c7ee9e79',
        'specifications': [
            {'name': 'Radius', 'value': 12, 'description': 'cm'}
        ],
        'is_public': False,
        'image': null
    },
    {
        'id': '3e9ec0e0-d685-42ec-8386-0fa24602a73e',
        'name': 'Maze setup',
        'location': 'Lab Room 102',
        'description': '',
        'setup_type': 'e1f14b91-e507-48c1-bfec-c68d7db9c166',
        'specifications': {},
        'is_public': True,
        'image': null
    }
]}

```

Public list responses also include a `meta` object (pagination/filter metadata).


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/personal_attributes/setup
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Additional notes:** `setup_type` is required for create requests.


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("setup",  data=
    {
        'name': 'MyNewEnv',
        'location': 'Lab Room 103',
        'description': '',
        'setup_type': '78dc6c02-dcb0-4a31-a035-a358c7ee9e79',
        'specifications': {
            'Length': 100,
            'Width': '30 cm'
        },
        'is_public': False
    }
)
```

### Response example
{: .no_toc}

```
{'setup': {
    'id': 'd0ada97d-8607-48da-817b-bdd54bc9077b',
    'name': 'MyNewEnv',
    'location': 'Lab Room 103',
    'description': '',
    'setup_type': '78dc6c02-dcb0-4a31-a035-a358c7ee9e79',
    'specifications': {
        'Length': 100,
        'Width': '30 cm'
    },
    'is_public': False,
    'image': null}
}
```



## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/personal_attributes/setup/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('setup', id='d0ada97d-8607-48da-817b-bdd54bc9077b')
```

### Response example
{: .no_toc}

```
{'setup': {
    'id': 'd0ada97d-8607-48da-817b-bdd54bc9077b',
    'name': 'MyNewEnv',
    'location': 'Lab Room 103',
    'description': '',
    'setup_type': '78dc6c02-dcb0-4a31-a035-a358c7ee9e79',
    'specifications': {
        'Length': 100,
        'Width': '30 cm'
    },
    'is_public': False,
    'image': null}
}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/personal_attributes/setup/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("setup", id="d0ada97d-8607-48da-817b-bdd54bc9077b", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'setup': {
    'id': 'd0ada97d-8607-48da-817b-bdd54bc9077b',
    'name': 'MyNewEnv',
    'location': 'Lab Room 103',
    'description': 'new text',
    'setup_type': '78dc6c02-dcb0-4a31-a035-a358c7ee9e79',
    'specifications': {
        'Length': 100,
        'Width': '30 cm'
    },
    'is_public': False,
    'image': null}
}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/personal_attributes/setup/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("setup", id="d0ada97d-8607-48da-817b-bdd54bc9077b")
``` 
