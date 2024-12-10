---
layout: default
title: Manipulation types
parent: Schemas
grand_parent: Data model
nav_order: 3
---

# Manipulation types
{: .no_toc}

Various manipulation types are available to modulate neural activity, study brain function, and potentially treat neurological and psychiatric disorders.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Electrical and Magnetic Stimulation

### Deep brain stimulation (DBS)

A neurosurgical procedure that involves implanting electrodes in specific areas of the brain to deliver electrical impulses. It's used to treat a variety of neurological conditions, including Parkinson's disease and essential tremor.

| Field | Description |
|:------|:------------|
| `Amplitude (A)` | Amplitude of the stimulation in Amperes |
| `Duration (s)` | Duration of the stimulation in seconds |
| `Stimulation profile` | Profile of the stimulation (e.g., Amplitude Modulated) |
| `Duty cycle` | Duty cycle of the stimulation |
| `Repetitions` | Number of repetitions of the stimulation |
| `Injection polarity` | Polarity of the stimulation injection |
| `Closed loop` | Whether the stimulation is closed-loop or not |

### Electrical stimulation

The application of electrical currents to neurons or neural tissues to activate or inhibit neural activity. This broad category can include invasive methods like intracortical microstimulation or non-invasive approaches like transcranial direct current stimulation (tDCS).

| Field | Description |
|:------|:------------|
| `Amplitude (V)` | Amplitude of the stimulation in Volts |
| `Duration (s)` | Duration of the stimulation in seconds |
| `Stimulation profile` | Profile of the stimulation (e.g., Amplitude Modulated) |
| `Duty cycle` | Duty cycle of the stimulation |
| `Repetitions` | Number of repetitions of the stimulation |
| `Injection polarity` | Polarity of the stimulation injection |
| `Closed loop` | Whether the stimulation is closed-loop or not |

### Electromagnetic field stimulation

Involves the use of magnetic or electric fields to modulate neuronal activity. This non-invasive method can influence brain function and is studied for therapeutic potential in psychiatric and neurological disorders.

| Field | Description |
|:------|:------------|
| `Amplitude (V)` | Amplitude of the stimulation in Volts |
| `Duration` | Duration of the stimulation |
| `Stimulation profile` | Profile of the stimulation (e.g., Amplitude Modulated) |
| `Duty cycle` | Duty cycle of the stimulation |
| `Repetitions` | Number of repetitions of the stimulation |
| `Injection polarity` | Polarity of the stimulation injection |
| `Closed loop` | Whether the stimulation is closed-loop or not |

### Transcranial Electrical Stimulation

A non-invasive method that applies electrical currents through the scalp and skull to modulate neuronal activity in the brain, used for research and therapeutic purposes.

| Field | Description |
|:------|:------------|
| `Amplitude (mA)` | Amplitude of the stimulation in milliamperes |
| `Duration (s)` | Duration of the stimulation in seconds |
| `Stimulation profile` | Profile of the stimulation (e.g., Amplitude Modulated) |
| `Duty cycle` | Duty cycle of the stimulation |
| `Repetitions` | Number of repetitions of the stimulation |
| `Injection polarity` | Polarity of the stimulation injection |
| `Closed loop` | Whether the stimulation is closed-loop or not |

### Transcranial Magnetic Stimulation (TMS)

A non-invasive technique that uses magnetic fields to induce electrical currents in the brain, capable of modulating neural activity and used for both research and treatment of various neurological and psychiatric conditions.

| Field | Description |
|:------|:------------|
| `Amplitude (mA)` | Amplitude of the stimulation in milliamperes |
| `Duration (s)` | Duration of the stimulation in seconds |
| `Stimulation profile` | Profile of the stimulation (e.g., Amplitude Modulated) |
| `Duty cycle` | Duty cycle of the stimulation |
| `Repetitions` | Number of repetitions of the stimulation |
| `Injection polarity` | Polarity of the stimulation injection |
| `Closed loop` | Whether the stimulation is closed-loop or not |

## Optical, Thermal, and Ultrasound Stimulation

### Optogenetic stimulation

Uses light to control neurons that have been genetically modified to express light-sensitive ion channels. This precise method enables the activation or inhibition of specific neuronal populations with high temporal resolution.

| Field | Description |
|:------|:------------|
| `Power (mW)` | Power of the light stimulation in milliwatts |
| `Amplitude (A)` | Amplitude of the stimulation in Amperes |
| `Stimulation profile` | Profile of the stimulation (e.g., Amplitude Modulated) |
| `Duration (s)` | Duration of the stimulation in seconds |
| `Duty cycle` | Duty cycle of the stimulation |
| `Repetitions` | Number of repetitions of the stimulation |
| `Wavelength (nm)` | Wavelength of the light in nanometers |
| `Closed loop` | Whether the stimulation is closed-loop or not |

### Thermal perturbation

The application of heat or cold to neural tissue to study the effects of temperature changes on neural activity, function, or structural integrity.

| Field | Description |
|:------|:------------|
| `Amplitude (°C)` | Amplitude of the temperature change in degrees Celsius |
| `Duration (s)` | Duration of the perturbation in seconds |
| `Thermal profile` | Profile of the thermal perturbation (e.g., Amplitude Modulated) |
| `Duty cycle` | Duty cycle of the perturbation |
| `Repetitions` | Number of repetitions of the perturbation |
| `Closed loop` | Whether the perturbation is closed-loop or not |

