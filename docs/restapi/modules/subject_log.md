---
layout: default
title: Subject Log
parent: Modules
grand_parent: REST API
nav_order: 7
---

# Subject Log API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | string with UUID identificator |
| `type` | string **[required]**. *See options below* |
| `description` | string |
| `subject` | string with the related subject ID **[required]** |
| `entries` | list of log entries **[read-only]**. *See entries format below* |

These are the available `type` options for Subject Log:
- `FoodConsumption`
- `WaterConsumption`
- `Weighing`


Each entry in the `entries` list is a dictionary with the following fields:

| Field        | Description  |
|:-------------|:-------------|
| `date_time` | string containing date and time (e.g. "2023-05-05T06:20:00Z") **[required]** |
| `notes` | string |
| `type_json` | JSON object. *See accepted schemas below* |

A detailed list of the accepted schemas for the `type_json` field, related to each `type`, can be found in

## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/modules/subjectlog
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'subjectlog')
```

### Response example
{: .no_toc}

```
{'subject_logs': [
    {
        'id': '36570c8f-707b-4ead-950a-f924acf14c37',
        'type': 'Weighing',
        'description': None,
        'subject': '0f87c229-6769-4854-83a5-c71e154246b8',
        'entries': [
            {'date_time': '2023-03-26T04:05:00Z',
             'notes': None,
             'type_json': {'weight': 1254.0}},
            {'date_time': '2023-03-03T17:05:00Z',
             'notes': None,
             'type_json': {'weight': 23.0}}
         ],
        'links': {'entries': 'entries/'}
    },
    {
        'id': '8d7f3c37-69f5-4069-aca7-406f09de50f8',
        'type': 'FoodConsumption',
        'description': None,
        'subject': '0cdaf69d-63cf-429f-b549-fc0cc163d046',
        'entries': [
            {'date_time': '2023-03-09T07:10:00Z',
             'notes': None,
             'type_json': {'foodAmount': 1.0}},
            {'date_time': '2023-03-01T13:45:00Z',
             'notes': None,
             'type_json': {'foodAmount': 2.0}}
         ],
        'links': {'entries': 'entries/'}}
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** http://brainstem.org/rest/private/modules/subjectlog
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "subjectlog",  data={
    "type": "WaterConsumption",
    "subject": "0cdaf69d-63cf-429f-b549-fc0cc163d046"})
```

### Response example
{: .no_toc}

```
{'subject_log': {
    'id': '9c3a8cc7-da48-4061-a118-d9c7dc3105c3',
    'type': 'WaterConsumption',
    'description': None,
    'subject': '0cdaf69d-63cf-429f-b549-fc0cc163d046',
    'entries': []}
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/modules/subjectlog/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'subjectlog', id='9c3a8cc7-da48-4061-a118-d9c7dc3105c3')
```

### Response example
{: .no_toc}

```
{'subject_log': {
    'id': '9c3a8cc7-da48-4061-a118-d9c7dc3105c3',
    'type': 'WaterConsumption',
    'description': None,
    'subject': '0cdaf69d-63cf-429f-b549-fc0cc163d046',
    'entries': []}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/modules/subjectlog/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "subjectlog", id="9c3a8cc7-da48-4061-a118-d9c7dc3105c3", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'subject_log': {
    'id': '9c3a8cc7-da48-4061-a118-d9c7dc3105c3',
    'type': 'WaterConsumption',
    'description': "new text",
    'subject': '0cdaf69d-63cf-429f-b549-fc0cc163d046',
    'entries': []}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** http://brainstem.org/rest/private/modules/subjectlog/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = delete_model(settings, "subjectlog", id="9c3a8cc7-da48-4061-a118-d9c7dc3105c3")
```


## Add entry
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/modules/subjectlog/<id\>/add_entry/
- **Data:** dictionary with the entry data
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "subjectlog", id="9c3a8cc7-da48-4061-a118-d9c7dc3105c3", options="add_entry", data={
            'date_time': '2023-04-05T13:45:00Z',
            'notes': None,
            'type_json': {'waterAmount': 9.0}
        }
)
```

### Response example
{: .no_toc}

```
{'subject_log': 
    {
        'id': '9c3a8cc7-da48-4061-a118-d9c7dc3105c3',
        'type': 'WaterConsumption',
        'description': 'new text',
        'subject': '0cdaf69d-63cf-429f-b549-fc0cc163d046',
        'entries': [
            {'date_time': '2023-04-05T13:45:00Z',
            'notes': None,
            'type_json': {'waterAmount': 9.0}}
        ],
        'links': {'entries': 'entries/'}
    }
}
```

## Change entry
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/modules/subjectlog/<id\>/change_entry/
- **Data:** dictionary with the entry data
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "subjectlog", id="9c3a8cc7-da48-4061-a118-d9c7dc3105c3", options="change_entry", data={'date_time': '2023-04-05T13:45:00Z', 'notes': 'new text'})
```

### Response example
{: .no_toc}

```
{'subject_log': 
    {
        'id': '9c3a8cc7-da48-4061-a118-d9c7dc3105c3',
        'type': 'WaterConsumption',
        'description': 'new text',
        'subject': '0cdaf69d-63cf-429f-b549-fc0cc163d046',
        'entries': [
            {'date_time': '2023-04-05T13:45:00Z',
            'notes': 'new text',
            'type_json': {'waterAmount': 9.0}}
        ],
        'links': {'entries': 'entries/'}
    }
}
```



## Remove entry
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/modules/subjectlog/<id\>/remove_entry/
- **Data:** dictionary with the entry data
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "subjectlog", id="9c3a8cc7-da48-4061-a118-d9c7dc3105c3", options="remove_entry", data={'date_time': '2023-04-05T13:45:00Z'})
```

### Response example
{: .no_toc}

```
{'subject_log': {
    'id': '9c3a8cc7-da48-4061-a118-d9c7dc3105c3',
    'type': 'WaterConsumption',
    'description': "new text",
    'subject': '0cdaf69d-63cf-429f-b549-fc0cc163d046',
    'entries': []}
}
``` 
