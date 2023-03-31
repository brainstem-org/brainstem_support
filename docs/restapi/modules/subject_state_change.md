---
layout: default
title: Modules - Subject State Change
parent: API endpoints
grand_parent: REST API
nav_order: 3
---

## Table of contents
- [Fields](/brainstem_support/restapi/modules/subject_state_change/#fields)
- Endpoints
  - [List view](/brainstem_support/restapi/modules/subject_state_change/#list-view)
  - [Add](/brainstem_support/restapi/modules/subject_state_change/#add)
  - [Detail](/brainstem_support/restapi/modules/subject_state_change/#detail)
  - [Change](/brainstem_support/restapi/modules/subject_state_change/#change)
  - [Delete](/brainstem_support/restapi/modules/subject_state_change/#delete)

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | string with UUID identificator |
| `type` | string **[required]**. *See options below* |
| `description` | string |
| `subject` | string with the related subject ID **[required]** |
| `date_time` | string containing date (e.g. "2023-03-22") |
| `hardware_device` | string with the related hardware device ID |
| `brain_region` | string with the related brain region ID |
| `type_json` | JSON object. *See accepted schemas below* |
| `coordinates` | string **[required]**. *See options below* |
| `coordinates_json` | JSON object. *See accepted schemas below* |


These are the available `type` options for Subject State Change:
- `Death`
- `Slice`
- `PerfusionFixation`
- `Craniotomy`
- `BrainLesion`

A detailed list of the accepted schemas for the `type_json` field, related to each `type`, can be found in


These are the available `coordinates` options for Subject State Change:
- `External_XYZ_Absolute`
- `Stereotaxic_BregmaAbsolute`
- `Stereotaxic_BregmaBrainSurface`
- `Stereotaxic_LambdaAbsolute`
- `Stereotaxic_LambdaBrainSurface`
- `Stereotaxic_XYZ_Absolute`
- `Stereotaxic_XY_Surface`

A detailed list of the accepted schemas for the `coordinates_json` field, related to each `coordinates`, can be found in


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/modules/subjectstatechange
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'subjectstatechange')
```

### Response example
```
{'subject_state_changes': [
    {
        'id': '7791fcff-fcee-4c74-bfff-e2b3e4e38481',
        'type': 'Slice',
        'description': None,
        'subject': '0cdaf69d-63cf-429f-b549-fc0cc163d046',
        'date_time': None,
        'hardware_device': None,
        'type_json': {
            'thickness': 12,
            'nSlices': 7,
            'orientation': 0,
            'fatalOutcome': True
        },
        'brain_region': None,
        'coordinates': 'Stereotaxic_BregmaAbsolute',
        'coordinates_json': {
            'apCoordinates': 6.0,
            'mlCoordinates': 6.0,
            'dvCoordinates': 6.0,
            'apAngle': 0.0,
            'mlAngle': 0.0,
            'dvAngle': 0.0
        }
    },
    {
        'id': '3d8ba812-2237-4811-875d-96cfdca66e18',
        'type': 'Death',
        'description': None,
        'subject': '0f87c229-6769-4854-83a5-c71e154246b8',
        'date_time': None,
        'hardware_device': None,
        'type_json': {
            'causeOfDeath': 'boredom', 
            'fatalOutcome': True
        },
        'brain_region': None,
        'coordinates': 'Stereotaxic_BregmaBrainSurface',
        'coordinates_json': {}
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** http://brainstem.org/rest/private/modules/subjectstatechange
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = save_model(settings, "subjectstatechange",  data={
    "type": "Death",
    "subject": "0f87c229-6769-4854-83a5-c71e154246b8",
    "description": "some text",
    "type_json": {'causeOfDeath': 'Unknown', 'fatalOutcome': False},
    "coordinates": "Stereotaxic_BregmaAbsolute",
    "coordinates_json": {}})
```

### Response example
```
{'subject_state_change': {
    'id': '93925815-9f8e-4d39-9c3a-cf1d6e13f150',
    'type': 'Death',
    'description': 'some text',
    'subject': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'hardware_device': None,
    'type_json': {'causeOfDeath': 'Unknown', 'fatalOutcome': False},
    'brain_region': None,
    'coordinates': 'Stereotaxic_BregmaAbsolute',
    'coordinates_json': {}
    }
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/modules/subjectstatechange/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'subjectstatechange', id='93925815-9f8e-4d39-9c3a-cf1d6e13f150')
```

### Response example
```
{'subject_state_change': {
    'id': '93925815-9f8e-4d39-9c3a-cf1d6e13f150',
    'type': 'Death',
    'description': 'some text',
    'subject': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'hardware_device': None,
    'type_json': {'causeOfDeath': 'Unknown', 'fatalOutcome': False},
    'brain_region': None,
    'coordinates': 'Stereotaxic_BregmaAbsolute',
    'coordinates_json': {}
    }
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/modules/subjectstatechange/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = save_model(settings, "subjectstatechange", id="93925815-9f8e-4d39-9c3a-cf1d6e13f150", data={"description": "new text"})
```

### Response example
```
{'subject_state_change': {
    'id': '93925815-9f8e-4d39-9c3a-cf1d6e13f150',
    'type': 'Death',
    'description': 'new text',
    'subject': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'hardware_device': None,
    'type_json': {'causeOfDeath': 'Unknown', 'fatalOutcome': False},
    'brain_region': None,
    'coordinates': 'Stereotaxic_BregmaAbsolute',
    'coordinates_json': {}
    }
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** http://brainstem.org/rest/private/modules/subjectstatechange/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = delete_model(settings, "subjectstatechange", id="93925815-9f8e-4d39-9c3a-cf1d6e13f150")
``` 
