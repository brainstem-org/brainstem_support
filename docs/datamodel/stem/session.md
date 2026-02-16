---
layout: default
title: Sessions
parent: Data model
nav_order: 3
has_toc: false
---

# Session model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction 

Sessions are modular structures that provide flexible and standardized descriptions of various aspects of experiments. Sessions have several direct fields but are primarily described by the following modules:

1. [__Behaviors__]({{"datamodel/modules/behavior"|absolute_url}}): Description of the animal subject(s) behavior during the session collection. A behavior is described by two personal attributes: the setup and the behavioral paradigm.
2. [__Data acquisition__]({{"datamodel/modules/dataacquisition"|absolute_url}}): Description of the data acquisition files. This module is highly flexible and can describe many types of experimental data, such as Extracellular and Intracellular Electrophysiology, 2-photon microscopy, Miniscope, Audio Recordings, and Behavioral Video Recordings. Details are tailored to each experiment type.
3. [__Manipulations__]({{"datamodel/modules/manipulation"|absolute_url}}): Description of any manipulations performed during an experiment. This crucial module documents alterations to the physiological conditions of a recording. It can describe various types of manipulations, such as Optogenetic Stimulation, Micro Perfusion, Pharmacological Injection, Thermal Perturbation, Transcranial Electrical Stimulation, and Ultrasound Stimulation. A manipulation is described by a protocol, typically consisting of the manipulation profile, power, duration, duty cycle, and number of repetitions.
4. __Epochs__: Temporal aspects of a session. An epoch is characterized by a name, start and end times relative to the session's start. Other modules (Data acquisition, Manipulations, and Behavior) can be linked to epochs, allowing for temporal segmentation of a session.

## Session fields

| Field | Description |
|:------|:------------|
| `Session name` | Name of the session (**required**; string; max length: 100 characters; must be unique across BrainSTEM). Example: "Memory_Task_Session1", "PV_Recording_20240313" |
| `Projects` | Projects the session belongs to (**required**). Learn more about project inheritance [here]({{"datamodel/stem/project/"|absolute_url}}). Example: "Hippocampal Memory Project" |
| `Description` | A text description of the session. Pictures can be uploaded and inserted through rich text formatting. Example: "Recording session during novel object recognition task..." |
| `Date and time onset` | Date and time of the session onset (YYYY-MM-DD format, e.g., "2023-03-22 14:30:00"). Can be left empty |
| `Tags` | Tags for the session. Great for organizational purposes, quick labeling and filtering. Tags are shared across all users. Example: "behavior", "recording", "morning-session" |
| `Data storage` | Describes where the data is stored. Example: "Lab Server", "External Drive 1" |
| `Session name in data storage` | Custom name for the session used in local data storage (string; max length: 200; optional). Example: "ses01_mem_2024" |
| `Additional fields` | Allows you to add extra fields to the session. Values can be strings or numeric. Saved as key-value pairs. Example: {"Room": "B115", "Temperature": "22C"} |
| `Public repositories` | If this session has been shared in a public repository, link it here. Example: "DANDI:123456" |

### Behaviors data fields
Please see the dedicated page describing the [Behaviors data model]({{"datamodel/modules/behavior"|absolute_url}}).

### Data acquisition data fields
Please see the dedicated page describing the [Data acquisition data model]({{"datamodel/modules/dataacquisition"|absolute_url}}).

{: .note }
> Each data acquisition module represents one recording file. Different setups or file separations require separate data acquisition modules.

### Manipulations data fields
Please see the dedicated page describing the [Manipulations data model]({{"datamodel/modules/manipulation"|absolute_url}}).

### Epoch fields

| Field | Description |
|:------|:------------|
| `Name` | Name of the epoch (**required**; string; max length: 100 characters). Example: "Baseline", "Stimulus_Period" |
| `Start` | Start time of the epoch, relative to the session onset. Example: "0:00:00" |
| `End` | End time of the epoch, relative to the session onset. Example: "0:05:00" |
| `Behavior` | Behaviors associated with the epoch. Example: "Open field exploration" |
| `Data acquisition` | Data acquisition associated with the epoch. Each data acquisition can only be assigned to one epoch. Example: "Calcium imaging" |
| `Manipulation` | Manipulations associated with the epoch. Example: "Optogenetic stimulation" |

### Collections data fields
Please see the dedicated page describing the [Collections data model]({{"datamodel/stem/collection"|absolute_url}}).

## Permissions

The session inherits permissions from its associated projects. Data storage is shared through the project groups, and you can only add data storage associated with the same groups as the selected projects. The relationships in modules also depend on the selected projects.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## API access

The API allows for programmable access to sessions. Learn more about the sessions' fields and data structure on the [Session API page]({{"api/stem/session/"|absolute_url}}).