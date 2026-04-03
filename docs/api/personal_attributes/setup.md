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
resp = client.load('setup')
```

### Response example
{: .no_toc}

```
{'setups': [
    {
        'id': '<id>',
        'name': 'Head-fixed wheel',
        'location': 'Lab Room 101',
        'description': '',
        'setup_type': '<setup_type-id>',
        'specifications': [
            {'name': 'Radius', 'value': 12, 'description': 'cm'}
        ],
        'is_public': False,
        'image': null
    },
    {
        'id': '<id>',
        'name': 'Maze setup',
        'location': 'Lab Room 102',
        'description': '',
        'setup_type': '<setup_type-id>',
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
resp = client.save("setup",  data=
    {
        'name': 'MyNewEnv',
        'location': 'Lab Room 103',
        'description': '',
        'setup_type': '<setup_type-id>',
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
    'id': '<id>',
    'name': 'MyNewEnv',
    'location': 'Lab Room 103',
    'description': '',
    'setup_type': '<setup_type-id>',
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
resp = client.load('setup', id='<id>')
```

### Response example
{: .no_toc}

```
{'setup': {
    'id': '<id>',
    'name': 'MyNewEnv',
    'location': 'Lab Room 103',
    'description': '',
    'setup_type': '<setup_type-id>',
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
resp = client.save("setup", id="<id>", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'setup': {
    'id': '<id>',
    'name': 'MyNewEnv',
    'location': 'Lab Room 103',
    'description': 'new text',
    'setup_type': '<setup_type-id>',
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
resp = client.delete("setup", id="<id>")
``` 
