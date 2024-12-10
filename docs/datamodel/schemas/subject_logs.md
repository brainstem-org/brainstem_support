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

### Food consumption log

Records the amount and type of food consumed by the subject. This information is crucial for studies examining the effects of diet on health, behavior, or disease progression.

| Field | Description |
|:------|:------------|
| `Date time` | Date and time of the food consumption measurement |
| `Food amount (grams)` | Amount of food consumed in grams (**required**) |
| `Notes` | Additional notes about the food consumption |

### Food deprivation log

Documents periods when food is withheld from the subject. Food deprivation can be used as a motivational tool in behavioral experiments or to study the physiological and psychological effects of fasting.

| Field | Description |
|:------|:------------|
| `Notes` | Additional notes about the food deprivation |
| `Responsible person (name and phone number)` | Name and contact information of the person responsible for the food deprivation (**required**) |
| `Protocol` | Description of the food deprivation protocol |
| `Start time` | Start time of the food deprivation period (**required**) |
| `End time` | End time of the food deprivation period |

### Housing log

Keeps track of the subject's living conditions, including the cage typehousing, location, light cycle, and any environmental enrichments. This log helps ensure that housing conditions remain consistent and meet ethical standards.

| Field | Description |
|:------|:------------|
| `Notes` | Additional notes about the housing |
| `Location` | Location of the housing |
| `Cage ID` | Identifier for the cage |
| `Cage type` | Type of cage used |
| `Light cycle` | Description of the light cycle in the housing |
| `Enrichment` | Description of any enrichment provided in the housing |
| `Start time` | Start time of the housing period (**required**) |
| `End time` | End time of the housing period |

### Water consumption log

Details the amount of water consumed by the subject. Monitoring water intake is essential for studies related to hydration, kidney function, or the effects of various substances on thirst and water balance.

| Field | Description |
|:------|:------------|
| `Date time` | Date and time of the water consumption measurement |
| `Water amount (mL)` | Amount of water consumed in milliliters (**required**) |
| `Notes` | Additional notes about the water consumption |

### Water deprivation log

Notes periods during which water is withheld from the subject. Similar to food deprivation, water deprivation can be used to study the effects of hydration status on various physiological and behavioral outcomes.

| Field | Description |
|:------|:------------|
| `Notes` | Additional notes about the water deprivation |
| `Responsible person (name and phone number)` | Name and contact information of the person responsible for the water deprivation (**required**) |
| `Protocol` | Description of the water deprivation protocol |
| `Start time` | Start time of the water deprivation period (**required**) |
| `End time` | End time of the water deprivation period |

### Weighing log

Records the subject's body weight over time. Regular weighing is critical for monitoring health, growth, and the effects of experimental treatments on body mass.

| Field | Description |
|:------|:------------|
| `Date time` | Date and time of the weighing |
| `Weight (grams)` | Weight of the subject in grams (**required**) |
| `Notes` | Additional notes about the weighing |

### Wellness log

Documents observations related to the subject's general health and well-being, including behavior, physical appearance, signs of distress, or illness. This log is essential for ensuring the ethical treatment of research subjects and for interpreting the effects of experimental manipulations on overall health.

| Field | Description |
|:------|:------------|
| `Date time` | Date and time of the wellness check |
| `Wellness` | Description of the subject's wellness status (**required**) |
| `Notes` | Additional notes about the wellness check |

## Subject log API access

The API allows for programmable access to Subject logs, enabling you to read, edit, and delete subject logs through the API. Learn more about the subject logs' fields and data structure on the [Subject log API page]({{"api/modules/subjectlog/"|absolute_url}}).