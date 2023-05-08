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

## Electrical stimulation
```
{
    "type": "object",
    "title": "ElectricalStimulation",
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
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "amplitude": 15,
    "duration": 300,
    "dutyCycle": 3,
    "repetitions": 40,
    "injectionPolarity": "positive",
    "fatalOutcome": True,
    "closedLoop": True
}
```

## Electromagnetic field stimulation
```
{
    "type": "object",
    "title": "ElectromagneticFieldStimulation",
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
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "amplitude": 15,
    "duration": 300,
    "dutyCycle": 3,
    "repetitions": 40,
    "injectionPolarity": "positive",
    "fatalOutcome": True,
    "closedLoop": True
}
```

## Liquid perturbation
```
{
    "type": "object",
    "title": "LiquidPerturbation",
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
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "liquidAgent": "ethanol",
    "concentration": 0.15,
    "volume": 7.2,
    "repetitions": 15,
    "flowRate": 4,
    "fatalOutcome": False,
    "closedLoop": True
}
```

## Microperfusion
```
{
    "type": "object",
    "title": "Microperfusion",
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
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "liquidAgent": "ethanol",
    "concentration": 0.15,
    "volume": 7.2,
    "repetitions": 15,
    "flowRate": 4,
    "fatalOutcome": False,
    "closedLoop": True
}
```

## Optogenetical stimulation
```
{
    "type": "object",
    "title": "OptogeneticalStimulation",
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
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "power": 66.6,
    "amplitude": 32,
    "duration": 300,
    "dutyCycle": {
        "title": "Duty cycle",
        "type": "number",
        "minimum": 0
    },
    "repetitions": 23,
    "wavelength": 42,
    "fatalOutcome": True,
    "closedLoop": False
}
```

## Pharmacological inhalation
```
{
    "type": "object",
    "title": "PharmacologicalInhalation",
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
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "liquidAgent": "ethanol",
    "concentration": 0.15,
    "volume": 7.2,
    "repetitions": 15,
    "analgesic": "Ibuprofen",
    "sedative": "Valium,
    "flowRate": 4,
    "fatalOutcome": False,
    "closedLoop": True
}
```

## Pharmacological injection
```
{
    "type": "object",
    "title": "PharmacologicalInjection",
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
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "liquidAgent": "ethanol",
    "concentration": 0.15,
    "volume": 7.2,
    "repetitions": 15,
    "flowRate": 4,
    "fatalOutcome": False,
    "closedLoop": True
}
```

## Pharmacological superfusion
```
{
    "type": "object",
    "title": "PharmacologicalSuperfusion",
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
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "liquidAgent": "ethanol",
    "concentration": 0.15,
    "volume": 7.2,
    "repetitions": 15,
    "flowRate": 4,
    "fatalOutcome": False,
    "closedLoop": True
}
```

## Sound stimulation
```
{
    "type": "object",
    "title": "SoundStimulation",
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
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "amplitude": 15,
    "duration": 300,
    "dutyCycle": 3,
    "repetitions": 40,
    "injectionPolarity": "positive",
    "fatalOutcome": True,
    "closedLoop": True
}
```

## Optic fiber implant
```
{
    "type": "object",
    "title": "ThermalPerturbation",
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
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "amplitude": 15,
    "duration": 300,
    "dutyCycle": 3,
    "repetitions": 40,
    "fatalOutcome": True,
    "closedLoop": True
}
```

## Optic fiber implant
```
{
    "type": "object",
    "title": "TranscranialElectricalStimulation",
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
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "amplitude": 15,
    "duration": 300,
    "dutyCycle": 3,
    "repetitions": 40,
    "injectionPolarity": "positive",
    "fatalOutcome": True,
    "closedLoop": True
}
```

## Optic fiber implant
```
{
    "type": "object",
    "title": "UltraSoundStimulation",
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
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "amplitude": 15,
    "duration": 300,
    "dutyCycle": 3,
    "repetitions": 40,
    "injectionPolarity": "positive",
    "fatalOutcome": True,
    "closedLoop": True
}
```
