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

Multiple log types are available to track and record various aspects of subject care, behavior, and experimental conditions. Each log type captures specific information critical for maintaining subject welfare and experimental integrity.

## Diet and Consumption Logs

### Food consumption log

Records the amount of food consumed by the subject. This information is crucial for studies examining the effects of diet on health, behavior, or disease progression.

| Field | Description |
|:------|:------------|
| `Food amount` | Amount of food consumed (float, ≥ 0). Required field that tracks precise food intake |

### Water consumption log

Details the amount of water consumed by the subject. Monitoring water intake is essential for studies related to hydration, kidney function, or the effects of various substances on thirst.

| Field | Description |
|:------|:------------|
| `Water amount` | Volume of water consumed (float, ≥ 0). Required field tracking fluid intake |

## Deprivation Logs

### Food deprivation log

Documents periods when food is withheld from the subject. Food deprivation can be used as a motivational tool in behavioral experiments or to study the physiological and psychological effects of fasting.

| Field | Description |
|:------|:------------|
| `Responsible person` | Contact information of the person overseeing the deprivation (string). Required field for accountability |
| `Protocol` | Description of the food deprivation procedure (string). Details the specific protocol being followed |

### Water deprivation log

Notes periods during which water is withheld from the subject. Similar to food deprivation, water deprivation can be used to study the effects of hydration status.

| Field | Description |
|:------|:------------|
| `Responsible person` | Contact information of the person overseeing the deprivation (string). Required field for accountability |
| `Protocol` | Description of the water deprivation procedure (string). Details the specific protocol followed |

## Housing and Environment Logs

### Housing log

Keeps track of the subject's living conditions, including cage type, location, and environmental enrichments. This log helps ensure consistent and ethical housing standards.

| Field | Description |
|:------|:------------|
| `Location` | Physical location of the subject's housing (string). Specifies the exact housing unit location |
| `Cage ID` | Unique identifier for the housing cage (string). Enables precise tracking of housing units |
| `Cage type` | Specification of the cage model used (string). Details the exact cage configuration |
| `Light cycle` | Description of the lighting schedule (string). Specifies normal or reversed light cycles |
| `Enrichment` | Environmental enrichment details (string). Lists items provided for subject welfare |

## Observation Logs

### Von Frey Mechanical sensitivity test

Documents mechanical sensitivity testing using Von Frey filaments to assess tactile responses and sensory thresholds.

| Field | Description |
|:------|:------------|
| `Stimulus location` | Anatomical location where the Von Frey filament was applied (string; enum). Options include: Left hind paw, Right hind paw, Left forepaw, Right forepaw, Face (left), Face (right), Tail, Other |
| `Stimulus force` | Force of the Von Frey filament used for mechanical stimulation (float, ≥ 0). Required field |
| `Response score` | Categorical assessment of behavioral response to stimulation (integer, 0-3). Required field. 0: No response, 1: Slight movement, 2: Strong withdrawal, 3: Flinching or escape |
| `Repetitions` | Number of repetitions of Von Frey stimulation at the given location (integer, ≥ 1; default: 10) |

### Hargreaves thermal sensitivity test

Documents thermal sensitivity testing using the Hargreaves method to assess responses to heat stimuli.

| Field | Description |
|:------|:------------|
| `Stimulus location` | Anatomical location where the thermal stimulus was applied (string; enum). Options include: Left hind paw, Right hind paw, Left forepaw, Right forepaw, Face (left), Face (right), Tail, Other |
| `Withdrawal latency` | Time from stimulus onset to paw withdrawal (float, ≥ 0). Required field measuring reaction time |
| `Cutoff latency` | Maximum allowable latency before automatic termination to prevent tissue damage (float, ≥ 0; default: 20) |
| `Response score` | Categorical assessment of behavioral response (integer, 0-3). Required field. 0: No response, 1: Delayed movement, 2: Normal withdrawal, 3: Exaggerated or escape behavior |
| `Repetitions` | Number of repeated Hargreaves trials at the given location (integer, ≥ 1; default: 3) |

### Generic observation

Documents general observations about the subject that don't fit into specific categories, allowing for flexible recording of various events or behaviors.

| Field | Description |
|:------|:------------|
| `Observation type` | Type or category of observation being recorded (string; enum). Options include: Pain score, Grooming, Exploration, Freezing, Facial expression, Unusual behavior, Other. Required field |
| `Observation` | Description of the observed behavior (string). Required field providing full context |
| `Repetitions` | How many times this observation was recorded under the same condition (integer, ≥ 1; default: 1) |

## Physical and Health Logs

### Weighing log

Records the subject's body weight over time. Regular weighing is critical for monitoring health, growth, and the effects of experimental treatments.

| Field | Description |
|:------|:------------|
| `Weight` | Subject's measured weight (float, ≥ 0). Required field tracking body mass |

### Wellness log

Documents observations related to the subject's general health and well-being, including behavior, physical appearance, and signs of distress or illness.

| Field | Description |
|:------|:------------|
| `Wellness` | Description of the subject's health status (string). Required field documenting overall condition |

## Experimental Preparation Logs

### Habituation log

Records habituation procedures used to acclimate subjects to handling or experimental conditions, reducing stress and improving data quality.

| Field | Description |
|:------|:------------|
| `Method of habituation` | Technique used for habituation (string). Examples include: tail lift, cupping, glove |

### Handling log

Documents handling sessions and techniques used to manage subjects, ensuring consistent and humane treatment.

| Field | Description |
|:------|:------------|
| `Method of handling` | Technique used for handling the subject (string). Examples include: tail lift, cupping, glove |

### Training session log

Records training sessions conducted to prepare subjects for experimental tasks or procedures.

| Field | Description |
|:------|:------------|
| `Task of the training` | Specific task or behavior being trained (string). Describes the training objective |
| `Setup of the training` | Configuration or environment used for training (string). Describes the training setup |
| `Reinforcement type` | Type of reinforcement used during training (string). Examples include: food, water, open-loop/closed loop |
| `The performance level` | Assessment of subject's performance during training (string). Describes how well the subject performs the task |

## API access

The API allows for programmable access to Subject logs, enabling you to read, edit, and delete subject logs through the API. Learn more about the subject logs' fields and data structure on the [Subject log API page]({{"api/schemas/subjectlog/"|absolute_url}}).