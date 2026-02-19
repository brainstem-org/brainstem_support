---
layout: default
title: Manipulation
parent: Schemas
grand_parent: API
nav_order: 5
---

# Manipulation schemas
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## How to use this page

- Use this page when calling `/api/private/modules/manipulation/`.
- Set `type` to one schema name from the list below.
- Send `details` that matches that schema exactly.
- Manipulation schemas are table-like arrays (`details` is typically a list of row objects).

## Quick type map

| Type value | Schema version | Required fields | Schema shape |
|:-----------|:---------------|:----------------|:-------------|
| `AuditoryStimulation` | `1.1.0` | none | `array items` |
| `DeepBrainStimulation` | `1.1.0` | none | `array items` |
| `ElectricalStimulation` | `1.1.0` | none | `array items` |
| `ElectromagneticFieldStimulation` | `1.1.0` | none | `array items` |
| `LiquidPerturbation` | `1.1.0` | none | `array items` |
| `Microperfusion` | `1.1.0` | none | `array items` |
| `MultisensoryStimulation` | `1.1.0` | none | `array items` |
| `OdorStimulation` | `1.1.0` | none | `array items` |
| `OptogeneticStimulation` | `1.1.0` | none | `array items` |
| `PharmacologicalInhalation` | `1.1.0` | none | `array items` |
| `PharmacologicalInjection` | `1.1.0` | none | `array items` |
| `PharmacologicalSuperfusion` | `1.1.0` | none | `array items` |
| `TactileStimulation` | `1.1.0` | none | `array items` |
| `ThermalPerturbation` | `1.1.0` | none | `array items` |
| `TranscranialElectricalStimulation` | `1.1.0` | none | `array items` |
| `TranscranialMagneticStimulation` | `1.1.0` | none | `array items` |
| `UltrasoundStimulation` | `1.1.0` | none | `array items` |
| `VisualStimulation` | `1.1.0` | none | `array items` |

## Examples

### Manipulation payload fragment
```json
{
  "type": "AuditoryStimulation",
  "details": [
    {
      "amplitude": {
        "unit": "dB",
        "value": 0
      },
      "duration": {
        "unit": "s",
        "value": 0
      },
      "frequency": {
        "unit": "Hz",
        "value": 0
      },
      "modulationFrequency": {
        "unit": "Hz",
        "value": 0
      }
    }
  ]
}
```

## Request pattern
```json
{
  "type": "AuditoryStimulation",
  "details": [
    {
      "amplitude": {
        "unit": "dB",
        "value": 0
      },
      "duration": {
        "unit": "s",
        "value": 0
      },
      "frequency": {
        "unit": "Hz",
        "value": 0
      },
      "modulationFrequency": {
        "unit": "Hz",
        "value": 0
      }
    }
  ]
}
```

## Schema reference

