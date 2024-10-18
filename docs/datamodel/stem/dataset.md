---
layout: default
title: Dataset
parent: STEM
grand_parent: Data model
nav_order: 3
---

# Dataset model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction 

A dataset is a modular construction that provides flexible and standardized descriptions of various aspects of experiments. The dataset has several direct fields but is primarily described by four modules:

1. Behavior: Description of the animal subject(s) behavior during the dataset collection. A behavior is described by two personal attributes: the experimental setup and the behavioral paradigm.
2. Experiment data: Description of the data acquisition files. This module is highly flexible and can describe many types of experimental data, such as Extracellular and Intracellular Electrophysiology, 2-photon microscopy, Miniscope, Audio Recordings, and Behavioral Video Recordings. Details are tailored to each experiment type.
3. Manipulations: Description of any manipulations performed during an experiment. This crucial module documents alterations to the physiological conditions of a recording. It can describe various types of manipulations, such as Optogenetic Stimulation, Micro Perfusion, Pharmacological Injection, Thermal Perturbation, Transcranial Electrical Stimulation, and Ultrasound Stimulation. A manipulation is described by a protocol, typically consisting of the manipulation profile, power, duration, duty cycle, and number of repetitions.
4. Epochs: Temporal aspects of a dataset. An epoch is characterized by a name, start and end times relative to the dataset's start. Other modules (Experiment Data, Manipulations, and Behavior) can be linked to epochs, allowing for temporal segmentation of a dataset.

## Dataset fields

| Field | Description |
|:------|:------------|
| `Name` | Name of the dataset (**required**; string; max length: 100 characters; must be unique) |
| `Projects` | Projects the dataset belongs to. Learn more about project inheritance [here] (**required**) |
| `Description` | A text description of the dataset. Pictures can be uploaded and inserted. |
| `Date and time onset` | Date and time of the dataset onset (YYYY-MM-DD format, e.g., "2023-03-22") |
| `Tags` | Tags for the dataset. Great for organizational purposes, quick labeling, and filtering. |
| `Data storage` | Describes where the data is stored |
| `Name used in storage` | Custom name for the dataset used in local data storage (string; max length: 200) |
| `Extra fields` | Allows you to add extra fields to the dataset. Values can be strings or numeric. |
| `Online repositories` | If this dataset has been shared in a public repository, link it here. |

### Epoch fields

| Field | Description |
|:------|:------------|
| `Name` | Name of the epoch (**required**; string; max length: 100 characters) |
| `Start` | Start time of the epoch, relative to the dataset onset |
| `End` | End time of the epoch, relative to the dataset onset |
| `Behavior` | Behavior associated with the epoch |
| `Experiment data` | Experiment data associated with the epoch |
| `Manipulation` | Manipulation associated with the epoch |

### Experiment data fields

Please see the dedicated page describing the [Experiment data model]({{"datamodel/modules/experiment_data"|absolute_url}}).

### Manipulation data fields

Please see the dedicated page describing the [Manipulations data model]({{"datamodel/modules/manipulation"|absolute_url}}).

### Behavior data fields

Please see the dedicated page describing the [Behavior data model]({{"datamodel/modules/behavior"|absolute_url}}).

## Permissions

The dataset inherits permissions from its associated projects. Data storage is shared through the project groups, and you can only add data storage associated with the same groups as the selected projects. The relationships in modules also depend on the selected projects.

Visit the [permissions page] to learn more. 

## Dataset API access

The API allows for programmable access to datasets. Learn more about the datasets' fields and data structure on the [Dataset API page]({{"api/stem/dataset/"|absolute_url}}).