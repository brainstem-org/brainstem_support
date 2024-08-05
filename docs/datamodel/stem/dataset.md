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
A dataset is a modular construction that provides flexible and standardized descriptions of various aspects of experiments. The dataset has a number of direct fields, but is primarily described by the four modules below: 
1. Behavior: Description of the behavior the animal subject(s) is doing during the collection of the dataset. A behavior is described by two personal attributes: the experimental setup and the behavioral paradigm.
2. Experiment data: Description of the data acquisition files. The Experiment Data module is highly flexible and can be used to describe many types of experimental data, such as Extracellular and Intracellular Electrophysiology, 2-photon microscopy, Miniscope, Audio Recordings, and Behavioral Video Recordings. Details are tailored to each experiment type.
3. Manipulations: Description of any manipulations performed during an experiment. This is a crusial module as manipulations alters the physiological conditions of a recording. The Manipulations module is flexible and can describe many types of manipulations, such as Optogenetic Stimulation, Micro Perfusion, Pharmacological Injection, Thermal Perturbation, Transcranial Electrical Stimulation, and Ultrasound Stimulation. A manipulation is described by a manipulation protocol, typically consisting of a description of the manipulation profile, its power, duration, duty cycle, and the number of repetitions.
4. Epochs: Temporal aspects of a dataset. An epoch is characterized by a name, a start and end time relative to the start of the dataset. The other modules (Experiment Data, Manipulations, and Behavior) can be linked to epochs, allowing for temporal segmentation of a dataset.

## Dataset fields

| Field            | Description |
|:-----------------|:------------|
| Name             | Name of the dataset (**required**; string; max length: 100 characters; must be unique) |
| Projects         | Any projects the dataset belongs to. Learn more about the project inheritance [here] (**required**) |
| Description      | A text description of the dataset. Pictures can be uploaded and inserted. |
| Date and time    | Date and time of the onset of the dataset (YYYY-MM-DD string containing date, e.g. "2023-03-22") |
| Datarepositories | Describes where the data is stored |
| Extra fields     | Allows you to add extra fields to the dataset. The values can be a string or a numeric value |
| Download links   | JSON dictionary | name value pairs allowing you to add extra content |
| Name used in repository | Custom name for a dataset used in an organization in a repository (string; max length: 200) |
| Tags             | Tags for the dataset. Tags are great for organizational purpose, to quickly label a dataset and can be used as a filter afterwards |


### Epoch fields

| Field           | Description |
|:----------------|:------------|
| Name            | Name of the epoch (**required**; a string; max length: 100 characters) |
| Start           | Start time of the epochs. The start time is relative to the onset of the dataset (the date and time field of the dataset) |
| End             | End time of the epochs. The start time is relative to the onset of the dataset (the date and time field of the dataset) |
| Behavior        | Behavior associated with the epoch |
| Experiment data | Experiment data associated with the epoch |
| Manipulation    | A manipulation associated with the epoch |


### Experiment data fields
Please see the dedicated page describing the [Experiment data model].

### Manipulation data fields
Please see the dedicated page describing the [Manipulations data model].

### Behavior data fields
Please see the dedicated page describing the [Behavior data model].

## Permissions
The dataset inherits permissions from projects associated with it. Data repositories are shared through the projects groups, and you are only able to add a data repository associated with the same groups as the selected projects. The relationships in modules also depends on the selected projects

Visit the [permissions page] to learn more. 


### Dataset API access
The API allows for programmable access to datasets. Learn more about the datasets' fields and data structure on the [Dataset API page]({{"api/stem/dataset/"|absolute_url}}). 

