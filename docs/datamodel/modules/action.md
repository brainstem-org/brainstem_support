---
layout: default
title: Action
parent: Modules
grand_parent: Data model
nav_order: 1
---

# Action model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction
Actions covers surgical procedures and other methods that allows you to track or record from a subject(s). Actions have type-specific fields that are tailored to various action-types. The types of actions currently supported by BrainSTEM are listed further down the page. An action is described by the fields in the next section.

## Fields

| Field               | Description  |
|:--------------------|:-------------|
| Type                | the type of action (**required**). *See options below* |
| Description         | Description of the action (max length: 500) |
| Subject             | The subject the action was performed on (**required**) |
| Date and time       | Date and time the action was performed (e.g. "2023-03-22") |
| Consumable          | Consumable used for the action |
| Hardware device     | Hardware device used to perform the action |
| Brain region        | Target brain region where the action was performed |
| Coordinates system  | Coordinate system  (**required**). *See options below* |
| Type details        | There are also a number of type specific fields. *See options below* |

## Types of actions
These are the available _Type_ options for Action:
- Optic fiber implant
- Single wire electrode
- Silicon probe implant
- Tetrode wire electrode
- Virus injection

A detailed list of the type-specific fields, can be found in the [action type page]({{"/datamodel/schemas/actions/"|absolute_url}}).

Below are the available Coordinates system options for Action:

| Type                             | Description  |
|:---------------------------------|:-------------|
| Stereotaxic Bregma absolute      | Stereotaxic coordinates with Bregma as the origin. AP, ML, DV are used as coordinates |
| Stereotaxic Bregma brain surface | Stereotaxic coordinates with Bregma as the origin. AP, ML and depth are used as coordinates |
| Stereotaxic Lambda absolute      | Stereotaxic coordinates with Lambda as the origin. AP, ML, DV are used as coordinates |
| Stereotaxic Lampda brain surface | Stereotaxic coordinates with Lambda as the origin. AP, ML and depth are used as coordinates |
| Stereotaxic X-Y-Z                | Stereotaxic coordinates using the Allen Institutes's absolute X-Y-Z as coordinates |
| Stereotaxic X-Y Surface          | Stereotaxic coordinates using the Allen Institutes's absolute X-Y-Surface depth as coordinates |

A detailed list of the fields in Coordinates system, can be found in the [Coordinate system page]({{"datamodel/schemas/coordinates/"|absolute_url}}).

## Permissions
Actions inherit permissions through the subject associated with it.

Visit the [permissions page] to learn more. 

## Action API access
The API allows for programmable access to actions. Learn more about the actions' fields and data structure on the [Action API page]({{"api/modules/action/"|absolute_url}}). 
