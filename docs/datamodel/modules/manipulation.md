---
layout: default
title: Manipulations
parent: Sessions
grand_parent: Data model
nav_order: 3
---

# Manipulation model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

The manipulations model describes temporal manipulations performed in a session. Manipulations are ways to perturb natural brain dynamics. The types of manipulations currently supported by BrainSTEM are listed below. A Manipulation is described by the fields in the next section.

## Fields

| Field | Description |
|:------|:------------|
| ``Type of manipulation`` | Type of manipulation (**required**). Selected from predefined types. Example: "Optogenetic stimulation". *See options below* |
| ``Session`` | Session of the manipulation (**required**). Must reference an existing [session]({{"datamodel/stem/session/"|absolute_url}}). Example: "Optogenetic stimulation session #2" |
| ``Subject procedures`` | Related subject procedures (**required**). Must reference existing [procedures]({{"datamodel/modules/procedure/"|absolute_url}}). Example: "Optic fiber implant #B789" |
| ``Setup`` | Setup filter for equipment. Used to filter available equipment by setup. |
| ``Equipment`` | Equipment used for the manipulation. Must reference existing [equipment]({{"datamodel/modules/equipment/"|absolute_url}}). Example: "LED driver #1" |
| ``Notes`` | Notes about the manipulation (string). Example: "20Hz stimulation protocol completed successfully" |
| ``Type specific fields`` | Custom fields based on manipulation type in JSON format. See [Manipulation types schema]({{"datamodel/schemas/manipulation/"|absolute_url}}) for type-specific fields |

## Types of manipulations

These are the available type options for manipulations:

See the schema for field details: [Manipulation types]({{"datamodel/schemas/manipulation/"|absolute_url}}).

### Electrical and Magnetic Stimulation

`Deep brain stimulation (DBS)`: Implanted electrodes deliver electrical pulses to targeted brain areas to modulate neural activity.

`Electrical stimulation`: Application of electrical currents to neural tissue (invasive or non‑invasive) to activate or inhibit activity.

`Electromagnetic field stimulation`: Modulation of neural activity using magnetic or electric fields in a non‑invasive manner.

`Transcranial Electrical Stimulation`: Scalp‑applied electrical currents (e.g., tDCS/tACS) to modulate brain activity.

`Transcranial Magnetic Stimulation (TMS)`: Magnetic fields induce cortical currents non‑invasively to modulate neural activity.

### Optical, Thermal and Ultrasound Stimulation

`Optogenetic stimulation`: Light control of genetically targeted neurons to activate or inhibit specific populations with high temporal precision.

`Thermal perturbation`: Heating or cooling neural tissue to probe temperature effects on activity and function.

`Ultrasound stimulation`: Non‑invasive modulation of neural activity using focused high‑frequency sound.

### Chemical and Pharmacological Perturbations

`Liquid perturbation`: Introduction of liquids (e.g., drugs/solutions) to alter brain environment or activity.

`Microperfusion`: Localized delivery of substances to targeted brain regions via fine cannula.

`Pharmacological injection`: Direct drug delivery into the body or brain tissue to study effects on activity and behavior.

`Pharmacological superfusion`: Controlled drug application onto neural tissues or cells, often via perfusion systems.

`Pharmacological inhalation`: Administration of vaporized drugs for pulmonary absorption and CNS effects.

### Sensory Stimulation

`Auditory stimulation`: Presentation of sound stimuli to study hearing, perception, cognition, and therapeutic effects.

`Multisensory stimulation`: Concurrent stimuli from multiple modalities to study sensory integration.

`Odor stimulation`: Controlled olfactory stimuli to probe sensory processing, neural activity, and behavior.

`Tactile stimulation`: Touch/pressure stimuli to study somatosensory processing and responses.

`Visual stimulation`: Visual stimuli to study visual processing from perception to complex cognition.






## Permissions

Manipulations inherit permissions through the session associated with them.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to manipulations. Learn more about the manipulations' fields and data structure on the [Manipulation API page]({{"api/modules/manipulation/"|absolute_url}}).
