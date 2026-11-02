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

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A procedure log is a longitudinal measurement series attached to one procedure: electrode impedances, linear drive displacement, tetrode drive adjustments. The log holds what stays the same across the series (the procedure and the kind of measurement); each entry holds one dated measurement. These logs document the effectiveness, consistency and potential issues of implants and equipment over time. Fields are tailored to the log type.

{% include datamodel_embed.html model="modules.procedurelog" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Type`` | Type of procedure log (**required**). Selected from predefined types. Example: "Impedances log". *See options below* |
| ``Description`` | Description of the log series (string; maximum length: 500 characters). Example: "Daily impedance measurements for tetrode array" |
| ``Procedure`` | The procedure of the log (**required**). Must reference an existing [procedure]({{"datamodel/modules/procedure/"|absolute_url}}). Example: "Silicon probe implant #A123" |
| **Log Entries** | Multiple log entries can be added from the log's own page, each containing: |
| ``Date and time`` | Timestamp of the entry (**required**; datetime; format: YYYY-MM-DD HH:mm:ss). |
| ``Performed by`` | User who performed the measurement. Can differ from the user who created the log. |
| ``Notes`` | Notes for the entry (string; maximum length: 500 characters). |
| ``Type specific fields`` | Fields based on the log type, per entry. See the [Procedure log types schema]({{"datamodel/schemas/procedurelog/"|absolute_url}}). |

## Types of procedure logs

These are the available type options for procedure logs. See the schema for field details: [Procedure log types]({{"datamodel/schemas/procedurelog/"|absolute_url}}).

`Impedances log`: Electrode impedance measurements over time, used to follow contact quality and detect failing channels. Entry fields: impedances (kΩ), phases (°) and the list of channels, recorded in the same order as the values.

`Linear displacement log`: Ordered position or depth adjustments for a probe advanced on a microdrive. Each entry is one movement, so the series reconstructs the device's depth history. Entry field: displacement.

`Tetrode adjustment log`: A sheet of drive adjustments. Each dated entry is one row and each tetrode one column; a cell records how far that tetrode was moved, as a distance or as screw rotation, with negative values retracting. The number of columns follows the procedure's tetrode count. The detail page shows a running total per tetrode and a depth chart.

## Submission form

The procedure log submission form consists of two parts:

1. First part: Fill in the required fields.
2. Second part: After clicking "Create and continue," you can edit all fields and add entries.

## Permissions

Procedure logs inherit permissions from projects via the subject and then the procedure associated with the log.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to procedure logs, enabling you to read, edit, and delete procedure logs through the API. Entries are added, changed and removed through the log's `add_entry`, `change_entry` and `remove_entry` actions. Learn more about the procedure logs' fields and data structure on the [Procedure logs API page]({{"api/modules/procedurelog/"|absolute_url}}).
