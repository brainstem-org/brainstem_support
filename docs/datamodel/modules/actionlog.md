---
layout: default
title: Procedure logs
parent: Modules
grand_parent: Data model
nav_order: 7
---

# Procedure logs model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Procedure logs refer to systematic records that track specific parameters or outcomes related to the actions (procedures) performed on or with subjects in scientific studies. These logs are vital for ensuring the accuracy and reproducibility of experimental results, allowing researchers to monitor the effectiveness, consistency, and potential issues associated with various procedures and equipment used in their studies. Procedure log types share relationships, but fields are tailored to the various procedure logs types.

## Fields

| Field | Description |
|:------|:------------|
| `Type` | Type of procedure logs (**required**). Selected from predefined types. Example: "Impedances log", "Linear displacement log". *See options below* |
| `Procedure` | The action of the log (**required**). Must reference an existing [procedure]({{"datamodel/modules/procedure/"|absolute_url}}). Example: "Silicon probe implant #A123" |
| `Description` | Description of the procedure logs. Can be left empty (string; maximum length: 500 characters). Example: "Daily impedance measurements for tetrode array" |
| `Date and time` | Timestamp for each entry in the log. Example: "2024-03-15 14:30:00" |
| `Type details` | Type-specific fields for each entry in the log. Fields vary by type. Example: For impedance log - impedance values in kOhm. *See options below* |
| `Notes` | Notes about the procedure logs for each entry in the log (string; maximum length: 500 characters). Example: "Observed slight increase in impedance values" |


## Types of procedure logss

These are the available *Type* options for Procedure logs:

- Impedances log
- Linear displacement log
- Tetrode log (4 tetrodes)
- Tetrode log (8 tetrodes)

A detailed list of the type-specific fields can be found on the [procedure logs types page]({{"datamodel/schemas/action_logs/"|absolute_url}}).

## Submission form

The procedure logs submission form consists of two parts:
1. First part: Fill in the required fields.
2. Second part: After clicking "Create and continue," you can edit all fields of the entry.

## Permissions

Procedure logs inherit permissions from projects via the subject and then the procedure associated with the entry.

Visit the [permissions page]({{"datamodel/permission/"|absolute_url}}) to learn more. 

## Procedure log API access

The API allows for programmable access to Procedure logs, enabling you to read, edit, and delete procedure logss through the API. Learn more about the procedure logss' fields and data structure on the [Procedure logs API page]({{"api/modules/actionlog/"|absolute_url}}).
