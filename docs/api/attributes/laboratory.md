---
layout: default
title: Laboratory
parent: General attributes
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
| `group` | related group ID formatted as a string **[required]** |
| `principal_investigators` | list of related principal investigators IDs formatted as strings **[required]** |
| `description` | string [max length: 500] |
| `website` | string [max length: 200] |
| `department` | string [max length: 100] |
| `institution` | string **[required]** [max length: 100] |
| `city` | string [max length: 100] |
| `country` | string [max length: 100] |


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/attributes/laboratory
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'laboratory')
```

### Response example
{: .no_toc}

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
- **URL:** https://www.brainstem.org/api/private/attributes/laboratory
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "laboratory",  data={
    'group': 41,
    'principal_investigators': [3],
    'institution': 'A university'}
)
```

### Response example
{: .no_toc}

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
- **URL:** https://www.brainstem.org/api/private/attributes/laboratory/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'laboratory', id='5d882f8b-5c74-428e-9ed9-41c8780527ff')
```

### Response example
{: .no_toc}

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
- **URL:** https://www.brainstem.org/api/private/attributes/laboratory/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "laboratory", id="5d882f8b-5c74-428e-9ed9-41c8780527ff", data={"description": "new text"})
```

### Response example
{: .no_toc}

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
- **URL:** https://www.brainstem.org/api/private/attributes/laboratory/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = delete_model(settings, "laboratory", id="5d882f8b-5c74-428e-9ed9-41c8780527ff")
``` 
