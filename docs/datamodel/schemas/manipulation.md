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

### Deep brain stimulation (DBS)

| Field | Description |
|:------|:------------|
| `Amplitude (A)` | Amplitude of the stimulation in Amperes |
| `Duration (s)` | Duration of the stimulation in seconds |
| `Stimulation profile` | Profile of the stimulation (e.g., Amplitude Modulated) |
| `Duty cycle` | Duty cycle of the stimulation |
| `Repetitions` | Number of repetitions of the stimulation |
| `Injection polarity` | Polarity of the stimulation injection |
| `Closed loop` | Whether the stimulation is closed-loop or not |

### Electromagnetic field stimulation

| Field | Description |
|:------|:------------|
| `Amplitude (V)` | Amplitude of the stimulation in Volts |
| `Duration` | Duration of the stimulation |
| `Stimulation profile` | Profile of the stimulation (e.g., Amplitude Modulated) |
| `Duty cycle` | Duty cycle of the stimulation |
| `Repetitions` | Number of repetitions of the stimulation |
| `Injection polarity` | Polarity of the stimulation injection |
| `Closed loop` | Whether the stimulation is closed-loop or not |

### Electrical stimulation

| Field | Description |
|:------|:------------|
| `Amplitude (V)` | Amplitude of the stimulation in Volts |
| `Duration (s)` | Duration of the stimulation in seconds |
| `Stimulation profile` | Profile of the stimulation (e.g., Amplitude Modulated) |
| `Duty cycle` | Duty cycle of the stimulation |
| `Repetitions` | Number of repetitions of the stimulation |
| `Injection polarity` | Polarity of the stimulation injection |
| `Closed loop` | Whether the stimulation is closed-loop or not |

### Liquid perturbation

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

| Field | Description |
|:------|:------------|
| `Liquid agent` | Name or type of the liquid agent used |
| `Concentration (mg/mL)` | Concentration of the liquid agent in mg/mL |
| `Volume (µL)` | Volume of the liquid agent in microliters |
| `Perturbation profile` | Profile of the perturbation (e.g., Bolus Injection) |
| `Repetitions` | Number of repetitions of the perfusion |
| `Flow rate (µL/min)` | Flow rate of the liquid agent in µL/min |
| `Closed loop` | Whether the perfusion is closed-loop or not |

### Optogenetic stimulation

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

### Pharmacological inhalation

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

### Pharmacological injection

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

| Field | Description |
|:------|:------------|
| `Liquid agent` | Name or type of the liquid agent used |
| `Concentration (mg/mL)` | Concentration of the liquid agent in mg/mL |
| `Volume (µL)` | Volume of the liquid agent in microliters |
| `Superfusion profile` | Profile of the superfusion (e.g., Bolus Injection) |
| `Repetitions` | Number of repetitions of the superfusion |
| `Flow rate (µL/min)` | Flow rate of the liquid agent in µL/min |
| `Closed loop` | Whether the superfusion is closed-loop or not |

### Sound stimulation

| Field | Description |
|:------|:------------|
| `Amplitude (dB)` | Amplitude of the sound stimulation in decibels |
| `Duration (s)` | Duration of the stimulation in seconds |
| `Stimulation profile` | Profile of the stimulation (e.g., Amplitude Modulated) |
| `Duty cycle` | Duty cycle of the stimulation |
| `Repetitions` | Number of repetitions of the stimulation |
| `Closed loop` | Whether the stimulation is closed-loop or not |

### Thermal perturbation

| Field | Description |
|:------|:------------|
| `Amplitude (°C)` | Amplitude of the temperature change in degrees Celsius |
| `Duration (s)` | Duration of the perturbation in seconds |
| `Thermal profile` | Profile of the thermal perturbation (e.g., Amplitude Modulated) |
| `Duty cycle` | Duty cycle of the perturbation |
| `Repetitions` | Number of repetitions of the perturbation |
| `Closed loop` | Whether the perturbation is closed-loop or not |

### Transcranial Electrical Stimulation

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

| Field | Description |
|:------|:------------|
| `Amplitude (mA)` | Amplitude of the stimulation in milliamperes |
| `Duration (s)` | Duration of the stimulation in seconds |
| `Stimulation profile` | Profile of the stimulation (e.g., Amplitude Modulated) |
| `Duty cycle` | Duty cycle of the stimulation |
| `Repetitions` | Number of repetitions of the stimulation |
| `Injection polarity` | Polarity of the stimulation injection |
| `Closed loop` | Whether the stimulation is closed-loop or not |

### Ultrasound stimulation

| Field | Description |
|:------|:------------|
| `Amplitude (V)` | Amplitude of the stimulation in Volts |
| `Duration (s)` | Duration of the stimulation in seconds |
| `Duty cycle` | Duty cycle of the stimulation |
| `Stimulation profile` | Profile of the stimulation (e.g., Amplitude Modulated) |
| `Repetitions` | Number of repetitions of the stimulation |
| `Injection polarity` | Polarity of the stimulation injection |
| `Closed loop` | Whether the stimulation is closed-loop or not |

## Manipulation API access

The API allows for programmable access to Manipulations, enabling you to read, edit, and delete manipulations through the API. Learn more about the manipulations' fields and data structure on the [Manipulation API page]({{"api/modules/manipulation/"|absolute_url}}).