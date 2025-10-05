---
layout: default
title: Procedure log
parent: Schemas
grand_parent: API
nav_order: 1
---

# Procedure log schemas
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Impedances
```
{
    "type": "object",
    "title": "Impedances",
    "properties": {
        "impedances": {
            "title": "Impedances (kOhm)",
            "type": "number",
            "minimum": 0
        },
        "phases": {
            "title": "Phases (degrees)",
            "type": ["number", "null"]
        },
        "channels": {
            "title": "List of channels",
            "type": "number",
            "minimum": 0
        }
    },
    "required": ["impedances"]
}
```

*Impedances* is a **required** field.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "impedances": 2,
    "phases": [15],
    "channels": [0,2,3]
}
```


## Linear displacement
```
{
    "type": "object",
    "title": "Linear displacement",
    "properties": {
        "displacement": {
            "title": "Displacement (µm)",
            "type": "number"
        }
    },
    "required": ["displacement"]
}
```

*Displacement* is a **required** field.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "displacement": 12
}
```


## Tetrodes4
```
{
    "type": "object",
    "title": "Tetrode log (4 tetrodes)",
    "options": {"compact": "true"},
    "additionalProperties": false,
    "properties": {
        "tetrode_1": {
            "title": "Tetrode #1 (µm)",
            "type": "number"
        },
        "tetrode_2": {
            "title": "Tetrode #2 (µm)",
            "type": "number"
        },
        "tetrode_3": {
            "title": "Tetrode #3 (µm)",
            "type": "number"
        },
        "tetrode_4": {
            "title": "Tetrode #4 (µm)",
            "type": "number"
        }
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "tetrode_1": 1000,
    "tetrode_2": 1050,
    "tetrode_3": 1100,
    "tetrode_4": 1150
}
```


## Tetrodes8
```
{
    "type": "object",
    "title": "Tetrode log (8 tetrodes)",
    "options": {"compact": "true"},
    "additionalProperties": false,
    "properties": {
        "tetrode_1": {
            "title": "Tetrode #1 (µm)",
            "type": "number"
        },
        "tetrode_2": {
            "title": "Tetrode #2 (µm)",
            "type": "number"
        },
        "tetrode_3": {
            "title": "Tetrode #3 (µm)",
            "type": "number"
        },
        "tetrode_4": {
            "title": "Tetrode #4 (µm)",
            "type": "number"
        },
        "tetrode_5": {
            "title": "Tetrode #5 (µm)",
            "type": "number"
        },
        "tetrode_6": {
            "title": "Tetrode #6 (µm)",
            "type": "number"
        },
        "tetrode_7": {
            "title": "Tetrode #7 (µm)",
            "type": "number"
        },
        "tetrode_8": {
            "title": "Tetrode #8 (µm)",
            "type": "number"
        }
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "tetrode_1": 1000,
    "tetrode_2": 1050,
    "tetrode_3": 1100,
    "tetrode_4": 1150,
    "tetrode_5": 1200,
    "tetrode_6": 1250,
    "tetrode_7": 1300,
    "tetrode_8": 1350
}
```