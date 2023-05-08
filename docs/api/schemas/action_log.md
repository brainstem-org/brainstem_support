---
layout: default
title: Action log
parent: Schemas
grand_parent: API
nav_order: 1
---

# Action log schemas
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
            "type": "string"
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
    "phases": 15,
    "channels": "0,2,3"
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