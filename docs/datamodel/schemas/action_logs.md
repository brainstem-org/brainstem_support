---
layout: default
title: Procedure log types
parent: Schemas
grand_parent: Data model
nav_order: 6
---

# Procedure log types
{: .no_toc}

Several procedure log types are provided to systematically record specific parameters or outcomes related to procedures performed during experiments.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Impedances log

This log records the electrical impedance of electrodes implanted in the brain or other tissues over time. Impedance measurement is crucial for assessing the quality of the electrical connection between the electrode and the surrounding tissue, which can affect the clarity and reliability of recorded neural signals. Impedances logs help in monitoring the condition and functionality of electrodes throughout the course of an experiment.

| Field | Description |
|:------|:------------|
| `Impedances (kOhm)` | Measured impedance values in kiloohms (**required**) |
| `Phases (degrees)` | Phase angles of the impedance measurements in degrees |
| `List of channels` | Identifiers for the channels being measured |

## Linear displacement log

A linear displacement log tracks the movement or position of an object or device in a straight line, often related to the precise placement of electrodes, probes, or other surgical tools during an experiment. This type of log is essential for documenting the depth and location adjustments of devices within neural tissue, ensuring that recordings or stimulations are made at consistent and intended sites.

| Field | Description |
|:------|:------------|
| `Displacement (μm)` | Measured displacement in micrometers (**required**) |

## Tetrode log (4 tetrodes)

This log keeps records related to the use and performance of a set of four tetrodes, which are specialized electrodes used for recording the electrical activity of neurons. A tetrode log would typically include information about the positioning, adjustments, impedance levels, and potentially the signal quality obtained from each of the four tetrodes. This information is crucial for analyzing neural data accurately and understanding the spatial context of the recordings.

| Field | Description |
|:------|:------------|
| `Tetrode #1 (μm)` | Position or depth of the first tetrode in micrometers |
| `Tetrode #2 (μm)` | Position or depth of the second tetrode in micrometers |
| `Tetrode #3 (μm)` | Position or depth of the third tetrode in micrometers |
| `Tetrode #4 (μm)` | Position or depth of the fourth tetrode in micrometers |

## Tetrode log (8 tetrodes)

Similar to the log for four tetrodes, this log pertains to experiments involving a set of eight tetrodes. It provides detailed records for each tetrode, including their placement, electrical properties, and the quality of neural recordings. Keeping a separate log for eight tetrodes might be necessary for experiments that require more extensive neural coverage or when comparing different regions or aspects of neural activity simultaneously.

| Field | Description |
|:------|:------------|
| `Tetrode #1 (μm)` | Position or depth of the first tetrode in micrometers |
| `Tetrode #2 (μm)` | Position or depth of the second tetrode in micrometers |
| `Tetrode #3 (μm)` | Position or depth of the third tetrode in micrometers |
| `Tetrode #4 (μm)` | Position or depth of the fourth tetrode in micrometers |
| `Tetrode #5 (μm)` | Position or depth of the fifth tetrode in micrometers |
| `Tetrode #6 (μm)` | Position or depth of the sixth tetrode in micrometers |
| `Tetrode #7 (μm)` | Position or depth of the seventh tetrode in micrometers |
| `Tetrode #8 (μm)` | Position or depth of the eighth tetrode in micrometers |

## Procedure log API access

The API allows for programmable access to Procedure logs, enabling you to read, edit, and delete procedure logs through the API. Learn more about the procedure logs' fields and data structure on the [Procedure log API page]({{"api/modules/actionlog/"|absolute_url}}).