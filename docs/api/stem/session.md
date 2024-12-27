---
layout: default
title: Session
parent: STEM
grand_parent: API
nav_order: 3
---

# Session API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `name` | string **[required]** [max length: 100; must be unique]|
| `description` | string |
| `projects` | list of related projects IDs formatted as strings **[required]** |
| `date_time` | string containing date (e.g. "2023-03-22") |
| `epochs` | list of related epoch IDs formatted as strings **[read-only]** |
| `datastorage` | list of related data storage IDs formatted as strings **[read-only]** |
| `extra_fields` | list of JSON dictionaries. *See structure below* |
| `download_links` | list of JSON dictionaries. *See structure below* |
| `dataacquisition` | list of related data acquisition IDs formatted as strings **[read-only]** |
| `behaviors` | list of related behaviors IDs formatted as strings **[read-only]** |
| `manipulations` | list of related manipulations IDs formatted as strings **[read-only]** |
| `name_used_in_storage` | string [max length: 200]|
| `tags` | list of strings |


`extra_fields` is a list of JSON dictionaries with two elements, `name` and `value` like the example below. The name must start with a letter and can only consist of letters, numbers and underscore. The value can be a string or a numeric value. 

```
{
    "extra_property": "setting1", 
    "another_property: 22
}
```

`extra_fields` is a list of JSON dictionaries with two elements, `Repository` and `URL`, like the following example:

```
[
    {"Repository": "DANDI", "URL": "https://dandiarchive.org/dandiset/123456?pos=1"}, 
    {"Repository": "GitHub", "URL": "https://github.com/my_user/my_code"}
]
```



## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/session
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('session')
```

### Response example
{: .no_toc}

```
{'sessions': [
    {
        'id': '1a827c68-19b4-4cec-8ae5-e13c8f1de900',
        'name': 'session1',
        'description': '',
        'epochs': [],
        'projects': ['c4b8a90b-2963-4d13-aa07-b6f497252dde'],
        'date_time': None,
        'datastorage': [],
        'extra_fields': [],
        'download_links': [],
        'dataacquisition': [],
        'behaviors': [],
        'manipulations': ['20387176-5f3c-433a-8bf9-34a0f2c431f7'],
        'tags': [],
        'links': {'projects': 'projects/', 'manipulations': 'manipulations/'}
    },
    {
        'id': 'd8e72f9d-eb25-4280-a241-3317d5914055',
        'name': 'session2',
        'description': '',
        'epochs': [],
        'projects': ['c4b8a90b-2963-4d13-aa07-b6f497252dde'],
        'date_time': None,
        'datastorage': [],
        'extra_fields': [],
        'download_links': [],
        'dataacquisition': ['1c77ae53-6f83-4398-bfe5-6eb95ff00610'],
        'behaviors': [],
        'manipulations': [],
        'tags': [],
        'links': {'projects': 'projects/', 'manipulations': 'manipulations/'}
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/stem/session
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("session",  data={
	"name": "NewSession", 
	"description": "some text",  
	"projects": ["c4b8a90b-2963-4d13-aa07-b6f497252dde"]
})
```

### Response example
{: .no_toc}

```
{'session': {'id': '13bdd793-86d4-428e-9708-167bbc26f6d2',
    'name': 'NewSession',
    'description': 'some text',
    'epochs': [],
    'projects': ['c4b8a90b-2963-4d13-aa07-b6f497252dde'],
    'date_time': None,
    'datastorage': [],
    'extra_fields': [],
    'download_links': [],
    'dataacquisition': [],
    'behaviors': [],
    'manipulations': [],
    'tags': [],
    'links': {'projects': 'projects/'}}
}
```


## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/session/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('session', id='13bdd793-86d4-428e-9708-167bbc26f6d2')
```

### Response example
{: .no_toc}

```
{'session': {'id': '13bdd793-86d4-428e-9708-167bbc26f6d2',
    'name': 'NewSession',
    'description': 'some text',
    'epochs': [],
    'projects': ['c4b8a90b-2963-4d13-aa07-b6f497252dde'],
    'date_time': None,
    'datastorage': [],
    'extra_fields': {
        "extra_property": "setting1", 
        "another_property: 22
    },
    'download_links': [
        {"Repository": "DANDI", "URL": "https://dandiarchive.org/dandiset/123456?pos=1"}, 
        {"Repository": "GitHub", "URL": "https://github.com/my_user/my_code"}
    ],
    'dataacquisition': [],
    'behaviors': [],
    'manipulations': [],
    'tags': [],
    'links': {'projects': 'projects/'}}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/stem/session/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("session", id="13bdd793-86d4-428e-9708-167bbc26f6d2", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'session': {'id': '13bdd793-86d4-428e-9708-167bbc26f6d2',
    'name': 'NewSession',
    'description': 'new text',
    'epochs': [],
    'projects': ['c4b8a90b-2963-4d13-aa07-b6f497252dde'],
    'date_time': None,
    'datastorage': [],
    'extra_fields': [],
    'download_links': [],
    'dataacquisition': [],
    'behaviors': [],
    'manipulations': [],
    'tags': [],
    'links': {'projects': 'projects/'}}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/stem/session/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("session", id="13bdd793-86d4-428e-9708-167bbc26f6d2")
``` 
