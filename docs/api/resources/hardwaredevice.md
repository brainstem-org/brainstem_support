---
layout: default
title: Hardware Device
parent: Resources
grand_parent: API
nav_order: 6
---

# Hardware Device API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `name` | string **[required]** [max length: 100; must be unique] |
| `description` | string [max length: 500] |
| `supplier` | related supplier ID formatted as a string **[required]** |
| `rrid` | Research Resource Identifier (RRID) |
| `rrid_url` | URL to RRID lookup page **[read-only]** |
| `external_identifiers` | JSON object containing external identifier information |
| `comments` | string, used when proposing approval changes |

Optional fields such as `comments` can be omitted from list/detail responses when empty.



## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/resources/hardwaredevice
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('hardwaredevice')
```

### Response example
{: .no_toc}

```
{'hardwaredevices': [
    {
        'id': '<id>',
        'name': 'RZ5D Processor',
        'description': '',
        'supplier': '<supplier-id>',
        'rrid': '',
        'rrid_url': '',
        'external_identifiers': []
    },
    {
        'id': '<id>',
        'name': 'Scout (128ch)',
        'description': '',
        'supplier': '<supplier-id>',
        'rrid': '',
        'rrid_url': '',
        'external_identifiers': []
    },
    {
        'id': '<id>',
        'name': 'SmartBox (256ch)',
        'description': '',
        'supplier': '<supplier-id>',
        'rrid': '',
        'rrid_url': '',
        'external_identifiers': []
    },
    {
        'id': '<id>',
        'name': 'SpikeGLX',
        'description': 'SpikeGLX is a recording system for extracellular neural probes',
        'supplier': '<supplier-id>',
        'rrid': '',
        'rrid_url': '',
        'external_identifiers': []
    }
]}
```

Public list responses also include a `meta` object (pagination/filter metadata).


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/resources/hardwaredevice
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: hardwaredevices submissions go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("hardwaredevice",  data={
    'name': 'MyNewHardwareDevice',
    'description': '',
    'supplier': '<supplier-id>'}
)
```

### Response example
{: .no_toc}

```
{'hardwaredevice_approval': {
    'id': '<id>',
    'name': 'MyNewHardwareDevice',
    'description': '',
    'supplier': '<supplier-id>'}
}
```



## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/resources/hardwaredevice/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('hardwaredevice', id='<id>')
```

### Response example
{: .no_toc}

```
{'hardwaredevice': {
    'id': '<id>',
    'name': 'MyNewHardwareDevice',
    'description': '',
    'supplier': '<supplier-id>',
    'rrid': '',
    'rrid_url': '',
    'external_identifiers': []}
}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/resources/hardwaredevice/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: hardwaredevices changes go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("hardwaredevice", id="<id>", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'hardwaredevice_approval': {
    'id': '<id>',
    'name': 'MyNewHardwareDevice',
    'description': 'new text',
    'supplier': '<supplier-id>'}
}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/resources/hardwaredevice/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

**Note**: only administrators can delete Hardware Devices.


### Use example (using Python API)
{: .no_toc}

{: .no_toc}

```
resp = client.delete("hardwaredevice", id="<id>")
``` 


## List approvals
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/resources/hardwaredeviceapproval
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

{: .no_toc}

```
resp = client.load('hardwaredeviceapproval')
```

### Response example
{: .no_toc}

{: .no_toc}

```
{'hardwaredevice_approvals': [
    {
        'id': '<id>',
        'name': 'MyNewHardwareDevice',
        'description': '',
        'supplier': '<supplier-id>',
        'instance_id': None,
        'action': 'Add',
        'reviewer': None,
        'status': 'Pending'
    },
    {
        'id': '<id>',
        'name': '16-Ch Extracellular Differential AC Amplifier Model 3500',
        'description': '123',
        'supplier': '<supplier-id>',
        'instance_id': '<instance_id-id>',
        'action': 'Change',
        'reviewer': 15,
        'status': 'Accepted'
    }
]}
```

Approval list responses also include a `meta` object (pagination/filter metadata).


## Detail approval
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/resources/hardwaredeviceapproval/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('hardwaredeviceapproval', id='<id>')
```

### Response example
{: .no_toc}

```
{'hardwaredevice_approval': {
    'id': '<id>',
    'name': 'MyNewHardwareDevice',
    'description': '',
    'supplier': '<supplier-id>',
    'instance_id': None,
    'action': 'Add',
    'reviewer': None,
    'status': 'Pending'}
}
```


## Accept approval
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/resources/hardwaredeviceapproval/<id\>/accept/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("hardwaredeviceapproval", id="<id>", options="accept")
```


## Reject approval
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/resources/hardwaredeviceapproval/<id\>/reject/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("hardwaredeviceapproval", id="<id>", options="reject")
```
