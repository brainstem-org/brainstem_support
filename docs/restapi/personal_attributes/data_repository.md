---
layout: default
title: Personal attributes - Data repository
parent: API endpoints
grand_parent: REST API
nav_order: 5
---

## Table of contents
- [Fields](/brainstem_support/restapi/personal_attributes/data_repository/#fields)
- Endpoints
  - [List view](/brainstem_support/restapi/personal_attributes/data_repository/#list-view)
  - [Add](/brainstem_support/restapi/personal_attributes/data_repository/#add)
  - [Detail](/brainstem_support/restapi/personal_attributes/data_repository/#detail)
  - [Change](/brainstem_support/restapi/personal_attributes/data_repository/#change)
  - [Delete](/brainstem_support/restapi/personal_attributes/data_repository/#delete)


## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | string with UUID identificator |
| `name` | string **[required]** |
| `description` | string |
| `is_public` | boolean |
| `data_organization_json` | JSON dictionary |
| `data_protocols_json` | JSON dictionary |
| `authgroups` | list of strings representing the related groups IDs **[required]** |

## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/personal_attributes/data_repository
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'datarepository')
```

### Response example
```
{'data_repositories': [
    {
        'id': '2ba92d91-349d-4e8c-9785-fc941ddd8868',
        'name': 'Peters testdata',
        'description': '',
        'is_public': False,
        'data_organization_json': [],
        'data_protocols_json': [],
        'authgroups': [8]
    },
    {
        'id': 'c2197dea-eab6-4bbc-8257-3f05537ffdb6',
        'name': "Rodrigo's data",
        'description': '',
        'is_public': False,
        'data_organization_json': [],
        'data_protocols_json': [],
        'authgroups': [41]
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** http://brainstem.org/rest/private/personal_attributes/data_repository
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = save_model(settings, "datarepository",  data=
    {
        'name': "MyNewRepo",
        'authgroups': [41]
    }
)
```

### Response example
```
{'data_repository': {
    'id': '9f322057-cf48-4ec7-ab19-d0d7175cffe2',
    'name': 'MyNewRepo',
    'description': '',
    'is_public': False,
    'data_organization_json': None,
    'data_protocols_json': None,
    'authgroups': [41]}
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/personal_attributes/data_repository/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'datarepository', id='9f322057-cf48-4ec7-ab19-d0d7175cffe2')
```

### Response example
```
{'data_repository': {
    'id': '9f322057-cf48-4ec7-ab19-d0d7175cffe2',
    'name': 'MyNewRepo',
    'description': '',
    'is_public': False,
    'data_organization_json': None,
    'data_protocols_json': None,
    'authgroups': [41]}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/personal_attributes/data_repository/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = save_model(settings, "datarepository", id="9f322057-cf48-4ec7-ab19-d0d7175cffe2", data={"description": "new text"})
```

### Response example
```
{'data_repository': {
    'id': '9f322057-cf48-4ec7-ab19-d0d7175cffe2',
    'name': 'MyNewRepo',
    'description': 'new text',
    'is_public': False,
    'data_organization_json': None,
    'data_protocols_json': None,
    'authgroups': [41]}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** http://brainstem.org/rest/private/personal_attributes/data_repository/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = delete_model(settings, "datarepository", id="9f322057-cf48-4ec7-ab19-d0d7175cffe2")
``` 