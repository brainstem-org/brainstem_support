---
layout: default
title: Procedures
parent: Subjects
grand_parent: Data model
nav_order: 1
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
| ``Type of procedure`` | Type of procedure (**required**). Selected from predefined types. Example: "Optic fiber implant". *See options below* |
| ``Subject`` | The subject the procedure was performed on (**required**). Must reference an existing [subjects]({{"datamodel/stem/subject/"|absolute_url}}). Example: "Mouse_01" |
| ``Date and time of the procedure`` | Date and time the procedure was performed. Example: "2024-03-22 10:30:00" |
| ``Inventory`` | Inventory filter for consumable stocks. Used to filter available consumable stocks by inventory. |
| ``Consumable stock`` | Consumable stock used in the procedure. Must reference an existing [consumable stock]({{"datamodel/modules/consumablestock/"|absolute_url}}). Example: "32-channel silicon probe" |
| ``Setup`` | Setup filter for equipment. Used to filter available equipment by setup. |
| ``Equipment`` | Equipment used in the procedure. Must reference existing [equipment]({{"datamodel/modules/equipment/"|absolute_url}}). Example: "Intan RHD2000" |
| ``Atlas`` | Brain atlas filter for brain regions. Used to filter available brain regions by atlas. |
| ``Brain region`` | Target brain region of the procedure. Must reference an existing [brain region]({{"datamodel/taxonomies/brainregion/"|absolute_url}}). Example: "Hippocampus CA1" |
| ``Notes`` | Notes about the procedure (string). Example: "Implant placed successfully with minimal bleeding" |
| ``Type specific fields`` | Custom fields based on procedure type in JSON format. See [Procedure types schema]({{"datamodel/schemas/procedure/"|absolute_url}}) for type-specific fields |

## Types of procedures

These are the available type options for procedures:

See the schema for field details: [Procedure types]({{"datamodel/schemas/procedure/"|absolute_url}}).

### Surgical Procedures

`Anesthesia`: Administration of anesthetic agents to provide analgesia and sedation during procedures.

`Burr hole`: Drilling small openings in the skull to access brain tissue or place probes/electrodes.

`Cranial window`: Replacing a skull section with a transparent window for optical access to the cortical surface.

`Craniectomy`: Permanent removal of a skull portion to provide extended access to brain tissue.

`Craniotomy`: Temporary removal of a skull flap to expose brain, with the bone replaced afterwards.

`Headcap`: Protective cap applied to the skull to cover and secure implants post‑surgery.

`Head fixation`: Stabilizing the head mechanically to ensure immobility during recordings or procedures.

`Headpost`: Implanting a post to secure the head during procedures or behavioral tasks.

### Implant Procedures

`Blood pressure sensor implant`: Implanting a device to continuously monitor blood pressure within the cardiovascular system.

`Breathing sensor implant`: Implanting sensors to monitor respiratory rate, pattern, and function.

`GRIN (Gradient Index) lens implant`: Implanting a gradient‑index lens to enable deep‑brain optical imaging.

`Catheter implant`: Placing a catheter for drug delivery or physiological fluid access/monitoring.

`ECG implant (Electrocardiography)`: Implanting electrodes to record the heart’s electrical activity.

`EEG implant (Electroencephalography)`: Implanting electrodes to record electrical activity of the brain.

`EMG implant (Electromyography)`: Implanting electrodes to record muscle electrical activity.

`Nerve cuff implant`: Placing a cuff electrode around a nerve for recording or stimulation.

`Optic fiber implant`: Implanting an optical fiber into brain tissue for optogenetic light delivery or collection.

`Prism implant`: Implanting a prism to redirect light paths for optical imaging experiments.

`Reference electrode implant`: Implanting a reference electrode to stabilize electrical recordings.

`Silicon probe implant`: Implanting silicon probes with multiple sites for high‑density neural recordings.

`Single wire electrode implant`: Implanting a thin wire electrode for recording or stimulation.

`Temperature sensor implant`: Implanting a device to monitor physiological temperature changes.

`Tetrode wire electrode implant`: Implanting a four‑wire (tetrode) bundle to record from nearby neurons simultaneously.

`Generic implant`: Flexible category for implants not covered above (e.g., sensors, optical devices, custom tools).

### Injection and Infusion Procedures

`Injection`: Delivering pharmacological or genetic solutions directly into targeted brain areas.

`Virus injection`: Injecting viral vectors to introduce or manipulate genes in targeted cell populations.

### Brain and Tissue Procedures

`Brain extraction`: Removing the brain for ex vivo processing and analysis.

`Brain lesion`: Creating a targeted injury to a brain region to study its function.

`Brain slice`: Preparing thin tissue sections for ex vivo recordings, imaging, and testing.

`Cryosectioning`: Sectioning frozen tissue into thin slices for histology.

`Brain perfusion fixation`: Preserving tissue by perfusing fixative through the circulatory system.

`Tissue clearing`: Chemically rendering tissue transparent for deep imaging.

`Vibratome sectioning`: Cutting tissue slices with a vibrating blade to preserve structure.

### Endpoint Procedures (Euthanasia)

`Cervical dislocation`: Euthanasia by dislocation of the cervical vertebrae.

`Decapitation`: Euthanasia by removal of the head.

`CO₂ chamber euthanasia`: Euthanasia using a controlled carbon dioxide chamber.

`Barbiturate Injection`: Euthanasia by barbiturate overdose injection.

`Inhalant Overdose`: Euthanasia by overdose of inhalant anesthetics.

### Abstract procedures

`Auditory stimulation`: Presenting controlled auditory stimuli to probe sensory processing and neural responses.

`Behavioral tracking`: Monitoring and quantifying behavior and movement during experiments.

`Odor stimulation`: Presenting controlled olfactory stimuli to study sensory processing and behavior.

`Tactile stimulation`: Applying touch or pressure stimuli to study somatosensory processing.

`Visual stimulation`: Presenting visual stimuli to study visual processing and neural activity.




## Coordinate system options

Available coordinate system options for procedures:

| Type | Description |
|:-----|:------------|
| External XYZ Coordinates with Angles | Three-dimensional Cartesian system with absolute positions (X, Y, Z) and angles relative to an external reference point. Ideal for precise global positioning. |
| Stereotaxic Bregma-Based Absolute Coordinates | Stereotaxic coordinates using Bregma on the skull as origin. Uses AP, ML, DV coordinates and angles for precise skull-based targeting. |
| Stereotaxic Bregma-Based Surface Coordinates with Depth | Stereotaxic coordinates measuring from brain surface beneath Bregma. Uses AP, ML coordinates, depth, and rotation. Accommodates brain surface curvature. |
| Stereotaxic Lambda-Based Absolute Coordinates | Stereotaxic coordinates using Lambda on the skull as origin. Uses AP, ML, DV coordinates and angles. Alternative skull-based reference point for varied setups. |
| Stereotaxic Lambda-Based Surface Coordinates with Depth | Stereotaxic coordinates measuring from brain surface beneath Lambda. Uses AP, ML coordinates, depth, and rotation. Useful for targeting occipital brain areas. |
| Common Coordinate Framework XYZ Absolute Coordinates | Common Coordinate Framework using X, Y, Z absolute positions and angles. |

A detailed description of the coordinate systems can be found on the [Coordinate systems page]({{"datamodel/schemas/coordinates/"|absolute_url}}).

## Permissions

Procedures inherit permissions through the subject associated with them.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

 
## API access

The API allows for programmable access to procedures. Learn more about the procedures' fields and data structure on the [Procedures API page]({{"api/modules/procedure/"|absolute_url}}).
