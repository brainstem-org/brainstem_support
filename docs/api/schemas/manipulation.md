---
layout: default
title: Manipulation
parent: Schemas
grand_parent: API
nav_order: 1
---

# Manipulation schemas
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Auditory stimulation
```
{
    "type": "array",
    "title": "Auditory stimulation",
    "items": {
        "type": "object",
        "title": "Auditory stimulation",
        "options": { "compact": true },
        "additionalProperties": false,
        "properties": {
            "amplitude": {
                "title": "Amplitude (dB)",
                "type": "number"
            },
            "duration": {
                "title": "Duration (s)",
                "type": "number",
                "minimum": 0
            },
            "frequency": {
                "title": "Frequency (Hz)",
                "type": "number",
                "minimum": 0
            },
            "modulationFrequency": {
                "title": "Modulation frequency (Hz)",
                "type": "number",
                "minimum": 0
            },
            "profile": {
                "title": "Stimulation profile",
                "type": "string",
                "enum": [
                    "Amplitude Modulated",
                    "Alternating Current",
                    "Biphasic",
                    "Burst",
                    "Chirp",
                    "Direct Current",
                    "Cosine",
                    "Frequency Hopping",
                    "Frequency Modulated",
                    "Decaying Exponential",
                    "Gaussian Pulse",
                    "Harmonic Stimulation",
                    "Gaussian Noise",
                    "Pseudo-random Binary Sequence",
                    "Pink Noise",
                    "Pulse train",
                    "Sawtooth",
                    "Staircase",
                    "Sine Wave",
                    "Sinc Pulse",
                    "Square",
                    "Stochastic",
                    "Step Function",
                    "Ramp",
                    "Rising Exponential",
                    "Trapezoidal Pulse",
                    "Triangle",
                    "Variable Rate Pulse Train",
                    "White Noise"
                ]
            },
            "dutyCycle": {
                "title": "Duty cycle",
                "type": "number",
                "minimum": 0
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "integer",
                "minimum": 0
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox"
            }
        },
        "required": []
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
[
    {
        "amplitude": 85,
        "duration": 2.5,
        "frequency": 1000,
        "modulationFrequency": 10,
        "profile": "Sine Wave",
        "dutyCycle": 0.5,
        "repetitions": 10,
        "closedLoop": false
    }
]
```

## Deep brain stimulation
```
{
    "type": "array",
    "title": "DeepBrainStimulation",
    "items": {
        "type": "object",
        "title": "DeepBrainStimulation",
        "options": { "compact": true },
        "additionalProperties": false,
        "properties": {
            "amplitude": {
                "title": "Amplitude (A)",
                "type": "number"
            },
            "duration": {
                "title": "Duration (s)",
                "type": "number",
                "minimum": 0
            },
            "profile": {
                "title": "Stimulation profile",
                "type": "string",
                "enum": [
                    "Amplitude Modulated",
                    "Alternating Current",
                    "Biphasic",
                    "Burst",
                    "Chirp",
                    "Direct Current",
                    "Cosine",
                    "Frequency Hopping",
                    "Frequency Modulated",
                    "Decaying Exponential",
                    "Gaussian Pulse",
                    "Harmonic Stimulation",
                    "Gaussian Noise",
                    "Pseudo-random Binary Sequence",
                    "Pink Noise",
                    "Pulse train",
                    "Sawtooth",
                    "Staircase",
                    "Sine Wave",
                    "Sinc Pulse",
                    "Square",
                    "Stochastic",
                    "Step Function",
                    "Ramp",
                    "Rising Exponential",
                    "Trapezoidal Pulse",
                    "Triangle",
                    "Variable Rate Pulse Train",
                    "White Noise"
                ]
            },
            "dutyCycle": {
                "title": "Duty cycle",
                "type": "number",
                "minimum": 0
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "integer",
                "minimum": 0
            },
            "injectionPolarity": {
                "title": "Injection polarity",
                "type": "string",
                "format": "text"
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox"
            }
        },
        "required": []
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
[
    {
        "amplitude": 2.5,
        "duration": 60,
        "profile": "Biphasic",
        "dutyCycle": 0.5,
        "repetitions": 100,
        "injectionPolarity": "anodal",
        "closedLoop": true
    }
]
```

