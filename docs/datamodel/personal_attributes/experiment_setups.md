---
layout: default
title: Experimental setups
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

Experimental setups describe where experiments, procedures, or manipulations takes place. It also describes the environment of a recorded subject. Experimental setups has physical dimensions and installations associate with it.

## Dataset fields

| Field                | Description |
|:---------------------|:------------|
| `Name`                 | Name of the experimental setup (**required**) |
| `Environment type`     | The type of environment the setup is of (**required**)|
| `Authenticated groups` | Groups that have change permissions for this experimental setup (**required**) |
| `Description`          | Text description of the experimental setup |
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

Experimental setups define the overall permissions level for installations. You manage permissions through the management tab, where you can assign individual users and groups access levels to a Experimental setup. Experimental setup have four permission levels: membership (read access), change permissions, managers, and owners.

Visit the [permissions page] to learn more. 

## Dataset API access

The API allows for programmable access to Experimental setups, enabling you to read, edit, and delete Experimental setups through the API. Learn more about the datasets' fields and data structure on the [Dataset API page]({{"api/personal_attributes/experimentalsetup/"|absolute_url}}).