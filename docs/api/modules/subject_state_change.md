---
layout: default
title: Subject State Change
parent: Modules
grand_parent: API
nav_order: 5
---

# Subject State Change API endpoint
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
| `date_time` | string containing date (e.g. "2023-03-22") |
| `hardware_device` | related hardware device ID formatted as a string |
| `brain_region` | related brain region ID formatted as a string |
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
- **URL:** https://www.brainstem.org/api/private/modules/subjectstatechange
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'subjectstatechange')
```

### Response example
{: .no_toc}

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
- **URL:** https://www.brainstem.org/api/private/modules/subjectstatechange
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

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
{: .no_toc}

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
- **URL:** https://www.brainstem.org/api/private/modules/subjectstatechange/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'subjectstatechange', id='93925815-9f8e-4d39-9c3a-cf1d6e13f150')
```

### Response example
{: .no_toc}

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
- **URL:** https://www.brainstem.org/api/private/modules/subjectstatechange/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "subjectstatechange", id="93925815-9f8e-4d39-9c3a-cf1d6e13f150", data={"description": "new text"})
```

### Response example
{: .no_toc}

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
- **URL:** https://www.brainstem.org/api/private/modules/subjectstatechange/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = delete_model(settings, "subjectstatechange", id="93925815-9f8e-4d39-9c3a-cf1d6e13f150")
``` 
