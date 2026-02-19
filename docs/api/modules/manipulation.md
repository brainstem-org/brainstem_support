---
layout: default
title: Manipulation
parent: Modules
grand_parent: API
nav_order: 5
---

# Manipulation API endpoint
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
| `procedures` | list of related procedure IDs formatted as strings **[required]** |
| `session` | related session ID formatted as a string **[required]** |
| `equipment` | list of related equipment IDs formatted as strings |
| `details` | JSON data (object or array) whose structure depends on the selected manipulation type |
| `type_schema_version` | string schema version for `details` |
| `order` | optional positive integer controlling display order within a session |


## Types of manipulation

A detailed list of the available `type` options and accepted schemas for the `details` field can be found in the [Manipulation schemas documentation](/api/schemas/manipulation).


## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/manipulation
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('manipulation')
```

### Response example
{: .no_toc}

```
{'manipulations': [
    {
        'id': '00000000-0000-0000-0000-000000000000',
        'type': 'ElectricalStimulation',
        'notes': 'motor cortex pulses',
        'procedures': ['00000000-0000-0000-0000-000000000000'],
        'equipment': ['00000000-0000-0000-0000-000000000000'],
        'session': '00000000-0000-0000-0000-000000000000',
        'details': [
            {
                'amplitude': 0.15,
                'duration': 5,
                'profile': 'Pulse train',
                'dutyCycle': 0.2,
                'repetitions': 5,
                'injectionPolarity': 'biphasic',
                'closedLoop': False
            }
        ],
        'type_schema_version': '0.0.0',
        'order': 0
    },
    {
        'id': '00000000-0000-0000-0000-000000000000',
        'type': 'LiquidPerturbation',
        'notes': 'saline wash',
        'procedures': ['00000000-0000-0000-0000-000000000000'],
        'equipment': [],
        'session': '00000000-0000-0000-0000-000000000000',
        'details': [
            {
                'liquidAgent': 'Saline',
                'concentration': 0.9,
                'volume': 100,
                'profile': 'Continuous Infusion',
                'repetitions': 1,
                'flowRate': 10,
                'closedLoop': False
            }
        ],
        'type_schema_version': '0.0.0',
        'order': 1
    }
]}
```


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/modules/manipulation
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model(
    "manipulation",
    data={
        'type': 'LiquidPerturbation',
        'session': '00000000-0000-0000-0000-000000000000',
        'procedures': ['00000000-0000-0000-0000-000000000000'],
        'equipment': ['00000000-0000-0000-0000-000000000000'],
        'notes': 'odorant rinse',
        'details': [
            {
                'liquidAgent': 'Water',
                'concentration': 1,
                'volume': 50,
                'profile': 'Bolus Injection',
                'repetitions': 3,
                'flowRate': 12,
                'closedLoop': True
            }
        ]
    }
)
```

### Response example
{: .no_toc}

```
{'manipulation': {
    'id': '00000000-0000-0000-0000-000000000000',
    'type': 'LiquidPerturbation',
    'notes': 'odorant rinse',
    'procedures': ['00000000-0000-0000-0000-000000000000'],
    'equipment': ['00000000-0000-0000-0000-000000000000'],
    'session': '00000000-0000-0000-0000-000000000000',
    'details': [
        {
            'liquidAgent': 'Water',
            'concentration': 1,
            'volume': 50,
            'profile': 'Bolus Injection',
            'repetitions': 3,
            'flowRate': 12,
            'closedLoop': True
        }
    ],
    'type_schema_version': '0.0.0',
    'order': 0
}}
```



## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/manipulation/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('manipulation', id='00000000-0000-0000-0000-000000000000')
```

### Response example
{: .no_toc}

```
{'manipulation': {
    'id': '00000000-0000-0000-0000-000000000000',
    'type': 'LiquidPerturbation',
    'notes': 'odorant rinse',
    'procedures': ['00000000-0000-0000-0000-000000000000'],
    'equipment': ['00000000-0000-0000-0000-000000000000'],
    'session': '00000000-0000-0000-0000-000000000000',
    'details': [
        {
            'liquidAgent': 'Water',
            'concentration': 1,
            'volume': 50,
            'profile': 'Bolus Injection',
            'repetitions': 3,
            'flowRate': 12,
            'closedLoop': True
        }
    ],
    'type_schema_version': '0.0.0',
    'order': 0
}}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/manipulation/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model(
    "manipulation",
    id="00000000-0000-0000-0000-000000000000",
    data={"notes": "rinse complete"}
)
```

### Response example
{: .no_toc}

```
{'manipulation': {
    'id': '00000000-0000-0000-0000-000000000000',
    'type': 'LiquidPerturbation',
    'notes': 'rinse complete',
    'procedures': ['00000000-0000-0000-0000-000000000000'],
    'equipment': ['00000000-0000-0000-0000-000000000000'],
    'session': '00000000-0000-0000-0000-000000000000',
    'details': [
        {
            'liquidAgent': 'Water',
            'concentration': 1,
            'volume': 50,
            'profile': 'Bolus Injection',
            'repetitions': 3,
            'flowRate': 12,
            'closedLoop': True
        }
    ],
    'type_schema_version': '0.0.0',
    'order': 0
}}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/modules/manipulation/<id\>/
- **Data:** None
- **Responses:** `204` OK; `400` Bad request; `403` Not allowed; `404` Not found

`400` is returned when the manipulation is still referenced by an epoch in the same session.


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("manipulation", id="00000000-0000-0000-0000-000000000000")
``` 
