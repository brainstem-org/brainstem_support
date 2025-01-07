---
layout: default
title: Setups
parent: Personal attributes
grand_parent: Data model
nav_order: 3
---

# Setups model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction 

Setups describe where experiments, procedures, or manipulations takes place. It also describes the environment of a recorded subject. Setups has physical dimensions and equipment associate with it.

## Session fields

| Field                | Description |
|:---------------------|:------------|
| `Name`                 | Name of the setup (**required**; string; maximum length: 50 characters). Example: "Behavior Room A - Setup 1" |
| `Environment type`     | The type of environment the setup is of (**required**). Example: "Linear track"|
| `Authenticated groups` | Groups that have change permissions for this setup (**required**). Example: "Behavior Core Team" |
| `Description`          | Rich text description of the setup. Can include uploaded images. Example: "Linear track setup with two reward ports and tracking cameras..." |
| `Image`				   | Image of the setup. Example: "setup1_overview.jpg"|
| `Public access`        | Determines if the setup is public or private. Example: "False" for private access |
| `Physical dimensions`  | Any physical dimensions used to describe the setup. Each dimension is a name value pair with any associated units or description. Example: {"length": "200 cm", "width": "10 cm", "height": "15 cm"} |

## Types of environment type

- Barnes maze
- Circular track
- Elevated plus maze
- Elevated zero maze
- Figure eight maze
- Forced swim test
- Head-fixed disc
- Homecage
- Linear Track
- Morris water maze
- Open field environment
- Radial arm maze
- Running wheel
- Sleepbox
- Square cage
- Theta maze
- T-maze
- Y-maze
- Other

## Permissions

Setups define the overall permissions level for equipment. You manage permissions through the management tab, where you can assign individual users and groups access levels to a setup. Setup have four permission levels: membership (read access), contributors, managers, and owners.

Equipment inherit permissions from their associated setup.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## Setups API access

The API allows for programmable access to setups, enabling you to read, edit, and delete Setups through the API. Learn more about the sessions' fields and data structure on the [Setups API page]({{"api/personal_attributes/setup/"|absolute_url}}).
