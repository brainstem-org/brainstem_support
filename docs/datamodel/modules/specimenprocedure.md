---
layout: default
title: Specimen procedures
parent: Specimen sets
grand_parent: Data model
nav_order: 2
---

# Specimen procedure model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A specimen procedure is one tissue-processing event performed on ex-vivo material: dissection, sectioning, fixation, embedding, clearing, staining, immunolabeling and similar steps. It is applied to a [specimen set]({{"datamodel/stem/specimenset/"|absolute_url}}) as a whole or to specific [specimens]({{"datamodel/stem/specimen/"|absolute_url}}) within the set. Specimen procedures are the ex-vivo counterpart of [procedures]({{"datamodel/modules/procedure/"|absolute_url}}), which record in-vivo interventions on a live subject.

A specimen procedure is an event. It is not a device (that is an [experimental interface]({{"datamodel/modules/experimentalinterface/"|absolute_url}})), not live-animal surgery (a procedure, which owns coordinates and anesthesia), not continuous monitoring (a [specimen log]({{"datamodel/modules/specimenlog/"|absolute_url}})), and not material identity. The reagents, media and supplies applied in the event are recorded as ordered [material usage]({{"datamodel/modules/materialusage/"|absolute_url}}) rows, and repeated within-event steps such as the baths of a staining protocol are recorded as [procedure stages]({{"datamodel/modules/procedurestage/"|absolute_url}}).

Performed whole-set specimen procedures update the preparation conditions of the set (for example a performed fixation adds the condition "Fixed"). Procedures that target specific specimens update the conditions of those specimens only.

{: .warning }
> The specimen procedure type family is still being refined and its type-specific fields may change between releases.

{% include datamodel_embed.html model="modules.specimenprocedure" %}

## Fields

| Field | Description |
|:------|:------------|
| `Procedure type` | Type of processing step (**required**; default: Sectioning). Selected from predefined types. Example: "Immunolabeling". *See options below.* |
| `Status` | Planning status (**required**; default: Performed). Choices: Planned (prepared but nothing has happened yet), Performed (this record describes what was done), Cancelled (planned and then dropped; kept for the record). *See the status section below.* |
| `Specimen set` | The [specimen set]({{"datamodel/stem/specimenset/"|absolute_url}}) the procedure was performed on (**required**). |
| `Target scope` | Whether the procedure applies to the whole specimen set or to specific specimens only (**required**; default: Whole set). Choices: Whole set, Specific specimens. |
| `Target specimens` | The individual [specimens]({{"datamodel/stem/specimen/"|absolute_url}}) targeted by the procedure. Leave empty when the procedure applies to the whole set. |
| `Date and time` | Date and time the procedure was performed (datetime format `YYYY-MM-DD HH:mm:ss`). Required to move a planned procedure to performed. |
| `Target regions` | [Anatomical regions]({{"datamodel/taxonomies/anatomicalregion/"|absolute_url}}) the processing was aimed at. Can include multiple regions. |
| `Equipment` | [Equipment]({{"datamodel/modules/equipment/"|absolute_url}}) used, such as a vibratome, cryostat or microscope. Can include multiple items. |
| `Protocol` | Optional reusable [protocol]({{"datamodel/personal_attributes/protocol/"|absolute_url}}) describing the method followed. Must have protocol type Specimen procedure. |
| `Licenses` | [Licenses]({{"datamodel/personal_attributes/license/"|absolute_url}}) authorizing the work, if applicable. |
| `Notes` | Notes about the procedure (string; maximum length: 500 characters). |
| `Type specific fields` | Fields that depend on the selected type, such as section thickness, orientation or retrieval method. See the [Specimen procedure types schema]({{"datamodel/schemas/specimenprocedure/"|absolute_url}}). |
| `Materials` | Ordered list of the [material usages]({{"datamodel/modules/materialusage/"|absolute_url}}) applied in the event (fixative, buffers, antibodies, mounting medium, slides, ...). Edited inside the procedure. *See below.* |
| `Stages` | Ordered list of the [procedure stages]({{"datamodel/modules/procedurestage/"|absolute_url}}) of the event. Edited inside the procedure. *See below.* |

