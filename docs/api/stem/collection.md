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
resp = client.load_model('collection')
```

### Response example
{: .no_toc}

```
{'collections': [
        {
            'id': '00000000-0000-0000-0000-000000000000',
            'name': 'newcollection1',
            'project': '00000000-0000-0000-0000-000000000000',
            'sessions': [
                            '00000000-0000-0000-0000-000000000000',
                            '00000000-0000-0000-0000-000000000000'
                        ]
        },
        {
            'id': '00000000-0000-0000-0000-000000000000',
            'name': 'collection2',
            'project': '00000000-0000-0000-0000-000000000000',
            'sessions': [
                            '00000000-0000-0000-0000-000000000000',
                            '00000000-0000-0000-0000-000000000000'
                        ]
        }
    ]
}
```


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/stem/collection
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("collection", data={"name": "NewRestCollection", "project": "00000000-0000-0000-0000-000000000000", "sessions": ["00000000-0000-0000-0000-000000000000"]})
```

### Response example
{: .no_toc}

```
{'collection': {
    'id': '00000000-0000-0000-0000-000000000000',
    'name': 'NewRestCollection',
    'project': '00000000-0000-0000-0000-000000000000',
    'sessions': ['00000000-0000-0000-0000-000000000000'],
    'links': {'sessions': 'sessions/'}
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
resp = client.load_model('collection', id='00000000-0000-0000-0000-000000000000')
```

### Response example
{: .no_toc}

```
{'collection': {
    'id': '00000000-0000-0000-0000-000000000000',
    'name': 'NewRestCollection',
    'project': '00000000-0000-0000-0000-000000000000',
    'sessions': ['00000000-0000-0000-0000-000000000000'],
    'links': {'sessions': 'sessions/'}
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
resp = client.save_model("collection", id="00000000-0000-0000-0000-000000000000", data={"name": "new name"})
```

### Response example
{: .no_toc}

```
{'collection': {
    'id': '00000000-0000-0000-0000-000000000000',
    'name': 'new name',
    'project': '00000000-0000-0000-0000-000000000000',
    'sessions': ['00000000-0000-0000-0000-000000000000'],
    'links': {'sessions': 'sessions/'}
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
resp = client.delete_model("collection", id="00000000-0000-0000-0000-000000000000")
```
