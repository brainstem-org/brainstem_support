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

## AuditoryStimulation
```
{
    "type": "array",
    "minItems": 1,
    "format": "table",
    "title": "Auditory stimulation",
    "options": {
        "compact": "true",
        "enable_array_copy": true,
        "disable_properties": false,
        "disable_edit_json": false,
        "disable_array_delete_last_row": true,
        "disable_array_delete_all_rows": true,
        "no_additional_properties": true
    },
    "items": {
        "type": "object",
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false,
        "properties": {
            "amplitude": {
                "title": "Amplitude (dB)",
                "units": "dB",
                "type": "number",
                "options": {
                    "infoText": "The maximum level of the sound pressure created by the stimulus, typically measured in decibels (dB), which determines the loudness of the sound presented."
                }
            },
            "duration": {
                "title": "Duration (s)",
                "units": "s",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "The length of time for which the sound is played, measured in seconds, which affects the temporal exposure of the subject to the stimulus."
                }
            },
            "frequency": {
                "title": "Frequency (Hz)",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "Base frequency of the sound stimulus, typically used for tones or frequency sweeps."
                }
            },
            "modulationFrequency": {
                "title": "Modulation frequency (Hz)",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "Modulation frequency if amplitude- or frequency-modulated (optional)."
                }
            },
            "profile": {
                "title": "Stimulation profile",
                "brief": "profile",
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
                ],
                "options": {
                    "infoText": "The specific waveform or pattern of the sound used for stimulation, which can influence the neural response depending on the research or therapeutic goals."
                }
            },
            "dutyCycle": {
                "title": "Duty cycle",
                "type": "number",
                "units": "",
                "minimum": 0,
                "options": {
                    "infoText": "The proportion of the period during which the sound is active, expressed as a fraction. Important for patterns like pulse trains where pauses between sounds affect response."
                }
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "integer",
                "units": "",
                "minimum": 0,
                "options": {
                    "inputAttributes": {
                        "placeholder": "integer"
                    },
                    "infoText": "The number of times the sound stimulus is repeated, crucial in studies assessing the effects of repeated exposure or conditioning."
                }
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox",
                "options": {
                    "infoText": "Indicates whether the sound stimulation system can adjust parameters automatically in response to feedback from the subject or environment, enhancing the adaptiveness of the stimulus."
                }
            }
        }
    }
}
```

## DeepBrainStimulation
```
{
    "type": "array",
    "minItems": 1,
    "format": "table",
    "title": "DeepBrainStimulation",
    "options": {
        "compact": "true",
        "enable_array_copy": true,
        "disable_properties": false,
        "disable_edit_json": false,
        "disable_array_delete_last_row": true,
        "disable_array_delete_all_rows": true,
        "no_additional_properties": true
    },
    "items": {
        "type": "object",
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false,
        "properties": {
            "amplitude": {
                "title": "Amplitude (A)",
                "brief": "amplitude",
                "units": "A",
                "type": "number",
                "options": {
                    "infoText": "The intensity of the electrical stimulus applied, measured in amperes."
                }
            },
            "duration": {
                "title": "Duration (s)",
                "brief": "duration",
                "units": "s",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "The length of time each stimulation lasts, measured in seconds."
                }
            },
            "profile": {
                "title": "Stimulation profile",
                "brief": "profile",
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
                ],
                "options": {
                    "infoText": "Defines the profile of the electrical signal used for stimulation, each designed to target specific neural mechanisms."
                }
            },
            "dutyCycle": {
                "title": "Duty cycle",
                "type": "number",
                "brief": "duty cycle",
                "units": "",
                "minimum": 0,
                "options": {
                    "infoText": "The proportion of the 'on' time to the total cycle time, expressed as a fraction."
                }
            },
            "repetitions": {
                "title": "Repetitions",
                "brief": "repetitions",
                "type": "integer",
                "units": "A",
                "minimum": 0,
                "options": {
                    "inputAttributes": {
                        "placeholder": "integer"
                    },
                    "infoText": "The number of times the stimulation cycle is repeated during a session."
                }
            },
            "injectionPolarity": {
                "title": "Injection polarity",
                "brief": "injection polarity",
                "type": "string",
                "format": "text",
                "options": {
                    "infoText": "Specifies the polarity of the stimulation, which can be anodal or cathodal, influencing the direction of the current flow."
                }
            },
            "closedLoop": {
                "title": "Closed loop",
                "brief": "closed loop",
                "type": "boolean",
                "format": "checkbox",
                "options": {
                    "infoText": "Indicates whether the stimulation system is capable of adjusting its parameters based on real-time feedback from the patient's physiological responses."
                }
            }
        }
    }
}
```

