---
layout: default
title: General attributes - Laboratory
parent: API endpoints
grand_parent: REST API
nav_order: 4
---

## Table of contents
- [Fields](/brainstem_support/restapi/attributes/laboratory/#fields)
- Endpoints
  - [List view](/brainstem_support/restapi/attributes/laboratory/#list-view)
  - [Add](/brainstem_support/restapi/attributes/laboratory/#add)
  - [Detail](/brainstem_support/restapi/attributes/laboratory/#detail)
  - [Change](/brainstem_support/restapi/attributes/laboratory/#change)
  - [Delete](/brainstem_support/restapi/attributes/laboratory/#delete)

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | string with UUID identificator |
| `group` | string with the related group ID **[required]** |
| `principal_investigators` | list of strings representing the related principal investigators IDs **[required]** |
| `description` | string |
| `website` | string |
| `department` | string |
| `institution` | string **[required]** |
| `city` | string |
| `country` | string |


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/attributes/laboratory
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'laboratory')
```

### Response example
```
{'laboratories': [
    {
        'id': '3362d1da-29e4-4723-b326-1605f390178a',
        'group': 1,
        'principal_investigators': [],
        'description': '',
        'website': 'https://buzsakilab.com/wp/',
        'department': 'Neuroscience Institute',
        'institution': 'NYU',
        'city': 'New York',
        'country': 'United States'
    },
    {
        'id': 'e5dc5bd9-072d-45e4-8b00-2a468a59db8b',
        'group': 8,
        'principal_investigators': [3, 7],
        'description': '',
        'website': '',
        'department': '',
        'institution': 'UAM',
        'city': '',
        'country': 'Spain'
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** http://brainstem.org/rest/private/attributes/laboratory
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found



### Use example (using Python API)
```
resp = save_model(settings, "laboratory",  data={
    'group': 41,
    'principal_investigators': [3],
    'institution': 'A university'}
)
```

### Response example
```
{'laboratory': {
    'id': '5d882f8b-5c74-428e-9ed9-41c8780527ff',
    'group': 41,
    'principal_investigators': [3],
    'description': '',
    'website': '',
    'department': '',
    'institution': 'A university',
    'city': '',
    'country': ''}
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/attributes/laboratory/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'laboratory', id='5d882f8b-5c74-428e-9ed9-41c8780527ff')
```

### Response example
```
{'laboratory': {
    'id': '5d882f8b-5c74-428e-9ed9-41c8780527ff',
    'group': 41,
    'principal_investigators': [3],
    'description': '',
    'website': '',
    'department': '',
    'institution': 'A university',
    'city': '',
    'country': ''}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/attributes/laboratory/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = save_model(settings, "laboratory", id="5d882f8b-5c74-428e-9ed9-41c8780527ff", data={"description": "new text"})
```

### Response example
```
{'laboratory': {
    'id': '5d882f8b-5c74-428e-9ed9-41c8780527ff',
    'group': 41,
    'principal_investigators': [3],
    'description': 'new text',
    'website': '',
    'department': '',
    'institution': 'A university',
    'city': '',
    'country': ''}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** http://brainstem.org/rest/private/attributes/laboratory/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = delete_model(settings, "laboratory", id="5d882f8b-5c74-428e-9ed9-41c8780527ff")
``` 