---
layout: default
title: Equipments
parent: Modules
grand_parent: Data model
nav_order: 3
---

# Equipments model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Equipments refer to the setup and utilization of various devices and sensors designed to monitor, record, or manipulate environmental variables or subject responses. These equipment are critical for creating controlled experimental conditions, collecting data, and delivering stimuli. Each equipment type has specific applications and functions within setups. While equipment types share relationships, fields are tailored to the various equipment types. The types of equipment currently supported by BrainSTEM are listed below.

## Fields

| Field | Description |
|:------|:------------|
| `Type` | Type of equipment (**required**). Selected from predefined types. Example: "Video camera", "Microphone". *See options below* |
| `Setup` | The setup the equipment is installed in (**required**). Must reference an existing [setups]({{"datamodel/personal_attributes/setup/"|absolute_url}}). Example: "Behavior room A setup" |
| `Notes` | Notes about the equipment (string). Example: "Camera positioned at 45-degree angle" |
| `Date and time` | Date and time the equipment was performed. Example: "2024-03-22 09:00:00" |
| `Consumable` | Consumable used for the equipment. Example: "HD webcam model XYZ" |
| `Hardware device` | Hardware device used to perform the equipment. Example: "Recording computer #2" |
| `Coordinates system` | Coordinate system (**required**). Selected from predefined systems. Example: "External X-Y-Z Absolute". *See options below* |
| `Type details` | Type-specific fields. Fields vary by equipment type. Example: For camera - resolution, frame rate. *See options below* |

## Types of equipment

These are the available *Type* options for equipment:

### Data Acquisition
- `Amplifier`: Amplifies electrical signals from biological sources such as neurons or muscles, making them suitable for processing and analysis. Essential for electrophysiological studies to ensure signal clarity.
- `Camera`: Captures video or still images to monitor subject behavior, movement, or environmental changes, supporting behavioral analysis and motion tracking.
- `Data Acquisition System`: Integrates hardware and software to collect, process, and store data from multiple sources in real-time.
- `Electroencephalography System (EEG)`: Records electrical activity from the scalp to study brain function and neural dynamics in humans or animals.
- `Electromyography Machine (EMG)`: Measures muscle electrical activity, aiding in studies of motor control and neuromuscular disorders.
- `Ephys Rig`: A comprehensive setup for electrophysiological recordings, including extracellular and intracellular methods for studying neural activity.
- `Fiber Photometry System`: Monitors neural activity by measuring calcium or neurotransmitter dynamics in vivo using fluorescence-based techniques.
- `Force Plate`: Measures forces exerted by subjects, commonly used in motor control, biomechanics, and locomotion studies.
- `Humidity Sensor`: Monitors humidity levels in experimental setups to ensure stable environmental conditions.
- `Light Sensor`: Detects and measures light intensity, often used in studies involving photosensitivity or optogenetics.
- `Magnetic Resonance Imaging System (MRI)`: Produces detailed anatomical and functional images of the brain using magnetic fields.
- `Magnetoencephalography System (MEG)`: Detects magnetic fields produced by neural activity, providing high temporal resolution for brain studies.
- `Magnetometer`: Measures magnetic fields, often used in studies involving brain stimulation or motion tracking.
- `Microphone`: Records audio data, including vocalizations or environmental sounds, supporting auditory and behavioral studies.
- `Miniscope`: Miniature fluorescence microscopes designed for imaging neural activity in freely moving animals.
- `Motion Tracking System`: Tracks subject movement in real-time for behavioral or neural experiments.
- `Ophys Rig`: Combines optical imaging with physiological recordings for simultaneous monitoring of neural activity.
- `Optical Coherence Tomography (OCT)`: Uses light waves to capture detailed cross-sectional images of tissues, such as brain slices.
- `Oscilloscope`: Visualizes electrical signals in real-time, aiding in diagnostics and monitoring.
- `Photodetector`: Measures light intensity in fluorescence or optical experiments.
- `Signal Processing Unit`: Processes and filters raw data from recording devices for analysis.
- `Single Photon Emission Computed Tomography (SPECT)`: Functional imaging method using gamma rays for studying metabolic activity.
- `Temperature Sensor`: Monitors thermal conditions in experimental setups to ensure stability and accuracy.
- `Ultrasound Imaging System`: Captures high-resolution internal images using sound waves, useful for structural studies.