## ElectricalStimulation
```
{
    "type": "array",
    "minItems": 1,
    "format": "table",
    "title": "Electrical Stimulation",
    "options": {
        "compact": true,
        "enable_array_copy": true,
        "disable_properties": false,
        "disable_edit_json": false,
        "disable_array_delete_last_row": true,
        "disable_array_delete_all_rows": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "items": {
        "type": "object",
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false,
        "properties": {
            "amplitude": {
                "title": "Amplitude (V)",
                "brief": "amplitude",
                "units": "V",
                "type": "number",
                "options": {
                    "infoText": "The magnitude of the electrical voltage applied during stimulation, measured in volts, which determines the strength of the stimulus."
                }
            },
            "duration": {
                "title": "Duration (s)",
                "brief": "duration",
                "units": "s",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "The length of time for which the stimulation is applied, typically measured in seconds (s). This can affect the efficacy and safety of the treatment."
                }
            },
            "profile": {
                "title": "Stimulation profile",
                "brief": "profile",
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
                ],
                "options": {
                    "infoText": "The pattern or waveform of the stimulation, each designed to target specific neural mechanisms or achieve specific physiological responses."
                }
            },
            "dutyCycle": {
                "title": "Duty cycle",
                "brief": "duty cycle",
                "units": "",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "The proportion of the stimulation cycle during which the stimulus is active, expressed as a fraction. This affects the total energy delivered during the therapy."
                }
            },
            "repetitions": {
                "title": "Repetitions",
                "brief": "repetitions",
                "type": "integer",
                "units": "",
                "minimum": 0,
                "options": {
                    "inputAttributes": {
                        "placeholder": "integer"
                    },
                    "infoText": "The number of times the stimulation is repeated during a session. More repetitions can increase the effects but also the risk of adverse reactions."
                }
            },
            "injectionPolarity": {
                "title": "Injection polarity",
                "brief": "polarity",
                "type": "string",
                "format": "text",
                "options": {
                    "infoText": "Refers to the direction of current flow in the stimulation, important for achieving the desired effect on neural tissues."
                }
            },
            "closedLoop": {
                "title": "Closed loop",
                "brief": "closed loop",
                "type": "boolean",
                "format": "checkbox",
                "options": {
                    "infoText": "Indicates whether the system adjusts the stimulation parameters based on real-time feedback from physiological sensors, enhancing the precision and safety of the treatment."
                }
            }
        }
    }
}
```

## ElectromagneticFieldStimulation
```
{
    "type": "array",
    "minItems": 1,
    "format": "table",
    "title": "Electromagnetic Field Stimulation",
    "options": {
        "compact": "true",
        "enable_array_copy": true,
        "disable_properties": false,
        "disable_edit_json": false,
        "disable_array_delete_last_row": true,
        "disable_array_delete_all_rows": true,
        "no_additional_properties": true
    },
    "items": {
        "type": "object",
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false,
        "properties": {
            "amplitude": {
                "title": "Amplitude (V)",
                "units": "V",
                "type": "number",
                "options": {
                    "infoText": "The intensity of the electromagnetic field applied, usually measured in volts per meter (V/m) or tesla (T), which determines the strength of the electromagnetic influence on the target area."
                }
            },
            "duration": {
                "title": "Duration",
                "units": "s",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "The length of time for which the electromagnetic field is applied during each session, typically measured in milliseconds or seconds. Duration impacts the therapeutic efficacy and safety."
                }
            },
            "profile": {
                "title": "Stimulation profile",
                "brief": "profile",
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
                ],
                "options": {
                    "infoText": "Defines the waveform of the electromagnetic field used during stimulation. Different profiles can target specific cellular mechanisms or achieve various physiological responses."
                }
            },
            "dutyCycle": {
                "title": "Duty cycle",
                "type": "number",
                "units": "",
                "minimum": 0,
                "options": {
                    "infoText": "The proportion of the stimulation cycle during which the electromagnetic field is active, expressed as a fraction. This affects the total energy delivered and can influence the treatment outcome."
                }
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "integer",
                "units": "",
                "minimum": 0,
                "options": {
                    "inputAttributes": {
                        "placeholder": "integer"
                    },
                    "infoText": "The number of times the stimulation cycle is repeated within a single session. Higher repetitions may increase efficacy but also the risk of adverse effects."
                }
            },
            "injectionPolarity": {
                "title": "Injection polarity",
                "type": "string",
                "format": "text",
                "options": {
                    "infoText": "Indicates the polarity of the electromagnetic field, which can be positive, negative, or alternating. Polarity may affect the direction of ion flow and neuronal excitation."
                }
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox",
                "options": {
                    "infoText": "Whether the stimulation system is capable of adjusting its output based on real-time feedback from sensors measuring biological responses. This feature enhances safety and efficacy by dynamically optimizing stimulation parameters."
                }
            }
        }
    }
}
```

