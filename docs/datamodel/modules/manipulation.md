---
layout: default
title: Manipulation
parent: Modules
grand_parent: Data model
nav_order: 3
---

# Manipulation model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction
The manipulation model describes temporal manipulations performed in a dataset. Manipulations are ways to perturb the natural brain dynamics. The types of manipulations that are currently supported by BrainSTEM are listed further down the page. A Manipulation is described by the fields in the next section.

## Fields

| Field           | Description  |
|:----------------|:-------------|
| Dataset         | Dataset of the manipulation  (**required**) |
| Type            | Type of manipulation (**required**). *See options below* |
| Procedures      | Related subject procedures (**required**) |
| Notes           | Notes of the manipulation (max length: 500) |
| Hardware device | Hardware device used to perform the manipulation |
| Type details    | There are also a number of type specific fields. *See options below* |

## Types of manipulations
These are the available _Type_ options for manipulations:
- Deep brain stimulation (DBS)
- Electromagnetic field stimulation
- Electrical stimulation
- Liquid perturbation
- Micro perfusion
- Optogenetical stimulation
- Pharmacological inhalation
- Pharmacological injection
- Pharmacological superfusion
- Sound stimulation
- Thermal perturbation
- Transcranial Electrical Stimulation
- Transcranial Magnetic Stimulation (TMS)
- Ultra sound stimulation

A detailed list of the type-specific fields, can be found in the [manipulation type page]({{"/datamodel/schemas/manipulation/"|absolute_url}}).


## Permissions
Manipulation inherit permissions through the dataset associated with it.

Visit the [permissions page] to learn more.


## Manipulation API access
The API allows for programmable access to manipulations. Learn more about the manipulations' fields and data structure on the [Manipulation API page]({{"api/modules/manipulation/"|absolute_url}}). 
