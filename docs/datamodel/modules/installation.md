---
layout: default
title: Equipments
parent: Modules
grand_parent: Data model
nav_order: 3
---

# Equipments model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Equipments refer to the setup and utilization of various devices and sensors designed to monitor, record, or manipulate environmental variables or subject responses. These equipments are critical for creating controlled experimental conditions, collecting data, and delivering stimuli. Each equipments type has specific applications and functions within setups. While equipments types share relationships, fields are tailored to the various equipments types. The types of equipments currently supported by BrainSTEM are listed below.

## Fields

| Field | Description |
|:------|:------------|
| `Type` | Type of equipments (**required**). Selected from predefined types. Example: "Video camera", "Microphone". *See options below* |
| `Setup` | The setup the equipments is installed in (**required**). Must reference an existing [setup]({{"datamodel/personal_attributes/experiment_setups/"|absolute_url}}). Example: "Behavior room A setup" |
| `Notes` | Notes about the equipments (string). Example: "Camera positioned at 45-degree angle" |
| `Date and time` | Date and time the equipments was performed. Example: "2024-03-22 09:00:00" |
| `Consumable` | Consumable used for the equipments. Example: "HD webcam model XYZ" |
| `Hardware device` | Hardware device used to perform the equipments. Example: "Recording computer #2" |
| `Coordinates system` | Coordinate system (**required**). Selected from predefined systems. Example: "External X-Y-Z Absolute". *See options below* |
| `Type details` | Type-specific fields. Fields vary by equipment type. Example: For camera - resolution, frame rate. *See options below* |

## Types of equipments

These are the available *Type* options for equipments:

- Microphone
- Video camera equipments
- Pressure sensor
- Thermometer
- Infrared camera
- Light sensor
- Light emitter
- Speaker

## Coordinate system options

Available Coordinate system options for equipments:

| Type | Description |
|:-----|:------------|
| External X-Y-Z Absolute | Absolute external coordinates. This can be used to describe, e.g., a camera's position in a room |

A detailed list of the fields in Coordinate system can be found on the [Coordinate systems page]({{"datamodel/schemas/coordinates/"|absolute_url}}).

## Permissions

Equipments inherit permissions through the setup associated with them.

Visit the [permissions page]({{"datamodel/permission/"|absolute_url}}) to learn more. 

## Equipments API access

The API allows for programmable access to equipments. Learn more about the equipments' fields and data structure on the [Equipments API page]({{"api/modules/installation/"|absolute_url}}).
