---
layout: default
title: Procedures
parent: Modules
grand_parent: Data model
nav_order: 6
---

# Procedure model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Procedures cover surgical procedures and other methods that allow tracking or recording from subject(s). Procedures have type-specific fields tailored to various procedure types. The types of procedures currently supported by BrainSTEM are listed below. A procedure is described by the fields in the next section.

## Fields

| Field | Description |
|:------|:------------|
| `Type` | Type of procedure (**required**). Selected from predefined types. Example: "Optic fiber implant". *See options below* |
| `Subject` | The subject the procedure was performed on (**required**). Must reference an existing [subjects]({{"datamodel/stem/subject/"|absolute_url}}). Example: "Mouse_01" |
| `Notes` | Notes about the procedure (string). Example: "Implant placed successfully with minimal bleeding" |
| `Date and time` | Date and time the procedure was performed. Example: "2024-03-22 10:30:00" |
| `Inventory` | The inventory record that tracks the consumable stocks (**required**). Must reference an existing [inventory]({{"datamodel/personal_attributes/inventory/"|absolute_url}}). Example: "Lab supplies inventory" |
| `Consumable stock` | Records and tracks laboratory supplies and materials used in experiments (**required**). Must be associated with an [inventory]({{"datamodel/personal_attributes/inventory/"|absolute_url}}) and have a specific type (Optic fiber, Silicon probe, Single wire electrode, or Virus solution). Example: "32-channel silicon probe in Lab A inventory" |
| `Setup` | The setup the equipment is installed in (**required**). Must reference an existing [setups]({{"datamodel/personal_attributes/setup/"|absolute_url}}). Example: "Behavior room A setup" |
| `Equipment` | Equipment used in the procedure (**required**). Must reference existing [equipment]({{"datamodel/modules/equipment/"|absolute_url}}). Example: "Intan RHD2000" |
| `Atlas` | The brain atlas used for anatomical reference (**required** if brain region is specified). Must reference an existing brain atlas. Example: "Allen Mouse Brain Atlas" |
| `Brain region` | Target brain region where the procedure was performed. Example: "Hippocampus CA1" |
| `Coordinates system` | Coordinate system (**required**). Selected from predefined systems. Example: "Stereotaxic Bregma-Based". *See options below* |
| `Type details` | Type-specific fields. Fields vary by procedure type. Example: For fiber implant - fiber tip shape. *See options below* |

## Types of procedures

These are the available *Type* options for Procedure:

### Surgical Procedures:
- `Craniectomy`: The surgical removal of a portion of the skull that is not replaced afterward. This approach provides prolonged, direct access to the brain or helps relieve increased intracranial pressure following injury.
- `Craniotomy`: A procedure in which part of the skull is temporarily removed to expose the brain. After surgery or research activities are completed, the bone flap is typically replaced, restoring the skull’s integrity.
- `Cranial window`: A surgical technique where a small section of skull is replaced with a transparent window. This allows for direct, long-term optical access to the brain’s surface for imaging and other optical investigations.

### Implant Procedures:
- `Optic fiber implant`: The surgical placement of a tiny optic fiber into brain tissue, commonly used in optogenetics. By delivering or detecting light, researchers can modulate or record neuronal activity in precise brain regions.
- `Silicon probe implant`: The insertion of a silicon-based probe equipped with multiple recording sites. These probes enable high-density recordings from many neurons simultaneously, facilitating detailed studies of neural circuits.
- `Single wire electrode`: The implantation of a thin wire electrode into the brain for recording electrical activity or stimulating neurons. This targeted approach aids in understanding single-neuron contributions to brain function.
- `Tetrode wire electrode`: The introduction of a four-wire electrode (tetrode) bundle into the brain. Tetrodes allow researchers to monitor and differentiate signals from multiple adjacent neurons, greatly enhancing the resolution of neural recordings.

### Injection and Infusion Procedures:
- `Injection`: The delivery of solutions, often containing genetic or pharmacological agents, directly into targeted brain areas. This method is commonly performed using a small glass capillary and can be used to alter gene expression or modulate neural activity.
- `Virus injection`: Similar to the above, but specifically involves injecting viral vectors to introduce or manipulate genetic material in targeted neuronal populations. This approach is key for studying gene function and developing gene therapies.

### Brain and Tissue Procedures:
- `Brain lesion`: A deliberate injury or destruction of a specific brain region to investigate its role in behavior, cognition, and physiological processes. Lesion studies help map functions to particular brain areas.
- `Brain perfusion fixation`: A tissue-preservation method in which a fixative solution is perfused through the circulatory system, stabilizing the brain’s structure for microscopic examination. This technique ensures that cellular and tissue-level details are well-preserved.
- `Brain slice`: The preparation of thin, ex vivo sections of brain tissue for detailed examination. Brain slices can be used for electrophysiological recordings, imaging, and testing pharmacological agents, providing insights into local circuit properties.

A detailed list of the type-specific fields can be found on the [procedure types page]({{"datamodel/schemas/procedure/"|absolute_url}}).


## Coordinate system options

Available Coordinate system options for Procedure:

| Type | Description |
|:-----|:------------|
| `External X-Y-Z Coordinates with Angles` | Three-dimensional Cartesian system with absolute positions (X, Y, Z) and angles relative to an external reference point. Ideal for precise global positioning. |
| `Stereotaxic Bregma-Based Absolute` | Stereotaxic coordinates using Bregma on the skull as origin. Uses AP, ML, DV coordinates and angles for precise skull-based targeting. |
| `Stereotaxic Bregma-Based Surface with Depth` | Stereotaxic coordinates measuring from brain surface beneath Bregma. Uses AP, ML coordinates, depth, and rotation. Accommodates brain surface curvature. |
| `Stereotaxic Lambda-Based Absolute` | Stereotaxic coordinates using Lambda on the skull as origin. Uses AP, ML, DV coordinates and angles. Alternative skull-based reference point for varied setups. |
| `Stereotaxic Lambda-Based Surface with Depth` | Stereotaxic coordinates measuring from brain surface beneath Lambda. Uses AP, ML coordinates, depth, and rotation. Useful for targeting occipital brain areas. |
| `Stereotaxic X-Y-Z Absolute` | Stereotaxic coordinates using X, Y, Z absolute positions and angles. Enables precise navigation within stereotaxic frame. |
| `Stereotaxic X-Y Surface with Depth` | Stereotaxic coordinates using X, Y positions on brain surface, plus depth and rotation. For experiments needing lateral and anteroposterior precision. |

A detailed list of the fields in Coordinate system can be found on the [Coordinate system page]({{"datamodel/schemas/coordinates/"|absolute_url}}).

## Permissions

Procedures inherit permissions through the subject associated with them.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## API access
The API allows for programmable access to procedures. Learn more about the procedures' fields and data structure on the [Procedures API page]({{"api/modules/procedure/"|absolute_url}}).
