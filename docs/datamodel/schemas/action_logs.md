---
layout: default
title: Action log types
parent: Schemas
grand_parent: Data model
nav_order: 6
---

# Action log types
{: .no_toc}

Several action log types are provided to systematically record specific parameters or outcomes related to actions performed during experiments.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Impedances log

This log records the electrical impedance of electrodes implanted in the brain or other tissues over time.

| Field | Description |
|:------|:------------|
| `Impedances (kOhm)` | Measured impedance values in kiloohms (**required**) |
| `Phases (degrees)` | Phase angles of the impedance measurements in degrees |
| `List of channels` | Identifiers for the channels being measured |

## Linear displacement log

A linear displacement log tracks the movement or position of an object or device in a straight line.

| Field | Description |
|:------|:------------|
| `Displacement (μm)` | Measured displacement in micrometers (**required**) |

## Tetrode log (4 tetrodes)

This log keeps records related to the use and performance of a set of four tetrodes.

| Field | Description |
|:------|:------------|
| `Tetrode #1 (μm)` | Position or depth of the first tetrode in micrometers |
| `Tetrode #2 (μm)` | Position or depth of the second tetrode in micrometers |
| `Tetrode #3 (μm)` | Position or depth of the third tetrode in micrometers |
| `Tetrode #4 (μm)` | Position or depth of the fourth tetrode in micrometers |

## Tetrode log (8 tetrodes)

Similar to the log for four tetrodes, this log pertains to experiments involving a set of eight tetrodes.

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