## LiquidPerturbation
```
{
    "type": "array",
    "minItems": 1,
    "format": "table",
    "title": "Liquid Perturbation",
    "options": {
        "compact": "true",
        "enable_array_copy": true,
        "disable_properties": false,
        "disable_edit_json": false,
        "disable_array_delete_last_row": true,
        "disable_array_delete_all_rows": true,
        "no_additional_properties": true
    },
    "items": {
        "type": "object",
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false,
        "properties": {
            "liquidAgent": {
                "title": "Liquid agent",
                "type": "string",
                "format": "text",
                "options": {
                    "infoText": "The type or name of the liquid agent used for perturbation, such as a specific drug, nutrient solution, or chemical compound."
                }
            },
            "concentration": {
                "title": "Concentration (mg/mL)",
                "type": "number",
                "units": "mg/mL",
                "minimum": 0,
                "options": {
                    "infoText": "The concentration of the liquid agent, specified in mg/mL or molarity, crucial for ensuring the desired potency and effect."
                }
            },
            "volume": {
                "title": "Volume (\u00b5L)",
                "units": "\u00b5L",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "The total volume of the agent to be administered, measured in microliters, determining the overall quantity of the agent delivered."
                }
            },
            "profile": {
                "title": "Perturbation profile",
                "brief": "profile",
                "type": "string",
                "enum": [
                    "Bolus Injection",
                    "Continuous Infusion",
                    "Tapered Dose",
                    "Intermittent Bolus",
                    "Staggered Injection",
                    "Ramp Infusion",
                    "Burst Infusion",
                    "Step Infusion",
                    "Layered Dosing",
                    "Titration"
                ],
                "options": {
                    "infoText": "Describes the method of liquid delivery, affecting how the agent impacts the system, which can vary from a single, rapid dose to a slowly escalating dose."
                }
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "integer",
                "units": "",
                "minimum": 0,
                "options": {
                    "inputAttributes": {
                        "placeholder": "integer"
                    },
                    "infoText": "The number of times the perturbation is to be repeated, important for experimental protocols requiring multiple dosages over time."
                }
            },
            "flowRate": {
                "title": "Flow rate (\u00b5L/min)",
                "units": "\u00b5L/min",
                "type": "number",
                "options": {
                    "infoText": "The rate at which the liquid agent is administered, measured in microliters per minute, which influences the speed and spread of the agent's effect."
                }
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox",
                "options": {
                    "infoText": "Indicates whether the system can adjust the flow, volume, or concentration of the agent based on real-time feedback, typically from sensors or monitoring equipment."
                }
            }
        }
    }
}
```

## Microperfusion
```
{
    "type": "array",
    "minItems": 1,
    "format": "table",
    "title": "Microperfusion",
    "options": {
        "compact": "true",
        "enable_array_copy": true,
        "disable_properties": false,
        "disable_edit_json": false,
        "disable_array_delete_last_row": true,
        "disable_array_delete_all_rows": true,
        "no_additional_properties": true,
        "use_type_default_value": false
    },
    "items": {
        "type": "object",
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false,
        "properties": {
            "liquidAgent": {
                "title": "Liquid agent",
                "type": "string",
                "format": "text",
                "options": {
                    "infoText": "The type or name of the liquid agent used in the microperfusion, such as a specific drug, dye, or nutrient solution."
                }
            },
            "concentration": {
                "title": "Concentration (mg/mL)",
                "units": "mg/mL",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "The concentration of the liquid agent, typically specified in mg/mL or molarity, critical for ensuring the desired physiological impact."
                }
            },
            "volume": {
                "title": "Volume (\u00b5L)",
                "units": "\u00b5L",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "The total volume of the agent to be administered through microperfusion, measured in microliters, which determines the extent of tissue exposure to the agent."
                }
            },
            "profile": {
                "title": "Perturbation profile",
                "brief": "profile",
                "type": "string",
                "enum": [
                    "Bolus Injection",
                    "Continuous Infusion",
                    "Tapered Dose",
                    "Intermittent Bolus",
                    "Staggered Injection",
                    "Ramp Infusion",
                    "Burst Infusion",
                    "Step Infusion",
                    "Layered Dosing",
                    "Titration"
                ],
                "options": {
                    "infoText": "The method or pattern of delivery for the liquid agent, which affects how the substance impacts the tissue or system being studied."
                }
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "integer",
                "units": "",
                "minimum": 0,
                "options": {
                    "inputAttributes": {
                        "placeholder": "integer"
                    },
                    "infoText": "The number of times the microperfusion procedure is repeated, important for experiments requiring consistent exposure over time."
                }
            },
            "flowRate": {
                "title": "Flow rate (\u00b5L/min)",
                "units": "\u00b5L/min",
                "type": "number",
                "options": {
                    "infoText": "The rate at which the liquid agent is administered, measured in microliters per minute, critical for controlling the speed of agent delivery and its dispersion within the target area."
                }
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox",
                "options": {
                    "infoText": "Indicates whether the microperfusion system adjusts the delivery parameters based on real-time feedback, typically from sensors measuring tissue response, to enhance precision and effectiveness."
                }
            }
        }
    }
}
```

