---
layout: default
title: Resources - Consumable
parent: API endpoints
grand_parent: REST API
nav_order: 6
---

## Table of contents
- [Fields](/brainstem_support/restapi/resources/consumable/#fields)
- Endpoints
  - [List view](/brainstem_support/restapi/resources/consumable/#list-view)
  - [Add](/brainstem_support/restapi/resources/consumable/#add)
  - [Detail](/brainstem_support/restapi/resources/consumable/#detail)
  - [Change](/brainstem_support/restapi/resources/consumable/#change)
  - [Delete](/brainstem_support/restapi/resources/consumable/#delete)
  - [List approvals](/brainstem_support/restapi/resources/consumable/#list-approvals)
  - [Detail approval](/brainstem_support/restapi/resources/consumable/#detail-approval)
  - [Accept approval](/brainstem_support/restapi/resources/consumable/#accept-approval)
  - [Reject approval](/brainstem_support/restapi/resources/consumable/#reject-approval)

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | string with UUID identificator |
| `name` | string **[required]** |
| `description` | string |
| `supplier` | string with the related supplier ID **[required]** |
| `type` | string **[required]**. *See options below* |
| `type_json` | JSON object. *See accepted schemas below* |
| `comments` | string |

These are the available `type` options for Consumable:
- `OpticFiberDesign`
- `SiliconProbeDesign`
- `VirusConstruct`
- `WireElectrode`

A detailed list of the accepted schemas for the `type_json` field, related to each `type`, can be found in


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/resources/consumable
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'consumable')
```

### Response example
```
{"consumables": [
    {
        "id": "0a533099-700a-4d9b-a3db-87be8d137770",
        "name": "AAV-EF1a-mCherry-IRES-WGA-Cre ",
        "description": "Transsynaptic Tracers: WGA-Cre (AAV2, 5 & 8)",
        "supplier": "4fa1c3b4-f955-47f5-8524-3f1afa3fc657",
        "type": "VirusConstruct",
        "type_json": {
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
        "type_json": {
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


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** http://brainstem.org/rest/private/resources/consumable
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: consumables submissions go through an approval process.

### Use example (using Python API)
```
resp = save_model(settings, "consumable",  data={
        "name": "MyNewConsumable",
        "description": "",
        "supplier": "fba48e24-eebf-4b11-a8b9-ac660854d779",
        "type": "OpticFiberDesign",
        "type_json": {
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
```
{'consumable_approval': {
        'id': 'b7595523-5578-45c0-b7ef-c1f1485ac041',
        'name': 'MyNewConsumable',
        'description': '',
        'supplier': 'fba48e24-eebf-4b11-a8b9-ac660854d779',
        'type': 'OpticFiberDesign',
        'type_json': {
            'productId': '42',
            'tipDescription': '',
            'coreDiameter': 0,
            'outerDiameter': 100,
            'aperture': 0.2
        },
        'comments': ''
    }
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/resources/consumable/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'consumable', id='67f263cd-5960-406f-a879-c1f259140979')
```

### Response example
```
{'consumable': {
        'id': '67f263cd-5960-406f-a879-c1f259140979',
        'name': 'MyNewConsumable',
        'description': '',
        'supplier': 'fba48e24-eebf-4b11-a8b9-ac660854d779',
        'type': 'OpticFiberDesign',
        'type_json': {
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
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/resources/consumable/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: consumables changes go through an approval process.

### Use example (using Python API)
```
resp = save_model(settings, "consumable", id="67f263cd-5960-406f-a879-c1f259140979", data={"description": "new text"})
```

### Response example
```
{'consumable_approval': {
        'id': '8cf7d857-a197-4e36-9e0c-1766bb6aa285',
        'name': 'MyNewConsumable',
        'description': 'new text',
        'supplier': 'fba48e24-eebf-4b11-a8b9-ac660854d779',
        'type': 'OpticFiberDesign',
        'type_json': {
            'productId': '42',
            'tipDescription': '',
            'coreDiameter': 0,
            'outerDiameter': 100,
            'aperture': 0.2
        },
        'comments': ''
    }
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** http://brainstem.org/rest/private/resources/consumable/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

**Note**: only administrators can delete Consumables.

### Use example (using Python API)
```
resp = delete_model(settings, "consumable", id="67f263cd-5960-406f-a879-c1f259140979")
``` 


## List approvals
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/resources/consumable_approvals
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'consumableapproval')
```

### Response example
```
{"consumable_approvals": [
    {
        "id": "b7595523-5578-45c0-b7ef-c1f1485ac041",
        "name": "MyNewConsumable",
        "description": "",
        "supplier": "fba48e24-eebf-4b11-a8b9-ac660854d779",
        "type": "OpticFiberDesign",
        "type_json": {
            "productId": "42",
            "tipDescription": "",
            "coreDiameter": 0,
            "outerDiameter": 100,
            "aperture": 0.2
        },
        "comments": "",
        "instance_id": null,
        "action": "Add",
        "reviewer": null,
        "status": "Pending"
    }
]}
```


## Detail approval
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/resources/consumable_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'consumableapproval', id='b7595523-5578-45c0-b7ef-c1f1485ac041')
```

### Response example
```
{'consumable_approval': {
        'id': 'b7595523-5578-45c0-b7ef-c1f1485ac041',
        'name': 'MyNewConsumable',
        'description': '',
        'supplier': 'fba48e24-eebf-4b11-a8b9-ac660854d779',
        'type': 'OpticFiberDesign',
        'type_json': {
            'productId': '42',
            'tipDescription': '',
            'coreDiameter': 0,
            'outerDiameter': 100,
            'aperture': 0.2
        },
        'comments': '',
        'instance_id': None,
        'action': 'Add',
        'reviewer': None,
        'status': 'Pending'
    }
}
```


## Accept approval
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/resources/consumable_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = save_model(settings, "consumableapproval", id="b7595523-5578-45c0-b7ef-c1f1485ac041", options="accept")
```


## Reject approval
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/resources/consumable_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = save_model(settings, "consumableapproval", id="8cf7d857-a197-4e36-9e0c-1766bb6aa285", options="reject")
```