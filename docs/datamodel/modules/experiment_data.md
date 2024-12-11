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
| `Session` | Session of the data acquisition (**required**) |
| `Type` | Type of data acquisition (**required**). *See options below* |
| `Procedures` | Related subject procedures (**required**) |
| `Equipments` | Equipments used to acquire the data (**required**) |
| `Notes` | Notes about the data acquisition (max length: 500 characters) |
| `Hardware device` | Hardware device used to perform the data acquisition |
| `Type details` | Type-specific fields. *See options below* |

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

A detailed list of the type-specific fields can be found on the [Data acquisition types page]({{"datamodel/schemas/experiment_data/"|absolute_url}}).

## Permissions

Data acquisition inherits permissions through its associated session.

Visit the [permissions page]({{"datamodel/permission/"|absolute_url}}) to learn more. 

## Data acquisition API access

The API allows for programmable access to data acquisition. Learn more about the data acquisition fields and data structure on the [data acquisition API page]({{"api/modules/experiment_data/"|absolute_url}}).
