---
layout: default
title: Subject state change
parent: Schemas
grand_parent: API
nav_order: 1
---

# Subject state change schemas
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Brain lesion
```
{
    "type": "object",
    "title": "Brain lesion",
    "properties": {
        "method": {
            "title": "Lesion method",
            "type": "string",
            "format": "text"
        },
        "volume": {
            "title": "Volume of brain lesion (µL)",
            "type": "number",
            "minimum": 0
        },
        "fatalOutcome": {
            "title": "Fatal outcome",
            "type": "boolean",
            "format": "checkbox"
        }
    },
    "required": ["method"]
}
```

*Lesion method* is a **required** field.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "method": "Iron rod impalement",
    "volume": 43.2,
    "fatalOutcome": False
}
```

## Craniotomy
```
{
    "type": "object",
    "title": "Craniotomy",
    "properties": {
        "shape": {
            "title": "Shape of craniotomy",
            "type": "string",
            "format": "text"
        },
        "length": {
            "title": "Length of craniotomy (µm)",
            "type": "number",
            "minimum": 0
        },
        "width": {
            "title": "Width of craniotomy (µm)",
            "type": "number",
            "minimum": 0
        },
        "rotation": {
            "title": "Orientation of craniotomy",
            "type": "string",
            "format": "text"
        },
        "fatalOutcome": {
            "title": "Fatal outcome",
            "type": "boolean",
            "format": "checkbox"
        }
    },
    "required": ["shape", "length"]
}
```

*Shape of craniotomy* is a **required** field.
*Length of craniotomy* is a **required** field.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "shape": "Circular",
    "length": 37,
    "width": 37,
    "rotation": "lateral",
    "fatalOutcome": False
}
```

## Death
```
{
    "type": "object",
    "title": "Death",
    "properties": {
        "causeOfDeath": {
            "title": "Cause of death",
            "type": "string",
            "format": "text"
        },
        "fatalOutcome": {
            "title": "Fatal outcome",
            "type": "boolean",
            "format": "checkbox"
        }
    },
    "required": ["causeOfDeath"]
}
```

*Cause of death* is a **required** field.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "causeOfDeath": "Iron rod impalement",
    "fatalOutcome": False
}
```

## Brain perfusion fixation
```
{
    "type": "object",
    "title": "Brain perfusion fixation",
    "properties": {
        "method": {
            "title": "Method of perfusion",
            "type": "string",
            "format": "text"
        },
        "volume": {
            "title": "Perfusion volume (mL)",
            "type": "number",
            "minimum": 0
        },
        "fatalOutcome": {
            "title": "Fatal outcome",
            "type": "boolean",
            "format": "checkbox"
        }
    },
    "required": ["method"]
}
```

*Method of perfusion* is a **required** field.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "method": "extracorporeal membrane oxygenation",
    "volume": 77.7,
    "fatalOutcome": True
}
```

## Brain slice
```
{
    "type": "object",
    "title": "Brain slice",
    "properties": {
        "thickness": {
            "title": "Thickness of slices (µm)",
            "type": "number",
            "minimum": 0
        },
        "nSlices": {
            "title": "Number of slices",
            "type": "number",
            "minimum": 0
        },
        "orientation": {
            "title": "Orientation of slices",
            "type": "number"
        },
        "medium": {
            "title": "Medium used for slice",
            "type": "string",
            "format": "text"
        },
        "vibratomeBladeAngle": {
            "title": "Vibratome blade angle",
            "type": "number",
            "minimum": 0
        },
        "fatalOutcome": {
            "title": "Fatal outcome",
            "type": "boolean",
            "format": "checkbox"
        }
    },
    "required": ["thickness", "orientation"]
}
```

*Thickness of slices* is a **required** field.
*Orientation of slices* is a **required** field.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "thickness": 2,
    "nSlices": 15,
    "orientation": "lateral",
    "medium": "l‑glutamine",
    "vibratomeBladeAngle": 30,
    "fatalOutcome": False
}
```
