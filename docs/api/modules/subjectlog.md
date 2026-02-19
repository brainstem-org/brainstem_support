---
layout: default
title: Subject Log
parent: Modules
grand_parent: API
nav_order: 8
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
| `id` | UUID identificator formatted as a string |
| `type` | string **[required]**. *See options below* |
| `description` | string [max length: 500] |
| `subject` | related subject ID formatted as a string **[required]** |
| `user` | ID of the user who created the log **[read-only]** |
| `entries` | list of log entries **[read-only]**. *See entries format below* |

`type` is writable on creation and becomes read-only afterwards. The `user` is automatically set to the authenticated user when the log is created.

## Types of subject logs

A detailed list of the available `type` options and accepted schemas for the `details` field can be found in the [Subject log schemas documentation](/api/schemas/subjectlog).


## Log entries

Entries are returned in one of two formats depending on the log `type`:

**Instantaneous entries** (most log types):

| Field        | Description  |
|:-------------|:-------------|
| `date_time` | string containing date and time (e.g. "2023-05-05T06:20:00Z") **[required]** |
| `notes` | string |
| `details` | JSON object. *See accepted schemas below* |

**Interval entries** (`Housing`, `FoodDeprivation`, `WaterDeprivation`, `Habituation`, `Handling`, `TrainingSession`):

| Field             | Description |
|:------------------|:------------|
| `start_date_time` | start of the interval (ISO 8601) **[required]** |
| `end_date_time`   | end of the interval (ISO 8601) **[required]** |
| `notes`           | string |
| `details`         | JSON object. *See accepted schemas below* |

A detailed list of the accepted schemas for the `details` field, related to each `type`, can be found in the JSON schema files under `modules/static/json/SubjectLog/` in the repository.

## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/subjectlog
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('subjectlog')
```

### Response example
{: .no_toc}

```
{'subject_logs': [
    {
        'id': '00000000-0000-0000-0000-000000000000',
        'type': 'Weighing',
        'description': None,
        'subject': '00000000-0000-0000-0000-000000000000',
        'user': '00000000-0000-0000-0000-000000000000',
        'entries': [
            {'date_time': '2023-03-26T04:05:00Z',
             'notes': None,
             'details': {'weight': 1254.0}},
            {'date_time': '2023-03-03T17:05:00Z',
             'notes': None,
             'details': {'weight': 23.0}}
         ]
    },
    {
        'id': '00000000-0000-0000-0000-000000000000',
        'type': 'FoodConsumption',
        'description': None,
        'subject': '00000000-0000-0000-0000-000000000000',
        'user': '00000000-0000-0000-0000-000000000000',
        'entries': [
            {'date_time': '2023-03-09T07:10:00Z',
             'notes': None,
             'details': {'foodAmount': 1.0}},
            {'date_time': '2023-03-01T13:45:00Z',
             'notes': None,
             'details': {'foodAmount': 2.0}}
         ]
    }
]}
```

Public list responses also include a `meta` object (pagination/filter metadata).


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/modules/subjectlog
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model(
    "subjectlog",
    data={
        "type": "WaterConsumption",
        "subject": "00000000-0000-0000-0000-000000000000",
        "description": "Baseline water access"
    }
)
```

### Response example
{: .no_toc}

```
{'subject_log': {
    'id': '00000000-0000-0000-0000-000000000000',
    'type': 'WaterConsumption',
    'description': 'Baseline water access',
    'subject': '00000000-0000-0000-0000-000000000000',
    'user': '00000000-0000-0000-0000-000000000000',
    'entries': []
}}
```



## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/subjectlog/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('subjectlog', id='00000000-0000-0000-0000-000000000000')
```

### Response example
{: .no_toc}

```
{'subject_log': {
    'id': '00000000-0000-0000-0000-000000000000',
    'type': 'WaterConsumption',
    'description': 'Baseline water access',
    'subject': '00000000-0000-0000-0000-000000000000',
    'user': '00000000-0000-0000-0000-000000000000',
    'entries': []
}}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/subjectlog/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model(
    "subjectlog",
    id="00000000-0000-0000-0000-000000000000",
    data={"description": "Post-deprivation monitoring"}
)
```

### Response example
{: .no_toc}

```
{'subject_log': {
    'id': '00000000-0000-0000-0000-000000000000',
    'type': 'WaterConsumption',
    'description': 'Post-deprivation monitoring',
    'subject': '00000000-0000-0000-0000-000000000000',
    'user': '00000000-0000-0000-0000-000000000000',
    'entries': []
}}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/modules/subjectlog/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("subjectlog", id="00000000-0000-0000-0000-000000000000")
```


## Add entry
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/subjectlog/<id\>/add_entry/
- **Data:** dictionary with the entry data
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("subjectlog", id="00000000-0000-0000-0000-000000000000", options="add_entry", data={
            'date_time': '2023-04-05T13:45:00Z',
            'notes': None,
            'details': {'waterAmount': 9.0}
        }
)
```

### Response example
{: .no_toc}

```
{'subject_log': {
    'id': '00000000-0000-0000-0000-000000000000',
    'type': 'WaterConsumption',
    'description': 'Post-deprivation monitoring',
    'subject': '00000000-0000-0000-0000-000000000000',
    'user': '00000000-0000-0000-0000-000000000000',
    'entries': [
        {'date_time': '2023-04-05T13:45:00Z',
         'notes': None,
         'details': {'waterAmount': 9.0}}
    ]
}}
```

## Change entry
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/subjectlog/<id\>/change_entry/
- **Data:** dictionary with the entry data
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model(
    "subjectlog",
    id="00000000-0000-0000-0000-000000000000",
    options="change_entry",
    data={'date_time': '2023-04-05T13:45:00Z', 'notes': 'Replaced drip line'}
)
```

### Response example
{: .no_toc}

```
{'subject_log': {
    'id': '00000000-0000-0000-0000-000000000000',
    'type': 'WaterConsumption',
    'description': 'Post-deprivation monitoring',
    'subject': '00000000-0000-0000-0000-000000000000',
    'user': '00000000-0000-0000-0000-000000000000',
    'entries': [
        {'date_time': '2023-04-05T13:45:00Z',
         'notes': 'Replaced drip line',
         'details': {'waterAmount': 9.0}}
    ]
}}
```



## Remove entry
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/subjectlog/<id\>/remove_entry/
- **Data:** dictionary with the entry data
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("subjectlog", id="00000000-0000-0000-0000-000000000000", options="remove_entry", data={'date_time': '2023-04-05T13:45:00Z'})
```

### Response example
{: .no_toc}

```
{'subject_log': {
    'id': '00000000-0000-0000-0000-000000000000',
    'type': 'WaterConsumption',
    'description': "new text",
    'subject': '00000000-0000-0000-0000-000000000000',
    'entries': []}
}
``` 
