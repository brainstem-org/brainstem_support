---
layout: default
title: Installation
parent: Modules
grand_parent: Data model
nav_order: 3
---

# Installation model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Installations refer to the setup and utilization of various devices and sensors designed to monitor, record, or manipulate environmental variables or subject responses. These installations are critical for creating controlled experimental conditions, collecting data, and delivering stimuli. Each installation type has specific applications and functions within experimental setups. While installation types share relationships, fields are tailored to the various installation types. The types of installations currently supported by BrainSTEM are listed below.

## Fields

| Field | Description |
|:------|:------------|
| `Type` | Type of installation (**required**). *See options below* |
| `Experimental setup` | The experimental setup the installation is installed in (**required**) |
| `Notes` | Notes about the installation (max length: 500 characters) |
| `Date and time` | Date and time the installation was performed (e.g., "2023-03-22") |
| `Consumable` | Consumable used for the installation |
| `Hardware device` | Hardware device used to perform the installation |
| `Coordinates system` | Coordinate system (**required**). *See options below* |
| `Type details` | Type-specific fields. *See options below* |

## Types of installations

These are the available *Type* options for Installation:

- Microphone
- Video camera installation
- Pressure sensor
- Thermometer
- Infrared camera
- Light sensor
- Light emitter
- Speaker

## Coordinate system options

Available Coordinate system options for Installation:

| Type | Description |
|:-----|:------------|
| External X-Y-Z Absolute | Absolute external coordinates. This can be used to describe, e.g., a camera's position in a room |

A detailed list of the fields in Coordinate system can be found on the [Coordinate systems page]({{"datamodel/schemas/coordinates/"|absolute_url}}).

## Permissions

Installations inherit permissions through the experimental setup associated with them.

Visit the [permissions page] to learn more.

## Installation API access

The API allows for programmable access to installations. Learn more about the installations' fields and data structure on the [Installation API page]({{"api/modules/installation/"|absolute_url}}).
