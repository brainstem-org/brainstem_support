---
layout: default
title: Consumable stock
parent: Schemas
grand_parent: API
nav_order: 1
---

# Consumable stock schemas
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## OpticFiber
```
{
    "type": "object",
    "title": "Optic fiber",
    "properties": {
        "fiberIds": {
            "title": "Fiber IDs",
            "type": "string",
            "format": "text",
            "brief": "fiber IDs",
            "options": {"infoText": "A unique identifier for each optic fiber."}
        },
        "quantity": {
            "title": "Quantity of optic fibers",
            "type": "integer",
            "minimum": 0,
            "brief": "quantity",
            "units": "",
            "options": {
                "inputAttributes": {"placeholder": "integer"},
                "infoText": "The quantity of optic fibers in the batch."
            }
        }
    }
}

```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "fiberIds": "id1",
    "quantity": 4
}
```


## SiliconProbe
```
{
    "type": "object",
    "title": "Silicon probe",
    "properties": {
        "probeIds": {
            "title": "Probe IDs",
            "type": "string",
            "format": "text",
            "brief": "probe IDs",
            "options": {"infoText": "A unique identifier for each silicon probe."}
        },
        "quantity": {
            "title": "Quantity of probes",
            "type": "integer",
            "minimum": 0,
            "brief": "quantity",
            "units": "",
            "options": {
                "inputAttributes": {"placeholder": "integer"},
                "infoText": "The quantity of probes in the batch."
            }
        }
    }
}

```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "fiberIds": "probe_id1",
    "quantity": 4
}
```

## SingleWireElectrode
```
{
    "type": "object",
    "title": "Single wire electrode",
    "properties": {
        "wireIds": {
            "title": "Wire IDs",
            "type": "string",
            "format": "text",
            "brief": "wire IDs",
            "options": {"infoText": "A unique identifier for the wire electrode as defined by the supplier."}
        },
        "quantity": {
            "title": "Quantity of electrodes",
            "type": "integer",
            "minimum": 0,
            "brief": "quantity",
            "units": "",
            "options": {
                "inputAttributes": {"placeholder": "integer"},
                "infoText": "The quantity of electrodes."
            }
        },
        "length": {
            "title": "Length (mm)",
            "type": "number",
            "brief": "length",
            "units": "mm",
            "options": {"infoText": "The length of the wire."}
        }
    }
}

```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "wireIds": "wireid1",
    "quantity": 2,
    "length": 4
}
```

## VirusConstruct
```
{
    "type": "object",
    "title": "Virus construct",
    "properties": {
        "titer": {
            "title": "Titer of virus solution (units/mL)",
            "type": "number",
            "minimum": 0,
            "brief": "titer",
            "units": "units/mL",
            "options": {
                "infoText": "The titer of the virus solution. In units per milliliter"
            }
        },
        "titerUnit": {
            "title": "Titer unit of virus solution",
            "type": "string",
            "enum": ["vg/mL", "TU/mL", "pfu/mL"],
            "brief": "titer unit",
            "options": {
                "infoText": "vg/mL: Viral genomes per milliliter; TU/mL: Transducing units per milliliter; pfu/mL: Plaque forming units per milliliter."
            }
        },
        "volume": {
            "title": "Volume of virus solution (mL)",
            "type": "number",
            "minimum": 0,
            "brief": "volume",
            "units": "mL",
            "options": {"infoText": "The volume of the virus solution."}
        },
        "aliquotCount": {
            "title": "The number of aliquots",
            "type": "integer",
            "minimum": 0,
            "brief": "aliquots",
            "units": "",
            "options": {
                "inputAttributes": {"placeholder": "integer"},
                "infoText": "The number of aliquots."
            }
        },
        "aliquotVolume": {
            "title": "The volume per aliquot (µL)",
            "type": "number",
            "minimum": 0,
            "brief": "volume",
            "units": "µL",
            "options": {"infoText": "The volume of each aliquot in micro liters."}
        }
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
        "titer": 0.0001,
        "titerUnit": "TU/mL",
        "volume": 1,
        "aliquotCount": 20,
        "aliquotVolume": 5
    }
```
