---
layout: default
title: User
parent: User endpoints
grand_parent: REST API
nav_order: 8
---

## Table of contents
- [Fields](/brainstem_support/restapi/users/user/#fields)
- Endpoints
  - [List view](/brainstem_support/restapi/users/user/#list-view)
  - [Add](/brainstem_support/restapi/users/user/#add)
  - [Detail](/brainstem_support/restapi/users/user/#detail)
  - [Change](/brainstem_support/restapi/users/user/#change)
  - [Delete](/brainstem_support/restapi/users/user/#delete)

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | string with UUID identificator |
| `email` | string |
| `first_name` | string |
| `last_name` | string |
| `groups_own_json` | list of dictionaries with each group owned by the user. *See structure below* |
| `website` | string |
| `google_scholar` | string |
| `orcid_id` | string |
| `atlas_preference` | string |

The following fields are only accessible for administrators:

| Field        | Description  |
|:-------------|:-------------|
| `is_superuser` | boolean |
| `is_project_admin` | boolean |
| `is_group_admin` | boolean |
| `is_taxonomies_admin` | boolean |
| `is_resources_admin` | boolean |
| `is_attributes_admin` | boolean |

Each dictionary in the `groups_own_json` list contains the group's `id` and `name`:
```
{'id': 8, 'name': 'test_group'}
```





## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/users/user
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'user')
```

### Response example
```
{'users': [
    {
        'id': 1,
        'email': 'petersen.peter@gmail.com',
        'first_name': 'Peter',
        'last_name': 'Petersen',
        'groups_own_json': [
            {'id': 9, 'name': 'my group1'},
            {'id': 13, 'name': 'Peters group'}
        ],
        'website': 'http://petersen.neuroscience.rocks/',
        'google_scholar': 'https://scholar.google.dk/citations?user=RywQhd8AAAAJ&hl',
        'orcid_id': 'https://orcid.org/0000-0002-2092-4791',
        'atlas_preference': 'AIA'
    },
    {
        'id': 16,
        'email': 'my@email.com',
        'first_name': 'New',
        'last_name': 'User',
        'groups_own_json': [],
        'website': '',
        'google_scholar': '',
        'orcid_id': '',
        'atlas_preference': 'AIA'
    }
]}
```


## Add
Users can only be added through the website Register form.


## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/users/user/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'user', id='16')
```

### Response example
```
{'user': {
    'id': 16,
    'email': 'my@email.com',
    'first_name': 'New',
    'last_name': 'User',
    'groups_own_json': [],
    'website': '',
    'google_scholar': '',
    'orcid_id': '',
    'atlas_preference': 'AIA'}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/users/user/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note:** Users can only change their own profiles, unless they are administrators.


### Use example (using Python API)
```
resp = save_model(settings, "user", id="16", data={"website": "www.someweb.com"})
```

### Response example
```
{'user': {
    'id': 16,
    'email': 'my@email.com',
    'first_name': 'New',
    'last_name': 'User',
    'groups_own_json': [],
    'website': 'http://www.someweb.com',
    'google_scholar': '',
    'orcid_id': '',
    'atlas_preference': 'AIA'}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** http://brainstem.org/rest/private/users/user/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

**Note:** only administrators can remove Users.

### Use example (using Python API)
```
resp = delete_model(settings, "user", id="16")
``` 