### `AuditoryStimulation`
- **Schema title:** Auditory stimulation
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Manipulation/AuditoryStimulation.json`
- **Schema shape:** `array items`
- **Required fields:** none

Example payload for this type:
```json
[
  {
    "amplitude": {
      "unit": "dB",
      "value": 0
    },
    "duration": {
      "unit": "s",
      "value": 0
    },
    "frequency": {
      "unit": "Hz",
      "value": 0
    },
    "modulationFrequency": {
      "unit": "Hz",
      "value": 0
    }
  }
]
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `amplitude` | `object(value:number, unit:enum[dB, dB SPL, Pa])` | no | format="numberUnit"; default={"unit": "dB"} |
| `closedLoop` | `boolean` | no | format="checkbox" |
| `duration` | `object(value:number, unit:enum[s, ms, µs, min, h])` | no | format="numberUnit"; default={"unit": "s"} |
| `dutyCycle` | `number` | no | minimum=0 |
| `frequency` | `object(value:number, unit:enum[Hz, kHz, MHz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `modulationFrequency` | `object(value:number, unit:enum[Hz, kHz, MHz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `profile` | `string` | no | enum=["Amplitude Modulated", "Alternating Current", "Biphasic", "Burst", "Chirp", "Direct Current", "Cosine", "Frequency Hopping", "Frequency Modulated", "Decaying Exponential", "Gaussian Pulse", "Harmonic Stimulation", "Gaussian Noise", "Pseudo-random Binary Sequence", "Pink Noise", "Pulse train", "Sawtooth", "Staircase", "Sine Wave", "Sinc Pulse", "Square", "Stochastic", "Step Function", "Ramp", "Rising Exponential", "Trapezoidal Pulse", "Triangle", "Variable Rate Pulse Train", "White Noise"] |
| `repetitions` | `integer` | no | minimum=0 |

### `DeepBrainStimulation`
- **Schema title:** DeepBrainStimulation
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Manipulation/DeepBrainStimulation.json`
- **Schema shape:** `array items`
- **Required fields:** none

Example payload for this type:
```json
[
  {
    "amplitude": {
      "unit": "A",
      "value": 0
    },
    "duration": {
      "unit": "s",
      "value": 0
    },
    "profile": "Amplitude Modulated",
    "dutyCycle": 0
  }
]
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `amplitude` | `object(value:number, unit:enum[A, mA, µA, nA])` | no | format="numberUnit"; default={"unit": "A"} |
| `closedLoop` | `boolean` | no | format="checkbox" |
| `duration` | `object(value:number, unit:enum[s, ms, µs, min, h])` | no | format="numberUnit"; default={"unit": "s"} |
| `dutyCycle` | `number` | no | minimum=0 |
| `injectionPolarity` | `string` | no | format="text" |
| `profile` | `string` | no | enum=["Amplitude Modulated", "Alternating Current", "Biphasic", "Burst", "Chirp", "Direct Current", "Cosine", "Frequency Hopping", "Frequency Modulated", "Decaying Exponential", "Gaussian Pulse", "Harmonic Stimulation", "Gaussian Noise", "Pseudo-random Binary Sequence", "Pink Noise", "Pulse train", "Sawtooth", "Staircase", "Sine Wave", "Sinc Pulse", "Square", "Stochastic", "Step Function", "Ramp", "Rising Exponential", "Trapezoidal Pulse", "Triangle", "Variable Rate Pulse Train", "White Noise"] |
| `repetitions` | `integer` | no | minimum=0 |

### `ElectricalStimulation`
- **Schema title:** Electrical Stimulation
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Manipulation/ElectricalStimulation.json`
- **Schema shape:** `array items`
- **Required fields:** none

Example payload for this type:
```json
[
  {
    "amplitude": {
      "unit": "V",
      "value": 0
    },
    "duration": {
      "unit": "s",
      "value": 0
    },
    "profile": "Amplitude Modulated",
    "dutyCycle": 0
  }
]
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `amplitude` | `object(value:number, unit:enum[V, mV, µV])` | no | format="numberUnit"; default={"unit": "V"} |
| `closedLoop` | `boolean` | no | format="checkbox" |
| `duration` | `object(value:number, unit:enum[s, ms, µs, min, h])` | no | format="numberUnit"; default={"unit": "s"} |
| `dutyCycle` | `number` | no | minimum=0 |
| `injectionPolarity` | `string` | no | format="text" |
| `profile` | `string` | no | enum=["Amplitude Modulated", "Alternating Current", "Biphasic", "Burst", "Chirp", "Direct Current", "Cosine", "Frequency Hopping", "Frequency Modulated", "Decaying Exponential", "Gaussian Pulse", "Harmonic Stimulation", "Gaussian Noise", "Pseudo-random Binary Sequence", "Pink Noise", "Pulse train", "Sawtooth", "Staircase", "Sine Wave", "Sinc Pulse", "Square", "Stochastic", "Step Function", "Ramp", "Rising Exponential", "Trapezoidal Pulse", "Triangle", "Variable Rate Pulse Train", "White Noise"] |
| `repetitions` | `integer` | no | minimum=0 |

### `ElectromagneticFieldStimulation`
- **Schema title:** Electromagnetic Field Stimulation
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Manipulation/ElectromagneticFieldStimulation.json`
- **Schema shape:** `array items`
- **Required fields:** none

Example payload for this type:
```json
[
  {
    "amplitude": {
      "unit": "V",
      "value": 0
    },
    "duration": {
      "unit": "s",
      "value": 0
    },
    "profile": "Amplitude Modulated",
    "dutyCycle": 0
  }
]
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `amplitude` | `object(value:number, unit:enum[V, mV, µV])` | no | format="numberUnit"; default={"unit": "V"} |
| `closedLoop` | `boolean` | no | format="checkbox" |
| `duration` | `object(value:number, unit:enum[s, ms, µs, min, h])` | no | format="numberUnit"; default={"unit": "s"} |
| `dutyCycle` | `number` | no | minimum=0 |
| `injectionPolarity` | `string` | no | format="text" |
| `profile` | `string` | no | enum=["Amplitude Modulated", "Alternating Current", "Biphasic", "Burst", "Chirp", "Direct Current", "Cosine", "Frequency Hopping", "Frequency Modulated", "Decaying Exponential", "Gaussian Pulse", "Harmonic Stimulation", "Gaussian Noise", "Pseudo-random Binary Sequence", "Pink Noise", "Pulse train", "Sawtooth", "Staircase", "Sine Wave", "Sinc Pulse", "Square", "Stochastic", "Step Function", "Ramp", "Rising Exponential", "Trapezoidal Pulse", "Triangle", "Variable Rate Pulse Train", "White Noise"] |
| `repetitions` | `integer` | no | minimum=0 |

### `LiquidPerturbation`
- **Schema title:** Liquid Perturbation
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Manipulation/LiquidPerturbation.json`
- **Schema shape:** `array items`
- **Required fields:** none

Example payload for this type:
```json
[
  {
    "liquidAgent": "example",
    "concentration": {
      "unit": "mg/mL",
      "value": 0
    },
    "volume": {
      "unit": "µL",
      "value": 0
    },
    "profile": "Bolus Injection"
  }
]
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `closedLoop` | `boolean` | no | format="checkbox" |
| `concentration` | `object(value:number, unit:enum[mg/mL, µg/mL, ng/mL, M, mM, µM, nM])` | no | format="numberUnit"; default={"unit": "mg/mL"} |
| `flowRate` | `object(value:number, unit:enum[µL/min, mL/min, L/min, nL/min, µL/s, mL/s])` | no | format="numberUnit"; default={"unit": "µL/min"} |
| `liquidAgent` | `string` | no | format="text" |
| `profile` | `string` | no | enum=["Bolus Injection", "Continuous Infusion", "Tapered Dose", "Intermittent Bolus", "Staggered Injection", "Ramp Infusion", "Burst Infusion", "Step Infusion", "Layered Dosing", "Titration"] |
| `repetitions` | `integer` | no | minimum=0 |
| `volume` | `object(value:number, unit:enum[µL, mL, L, nL])` | no | format="numberUnit"; default={"unit": "µL"} |

### `Microperfusion`
- **Schema title:** Microperfusion
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Manipulation/Microperfusion.json`
- **Schema shape:** `array items`
- **Required fields:** none

Example payload for this type:
```json
[
  {
    "liquidAgent": "example",
    "concentration": {
      "unit": "mg/mL",
      "value": 0
    },
    "volume": {
      "unit": "µL",
      "value": 0
    },
    "profile": "Bolus Injection"
  }
]
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `closedLoop` | `boolean` | no | format="checkbox" |
| `concentration` | `object(value:number, unit:enum[mg/mL, µg/mL, ng/mL, M, mM, µM, nM])` | no | format="numberUnit"; default={"unit": "mg/mL"} |
| `flowRate` | `object(value:number, unit:enum[µL/min, mL/min, L/min, nL/min, µL/s, mL/s])` | no | format="numberUnit"; default={"unit": "µL/min"} |
| `liquidAgent` | `string` | no | format="text" |
| `profile` | `string` | no | enum=["Bolus Injection", "Continuous Infusion", "Tapered Dose", "Intermittent Bolus", "Staggered Injection", "Ramp Infusion", "Burst Infusion", "Step Infusion", "Layered Dosing", "Titration"] |
| `repetitions` | `integer` | no | minimum=0 |
| `volume` | `object(value:number, unit:enum[µL, mL, L, nL])` | no | format="numberUnit"; default={"unit": "µL"} |

### `MultisensoryStimulation`
- **Schema title:** Multisensory stimulation
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Manipulation/MultisensoryStimulation.json`
- **Schema shape:** `array items`
- **Required fields:** none

Example payload for this type:
```json
[
  {
    "modalities": [],
    "synchronization": "Synchronous",
    "duration": {
      "unit": "s",
      "value": 0
    },
    "repetitions": 0
  }
]
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `closedLoop` | `boolean` | no | format="checkbox" |
| `duration` | `object(value:number, unit:enum[s, ms, µs, min, h])` | no | format="numberUnit"; default={"unit": "s"} |
| `modalities` | `array` | no | format="select" |
| `repetitions` | `integer` | no | minimum=0 |
| `synchronization` | `string` | no | enum=["Synchronous", "Asynchronous", "Randomized", "Unknown"] |

### `OdorStimulation`
- **Schema title:** Odor stimulation
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Manipulation/OdorStimulation.json`
- **Schema shape:** `array items`
- **Required fields:** none

Example payload for this type:
```json
[
  {
    "odor": "example",
    "concentration": {
      "unit": "mg/mL",
      "value": 0
    },
    "flowRate": {
      "unit": "mL/min",
      "value": 0
    },
    "repetitions": 0
  }
]
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `concentration` | `object(value:number, unit:enum[mg/mL, µg/mL, g/L, mg/L, µg/L, % w/v, % v/v, % w/w])` | no | format="numberUnit"; default={"unit": "mg/mL"} |
| `flowRate` | `object(value:number, unit:enum[mL/min, µL/min, mL/s, µL/s, L/min])` | no | format="numberUnit"; default={"unit": "mL/min"} |
| `inhalationPhase` | `string` | no | format="text" |
| `odor` | `string` | no | format="text" |
| `repetitions` | `integer` | no | minimum=0 |

### `OptogeneticStimulation`
- **Schema title:** Optogenetic Stimulation
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Manipulation/OptogeneticStimulation.json`
- **Schema shape:** `array items`
- **Required fields:** none

Example payload for this type:
```json
[
  {
    "power": {
      "unit": "mW",
      "value": 0
    },
    "profile": "Amplitude Modulated",
    "duration": {
      "unit": "s",
      "value": 0
    },
    "dutyCycle": 0
  }
]
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `closedLoop` | `boolean` | no | format="checkbox" |
| `duration` | `object(value:number, unit:enum[s, ms, µs, min, h])` | no | format="numberUnit"; default={"unit": "s"} |
| `dutyCycle` | `number` | no | minimum=0 |
| `power` | `object(value:number, unit:enum[W, mW, µW])` | no | format="numberUnit"; default={"unit": "mW"} |
| `profile` | `string` | no | enum=["Amplitude Modulated", "Alternating Current", "Biphasic", "Burst", "Chirp", "Direct Current", "Cosine", "Frequency Hopping", "Frequency Modulated", "Decaying Exponential", "Gaussian Pulse", "Harmonic Stimulation", "Gaussian Noise", "Pseudo-random Binary Sequence", "Pink Noise", "Pulse train", "Sawtooth", "Staircase", "Sine Wave", "Sinc Pulse", "Square", "Stochastic", "Step Function", "Ramp", "Rising Exponential", "Trapezoidal Pulse", "Triangle", "Variable Rate Pulse Train", "White Noise"] |
| `repetitions` | `integer` | no | minimum=0 |
| `wavelength` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "nm"} |

### `PharmacologicalInhalation`
- **Schema title:** Pharmacological Inhalation
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Manipulation/PharmacologicalInhalation.json`
- **Schema shape:** `array items`
- **Required fields:** none

Example payload for this type:
```json
[
  {
    "liquidAgent": "example",
    "concentration": {
      "unit": "mg/mL",
      "value": 0
    },
    "flowRate": {
      "unit": "µL/min",
      "value": 0
    },
    "profile": "Bolus Inhalation"
  }
]
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `analgesic` | `string` | no | format="text" |
| `closedLoop` | `boolean` | no | format="checkbox" |
| `concentration` | `object(value:number, unit:enum[mg/mL, µg/mL, g/L, mg/L, µg/L, % w/v, % v/v, % w/w])` | no | format="numberUnit"; default={"unit": "mg/mL"} |
| `flowRate` | `object(value:number, unit:enum[µL/min, mL/min, µL/s, mL/s, L/min])` | no | format="numberUnit"; default={"unit": "µL/min"} |
| `liquidAgent` | `string` | no | format="text" |
| `profile` | `string` | no | enum=["Bolus Inhalation", "Continuous Inhalation", "Controlled Release Inhalation", "Deep Lung Inhalation", "High-Frequency Inhalation", "Holding Breath", "Low Volume Inhalation", "Positive Pressure Inhalation", "Pulse Inhalation", "Ramp Inhalation", "Rescue Inhalation", "Stacked Breathing", "Tidal Breathing"] |
| `repetitions` | `integer` | no | minimum=0 |
| `sedative` | `string` | no | format="text" |
| `volume` | `object(value:number, unit:enum[L, mL, µL, nL, pL])` | no | format="numberUnit"; default={"unit": "µL"} |

### `PharmacologicalInjection`
- **Schema title:** Pharmacological Injection
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Manipulation/PharmacologicalInjection.json`
- **Schema shape:** `array items`
- **Required fields:** none

Example payload for this type:
```json
[
  {
    "liquidAgent": "example",
    "concentration": {
      "unit": "mg/mL",
      "value": 0
    },
    "volume": {
      "unit": "µL",
      "value": 0
    },
    "profile": "Bolus Injection"
  }
]
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `closedLoop` | `boolean` | no | format="checkbox" |
| `concentration` | `object(value:number, unit:enum[mg/mL, µg/mL, ng/mL, M, mM, µM, nM])` | no | format="numberUnit"; default={"unit": "mg/mL"} |
| `flowRate` | `object(value:number, unit:enum[µL/min, mL/min, L/min, nL/min, µL/s, mL/s])` | no | format="numberUnit"; default={"unit": "µL/min"} |
| `liquidAgent` | `string` | no | format="text" |
| `profile` | `string` | no | enum=["Bolus Injection", "Continuous Infusion", "Tapered Dose", "Intermittent Bolus", "Staggered Injection", "Ramp Infusion", "Burst Infusion", "Step Infusion", "Layered Dosing", "Titration"] |
| `repetitions` | `integer` | no | minimum=0 |
| `volume` | `object(value:number, unit:enum[µL, mL, L, nL])` | no | format="numberUnit"; default={"unit": "µL"} |

### `PharmacologicalSuperfusion`
- **Schema title:** Pharmacological Superfusion
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Manipulation/PharmacologicalSuperfusion.json`
- **Schema shape:** `array items`
- **Required fields:** none

Example payload for this type:
```json
[
  {
    "liquidAgent": "example",
    "concentration": {
      "unit": "mg/mL",
      "value": 0
    },
    "volume": {
      "unit": "µL",
      "value": 0
    },
    "profile": "Bolus Injection"
  }
]
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `closedLoop` | `boolean` | no | format="checkbox" |
| `concentration` | `object(value:number, unit:enum[mg/mL, µg/mL, ng/mL, M, mM, µM, nM])` | no | format="numberUnit"; default={"unit": "mg/mL"} |
| `flowRate` | `object(value:number, unit:enum[µL/min, mL/min, L/min, nL/min, µL/s, mL/s])` | no | format="numberUnit"; default={"unit": "µL/min"} |
| `liquidAgent` | `string` | no | format="text" |
| `profile` | `string` | no | enum=["Bolus Injection", "Continuous Infusion", "Tapered Dose", "Intermittent Bolus", "Staggered Injection", "Ramp Infusion", "Burst Infusion", "Step Infusion", "Layered Dosing", "Titration"] |
| `repetitions` | `integer` | no | minimum=0 |
| `volume` | `object(value:number, unit:enum[µL, mL, L, nL])` | no | format="numberUnit"; default={"unit": "µL"} |

### `TactileStimulation`
- **Schema title:** Tactile stimulation
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Manipulation/TactileStimulation.json`
- **Schema shape:** `array items`
- **Required fields:** none

Example payload for this type:
```json
[
  {
    "contactType": "Mechanical (contact)",
    "site": "example",
    "force": {
      "unit": "mN",
      "value": 0
    },
    "duration": {
      "unit": "s",
      "value": 0
    }
  }
]
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `closedLoop` | `boolean` | no | format="checkbox" |
| `contactType` | `string` | no | enum=["Mechanical (contact)", "Mechanical (vibration)", "Air puff", "Brush", "Cotton swab", "Other"] |
| `duration` | `object(value:number, unit:enum[s, ms, µs, min, h])` | no | format="numberUnit"; default={"unit": "s"} |
| `force` | `object(value:number, unit:enum[mN, N, µN, gf, kgf])` | no | format="numberUnit"; default={"unit": "mN"} |
| `profile` | `string` | no | enum=["Single pulse", "Pulse train", "Sinusoidal", "Square wave", "Sawtooth", "Burst", "Ramp", "Step function", "Manual"] |
| `repetitions` | `integer` | no | minimum=0 |
| `site` | `string` | no | — |

### `ThermalPerturbation`
- **Schema title:** Thermal Perturbation
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Manipulation/ThermalPerturbation.json`
- **Schema shape:** `array items`
- **Required fields:** none

Example payload for this type:
```json
[
  {
    "amplitude": {
      "unit": "°C",
      "value": 0
    },
    "duration": {
      "unit": "s",
      "value": 0
    },
    "profile": "Amplitude Modulated",
    "dutyCycle": 0
  }
]
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `amplitude` | `object(value:number, unit:enum[°C, K, °F])` | no | format="numberUnit"; default={"unit": "°C"} |
| `closedLoop` | `boolean` | no | format="checkbox" |
| `duration` | `object(value:number, unit:enum[s, ms, µs, min, h])` | no | format="numberUnit"; default={"unit": "s"} |
| `dutyCycle` | `number` | no | minimum=0 |
| `profile` | `string` | no | enum=["Amplitude Modulated", "Burst", "Chirp", "Decaying Exponential", "Gaussian Pulse", "Harmonic Stimulation", "Gaussian Noise", "Pseudo-random Binary Sequence", "Pink Noise", "Pulse train", "Sawtooth", "Staircase", "Sine Wave", "Sinc Pulse", "Square", "Stochastic", "Step Function", "Ramp", "Rising Exponential", "Trapezoidal Pulse", "Triangle", "Variable Rate Pulse Train", "White Noise"] |
| `repetitions` | `integer` | no | minimum=0 |

### `TranscranialElectricalStimulation`
- **Schema title:** Transcranial Electrical Stimulation
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Manipulation/TranscranialElectricalStimulation.json`
- **Schema shape:** `array items`
- **Required fields:** none

Example payload for this type:
```json
[
  {
    "amplitude": {
      "unit": "mA",
      "value": 0
    },
    "duration": {
      "unit": "s",
      "value": 0
    },
    "profile": "Amplitude Modulated",
    "dutyCycle": 0
  }
]
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `amplitude` | `object(value:number, unit:enum[A, mA, µA, nA])` | no | format="numberUnit"; default={"unit": "mA"} |
| `closedLoop` | `boolean` | no | format="checkbox" |
| `duration` | `object(value:number, unit:enum[s, ms, µs, min, h])` | no | format="numberUnit"; default={"unit": "s"} |
| `dutyCycle` | `number` | no | minimum=0 |
| `injectionPolarity` | `string` | no | format="text" |
| `profile` | `string` | no | enum=["Amplitude Modulated", "Alternating Current", "Biphasic", "Burst", "Chirp", "Direct Current", "Cosine", "Frequency Hopping", "Frequency Modulated", "Decaying Exponential", "Gaussian Pulse", "Harmonic Stimulation", "Gaussian Noise", "Pseudo-random Binary Sequence", "Pink Noise", "Pulse train", "Sawtooth", "Staircase", "Sine Wave", "Sinc Pulse", "Square", "Stochastic", "Step Function", "Ramp", "Rising Exponential", "Trapezoidal Pulse", "Triangle", "Variable Rate Pulse Train", "White Noise"] |
| `repetitions` | `integer` | no | minimum=0 |

### `TranscranialMagneticStimulation`
- **Schema title:** Transcranial Magnetic Stimulation
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Manipulation/TranscranialMagneticStimulation.json`
- **Schema shape:** `array items`
- **Required fields:** none

Example payload for this type:
```json
[
  {
    "amplitude": {
      "unit": "% MSO",
      "value": 0
    },
    "duration": {
      "unit": "s",
      "value": 0
    },
    "profile": "Amplitude Modulated",
    "dutyCycle": 0
  }
]
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `amplitude` | `object(value:number, unit:enum[% MSO, T, mT, µT])` | no | format="numberUnit"; default={"unit": "% MSO"} |
| `closedLoop` | `boolean` | no | format="checkbox" |
| `duration` | `object(value:number, unit:enum[s, ms, µs, min, h])` | no | format="numberUnit"; default={"unit": "s"} |
| `dutyCycle` | `number` | no | minimum=0 |
| `injectionPolarity` | `string` | no | format="text" |
| `profile` | `string` | no | enum=["Amplitude Modulated", "Alternating Current", "Biphasic", "Burst", "Chirp", "Direct Current", "Cosine", "Frequency Hopping", "Frequency Modulated", "Decaying Exponential", "Gaussian Pulse", "Harmonic Stimulation", "Gaussian Noise", "Pseudo-random Binary Sequence", "Pink Noise", "Pulse train", "Sawtooth", "Staircase", "Sine Wave", "Sinc Pulse", "Square", "Stochastic", "Step Function", "Ramp", "Rising Exponential", "Trapezoidal Pulse", "Triangle", "Variable Rate Pulse Train", "White Noise"] |
| `repetitions` | `integer` | no | minimum=0 |

### `UltrasoundStimulation`
- **Schema title:** Ultrasound Stimulation
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Manipulation/UltrasoundStimulation.json`
- **Schema shape:** `array items`
- **Required fields:** none

Example payload for this type:
```json
[
  {
    "acousticPressure": {
      "unit": "MPa",
      "value": 0
    },
    "acousticIntensity": {
      "unit": "W/cm²",
      "value": 0
    },
    "duration": {
      "unit": "s",
      "value": 0
    },
    "dutyCycle": 0
  }
]
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `acousticIntensity` | `object(value:number, unit:enum[W/cm², mW/cm²])` | no | format="numberUnit"; default={"unit": "W/cm²"} |
| `acousticPressure` | `object(value:number, unit:enum[Pa, kPa, MPa])` | no | format="numberUnit"; default={"unit": "MPa"} |
| `closedLoop` | `boolean` | no | format="checkbox" |
| `duration` | `object(value:number, unit:enum[s, ms, µs, min, h])` | no | format="numberUnit"; default={"unit": "s"} |
| `dutyCycle` | `number` | no | minimum=0 |
| `injectionPolarity` | `string` | no | format="text" |
| `profile` | `string` | no | enum=["Amplitude Modulated", "Alternating Current", "Biphasic", "Burst", "Chirp", "Direct Current", "Cosine", "Frequency Hopping", "Frequency Modulated", "Decaying Exponential", "Gaussian Pulse", "Harmonic Stimulation", "Gaussian Noise", "Pseudo-random Binary Sequence", "Pink Noise", "Pulse train", "Sawtooth", "Staircase", "Sine Wave", "Sinc Pulse", "Square", "Stochastic", "Step Function", "Ramp", "Rising Exponential", "Trapezoidal Pulse", "Triangle", "Variable Rate Pulse Train", "White Noise"] |
| `repetitions` | `integer` | no | minimum=0 |

### `VisualStimulation`
- **Schema title:** Visual stimulation
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Manipulation/VisualStimulation.json`
- **Schema shape:** `array items`
- **Required fields:** none

Example payload for this type:
```json
[
  {
    "stimulusTypes": [],
    "presentationDevice": "Monitor",
    "stimulationPosition": "Contralateral",
    "duration": {
      "unit": "s",
      "value": 0
    }
  }
]
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `closedLoop` | `boolean` | no | format="checkbox" |
| `duration` | `object(value:number, unit:enum[s, ms, µs, min, h])` | no | format="numberUnit"; default={"unit": "s"} |
| `presentationDevice` | `string` | no | enum=["Monitor", "LED panel", "Projector", "Head-mounted display", "Fiber-coupled light source", "Other"] |
| `repetitions` | `integer` | no | minimum=0 |
| `stimulationPosition` | `string` | no | enum=["Contralateral", "Ipsilateral", "Bilateral", "Centered", "Surround", "Other", "Unknown"] |
| `stimulusTypes` | `array` | no | — |
