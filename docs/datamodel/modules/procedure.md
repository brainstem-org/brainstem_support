---
layout: default
title: Procedure
parent: Modules
grand_parent: Data model
nav_order: 4
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
| Type | Type of procedure (**required**). *See options below* |
| Subject | The subject the procedure was performed on (**required**) |
| Notes | Notes about the procedure (max length: 500 characters) |
| Date and time | Date and time the procedure was performed (e.g., "2023-03-22") |
| Consumable | Consumable used for the procedure |
| Hardware device | Hardware device used to perform the procedure |
| Brain region | Target brain region where the procedure was performed |
| Coordinates system | Coordinate system (**required**). *See options below* |
| Type details | Type-specific fields. *See options below* |

## Types of procedures
These are the available *Type* options for Procedure:

- Optic fiber implant
- Single wire electrode
- Silicon probe implant
- Tetrode wire electrode
- Virus injection

A detailed list of the type-specific fields can be found on the [procedure type page]({{"datamodel/schemas/procedures/"|absolute_url}}).

## Coordinate system options
Available Coordinate system options for Procedure:

| Type | Description |
|:-----|:------------|
| Stereotaxic Bregma absolute | Stereotaxic coordinates with Bregma as the origin. AP, ML, DV are used as coordinates |
| Stereotaxic Bregma brain surface | Stereotaxic coordinates with Bregma as the origin. AP, ML and depth are used as coordinates |
| Stereotaxic Lambda absolute | Stereotaxic coordinates with Lambda as the origin. AP, ML, DV are used as coordinates |
| Stereotaxic Lambda brain surface | Stereotaxic coordinates with Lambda as the origin. AP, ML and depth are used as coordinates |
| Stereotaxic X-Y-Z | Stereotaxic coordinates using the Allen Institute's absolute X-Y-Z as coordinates |
| Stereotaxic X-Y Surface | Stereotaxic coordinates using the Allen Institute's absolute X-Y-Surface depth as coordinates |

A detailed list of the fields in Coordinate system can be found on the [Coordinate system page]({{"datamodel/schemas/coordinates/"|absolute_url}}).

## Permissions
Procedures inherit permissions through the subject associated with them.

Visit the [permissions page] to learn more. 

## Procedure API access
The API allows for programmable access to procedures. Learn more about the procedures' fields and data structure on the [Procedure API page]({{"api/modules/procedure/"|absolute_url}}).