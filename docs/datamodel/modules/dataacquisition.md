---
layout: default
title: Data acquisition
parent: Sessions
grand_parent: Data model
nav_order: 2
---

# Data acquisition model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A data acquisition describes one recording stream captured during a session: an electrophysiology recording, a microscopy or tomography acquisition, audio, or tracking. Each data acquisition is one stream. Use separate entries when streams have different acquisition methods or their own file, channel or timing details, even when they were recorded simultaneously. Fields are tailored to the data acquisition type.

The signal is linked to what produced it through [experimental interfaces]({{"datamodel/modules/experimentalinterface/"|absolute_url}}): the probe, fiber, lens, sensor or other target-facing interface the signal came through. The procedure that installed an interface is reached through the interface itself, so a data acquisition no longer links to procedures directly. [Equipment]({{"datamodel/modules/equipment/"|absolute_url}}) identifies the reusable instruments around it: amplifiers, cameras, microscopes, acquisition systems.

[![A session and its parts: the behavior (what the subjects were doing), data acquisitions (what was recorded) and manipulations (what was delivered), each placed in an epoch of the session (when); behaviors run an assay on a setup, and acquisitions and manipulations pass through experimental interfaces.]({{site.baseurl}}/assets/images/diagrams/session-parts-dataacquisition.svg)]({{site.baseurl}}/assets/images/diagrams/session-parts-dataacquisition.svg)
*A session and its parts. Data acquisitions, drawn solid, say what was recorded, each through the experimental interfaces the signal came through; the behavior says what the subjects were doing, manipulations what was delivered, and epochs when.*

{% include datamodel_embed.html model="modules.dataacquisition" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Type of data acquisition`` | Type of data acquisition (**required**). Selected from predefined types. Example: "Extracellular Electrophysiology". *See options below* |
| ``Session`` | Session of the data acquisition (**required**). Must reference an existing [session]({{"datamodel/stem/session/"|absolute_url}}). The session's subjects or specimen sets decide which interfaces are offered. |
| ``Experimental interfaces`` | The interfaces the signal was acquired through (**required**; one or more). The choices are the interfaces installed on the session's subjects or specimen sets, limited to interface types that fit the acquisition type. The order you select them in is stored; list them in the order of your channel or stream layout. |
| ``Setup`` | Form-only filter for the equipment field. Not stored. |
| ``Equipment`` | Equipment used to acquire the data. Must reference existing [equipment]({{"datamodel/modules/equipment/"|absolute_url}}) in setups where you are at least a Contributor. Example: "Intan RHD2000" |
| ``Data`` | Type-specific fields covering the file, format and acquisition parameters. See the [Data acquisition types schema]({{"datamodel/schemas/dataacquisition/"|absolute_url}}). For extracellular recordings this includes electrode groups and channel tags for the probe layout. |
| ``Order`` | Where this acquisition appears among the session's entries. Does not imply a start time. |
| ``Image`` | A representative preview, such as a field of view or an example trace. Illustrative only; it is not the dataset. |
| ``Notes`` | Deviations, quality problems or other context (string; maximum length: 500 characters). |

## Types of Data acquisition

These are the available type options for Data acquisition:

See the schema for field details: [Data acquisition types]({{"datamodel/schemas/dataacquisition/"|absolute_url}}).

### Audio and Behavior Tracking

`Audio`: Recordings of sounds, vocalizations, or auditory stimuli used to study auditory processing, communication, and sound–behavior relationships.

`Behavioral Tracking`: Monitoring and quantifying movements, actions, and task responses to link behavior with neural activity, learning, memory, and decision‑making.

`Video Tracking`: Visual monitoring and analysis of movements and behaviors using video systems; supports pose estimation, activity scoring, and context annotation.

### Electrophysiology

`Electroencephalography (EEG)`: Non‑invasive recordings of electrical brain activity from scalp electrodes to study large‑scale dynamics, sleep, sensory processing, and cognition.

`Electroneurogram (ENG)`: Direct recordings of peripheral or central nerve activity to characterize signal propagation, nerve function, and health.

`Extracellular Electrophysiology`: Recordings of neuronal activity from outside cells for single‑unit and population monitoring, enabling network dynamics and population coding analyses.

`Intracellular Electrophysiology`: High‑precision measurements from electrodes inside cells to resolve subthreshold events, synaptic inputs, and intrinsic cellular properties.

### Optical Imaging

`Fiber Photometry`: Population‑level calcium or neuromodulator signals measured via fiber‑coupled fluorescence for circuit‑specific activity dynamics.

`Miniscope Microscopy`: Head‑mounted fluorescence microscopy to image large neuronal populations in freely moving animals, linking naturalistic behavior to neural activity.

`Confocal Microscopy`: Pinhole‑based optical sectioning for high‑resolution, high‑contrast images and 3D reconstructions of cells and tissue morphology.

`Light Field Microscopy`: Scanning‑free 3D imaging that captures the full light field for rapid volumetric imaging and circuit‑level reconstructions.

`Single-Photon Microscopy`: Fluorescence imaging with single‑photon excitation for detailed observation of cellular and subcellular structures in living tissue.

`Two-Photon Microscopy`: Near‑infrared, two‑photon excitation for deeper imaging in scattering tissue; well‑suited to functional neuronal activity in intact brain.

`Three-Photon Microscopy`: Nonlinear three‑photon excitation to achieve deeper penetration and high spatial resolution in challenging tissue environments.

### Magnetic and Functional Imaging

`Magnetic Resonance Imaging (MRI)`: Magnetic fields and radio waves generate detailed anatomical images without ionizing radiation; cornerstone for structural brain imaging.

`Functional Magnetic Resonance Imaging (fMRI)`: Indirect measures of brain activity via blood‑flow changes to map functional networks, cognitive states, and sensorimotor processing.

`Magnetoencephalography (MEG)`: Detection of magnetic fields from neuronal activity with high temporal resolution to study real‑time dynamics and functional connectivity.

### Tomography and Ultrasound

`Computed Tomography (CT)`: X‑ray‑based cross‑sectional imaging of internal structures for identifying pathologies and structural abnormalities.

`Optical Coherence Tomography (OCT)`: Low‑coherence interferometric imaging for micrometer‑resolution cross‑sections of biological tissue.

`Positron Emission Tomography (PET)`: Radioactive tracers visualize metabolic and physiological processes; widely used for neurotransmitter systems, blood flow, and metabolism.

`Single-Photon Emission Computed Tomography (SPECT)`: Nuclear imaging that captures 3D functional information, often combined with other modalities for comprehensive analysis.

`Functional Ultrasound Imaging (fUS)`: Non‑invasive ultrasound measurement of blood‑flow or metabolic changes related to neural activity, with high spatial and temporal resolution.

### General and Time-Series Data

`General time-series`: Continuous time‑dependent data (e.g., neural firing, physiological signals, behavioral readouts) for analyzing temporal patterns and dynamics.



## Permissions

Data acquisition inherits permissions through the projects of its associated session. The form limits sessions, interfaces and equipment to entries you are permitted to use.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to data acquisition. Interfaces are supplied as `interfaces`, an ordered list of interface ids. Learn more about the data acquisition fields and data structure on the [data acquisition API page]({{"api/modules/dataacquisition/"|absolute_url}}).
