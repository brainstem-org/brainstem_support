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

### Cranial window

A surgical procedure to create a transparent window in the skull, allowing for optical access to the brain for imaging or other experimental purposes.

| Field | Description |
|:------|:------------|
| `Method of cranial window` | Surgical technique used (string; required). Common methods include surgical drill, bone saw, manual/automatic cutting tools |
| `Shape of cranial window` | Shape of the window performed (string; required). Such as square, circular, elliptical, etc |
| `Length of cranial window (µm)` | Length dimension of the window (float, ≥ 0; required; measured in micrometers). Critical for determining exposure area |
| `Width of cranial window (µm)` | Width dimension of the window (float, ≥ 0; required; measured in micrometers). Important for planning surgical access |
| `Thickness of cranial window (µm)` | Thickness of the window (float, ≥ 0; measured in micrometers). Affects optical properties |
| `Orientation of cranial window` | Orientation relative to anatomical landmarks (string). Includes angle and direction for precise targeting |

### Craniectomy

Involves the surgical removal of a portion of the skull to access the brain, without replacing the skull bone afterward. This procedure is often used in cases requiring prolonged brain access or to alleviate pressure after brain injury.

| Field | Description |
|:------|:------------|
| `Method of craniectomy` | Surgical technique used for the craniectomy (string; required). Common methods include surgical drill, bone saw, or manual cutting tools |
| `Shape of craniectomy` | Shape of the craniectomy (string; required). Describes form such as square, circular, oval, or irregular |
| `Length of craniectomy (μm)` | Length of the craniectomy (float, ≥ 0; required; measured in micrometers). Critical dimension for exposure |
| `Width of craniectomy (μm)` | Width of the craniectomy (float, ≥ 0; required; measured in micrometers). Important for access planning |
| `Orientation of craniectomy` | Orientation relative to major anatomical landmarks (string). Helps define spatial relationships |
| `Fatal outcome` | Whether procedure resulted in fatal outcome (boolean). Indicates procedure mortality |

### Craniotomy

A surgical procedure where part of the skull is temporarily removed to expose the brain for surgery or research purposes. The removed bone is typically replaced after the procedure, making it a temporary opening.

| Field | Description |
|:------|:------------|
| `Method of craniotomy` | Surgical technique used for the craniotomy (string; required). Involves surgical drill, bone saw, or cutting tools |
| `Shape of craniotomy` | Shape of the craniotomy performed (string; required). Such as square, circular, or elliptical |
| `Length of craniotomy (μm)` | Length of the craniotomy (float, ≥ 0; required; measured in micrometers). Critical for brain area exposure |
| `Width of craniotomy (μm)` | Width of the craniotomy (float, ≥ 0; required; measured in micrometers). Important for surgical access |
| `Orientation of craniotomy` | Orientation relative to anatomical landmarks (string). Includes angle and direction for targeting |
| `Fatal outcome` | Whether procedure resulted in fatal outcome (boolean). Tracks procedure mortality |

## Implant Procedures

### Optic fiber implant

Involves the surgical implantation of an optic fiber into the brain, often used in optogenetics research to manipulate or record neuronal activity with light.

| Field | Description |
|:------|:------------|
| `Fiber tip shape` | Shape of the optic fiber tip (string; required). Common shapes include flat, angled, or rounded |
| `Fiber ID` | Unique identifier for the optic fiber (string). For tracking purposes |
| `Sterilization Method` | Method used for sterilization (string; enum: [Autoclave, Ethylene Oxide, Gamma Irradiation, Alcohol, None]). Ensures implant safety |

### Silicon probe implant

Involves the implantation of a silicon probe, a device equipped with multiple recording sites, into the brain. Silicon probes are used for high-density recording of neural activity.

| Field | Description |
|:------|:------------|
| `Probe ID` | Unique identifier for the silicon probe (string). For tracking purposes |
| `Sterilization Method` | Method used for sterilization (string; enum: [Autoclave, Ethylene Oxide, Gamma Irradiation, Alcohol, None]). Ensures implant safety |

### Single wire electrode

Refers to the implantation of a single wire electrode into the brain, used for recording electrical activity from or stimulating specific neurons or brain areas.

