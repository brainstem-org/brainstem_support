---
layout: default
title: Dataset
parent: STEM
grand_parent: API
nav_order: 3
---

# Dataset API endpoint
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
| `epochs` | list of related actions IDs formatted as strings **[read-only]** |
| `datarepositories` | list of related data repositories IDs formatted as strings **[read-only]** |
| `extra_content_json` | list of JSON dictionaries. *See structure below* |
| `repository_links_json` | list of JSON dictionaries. *See structure below* |
| `experimentdata` | list of related experiment data IDs formatted as strings **[read-only]** |
| `behaviors` | list of related behaviors IDs formatted as strings **[read-only]** |
| `manipulations` | list of related manipulations IDs formatted as strings **[read-only]** |
| `name_used_in_repository` | string [max length: 200]|
| `tags` | list of strings |


`extra_content_json` is a list of JSON dictionaries with two elements, `key` and `value`, like the following example:

```
[
    {"key": "extra property", "value": "1"}, 
    {"key": "another property", "value": "2"}
]
```

`repository_links_json` is a list of JSON dictionaries with two elements, `Repository` and `URL`, like the following example:

```
[
    {"Repository": "DANDI", "URL": "https://dandiarchive.org/dandiset/123456?pos=1"}, 
    {"Repository": "GitHub", "URL": "https://github.com/my_user/my_code"}
]
```



## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/dataset
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'dataset')
```

### Response example
{: .no_toc}

```
{'datasets': [
    {
        'id': '1a827c68-19b4-4cec-8ae5-e13c8f1de900',
        'name': 'dataset1',
        'description': '',
        'epochs': [],
        'projects': ['c4b8a90b-2963-4d13-aa07-b6f497252dde'],
        'date_time': None,
        'datarepositories': [],
        'extra_content_json': [],
        'repository_links_json': [],
        'experimentdata': [],
        'behaviors': [],
        'manipulations': ['20387176-5f3c-433a-8bf9-34a0f2c431f7'],
        'tags': [],
        'links': {'projects': 'projects/', 'manipulations': 'manipulations/'}
    },
    {
        'id': 'd8e72f9d-eb25-4280-a241-3317d5914055',
        'name': 'dataset2',
        'description': '',
        'epochs': [],
        'projects': ['c4b8a90b-2963-4d13-aa07-b6f497252dde'],
        'date_time': None,
        'datarepositories': [],
        'extra_content_json': [],
        'repository_links_json': [],
        'experimentdata': ['1c77ae53-6f83-4398-bfe5-6eb95ff00610'],
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
- **URL:** https://www.brainstem.org/api/private/stem/dataset
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "dataset",  data={
	"name": "NewDataset", 
	"description": "some text",  
	"projects": ["c4b8a90b-2963-4d13-aa07-b6f497252dde"]
})
```

### Response example
{: .no_toc}

```
{'dataset': {'id': '3654964e-1bf7-40c7-a376-9dcec4c125cd',
    'name': 'NewDataset',
    'description': 'some text',
    'epochs': [],
    'projects': ['c4b8a90b-2963-4d13-aa07-b6f497252dde'],
    'date_time': None,
    'datarepositories': [],
    'extra_content_json': [],
    'repository_links_json': [],
    'experimentdata': [],
    'behaviors': [],
    'manipulations': [],
    'tags': [],
    'links': {'projects': 'projects/'}}
}
```


## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/dataset/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'dataset', id='3654964e-1bf7-40c7-a376-9dcec4c125cd')
```

### Response example
{: .no_toc}

```
{'dataset': {'id': '3654964e-1bf7-40c7-a376-9dcec4c125cd',
    'name': 'NewDataset',
    'description': 'some text',
    'epochs': [],
    'projects': ['c4b8a90b-2963-4d13-aa07-b6f497252dde'],
    'date_time': None,
    'datarepositories': [],
    'extra_content_json': [
        {"key": "extra property", "value": " 1"}, 
        {"key": "another property", "value": "2"}
    ],
    'repository_links_json': [
        {"Repository": "DANDI", "URL": "https://dandiarchive.org/dandiset/123456?pos=1"}, 
        {"Repository": "GitHub", "URL": "https://github.com/my_user/my_code"}
    ],
    'experimentdata': [],
    'behaviors': [],
    'manipulations': [],
    'tags': [],
    'links': {'projects': 'projects/'}}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/stem/dataset/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "dataset", id="3654964e-1bf7-40c7-a376-9dcec4c125cd", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'dataset': {'id': '3654964e-1bf7-40c7-a376-9dcec4c125cd',
    'name': 'NewDataset',
    'description': 'new text',
    'epochs': [],
    'projects': ['c4b8a90b-2963-4d13-aa07-b6f497252dde'],
    'date_time': None,
    'datarepositories': [],
    'extra_content_json': [],
    'repository_links_json': [],
    'experimentdata': [],
    'behaviors': [],
    'manipulations': [],
    'tags': [],
    'links': {'projects': 'projects/'}}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/stem/dataset/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = delete_model(settings, "dataset", id="3654964e-1bf7-40c7-a376-9dcec4c125cd")
``` 
