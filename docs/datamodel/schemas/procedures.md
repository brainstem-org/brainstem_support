---
layout: default
title: Procedure types
parent: Schemas
grand_parent: Data model
nav_order: 4
---

# Procedure types
{: .no_toc}

Various procedure types are available for different experimental manipulations and interventions in neuroscience research.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

### Brain lesion

| Field | Description |
|:------|:------------|
| `Lesion method` | Method used to create the brain lesion (**required**) |
| `Volume of brain lesion (μL)` | Volume of the brain lesion in microliters (**required**) |
| `Fatal outcome` | Checkbox to indicate if the procedure resulted in a fatal outcome |

### Craniectomy

| Field | Description |
|:------|:------------|
| `Method of craniectomy` | Method used for the craniectomy (**required**) |
| `Shape of craniectomy` | Shape of the craniectomy (**required**) |
| `Length of craniectomy (μm)` | Length of the craniectomy in micrometers (**required**) |
| `Width of craniectomy (μm)` | Width of the craniectomy in micrometers (**required**) |
| `Orientation of craniectomy` | Orientation of the craniectomy |
| `Fatal outcome` | Checkbox to indicate if the procedure resulted in a fatal outcome |

### Craniotomy

| Field | Description |
|:------|:------------|
| `Method of craniotomy` | Method used for the craniotomy (**required**) |
| `Shape of craniotomy` | Shape of the craniotomy (**required**) |
| `Length of craniotomy (μm)` | Length of the craniotomy in micrometers (**required**) |
| `Width of craniotomy (μm)` | Width of the craniotomy in micrometers (**required**) |
| `Orientation of craniotomy` | Orientation of the craniotomy |
| `Fatal outcome` | Checkbox to indicate if the procedure resulted in a fatal outcome |

### Optic fiber implant

| Field | Description |
|:------|:------------|
| `Fiber tip shape` | Shape of the optic fiber tip (**required**) |
| `Sterilization Method` | Method used to sterilize the optic fiber implant |

### Brain perfusion fixation

| Field | Description |
|:------|:------------|
| `Perfusion method` | Method used for brain perfusion fixation (**required**) |
| `Perfusion volume (mL)` | Volume of perfusion solution in milliliters |
| `Fatal outcome` | Checkbox to indicate if the procedure resulted in a fatal outcome |

### Single wire electrode

| Field | Description |
|:------|:------------|
| `Wire count` | Number of wires (**required**, default: 1) |
| `Wire diameter (μm)` | Diameter of the wire in micrometers |
| `Wire material` | Material of the wire |
| `Impedance (kOhms)` | Impedance of the wire in kiloohms |
| `Sterilization Method` | Method used to sterilize the electrode |

### Silicon probe implant

| Field | Description |
|:------|:------------|
| `Sterilization Method` | Method used to sterilize the silicon probe |

### Brain slice

| Field | Description |
|:------|:------------|
| `Thickness of slices (μm)` | Thickness of the brain slices in micrometers (**required**) |
| `Number of slices` | Number of brain slices (integer) |
| `Orientation of slices` | Orientation of the brain slices (**required**) |
| `Medium used for slice` | Medium used for maintaining the brain slices |
| `Vibratome blade angle (°)` | Angle of the vibratome blade in degrees |

### Tetrode wire electrode

| Field | Description |
|:------|:------------|
| `Tetrode count` | Number of tetrodes (**required**, integer) |
| `Wires per tetrode` | Number of wires per tetrode (integer) |
| `Wire diameter (μm)` | Diameter of the wires in micrometers |
| `Wire material` | Material of the wires |
| `Sterilization Method` | Method used to sterilize the tetrode wire electrode |

### Virus injection

| Field | Description |
|:------|:------------|
| `Injection volume (nL)` | Volume of virus injected in nanoliters |
| `Injection rate (nL/min)` | Rate of virus injection in nanoliters per minute |
| `Injection profile` | Profile of the virus injection |

### Coordinates

For all procedure types, coordinates are specified using the following system: [Coordinates systems page]({{"datamodel/schemas/coordinates/"|absolute_url}})

## Procedure API access

The API allows for programmable access to Procedures, enabling you to read, edit, and delete procedures through the API. Learn more about the procedures' fields and data structure on the [Procedure API page]({{"api/modules/procedure/"|absolute_url}}).