### Ultrasound stimulation

Utilizes high-frequency sound waves to non-invasively modulate neural activity. This method has potential applications in both research and clinical settings for mapping brain function and treating neurological disorders.

| Field | Description |
|:------|:------------|
| `Amplitude (V)` | Amplitude of the stimulation in Volts |
| `Duration (s)` | Duration of the stimulation in seconds |
| `Duty cycle` | Duty cycle of the stimulation |
| `Stimulation profile` | Profile of the stimulation (e.g., Amplitude Modulated) |
| `Repetitions` | Number of repetitions of the stimulation |
| `Injection polarity` | Polarity of the stimulation injection |
| `Closed loop` | Whether the stimulation is closed-loop or not |

## Chemical and Pharmacological Perturbations

### Liquid perturbation

Introduces liquids into the brain environment to study the effects of various substances or to physically disrupt brain activity. This can include the injection of drugs, solutions, or other compounds.

| Field | Description |
|:------|:------------|
| `Liquid agent` | Name or type of the liquid agent used |
| `Concentration (mg/mL)` | Concentration of the liquid agent in mg/mL |
| `Volume (µL)` | Volume of the liquid agent in microliters |
| `Perturbation profile` | Profile of the perturbation (e.g., Bolus Injection) |
| `Repetitions` | Number of repetitions of the perturbation |
| `Flow rate (µL/min)` | Flow rate of the liquid agent in µL/min |
| `Closed loop` | Whether the perturbation is closed-loop or not |

### Micro perfusion

A technique that allows the localized delivery of substances directly to a targeted area of the brain through a fine cannula, enabling the study of the effects of drugs or other agents on specific brain regions.

| Field | Description |
|:------|:------------|
| `Liquid agent` | Name or type of the liquid agent used |
| `Concentration (mg/mL)` | Concentration of the liquid agent in mg/mL |
| `Volume (µL)` | Volume of the liquid agent in microliters |
| `Perturbation profile` | Profile of the perturbation (e.g., Bolus Injection) |
| `Repetitions` | Number of repetitions of the perfusion |
| `Flow rate (µL/min)` | Flow rate of the liquid agent in µL/min |
| `Closed loop` | Whether the perfusion is closed-loop or not |

### Pharmacological injection

The direct injection of drugs or other substances into the body or directly into brain tissue to study their effects on neural activity, brain function, or behavior.

| Field | Description |
|:------|:------------|
| `Liquid agent` | Name or type of the liquid agent used |
| `Concentration (mg/mL)` | Concentration of the liquid agent in mg/mL |
| `Volume (µL)` | Volume of the liquid agent in microliters |
| `Injection profile` | Profile of the injection (e.g., Bolus Injection) |
| `Repetitions` | Number of repetitions of the injection |
| `Flow rate (µL/min)` | Flow rate of the liquid agent in µL/min |
| `Closed loop` | Whether the injection is closed-loop or not |

### Pharmacological superfusion

A technique where drugs are applied directly to neural tissues or cells in a controlled manner, often using a perfusion system, allowing for the study of drug effects on neural activity in vitro.

| Field | Description |
|:------|:------------|
| `Liquid agent` | Name or type of the liquid agent used |
| `Concentration (mg/mL)` | Concentration of the liquid agent in mg/mL |
| `Volume (µL)` | Volume of the liquid agent in microliters |
| `Superfusion profile` | Profile of the superfusion (e.g., Bolus Injection) |
| `Repetitions` | Number of repetitions of the superfusion |
| `Flow rate (µL/min)` | Flow rate of the liquid agent in µL/min |
| `Closed loop` | Whether the superfusion is closed-loop or not |

### Pharmacological inhalation

Involves the administration of drugs in vapor form so that they are inhaled and absorbed through the lungs, affecting the brain. This method is used to study the effects of inhaled substances on neural activity and behavior.

| Field | Description |
|:------|:------------|
| `Liquid agent` | Name or type of the liquid agent used |
| `Concentration (mg/mL)` | Concentration of the liquid agent in mg/mL |
| `Flow rate (µL/min)` | Flow rate of the liquid agent in µL/min |
| `Stimulation profile` | Profile of the stimulation (e.g., Bolus Inhalation) |
| `Volume (µL)` | Volume of the liquid agent in microliters |
| `Repetitions` | Number of repetitions of the inhalation |
| `Analgesic` | Whether the agent is an analgesic |
| `Sedative` | Whether the agent is a sedative |
| `Closed loop` | Whether the inhalation is closed-loop or not |

## Sensory Stimulation

### Sound stimulation

The use of auditory stimuli to influence brain activity and study the neural mechanisms of hearing, perception, and cognition, as well as the therapeutic effects of sound.

| Field | Description |
|:------|:------------|
| `Amplitude (dB)` | Amplitude of the sound stimulation in decibels |
| `Duration (s)` | Duration of the stimulation in seconds |
| `Stimulation profile` | Profile of the stimulation (e.g., Amplitude Modulated) |
| `Duty cycle` | Duty cycle of the stimulation |
| `Repetitions` | Number of repetitions of the stimulation |
| `Closed loop` | Whether the stimulation is closed-loop or not |

## Manipulation API access

The API allows for programmable access to Manipulations, enabling you to read, edit, and delete manipulations through the API. Learn more about the manipulations' fields and data structure on the [Manipulation API page]({{"api/modules/manipulation/"|absolute_url}}).