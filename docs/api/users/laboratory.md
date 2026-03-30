---
layout: default
title: Laboratory
parent: Users
grand_parent: API
nav_order: 4
---

# Laboratory API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `group` | related group ID formatted as an integer **[required]** |
| `principal_investigators` | list of related principal investigator IDs formatted as integers **[required]** |
| `description` | string [max length: 500] |
| `website` | string [max length: 200] |
| `department` | string [max length: 100] |
| `institution` | string **[required]** [max length: 100] |
| `city` | string [max length: 100] |
| `country` | string [max length: 100] |


## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/laboratory
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('laboratory')
```

### Response example
{: .no_toc}

```
{'laboratories': [
    {
        'id': '<id>',
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
        'id': '<id>',
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

Public list responses also include a `meta` object (pagination/filter metadata).


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/users/laboratory
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save("laboratory",  data={
    'group': 41,
    'principal_investigators': [3],
    'institution': 'A university'}
)
```

### Response example
{: .no_toc}

```
{'laboratory': {
    'id': '<id>',
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
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/laboratory/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('laboratory', id='<id>')
```

### Response example
{: .no_toc}

```
{'laboratory': {
    'id': '<id>',
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
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/users/laboratory/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save("laboratory", id="<id>", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'laboratory': {
    'id': '<id>',
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
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/users/laboratory/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete("laboratory", id="<id>")
``` 
