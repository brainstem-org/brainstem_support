---
layout: default
title: Data acquisition
parent: Modules
grand_parent: Data model
nav_order: 2
---

# Data acquisition model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Data acquisition encompasses the diverse range of data types acquired during scientific experiments. These data types are crucial for understanding the complex workings of the brain and nervous system, offering insights into neural function, structure, behavior, and the effects of various interventions. While Data acquisition types share relationships, fields are tailored to the various data types.

## Fields

| Field | Description |
|:------|:------------|
| `Session` | Session of the data acquisition (**required**). Must reference an existing [session]({{"datamodel/stem/session/"|absolute_url}}). Example: "Recording session #3" |
| `Type` | Type of data acquisition (**required**). Selected from predefined types. Example: "Extracellular Electrophysiology". *See options below* |
| `Procedures` | Related subject procedures (**required**). Must reference existing [procedures]({{"datamodel/modules/procedure/"|absolute_url}}). Example: "Silicon probe implant #A123" |
| `Equipments` | Equipments used to acquire the data (**required**). Must reference existing [equipment]({{"datamodel/modules/equipment/"|absolute_url}}). Example: "Intan RHD2000" |
| `Notes` | Notes about the data acquisition (string). Example: "Good signal quality throughout recording" |
| `Hardware device` | Hardware device used to perform the data acquisition. Example: "Neuralynx Digital Lynx" |
| `Type details` | Type-specific fields. Fields vary by acquisition type. Example: For electrophysiology - sampling rate, number of channels. *See options below* |

## Types of Data acquisition

These are the available *Type* options for data acquisition:

### Audio and Behavioral Tracking
- Audio
- Behavioral Tracking

### Electrophysiology
- Electroencephalography (EEG)
- Electroneurogram (ENG)
- Extracellular Electrophysiology
- Intracellular Electrophysiology

### Optical Imaging
- Confocal Microscopy
- Fiber Photometry
- Light Field Microscopy (LFM)
- Miniscope Microscopy
- Single-Photon Microscopy
- Two-Photon Microscopy
- Three-Photon Microscopy

### Magnetic and Functional Imaging
- Functional Magnetic Resonance Imaging (fMRI)
- Magnetic Resonance Imaging (MRI)
- Magnetoencephalography (MEG)

### Tomography and Ultrasound
- Computed Tomography (CT)
- Positron Emission Tomography (PET)
- Single-Photon Emission Computed Tomography (SPECT)
- Functional Ultrasound Imaging (fUS)

A detailed list of the type-specific fields can be found on the [Data acquisition types page]({{"datamodel/schemas/dataacquisition/"|absolute_url}}).

## Permissions

Data acquisition inherits permissions through its associated session.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## Data acquisition API access

The API allows for programmable access to data acquisition. Learn more about the data acquisition fields and data structure on the [data acquisition API page]({{"api/modules/dataacquisition/"|absolute_url}}).
