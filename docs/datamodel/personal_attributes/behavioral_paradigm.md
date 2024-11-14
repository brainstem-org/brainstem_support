---
layout: default
title: Behavioral paradigm
parent: Personal attributes
grand_parent: Data model
nav_order: 1
---

# Dataset model
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
| `Name`                 | Name of the behavioral paradigm (**required**) |
| `Environment type`     | Type of environment in which the behavioral paradigm is performed (**required**) |
| `Authenticated groups` | Groups that have change permissions for this behavioral paradigm (**required**) |
| `Description`          | Text description of the behavioral paradigm |
| `Sensory stimulus type`| Type of sensory stimulus presented to the subject during the behavioral paradigm |
| `Public access`        | Determines if the behavioral paradigm is publicly available or accessible only through the private portal |

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

Visit the [permissions page]({{"datamodel/permission}}) to learn more. 

## Dataset API access

The API allows for programmable access to Behavioral paradigms, enabling you to read, edit, and delete Behavioral paradigms through the API. Learn more about the datasets' fields and data structure on the [Dataset API page]({{"api/personal_attributes/behavioralparadigm/"|absolute_url}}). 
