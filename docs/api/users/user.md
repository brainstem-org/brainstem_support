---
layout: default
title: User
parent: Users
grand_parent: API
nav_order: 1
---

# User API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | integer user ID |
| `email` | string [must be unique]|
| `first_name` | string |
| `last_name` | string |
| `groups_own_json` | list of dictionaries with each group owned by the user. *See structure below* |
| `website` | string [max length: 200] |
| `google_scholar` | string [max length: 200] |
| `orcid_id` | string [max length: 100] |
| `atlas_preference` | string [max length: 7]|
| `active_projects` | list of related project IDs |

Each dictionary in the `groups_own_json` list contains the group's `id` and `name`:
```
{'id': 8, 'name': 'test_group'}
```

## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/user
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}


```
resp = client.load_model('user')
```

### Response example
{: .no_toc}


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
        'website': 'https://petersenlab.org/',
        'google_scholar': 'https://scholar.google.dk/citations?user=RywQhd8AAAAJ&hl',
        'orcid_id': 'https://orcid.org/0000-0002-2092-4791',
        'atlas_preference': 'AIA',
        'active_projects': []
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
        'atlas_preference': 'AIA',
        'active_projects': []
    }
]}
```

Public list responses also include a `meta` object (pagination/filter metadata).


## Add
Users can only be added through the website Register form.


## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/user/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}


```
resp = client.load_model('user', id='16')
```

### Response example
{: .no_toc}

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
    'atlas_preference': 'AIA',
    'active_projects': []}
}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/users/user/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note:** Users can only change their own profiles, unless they are administrators.


### Use example (using Python API)
{: .no_toc}


```
resp = client.save_model("user", id="16", data={"website": "www.someweb.com"})
```

### Response example
{: .no_toc}


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
    'atlas_preference': 'AIA',
    'active_projects': []}
}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/users/user/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

**Note:** only administrators can remove Users.

### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("user", id="16")
``` 
