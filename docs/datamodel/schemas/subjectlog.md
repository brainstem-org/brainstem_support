---
layout: default
title: Subject log types
parent: Schemas
grand_parent: Data model
nav_order: 5
---

# Subject log types
{: .no_toc}

Multiple log types are available to track and record various aspects of subject care, behavior, and experimental conditions.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

# Subject log types

Multiple log types are available to track and record various aspects of subject care, behavior, and experimental conditions. Each log type captures specific information critical for maintaining subject welfare and experimental integrity.

## Diet And Consumption Logs

### Food consumption log

Records the amount and type of food consumed by the subject. This information is crucial for studies examining the effects of diet on health, behavior, or disease progression.

| Field | Description |
|:------|:------------|
| `Date time` | Timestamp of the food consumption measurement (datetime). Records when the measurement was taken |
| `Food amount (grams)` | Amount of food consumed (float, ≥ 0; measured in grams). Required field that tracks precise food intake |
| `Notes` | Additional observations or comments (string). Provides context for the measurement |

### Water consumption log

Details the amount of water consumed by the subject. Monitoring water intake is essential for studies related to hydration, kidney function, or the effects of various substances on thirst.

| Field | Description |
|:------|:------------|
| `Date time` | Timestamp of the measurement (datetime). Records when consumption was measured |
| `Water amount (mL)` | Volume of water consumed (float, ≥ 0; measured in milliliters). Required field tracking fluid intake |
| `Notes` | Additional observations (string). Provides context for the measurement |

## Deprivation Logs

### Food deprivation log

Documents periods when food is withheld from the subject. Food deprivation can be used as a motivational tool in behavioral experiments or to study the physiological and psychological effects of fasting.

| Field | Description |
|:------|:------------|
| `Notes` | Additional relevant information (string). Captures any deviations or observations |
| `Responsible person (name and phone number)` | Contact information of the person overseeing the deprivation (string). Required field for accountability |
| `Protocol` | Description of the food deprivation procedure (string). Details the specific protocol being followed |
| `Start time` | Beginning of the food deprivation period (datetime). Required field marking when deprivation begins |
| `End time` | Conclusion of the food deprivation period (datetime). Marks when regular feeding resumes |

### Water deprivation log

Notes periods during which water is withheld from the subject. Similar to food deprivation, water deprivation can be used to study the effects of hydration status.

| Field | Description |
|:------|:------------|
| `Notes` | Additional relevant information (string). Captures any deviations or observations |
| `Responsible person (name and phone number)` | Contact information of the person overseeing the deprivation (string). Required field for accountability |
| `Protocol` | Description of the water deprivation procedure (string). Details the specific protocol followed |
| `Start time` | Beginning of the water deprivation period (datetime). Required field marking when deprivation begins |
| `End time` | Conclusion of the water deprivation period (datetime). Marks when regular water access resumes |

## Housing And Environment Logs

### Housing log

Keeps track of the subject's living conditions, including cage type, location, and environmental enrichments. This log helps ensure consistent and ethical housing standards.

| Field | Description |
|:------|:------------|
| `Notes` | Additional housing-related information (string). Records any relevant observations |
| `Location` | Physical location of the subject's housing (string). Specifies the exact housing unit location |
| `Cage ID` | Unique identifier for the housing cage (string). Enables precise tracking of housing units |
| `Cage type` | Specification of the cage model used (string). Details the exact cage configuration |
| `Light cycle` | Description of the lighting schedule (string). Specifies normal or reversed light cycles |
| `Enrichment` | Environmental enrichment details (string). Lists items provided for subject welfare |
| `Start time` | Beginning of the housing period (datetime). Required field marking when housing begins |
| `End time` | Conclusion of the housing period (datetime). Marks when housing arrangement changes |

## Physical And Health Logs

### Weighing log

Records the subject's body weight over time. Regular weighing is critical for monitoring health, growth, and the effects of experimental treatments.

| Field | Description |
|:------|:------------|
| `Date time` | Timestamp of the weighing (datetime). Records when measurement was taken |
| `Weight (grams)` | Subject's measured weight (float, ≥ 0; measured in grams). Required field tracking body mass |
| `Notes` | Additional observations (string). Provides context for the measurement |

### Wellness log

Documents observations related to the subject's general health and well-being, including behavior, physical appearance, and signs of distress or illness.

| Field | Description |
|:------|:------------|
| `Date time` | Timestamp of the wellness check (datetime). Records when assessment was made |
| `Wellness` | Description of the subject's health status (string). Required field documenting overall condition |
| `Notes` | Additional health-related observations (string). Captures detailed observations |

## Subject log schemas API access

The API allows for programmable access to Subject logs, enabling you to read, edit, and delete subject logs through the API. Learn more about the subject logs' fields and data structure on the [Subject log API page]({{"api/schemas/subjectlog/"|absolute_url}}).