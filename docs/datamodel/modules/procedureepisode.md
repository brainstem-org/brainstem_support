---
layout: default
title: Procedure episodes
parent: Subjects
grand_parent: Data model
nav_order: 2
---

# Procedure episode model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A procedure episode groups the [procedures]({{"datamodel/modules/procedure/"|absolute_url}}) of one perioperative event on a [subject]({{"datamodel/stem/subject/"|absolute_url}}) into a single compliance record. A typical episode is one surgery day: the anesthesia, the craniotomy, the implant, the analgesic and the fluid therapy are separate procedures, and the episode is the container that says they belong to one intervention, who took part, which protocol and licenses covered it, how severe it was and how the animal recovered.

The episode is the unit that regulatory reporting asks about. It carries the intervention class, the severity classification in the scheme of your regulator or institution, the recovery outcome, the personnel and a narrative. The individual procedures keep the scientific detail (coordinates, materials, type-specific fields). A procedure links to its episode through the procedure's "Procedure episode" field; an episode can hold many procedures. An episode is not a procedure itself, and it is not a [subject log]({{"datamodel/modules/subjectlog/"|absolute_url}}) (welfare checks and other follow-up observations stay in the logs).

{% include datamodel_embed.html model="modules.procedureepisode" %}

## Fields

| Field | Description |
|:------|:------------|
| `Intervention class` | Kind of intervention (**required**). Choices: Anesthesia only, Surgical, Non-surgical procedure, Euthanasia / tissue collection, Clinical treatment, Other. |
| `Name` | Name of the episode (**required**; string; maximum length: 200 characters). Example: "Mouse_01 probe implant surgery" |
| `Start date and time` | When the episode started (**required**; datetime format `YYYY-MM-DD HH:mm:ss`). |
| `End date and time` | When the episode ended. Leave empty while the episode is ongoing. |
| `Status` | Lifecycle status of the episode (**required**; default: Draft). Choices: Planned, Draft, Active, Post-operative, Complete. *See the status section below.* |
| `Subject` | The [subject]({{"datamodel/stem/subject/"|absolute_url}}) the episode is performed on (**required**). |
| `Protocol` | Optional reusable [protocol]({{"datamodel/personal_attributes/protocol/"|absolute_url}}) describing the method followed. |
| `Licenses` | Regulatory [licenses]({{"datamodel/personal_attributes/license/"|absolute_url}}) covering the episode. Can include multiple licenses. |
| `Severity` | Classified severity. The regulatory or institutional scheme is encoded in the selected value. *See the severity section below.* |
| `Recovery outcome` | Observed recovery, terminal, endpoint or cancellation outcome (**required**; default: Unknown). Choices: Unknown, Recovered / survival, Ongoing recovery, Non-recovery procedure, Planned terminal endpoint, Humane endpoint euthanasia, Unexpected death, Aborted, Cancelled. |
| `Description` | Rich text narrative covering complications, outcomes, amendments and other notes. |
| `Personnel` | The people who took part and their roles. Each row names a BrainSTEM user and one role: Surgeon, Anesthetist, Assistant, Observer, Veterinarian, Responsible person. The same person can hold several roles. |
| `Procedures` | The [procedures]({{"datamodel/modules/procedure/"|absolute_url}}) that belong to the episode. Set on each procedure through its "Procedure episode" field. |

## Status lifecycle

| Status | Meaning |
|:-------|:--------|
| Planned | A surgery day that has not come yet. The subject may still be planned too. A planned episode cannot contain performed procedures. |
| Draft | The record is being filled in (default for new episodes). |
| Active | The intervention is under way. The subject must exist in the lab (its status cannot be Planned). |
| Post-operative | The intervention is over and the animal is in post-operative care. |
| Complete | The episode is closed. A complete episode must include a named Responsible person in its personnel. |

Lists in the REST API exclude planned episodes by default; add `include_planned=true` or a status filter to see them.

## Severity classifications

The severity field holds one value, and the value says which scheme it belongs to. Choose the scheme of your regulator or institution:

| Scheme | Choices |
|:-------|:--------|
| EU Directive 2010/63/EU, actual severity | Non-recovery, Mild, Moderate, Severe |
| UK ASPA, actual severity | Sub-threshold, Non-recovery, Mild, Moderate, Severe |
| US IACUC / USDA, pain and distress category | No pain/distress, Pain/distress with relief, Pain/distress without relief |
| Canada CCAC, category of invasiveness | A (non-animal or tissue-only work), B (little or no discomfort or stress), C (minor, short-duration stress or pain), D (moderate to severe distress or discomfort), E (severe pain near the tolerance threshold) |
| Local / institutional classification | Sub-threshold, Non-recovery, Mild, Moderate, Severe |
| Not applicable | Not applicable |

## Templates

Procedure episode templates prefill a new episode with an intervention class, protocol, licenses, severity, recovery outcome and description. Read more on the [Templates page]({{"datamodel/modules/templates/"|absolute_url}}).

## Permissions

Procedure episodes inherit permissions through the subject associated with them, and so from the projects of that subject. Deleting an episode does not delete its procedures; it clears the episode link on them.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to procedure episodes and their personnel rows. Learn more about the procedure episodes' fields and data structure on the [Procedure episode API page]({{"api/modules/procedureepisode/"|absolute_url}}) and the [Episode personnel API page]({{"api/modules/episodepersonnel/"|absolute_url}}).
