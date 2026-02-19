---
layout: default
title: Procedure Log
parent: Modules
grand_parent: API
nav_order: 7
---

# Procedure Log API endpoint
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
| `procedure` | related procedure ID formatted as a string **[required]** |
| `entries` | list of log entries **[read-only]**. *See entries format below* |

`type` is writable on creation but treated as read-only on subsequent updates.

## Types of procedure logs

- `Impedances`: Impedances log
- `LinearDisplacement`: Linear displacement log
- `Tetrodes4`: Tetrode log (4 tetrodes)
- `Tetrodes8`: Tetrode log (8 tetrodes)


## Log entries

Each entry in the `entries` list is a dictionary with the following fields:

| Field        | Description  |
|:-------------|:-------------|
| `date_time` | string containing date and time (e.g. "2023-05-05T06:20:00Z") **[required]** |
| `notes` | string |
| `details` | JSON object. *See accepted schemas below* |

A detailed list of the available `type` options and accepted schemas for the `details` and `coordinates_details` fields can be found in the [Procedure log schemas documentation](/api/schemas/procedurelog).

## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/procedurelog
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('procedurelog')
```

### Response example
{: .no_toc}

```
{'procedure_logs': [
    {
        'id': '00000000-0000-0000-0000-000000000000',
        'type': 'Impedances',
        'description': None,
        'procedure': '00000000-0000-0000-0000-000000000000',
        'entries': [
            {'date_time': '2023-05-05T06:20:00Z',
             'notes': None,
             'details': {'impedances': 3.0, 'phases': None, 'channels': ''}},
            {'date_time': '2023-04-05T07:10:00Z',
             'notes': 'aa',
             'details': {'impedances': 2.0, 'phases': None, 'channels': ''}},
            {'date_time': '2023-03-26T13:20:00Z',
             'notes': None,
             'details': {'impedances': 1.0, 'phases': None, 'channels': ''}},
            {'date_time': '2023-03-13T07:10:00Z',
             'notes': None,
             'details': {'impedances': 2.0, 'phases': None, 'channels': ''}}
        ]
    },
    {
        'id': '00000000-0000-0000-0000-000000000000',
        'type': 'LinearDisplacement',
        'description': None,
        'procedure': '00000000-0000-0000-0000-000000000000',
        'entries': [
            {'date_time': '2023-04-05T13:45:00Z',
             'notes': None,
             'details': {'displacement': 9.0}},
            {'date_time': '2023-03-31T09:05:00Z',
             'notes': None,
             'details': {'displacement': 7.0}}
        ]
    }
]}
```

Public list responses also include a `meta` object (pagination/filter metadata).


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/modules/procedurelog
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("procedurelog",  data={
    "type": "LinearDisplacement",
    "procedure": "00000000-0000-0000-0000-000000000000"})
```

### Response example
{: .no_toc}

```
{'procedure_log': {
    'id': '00000000-0000-0000-0000-000000000000',
    'type': 'LinearDisplacement',
    'description': None,
    'procedure': '00000000-0000-0000-0000-000000000000',
    'entries': []}
}
```



## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/procedurelog/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('procedurelog', id='00000000-0000-0000-0000-000000000000')
```

### Response example
{: .no_toc}

```
{'procedure_log': {
    'id': '00000000-0000-0000-0000-000000000000',
    'type': 'LinearDisplacement',
    'description': None,
    'procedure': '00000000-0000-0000-0000-000000000000',
    'entries': []}
}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/procedurelog/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("procedurelog", id="00000000-0000-0000-0000-000000000000", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'procedure_log': {
    'id': '00000000-0000-0000-0000-000000000000',
    'type': 'LinearDisplacement',
    'description': "new text",
    'procedure': '00000000-0000-0000-0000-000000000000',
    'entries': []}
}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/modules/procedurelog/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("procedurelog", id="00000000-0000-0000-0000-000000000000")
```


## Add entry
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/procedurelog/<id\>/add_entry/
- **Data:** dictionary with the entry data
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("procedurelog", id="00000000-0000-0000-0000-000000000000", options="add_entry", data={
            'date_time': '2023-04-05T13:45:00Z',
            'notes': None,
            'details': {'displacement': 9.0}
        }
)
```

### Response example
{: .no_toc}

```
{'procedure_log': {
        'id': '00000000-0000-0000-0000-000000000000',
        'type': 'LinearDisplacement',
        'description': 'new text',
        'procedure': '00000000-0000-0000-0000-000000000000',
        'entries': [
            {'date_time': '2023-04-05T13:45:00Z',
            'notes': None,
            'details': {'displacement': 9.0}}
        ],
        'links': {'entries': 'entries/'}
    }
}
```

## Change entry
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/procedurelog/<id\>/change_entry/
- **Data:** dictionary with the entry data
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("procedurelog", id="00000000-0000-0000-0000-000000000000", options="change_entry", data={'date_time': '2023-04-05T13:45:00Z', 'notes': 'new text'})
```

### Response example
{: .no_toc}

```
{'procedure_log': {
        'id': '00000000-0000-0000-0000-000000000000',
        'type': 'LinearDisplacement',
        'description': 'new text',
        'procedure': '00000000-0000-0000-0000-000000000000',
        'entries': [
            {'date_time': '2023-04-05T13:45:00Z',
            'notes': "new text",
            'details': {'displacement': 9.0}}
        ],
        'links': {'entries': 'entries/'}
    }
}
```


## Remove entry
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/procedurelog/<id\>/remove_entry/
- **Data:** dictionary with the entry data
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("procedurelog", id="00000000-0000-0000-0000-000000000000", options="remove_entry", data={'date_time': '2023-04-05T13:45:00Z'})
```

### Response example
{: .no_toc}

```
{'procedure_log': {
        'id': '00000000-0000-0000-0000-000000000000',
        'type': 'LinearDisplacement',
        'description': 'new text',
        'procedure': '00000000-0000-0000-0000-000000000000',
        'entries': []
    }
}
```
