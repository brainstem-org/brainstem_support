---
layout: default
title: Action Log
parent: Modules
grand_parent: REST API
nav_order: 3
---

# Action Log API endpoint
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
| `action` | string with the related action ID **[required]** |
| `entries` | list of log entries **[read-only]**. *See entries format below* |

These are the available `type` options for Action Log:
- `Impedances`
- `LinearDisplacement`


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
- **URL:** http://brainstem.org/rest/private/modules/actionlog
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'actionlog')
```

### Response example
```
{'action_logs': [
    {
        'id': '6a24ec67-59df-4da2-beae-c138102e69b1',
        'type': 'Impedances',
        'description': None,
        'action': '6a7c4ef9-f633-4b60-aa21-21d274ebab17',
        'entries': [
            {'date_time': '2023-05-05T06:20:00Z',
             'notes': None,
             'type_json': {'impedances': 3.0, 'phases': None, 'channels': ''}},
            {'date_time': '2023-04-05T07:10:00Z',
             'notes': 'aa',
             'type_json': {'impedances': 2.0, 'phases': None, 'channels': ''}},
            {'date_time': '2023-03-26T13:20:00Z',
             'notes': None,
             'type_json': {'impedances': 1.0, 'phases': None, 'channels': ''}},
            {'date_time': '2023-03-13T07:10:00Z',
             'notes': None,
             'type_json': {'impedances': 2.0, 'phases': None, 'channels': ''}}
        ],
        'links': {'entries': 'entries/'}
    },
    {
        'id': '88331276-e142-45ec-ae63-45a513881ed7',
        'type': 'LinearDisplacement',
        'description': None,
        'action': '61da7e53-1066-42de-a1a2-3db96bb7cba2',
        'entries': [
            {'date_time': '2023-04-05T13:45:00Z',
             'notes': None,
             'type_json': {'displacement': 9.0}},
            {'date_time': '2023-03-31T09:05:00Z',
             'notes': None,
             'type_json': {'displacement': 7.0}}
        ],
        'links': {'entries': 'entries/'}
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** http://brainstem.org/rest/private/modules/actionlog
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = save_model(settings, "actionlog",  data={
    "type": "LinearDisplacement",
    "action": "61da7e53-1066-42de-a1a2-3db96bb7cba2"})
```

### Response example
```
{'action_log': {
    'id': '743d9483-25d7-4c36-8b2a-e5f30dbbe062',
    'type': 'LinearDisplacement',
    'description': None,
    'action': '61da7e53-1066-42de-a1a2-3db96bb7cba2',
    'entries': []}
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/modules/actionlog/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'actionlog', id='743d9483-25d7-4c36-8b2a-e5f30dbbe062')
```

### Response example
```
{'action_log': {
    'id': '743d9483-25d7-4c36-8b2a-e5f30dbbe062',
    'type': 'LinearDisplacement',
    'description': None,
    'action': '61da7e53-1066-42de-a1a2-3db96bb7cba2',
    'entries': []}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/modules/actionlog/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = save_model(settings, "actionlog", id="743d9483-25d7-4c36-8b2a-e5f30dbbe062", data={"description": "new text"})
```

### Response example
```
{'action_log': {
    'id': '743d9483-25d7-4c36-8b2a-e5f30dbbe062',
    'type': 'LinearDisplacement',
    'description': "new text",
    'action': '61da7e53-1066-42de-a1a2-3db96bb7cba2',
    'entries': []}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** http://brainstem.org/rest/private/modules/actionlog/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = delete_model(settings, "actionlog", id="743d9483-25d7-4c36-8b2a-e5f30dbbe062")
```


## Add entry
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/modules/actionlog/<id\>/add_entry/
- **Data:** dictionary with the entry data
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = save_model(settings, "actionlog", id="743d9483-25d7-4c36-8b2a-e5f30dbbe062", options="add_entry", data={
            'date_time': '2023-04-05T13:45:00Z',
            'notes': None,
            'type_json': {'displacement': 9.0}
        }
)
```

### Response example
```
{'action_log': {
        'id': '743d9483-25d7-4c36-8b2a-e5f30dbbe062',
        'type': 'LinearDisplacement',
        'description': 'new text',
        'action': '61da7e53-1066-42de-a1a2-3db96bb7cba2',
        'entries': [
            {'date_time': '2023-04-05T13:45:00Z',
            'notes': None,
            'type_json': {'displacement': 9.0}}
        ],
        'links': {'entries': 'entries/'}
    }
}
```

## Change entry
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/modules/actionlog/<id\>/change_entry/
- **Data:** dictionary with the entry data
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = save_model(settings, "actionlog", id="743d9483-25d7-4c36-8b2a-e5f30dbbe062", options="change_entry", data={'date_time': '2023-04-05T13:45:00Z', 'notes': 'new text'})
```

### Response example
```
{'action_log': {
        'id': '743d9483-25d7-4c36-8b2a-e5f30dbbe062',
        'type': 'LinearDisplacement',
        'description': 'new text',
        'action': '61da7e53-1066-42de-a1a2-3db96bb7cba2',
        'entries': [
            {'date_time': '2023-04-05T13:45:00Z',
            'notes': "new text",
            'type_json': {'displacement': 9.0}}
        ],
        'links': {'entries': 'entries/'}
    }
}
```



## Remove entry
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/modules/actionlog/<id\>/remove_entry/
- **Data:** dictionary with the entry data
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = save_model(settings, "actionlog", id="743d9483-25d7-4c36-8b2a-e5f30dbbe062", options="remove_entry", data={'date_time': '2023-04-05T13:45:00Z'})
```

### Response example
```
{'action_log': {
        'id': '743d9483-25d7-4c36-8b2a-e5f30dbbe062',
        'type': 'LinearDisplacement',
        'description': 'new text',
        'action': '61da7e53-1066-42de-a1a2-3db96bb7cba2',
        'entries': []
    }
}
```