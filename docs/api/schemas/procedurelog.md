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
    "options": {
        "compact": "true"
    },
    "additionalProperties": false,
    "properties": {
        "impedances": {
            "title": "Impedances (kOhm)",
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "number",
                "minimum": 0
            }
        },
        "phases": {
            "title": "Phases (degrees)",
            "type": "array",
            "items": {
                "type": "number",
                "minimum": 0
            }
        },
        "channels": {
            "title": "List of channels",
            "type": "array",
            "items": {
                "type": "number",
                "minimum": 0
            }
        }
    },
    "required": [
        "impedances"
    ]
}
```

## LinearDisplacement
```
{
    "type": "object",
    "title": "Linear displacement",
    "options": {
        "compact": "true"
    },
    "additionalProperties": false,
    "properties": {
        "displacement": {
            "title": "Displacement (\u00b5m)",
            "type": "number"
        }
    },
    "required": [
        "displacement"
    ]
}
```

## Tetrodes4
```
{
    "type": "object",
    "title": "Tetrode log (4 tetrodes)",
    "options": {
        "compact": "true"
    },
    "additionalProperties": false,
    "properties": {
        "tetrode_1": {
            "title": "Tetrode #1 (\u00b5m)",
            "type": "number"
        },
        "tetrode_2": {
            "title": "Tetrode #2 (\u00b5m)",
            "type": "number"
        },
        "tetrode_3": {
            "title": "Tetrode #3 (\u00b5m)",
            "type": "number"
        },
        "tetrode_4": {
            "title": "Tetrode #4 (\u00b5m)",
            "type": "number"
        }
    }
}
```

## Tetrodes8
```
{
    "type": "object",
    "title": "Tetrode log (4 tetrodes)",
    "options": {
        "compact": "true"
    },
    "additionalProperties": false,
    "properties": {
        "tetrode_1": {
            "title": "Tetrode #1 (\u00b5m)",
            "type": "number"
        },
        "tetrode_2": {
            "title": "Tetrode #2 (\u00b5m)",
            "type": "number"
        },
        "tetrode_3": {
            "title": "Tetrode #3 (\u00b5m)",
            "type": "number"
        },
        "tetrode_4": {
            "title": "Tetrode #4 (\u00b5m)",
            "type": "number"
        },
        "tetrode_5": {
            "title": "Tetrode #5 (\u00b5m)",
            "type": "number"
        },
        "tetrode_6": {
            "title": "Tetrode #6 (\u00b5m)",
            "type": "number"
        },
        "tetrode_7": {
            "title": "Tetrode #7 (\u00b5m)",
            "type": "number"
        },
        "tetrode_8": {
            "title": "Tetrode #8 (\u00b5m)",
            "type": "number"
        }
    }
}
```

