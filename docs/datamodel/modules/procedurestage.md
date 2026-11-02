---
layout: default
title: Procedure stages
parent: Materials
grand_parent: Data model
nav_order: 2
---

# Procedure stage model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A procedure stage is one ordered phase of a [procedure]({{"datamodel/modules/procedure/"|absolute_url}}) or a [specimen procedure]({{"datamodel/modules/specimenprocedure/"|absolute_url}}): a phase that several materials take part in together. The induction and the maintenance of an anesthetic are two stages of one Anesthesia procedure; the flush and the fixation are two stages of one perfusion; the permeabilization, blocking, primary incubation, wash, secondary incubation and detection are stages of one Immunolabeling. The stage carries the conditions shared by its materials once (route, rate, duration, temperature, agitation, number of cycles, bath volume), and each [material usage]({{"datamodel/modules/materialusage/"|absolute_url}}) row can name the stage it took part in.

A stage is not a procedure (the parent owns the event, its date and its type-specific fields), and not a material row (materials name a stage; they do not live inside it). Stages are also not a type family of their own: which stage types exist is set per procedure type, and two shared detail schemas serve all of them. Stages are edited inside the parent entry and have no API route of their own; they appear in the `stages` list of the parent's payload.

![A procedure type's rules can declare stages. Each stage carries the conditions its materials share (route, rate, duration), and every material usage row names one stage or none for the whole procedure.]({{site.baseurl}}/assets/images/diagrams/procedure-stages.svg)
*A procedure type's rules can declare stages. Each stage carries the conditions its materials share (route, rate, duration), and every material usage row names one stage or none for the whole procedure.*

{% include datamodel_embed.html model="modules.procedurestage" %}

## Fields

| Field | Description |
|:------|:------------|
| `Stage type` | The phase this stage represents (**required**). Chosen from the stage types declared for the parent's procedure type. Example: "Induction", "Maintenance", "Fixation step", "Wash step". *See options below.* |
| `Detail type` | The detail schema that records the conditions of the stage. Set by the stage type: Administration stage, Specimen processing stage, or none. A stage type with no detail schema carries order, type and notes only. |
| `Order` | Position of the stage in the parent's stage list (number). Stages are reordered by dragging in the web interface. |
| `Details` | The shared conditions of the stage, following the detail type. See the [Procedure stage types schema]({{"datamodel/schemas/specimenprocedurestage/"|absolute_url}}). |
| `Target scope` | Which targets of the parent the stage applied to (default: Procedure targets). Choices: Procedure targets (the same targets as the parent), Specific specimens. Only stages of a specimen procedure can target specific specimens. |
| `Target specimens` | For specimen procedure stages with target scope "Specific specimens": the [specimens]({{"datamodel/stem/specimen/"|absolute_url}}) the stage was applied to. |
| `Notes` | Notes about the stage (string; maximum length: 500 characters). |

## Detail schemas

Two detail schemas record stage conditions. See the field lists on the [Procedure stage types schema page]({{"datamodel/schemas/specimenprocedurestage/"|absolute_url}}).

`Administration stage`: For stages of an in-vivo administration. Route (inhaled, IP, IV, SC, IM, oral, topical), delivery method for inhaled stages (chamber, nose cone, face mask, intubation), gas concentration, volume, infusion rate and duration.

`Specimen processing stage`: For stages of ex-vivo processing. Applied/contact duration, applied/contact temperature, agitation, number of repeated cycles and applied/contact bath volume.

## Stage types per procedure type

Which stage types exist is part of the rules of each procedure type and specimen procedure type. Examples:

| Parent type | Stage types |
|:------------|:------------|
| Anesthesia (procedure) | Induction, Maintenance, Top-up, Reversal, Emergence, Other (Administration stage details) |
| Sedative (procedure) | Induction, Maintenance (no detail schema) |
| Brain perfusion fixation (procedure) | Flush, Fixation (no detail schema) |
| Sectioning (specimen procedure) | Sectioning run, Collection step, Storage step |
| Cryosectioning (specimen procedure) | Cryostat run, Collection step, Storage step |
| Fixation (immersion) (specimen procedure) | Fixation step, Wash step |
| Immunolabeling (specimen procedure) | Permeabilization step, Blocking step, Primary incubation, Wash step, Secondary incubation, Detection step, Counterstain step |
| Staining (specimen procedure) | Staining step, Differentiation step, Rinse step, Bluing step, Counterstain step, Dehydration step |
| Tissue clearing (specimen procedure) | Permeabilization, Decolorization, Delipidation, Wash, Clearing, Index matching, Other |

All specimen procedure types declare stages with Specimen processing stage details. Procedure types without declared stages (most surgical and implant procedures) have no stage list. The stages offered for each type are listed under the type on the [Procedure types]({{"datamodel/schemas/procedure/"|absolute_url}}) and [Specimen procedure types]({{"datamodel/schemas/specimenprocedure/"|absolute_url}}) schema pages.

## Stages and materials

A material usage names the stage it took part in through its "Stage" field. Each material role also declares which stages it may be assigned to; for example a Carrier gas on an Anesthesia procedure can be assigned to Induction, Maintenance, Top-up, Emergence or Other. A stage cannot be deleted while material rows still point to it.

## Templates

Procedure templates and specimen procedure templates carry their own stage templates, and the material usage templates in them can name a stage template. Applying the template creates the stages together with the material rows. Read more on the [Templates page]({{"datamodel/modules/templates/"|absolute_url}}).

## Permissions

Stages are part of their parent entry and share its permissions: through the subject of a procedure or the specimen set of a specimen procedure, and so from the projects of that record.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

Stages have no API route of their own. They are read and written as the `stages` list inside the [Procedure API]({{"api/modules/procedure/"|absolute_url}}) and [Specimen procedure API]({{"api/modules/specimenprocedure/"|absolute_url}}) payloads. The detail schemas are documented on the [SpecimenProcedureStage schemas API page]({{"api/schemas/specimenprocedurestage/"|absolute_url}}).