| Field | Description |
|:------|:------------|
| `Wire count` | Number of wires in electrode assembly (integer, ≥ 0; required; default: 1) |
| `Wire diameter (μm)` | Diameter of electrode wire (float, ≥ 0; measured in micrometers). Affects impedance and capabilities |
| `Wire material` | Material of the wire (string). Common options include stainless steel, platinum-iridium, gold |
| `Impedance (kOhms)` | Electrical impedance (float; measured in kiloohms). Critical for recording equipment matching |
| `Sterilization Method` | Sterilization technique used (string; enum: [Autoclave, Ethylene Oxide, Gamma Irradiation, Alcohol, None]) |

### Tetrode wire electrode

The implantation of a tetrode, a device made of four intertwined wire electrodes, into the brain. Tetrodes allow for the recording of electrical signals from multiple neurons simultaneously.

| Field | Description |
|:------|:------------|
| `Tetrode count` | Number of tetrodes in assembly (integer, ≥ 0; required; default: 1). Used for different brain regions |
| `Wires per tetrode` | Number of wires per tetrode (integer, ≥ 0; default: 4). Standard tetrodes use four wires |
| `Wire diameter (μm)` | Diameter of the wires (float, ≥ 0; measured in micrometers). Affects recording quality |
| `Wire material` | Material used for wires (string). Options include platinum-iridium, stainless steel, nichrome |
| `Sterilization Method` | Method used for sterilization (string; enum: [Autoclave, Ethylene Oxide, Gamma Irradiation, Alcohol, None]) |

## Brain and Tissue Procedures

### Brain lesion

A surgical procedure that intentionally damages or destroys brain tissue to study the functions of specific brain areas. Lesions can help identify the roles of different brain regions in behavior and cognition.

| Field | Description |
|:------|:------------|
| `Lesion method` | Technique used for lesion (string; required). Such as surgical, suction, chemical, thermal methods |
| `Volume of brain lesion (μL)` | Estimated volume of the lesion (float, ≥ 0; required; measured in microliters) |
| `Fatal outcome` | Whether lesion results in mortality (boolean). Tracks procedure outcome |

### Brain perfusion fixation

A technique for preserving brain tissue where a fixative solution is pumped through the circulatory system to stabilize and preserve tissue structure. This method is essential for preparing brain specimens for microscopic examination.

| Field | Description |
|:------|:------------|
| `Perfusion method` | Method used for fixation (string; required). Details the perfusion approach |
| `Perfusion volume (mL)` | Volume of fixative solution (float, ≥ 0; measured in milliliters). Important for tissue preservation |
| `Fatal outcome` | Whether procedure is terminal (boolean). Indicates procedure mortality |

### Brain slice

Refers to ex vivo preparations obtained by sectioning brain tissue into thin slices. These slices are used for various types of experiments, including electrophysiological recordings and pharmacological studies.

| Field | Description |
|:------|:------------|
| `Thickness of slices (μm)` | Thickness of brain slices (float, ≥ 0; required; measured in micrometers; default: 50) |
| `Number of slices` | Total slices obtained (integer, ≥ 0). Tracks preparation quantity |
| `Orientation of slices` | Slice orientation (string; required; default: "coronal"). Such as coronal, sagittal, horizontal |
| `Medium used for slice` | Preservation medium (string). Such as aCSF or specific preservation solutions |
| `Vibratome blade angle (°)` | Angle of vibratome blade (float, ≥ 0; measured in degrees). For precise cutting |

## Injection and Infusion Procedures

### Virus injection

Involves injecting a virus into the brain, typically to deliver genetic material for research purposes, such as gene therapy experiments or to manipulate gene expression in specific brain regions. Typically performed with a small glass capillary.

| Field | Description |
|:------|:------------|
| `Injection volume (nL)` | Volume of viral solution (float, ≥ 0; required; measured in nanoliters) |
| `Injection rate (nL/min)` | Rate of injection (float, ≥ 0; measured in nanoliters/minute). Controls distribution |
| `Titer (units/mL)` | Viral solution concentration (float, ≥ 0; measured in units/mL). Differs from stock titer |
| `Titer unit` | Unit of titer measurement (string; enum: [vg/mL, TU/mL, pfu/mL]). Specifies concentration type |
| `Injection profile` | Delivery method (string; enum: [Bolus Injection, Continuous Infusion, etc]). Defines administration pattern |

### Coordinates

For all procedure types, coordinates are specified using the following system: [Coordinates systems page]({{"datamodel/schemas/coordinates/"|absolute_url}})

## Procedure schemas API access

The API allows for programmable access to Procedures, enabling you to read, edit, and delete procedures through the API. Learn more about the procedures' fields and data structure on the [Procedure API page]({{"api/schemas/procedure/"|absolute_url}}).