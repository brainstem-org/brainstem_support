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
| `Equipment` | Equipment used to acquire the data (**required**). Must reference existing [equipment]({{"datamodel/modules/equipment/"|absolute_url}}). Example: "Intan RHD2000" |
| `Notes` | Notes about the data acquisition (string). Example: "Good signal quality throughout recording" |
| `Hardware devices` | Hardware device used to perform the data acquisition. Example: "Neuralynx Digital Lynx" |
| `Type details` | Type-specific fields. Fields vary by acquisition type. Example: For electrophysiology - sampling rate, number of channels. *See options below* |

## Types of Data acquisition

These are the available *Type* options for Data acquisition:

### Audio and Behavior Tracking
- `Audio`: Recordings of sounds, vocalizations, or auditory stimuli. These datasets aid in examining how the brain processes sound, supports communication, and integrates auditory information into behavior.
- `Behavioral Tracking`: Monitoring and quantifying subjects’ movements, actions, and responses under specific conditions. This information is vital for linking neural activity to behavior, learning, memory, and decision-making processes.

### Electrophysiology
- `Electroencephalography (EEG)`: Non-invasive recordings of the brain’s electrical activity from electrodes placed on the scalp. EEG helps researchers study large-scale neural dynamics, sleep states, sensory processing, and cognitive functions.
- `Electroneurogram (ENG)`: Direct measurements of electrical activity from nerves or neurons in the central or peripheral nervous system. ENG data elucidate how neural signals propagate and inform on nerve health and function.
- `Extracellular Electrophysiology`: Recordings of neuronal signals from outside the cells. This method allows for simultaneous long-term monitoring of multiple neurons, providing insight into network dynamics and population coding.
- `Intracellular Electrophysiology`: High-precision recordings of a single cell’s electrical activity using a microelectrode inserted into the neuron. Intracellular data reveal subthreshold events, synaptic inputs, and intrinsic cellular properties.

### Optical Imaging
- `Fiber Photometry`: A calcium imaging technique capturing population-level neural activity changes via light signals. It is especially useful for studying the dynamics of specific cell types within a brain circuit.
- `Miniscope Microscopy`: Small, head-mounted microscopes that let researchers visualize large populations of neurons in freely moving animals, bridging the gap between naturalistic behavior and underlying neural activity.
- `Confocal Microscopy`: An optical imaging technique that uses a pinhole to achieve high-resolution, high-contrast images and 3D reconstructions. Commonly applied to study cellular structures and brain tissue morphology.
- `Light Field Microscopy`: A scanning-free, 3D imaging method capturing entire light fields, enabling rapid volumetric imaging at micron-scale resolution. Ideal for reconstructing complex neural circuits in three dimensions.
- `Single-Photon Microscopy`: A fluorescence imaging method utilizing single-photon excitation for detailed observation of cellular and subcellular structures in living tissue.
- `Two-Photon Microscopy`: A fluorescence imaging technique using near-infrared light for deeper imaging in scattering tissue. It is well-suited for probing functional neuronal activity in intact brain tissue.
- `Three-Photon Microscopy`: A nonlinear optical method employing three-photon excitation to achieve deeper penetration and higher spatial resolution, allowing imaging of neuronal activity in challenging tissue environments.

### Magnetic and Functional Imaging
- `Magnetic Resonance Imaging (MRI)`: Uses magnetic fields and radio waves to generate detailed anatomical images of the brain and other organs, without ionizing radiation. MRI is a cornerstone of structural brain imaging.
- `Functional Magnetic Resonance Imaging (fMRI)`: Measures brain activity indirectly through changes in blood flow. fMRI helps map functional networks, cognitive states, and sensory-motor processing.
- `Magnetoencephalography (MEG)`: Detects the magnetic fields produced by neuronal activity. With excellent temporal resolution, MEG provides insights into real-time brain dynamics and functional connectivity.

### Tomography and Ultrasound
- `Computed Tomography (CT)`: An X-ray-based imaging modality that produces cross-sectional images of internal brain structures, aiding in the identification of pathologies and structural abnormalities.
- `Positron Emission Tomography (PET)`: Uses radioactive tracers to visualize metabolic processes and physiological activities. PET is invaluable for studying neurotransmitter systems, blood flow, and metabolic states in the brain.
- `Single-Photon Emission Computed Tomography (SPECT)`: A nuclear imaging technique capturing 3D information on functional processes. SPECT data are often used alongside other imaging modalities for comprehensive analysis.
- `Functional Ultrasound Imaging (fUS)`: Measures changes in blood flow or metabolism related to neural activity. As a non-invasive method with high spatial and temporal resolution, fUS is emerging as a versatile neuroimaging tool.

### General and Time-Series Data
- `General Time-Series`: Any continuous, time-dependent data—such as neural firing rates, physiological signals, or behavioral readouts—used to analyze temporal patterns, rhythms, and dynamics in neural and physiological systems.

A detailed list of the type-specific fields can be found on the [Data acquisition types page]({{"datamodel/schemas/dataacquisition/"|absolute_url}}).


## Permissions

Data acquisition inherits permissions through its associated session.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## Data acquisition API access

The API allows for programmable access to data acquisition. Learn more about the data acquisition fields and data structure on the [data acquisition API page]({{"api/modules/dataacquisition/"|absolute_url}}).