## Electrical stimulation
```
{
    "type": "array",
    "title": "ElectricalStimulation",
    "items": {
        "type": "object",
        "title": "ElectricalStimulation",
        "options": { "compact": true },
        "additionalProperties": false,
        "properties": {
            "amplitude": {
                "title": "Amplitude",
                "type": "number"
            },
            "duration": {
                "title": "Duration",
                "type": "number",
                "minimum": 0
            },
            "dutyCycle": {
                "title": "Duty cycle",
                "type": "number",
                "minimum": 0
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "number",
                "minimum": 0
            },
            "injectionPolarity": {
                "title": "Injection polarity",
                "type": "string",
                "format": "text"
            },
            "fatalOutcome": {
                "title": "Fatal outcome",
                "type": "boolean",
                "format": "checkbox"
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox"
            }
        },
        "required": []
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
[
    {
        "amplitude": 15,
        "duration": 300,
        "dutyCycle": 3,
        "repetitions": 40,
        "injectionPolarity": "positive",
        "fatalOutcome": true,
        "closedLoop": true
    }
]
```

## Electromagnetic field stimulation
```
{
    "type": "array",
    "title": "ElectromagneticFieldStimulation",
    "items": {
        "type": "object",
        "title": "ElectromagneticFieldStimulation",
        "options": { "compact": true },
        "additionalProperties": false,
        "properties": {
            "amplitude": {
                "title": "Amplitude",
                "type": "number"
            },
            "duration": {
                "title": "Duration",
                "type": "number",
                "minimum": 0
            },
            "dutyCycle": {
                "title": "Duty cycle",
                "type": "number",
                "minimum": 0
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "number",
                "minimum": 0
            },
            "injectionPolarity": {
                "title": "Injection polarity",
                "type": "string",
                "format": "text"
            },
            "fatalOutcome": {
                "title": "Fatal outcome",
                "type": "boolean",
                "format": "checkbox"
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox"
            }
        },
        "required": []
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
[
    {
        "amplitude": 15,
        "duration": 300,
        "dutyCycle": 3,
        "repetitions": 40,
        "injectionPolarity": "positive",
        "fatalOutcome": true,
        "closedLoop": true
    }
]
```

## Liquid perturbation
```
{
    "type": "array",
    "title": "LiquidPerturbation",
    "items": {
        "type": "object",
        "title": "LiquidPerturbation",
        "options": { "compact": true },
        "additionalProperties": false,
        "properties": {
            "liquidAgent": {
                "title": "Liquid agent",
                "type": "string",
                "format": "text"
            },
            "concentration": {
                "title": "Concentration",
                "type": "number",
                "minimum": 0
            },
            "volume": {
                "title": "Volume (µL)",
                "type": "number",
                "minimum": 0
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "number",
                "minimum": 0
            },
            "flowRate": {
                "title": "Flow rate (µL/min)",
                "type": "number"
            },
            "fatalOutcome": {
                "title": "Fatal outcome",
                "type": "boolean",
                "format": "checkbox"
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox"
            }
        },
        "required": []
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
[
    {
        "liquidAgent": "ethanol",
        "concentration": 0.15,
        "volume": 7.2,
        "repetitions": 15,
        "flowRate": 4,
        "fatalOutcome": false,
        "closedLoop": true
    }
]
```

## Microperfusion
```
{
    "type": "array",
    "title": "Microperfusion",
    "items": {
        "type": "object",
        "title": "Microperfusion",
        "options": { "compact": true },
        "additionalProperties": false,
        "properties": {
            "liquidAgent": {
                "title": "Liquid agent",
                "type": "string",
                "format": "text"
            },
            "concentration": {
                "title": "Concentration",
                "type": "number",
                "minimum": 0
            },
            "volume": {
                "title": "Volume (µL)",
                "type": "number",
                "minimum": 0
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "number",
                "minimum": 0
            },
            "flowRate": {
                "title": "Flow rate (µL/min)",
                "type": "number"
            },
            "fatalOutcome": {
                "title": "Fatal outcome",
                "type": "boolean",
                "format": "checkbox"
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox"
            }
        },
        "required": []
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
[
    {
        "liquidAgent": "ethanol",
        "concentration": 0.15,
        "volume": 7.2,
        "repetitions": 15,
        "flowRate": 4,
        "fatalOutcome": false,
        "closedLoop": true
    }
]
```