## Types of specimen procedures

These are the 17 available type options. See the schema for field details: [Specimen procedure types]({{"datamodel/schemas/specimenprocedure/"|absolute_url}}).

### Preparation

`Dissection`: Isolating a region or structure from the tissue.

### Sectioning

`Sectioning`: Cutting the tissue into slices or sections, for example with a vibratome or microtome.

`Cryosectioning`: Cutting frozen tissue into thin sections with a cryostat.

### Fixation and Preservation

`Fixation (immersion)`: Preserving the tissue by immersion in a fixative.

`Cryopreservation`: Equilibrating the tissue in a cryoprotectant and freezing it.

`Embedding`: Infiltrating and embedding the tissue in a supporting medium.

### Tissue Processing

`Dehydration`: Removing water from the tissue through a graded series of solvents.

### Labeling and Staining

`Antigen retrieval`: Unmasking antigens, typically by heat or enzymes, before immunolabeling.

`Blocking`: Reducing non-specific binding before labeling.

`Dye loading`: Loading the tissue with a dye, for example a calcium indicator.

`Immunolabeling`: Labeling with primary and secondary antibodies and a detection step.

`In situ hybridization`: Labeling nucleic acids with hybridization probes.

`Staining`: Histological staining with dyes.

`Wash step`: One or more wash cycles between labeling steps.

### Clearing and Mounting

`Tissue clearing`: Chemically rendering the tissue transparent for deep imaging.

`Mounting`: Mounting sections on slides or in a chamber with a mounting medium.

### Generic

`Generic intervention`: A processing step not covered by the types above.

## Target scope

A specimen procedure either applies to the whole set or to specific specimens. With the target scope "Whole set", the target specimens field stays empty and the conditions added by the procedure are written to the set and to all of its specimens. With "Specific specimens", you pick the specimens the procedure was applied to and only those specimens receive the conditions. Material usages and stages of a specimen procedure can in turn name the specimens they were applied to, for example when different sections of one series went through different baths.

## Materials and stages

Materials are not fields of the type schema. Each material is one [material usage]({{"datamodel/modules/materialusage/"|absolute_url}}) row with a role (for example Fixative, Primary immunolabeling reagent, Mounting medium), a source (an inventory stock, a catalog consumable or a manual entry) and the values as applied in this event. Which roles a procedure type allows, which are required and when a row counts as complete is declared per type. These rules are listed in the "Materials that can be recorded on this type" tables on the [Specimen procedure types schema page]({{"datamodel/schemas/specimenprocedure/"|absolute_url}}).

Stages split one event into ordered phases that several materials take part in together, such as the permeabilization, blocking, primary incubation, wash, secondary incubation, detection and counterstain steps of an immunolabeling. Each stage carries the shared conditions once (duration, temperature, agitation, number of cycles, bath volume) using the Specimen processing stage detail schema. Each material row can name the stage it took part in. Read more on the [Procedure stages page]({{"datamodel/modules/procedurestage/"|absolute_url}}).

## Planning status

Specimen procedures take part in the planning lifecycle. A planned procedure describes work that has not happened yet; a performed procedure describes what was done; a cancelled procedure was planned and then dropped but is kept for the record. Titles of planned and cancelled records are prefixed "Planned:" and "Cancelled:" in the web interface. Only performed procedures update the preparation conditions of the set and its specimens. Moving a procedure from planned to performed requires a date and time. Lists in the REST API return performed procedures by default; add `include_planned=true` or a status filter to see plans.

## Permissions

Specimen procedures inherit permissions through the specimen set associated with them, and so from the projects of that set.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to specimen procedures, including their materials. Learn more about the specimen procedures' fields and data structure on the [Specimen procedure API page]({{"api/modules/specimenprocedure/"|absolute_url}}).
