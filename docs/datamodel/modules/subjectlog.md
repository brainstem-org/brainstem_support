---
layout: default
title: Subject logs
parent: Subjects
grand_parent: Data model
nav_order: 2
---

# Subject log model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Subject logs refers to records that track various aspects of the subjects' living conditions, physiological states, and behaviors over time. These logs are essential for ensuring the welfare of subjects, maintaining consistent experimental conditions, and accurately interpreting the effects of interventions.

## Fields

| Field | Description |
|:------|:------------|
| ``Type`` | Type of subject logs (**required**). Selected from predefined types. Example: "Food consumption log", "Housing log". *See options below* |
| ``Description`` | Description of the subject logs (optional). Can be left empty (string, max 500 characters). Example: "Daily food consumption" |
| ``Subject`` | The subject of the log (**required**). Must reference a [subject]({{"datamodel/stem/subject/"|absolute_url}}). Example: "Mouse_01" |
| **Log Entries** | Multiple log entries can be added, each containing: |
| ``Date and time`` | Timestamp for each log entry. Used for simple timestamp logs (datetime). Format: YYYY-MM-DD HH:mm:ss. Example: "2024-03-15 14:30:00" |
| ``Start and end time`` | Start and stop timestamps for duration-based logs (datetime). Used for Housing, Deprivation, Habituation, Handling, and Training logs. Format: YYYY-MM-DD HH:mm:ss. Example: Start: "2024-03-15 14:30:00", End: "2024-03-15 15:30:00" |
| ``Performed by`` | User who performed the action recorded in this entry (optional). Can be different from the user who created the log. Example: "Dr. Smith" |
| ``Type details`` | Type-specific fields for each entry in the log. Fields vary by type. Example: For food consumption log - food amount in grams. *See options below* |
| ``Notes`` | Notes about the subject logs for each entry in the log (string, max 500 characters). Example: "Subject appeared healthy during feeding" |

## Types of subject logs

These are the available type options for subject logs:

See the schema for field details: [Subject logs types]({{"datamodel/schemas/subjectlog/"|absolute_url}}).

### Diet and Consumption Logs

`Food consumption log`: Records amount and type of food consumed to support diet, health, and intervention analyses.

`Water consumption log`: Records water intake to monitor hydration and assess intervention effects.

### Deprivation Logs

`Food deprivation log`: Logs periods without food for motivation paradigms or fasting‑related studies.

`Water deprivation log`: Logs periods without water to study hydration effects and behavioral outcomes.

### Housing and Environment Logs

`Housing log`: Tracks living conditions (cage, housing, location, light cycle, enrichment) for consistency and welfare.

### Observation Logs

`Von Frey Mechanical sensitivity test`: Logs mechanical sensitivity testing with Von Frey filaments; measures withdrawal thresholds for tactile/pain sensitivity.

`Hargreaves thermal sensitivity test`: Logs thermal sensitivity via radiant heat; records withdrawal latency for pain and hyperalgesia assessment.

`Generic observation`: Flexible welfare/behavior observations not covered elsewhere (e.g., pain scores, grooming, exploration).

### Physical and Health Logs

`Weighing log`: Records body weight over time to monitor health, growth, and treatment effects.

`Wellness log`: Logs general health and well‑being indicators (behavior, appearance, distress/illness) for oversight and analysis.

### Experimental Preparation Logs

`Habituation log`: Records acclimation sessions to environments, equipment, or procedures to reduce stress and improve data quality.

`Handling log`: Logs handling sessions for acclimatization, health checks, or procedural readiness.

`Training session log`: Records training sessions for task learning and conditioning (shaping, reinforcement, skill acquisition).

### Genetic Logs

`Genotyping log`: Records genotype testing outcomes and related metadata for subject identification and experimental grouping.




## Submission form

The subject logs submission form consists of two parts:

1. First part: Fill in the required fields.
2. Second part: After clicking "Create and continue," you can edit all fields of the entry.


## Permissions

Subject logs inherit permissions from projects via the subject associated with the entry.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more.

## API access

The API allows for programmable access to Subject logs, enabling you to read, edit, and delete subject logs through the API. Learn more about the subject logs' fields and data structure on the [Subject logs API page]({{"api/modules/subjectlog/"|absolute_url}}).
