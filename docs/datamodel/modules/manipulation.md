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

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A manipulation describes one controlled stimulus or perturbation delivered during a session: electrical, magnetic, optogenetic, thermal, ultrasound, chemical or pharmacological, or sensory stimulation. Each manipulation is one delivered stimulus. Use separate entries when the stimuli have different types or their own delivery parameters.

A manipulation is applied during a session to perturb the target. A [procedure]({{"datamodel/modules/procedure/"|absolute_url}}) is the action that established the access route, and a [data acquisition]({{"datamodel/modules/dataacquisition/"|absolute_url}}) is the signal recorded. An optogenetic light pulse is a manipulation; the fiber implant that made it possible is a procedure; the photometry trace recorded alongside it is a data acquisition. The stimulus reaches the target through [experimental interfaces]({{"datamodel/modules/experimentalinterface/"|absolute_url}}), and the installing procedure is reached through the interface. Agents delivered (drugs, solutions) belong to the material rows of the procedure or interface that installed them, never directly to the manipulation.

{% include datamodel_embed.html model="modules.manipulation" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Type of manipulation`` | Type of manipulation (**required**). Selected from predefined types. Example: "Optogenetic stimulation". *See options below* |
| ``Session`` | Session of the manipulation (**required**). Must reference an existing [session]({{"datamodel/stem/session/"|absolute_url}}). |
| ``Experimental interfaces`` | The interfaces through which the stimulus was delivered, such as an optic fiber, cannula or stimulating electrode (**required**; one or more). Limited to interfaces installed on the session's subjects or specimen sets. The selection order is stored. |
| ``Setup`` | Form-only filter for the equipment field. Not stored. |
| ``Equipment`` | Instruments that generated or controlled the stimulus, such as a laser, stimulator or olfactometer. Must reference existing [equipment]({{"datamodel/modules/equipment/"|absolute_url}}). |
| ``Data`` | Type-specific parameters. Every manipulation type is a table: each row is one stimulation or perturbation epoch with its own parameter set, so a record is a sequence of repeated epochs. Numeric parameters carry their own unit. See the [Manipulation types schema]({{"datamodel/schemas/manipulation/"|absolute_url}}). |
| ``Order`` | Where this manipulation appears among the session's entries. Does not imply a start time. |
| ``Notes`` | Exceptional context, deviations or delivery problems (string; maximum length: 500 characters). |

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

Manipulations inherit permissions through the projects of the session associated with them. The form limits sessions, interfaces and equipment to entries you are permitted to use.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to manipulations. Interfaces are supplied as `interfaces`, an ordered list of interface ids. Learn more about the manipulations' fields and data structure on the [Manipulation API page]({{"api/modules/manipulation/"|absolute_url}}).
