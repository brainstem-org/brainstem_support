---
layout: default
title: Experiment data
parent: Modules
grand_parent: Data model
nav_order: 5
---

# Manipulation model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction
Experiment data encompasses the diverse range of data types acquired during scientific experiments. These data types are crucial for understanding the complex workings of the brain and nervous system, offering insights into neural function, structure, behavior, and the effects of various interventions. Experiment data types share relationships, but fields are tailored to the various data-types.

## Fields

| Field           | Description  |
|:----------------|:-------------|
| Dataset         | Dataset of the manipulation  (**required**) |
| Type            | Type of manipulation (**required**). *See options below* |
| Procedures      | Related subject procedures (**required**) |
| Installations   | The Installations used to acquire the data with (**required**).|
| Notes           | Notes of the manipulation (max length: 500) |
| Hardware device | Hardware device used to perform the manipulation |
| Type details    | There are also a number of type specific fields. *See options below* |

## Types of experiment data
These are the available _Type_ options for manipulations:
- Audio
- Behavioral Tracking
- Computed tomography (CT)
- Electroencephalography (EEG)
- Electroneurogram (ENG)
- Confocal Microscopy
- Extracellular Electrophysiology
- Fiber Photometry
- Functional Magnetic Resonance Imaging (fMRI)
- Functional Ultrasound Imaging (fUS)
- Intracellular Electrophysiology
- Light Field Microscopy: Light field microscopy (LFM)
- Magnetic Resonance Imaging (MRI)
- Magnetoencephalography (MEG)
- Miniscope Microscopy
- Positron Emission Tomography (PET)
- Single-photon emission computed tomography (SPECT)
- Single-Photon Microscopy
- Two-Photon Microscopy
- Three-Photon Microscopy

A detailed list of the type-specific fields, can be found in the [experiment data type page]({{"/datamodel/schemas/experiment_data/"|absolute_url}}).


## Permissions
Experiment data inherit permissions through the dataset associated with it.

Visit the [permissions page] to learn more.


## Manipulation API access
The API allows for programmable access to experiment data. Learn more about the 'experiment data' fields and data structure on the [experiment data API page]({{"api/modules/experiment_data/"|absolute_url}}). 
