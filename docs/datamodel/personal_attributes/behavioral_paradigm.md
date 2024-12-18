---
layout: default
title: Behavioral paradigm
parent: Personal attributes
grand_parent: Data model
nav_order: 1
---

# Behavior paradigm model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction 

Behavioral paradigms describe the paradigm a subject performs in details. The paradigm belongs to a type of environment.

## Dataset fields

| Field                | Description |
|:---------------------|:------------|
| `Name`                 | Name of the behavioral paradigm (**required**; string; maximum length: 50 characters). Example: "T-maze alternation task" |
| `Environment type`     | Type of environment in which the behavioral paradigm is performed (**required**). Example: "T-maze" |
| `Authenticated groups` | Groups that have change permissions for this behavioral paradigm (**required**). Example: "Lab A", "Neuroscience Department" |
| `Description`          | Rich text description of the behavioral paradigm. Can include uploaded images. Example: "In this task, rodents alternate between left and right arms of a T-maze to receive rewards..." |
| `Public access`        | Determines if the behavioral paradigm is publicly available or accessible only through the private portal. Example: "True" for public access |

## Types of environment type

- Barnes maze
- Circular track
- Elevated plus maze
- Elevated zero maze
- Figure eight maze
- Forced swim test
- Head-fixed disc
- Homecage
- Linear Track
- Morris water maze
- Open field environment
- Radial arm maze
- Running wheel
- Sleepbox
- Square cage
- Theta maze
- T-maze
- Y-maze
- Other

## Permissions

You manage permissions through the management tab, where you can assign individual users and groups access levels to a Behavioral paradigm. Behavioral paradigm have four permission levels: membership (read access), contributors, managers, and owners.

Visit the [permissions page]({{"datamodel/permission/"|absolute_url}}) to learn more. 

## Dataset API access

The API allows for programmable access to Behavioral paradigms, enabling you to read, edit, and delete Behavioral paradigms through the API. Learn more about the datasets' fields and data structure on the [Dataset API page]({{"api/personal_attributes/behavioralparadigm/"|absolute_url}}). 
