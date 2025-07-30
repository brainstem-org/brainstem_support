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
| `Type` | Type of subject logs (**required**). Selected from predefined types. Example: "Food consumption log", "Housing log". *See options below* |
| `Subject` | The subject of the log (**required**). Must reference a [subject]({{"datamodel/stem/subject/"|absolute_url}}). Example: "Silicon probe implant #A123" |
| `Description` | Description of the subject logs. Can be left empty (string). Example: "Daily food consumption" |
| `Date and time` | Timestamp for each log-entry. There are two types of subject logs with either simple timestamps or time period defined by a start and an end timestamps. Example: "2024-03-15 14:30:00" |
| `Start and end time` | Start and stop timestamp of each log-entry. Example: "2024-03-15 14:30:00" |
| `Type details` | Type-specific fields for each entry in the log. Fields vary by type. Example: For impedance log - impedance values in kOhm. *See options below* |
| `Notes` | Notes about the subject logs for each entry in the log (string). Example: "Observed slight increase in impedance values" |

## Types of subject logs

These are the available *Type* options for Subject logs:

- `Food consumption log`: Records the amount and type of food consumed by the subject. This information is crucial for studies examining the effects of diet on health, behavior, or disease progression.
- `Food deprivation log`: Documents periods when food is withheld from the subject. Food deprivation can be used as a motivational tool in behavioral experiments or to study the physiological and psychological effects of fasting.
- `Housing log`: Keeps track of the subject's living conditions, including the cage type, housing, location, light cycle, and any environmental enrichment. This log helps ensure that housing conditions remain consistent and meet ethical standards.
- `Water consumption log`: Details the amount of water consumed by the subject. Monitoring water intake is essential for studies related to hydration, kidney function, or the effects of various substances on thirst and water balance.
- `Water deprivation log`: Notes periods during which water is withheld from the subject. Similar to food deprivation, water deprivation can be used to study the effects of hydration status on various physiological and behavioral outcomes.
- `Weighing log`: Records the subject's body weight over time. Regular weighing is critical for monitoring health, growth, and the effects of experimental treatments on body mass.
- `Wellness log`: Documents observations related to the subject's general health and well-being, including behavior, physical appearance, signs of distress, or illness. This log is essential for ensuring the ethical treatment of research subjects and for interpreting the effects of experimental manipulations on overall health.
- `Von Frey test`: Records mechanical sensitivity testing using Von Frey filaments. This standardized test measures withdrawal responses to graded mechanical stimuli and is commonly used to assess pain sensitivity, tactile thresholds, and the effects of analgesic treatments.
- `Hargreaves test`: Documents thermal sensitivity testing using the Hargreaves method. This test measures withdrawal latencies to radiant heat stimuli applied to the paw and is a standard assessment for thermal pain sensitivity and hyperalgesia.
- `Generic observation`: Captures flexible behavioral and welfare observations not covered by specific log types. This includes pain scoring, grooming behaviors, exploration patterns, and other custom observations important for research protocols.

A detailed list of the type-specific fields can be found on the [subject logs types page]({{"datamodel/schemas/subjectlog/"|absolute_url}}).


## Submission form

The subject logs submission form consists of two parts:
1. First part: Fill in the required fields.
2. Second part: After clicking "Create and continue," you can edit all fields of the entry.

## Permissions

Subject logs inherit permissions from projects via the subject and then the subject associated with the entry.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## API access

The API allows for programmable access to Subject logs, enabling you to read, edit, and delete subject logss through the API. Learn more about the subject logs' fields and data structure on the [Subject logs API page]({{"api/modules/subjectlog/"|absolute_url}}).
