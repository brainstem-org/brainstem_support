---
layout: default
title: Subject logs
parent: Schemas
grand_parent: Data model
nav_order: 5
---

# Subject logs model
{: .no_toc}

Multiple log types are available to track and record various aspects of subject care, behavior, and experimental conditions.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

### Food consumption log

| Field | Description |
|:------|:------------|
| `Date time` | Date and time of the food consumption measurement |
| `Food amount (grams)` | Amount of food consumed in grams (**required**) |
| `Notes` | Additional notes about the food consumption |

### Food deprivation log

| Field | Description |
|:------|:------------|
| `Notes` | Additional notes about the food deprivation |
| `Responsible person (name and phone number)` | Name and contact information of the person responsible for the food deprivation (**required**) |
| `Protocol` | Description of the food deprivation protocol |
| `Start time` | Start time of the food deprivation period (**required**) |
| `End time` | End time of the food deprivation period |

### Housing log

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

| Field | Description |
|:------|:------------|
| `Date time` | Date and time of the water consumption measurement |
| `Water amount (mL)` | Amount of water consumed in milliliters (**required**) |
| `Notes` | Additional notes about the water consumption |

### Water deprivation log

| Field | Description |
|:------|:------------|
| `Notes` | Additional notes about the water deprivation |
| `Responsible person (name and phone number)` | Name and contact information of the person responsible for the water deprivation (**required**) |
| `Protocol` | Description of the water deprivation protocol |
| `Start time` | Start time of the water deprivation period (**required**) |
| `End time` | End time of the water deprivation period |

### Weighing log

| Field | Description |
|:------|:------------|
| `Date time` | Date and time of the weighing |
| `Weight (grams)` | Weight of the subject in grams (**required**) |
| `Notes` | Additional notes about the weighing |

### Wellness log

| Field | Description |
|:------|:------------|
| `Date time` | Date and time of the wellness check |
| `Wellness` | Description of the subject's wellness status (**required**) |
| `Notes` | Additional notes about the wellness check |

## Subject log API access

The API allows for programmable access to Subject logs, enabling you to read, edit, and delete subject logs through the API. Learn more about the subject logs' fields and data structure on the [Subject log API page]({{"api/modules/subjectlog/"|absolute_url}}).