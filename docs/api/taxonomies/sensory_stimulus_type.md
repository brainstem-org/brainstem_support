---
layout: default
title: Sensory stimulus type
parent: Taxonomies
grand_parent: API
nav_order: 7
---

# Sensory stimulus type API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | string with UUID identificator |
| `name` | string **[required]** [max length: 200; must be unique]|
| `description` | string **[required]** [max length: 500] |
| `comments` | string |



## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/sensorystimulustype
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'sensorystimulustype')
```

### Response example
{: .no_toc}

```
{'sensory_stimulus_types': [
    {
        'id': '78237811-35f6-4473-8c7e-c478d2fe3e61',
        'name': 'Auditory',
        'description': 'Auditory cue'
    },
    {
        'id': 'b1912fcf-14dd-4b3b-b779-2d076df50150',
        'name': 'Electrical',
        'description': 'Electrical cue'
    },
    {
        'id': '93e6d4d1-e6c7-4b81-bce9-a3324e2a5231',
        'name': 'Visual',
        'description': 'Visual cue'
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/taxonomies/sensorystimulustype
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: Sensory Stimulus Types submissions go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "sensorystimulustype",  data={
        "name": "MyNewSensoryStimulusType",
        "description": "some text",
    }
)
```

### Response example
{: .no_toc}

```
{'sensory_stimulus_type_approval': {
    'id': '9a4e8ce4-b7a1-4431-9176-514640681d59',
    'name': 'MyNewSensoryStimulusType',
    'description': 'some text',
    'comments': ''}
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/sensorystimulustype/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'sensorystimulustype', id='6094032c-c54f-4115-b8c8-139d93b98b80')
```

### Response example
{: .no_toc}

```
{'sensory_stimulus_type': {
    'id': '6094032c-c54f-4115-b8c8-139d93b98b80',
    'name': 'MyNewSensoryStimulusType',
    'description': 'some text'}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/sensorystimulustype/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: sensorystimulustypes changes go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "sensorystimulustype", id="6094032c-c54f-4115-b8c8-139d93b98b80", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'sensory_stimulus_type_approval': {
    'id': '06552cc2-a2db-44ea-90bc-8c529440acdd',
    'name': 'MyNewSensoryStimulusType',
    'description': 'new text',
    'comments': ''}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/taxonomies/sensorystimulustype/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

**Note**: only administrators can delete SensoryStimulusTypes.

### Use example (using Python API)
{: .no_toc}

```
resp = delete_model(settings, "sensorystimulustype", id="6094032c-c54f-4115-b8c8-139d93b98b80")
``` 


## List approvals
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/sensorystimulustype_approvals
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'sensorystimulustypeapproval')
```

### Response example
{: .no_toc}

```
{'sensory_stimulus_type_approvals': [
    {
        'id': '9a4e8ce4-b7a1-4431-9176-514640681d59',
        'name': 'MyNewSensoryStimulusType',
        'description': 'some text',
        'comments': '',
        'instance_id': None,
        'action': 'Add',
        'reviewer': None,
        'status': 'Pending'
    },
    {
        'id': '8ded8d4b-c30b-4dce-861d-03a74888962b',
        'name': 'NewCue',
        'description': '',
        'comments': '',
        'instance_id': 'd10cdc76-3395-4d2f-af55-ea8c846603a2',
        'action': 'Add',
        'reviewer': 3,
        'status': 'Accepted'
    }
]}
```


## Detail approval
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/sensorystimulustype_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'sensorystimulustypeapproval', id='9a4e8ce4-b7a1-4431-9176-514640681d59')
```

### Response example
{: .no_toc}

```
{'sensory_stimulus_type_approval': {
    'id': '9a4e8ce4-b7a1-4431-9176-514640681d59',
    'name': 'MyNewSensoryStimulusType',
    'description': 'some text',
    'comments': '',
    'instance_id': None,
    'action': 'Add',
    'reviewer': None,
    'status': 'Pending'}
}
```


## Accept approval
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/sensorystimulustype_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "sensorystimulustypeapproval", id="9a4e8ce4-b7a1-4431-9176-514640681d59", options="accept")
```


## Reject approval
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/sensorystimulustype_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "sensorystimulustypeapproval", id="06552cc2-a2db-44ea-90bc-8c529440acdd", options="reject")
```