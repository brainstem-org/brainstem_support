---
layout: default
title: Collection
parent: STEM
grand_parent: API
nav_order: 4
---

# Collection API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `name` | string **[required]** [max length: 100]|
| `description` | string |
| `project` | related project ID formatted as a string **[required]** |
| `sessions` | list of related sessions IDs formatted as strings |
| `tags` | list of strings |

## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/collection
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('collection')
```

### Response example
{: .no_toc}

```
{'collections': [
        {
            'id': '<id>',
            'name': 'newcollection1',
            'project': '<project-id>',
            'sessions': [
                            '<id>',
                            '<id>'
                        ]
        },
        {
            'id': '<id>',
            'name': 'collection2',
            'project': '<project-id>',
            'sessions': [
                            '<id>',
                            '<id>'
                        ]
        }
    ]
}
```

Public list responses also include a `meta` object (pagination/filter metadata).


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/stem/collection
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("collection", data={"name": "NewRestCollection", "project": "<project-id>", "sessions": ["<id>"]})
```

### Response example
{: .no_toc}

```
{'collection': {
    'id': '<id>',
    'name': 'NewRestCollection',
    'project': '<project-id>',
    'sessions': ['<id>']
    }
}
```



## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/collection/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('collection', id='<id>')
```

### Response example
{: .no_toc}

```
{'collection': {
    'id': '<id>',
    'name': 'NewRestCollection',
    'project': '<project-id>',
    'sessions': ['<id>']
    }
}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/stem/collection/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save("collection", id="<id>", data={"name": "new name"})
```

### Response example
{: .no_toc}

```
{'collection': {
    'id': '<id>',
    'name': 'new name',
    'project': '<project-id>',
    'sessions': ['<id>']
    }
}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/stem/collection/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete("collection", id="<id>")
```
