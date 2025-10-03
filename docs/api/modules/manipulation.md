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
| `order` | optional positive integer controlling display order within a session |


## Types of manipulation

### Electrical and Magnetic Stimulation
- `DeepBrainStimulation`: Deep brain stimulation (DBS)
- `ElectricalStimulation`: Electrical stimulation
- `ElectromagneticFieldStimulation`: Electromagnetic field stimulation
- `TranscranialElectricalStimulation`: Transcranial electrical stimulation
- `TranscranialMagneticStimulation`: Transcranial magnetic stimulation (TMS)

### Optical, Thermal and Ultrasound Stimulation
- `OptogeneticStimulation`: Optogenetic stimulation
- `ThermalPerturbation`: Thermal perturbation
- `UltrasoundStimulation`: Ultrasound stimulation

### Chemical and Pharmacological Perturbations
- `LiquidPerturbation`: Liquid perturbation
- `Microperfusion`: Microperfusion
- `PharmacologicalInjection`: Pharmacological injection
- `PharmacologicalSuperfusion`: Pharmacological superfusion
- `PharmacologicalInhalation`: Pharmacological inhalation

### Sensory Stimulation
- `AuditoryStimulation`: Auditory stimulation
- `MultisensoryStimulation`: Multisensory stimulation
- `OdorStimulation`: Odor stimulation
- `TactileStimulation`: Tactile stimulation
- `VisualStimulation`: Visual stimulation


## List view
- **Allowed portals:** public, private, super
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
        'id': '63a9caa1-620e-4ac5-8bf2-c2525a4b9e89',
        'type': 'ElectricalStimulation',
        'notes': 'motor cortex pulses',
        'procedures': ['43bd31cd-7122-42b8-b82e-b391fdfdad9e'],
        'equipment': ['5b032f95-3f5b-4a27-9680-5f8f671dba22'],
        'session': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
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
        'order': 0
    },
    {
        'id': '1102d210-362e-4b8e-b434-8d3b60c7d535',
        'type': 'LiquidPerturbation',
        'notes': 'saline wash',
        'procedures': ['64b6ae70-d07f-4fbc-ac04-cdfcfe27936f'],
        'equipment': [],
        'session': 'ef7ae22f-143a-4a5e-adf6-1c623531dd63',
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
        'order': 1
    }
]}
```


## Add
- **Allowed portals:** private, super
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
        'session': '1a827c68-19b4-4cec-8ae5-e13c8f1de900',
        'procedures': ['61da7e53-1066-42de-a1a2-3db96bb7cba2'],
        'equipment': ['5b032f95-3f5b-4a27-9680-5f8f671dba22'],
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
    'id': 'd05f56c6-9aea-4c38-a1cb-8680e015cad0',
    'type': 'LiquidPerturbation',
    'notes': 'odorant rinse',
    'procedures': ['61da7e53-1066-42de-a1a2-3db96bb7cba2'],
    'equipment': ['5b032f95-3f5b-4a27-9680-5f8f671dba22'],
    'session': '1a827c68-19b4-4cec-8ae5-e13c8f1de900',
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
    'order': 0
}}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/manipulation/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('manipulation', id='d05f56c6-9aea-4c38-a1cb-8680e015cad0')
```

### Response example
{: .no_toc}

```
{'manipulation': {
    'id': 'd05f56c6-9aea-4c38-a1cb-8680e015cad0',
    'type': 'LiquidPerturbation',
    'notes': 'odorant rinse',
    'procedures': ['61da7e53-1066-42de-a1a2-3db96bb7cba2'],
    'equipment': ['5b032f95-3f5b-4a27-9680-5f8f671dba22'],
    'session': '1a827c68-19b4-4cec-8ae5-e13c8f1de900',
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
    'order': 0
}}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/manipulation/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model(
    "manipulation",
    id="d05f56c6-9aea-4c38-a1cb-8680e015cad0",
    data={"notes": "rinse complete"}
)
```

### Response example
{: .no_toc}

```
{'manipulation': {
    'id': 'd05f56c6-9aea-4c38-a1cb-8680e015cad0',
    'type': 'LiquidPerturbation',
    'notes': 'rinse complete',
    'procedures': ['61da7e53-1066-42de-a1a2-3db96bb7cba2'],
    'equipment': ['5b032f95-3f5b-4a27-9680-5f8f671dba22'],
    'session': '1a827c68-19b4-4cec-8ae5-e13c8f1de900',
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
    'order': 0
}}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/modules/manipulation/<id\>/
- **Data:** None
- **Responses:** `204` OK; `400` Bad request; `403` Not allowed; `404` Not found

`400` is returned when the manipulation is still referenced by an epoch in the same session.


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("manipulation", id="d05f56c6-9aea-4c38-a1cb-8680e015cad0")
``` 
