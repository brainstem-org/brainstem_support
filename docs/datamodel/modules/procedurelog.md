---
layout: default
title: Procedure logs
parent: Procedures
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
| ``Type`` | Type of procedure logs (**required**). Selected from predefined types. Example: "Impedances log", "Linear displacement log". *See options below* |
| ``Description`` | Description of the procedure logs. Can be left empty (string). Example: "Daily impedance measurements for tetrode array" |
| ``Procedure`` | The procedure of the log (**required**). Must reference an existing [procedure]({{"datamodel/modules/procedure/"|absolute_url}}). Example: "Silicon probe implant #A123" |
| **Log Entries** | Multiple log entries can be added, each containing: |
| ``Date and time`` | Timestamp for each entry in the log (**required**, datetime). Format: YYYY-MM-DD HH:mm:ss. Example: "2024-03-15 14:30:00" |
| ``Notes`` | Notes for each entry in the log (optional, string). Example: "Observed slight increase in impedance values" |
| ``Type specific fields`` | Custom fields based on procedure log type in JSON format for each entry. See [Procedure log types schema]({{"datamodel/schemas/procedurelog/"|absolute_url}}) for type-specific fields |


## Types of procedure logs

These are the available type options for procedure logs:

See the schema for field details: [Procedure logs types]({{"datamodel/schemas/procedurelog/"|absolute_url}}).

`Impedances log`: Records electrode impedance over time to assess contact quality and track electrode/tissue interface health.

`Linear displacement log`: Tracks linear movement or position (e.g., depth adjustments of probes/electrodes) to document precise placement over time.

`Tetrode log (4 tetrodes)`: Logs positioning, adjustments, impedances, and signal quality for a bundle of four tetrodes.

`Tetrode log (8 tetrodes)`: Logs positioning, adjustments, impedances, and signal quality for a bundle of eight tetrodes.


## Submission form

The procedure logs submission form consists of two parts:

1. First part: Fill in the required fields.
2. Second part: After clicking "Create and continue," you can edit all fields of the entry.


## Permissions

Procedure logs inherit permissions from projects via the subject and then the procedure associated with the entry.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to Procedure logs, enabling you to read, edit, and delete procedure logs through the API. Learn more about the procedure logs' fields and data structure on the [Procedure logs API page]({{"api/modules/procedurelog/"|absolute_url}}).
