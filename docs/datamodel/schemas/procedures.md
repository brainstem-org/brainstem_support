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

## Surgical Procedures

### Craniectomy

Involves the surgical removal of a portion of the skull to access the brain, without replacing the skull bone afterward. This procedure is often used in cases requiring prolonged brain access or to alleviate pressure after brain injury.

| Field | Description |
|:------|:------------|
| `Method of craniectomy` | Method used for the craniectomy (**required**) |
| `Shape of craniectomy` | Shape of the craniectomy (**required**) |
| `Length of craniectomy (μm)` | Length of the craniectomy in micrometers (**required**) |
| `Width of craniectomy (μm)` | Width of the craniectomy in micrometers (**required**) |
| `Orientation of craniectomy` | Orientation of the craniectomy |
| `Fatal outcome` | Checkbox to indicate if the procedure resulted in a fatal outcome |

### Craniotomy

A surgical procedure where part of the skull is temporarily removed to expose the brain for surgery or research purposes. The removed bone is typically replaced after the procedure, making it a temporary opening.

| Field | Description |
|:------|:------------|
| `Method of craniotomy` | Method used for the craniotomy (**required**) |
| `Shape of craniotomy` | Shape of the craniotomy (**required**) |
| `Length of craniotomy (μm)` | Length of the craniotomy in micrometers (**required**) |
| `Width of craniotomy (μm)` | Width of the craniotomy in micrometers (**required**) |
| `Orientation of craniotomy` | Orientation of the craniotomy |
| `Fatal outcome` | Checkbox to indicate if the procedure resulted in a fatal outcome |

## Implant Procedures

### Optic fiber implant

Involves the surgical implantation of an optic fiber into the brain, often used in optogenetics research to manipulate or record neuronal activity with light.

| Field | Description |
|:------|:------------|
| `Fiber tip shape` | Shape of the optic fiber tip (**required**) |
| `Sterilization Method` | Method used to sterilize the optic fiber implant |

### Silicon probe implant

Involves the implantation of a silicon probe, a device equipped with multiple recording sites, into the brain. Silicon probes are used for high-density recording of neural activity.

| Field | Description |
|:------|:------------|
| `Sterilization Method` | Method used to sterilize the silicon probe |

### Single wire electrode

Refers to the implantation of a single wire electrode into the brain, used for recording electrical activity from or stimulating specific neurons or brain areas.

| Field | Description |
|:------|:------------|
| `Wire count` | Number of wires (**required**, default: 1) |
| `Wire diameter (μm)` | Diameter of the wire in micrometers |
| `Wire material` | Material of the wire |
| `Impedance (kOhms)` | Impedance of the wire in kiloohms |
| `Sterilization Method` | Method used to sterilize the electrode |

### Tetrode wire electrode

The implantation of a tetrode, a device made of four intertwined wire electrodes, into the brain. Tetrodes allow for the recording of electrical signals from multiple neurons simultaneously.

| Field | Description |
|:------|:------------|
| `Tetrode count` | Number of tetrodes (**required**, integer) |
| `Wires per tetrode` | Number of wires per tetrode (integer) |
| `Wire diameter (μm)` | Diameter of the wires in micrometers |
| `Wire material` | Material of the wires |
| `Sterilization Method` | Method used to sterilize the tetrode wire electrode |

## Brain and Tissue Procedures

### Brain lesion

A surgical procedure that intentionally damages or destroys brain tissue to study the functions of specific brain areas. Lesions can help identify the roles of different brain regions in behavior and cognition.

| Field | Description |
|:------|:------------|
| `Lesion method` | Method used to create the brain lesion (**required**) |
| `Volume of brain lesion (μL)` | Volume of the brain lesion in microliters (**required**) |
| `Fatal outcome` | Checkbox to indicate if the procedure resulted in a fatal outcome |

### Brain perfusion fixation

A technique for preserving brain tissue where a fixative solution is pumped through the circulatory system to stabilize and preserve tissue structure. This method is essential for preparing brain specimens for microscopic examination.

| Field | Description |
|:------|:------------|
| `Perfusion method` | Method used for brain perfusion fixation (**required**) |
| `Perfusion volume (mL)` | Volume of perfusion solution in milliliters |
| `Fatal outcome` | Checkbox to indicate if the procedure resulted in a fatal outcome |

### Brain slice

Refers to ex vivo preparations obtained by sectioning brain tissue into thin slices. These slices are used for various types of experiments, including electrophysiological recordings and pharmacological studies.

| Field | Description |
|:------|:------------|
| `Thickness of slices (μm)` | Thickness of the brain slices in micrometers (**required**) |
| `Number of slices` | Number of brain slices (integer) |
| `Orientation of slices` | Orientation of the brain slices (**required**) |
| `Medium used for slice` | Medium used for maintaining the brain slices |
| `Vibratome blade angle (°)` | Angle of the vibratome blade in degrees |

## Injection and Infusion Procedures

### Virus injection

Involves injecting a virus into the brain, typically to deliver genetic material for research purposes, such as gene therapy experiments or to manipulate gene expression in specific brain regions. Typically performed with a small glass capillary.

| Field | Description |
|:------|:------------|
| `Injection volume (nL)` | Volume of virus injected in nanoliters |
| `Injection rate (nL/min)` | Rate of virus injection in nanoliters per minute |
| `Injection profile` | Profile of the virus injection |

### Coordinates

For all procedure types, coordinates are specified using the following system: [Coordinates systems page]({{"datamodel/schemas/coordinates/"|absolute_url}})

## Procedure API access

The API allows for programmable access to Procedures, enabling you to read, edit, and delete procedures through the API. Learn more about the procedures' fields and data structure on the [Procedure API page]({{"api/modules/procedure/"|absolute_url}}).