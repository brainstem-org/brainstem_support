---
layout: default
title: Equipment
parent: Setups
grand_parent: Personal attributes
nav_order: 1
---

# Equipment model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

Equipment is one named, reusable instrument installed in a [setup]({{"datamodel/personal_attributes/setup/"|absolute_url}}): an amplifier, a camera, a laser, a stereotaxic frame, a fume hood. Each equipment record is one physical item in one setup, so procedures, data acquisitions, manipulations and experimental interfaces can point at the actual apparatus used rather than at a generic catalog product. The types of equipment currently supported by BrainSTEM are listed below.

Equipment is the durable apparatus around an experiment. [Hardware devices]({{"datamodel/resources/hardwaredevice/"|absolute_url}}) and [consumables]({{"datamodel/resources/consumable/"|absolute_url}}) are the catalog identities a piece of equipment can point at. An [experimental interface]({{"datamodel/modules/experimentalinterface/"|absolute_url}}) is the probe, fiber or window that contacts the subject or specimen. A [consumable stock]({{"datamodel/modules/consumablestock/"|absolute_url}}) is a lot that gets used up or belongs to one subject.

{% include datamodel_embed.html model="modules.equipment" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Equipment name`` | Local name of the equipment (**required**; string; maximum length: 100 characters). Example: "Ephys amplifier" or "Ceiling mounted camera" |
| ``Type of equipment`` | Type of equipment (**required**). Selected from predefined types. The type classifies the item for search and comparison; the registry is shared with hardware devices. *See options below* |
| ``Setup`` | The setup the equipment is installed in (**required**). Must reference an existing [setup]({{"datamodel/personal_attributes/setup/"|absolute_url}}) where you are at least a Contributor. The setup decides who may see and edit the equipment; moving an item to another setup moves its access with it. |
| ``Date and time`` | When this configuration or placement applies from. Useful when a rig is reconfigured. |
| ``Consumable supplier`` | Form-only filter for the consumable field. Not stored. |
| ``Consumable`` | The catalog [consumable]({{"datamodel/resources/consumable/"|absolute_url}}) this item corresponds to, when the item is a catalog product rather than a device. |
| ``Hardware device supplier`` | Form-only filter for the hardware device field. Not stored. |
| ``Hardware device`` | The catalog [hardware device]({{"datamodel/resources/hardwaredevice/"|absolute_url}}) identity, so model and manufacturer details are not repeated on every equipment entry. Only approved catalog entries are offered. An equipment entry links either a consumable or a hardware device. |
| ``Coordinate system`` | How the item's position is expressed (**required**; default: External XYZ Coordinates with Euler Orientation). The same systems as for procedures are offered. For apparatus fixed in the rig, an External XYZ system is normally right; the anatomical systems only make sense for equipment positioned relative to a landmark on the animal. *See options below* |
| ``Coordinates`` | The item's position and orientation in the selected system. Leave empty when the position is not fixed or not meaningful. |
| ``Notes`` | Model and serial number, settings, firmware, calibration or known quirks (string; maximum length: 500 characters). |
| ``Type specific fields`` | Structured details where the equipment type's schema defines them. See the [Equipment types schema]({{"datamodel/schemas/equipment/"|absolute_url}}). |

## How it fits together

[![A setup is built as a setup type and holds its equipment, and each piece of equipment can name its model in the shared catalog. Procedures, specimen procedures, experimental interfaces, data acquisitions and manipulations name the equipment they used; a behavior names the whole setup.]({{site.baseurl}}/assets/images/diagrams/setup-hub-equipment.svg)]({{site.baseurl}}/assets/images/diagrams/setup-hub-equipment.svg)
*Equipment is installed in one [setup]({{"datamodel/personal_attributes/setup/"|absolute_url}}) and can name its model in the shared catalog. Procedures, specimen procedures and experimental interfaces on a subject or specimen set, and data acquisitions and manipulations in a session, name the equipment they used; their templates can prefill it. A behavior names the whole setup instead. This page describes equipment, drawn solid.*

## Types of equipment

These are the available type options for equipment:

See the schema for field details: [Equipment types]({{"datamodel/schemas/equipment/"|absolute_url}}). The same type list is used for [hardware devices]({{"datamodel/resources/hardwaredevice/"|absolute_url}}).

### Data acquisition

`Amplifier`: Amplifies bioelectrical signals (neural or muscular) for recording and analysis in electrophysiology.

`Camera`: Captures video or still images to monitor behavior, movement, and experimental context.

`Data acquisition system`: Acquires, synchronizes, and stores signals from multiple sources in real time.

`Electroencephalography system (EEG)`: Records scalp electrical activity to study large‑scale brain dynamics and function.

`Electromyography machine`: Measures muscle electrical activity for motor control and neuromuscular studies.

`Ephys rig`: Integrated setup for extra‑/intracellular electrophysiological recordings of neural activity.

`Fiber photometry system`: Measures population fluorescence (e.g., calcium or neuromodulators) in vivo via fiber‑coupled optics.

`Force plate`: Measures ground reaction forces for locomotion, biomechanics, and motor control.

`Humidity sensor`: Monitors ambient humidity in experimental environments.

`Light sensor`: Measures light intensity for stimulus calibration and environmental monitoring.

`Magnetic resonance imaging (MRI) system`: Generates anatomical or functional images using magnetic fields and radiofrequency pulses.

`Magnetoencephalography (MEG) system`: Detects magnetic fields generated by neural activity with high temporal resolution.

`Magnetometer`: Measures magnetic fields for stimulation alignment, motion tracking, or environmental monitoring.

`Microphone`: Records audio (vocalizations, stimuli, ambient) for auditory and behavioral studies.

`Miniscope`: Head‑mounted fluorescence microscope for imaging neural activity in freely moving animals.

`Motion tracking system`: Tracks 2D/3D movement and pose in real time.

`Ophys rig`: Optical physiology setup combining imaging with physiological readouts.

`Optical Coherence Tomography (OCT)`: Micrometer‑scale, cross‑sectional imaging of tissue using low‑coherence interferometry.

`Oscilloscope`: Displays and analyzes electrical waveforms in real time for diagnostics and monitoring.

`Photodetector`: Detects and quantifies light intensity in optical experiments.

`Signal processing unit`: Conditions, filters, and digitizes signals prior to analysis.

`Single-photon emission computed tomography (SPECT)`: Gamma‑ray functional imaging for metabolic and physiological activity.

`Temperature sensor`: Monitors temperature of environments, apparatus, or subjects.

`Ultrasound imaging system`: Produces internal images using high‑frequency sound for structural and functional studies.

### Behavioral and stimulation tools

`Behavior rig`: Controlled environment with sensors and actuators for behavioral experiments.

`Iontophoresis stimulator`: Delivers charged molecules into tissue via controlled electrical current.

`Laser`: Provides focused light for stimulation, ablation, or imaging.

`LED Driver`: Controls LEDs for visual stimuli or optogenetic protocols with precise intensity and timing.

`Light emitter`: Delivers controlled light stimuli to subjects or preparations.

`Running Wheel`: Measures locomotion and provides voluntary exercise.

`Speaker`: Delivers auditory stimuli (tones, noise, vocalizations) for research and conditioning.

`Stimulation device`: Applies controlled electrical, magnetic, or mechanical stimulation to tissue.

`Treadmill`: Enables controlled locomotion, often combined with VR or tracking systems.

### Environmental controllers

`Anti-vibration table`: Isolates setups from external vibrations for precision experiments.

`Floating air platform`: Actively isolates against vibrations for highly sensitive measurements.

`Humidity controller`: Regulates humidity to maintain stable environmental conditions.

`Noise isolation chamber`: Reduces acoustic noise to protect sensitive recordings and experiments.

`Thermal controller`: Regulates temperature of environments, equipment, or subjects.

### Surgical equipment

`Anesthesia system`: Delivers and monitors anesthesia safely during procedures.

`Injection system`: Dispenses precise volumes into tissues or cells.

`Micromanipulator`: Precisely positions tools or electrodes during surgery and recordings.

`Stereotaxic frame`: Immobilizes subjects and enables atlas‑based, precise targeting of brain regions.

`Surgical power tool`: Powered instruments (e.g., drills) for cranial procedures and implantations.

`Perfusion system`: Provides oxygenated or conditioned solutions to maintain tissue viability.

### Miscellaneous

`Biosafety cabinet`: Provides a sterile, contained workspace for handling biological materials.

`Computer`: Runs acquisition, control, and analysis software within the setup.

`Electronic component`: Discrete parts or modules (e.g., resistors, sensors, drivers) for custom hardware and integration.

`Fume hood`: Vented enclosure for safe handling of volatile chemicals.

`Glass micropipette puller`: Fabricates fine‑tipped glass micropipettes for injections or recordings.

`Microcontroller (e.g. Arduino)`: Embedded controller for stimulus delivery, device control, or data acquisition (e.g., Arduino).

`Microscope`: Optical instrument for high‑resolution imaging (e.g., brightfield, fluorescence, confocal, two‑photon).

`Monitor`: Displays visual stimuli to subjects or experimental data to researchers.

`Single-board computer (e.g. Raspberry Pi)`: Compact computer for control, automation, and edge processing (e.g., Raspberry Pi).

### Legacy types

`Drug Delivery System` and `Pressure Sensor` are no longer selectable for new records. Existing records keep them.

## Coordinate systems

Equipment is offered the same coordinate systems as a procedure: External (XYZ with Euler or quaternion orientation), Stereotaxic (Bregma- or Lambda-based, absolute or surface with depth), Landmark-referenced, Spinal, and the standardized reference spaces (Allen Mouse CCFv3, Waxholm rat, MNI152 human, NIMH macaque, mapzebrain, JRC2018 fly, Brain/MINDS marmoset). Each system and its fields are described on the [Coordinate systems page]({{"datamodel/schemas/coordinates/"|absolute_url}}).

## Permissions

Equipment inherits permissions from its setup. Contributors of the setup can add, edit and remove its equipment and select it on procedures, data acquisitions, manipulations and experimental interfaces. This is a group boundary rather than a project one: colleagues on a project do not get access to your rig unless the setup is shared with them.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to equipment. Position data uses `coordinates_system` and `coordinates_details`. Learn more about the equipment fields and data structure on the [Equipment API page]({{"api/modules/equipment/"|absolute_url}}).