## MultisensoryStimulation
```
{
    "type": "array",
    "minItems": 1,
    "format": "table",
    "title": "Multisensory stimulation",
    "options": {
        "compact": "true",
        "enable_array_copy": true,
        "disable_properties": false,
        "disable_edit_json": false,
        "disable_array_delete_last_row": true,
        "disable_array_delete_all_rows": true,
        "no_additional_properties": true,
        "use_type_default_value": false
    },
    "items": {
        "type": "object",
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false,
        "properties": {
            "modalities": {
                "title": "Modalities",
                "type": "array",
                "items": {
                    "type": "string",
                    "enum": [
                        "Visual",
                        "Auditory",
                        "Tactile",
                        "Olfactory",
                        "Gustatory",
                        "Vestibular",
                        "Other"
                    ]
                },
                "uniqueItems": true,
                "format": "select",
                "options": {
                    "infoText": "Select the sensory modalities presented together in this stimulation event."
                }
            },
            "synchronization": {
                "title": "Temporal relationship",
                "type": "string",
                "enum": [
                    "Synchronous",
                    "Asynchronous",
                    "Randomized",
                    "Unknown"
                ],
                "options": {
                    "infoText": "Indicates how the different sensory stimuli were timed relative to each other."
                }
            },
            "duration": {
                "title": "Duration (s)",
                "type": "number",
                "minimum": 0,
                "units": "s",
                "options": {
                    "infoText": "Overall duration of the multisensory event, i.e., the time window during which stimuli were presented."
                }
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "integer",
                "minimum": 0,
                "options": {
                    "inputAttributes": {
                        "placeholder": "integer"
                    },
                    "infoText": "Number of times this multisensory stimulus combination was repeated."
                }
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox",
                "options": {
                    "infoText": "Was stimulus timing or modality selection dynamically adapted based on behavioral or physiological signals?"
                }
            }
        }
    }
}
```

## OdorStimulation
```
{
    "type": "array",
    "minItems": 1,
    "format": "table",
    "title": "Odor stimulation",
    "options": {
        "compact": "true",
        "enable_array_copy": true,
        "disable_properties": false,
        "disable_edit_json": false,
        "disable_array_delete_last_row": true,
        "disable_array_delete_all_rows": true,
        "no_additional_properties": true
    },
    "items": {
        "type": "object",
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false,
        "properties": {
            "odor": {
                "title": "Odor presented",
                "type": "string",
                "format": "text",
                "options": {
                    "infoText": "The specific odor administered through inhalation."
                }
            },
            "concentration": {
                "title": "Concentration (mg/mL)",
                "units": "mg/mL",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "The concentration of the odor in the inhalation mixture, typically specified in percentage or mg/mL, crucial for dosing."
                }
            },
            "flowRate": {
                "title": "Flow rate (mL/min)",
                "units": "mL/min",
                "type": "number",
                "options": {
                    "infoText": "The rate at which the inhalation agent is delivered to the subject, measured in milliliters per minute, determining the speed and extent of administration."
                }
            },
            "repetitions": {
                "title": "Repetitions",
                "brief": "repetitions",
                "type": "integer",
                "units": "",
                "minimum": 0,
                "options": {
                    "inputAttributes": {
                        "placeholder": "integer"
                    },
                    "infoText": "The number of times the inhalation procedure is repeated, relevant in protocols requiring multiple dosages or sessions."
                }
            },
            "inhalationPhase": {
                "title": "Inhalation phase",
                "brief": "inhalation phase",
                "type": "string",
                "format": "text",
                "options": {
                    "infoText": "Is the odor presented at a specific inhalation phase?"
                }
            }
        }
    }
}
```

## OptogeneticStimulation
```
{
    "type": "array",
    "minItems": 1,
    "format": "table",
    "title": "Optogenetic Stimulation",
    "options": {
        "compact": "true",
        "enable_array_copy": true,
        "disable_properties": false,
        "disable_edit_json": false,
        "disable_array_delete_last_row": true,
        "disable_array_delete_all_rows": true,
        "no_additional_properties": true
    },
    "items": {
        "type": "object",
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false,
        "properties": {
            "power": {
                "title": "Power (mW)",
                "units": "mW",
                "type": "number",
                "format": "number",
                "options": {
                    "infoText": "The output power of the light source used for stimulation, measured in milliwatts, which affects the intensity and efficacy of the stimulation."
                }
            },
            "amplitude": {
                "title": "Amplitude (A)",
                "units": "A",
                "type": "number",
                "options": {
                    "infoText": "The peak amplitude of the light signal, which can influence the activation threshold and response of optogenetic actuators."
                }
            },
            "profile": {
                "title": "Stimulation profile",
                "brief": "profile",
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
                ],
                "options": {
                    "infoText": "The pattern or waveform of the light used during stimulation, critical for achieving specific neuronal responses and study outcomes."
                }
            },
            "duration": {
                "title": "Duration (s)",
                "units": "s",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "The length of time each light stimulation lasts, measured in seconds, crucial for timing the activation and deactivation of optogenetic channels."
                }
            },
            "dutyCycle": {
                "title": "Duty cycle",
                "type": "number",
                "units": "",
                "minimum": 0,
                "options": {
                    "infoText": "The fraction of one period in which a signal or system is active, impacting the temporal dynamics of light exposure."
                }
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "integer",
                "units": "",
                "minimum": 0,
                "options": {
                    "inputAttributes": {
                        "placeholder": "integer"
                    },
                    "infoText": "The number of times the stimulation is repeated, important for protocols that require multiple activations to assess cumulative effects or recovery."
                }
            },
            "wavelength": {
                "title": "Wavelength (nm)",
                "units": "nm",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "The wavelength of the light used, measured in nanometers, selected based on the activation spectrum of the specific optogenetic actuators used."
                }
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox",
                "options": {
                    "infoText": "Indicates whether the stimulation parameters can be automatically adjusted based on feedback from sensors or other measurements, enhancing precision and responsiveness."
                }
            }
        }
    }
}
```

