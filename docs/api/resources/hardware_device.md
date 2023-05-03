---
layout: default
title: Hardware Device
parent: Resources
grand_parent: REST API
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
| `id` | string with UUID identificator |
| `name` | string **[required]** [max length: 100; must be unique] |
| `description` | string [max length: 500] |
| `supplier` | string with the related supplier ID **[required]** |
| `comments` | string |


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/resources/hardware_device
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'hardwaredevice')
```

### Response example
{: .no_toc}

```
{'hardware_devices': [
    {
        'id': 'a14cc671-6d21-4688-9772-1d2bf765b793',
        'name': 'RZ5D Processor',
        'description': '',
        'supplier': '56c6f4c3-cf31-48ac-bd16-410123776324'
    },
    {
        'id': '33c67482-af52-44f4-a3ef-6d692512a6ca',
        'name': 'Scout (128ch)',
        'description': '',
        'supplier': 'f309ec90-914b-4382-955e-017bf5d1def1'
    },
    {
        'id': '4d33e7ad-c141-4e9d-bc9c-034c51dcfc5a',
        'name': 'SmartBox (256ch)',
        'description': '',
        'supplier': 'fba48e24-eebf-4b11-a8b9-ac660854d779'
    },
    {
        'id': '3ca40603-b7f0-4d58-8579-d48b3d6e7ad6',
        'name': 'SpikeGLX',
        'description': 'SpikeGLX is a recording system for extracellular neural probes',
        'supplier': 'b8146db2-f50e-40c0-9558-1df3586a3b08'
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/resources/hardware_device
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: hardware_devices submissions go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "hardwaredevice",  data={
    'name': 'MyNewHardwareDevice',
    'description': '',
    'supplier': 'b8146db2-f50e-40c0-9558-1df3586a3b08'}
)
```

### Response example
{: .no_toc}

```
{'hardware_device_approval': {
    'id': '23105f29-f31d-47c8-9cc5-0198222ee7dd',
    'name': 'MyNewHardwareDevice',
    'description': '',
    'supplier': 'b8146db2-f50e-40c0-9558-1df3586a3b08',
    'comments': ''}
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/resources/hardware_device/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'hardwaredevice', id='0e6c723c-e5f8-4979-b7f9-e77a3ae4e817')
```

### Response example
{: .no_toc}

```
{'hardware_device': {
    'id': '0e6c723c-e5f8-4979-b7f9-e77a3ae4e817',
    'name': 'MyNewHardwareDevice',
    'description': '',
    'supplier': 'b8146db2-f50e-40c0-9558-1df3586a3b08'}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/resources/hardware_device/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: hardware_devices changes go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "hardwaredevice", id="0e6c723c-e5f8-4979-b7f9-e77a3ae4e817", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'hardware_device_approval': {
    'id': 'd10aaf4c-be23-45b2-9f81-ef1d65ca6c32',
    'name': 'MyNewHardwareDevice',
    'description': 'new text',
    'supplier': 'b8146db2-f50e-40c0-9558-1df3586a3b08',
    'comments': ''}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/resources/hardware_device/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

**Note**: only administrators can delete Hardware Devices.


### Use example (using Python API)
{: .no_toc}

{: .no_toc}

```
resp = delete_model(settings, "hardwaredevice", id="0e6c723c-e5f8-4979-b7f9-e77a3ae4e817")
``` 


## List approvals
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/resources/hardware_device_approvals
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

{: .no_toc}

```
resp = load_model(settings, 'hardwaredeviceapproval')
```

### Response example
{: .no_toc}

{: .no_toc}

```
{'hardware_device_approvals': [
    {
        'id': '23105f29-f31d-47c8-9cc5-0198222ee7dd',
        'name': 'MyNewHardwareDevice',
        'description': '',
        'supplier': 'b8146db2-f50e-40c0-9558-1df3586a3b08',
        'comments': '',
        'instance_id': None,
        'action': 'Add',
        'reviewer': None,
        'status': 'Pending'
    },
    {
        'id': 'accd5fe5-6739-4e44-ba24-3910eff01fef',
        'name': '16-Ch Extracellular Differential AC Amplifier Model 3500',
        'description': '123',
        'supplier': '866fda99-0ae7-4aeb-a163-5c2e8a3ed4af',
        'comments': '',
        'instance_id': '56854ab5-708b-48b2-92a8-3bd84439c1e0',
        'action': 'Change',
        'reviewer': 15,
        'status': 'Accepted'
    }
]}
```


## Detail approval
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/resources/hardware_device_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'hardwaredeviceapproval', id='23105f29-f31d-47c8-9cc5-0198222ee7dd')
```

### Response example
{: .no_toc}

```
{'hardware_device_approval': {
    'id': '23105f29-f31d-47c8-9cc5-0198222ee7dd',
    'name': 'MyNewHardwareDevice',
    'description': '',
    'supplier': 'b8146db2-f50e-40c0-9558-1df3586a3b08',
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
- **URL:** https://www.brainstem.org/api/private/resources/hardware_device_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "hardwaredeviceapproval", id="23105f29-f31d-47c8-9cc5-0198222ee7dd", options="accept")
```


## Reject approval
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/resources/hardware_device_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "hardwaredeviceapproval", id="fd7f6132-0527-4310-a9da-9241728a9163", options="reject")
```