## Multisensory stimulation
```
{
    "type": "array",
    "title": "Multisensory stimulation",
    "items": {
        "type": "object",
        "title": "Multisensory stimulation",
        "options": { "compact": true },
        "additionalProperties": false,
        "properties": {
            "modalities": {
                "title": "Modalities",
                "type": "array",
                "items": {
                    "type": "string",
                    "enum": ["Visual", "Auditory", "Tactile", "Olfactory", "Gustatory", "Vestibular", "Other"]
                },
                "uniqueItems": true,
                "format": "select"
            },
            "synchronization": {
                "title": "Temporal relationship",
                "type": "string",
                "enum": ["Synchronous", "Asynchronous", "Randomized", "Unknown"]
            },
            "duration": {
                "title": "Duration (s)",
                "type": "number",
                "minimum": 0
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "integer",
                "minimum": 0
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox"
            }
        },
        "required": []
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
[
    {
        "modalities": ["Visual", "Auditory"],
        "synchronization": "Synchronous",
        "duration": 5.0,
        "repetitions": 20,
        "closedLoop": false
    }
]
```

## Odor stimulation
```
{
    "type": "array",
    "title": "Odor stimulation",
    "items": {
        "type": "object",
        "title": "Odor stimulation",
        "options": { "compact": true },
        "additionalProperties": false,
        "properties": {
            "odor": {
                "title": "Odor presented",
                "type": "string",
                "format": "text"
            },
            "concentration": {
                "title": "Concentration (mg/mL)",
                "type": "number",
                "minimum": 0
            },
            "flowRate": {
                "title": "Flow rate (mL/min)",
                "type": "number"
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "integer",
                "minimum": 0
            },
            "inhalationPhase": {
                "title": "Inhalation phase",
                "type": "string",
                "format": "text"
            }
        },
        "required": []
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
[
    {
        "odor": "vanilla",
        "concentration": 0.5,
        "flowRate": 2.0,
        "repetitions": 10,
        "inhalationPhase": "inspiration"
    }
]
```

## Optogenetical stimulation
```
{
    "type": "array",
    "title": "OptogeneticalStimulation",
    "items": {
        "type": "object",
        "title": "OptogeneticalStimulation",
        "options": { "compact": true },
        "additionalProperties": false,
        "properties": {
            "power": {
                "title": "Power (mW)",
                "type": "number",
                "format": "number"
            },
            "amplitude": {
                "title": "Amplitude (A)",
                "type": "number"
            },
            "duration": {
                "title": "Duration (s)",
                "type": "number",
                "minimum": 0
            },
            "dutyCycle": {
                "title": "Duty cycle",
                "type": "number",
                "minimum": 0
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "number",
                "minimum": 0
            },
            "wavelength": {
                "title": "Wavelength (nm)",
                "type": "number",
                "minimum": 0
            },
            "fatalOutcome": {
                "title": "Fatal outcome",
                "type": "boolean",
                "format": "checkbox"
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox"
            }
        },
        "required": []
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
[
    {
        "power": 66.6,
        "amplitude": 32,
        "duration": 300,
        "dutyCycle": 0.3,
        "repetitions": 23,
        "wavelength": 42,
        "fatalOutcome": true,
        "closedLoop": false
    }
]
```

## Pharmacological inhalation
```
{
    "type": "array",
    "title": "PharmacologicalInhalation",
    "items": {
        "type": "object",
        "title": "PharmacologicalInhalation",
        "options": { "compact": true },
        "additionalProperties": false,
        "properties": {
            "liquidAgent": {
                "title": "Liquid agent",
                "type": "string",
                "format": "text"
            },
            "concentration": {
                "title": "Concentration",
                "type": "number",
                "minimum": 0
            },
            "flowRate": {
                "title": "flow rate (µL/min)",
                "type": "number"
            },
            "volume": {
                "title": "Volume (µL)",
                "type": "number",
                "minimum": 0
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "number",
                "minimum": 0
            },
            "analgesic": {
                "title": "Analgesic",
                "type": "string",
                "format": "text"
            },
            "sedative": {
                "title": "Sedative",
                "type": "string",
                "format": "text"
            },
            "fatalOutcome": {
                "title": "Fatal outcome",
                "type": "boolean",
                "format": "checkbox"
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox"
            }
        },
        "required": []
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
[
    {
        "liquidAgent": "ethanol",
        "concentration": 0.15,
        "volume": 7.2,
        "repetitions": 15,
        "analgesic": "Ibuprofen",
        "sedative": "Valium",
        "flowRate": 4,
        "fatalOutcome": false,
        "closedLoop": true
    }
]
```

