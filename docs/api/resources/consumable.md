---
layout: default
title: Consumable
parent: Resources
grand_parent: API
nav_order: 6
---

# Consumable API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `name` | string **[required]** [max length: 100; must be unique]|
| `description` | string [max length: 500] |
| `supplier` | related supplier ID formatted as a string **[required]** |
| `type` | string **[required]**. *See options below* |
| `details` | JSON object. *See accepted schemas below* |
| `rrid` | Research Resource Identifier (RRID) |
| `rrid_url` | URL to RRID lookup page **[read-only]** |
| `external_identifiers` | JSON object containing external identifier information |
| `comments` | string, used when proposing approval changes |

A detailed list of the available `type` options and accepted schemas for the `details` field can be found in the [Consumable schemas documentation](/api/schemas/consumable.md).


## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/resources/consumable
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('consumable')
```

### Response example
{: .no_toc}

```
{"consumables": [
    {
        "id": "0a533099-700a-4d9b-a3db-87be8d137770",
        "name": "AAV-EF1a-mCherry-IRES-WGA-Cre ",
        "description": "Transsynaptic Tracers: WGA-Cre (AAV2, 5 & 8)",
        "supplier": "4fa1c3b4-f955-47f5-8524-3f1afa3fc657",
        "type": "VirusConstruct",
        "rrid": "",
        "rrid_url": "",
        "external_identifiers": [],
        "details": {
            "virus_type": "AAV",
            "notes": "Transsynaptic Tracers: WGA-Cre (AAV2, 5 & 8)"
        }
    },
    {
        "id": "3e3a4787-a688-485a-bdc6-c0cb1a2a23e1",
        "name": "A16x1-2mm-100-177",
        "description": "",
        "supplier": "fba48e24-eebf-4b11-a8b9-ac660854d779",
        "type": "SiliconProbeDesign",
        "rrid": "",
        "rrid_url": "",
        "external_identifiers": [],
        "details": {
            "product_id": "A16x1-2mm-100-177",
            "shanksLength": 2,
            "nChannels": 16,
            "nShanks": 16,
            "shanksSpacing": 100,
            "siteArea": 177,
            "layout": "linear",
            "uniformLayout": true,
            "customDesign": false
        }
    }
]}
```

Public list responses also include a `meta` object (pagination/filter metadata).


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/resources/consumable
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: consumables submissions go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("consumable",  data={
        "name": "MyNewConsumable",
        "description": "",
        "supplier": "fba48e24-eebf-4b11-a8b9-ac660854d779",
        "type": "OpticFiberDesign",
        "details": {
            "productId": "42",
            "tipDescription": "",
            "coreDiameter": 0,
            "outerDiameter": 100,
            "aperture": 0.2
        }
    }
)
```

### Response example
{: .no_toc}

```
{'consumable_approval': {
        'id': 'b7595523-5578-45c0-b7ef-c1f1485ac041',
        'name': 'MyNewConsumable',
        'description': '',
        'supplier': 'fba48e24-eebf-4b11-a8b9-ac660854d779',
        'type': 'OpticFiberDesign',
        'details': {
            'productId': '42',
            'tipDescription': '',
            'coreDiameter': 0,
            'outerDiameter': 100,
            'aperture': 0.2
        }
    }
}
```



## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/resources/consumable/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('consumable', id='67f263cd-5960-406f-a879-c1f259140979')
```

### Response example
{: .no_toc}

```
{'consumable': {
        'id': '67f263cd-5960-406f-a879-c1f259140979',
        'name': 'MyNewConsumable',
        'description': '',
        'supplier': 'fba48e24-eebf-4b11-a8b9-ac660854d779',
        'type': 'OpticFiberDesign',
        'rrid': '',
        'rrid_url': '',
        'external_identifiers': [],
        'details': {
            'productId': '42',
            'tipDescription': '',
            'coreDiameter': 0,
            'outerDiameter': 100,
            'aperture': 0.2
        }
    }
}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/resources/consumable/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: consumables changes go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("consumable", id="67f263cd-5960-406f-a879-c1f259140979", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'consumable_approval': {
        'id': '8cf7d857-a197-4e36-9e0c-1766bb6aa285',
        'name': 'MyNewConsumable',
        'description': 'new text',
        'supplier': 'fba48e24-eebf-4b11-a8b9-ac660854d779',
        'type': 'OpticFiberDesign',
        'details': {
            'productId': '42',
            'tipDescription': '',
            'coreDiameter': 0,
            'outerDiameter': 100,
            'aperture': 0.2
        }
    }
}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/resources/consumable/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

**Note**: only administrators can delete Consumables.

### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("consumable", id="67f263cd-5960-406f-a879-c1f259140979")
``` 


## List approvals
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/resources/consumableapproval
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('consumableapproval')
```

### Response example
{: .no_toc}

```
{"consumable_approvals": [
    {
        "id": "b7595523-5578-45c0-b7ef-c1f1485ac041",
        "name": "MyNewConsumable",
        "description": "",
        "supplier": "fba48e24-eebf-4b11-a8b9-ac660854d779",
        "type": "OpticFiberDesign",
        "details": {
            "productId": "42",
            "tipDescription": "",
            "coreDiameter": 0,
            "outerDiameter": 100,
            "aperture": 0.2
        },
        "instance_id": null,
        "action": "Add",
        "reviewer": null,
        "status": "Pending"
    }
]}
```

Approval list responses also include a `meta` object (pagination/filter metadata).


## Detail approval
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/resources/consumableapproval/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('consumableapproval', id='b7595523-5578-45c0-b7ef-c1f1485ac041')
```

### Response example
{: .no_toc}

```
{'consumable_approval': {
        'id': 'b7595523-5578-45c0-b7ef-c1f1485ac041',
        'name': 'MyNewConsumable',
        'description': '',
        'supplier': 'fba48e24-eebf-4b11-a8b9-ac660854d779',
        'type': 'OpticFiberDesign',
        'details': {
            'productId': '42',
            'tipDescription': '',
            'coreDiameter': 0,
            'outerDiameter': 100,
            'aperture': 0.2
        },
        'instance_id': None,
        'action': 'Add',
        'reviewer': None,
        'status': 'Pending'
    }
}
```


## Accept approval
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/resources/consumableapproval/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("consumableapproval", id="b7595523-5578-45c0-b7ef-c1f1485ac041", options="accept")
```


## Reject approval
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/resources/consumableapproval/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("consumableapproval", id="8cf7d857-a197-4e36-9e0c-1766bb6aa285", options="reject")
```
