---
layout: default
title: Relations
parent: Schemas
grand_parent: Data model
nav_order: 9
---

# Relations
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Relations define which items you can select in one module based on selections made in another module. When you select certain types in a module, the available options in related fields will be automatically filtered to show only relevant choices.

## Module Relations

### Consumable Stock Relations

| Consumable Stock Type | Available Comsumable Type |
|:---------------------------|:---------------------------|
| Optic fiber | Optic fiber designs |
| Silicon probe | Silicon probe designs |
| Single wire electrode | Single wire electrode designs |
| Virus solution | Virus constructs |

### Data Acquisition Relations

| Data Acquisition Type | Available Procedure Type |
|:---------------------------|:------------------------------------------|
| Audio | Silicon probe implant, Tetrode wire electrode, Single wire electrode |
| Behavioral tracking | Silicon probe implant, Tetrode wire electrode, Single wire electrode |
| Computed Tomography (CT) | Silicon probe implant, Tetrode wire electrode, Single wire electrode |
| Confocal Microscopy | Silicon probe implant, Tetrode wire electrode, Single wire electrode |
| Electroencephalography (EEG) | Silicon probe implant, Tetrode wire electrode, Single wire electrode |
| Electroneurogram (ENG) | Silicon probe implant, Tetrode wire electrode, Single wire electrode |
| Extracellular Electrophysiology | Silicon probe implant, Tetrode wire electrode, Single wire electrode |
| Fiber Photometry | Optic fiber implant |
| Functional Magnetic Resonance Imaging (fMRI) | [Relations to be defined] |
| Functional Ultrasound Imaging (fUS) | [Relations to be defined] |
| General Time Series | Silicon probe implant, Tetrode wire electrode, Single wire electrode, Optic fiber implant |
| Intracellular Electrophysiology | Tetrode wire electrode, Single wire electrode |
| Light Field Microscopy (LFM) | Optic fiber implant, Cranial window, Craniectomy, Craniotomy |
| Magnetic Resonance Imaging (MRI) | [Relations to be defined] |
| Magnetoencephalography (MEG) | [Relations to be defined] |
| Miniscope Microscopy | Optic fiber implant, Cranial window, Craniectomy, Craniotomy |
| Positron Emission Tomography (PET) | Optic fiber implant, Cranial window, Craniectomy, Craniotomy |
| Single-Photon Emission Computed Tomography (SPECT) | [Relations to be defined] |
| Single-Photon Microscopy | Optic fiber implant, Cranial window, Craniectomy, Craniotomy |
| Two-Photon Microscopy | Optic fiber implant, Cranial window, Craniectomy, Craniotomy |
| Three-Photon Microscopy | Optic fiber implant, Cranial window, Craniectomy, Craniotomy |

### Equipment Relations

All equipment types have the following relations:
- Can select from these consumables: Optic fiber designs, Silicon probe designs, Virus constructs, Single wire electrodes
- Uses External XYZ Absolute coordinates

### Manipulation Relations 

| Manipulation Type | Available Procedure Type |
|:-----------------|:-------------------------|
| Deep Brain Stimulation (DBS) | - Silicon Probe Implant<br>- Tetrode Wire Electrode<br>- Single Wire Electrode<br>- Optic Fiber Implant |
| Electrical Stimulation | - Silicon Probe Implant<br>- Tetrode Wire Electrode<br>- Single Wire Electrode<br>- Optic Fiber Implant |
| Electromagnetic Field Stimulation | - Silicon Probe Implant<br>- Tetrode Wire Electrode<br>- Single Wire Electrode<br>- Optic Fiber Implant |
| Liquid Perturbation | - Silicon Probe Implant<br>- Tetrode Wire Electrode<br>- Single Wire Electrode<br>- Optic Fiber Implant |
| Microperfusion | - Silicon Probe Implant<br>- Tetrode Wire Electrode<br>- Single Wire Electrode<br>- Optic Fiber Implant |
| Odor Stimulation | - Silicon Probe Implant<br>- Tetrode Wire Electrode<br>- Single Wire Electrode<br>- Optic Fiber Implant |
| Optogenetic Stimulation | - Silicon Probe Implant<br>- Tetrode Wire Electrode<br>- Single Wire Electrode<br>- Optic Fiber Implant |
| Pharmacological Inhalation | - Silicon Probe Implant<br>- Tetrode Wire Electrode<br>- Single Wire Electrode<br>- Optic Fiber Implant |
| Pharmacological Injection | - Silicon Probe Implant<br>- Tetrode Wire Electrode<br>- Single Wire Electrode<br>- Optic Fiber Implant |
| Pharmacological Superfusion | - Silicon Probe Implant<br>- Tetrode Wire Electrode<br>- Single Wire Electrode<br>- Optic Fiber Implant |
| Sound Stimulation | - Silicon Probe Implant<br>- Tetrode Wire Electrode<br>- Single Wire Electrode<br>- Optic Fiber Implant |
| Thermal Perturbation | - Silicon Probe Implant<br>- Tetrode Wire Electrode<br>- Single Wire Electrode<br>- Optic Fiber Implant |
| Transcranial Electrical Stimulation | - Silicon Probe Implant<br>- Tetrode Wire Electrode<br>- Single Wire Electrode<br>- Optic Fiber Implant |
| Transcranial Magnetic Stimulation (TMS) | - Silicon Probe Implant<br>- Tetrode Wire Electrode<br>- Single Wire Electrode<br>- Optic Fiber Implant |
| Ultrasound Stimulation | - Silicon Probe Implant<br>- Tetrode Wire Electrode<br>- Single Wire Electrode<br>- Optic Fiber Implant |