## PharmacologicalInhalation
```
{
    "type": "array",
    "minItems": 1,
    "format": "table",
    "title": "Pharmacological Inhalation",
    "options": {
        "compact": "true",
        "enable_array_copy": true,
        "disable_properties": false,
        "disable_edit_json": false,
        "disable_array_delete_last_row": true,
        "disable_array_delete_all_rows": true,
        "no_additional_properties": true
    },
    "items": {
        "type": "object",
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false,
        "properties": {
            "liquidAgent": {
                "title": "Liquid agent",
                "type": "string",
                "format": "text",
                "options": {
                    "infoText": "The specific agent or medication administered through inhalation, which could be a bronchodilator, steroid, or other therapeutic substance."
                }
            },
            "concentration": {
                "title": "Concentration (mg/mL)",
                "units": "mg/mL",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "The concentration of the liquid agent in the inhalation mixture, typically specified in percentage or mg/mL, crucial for dosing."
                }
            },
            "flowRate": {
                "title": "Flow rate (\u00b5L/min)",
                "units": "\u00b5L/min",
                "type": "number",
                "options": {
                    "infoText": "The rate at which the inhalation agent is delivered to the patient, measured in microliters per minute, determining the speed and extent of administration."
                }
            },
            "profile": {
                "title": "Stimulation profile",
                "brief": "profile",
                "type": "string",
                "enum": [
                    "Bolus Inhalation",
                    "Continuous Inhalation",
                    "Controlled Release Inhalation",
                    "Deep Lung Inhalation",
                    "High-Frequency Inhalation",
                    "Holding Breath",
                    "Low Volume Inhalation",
                    "Positive Pressure Inhalation",
                    "Pulse Inhalation",
                    "Ramp Inhalation",
                    "Rescue Inhalation",
                    "Stacked Breathing",
                    "Tidal Breathing"
                ],
                "options": {
                    "infoText": "The method or pattern of inhalation used, which can affect the distribution and absorption of the agent within the respiratory tract."
                }
            },
            "volume": {
                "title": "Volume (\u00b5L)",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "Total volume of the inhalation agent administered per session, important for ensuring therapeutic effectiveness and safety."
                }
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "integer",
                "units": "",
                "minimum": 0,
                "options": {
                    "inputAttributes": {
                        "placeholder": "integer"
                    },
                    "infoText": "The number of times the inhalation procedure is repeated, relevant in protocols requiring multiple dosages or sessions."
                }
            },
            "analgesic": {
                "title": "Analgesic",
                "type": "string",
                "format": "text",
                "options": {
                    "infoText": "Details any analgesic properties of the inhaled substance, particularly in contexts where pain management is a focus."
                }
            },
            "sedative": {
                "title": "Sedative",
                "type": "string",
                "format": "text",
                "options": {
                    "infoText": "Details any sedative components of the inhalation therapy, often used in procedures requiring patient relaxation or reduced anxiety."
                }
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox",
                "options": {
                    "infoText": "Indicates if the inhalation system adjusts the flow, volume, or dosage based on feedback, such as patient respiratory rate or drug absorption levels, to optimize therapeutic outcomes."
                }
            }
        }
    }
}
```

## PharmacologicalInjection
```
{
    "type": "array",
    "minItems": 1,
    "format": "table",
    "title": "Pharmacological Injection",
    "options": {
        "compact": "true",
        "enable_array_copy": true,
        "disable_properties": false,
        "disable_edit_json": false,
        "disable_array_delete_last_row": true,
        "disable_array_delete_all_rows": true,
        "no_additional_properties": true
    },
    "items": {
        "type": "object",
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false,
        "properties": {
            "liquidAgent": {
                "title": "Liquid agent",
                "type": "string",
                "format": "text",
                "options": {
                    "infoText": "The type or name of the pharmacological agent administered, specifying the drug or compound used in the injection."
                }
            },
            "concentration": {
                "title": "Concentration (mg/mL)",
                "units": "mg/mL",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "The concentration of the active ingredient in the injection solution, usually specified in mg/mL, essential for dosing accuracy."
                }
            },
            "volume": {
                "title": "Volume (\u00b5L)",
                "units": "\u00b5L",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "The total volume of the injection given, measured in microliters, critical for ensuring the precise amount of the agent is administered."
                }
            },
            "profile": {
                "title": "Injection profile",
                "brief": "profile",
                "type": "string",
                "enum": [
                    "Bolus Injection",
                    "Continuous Infusion",
                    "Tapered Dose",
                    "Intermittent Bolus",
                    "Staggered Injection",
                    "Ramp Infusion",
                    "Burst Infusion",
                    "Step Infusion",
                    "Layered Dosing",
                    "Titration"
                ],
                "options": {
                    "infoText": "The method of injection used, which determines how the agent is delivered over time, affecting its pharmacokinetics and dynamics."
                }
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "integer",
                "units": "",
                "minimum": 0,
                "options": {
                    "inputAttributes": {
                        "placeholder": "integer"
                    },
                    "infoText": "The number of times the injection is administered, important for treatments requiring multiple doses to achieve therapeutic effects."
                }
            },
            "flowRate": {
                "title": "Flow rate (\u00b5L/min)",
                "units": "\u00b5L/min",
                "type": "number",
                "options": {
                    "infoText": "The rate at which the injection is administered, measured in microliters per minute, which can influence the absorption and effect of the agent."
                }
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox",
                "options": {
                    "infoText": "Specifies whether the injection system automatically adjusts based on feedback mechanisms, such as patient response, to optimize the dosing."
                }
            }
        }
    }
}
```

