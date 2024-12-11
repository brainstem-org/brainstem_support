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

## Electrical and Magnetic Stimulation
- Deep brain stimulation (DBS)
- Electrical stimulation
- Electromagnetic field stimulation
- Transcranial Electrical Stimulation
- Transcranial Magnetic Stimulation (TMS)

## Optical, Thermal, and Ultrasound Stimulation
- Optogenetic stimulation
- Thermal perturbation
- Ultrasound stimulation

## Chemical and Pharmacological Perturbations
- Liquid perturbation
- Micro perfusion
- Pharmacological injection
- Pharmacological superfusion
- Pharmacological inhalation

## Sensory Stimulation
- Sound stimulation

A detailed list of the type-specific fields can be found on the [manipulation types page]({{"datamodel/schemas/manipulation/"|absolute_url}}).

## Permissions

Manipulations inherit permissions through the session associated with them.

Visit the [permissions page]({{"datamodel/permission/"|absolute_url}}) to learn more. 

## Manipulation API access

The API allows for programmable access to manipulations. Learn more about the manipulations' fields and data structure on the [Manipulation API page]({{"api/modules/manipulation/"|absolute_url}}).