### Procedure Relations

| Procedure Type | Available Consumable Stock Type | Available Coordinate System |
|:--------------|:--------------------------------|:---------------------------|
| Brain Lesion | - Silicon Probe<br>- Single Wire Electrode | - Stereotaxic Bregma Brain Surface<br>- Stereotaxic Lambda Brain Surface<br>- Common Coordinate Framework XYZ Absolute<br>- Stereotaxic Bregma Absolute<br>- Stereotaxic Lambda Absolute |
| Cranial Window | - Silicon Probe<br>- Single Wire Electrode | - Stereotaxic Bregma Brain Surface<br>- Stereotaxic Lambda Brain Surface<br>- Common Coordinate Framework XYZ Absolute<br>- Stereotaxic Bregma Absolute<br>- Stereotaxic Lambda Absolute |
| Craniectomy | - Silicon Probe<br>- Single Wire Electrode | - Stereotaxic Bregma Brain Surface<br>- Stereotaxic Lambda Brain Surface<br>- Common Coordinate Framework XYZ Absolute<br>- Stereotaxic Bregma Absolute<br>- Stereotaxic Lambda Absolute |
| Craniotomy | - Silicon Probe<br>- Single Wire Electrode | - Stereotaxic Bregma Brain Surface<br>- Stereotaxic Lambda Brain Surface<br>- Common Coordinate Framework XYZ Absolute<br>- Stereotaxic Bregma Absolute<br>- Stereotaxic Lambda Absolute |
| Injection | - Silicon Probe | - Stereotaxic Bregma Brain Surface<br>- Stereotaxic Lambda Brain Surface<br>- Common Coordinate Framework XYZ Absolute<br>- Stereotaxic Bregma Absolute<br>- Stereotaxic Lambda Absolute |
| Optic Fiber Implant | - Optic Fiber | - Stereotaxic Bregma Brain Surface<br>- Stereotaxic Lambda Brain Surface<br>- Common Coordinate Framework XYZ Absolute<br>- Stereotaxic Bregma Absolute<br>- Stereotaxic Lambda Absolute |
| Perfusion Fixation | - Silicon Probe<br>- Single Wire Electrode | - Stereotaxic Bregma Brain Surface<br>- Stereotaxic Lambda Brain Surface<br>- Common Coordinate Framework XYZ Absolute<br>- Stereotaxic Bregma Absolute<br>- Stereotaxic Lambda Absolute |
| Silicon Probe Implant | - Silicon Probe | - Stereotaxic Bregma Brain Surface<br>- Stereotaxic Lambda Brain Surface<br>- Common Coordinate Framework XYZ Absolute<br>- Stereotaxic Bregma Absolute<br>- Stereotaxic Lambda Absolute |
| Single Wire Electrode | - Single Wire Electrode | - Stereotaxic Bregma Brain Surface<br>- Stereotaxic Lambda Brain Surface<br>- Common Coordinate Framework XYZ Absolute<br>- Stereotaxic Bregma Absolute<br>- Stereotaxic Lambda Absolute |
| Slice | - Silicon Probe<br>- Single Wire Electrode | - Stereotaxic Bregma Brain Surface<br>- Stereotaxic Lambda Brain Surface<br>- Common Coordinate Framework XYZ Absolute<br>- Stereotaxic Bregma Absolute<br>- Stereotaxic Lambda Absolute |
| Tetrode Wire Electrode | - Silicon Probe<br>- Single Wire Electrode | - Stereotaxic Bregma Brain Surface<br>- Stereotaxic Lambda Brain Surface<br>- Common Coordinate Framework XYZ Absolute<br>- Stereotaxic Bregma Absolute<br>- Stereotaxic Lambda Absolute |
| Virus Injection | - Virus Solution | - Stereotaxic Bregma Brain Surface<br>- Stereotaxic Lambda Brain Surface<br>- Common Coordinate Framework XYZ Absolute<br>- Stereotaxic Bregma Absolute<br>- Stereotaxic Lambda Absolute |

### Procedure Log Relations

| Manipulation Type | Available Procedure Type |
|:-----------------|:-------------------------|
| Impedences | |
| Linear Displacements | |


### Subject Log Relations

| Manipulation Type | Available Procedure Type |
|:-----------------|:-------------------------|
| Food Deprivation Log |  |
| Water Deprivation Log |  |
| Weighing Log |  |
