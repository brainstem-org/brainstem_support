---
layout: default
title: Manipulations
parent: Sessions
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

The manipulations model describes temporal manipulations performed in a session. Manipulations are ways to perturb natural brain dynamics. The types of manipulations currently supported by BrainSTEM are listed below. A Manipulation is described by the fields in the next section.

## Fields

| Field | Description |
|:------|:------------|
| `Session` | Session of the manipulation (**required**). Must reference an existing [session]({{"datamodel/stem/session/"|absolute_url}}). Example: "Optogenetic stimulation session #2" |
| `Type` | Type of manipulation (**required**). Selected from predefined types. Example: "Optogenetic stimulation". *See options below* |
| `Procedures` | Related subject procedures (**required**). Must reference existing [procedures]({{"datamodel/modules/procedure/"|absolute_url}}). Example: "Optic fiber implant #B789" |
| `Setup` | The setup where the manipulation was performed (**required**). Must reference an existing [setup]({{"datamodel/personal_attributes/setup/"|absolute_url}}). Example: "Behavior Room A" |
| `Equipment` | Equipment used for the manipulation (**required**). Must reference existing [equipment]({{"datamodel/modules/equipment/"|absolute_url}}). Example: "LED driver #1" |
| `Notes` | Notes about the manipulation (string). Example: "20Hz stimulation protocol completed successfully" |
| `Type details` | Type-specific fields. Fields vary by manipulation type. Example: For optogenetics - power, frequency, duration. *See options below* |

## Types of manipulations

These are the available *Type* options for manipulations:

### Electrical and Magnetic Stimulation:
- `Deep brain stimulation (DBS)`: A neurosurgical procedure that involves implanting electrodes in specific areas of the brain to deliver electrical impulses. It's used to treat a variety of neurological conditions, including Parkinson's disease and essential tremor.
- `Electrical stimulation`: The application of electrical currents to neurons or neural tissues to activate or inhibit neural activity. This broad category can include invasive methods like intracortical microstimulation or non-invasive approaches like transcranial direct current stimulation (tDCS).
- `Electromagnetic field stimulation`: Involves the use of magnetic or electric fields to modulate neuronal activity. This non-invasive method can influence brain function and is studied for therapeutic potential in psychiatric and neurological disorders.
- `Transcranial Electrical Stimulation`: A non-invasive method that applies electrical currents through the scalp and skull to modulate neuronal activity in the brain, used for research and therapeutic purposes.
- `Transcranial Magnetic Stimulation (TMS)`: A non-invasive technique that uses magnetic fields to induce electrical currents in the brain, capable of modulating neural activity and used for both research and treatment of various neurological and psychiatric conditions.

### Optical, Thermal, and Ultrasound Stimulation:
- `Optogenetical stimulation`: Uses light to control neurons that have been genetically modified to express light-sensitive ion channels. This precise method enables the activation or inhibition of specific neuronal populations with high temporal resolution.
- `Thermal perturbation`: The application of heat or cold to neural tissue to study the effects of temperature changes on neural activity, function, or structural integrity.
- `Ultrasound stimulation`: Utilizes high-frequency sound waves to non-invasively modulate neural activity. This method has potential applications in both research and clinical settings for mapping brain function and treating neurological disorders.

### Chemical and Pharmacological Perturbations:
- `Liquid perturbation`: Introduces liquids into the brain environment to study the effects of various substances or to physically disrupt brain activity. This can include the injection of drugs, solutions, or other compounds.
- `Micro perfusion`: A technique that allows the localized delivery of substances directly to a targeted area of the brain through a fine cannula, enabling the study of the effects of drugs or other agents on specific brain regions.
- `Pharmacological injection`: The direct injection of drugs or other substances into the body or directly into brain tissue to study their effects on neural activity, brain function, or behavior.
- `Pharmacological superfusion`: A technique where drugs are applied directly to neural tissues or cells in a controlled manner, often using a perfusion system, allowing for the study of drug effects on neural activity in vitro.
- `Pharmacological inhalation`: Involves the administration of drugs in vapor form so that they are inhaled and absorbed through the lungs, affecting the brain. This method is used to study the effects of inhaled substances on neural activity and behavior.

### Odor and Sound Stimulation:
- `Odor stimulation`: The presentation of controlled olfactory stimuli to study sensory processing, neural activity, and behavior influenced by smells.
- `Sound stimulation`: The use of auditory stimuli to influence brain activity and study the neural mechanisms of hearing, perception, and cognition, as well as the therapeutic effects of sound.

A detailed list of the type-specific fields can be found on the [manipulation types page]({{"datamodel/schemas/manipulation/"|absolute_url}}).




## Permissions

Manipulations inherit permissions through the session associated with them.

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## API access

The API allows for programmable access to manipulations. Learn more about the manipulations' fields and data structure on the [Manipulation API page]({{"api/modules/manipulation/"|absolute_url}}).
