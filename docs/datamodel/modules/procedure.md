---
layout: default
title: Procedure
parent: Modules
grand_parent: Data model
nav_order: 6
---

# Procedure model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Procedures cover surgical procedures and other methods that allow tracking or recording from subject(s). Procedures have type-specific fields tailored to various procedure types. The types of procedures currently supported by BrainSTEM are listed below. A procedure is described by the fields in the next section.

## Fields

| Field | Description |
|:------|:------------|
| `Type` | Type of procedure (**required**). *See options below* |
| `Subject` | The subject the procedure was performed on (**required**) |
| `Notes` | Notes about the procedure (max length: 500 characters) |
| `Date and time` | Date and time the procedure was performed (e.g., "2023-03-22") |
| `Consumable` | Consumable used for the procedure |
| `Hardware device` | Hardware device used to perform the procedure |
| `Brain region` | Target brain region where the procedure was performed |
| `Coordinates system` | Coordinate system (**required**). *See options below* |
| `Type details` | Type-specific fields. *See options below* |

## Types of procedures

These are the available *Type* options for Procedure:

- Brain lesion
- Craniectomy
- Craniotomy
- Optic fiber implant
- Brain perfusion fixation
- Single wire electrode
- Silicon probe implant
- Brain slice
- Tetrode wire electrode
- Virus injection

A detailed list of the type-specific fields can be found on the [procedure types page]({{"datamodel/schemas/procedures/"|absolute_url}}).

## Coordinate system options

Available Coordinate system options for Procedure:

| Type | Description |
|:-----|:------------|
| `External X-Y-Z Coordinates with Angles` | Three-dimensional Cartesian system with absolute positions (X, Y, Z) and angles relative to an external reference point. Ideal for precise global positioning. |
| `Stereotaxic Bregma-Based Absolute` | Stereotaxic coordinates using Bregma on the skull as origin. Uses AP, ML, DV coordinates and angles for precise skull-based targeting. |
| `Stereotaxic Bregma-Based Surface with Depth` | Stereotaxic coordinates measuring from brain surface beneath Bregma. Uses AP, ML coordinates, depth, and rotation. Accommodates brain surface curvature. |
| `Stereotaxic Lambda-Based Absolute` | Stereotaxic coordinates using Lambda on the skull as origin. Uses AP, ML, DV coordinates and angles. Alternative skull-based reference point for varied setups. |
| `Stereotaxic Lambda-Based Surface with Depth` | Stereotaxic coordinates measuring from brain surface beneath Lambda. Uses AP, ML coordinates, depth, and rotation. Useful for targeting occipital brain areas. |
| `Stereotaxic X-Y-Z Absolute` | Stereotaxic coordinates using X, Y, Z absolute positions and angles. Enables precise navigation within stereotaxic frame. |
| `Stereotaxic X-Y Surface with Depth` | Stereotaxic coordinates using X, Y positions on brain surface, plus depth and rotation. For experiments needing lateral and anteroposterior precision. |

A detailed list of the fields in Coordinate system can be found on the [Coordinate system page]({{"datamodel/schemas/coordinates/"|absolute_url}}).

## Permissions

Procedures inherit permissions through the subject associated with them.

Visit the [permissions page]({{"datamodel/permission}}) to learn more. 

## Procedure API access
The API allows for programmable access to procedures. Learn more about the procedures' fields and data structure on the [Procedure API page]({{"api/modules/procedure/"|absolute_url}}).