## Pharmacological injection
```
{
    "type": "array",
    "title": "PharmacologicalInjection",
    "items": {
        "type": "object",
        "title": "PharmacologicalInjection",
        "options": { "compact": true },
        "additionalProperties": false,
        "properties": {
            "liquidAgent": {
                "title": "Liquid agent",
                "type": "string",
                "format": "text"
            },
            "concentration": {
                "title": "Concentration",
                "type": "number",
                "minimum": 0
            },
            "volume": {
                "title": "Volume (µL)",
                "type": "number",
                "minimum": 0
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "number",
                "minimum": 0
            },
            "flowRate": {
                "title": "Flow rate (µL/min)",
                "type": "number"
            },
            "fatalOutcome": {
                "title": "Fatal outcome",
                "type": "boolean",
                "format": "checkbox"
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox"
            }
        },
        "required": []
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
[
    {
        "liquidAgent": "ethanol",
        "concentration": 0.15,
        "volume": 7.2,
        "repetitions": 15,
        "flowRate": 4,
        "fatalOutcome": false,
        "closedLoop": true
    }
]
```

## Pharmacological superfusion
```
{
    "type": "array",
    "title": "PharmacologicalSuperfusion",
    "items": {
        "type": "object",
        "title": "PharmacologicalSuperfusion",
        "options": { "compact": true },
        "additionalProperties": false,
        "properties": {
            "liquidAgent": {
                "title": "Liquid agent",
                "type": "string",
                "format": "text"
            },
            "concentration": {
                "title": "Concentration",
                "type": "number",
                "minimum": 0
            },
            "volume": {
                "title": "Volume (µL)",
                "type": "number",
                "minimum": 0
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "number",
                "minimum": 0
            },
            "flowRate": {
                "title": "Flow rate (µL/min)",
                "type": "number"
            },
            "fatalOutcome": {
                "title": "Fatal outcome",
                "type": "boolean",
                "format": "checkbox"
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox"
            }
        },
        "required": []
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
[
    {
        "liquidAgent": "ethanol",
        "concentration": 0.15,
        "volume": 7.2,
        "repetitions": 15,
        "flowRate": 4,
        "fatalOutcome": false,
        "closedLoop": true
    }
]
```

## Sound stimulation
```
{
    "type": "array",
    "title": "SoundStimulation",
    "items": {
        "type": "object",
        "title": "SoundStimulation",
        "options": { "compact": true },
        "additionalProperties": false,
        "properties": {
            "amplitude": {
                "title": "Amplitude",
                "type": "number"
            },
            "duration": {
                "title": "Duration (s)",
                "type": "number",
                "minimum": 0
            },
            "dutyCycle": {
                "title": "Duty cycle",
                "type": "number",
                "minimum": 0
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "number",
                "minimum": 0
            },
            "injectionPolarity": {
                "title": "Injection polarity",
                "type": "string",
                "format": "text"
            },
            "fatalOutcome": {
                "title": "Fatal outcome",
                "type": "boolean",
                "format": "checkbox"
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox"
            }
        },
        "required": []
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
[
    {
        "amplitude": 15,
        "duration": 300,
        "dutyCycle": 3,
        "repetitions": 40,
        "injectionPolarity": "positive",
        "fatalOutcome": true,
        "closedLoop": true
    }
]
```

## Tactile stimulation
```
{
    "type": "array",
    "title": "Tactile stimulation",
    "items": {
        "type": "object",
        "title": "Tactile stimulation",
        "options": { "compact": true },
        "additionalProperties": false,
        "properties": {
            "contactType": {
                "title": "Contact type",
                "type": "string",
                "enum": [
                    "Mechanical (contact)",
                    "Mechanical (vibration)",
                    "Air puff",
                    "Brush",
                    "Cotton swab",
                    "Other"
                ]
            },
            "site": {
                "title": "Stimulation site",
                "type": "string"
            },
            "force": {
                "title": "Force (mN)",
                "type": "number"
            },
            "duration": {
                "title": "Duration (s)",
                "type": "number",
                "minimum": 0
            },
            "profile": {
                "title": "Stimulation profile",
                "type": "string",
                "enum": [
                    "Single pulse",
                    "Pulse train",
                    "Sinusoidal",
                    "Square wave",
                    "Sawtooth",
                    "Burst",
                    "Ramp",
                    "Step function",
                    "Manual"
                ]
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "integer",
                "minimum": 0
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox"
            }
        },
        "required": []
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
[
    {
        "contactType": "Mechanical (vibration)",
        "site": "whisker pad",
        "force": 10,
        "duration": 0.5,
        "profile": "Pulse train",
        "repetitions": 20,
        "closedLoop": false
    }
]
```