## PharmacologicalSuperfusion
```
{
    "type": "array",
    "minItems": 1,
    "format": "table",
    "title": "Pharmacological Superfusion",
    "options": {
        "compact": "true",
        "enable_array_copy": true,
        "disable_properties": false,
        "disable_edit_json": false,
        "disable_array_delete_last_row": true,
        "disable_array_delete_all_rows": true,
        "no_additional_properties": true
    },
    "items": {
        "type": "object",
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false,
        "properties": {
            "liquidAgent": {
                "title": "Liquid agent",
                "type": "string",
                "format": "text",
                "options": {
                    "infoText": "The chemical or pharmacological agent used in the superfusion, specifying its scientific or common name."
                }
            },
            "concentration": {
                "title": "Concentration (mg/mL)",
                "units": "mg/mL",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "The concentration of the liquid agent within the superfusion solution, usually specified in percentage or mg/mL, critical for achieving the desired biological effect."
                }
            },
            "volume": {
                "title": "Volume (\u00b5L)",
                "units": "\u00b5L",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "The total volume of the superfusion fluid used throughout the experiment or procedure, which helps in determining the extent of exposure."
                }
            },
            "profile": {
                "title": "Superfusion profile",
                "brief": "profile",
                "type": "string",
                "enum": [
                    "Bolus Injection",
                    "Continuous Infusion",
                    "Tapered Dose",
                    "Intermittent Bolus",
                    "Staggered Injection",
                    "Ramp Infusion",
                    "Burst Infusion",
                    "Step Infusion",
                    "Layered Dosing",
                    "Titration"
                ],
                "options": {
                    "infoText": "The pattern or method of superfusion, which defines how the agent is applied over time to the biological system or tissue."
                }
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "integer",
                "units": "",
                "minimum": 0,
                "options": {
                    "inputAttributes": {
                        "placeholder": "integer"
                    },
                    "infoText": "The number of cycles or iterations of superfusion performed during the experiment, essential for protocols requiring repeated applications."
                }
            },
            "flowRate": {
                "title": "Flow rate (\u00b5L/min)",
                "units": "\u00b5L/min",
                "type": "number",
                "options": {
                    "infoText": "The rate at which the superfusion solution is applied, measured in microliters per minute, influencing the rate of agent delivery and tissue contact."
                }
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox",
                "options": {
                    "infoText": "Indicates if the superfusion system adjusts the delivery parameters dynamically based on real-time feedback from sensors or other measurements, ensuring optimal dosing and application consistency."
                }
            }
        }
    }
}
```

## TactileStimulation
```
{
    "type": "array",
    "minItems": 1,
    "format": "table",
    "title": "Tactile stimulation",
    "options": {
        "compact": "true",
        "enable_array_copy": true,
        "disable_properties": false,
        "disable_edit_json": false,
        "disable_array_delete_last_row": true,
        "disable_array_delete_all_rows": true,
        "no_additional_properties": true
    },
    "items": {
        "type": "object",
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false,
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
                ],
                "options": {
                    "infoText": "General type of tactile interaction used for stimulation. Includes contact-based and non-contact methods like air puffs."
                }
            },
            "site": {
                "title": "Stimulation site",
                "type": "string",
                "options": {
                    "infoText": "The anatomical location where the tactile stimulus is applied, e.g., 'whisker pad', 'forepaw', or 'tail'."
                }
            },
            "force": {
                "title": "Force (mN)",
                "units": "mN",
                "type": "number",
                "options": {
                    "infoText": "Approximate mechanical force applied during stimulation, in milliNewtons. Can be estimated if not measured precisely."
                }
            },
            "duration": {
                "title": "Duration (s)",
                "units": "s",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "Duration for which the tactile stimulus is applied, measured in seconds."
                }
            },
            "profile": {
                "title": "Stimulation profile",
                "brief": "profile",
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
                ],
                "options": {
                    "infoText": "Temporal profile or shape of the stimulation waveform. 'Manual' can be selected if triggered by hand."
                }
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "integer",
                "units": "",
                "minimum": 0,
                "options": {
                    "inputAttributes": {
                        "placeholder": "integer"
                    },
                    "infoText": "Number of times the tactile stimulus is delivered, useful for repeated trial-based experiments."
                }
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox",
                "options": {
                    "infoText": "Indicates whether stimulation is delivered based on real-time behavioral or physiological signals."
                }
            }
        }
    }
}
```

