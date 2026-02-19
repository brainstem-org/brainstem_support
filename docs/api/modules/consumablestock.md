---
layout: default
title: Consumable stock
parent: Modules
grand_parent: API
nav_order: 2
---

# Consumable stock API endpoint
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
| `status` | string stock status (e.g. `AVAILABLE`, `RESERVED`, `DEPLETED`) |
| `notes` | string [max length: 500] |
| `inventory` | related inventory ID formatted as a string **[required]** |
| `acquisition_date` | string containing date (e.g. "2023-03-22") |
| `expiration_date` | string containing date (e.g. "2023-03-22") |
| `storage_location` | string describing where the consumable is stored [max length: 100] |
| `storage_conditions` | string describing the consumable storage conditions [max length: 100] |
| `intended_use` | string [max length: 100] |
| `cost` | string [max length: 100] |
| `consumable` | related consumable ID formatted as a string |
| `details` | JSON object mapped to the internal `type_json` field. *See accepted schemas below* |
| `type_schema_version` | string schema version for `details` |


## Types of consumable stock

A detailed list of the available `type` options and accepted schemas for the `details` field can be found in the [Consumable stock schemas documentation](/api/schemas/consumablestock).

## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/consumablestock
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('consumablestock')
```

### Response example
{: .no_toc}

```
{'consumable stocks': [
    {
        'id': '00000000-0000-0000-0000-000000000000',
        'type': 'OpticFiber',
        'status': 'AVAILABLE',
        'notes': 'Backup spool',
        'inventory': '00000000-0000-0000-0000-000000000000',
        'acquisition_date': '2024-03-01',
        'expiration_date': None,
        'storage_location': 'Cabinet A',
        'storage_conditions': 'Room temperature',
        'intended_use': 'Optogenetics',
        'cost': '120 USD',
        'consumable': '00000000-0000-0000-0000-000000000000',
        'details': {
            'fiberIds': 'OF-2024-03-A',
            'quantity': 12
        },
        'type_schema_version': '0.0.0'
    },
    {
        'id': '00000000-0000-0000-0000-000000000000',
        'type': 'SiliconProbe',
        'status': 'RESERVED',
        'notes': 'Quarterly order',
        'inventory': '00000000-0000-0000-0000-000000000000',
        'acquisition_date': '2024-02-15',
        'expiration_date': None,
        'storage_location': 'Freezer shelf 2',
        'storage_conditions': '4C',
        'intended_use': 'Acute recordings',
        'cost': '3400 USD',
        'consumable': None,
        'details': {
            'probeIds': 'SP-64A,SP-64B',
            'quantity': 2
        },
        'type_schema_version': '0.0.0'
    }
]}
```


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/modules/consumablestock
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model(
    "consumablestock",
    data={
        "type": "OpticFiber",
        "inventory": "00000000-0000-0000-0000-000000000000",
        "consumable": "00000000-0000-0000-0000-000000000000",
        "notes": "Initial batch",
        "acquisition_date": "2024-03-01",
        "storage_location": "Cabinet A",
        "details": {"fiberIds": "OF-2024-03-A", "quantity": 12}
    }
)
```

### Response example
{: .no_toc}

```
{'consumable stock': {
    'id': '00000000-0000-0000-0000-000000000000',
    'type': 'OpticFiber',
    'status': 'AVAILABLE',
    'notes': 'Initial batch',
    'inventory': '00000000-0000-0000-0000-000000000000',
    'acquisition_date': '2024-03-01',
    'expiration_date': None,
    'storage_location': 'Cabinet A',
    'storage_conditions': None,
    'intended_use': None,
    'cost': None,
    'consumable': '00000000-0000-0000-0000-000000000000',
    'details': {'fiberIds': 'OF-2024-03-A', 'quantity': 12},
    'type_schema_version': '0.0.0'
}}
```


## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/consumablestock/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('consumablestock', id='00000000-0000-0000-0000-000000000000')
```

### Response example
{: .no_toc}

```
{'consumable stock': {
    'id': '00000000-0000-0000-0000-000000000000',
    'type': 'OpticFiber',
    'status': 'AVAILABLE',
    'notes': 'Initial batch',
    'inventory': '00000000-0000-0000-0000-000000000000',
    'acquisition_date': '2024-03-01',
    'expiration_date': None,
    'storage_location': 'Cabinet A',
    'storage_conditions': None,
    'intended_use': None,
    'cost': None,
    'consumable': '00000000-0000-0000-0000-000000000000',
    'details': {'fiberIds': 'OF-2024-03-A', 'quantity': 12},
    'type_schema_version': '0.0.0'
}}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/consumablestock/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model(
    "consumablestock",
    id="00000000-0000-0000-0000-000000000000",
    data={"notes": "Updated notes"}
)
```

### Response example
{: .no_toc}

```
{'consumable stock': {
    'id': '00000000-0000-0000-0000-000000000000',
    'type': 'OpticFiber',
    'status': 'AVAILABLE',
    'notes': 'Updated notes',
    'inventory': '00000000-0000-0000-0000-000000000000',
    'acquisition_date': '2024-03-01',
    'expiration_date': None,
    'storage_location': 'Cabinet A',
    'storage_conditions': None,
    'intended_use': None,
    'cost': None,
    'consumable': '00000000-0000-0000-0000-000000000000',
    'details': {'fiberIds': 'OF-2024-03-A', 'quantity': 12},
    'type_schema_version': '0.0.0'
}}
```

## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/modules/consumablestock/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("consumablestock", id="00000000-0000-0000-0000-000000000000")
```