## Thermal perturbation
```
{
    "type": "array",
    "title": "ThermalPerturbation",
    "items": {
        "type": "object",
        "title": "ThermalPerturbation",
        "options": { "compact": true },
        "additionalProperties": false,
        "properties": {
            "amplitude": {
                "title": "Amplitude (°C)",
                "type": "number"
            },
            "duration": {
                "title": "Duration (s)",
                "type": "number",
                "minimum": 0
            },
            "dutyCycle": {
                "title": "Duty cycle",
                "type": "number",
                "minimum": 0
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "number",
                "minimum": 0
            },
            "fatalOutcome": {
                "title": "Fatal outcome",
                "type": "boolean",
                "format": "checkbox"
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox"
            }
        },
        "required": []
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
[
    {
        "amplitude": 15,
        "duration": 300,
        "dutyCycle": 3,
        "repetitions": 40,
        "fatalOutcome": true,
        "closedLoop": true
    }
]
```

## Transcranial electrical stimulation
```
{
    "type": "array",
    "title": "Transcranial Electrical Stimulation",
    "items": {
        "type": "object",
        "title": "Transcranial Electrical Stimulation",
        "options": { "compact": true },
        "additionalProperties": false,
        "properties": {
            "amplitude": {
                "title": "Amplitude (mA)",
                "type": "number"
            },
            "duration": {
                "title": "Duration (s)",
                "type": "number",
                "minimum": 0
            },
            "profile": {
                "title": "Stimulation profile",
                "type": "string",
                "enum": [
                    "Amplitude Modulated",
                    "Alternating Current",
                    "Biphasic",
                    "Burst",
                    "Chirp",
                    "Direct Current",
                    "Cosine",
                    "Frequency Hopping",
                    "Frequency Modulated",
                    "Decaying Exponential",
                    "Gaussian Pulse",
                    "Harmonic Stimulation",
                    "Gaussian Noise",
                    "Pseudo-random Binary Sequence",
                    "Pink Noise",
                    "Pulse train",
                    "Sawtooth",
                    "Staircase",
                    "Sine Wave",
                    "Sinc Pulse",
                    "Square",
                    "Stochastic",
                    "Step Function",
                    "Ramp",
                    "Rising Exponential",
                    "Trapezoidal Pulse",
                    "Triangle",
                    "Variable Rate Pulse Train",
                    "White Noise"
                ]
            },
            "dutyCycle": {
                "title": "Duty cycle",
                "type": "number",
                "minimum": 0
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "integer",
                "minimum": 0
            },
            "injectionPolarity": {
                "title": "Injection polarity",
                "type": "string",
                "format": "text"
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox"
            }
        },
        "required": []
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
[
    {
        "amplitude": 2.0,
        "duration": 1200,
        "profile": "Direct Current",
        "dutyCycle": 1.0,
        "repetitions": 1,
        "injectionPolarity": "anodal",
        "closedLoop": false
    }
]
```

## Transcranial magnetic stimulation
```
{
    "type": "array",
    "title": "Transcranial Electrical Stimulation",
    "items": {
        "type": "object",
        "title": "Transcranial Electrical Stimulation",
        "options": { "compact": true },
        "additionalProperties": false,
        "properties": {
            "amplitude": {
                "title": "Amplitude (mA)",
                "type": "number"
            },
            "duration": {
                "title": "Duration (s)",
                "type": "number",
                "minimum": 0
            },
            "profile": {
                "title": "Stimulation profile",
                "type": "string",
                "enum": [
                    "Amplitude Modulated",
                    "Alternating Current",
                    "Biphasic",
                    "Burst",
                    "Chirp",
                    "Direct Current",
                    "Cosine",
                    "Frequency Hopping",
                    "Frequency Modulated",
                    "Decaying Exponential",
                    "Gaussian Pulse",
                    "Harmonic Stimulation",
                    "Gaussian Noise",
                    "Pseudo-random Binary Sequence",
                    "Pink Noise",
                    "Pulse train",
                    "Sawtooth",
                    "Staircase",
                    "Sine Wave",
                    "Sinc Pulse",
                    "Square",
                    "Stochastic",
                    "Step Function",
                    "Ramp",
                    "Rising Exponential",
                    "Trapezoidal Pulse",
                    "Triangle",
                    "Variable Rate Pulse Train",
                    "White Noise"
                ]
            },
            "dutyCycle": {
                "title": "Duty cycle",
                "type": "number",
                "minimum": 0
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "integer",
                "minimum": 0
            },
            "injectionPolarity": {
                "title": "Injection polarity",
                "type": "string",
                "format": "text"
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox"
            }
        },
        "required": []
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
[
    {
        "amplitude": 1.5,
        "duration": 600,
        "profile": "Biphasic",
        "dutyCycle": 0.5,
        "repetitions": 1000,
        "injectionPolarity": "biphasic",
        "closedLoop": false
    }
]
```