## ThermalPerturbation
```
{
    "type": "array",
    "minItems": 1,
    "format": "table",
    "title": "Thermal Perturbation",
    "options": {
        "compact": "true",
        "enable_array_copy": true,
        "disable_properties": false,
        "disable_edit_json": false,
        "disable_array_delete_last_row": true,
        "disable_array_delete_all_rows": true,
        "no_additional_properties": true,
        "use_type_default_value": false
    },
    "items": {
        "type": "object",
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false,
        "properties": {
            "amplitude": {
                "title": "Amplitude (\u00b0C)",
                "units": "\u00b0C",
                "type": "number",
                "options": {
                    "infoText": "The maximum change in temperature from the baseline or ambient level, measured in degrees Celsius, defining the intensity of the thermal stimulus."
                }
            },
            "duration": {
                "title": "Duration (s)",
                "units": "s",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "The length of time for which the thermal stimulus is applied, measured in seconds. This parameter is crucial for understanding the temporal impact of the stimulus on the subject or system."
                }
            },
            "profile": {
                "title": "Thermal profile",
                "brief": "profile",
                "type": "string",
                "enum": [
                    "Amplitude Modulated",
                    "Burst",
                    "Chirp",
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
                ],
                "options": {
                    "infoText": "Describes the pattern or modulation of the thermal stimulus, which can influence the thermal response of the biological or material system being studied."
                }
            },
            "dutyCycle": {
                "title": "Duty cycle",
                "type": "number",
                "units": "",
                "minimum": 0,
                "options": {
                    "infoText": "Represents the fraction of the total period during which the thermal stimulus is active, expressed as a fraction. This affects the pattern of temperature variation and can be crucial in cyclic thermal tests."
                }
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "integer",
                "units": "",
                "minimum": 0,
                "options": {
                    "inputAttributes": {
                        "placeholder": "integer"
                    },
                    "infoText": "The number of times the thermal stimulus is repeated during an experiment, important for studies investigating the effects of repeated thermal exposure."
                }
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox",
                "options": {
                    "infoText": "Indicates whether the thermal control system automatically adjusts based on feedback, which can be essential for maintaining precise temperature conditions throughout the experiment."
                }
            }
        }
    }
}
```

## TranscranialElectricalStimulation
```
{
    "type": "array",
    "minItems": 1,
    "format": "table",
    "title": "Transcranial Electrical Stimulation",
    "options": {
        "compact": "true",
        "enable_array_copy": true,
        "disable_properties": false,
        "disable_edit_json": false,
        "disable_array_delete_last_row": true,
        "disable_array_delete_all_rows": true,
        "no_additional_properties": true
    },
    "items": {
        "type": "object",
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false,
        "properties": {
            "amplitude": {
                "title": "Amplitude (mA)",
                "units": "mA",
                "type": "number",
                "options": {
                    "infoText": "The intensity of the electrical current applied, measured in milliamperes (mA). This is a crucial parameter as it influences the depth and effect of stimulation."
                }
            },
            "duration": {
                "title": "Duration (s)",
                "units": "s",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "The length of time each stimulation session lasts, typically measured in seconds or minutes. This affects how long the brain regions are stimulated during the procedure."
                }
            },
            "profile": {
                "title": "Stimulation profile",
                "brief": "profile",
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
                ],
                "options": {
                    "infoText": "Describes the waveform or modulation method used during stimulation, each having different neurological impacts and applications."
                }
            },
            "dutyCycle": {
                "title": "Duty cycle",
                "type": "number",
                "units": "",
                "minimum": 0,
                "options": {
                    "infoText": "The ratio of the stimulation 'on' time to the total cycle period, expressed as a fraction. This can affect the therapy\u2019s effectiveness and comfort level."
                }
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "integer",
                "units": "",
                "minimum": 0,
                "options": {
                    "inputAttributes": {
                        "placeholder": "integer"
                    },
                    "infoText": "The number of times the stimulation cycle is repeated during a session. Multiple repetitions can enhance the stimulation effects."
                }
            },
            "injectionPolarity": {
                "title": "Injection polarity",
                "type": "string",
                "format": "text",
                "options": {
                    "infoText": "Refers typically to the directionality of current flow in other contexts; here, it might be better defined or replaced with polarity related to electrode setup."
                }
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox",
                "options": {
                    "infoText": "Indicates whether the system uses feedback from the patient's physiological responses to automatically adjust stimulation parameters."
                }
            }
        }
    }
}
```

## TranscranialMagneticStimulation
```
{
    "type": "array",
    "minItems": 1,
    "format": "table",
    "title": "Transcranial Electrical Stimulation",
    "options": {
        "compact": "true",
        "enable_array_copy": true,
        "disable_properties": false,
        "disable_edit_json": false,
        "disable_array_delete_last_row": true,
        "disable_array_delete_all_rows": true,
        "no_additional_properties": true
    },
    "items": {
        "type": "object",
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false,
        "properties": {
            "amplitude": {
                "title": "Amplitude (mA)",
                "brief": "amplitude",
                "units": "mA",
                "type": "number",
                "options": {
                    "infoText": "Specifies the intensity of the electrical current used in stimulation, measured in milliamperes (mA)."
                }
            },
            "duration": {
                "title": "Duration (s)",
                "brief": "duration",
                "units": "s",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "Defines the total time each stimulation lasts, measured in seconds or milliseconds."
                }
            },
            "profile": {
                "title": "Stimulation profile",
                "brief": "profile",
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
                ],
                "options": {
                    "infoText": "Describes the waveform type of the electrical signal. Different profiles influence brain activity in varying ways."
                }
            },
            "dutyCycle": {
                "title": "Duty cycle",
                "brief": "duty cycle",
                "units": "",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "The fraction of one period in which a signal or system is active. Affects the frequency and effect of the pulses."
                }
            },
            "repetitions": {
                "title": "Repetitions",
                "brief": "repetitions",
                "units": "",
                "type": "integer",
                "minimum": 0,
                "options": {
                    "inputAttributes": {
                        "placeholder": "integer"
                    },
                    "infoText": "The number of times the stimulation is repeated during a session. More repetitions can increase the effectiveness or risk of side effects."
                }
            },
            "injectionPolarity": {
                "title": "Injection polarity",
                "brief": "polarity",
                "type": "string",
                "format": "text",
                "options": {
                    "infoText": "Typically refers to the directionality of the current in conventional terms; it is important to specify whether it's anodal or cathodal in transcranial applications."
                }
            },
            "closedLoop": {
                "title": "Closed loop",
                "brief": "closed loop",
                "type": "boolean",
                "format": "checkbox",
                "options": {
                    "infoText": "Indicates if the stimulation system adjusts parameters in real-time based on feedback to achieve desired outcomes."
                }
            }
        }
    }
}
```

