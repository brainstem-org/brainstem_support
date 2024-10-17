---
layout: default
title: Experiment data
parent: Modules
grand_parent: Data model
nav_order: 2
---

# Experiment data model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Experiment data encompasses the diverse range of data types acquired during scientific experiments. These data types are crucial for understanding the complex workings of the brain and nervous system, offering insights into neural function, structure, behavior, and the effects of various interventions. While experiment data types share relationships, fields are tailored to the various data types.

## Fields

| Field | Description |
|:------|:------------|
| `Dataset` | Dataset of the experiment data (**required**) |
| `Type` | Type of experiment data (**required**). *See options below* |
| `Procedures` | Related subject procedures (**required**) |
| `Installations` | Installations used to acquire the data (**required**) |
| `Notes` | Notes about the experiment data (max length: 500 characters) |
| `Hardware device` | Hardware device used to perform the data acquisition |
| `Type details` | Type-specific fields. *See options below* |

## Types of experiment data

These are the available *Type* options for experiment data:

- Audio
- Behavioral Tracking
- Computed Tomography (CT)
- Electroencephalography (EEG)
- Electroneurogram (ENG)
- Confocal Microscopy
- Extracellular Electrophysiology
- Fiber Photometry
- Functional Magnetic Resonance Imaging (fMRI)
- Functional Ultrasound Imaging (fUS)
- Intracellular Electrophysiology
- Light Field Microscopy (LFM)
- Magnetic Resonance Imaging (MRI)
- Magnetoencephalography (MEG)
- Miniscope Microscopy
- Positron Emission Tomography (PET)
- Single-Photon Emission Computed Tomography (SPECT)
- Single-Photon Microscopy
- Two-Photon Microscopy
- Three-Photon Microscopy

A detailed list of the type-specific fields can be found on the [experiment data types page]({{"datamodel/schemas/experiment_data/"|absolute_url}}).

## Permissions

Experiment data inherits permissions through its associated dataset.

Visit the [permissions page] to learn more.

## Experiment data API access

The API allows for programmable access to experiment data. Learn more about the experiment data fields and data structure on the [Experiment data API page]({{"api/modules/experiment_data/"|absolute_url}}).