## Ultrasound stimulation
```
{
    "type": "array",
    "title": "Ultrasound Stimulation",
    "items": {
        "type": "object",
        "title": "Ultrasound Stimulation",
        "options": { "compact": true },
        "additionalProperties": false,
        "properties": {
            "amplitude": {
                "title": "Amplitude (V)",
                "type": "number"
            },
            "duration": {
                "title": "Duration (s)",
                "type": "number",
                "minimum": 0
            },
            "dutyCycle": {
                "title": "Duty cycle",
                "type": "number",
                "minimum": 0
            },
            "profile": {
                "title": "Stimulation profile",
                "type": "string",
                "enum": [
                    "Amplitude Modulated",
                    "Alternating Current",
                    "Biphasic",
                    "Burst",
                    "Chirp",
                    "Direct Current",
                    "Cosine",
                    "Frequency Hopping",
                    "Frequency Modulated",
                    "Decaying Exponential",
                    "Gaussian Pulse",
                    "Harmonic Stimulation",
                    "Gaussian Noise",
                    "Pseudo-random Binary Sequence",
                    "Pink Noise",
                    "Pulse train",
                    "Sawtooth",
                    "Staircase",
                    "Sine Wave",
                    "Sinc Pulse",
                    "Square",
                    "Stochastic",
                    "Step Function",
                    "Ramp",
                    "Rising Exponential",
                    "Trapezoidal Pulse",
                    "Triangle",
                    "Variable Rate Pulse Train",
                    "White Noise"
                ]
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "integer",
                "minimum": 0
            },
            "injectionPolarity": {
                "title": "Injection polarity",
                "type": "string",
                "format": "text"
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox"
            }
        },
        "required": []
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
[
    {
        "amplitude": 10,
        "duration": 300,
        "profile": "Burst",
        "dutyCycle": 0.2,
        "repetitions": 100,
        "injectionPolarity": "positive",
        "closedLoop": false
    }
]
```

## Visual stimulation
```
{
    "type": "array",
    "title": "Visual stimulation",
    "items": {
        "type": "object",
        "title": "Visual stimulation",
        "options": { "compact": true },
        "additionalProperties": false,
        "properties": {
            "stimulusTypes": {
                "title": "Stimulus types",
                "type": "array",
                "items": {
                    "type": "string",
                    "enum": [
                        "Gratings",
                        "Natural images",
                        "LED flashes",
                        "Checkerboard",
                        "Full-field flashes",
                        "Moving bars",
                        "Flicker",
                        "Other"
                    ]
                },
                "uniqueItems": true
            },
            "presentationDevice": {
                "title": "Presentation device",
                "type": "string",
                "enum": [
                    "Monitor",
                    "LED panel",
                    "Projector",
                    "Head-mounted display",
                    "Fiber-coupled light source",
                    "Other"
                ]
            },
            "stimulationPosition": {
                "title": "Stimulus position",
                "type": "string",
                "enum": [
                    "Contralateral",
                    "Ipsilateral",
                    "Bilateral",
                    "Centered",
                    "Surround",
                    "Other",
                    "Unknown"
                ]
            },
            "duration": {
                "title": "Duration (s)",
                "type": "number",
                "minimum": 0
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "integer",
                "minimum": 0
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox"
            }
        },
        "required": []
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
[
    {
        "stimulusTypes": ["Gratings", "Moving bars"],
        "presentationDevice": "Monitor",
        "stimulationPosition": "Contralateral",
        "duration": 2.0,
        "repetitions": 50,
        "closedLoop": false
    }
]
```