---
layout: default
title: Equipment
parent: Modules
grand_parent: Data model
nav_order: 3
---

# Equipment model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Equipment refer to the setup and utilization of various devices and sensors designed to monitor, record, or manipulate environmental variables or subject responses. These equipment are critical for creating controlled experimental conditions, collecting data, and delivering stimuli. Each equipment type has specific applications and functions within setups. While equipment types share relationships, fields are tailored to the various equipment types. The types of equipment currently supported by BrainSTEM are listed below.

## Fields

| Field | Description |
|:------|:------------|
| `Type` | Type of equipment (**required**). Selected from predefined types. Example: "Video camera", "Microphone". *See options below* |
| `Setup` | The setup the equipment is installed in (**required**). Must reference an existing [setup]({{"datamodel/personal_attributes/setup/"|absolute_url}}). Example: "Behavior room A setup" |
| `Notes` | Notes about the equipment (string). Example: "Camera positioned at 45-degree angle" |
| `Date and time` | Date and time the equipment was performed. Example: "2024-03-22 09:00:00" |
| `Consumable` | Consumable used for the equipment. Example: "HD webcam model XYZ" |
| `Hardware device` | Hardware device used to perform the equipment. Example: "Recording computer #2" |
| `Coordinates system` | Coordinate system (**required**). Selected from predefined systems. Example: "External X-Y-Z Absolute". *See options below* |
| `Type details` | Type-specific fields. Fields vary by equipment type. Example: For camera - resolution, frame rate. *See options below* |

## Types of equipment

{% include_relative ../../type_descriptions/equipment_types.md %}


## Coordinate system options

Available Coordinate system options for equipment:

| Type | Description |
|:-----|:------------|
| External X-Y-Z Absolute | Absolute external coordinates. This can be used to describe, e.g., a camera's position in a room |

A detailed list of the fields in Coordinate system can be found on the [Coordinate systems page]({{"datamodel/schemas/coordinates/"|absolute_url}}).

## Permissions

Equipment inherit permissions through the setup associated with them.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## Equipment API access

The API allows for programmable access to equipment. Learn more about the equipment' fields and data structure on the [Equipment API page]({{"api/modules/equipment/"|absolute_url}}).
