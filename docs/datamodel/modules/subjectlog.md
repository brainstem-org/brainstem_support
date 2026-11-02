---
layout: default
title: Subject logs
parent: Subjects
grand_parent: Data model
nav_order: 3
---

# Subject log model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

{::options toc_levels="2..2" /}
1. TOC
{:toc}

## Introduction

A subject log is a named stream of repeated observations for one subject: weight and welfare monitoring, consumption, deprivation, training, housing, genotyping. Create the stream once, then add dated entries over time. The log holds what stays the same across the series (subject, type, protocol, description); each entry holds one dated observation. Start a separate log when the type, subject, protocol or purpose changes.

Drug administrations are not subject logs. They are recorded as [procedures]({{"datamodel/modules/procedure/"|absolute_url}}) of the Anesthesia, Drug and Fluid Administration group.

{% include datamodel_embed.html model="modules.subjectlog" %}

## Fields

| Field | Description |
|:------|:------------|
| ``Type`` | Type of subject log (**required**). Fixes the fields every entry offers. Example: "Monitoring log", "Housing log". *See options below* |
| ``Subject`` | The subject of the log (**required**; fixed after creation). Must reference a [subject]({{"datamodel/stem/subject/"|absolute_url}}). |
| ``Protocol`` | Optional reusable [protocol]({{"datamodel/personal_attributes/protocol/"|absolute_url}}) for the whole log. Must have protocol type Subject log and either no subtype restrictions or include this log type. Only protocols where you are at least a Contributor are offered. |
| ``Description`` | What this series is for and how to read it (string; maximum length: 500 characters). Example: "Daily food consumption" |
| **Log Entries** | Multiple log entries can be added from the log's own page, each containing: |
| ``Date and time`` | Timestamp of the entry (datetime; format: YYYY-MM-DD HH:mm:ss). |
| ``Start and end time`` | Start and stop timestamps for duration-based logs (Housing, Deprivation, Habituation, Handling and Training logs). |
| ``Performed by`` | User who performed the observation. Can differ from the user who created the log. |
| ``Episode phase`` | When the log is linked to a [procedure episode]({{"datamodel/modules/procedureepisode/"|absolute_url}}), an entry can be placed in an episode phase: baseline, pre-procedure, induction, during, recovery, post-procedure or follow-up. |
| ``Notes`` | Notes for the entry (string; maximum length: 500 characters). |
| ``Type specific fields`` | Fields based on the log type, per entry. See the [Subject log types schema]({{"datamodel/schemas/subjectlog/"|absolute_url}}). |

## Types of subject logs

These are the available type options for subject logs. See the schema for field details: [Subject log types]({{"datamodel/schemas/subjectlog/"|absolute_url}}).

### Consumption Logs

`Food consumption log`: How much food the subject ate on each occasion. Entry field: food amount.

`Water consumption log`: How much water the subject drank on each occasion. Entry field: water amount.

### Deprivation Logs

`Food deprivation log`: A period of restricted food access. Entry fields: responsible person and protocol.

`Water deprivation log`: A period of restricted water access, most often supporting a motivated behavioral task. Entry fields: responsible person and protocol.

### Experimental Preparation Logs

`Habituation log`: Sessions acclimatizing the subject to the apparatus, handling or restraint. Entry field: method of habituation.

`Handling log`: Sessions in which the subject was handled to reduce stress. Entry field: method of handling.

`Training session log`: Task training sessions and how the subject performed. Entry fields: task, setup, reinforcement type and performance level.

### Genetic Logs

`Genotyping log`: Genotyping results, including which sample and assay produced them. Entry fields: genotype result, sample, assay or panel name, QC or confidence, and per-locus calls.

### Housing Logs

`Housing log`: Where and how the subject was housed, and when that changed. Entry fields: location, cage ID, cage type, light cycle and enrichment.

### Observation Logs

`Von Frey mechanical sensitivity test`: Mechanical withdrawal thresholds measured with calibrated filaments. Entry fields: stimulus location, stimulus force, response score (0-3) and repetitions.

`Hargreaves thermal sensitivity test`: Thermal withdrawal latency measured with a radiant heat source. Entry fields: stimulus location, withdrawal latency, cutoff latency, response score (0-3) and repetitions.

`Generic observation`: A recurring observation that does not fit a dedicated type. Name what is observed in the observation type field. Entry fields: observation type, observation and repetitions.

### Physical and Health Logs

`Monitoring log`: Routine measurement of body weight, intake and condition. This is the type to use for ordinary weight tracking. Each entry must record at least one value. Entry fields: weight, food consumed, water consumed, body condition score (1-5) and health observations.

`Welfare check`: A structured welfare assessment against defined endpoint criteria. Entry fields: clinical signs, actions taken, condition and demeanour (0-4), monitoring plan, pain scoring, wound site observation, endpoint criterion and whether humane endpoint criteria were met.

`Weighing log`: A weight-only stream. Legacy type: use Monitoring for new weight records. Existing logs stay readable.

`Wellness log`: A free-text health stream. Legacy type: use Welfare check for new health records. Existing logs stay readable.

## Submission form

The subject log submission form consists of two parts:

1. First part: Fill in the type and subject.
2. Second part: After clicking "Create and continue," you can add the protocol and description, and start recording entries.

## Permissions

Subject logs inherit permissions from projects via the subject associated with the log.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to subject logs, enabling you to read, edit, and delete subject logs through the API. Entries are added, changed and removed through the log's `add_entry`, `change_entry` and `remove_entry` actions. Learn more about the subject logs' fields and data structure on the [Subject logs API page]({{"api/modules/subjectlog/"|absolute_url}}).
