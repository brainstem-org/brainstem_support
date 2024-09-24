---
layout: default
title: Procedure
parent: Schemas
grand_parent: API
nav_order: 1
---

# Procedure schemas
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Optic fiber implant
```
{
    "type": "object",
    "title": "Optic fiber implant",
    "properties": {
        "fiberTipShape": {
            "title": "Fiber tip shape",
            "type": "string",
            "format": "text",
            "default": "flat"
        }
    },
    "required": ["fiberTipShape"]
}
```

*Fiber tip shape* is a **required** field - **default** value set is `flat`.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "fiberTipShape": "flat"
}
```

## Silicon probe implant
```
{
    "type": "object",
    "title": "Silicon probe implant",
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{ }
```

## Single wire electrode
```
{
    "type": "object",
    "title": "Single wire electrode",
    "properties": {
        "wireCount": {
            "title": "Wire count",
            "type": "number",
            "minimum": 0,
            "default": 1
        },
        "wireDiameter": {
            "title": "Wire diameter (µm)",
            "type": "number",
            "minimum": 0
        },
        "wireMaterial": {
            "title": "Wire material",
            "type": "string",
            "format": "text"
        }
    },
    "required": ["wireCount"]
}
```

*Wire count* is a **required** field - **default** value set is `1`.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "wireCount": 4,
    "wireDiameter": 50,
    "wireMaterial": "Titanium",
    "rotation": 0,
    "apAngle": 15,
    "mlAngle": 15
}
```

## Tetrode wire electrode
```
{
    "type": "object",
    "title": "Tetrode wire electrode",
    "properties": {
        "tetrodeCount": {
            "title": "Tetrode count",
            "type": "integer",
            "minimum": 0,
            "default": 1
        },
        "nWiresTetrode": {
            "title": "Wires per tetrode",
            "type": "integer",
            "minimum": 0,
            "default": 4
        },
        "wireDiameter": {
            "title": "Wire diameter (µm)",
            "type": "number",
            "minimum": 0
        },
        "wireMaterial": {
            "title": "Wire material",
            "type": "string",
            "format": "text"
        }
    },
    "required": ["tetrodeCount"]
}
```

*Tetrode count* is a **required** field - **default** value set is `1`.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "tetrodeCount": 2,
    "nWiresTetrode": 4,
    "wireDiameter": 50,
    "wireMaterial": "Titanium"
}
```

## Virus injection
```
{
    "type": "object",
    "title": "Virus injection",
    "properties": {
        "injectionVolume": {
            "title": "Injection volume (nL)",
            "type": "number",
            "minimum": 0,
            "default": "0"
        },
        "injectionRate": {
            "title": "Injection Rate (nL/s)",
            "type": "number"
        },
        "injectionSchema": {
            "title": "Injection schema",
            "type": "string",
            "enum": ["Gradual","Pulses","unknown"]
        }
    },
    "required": ["injectionVolume"]
}
```

*Injection volume* is a **required** field - **default** value set is `0`.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "injectionVolume": 100,
    "injectionRate": 50,
    "injectionSchema": "Gradual"
}
```
