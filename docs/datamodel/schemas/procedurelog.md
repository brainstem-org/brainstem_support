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
| `Impedances` | Array of impedance measurements for the electrodes (**required**; non-negative numbers; measured in kOhm). These values indicate the resistance to electrical current flow between the electrode and surrounding tissue |
| `Phases` | Array of phase angle measurements (non-negative numbers; measured in degrees). These values represent the phase shift between voltage and current, providing information about the electrode-tissue interface properties |
| `List of channels` | Array of channel identifiers (non-negative integers) corresponding to the recording channels being measured. Used to track which impedance measurements correspond to which electrode channels |

## Linear displacement log

A linear displacement log tracks the movement or position of an object or device in a straight line, often related to the precise placement of electrodes, probes, or other surgical tools during an experiment. This type of log is essential for documenting the depth and location adjustments of devices within neural tissue, ensuring that recordings or stimulations are made at consistent and intended sites.

| Field | Description |
|:------|:------------|
| `Displacement` | The distance moved from a reference position (**required**; float; measured in μm). Records the linear movement of the device, typically representing depth in brain tissue or position along a track |

## Tetrode log (4 tetrodes)

This log keeps records related to the use and performance of a set of four tetrodes, which are specialized electrodes used for recording the electrical activity of neurons. A tetrode log would typically include information about the positioning, adjustments, impedance levels, and potentially the signal quality obtained from each of the four tetrodes. This information is crucial for analyzing neural data accurately and understanding the spatial context of the recordings.

| Field | Description |
|:------|:------------|
| `Tetrode #1` | Position measurement for the first tetrode (float; measured in μm) |
| `Tetrode #2` | Position measurement for the second tetrode (float; measured in μm) |
| `Tetrode #3` | Position measurement for the third tetrode (float; measured in μm) |
| `Tetrode #4` | Position measurement for the fourth tetrode (float; measured in μm) |

## Tetrode log (8 tetrodes)

Similar to the log for four tetrodes, this log pertains to experiments involving a set of eight tetrodes. It provides detailed records for each tetrode, including their placement, electrical properties, and the quality of neural recordings. Keeping a separate log for eight tetrodes might be necessary for experiments that require more extensive neural coverage or when comparing different regions or aspects of neural activity simultaneously.

| Field | Description |
|:------|:------------|
| `Tetrode #1` | Position measurement for the first tetrode (float; measured in μm) |
| `Tetrode #2` | Position measurement for the second tetrode (float; measured in μm) |
| `Tetrode #3` | Position measurement for the third tetrode (float; measured in μm) |
| `Tetrode #4` | Position measurement for the fourth tetrode (float; measured in μm) |
| `Tetrode #5` | Position measurement for the fifth tetrode (float; measured in μm) |
| `Tetrode #6` | Position measurement for the sixth tetrode (float; measured in μm) |
| `Tetrode #7` | Position measurement for the seventh tetrode (float; measured in μm) |
| `Tetrode #8` | Position measurement for the eighth tetrode (float; measured in μm) |

## API access

The API allows for programmable access to Procedure logs, enabling you to read, edit, and delete procedure logs through the API. Learn more about the procedure logs' schema fields on the [Procedure log schemas API page]({{"api/schemas/procedurelog/"|absolute_url}}).