### Behavioral and Stimulation Tools
- `Behavior Rig`: Designed for studying animal behavior under controlled conditions, often equipped with cameras, sensors, and stimulus delivery systems.
- `Iontophoresis Stimulator`: Applies electrical currents to deliver charged molecules to tissues with high precision.
- `Laser`: Provides focused light for stimulation, imaging, or tissue ablation in experimental setups.
- `LED Driver`: Controls light-emitting diodes (LEDs) for visual experiments or optogenetics, enabling precise light modulation.
- `Light Emitter`: Provides controlled light stimuli, often used in optogenetics or photosensitivity studies.
- `Running Wheel`: Tracks locomotor activity or provides exercise for experimental subjects.
- `Speaker`: Delivers auditory stimuli, such as tones or sounds, for auditory research or conditioning experiments.
- `Stimulation Device`: Delivers controlled electrical, magnetic, or mechanical stimulation to tissues.
- `Treadmill`: Used for locomotion studies, often combined with virtual reality setups for precise tracking.

### Environmental Controllers
- `Anti-Vibration Table`: Provides a stable, vibration-free platform for precision experiments, such as microscopy or electrophysiology setups.
- `Floating Air Platform`: Minimizes external vibrations for highly sensitive experiments, ensuring precise and reliable measurements.
- `Humidity Controller`: Monitors and adjusts humidity levels in experimental setups, critical for environmental studies and tissue preservation.
- `Noise Isolation Chamber`: Minimizes external noise, ensuring controlled experimental conditions for sensitive studies.
- `Thermal Controller`: Regulates temperature in experimental environments or for subject maintenance, ensuring optimal conditions.

### Surgical Equipments
- `Anesthesia System`: Ensures safe and controlled administration of anesthesia to experimental subjects during procedures.
- `Injection System`: Delivers precise volumes of substances into biological tissues or cells.
- `Micromanipulator`: Precisely positions electrodes or devices during surgeries or neural recordings, ensuring accurate placement.
- `Microscope`: Provides high-resolution imaging of biological samples, with specialized models for fluorescence, confocal, or two-photon imaging.
- `Stereotaxic Frame`: Stabilizes subjects during surgeries or recordings, enabling precise targeting of brain regions.
- `Surgical Power Tool`: Includes drills or other tools used for cranial surgeries or electrode implantations.
- `Perfusion System`: Maintains tissue viability by providing oxygenated solutions during experiments.

### Miscellaneous
- `Biosafety Cabinet`: Creates a sterile environment for handling biological materials, ensuring the safety of users and samples.
- `Computer`: Runs software for data collection, analysis, and control of experimental equipment. Includes desktop workstations or high-performance servers configured for specialized tasks.
- `Electronic Component`: Fundamental building blocks of electronic systems, including resistors, capacitors, transistors, and modules. Used for custom hardware solutions in signal processing, device control, or stimulation systems.
- `Fume Hood`: Provides a controlled environment to handle volatile chemicals safely, protecting users from hazardous fumes.
- `Glass Micropipette Puller`: Creates fine-tipped glass micropipettes for use in microinjections or electrophysiological recordings.
- `Microcontroller`: Compact devices designed to control specific operations, such as managing stimuli delivery or data acquisition. Popular examples include Arduino, used for rapid prototyping and custom experiment control systems.
- `Monitor`: Displays visual stimuli for subjects or experimental data for researchers.
- `Single-Board Computer`: Lightweight, versatile computers like Raspberry Pi that run custom software for experimental control, automation, and localized data processing.

A detailed list of the accepted schemas for the `details` field, related to each `type`, can be found in the [Equipments schemas page]({{"/api/schemas/equipment/"|absolute_url}}).


## Coordinate system options

Available Coordinate system options for equipment:

| Type | Description |
|:-----|:------------|
| External X-Y-Z Absolute | Absolute external coordinates. This can be used to describe, e.g., a camera's position in a room |

A detailed list of the fields in Coordinate system can be found on the [Coordinate systems page]({{"datamodel/schemas/coordinates/"|absolute_url}}).

## Permissions

Equipments inherit permissions through the setup associated with them.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## Equipments API access

The API allows for programmable access to equipment. Learn more about the equipment' fields and data structure on the [Equipments API page]({{"api/modules/equipment/"|absolute_url}}).
