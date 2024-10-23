---
layout: default
title: Action logs
parent: Modules
grand_parent: Data model
nav_order: 7
---

# Action logs model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Action logs refer to systematic records that track specific parameters or outcomes related to the actions (procedures) performed on or with subjects in scientific studies. These logs are vital for ensuring the accuracy and reproducibility of experimental results, allowing researchers to monitor the effectiveness, consistency, and potential issues associated with various procedures and equipment used in their studies. Action log types share relationships, but fields are tailored to the various action log types.

## Fields

| Field | Description |
|:------|:------------|
| `Type` | Type of action log (**required**). *See options below* |
| `Procedure` | The action of the log (**required**) |
| `Description` | Description of the action log |
| `Date and time` | Timestamp for each entry in the log |
| `Type details` | Type-specific fields for each entry in the log. *See options below* |
| `Notes` | Notes about the action log for each entry in the log |

## Types of action logs

These are the available *Type* options for Action logs:

- Impedances log
- Linear displacement log
- Tetrode log (4 tetrodes)
- Tetrode log (8 tetrodes)

A detailed list of the type-specific fields can be found on the [action log types page]({{"datamodel/schemas/action_logs/"|absolute_url}}).

## Submission form

The action log submission form consists of two parts:
1. First part: Fill in the required fields.
2. Second part: After clicking "Create and continue," you can edit all fields of the entry.

## Permissions

Action logs inherit permissions from projects via the subject and then the procedure associated with the entry.

Visit the [permissions page] to learn more.

## Action log API access

The API allows for programmable access to Action logs, enabling you to read, edit, and delete action logs through the API. Learn more about the action logs' fields and data structure on the [Action log API page]({{"api/modules/actionlog/"|absolute_url}}).
