---
layout: default
title: Setups
parent: Personal attributes
grand_parent: Data model
nav_order: 3
---

# Dataset model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction 

Setups describe where experiments, procedures, or manipulations takes place. It also describes the environment of a recorded subject. Setups has physical dimensions and equipments associate with it.

## Dataset fields

| Field                | Description |
|:---------------------|:------------|
| `Name`                 | Name of the setup (**required**) |
| `Environment type`     | The type of environment the setup is of (**required**)|
| `Authenticated groups` | Groups that have change permissions for this setup (**required**) |
| `Description`          | Text description of the setup |
| `Image`				   | Image of the setup|
| `Public access`        | Determines if the setup is public or private |
| `Physical dimensions`  | Any physical dimensions used to describe the setup. Each dimension is a name value pair with any associated units or description. |

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

Setups define the overall permissions level for equipments. You manage permissions through the management tab, where you can assign individual users and groups access levels to a setup. Setup have four permission levels: membership (read access), contributors, managers, and owners.

Equipments inherit permissions from their associated setup.

Visit the [permissions page]({{"datamodel/permission/"|absolute_url}}) to learn more. 

## Dataset API access

The API allows for programmable access to setups, enabling you to read, edit, and delete Setups through the API. Learn more about the datasets' fields and data structure on the [Dataset API page]({{"api/personal_attributes/experimentalsetup/"|absolute_url}}).