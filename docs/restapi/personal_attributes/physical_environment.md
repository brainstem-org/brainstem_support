---
layout: default
title: Personal attributes - Physical environment
parent: API endpoints
grand_parent: REST API
nav_order: 4
---

## Table of contents
- [Fields](/brainstem_support/restapi/personal-attributes/physical-environment/#fields)
- Endpoints
  - [List view](/brainstem_support/restapi/personal-attributes/physical-environment/#list-view)
  - [Add](/brainstem_support/restapi/personal-attributes/physical-environment/#add)
  - [Detail](/brainstem_support/restapi/personal-attributes/physical-environment/#detail)
  - [Change](/brainstem_support/restapi/personal-attributes/physical-environment/#change)
  - [Delete](/brainstem_support/restapi/personal-attributes/physical-environment/#delete)


## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | string with UUID identificator |
| `name` | string **[required]** |
| `description` | string |
| `environment_type` | string with the related environment type ID **[required]** |
| `physical_dimensions_json` | JSON dictionary |
| `authgroups` | list of strings representing the related groups IDs **[required]** |
| `is_public` | boolean |


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/personal_attributes/physical_environment
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'physicalenvironment')
```

### Response example
```
{'physical_environments': [
    {
        'id': '58e0003d-16c2-4264-913d-288463c0356d',
        'name': 'Head-fixed wheel',
        'description': '',
        'environment_type': '78dc6c02-dcb0-4a31-a035-a358c7ee9e79',
        'physical_dimensions_json': [
            {'name': 'Radius', 'value': 12, 'description': 'cm'}
        ],
        'authgroups': [41],
        'is_public': False
    },
    {
        'id': '3e9ec0e0-d685-42ec-8386-0fa24602a73e',
        'name': "Mino's Maze",
        'description': '',
        'environment_type': 'e1f14b91-e507-48c1-bfec-c68d7db9c166',
        'physical_dimensions_json': [],
        'authgroups': [8],
        'is_public': True
    }
]}

```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** http://brainstem.org/rest/private/personal_attributes/physical_environment
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = save_model(settings, "physicalenvironment",  data=
    {
        'name': 'MyNewEnv',
        'description': '',
        'environment_type': '78dc6c02-dcb0-4a31-a035-a358c7ee9e79',
        'physical_dimensions_json': [
            {'name': 'Length', 'value': 100, 'description': 'yards'}
        ],
        'authgroups': [41],
        'is_public': False
    }
)
```

### Response example
```
{'physical_environment': {
    'id': 'd0ada97d-8607-48da-817b-bdd54bc9077b',
    'name': 'MyNewEnv',
    'description': '',
    'environment_type': '78dc6c02-dcb0-4a31-a035-a358c7ee9e79',
    'physical_dimensions_json': [
        {'name': 'Length', 'value': 100, 'description': 'yards'}
    ],
    'authgroups': [41],
    'is_public': False}
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/personal_attributes/physical_environment/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'physicalenvironment', id='d0ada97d-8607-48da-817b-bdd54bc9077b')
```

### Response example
```
{'physical_environment': {
    'id': 'd0ada97d-8607-48da-817b-bdd54bc9077b',
    'name': 'MyNewEnv',
    'description': '',
    'environment_type': '78dc6c02-dcb0-4a31-a035-a358c7ee9e79',
    'physical_dimensions_json': [
        {'name': 'Length', 'value': 100, 'description': 'yards'}
    ],
    'authgroups': [41],
    'is_public': False}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/personal_attributes/physical_environment/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = save_model(settings, "physicalenvironment", id="d0ada97d-8607-48da-817b-bdd54bc9077b", data={"description": "new text"})
```

### Response example
```
{'physical_environment': {
    'id': 'd0ada97d-8607-48da-817b-bdd54bc9077b',
    'name': 'MyNewEnv',
    'description': 'new text',
    'environment_type': '78dc6c02-dcb0-4a31-a035-a358c7ee9e79',
    'physical_dimensions_json': [
        {'name': 'Length', 'value': 100, 'description': 'yards'}
    ],
    'authgroups': [41],
    'is_public': False}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** http://brainstem.org/rest/private/personal_attributes/physical_environment/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = delete_model(settings, "physicalenvironment", id="d0ada97d-8607-48da-817b-bdd54bc9077b")
``` 