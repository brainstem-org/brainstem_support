---
layout: default
title: Subject log
parent: Schemas
grand_parent: API
nav_order: 1
---

# Subject log schemas
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Food consumption log
```
{
    "type": "object",
    "title": "Food Consumption log",
    "properties": {
        "foodAmount": {
            "title": "Food amount (grams)",
            "type": "number",
            "minimum": 0
        }
    },
    "required": ["foodAmount"]
}
```

*Food amount* is a **required** field.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "foodAmount": 32.4
}
```


## Water consumption log
```
{
    "type": "object",
    "title": "Water consumption log",
    "properties": {
        "waterAmount": {
            "title": "Water Amount (mL)",
            "type": "number",
            "minimum": 0
        }
    },
    "required": ["waterAmount"]
}
```

*Water amount* is a **required** field.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "waterAmount": 53.9
}
```


## Weighing log
```
{
    "type": "object",
    "title": "Weighing log",
    "properties": {
        "weight": {
            "title": "Weight (grams)",
            "type": "number",
            "minimum": 0
        }
    },
    "required": ["weight"]
}
```

*Weight* is a **required** field.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "weight": 2.5
}
```