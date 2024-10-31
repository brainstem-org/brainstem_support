---
layout: default
title: Manipulation
parent: Modules
grand_parent: Data model
nav_order: 5
---

# Manipulation model
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

The manipulation model describes temporal manipulations performed in a session. Manipulations are ways to perturb natural brain dynamics. The types of manipulations currently supported by BrainSTEM are listed below. A Manipulation is described by the fields in the next section.

## Fields

| Field | Description |
|:------|:------------|
| `Session` | Session of the manipulation (**required**) |
| `Type` | Type of manipulation (**required**). *See options below* |
| `Procedures` | Related subject procedures (**required**) |
| `Notes` | Notes about the manipulation (max length: 500 characters) |
| `Hardware device` | Hardware device used to perform the manipulation |
| `Type details` | Type-specific fields. *See options below* |

## Types of manipulations

These are the available *Type* options for manipulations:

- Deep brain stimulation (DBS)
- Electromagnetic field stimulation
- Electrical stimulation
- Liquid perturbation
- Micro perfusion
- Optogenetic stimulation
- Pharmacological inhalation
- Pharmacological injection
- Pharmacological superfusion
- Sound stimulation
- Thermal perturbation
- Transcranial Electrical Stimulation
- Transcranial Magnetic Stimulation (TMS)
- Ultrasound stimulation

A detailed list of the type-specific fields can be found on the [manipulation types page]({{"datamodel/schemas/manipulation/"|absolute_url}}).

## Permissions

Manipulations inherit permissions through the session associated with them.

Visit the [permissions page] to learn more.

## Manipulation API access

The API allows for programmable access to manipulations. Learn more about the manipulations' fields and data structure on the [Manipulation API page]({{"api/modules/manipulation/"|absolute_url}}).
