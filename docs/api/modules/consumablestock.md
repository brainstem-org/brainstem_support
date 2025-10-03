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


## Types of consumable stock

Consumable stock `type` values are grouped as follows:

### Reagents and Solutions
- `ChemicalReagent`: Chemical reagent
- `ImmunoReagent`: Antibody or immunoreagent
- `PharmacologicalAgent`: Pharmacological agent
- `PhysiologicalSolution`: Physiological solution
- `TracerDye`: Tracer or dye
- `VirusSolution`: Virus solution

### Device-Linked Consumables
- `ConsumableDevice`: Consumable device
- `OpticalComponent`: Optical component
- `OpticFiber`: Optic fiber
- `SiliconProbe`: Silicon probe
- `SingleWireElectrode`: Single wire electrode

## List view
- **Allowed portals:** public, private, super
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
{'consumablestock': [
    {
        'id': 'f79d84c8-6bec-40e3-b18a-5b25e57f4a09',
        'type': 'OpticFiber',
        'notes': 'Backup spool',
        'inventory': '6b80ffa7-40b3-4d3d-8d1a-2c1d581fd88e',
        'acquisition_date': '2024-03-01',
        'expiration_date': None,
        'storage_location': 'Cabinet A',
        'storage_conditions': 'Room temperature',
        'intended_use': 'Optogenetics',
        'cost': '120 USD',
        'consumable': 'a5f29099-2758-4163-a8e4-e5e2898e57b2',
        'details': {
            'fiberIds': 'OF-2024-03-A',
            'quantity': 12
        }
    },
    {
        'id': 'a18dd2b1-6393-468c-9424-1bc77b9e4976',
        'type': 'SiliconProbe',
        'notes': 'Quarterly order',
        'inventory': '6b80ffa7-40b3-4d3d-8d1a-2c1d581fd88e',
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
        }
    }
]}
```


## Add
- **Allowed portals:** private, super
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
        "inventory": "6b80ffa7-40b3-4d3d-8d1a-2c1d581fd88e",
        "consumable": "a5f29099-2758-4163-a8e4-e5e2898e57b2",
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
{'consumablestock': {
    'id': 'd37c9255-d5ae-47d9-b6e1-4ec760c200fb',
    'type': 'OpticFiber',
    'notes': 'Initial batch',
    'inventory': '6b80ffa7-40b3-4d3d-8d1a-2c1d581fd88e',
    'acquisition_date': '2024-03-01',
    'expiration_date': None,
    'storage_location': 'Cabinet A',
    'storage_conditions': None,
    'intended_use': None,
    'cost': None,
    'consumable': 'a5f29099-2758-4163-a8e4-e5e2898e57b2',
    'details': {'fiberIds': 'OF-2024-03-A', 'quantity': 12}
}}
```


## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/consumablestock/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('consumablestock', id='d37c9255-d5ae-47d9-b6e1-4ec760c200fb')
```

### Response example
{: .no_toc}

```
{'consumablestock': {
    'id': 'd37c9255-d5ae-47d9-b6e1-4ec760c200fb',
    'type': 'OpticFiber',
    'notes': 'Initial batch',
    'inventory': '6b80ffa7-40b3-4d3d-8d1a-2c1d581fd88e',
    'acquisition_date': '2024-03-01',
    'expiration_date': None,
    'storage_location': 'Cabinet A',
    'storage_conditions': None,
    'intended_use': None,
    'cost': None,
    'consumable': 'a5f29099-2758-4163-a8e4-e5e2898e57b2',
    'details': {'fiberIds': 'OF-2024-03-A', 'quantity': 12}
}}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/consumablestock/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model(
    "consumablestock",
    id="d37c9255-d5ae-47d9-b6e1-4ec760c200fb",
    data={"notes": "Updated notes"}
)
```

### Response example
{: .no_toc}

```
{'consumablestock': {
    'id': 'd37c9255-d5ae-47d9-b6e1-4ec760c200fb',
    'type': 'OpticFiber',
    'notes': 'Updated notes',
    'inventory': '6b80ffa7-40b3-4d3d-8d1a-2c1d581fd88e',
    'acquisition_date': '2024-03-01',
    'expiration_date': None,
    'storage_location': 'Cabinet A',
    'storage_conditions': None,
    'intended_use': None,
    'cost': None,
    'consumable': 'a5f29099-2758-4163-a8e4-e5e2898e57b2',
    'details': {'fiberIds': 'OF-2024-03-A', 'quantity': 12}
}}
```

## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/modules/consumablestock/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("consumablestock", id="d37c9255-d5ae-47d9-b6e1-4ec760c200fb")
```
