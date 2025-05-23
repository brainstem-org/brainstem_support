---
layout: default
title: Procedure logs
parent: Procedure
grand_parent: Subjects
nav_order: 1
---

# Procedure log model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Procedure logs refer to systematic records that track specific parameters or outcomes related to the procedures performed on or with subjects in scientific studies. These logs are vital for ensuring the accuracy and reproducibility of experimental results, allowing researchers to monitor the effectiveness, consistency, and potential issues associated with various procedures and equipment used in their studies. Procedure log types share relationships, but fields are tailored to the various procedure logs types.

## Fields

| Field | Description |
|:------|:------------|
| `Type` | Type of procedure logs (**required**). Selected from predefined types. Example: "Impedances log", "Linear displacement log". *See options below* |
| `Procedure` | The procedure of the log (**required**). Must reference an existing [procedure]({{"datamodel/modules/procedure/"|absolute_url}}). Example: "Silicon probe implant #A123" |
| `Description` | Description of the procedure logs. Can be left empty (string). Example: "Daily impedance measurements for tetrode array" |
| `Date and time` | Timestamp for each entry in the log. Example: "2024-03-15 14:30:00" |
| `Type details` | Type-specific fields for each entry in the log. Fields vary by type. Example: For impedance log - impedance values in kOhm. *See options below* |
| `Notes` | Notes about the procedure logs for each entry in the log (string). Example: "Observed slight increase in impedance values" |


## Types of procedure logs

These are the available *Type* options for Procedure logs:

- `Impedances log`: This log records the electrical impedance of electrodes implanted in the brain or other tissues over time. Impedance measurement is crucial for assessing the quality of the electrical connection between the electrode and the surrounding tissue, which can affect the clarity and reliability of recorded neural signals. Impedances logs help in monitoring the condition and functionality of electrodes throughout the course of an experiment.
- `Linear displacement log`: A linear displacement log tracks the movement or position of an object or device in a straight line, often related to the precise placement of electrodes, probes, or other surgical tools during an experiment. This type of log is essential for documenting the depth and location adjustments of devices within neural tissue, ensuring that recordings or stimulations are made at consistent and intended sites.
- `Tetrode log (4 tetrodes)`: This log keeps records related to the use and performance of a set of four tetrodes, which are specialized electrodes used for recording the electrical activity of neurons. A tetrode log would typically include information about the positioning, adjustments, impedance levels, and potentially the signal quality obtained from each of the four tetrodes. This information is crucial for analyzing neural data accurately and understanding the spatial context of the recordings.
- `Tetrode log (8 tetrodes)`: Similar to the log for four tetrodes, this log pertains to experiments involving a set of eight tetrodes. It provides detailed records for each tetrode, including their placement, electrical properties, and the quality of neural recordings. Keeping a separate log for eight tetrodes might be necessary for experiments that require more extensive neural coverage or when comparing different regions or aspects of neural activity simultaneously.

A detailed list of the type-specific fields can be found on the [procedure logs types page]({{"datamodel/schemas/procedurelog/"|absolute_url}}).


## Submission form

The procedure logs submission form consists of two parts:
1. First part: Fill in the required fields.
2. Second part: After clicking "Create and continue," you can edit all fields of the entry.

## Permissions

Procedure logs inherit permissions from projects via the subject and then the procedure associated with the entry.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## API access

The API allows for programmable access to Procedure logs, enabling you to read, edit, and delete procedure logss through the API. Learn more about the procedure logss' fields and data structure on the [Procedure logs API page]({{"api/modules/procedurelog/"|absolute_url}}).
