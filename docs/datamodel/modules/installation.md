---
layout: default
title: Installation
parent: Modules
grand_parent: Data model
nav_order: 2
---

# Installation model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction
Installations refer to the setup and utilization of various devices and sensors designed to monitor, record, or manipulate environmental variables or subject responses. These installations are critical for creating controlled experimental conditions, collecting data, and delivering stimuli. Each installation type has specific applications and functions within experimental setups. Installation types share relationships, but fields are tailored to the various installation-types. The types of installations currently supported by BrainSTEM are listed further down the page. An installation is described by the fields in the next section.

## Fields

| Field               | Description  |
|:--------------------|:-------------|
| Type                | the type of installation (**required**). *See options below* |
| Experimental setup  | The experimental setup the installation is installed in (**required**) |
| Notes               | Notes of the installation (max length: 500) |
| Date and time       | Date and time the installation was performed (e.g. "2023-03-22") |
| Consumable          | Consumable used for the installation |
| Hardware device     | Hardware device used to perform the installation |
| Coordinates system  | Coordinate system  (**required**). *See options below* |
| Type details        | There are also a number of type specific fields. *See options below* |

## Types of installations
These are the available _Type_ options for Installation:
- CameraInstallation
- InfraredCamera
- Microphone
- PressureSensor
- Thermostat

A detailed list of the type-specific fields, can be found in the [installation type page]({{"/datamodel/schemas/installations/"|absolute_url}}).

Below are the available Coordinates system options for Installation:

| Type                             | Description  |
|:---------------------------------|:-------------|
| External X-Y-Z Absolute          | Absolute external coordinates. This can be used to describe e.g. a cameras position in a room |

A detailed list of the fields in Coordinates system, can be found in the [Coordinate system page]({{"datamodel/schemas/coordinates/"|absolute_url}}).

## Permissions
Installations inherit permissions through the experimental setup associated with it.

Visit the [permissions page] to learn more.

## Installation API access
The API allows for programmable access to installations. Learn more about the installations' fields and data structure on the [Installation API page]({{"api/modules/installation/"|absolute_url}}).