## UltrasoundStimulation
```
{
    "type": "array",
    "minItems": 1,
    "format": "table",
    "title": "Ultrasound Stimulation",
    "options": {
        "compact": "true",
        "enable_array_copy": true,
        "disable_properties": false,
        "disable_edit_json": false,
        "disable_array_delete_last_row": true,
        "disable_array_delete_all_rows": true,
        "no_additional_properties": true
    },
    "items": {
        "type": "object",
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false,
        "properties": {
            "amplitude": {
                "title": "Amplitude (V)",
                "brief": "amplitude",
                "units": "V",
                "type": "number",
                "options": {
                    "infoText": "The intensity of the ultrasound waves, measured in volts or as a mechanical index."
                }
            },
            "duration": {
                "title": "Duration (s)",
                "brief": "duration",
                "type": "number",
                "units": "s",
                "minimum": 0,
                "options": {
                    "infoText": "The total time each ultrasound session lasts, measured in seconds, which influences the therapeutic outcomes."
                }
            },
            "dutyCycle": {
                "title": "Duty cycle",
                "brief": "duty cycle",
                "units": "",
                "type": "number",
                "minimum": 0,
                "options": {
                    "infoText": "The ratio of the 'on' time to the total period of the ultrasound pulse cycle, expressed as a fraction. Impacting the intensity and effect of the treatment."
                }
            },
            "profile": {
                "title": "Stimulation profile",
                "brief": "profile",
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
                ],
                "options": {
                    "infoText": "Specifies the pattern or type of ultrasound waves used, which can affect the biological impact on targeted tissues."
                }
            },
            "repetitions": {
                "title": "Repetitions",
                "brief": "repetitions",
                "units": "",
                "type": "integer",
                "minimum": 0,
                "options": {
                    "inputAttributes": {
                        "placeholder": "integer"
                    },
                    "infoText": "The number of times the ultrasound pulses are repeated within a session, affecting cumulative dose and efficacy."
                }
            },
            "injectionPolarity": {
                "title": "Injection polarity",
                "brief": "polarity",
                "type": "string",
                "format": "text",
                "options": {
                    "infoText": "Typically refers to the polarity of electrical input in electromechanical systems; may need clarification or context-specific definition."
                }
            },
            "closedLoop": {
                "title": "Closed loop",
                "brief": "closed loop",
                "type": "boolean",
                "format": "checkbox",
                "options": {
                    "infoText": "Indicates whether the stimulation parameters are dynamically adjusted in response to real-time feedback from physiological sensors or biomarkers."
                }
            }
        }
    }
}
```

## VisualStimulation
```
{
    "type": "array",
    "minItems": 1,
    "format": "table",
    "title": "Visual stimulation",
    "options": {
        "compact": "true",
        "enable_array_copy": true,
        "disable_properties": false,
        "disable_edit_json": false,
        "disable_array_delete_last_row": true,
        "disable_array_delete_all_rows": true,
        "no_additional_properties": true,
        "use_type_default_value": false
    },
    "items": {
        "type": "object",
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false,
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
                "uniqueItems": true,
                "options": {
                    "infoText": "Select one or more visual stimulus types used in this stimulation event."
                }
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
                ],
                "options": {
                    "infoText": "Device used to deliver the visual stimulus to the subject."
                }
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
                ],
                "options": {
                    "infoText": "Location of the stimulus relative to the subject's visual field."
                }
            },
            "duration": {
                "title": "Duration (s)",
                "type": "number",
                "minimum": 0,
                "units": "s",
                "options": {
                    "infoText": "Duration of this visual stimulus presentation, in seconds."
                }
            },
            "repetitions": {
                "title": "Repetitions",
                "type": "integer",
                "minimum": 0,
                "options": {
                    "inputAttributes": {
                        "placeholder": "integer"
                    },
                    "infoText": "Number of times this visual stimulus was repeated."
                }
            },
            "closedLoop": {
                "title": "Closed loop",
                "type": "boolean",
                "format": "checkbox",
                "options": {
                    "infoText": "Whether the visual stimulus was dynamically adapted to the subject's behavior or physiological signals."
                }
            }
        }
    }
}
```

