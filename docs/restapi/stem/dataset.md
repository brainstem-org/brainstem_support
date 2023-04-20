---
layout: default
title: Stem - Dataset
parent: API endpoints
grand_parent: REST API
nav_order: 2
---

## Table of contents
- [Fields](/brainstem_support/restapi/stem/dataset/#fields)
- Endpoints
  - [List view](/brainstem_support/restapi/stem/dataset/#list-view)
  - [Add](/brainstem_support/restapi/stem/dataset/#add)
  - [Detail](/brainstem_support/restapi/stem/dataset/#detail)
  - [Change](/brainstem_support/restapi/stem/dataset/#change)
  - [Delete](/brainstem_support/restapi/stem/dataset/#delete)

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | string with UUID identificator |
| `name` | string **[required]** |
| `description` | string |
| `projects` | list of strings representing the related projects IDs **[required]** |
| `date_time` | string containing date (e.g. "2023-03-22") |
| `epochs` | list of strings representing the related actions IDs **[read-only]** |
| `datarepositories` | list of strings representing the related dataset state changes IDs **[read-only]** |
| `extra_content_json` | JSON dictionary |
| `repository_links_json` | JSON dictionary |
| `experimentdata` | list of strings representing the related experiment data IDs **[read-only]** |
| `behaviors` | list of strings representing the related behaviors IDs **[read-only]** |
| `manipulations` | list of strings representing the related manipulations IDs **[read-only]** |
| `tags` | list of strings |



## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/stem/dataset
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'dataset')
```

### Response example
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
- **URL:** http://brainstem.org/rest/private/stem/dataset
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = save_model(settings, "dataset",  data={
	"name": "NewDataset", 
	"description": "some text",  
	"projects": ["c4b8a90b-2963-4d13-aa07-b6f497252dde"]
})
```

### Response example
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
- **URL:** http://brainstem.org/rest/private/stem/dataset/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'dataset', id='3654964e-1bf7-40c7-a376-9dcec4c125cd')
```

### Response example
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


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/stem/dataset/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = save_model(settings, "dataset", id="3654964e-1bf7-40c7-a376-9dcec4c125cd", data={"description": "new text"})
```

### Response example
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
- **URL:** http://brainstem.org/rest/private/stem/dataset/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = delete_model(settings, "dataset", id="3654964e-1bf7-40c7-a376-9dcec4c125cd")
``` 
