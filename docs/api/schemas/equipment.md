---
layout: default
title: Equipment
parent: Schemas
grand_parent: API
nav_order: 4
---

# Equipment schemas
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## How to use this page

- Use this page when calling `/api/private/modules/equipment/`.
- Set `type` to one schema name from the list below.
- Send `details` that matches that schema exactly.
- Some equipment types currently expose no custom fields, so `{}` is valid when no fields are defined.

## Quick type map

| Type value | Schema version | Required fields | Schema shape |
|:-----------|:---------------|:----------------|:-------------|
| `Amplifier` | `1.0.0` | none | `object` |
| `AnesthesiaSystem` | `1.0.0` | none | `object` |
| `AntiVibrationTable` | `1.0.0` | none | `object` |
| `BehaviorRig` | `1.0.0` | none | `object` |
| `BiosafetyCabinet` | `1.0.0` | none | `object` |
| `Camera` | `1.0.0` | none | `object` |
| `Computer` | `1.0.0` | none | `object` |
| `DataAcquisitionSystem` | `1.0.0` | none | `object` |
| `DrugDeliverySystem` | `1.0.0` | none | `object` |
| `ElectroencephalographySystem` | `1.0.0` | none | `object` |
| `ElectromyographyMachine` | `1.0.0` | none | `object` |
| `ElectronicComponent` | `1.0.0` | none | `object` |
| `EphysRig` | `1.0.0` | none | `object` |
| `FiberPhotometrySystem` | `1.0.0` | none | `object` |
| `FloatingAirPlatform` | `1.0.0` | none | `object` |
| `ForcePlate` | `1.0.0` | none | `object` |
| `FumeHood` | `1.0.0` | none | `object` |
| `GlassMicropipettePuller` | `1.0.0` | none | `object` |
| `HumidityController` | `1.0.0` | none | `object` |
| `HumiditySensor` | `1.0.0` | none | `object` |
| `InjectionSystem` | `1.0.0` | none | `object` |
| `IontophoresisStimulator` | `1.0.0` | none | `object` |
| `Laser` | `1.0.0` | none | `object` |
| `LedDriver` | `1.0.0` | none | `object` |
| `LightEmitter` | `1.0.0` | none | `object` |
| `LightSensor` | `1.0.0` | none | `object` |
| `MagneticResonanceImagingSystem` | `1.0.0` | none | `object` |
| `MagnetoencephalographySystem` | `1.0.0` | none | `object` |
| `Magnetometer` | `1.0.0` | none | `object` |
| `Microcontroller` | `1.0.0` | none | `object` |
| `Micromanipulator` | `1.0.0` | none | `object` |
| `Microphone` | `1.0.0` | none | `object` |
| `Microscope` | `1.0.0` | none | `object` |
| `Miniscope` | `1.0.0` | none | `object` |
| `Monitor` | `1.0.0` | none | `object` |
| `MotionTrackingSystem` | `1.0.0` | none | `object` |
| `NoiseIsolationChamber` | `1.0.0` | none | `object` |
| `OnePhotonMicroscope` | `1.0.0` | none | `object` |
| `OphysRig` | `1.0.0` | none | `object` |
| `OpticalCoherenceTomography` | `1.0.0` | none | `object` |
| `Oscilloscope` | `1.0.0` | none | `object` |
| `PerfusionSystem` | `1.0.0` | none | `object` |
| `Photodetector` | `1.0.0` | none | `object` |
| `PressureSensor` | `1.0.0` | none | `object` |
| `RunningWheel` | `1.0.0` | none | `object` |
| `SignalProcessingUnit` | `1.0.0` | none | `object` |
| `SingleBoardComputer` | `1.0.0` | none | `object` |
| `SinglePhotonEmissionComputedTomography` | `1.0.0` | none | `object` |
| `Speaker` | `1.0.0` | none | `object` |
| `StereotaxicFrame` | `1.0.0` | none | `object` |
| `StimulationDevice` | `1.0.0` | none | `object` |
| `SurgicalPowerTool` | `1.0.0` | none | `object` |
| `TemperatureSensor` | `1.0.0` | none | `object` |
| `ThermalController` | `1.0.0` | none | `object` |
| `ThreePhotonMicroscopy` | `1.0.0` | none | `object` |
| `Treadmill` | `1.0.0` | none | `object` |
| `TwoPhotonMicroscope` | `1.0.0` | none | `object` |
| `UltrasoundImagingSystem` | `1.0.0` | none | `object` |

## Examples

### Equipment payload fragment

```json
{
  "type": "Amplifier",
  "details": {}
}
```

## Request pattern

```json
{
  "type": "Amplifier",
  "details": {}
}
```

## Schema reference

### `Amplifier`
- **Schema title:** Amplifier
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/Amplifier.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `AnesthesiaSystem`
- **Schema title:** Anesthesia System
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/AnesthesiaSystem.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `AntiVibrationTable`
- **Schema title:** Anti Vibration Table
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/AntiVibrationTable.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `BehaviorRig`
- **Schema title:** Behavior rig
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/BehaviorRig.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `BiosafetyCabinet`
- **Schema title:** Biosafety Cabinet
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/BiosafetyCabinet.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `Camera`
- **Schema title:** Camera
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/Camera.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `Computer`
- **Schema title:** Computer
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/Computer.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `DataAcquisitionSystem`
- **Schema title:** Data acquisition system
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/DataAcquisitionSystem.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `DrugDeliverySystem`
- **Schema title:** Drug Delivery System
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/DrugDeliverySystem.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `ElectroencephalographySystem`
- **Schema title:** Electroencephalography System
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/ElectroencephalographySystem.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `ElectromyographyMachine`
- **Schema title:** Electromyography Machine
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/ElectromyographyMachine.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `ElectronicComponent`
- **Schema title:** ElectronicComponent
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/ElectronicComponent.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `EphysRig`
- **Schema title:** Ephys rig
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/EphysRig.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `FiberPhotometrySystem`
- **Schema title:** Fiber photometry system
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/FiberPhotometrySystem.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `FloatingAirPlatform`
- **Schema title:** Floating Air Platform
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/FloatingAirPlatform.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `ForcePlate`
- **Schema title:** Force Plate
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/ForcePlate.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `FumeHood`
- **Schema title:** Fume Hood
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/FumeHood.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `GlassMicropipettePuller`
- **Schema title:** Glass Micropipette Puller
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/GlassMicropipettePuller.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `HumidityController`
- **Schema title:** Humidity Controller
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/HumidityController.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `HumiditySensor`
- **Schema title:** Humidity Sensor
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/HumiditySensor.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `InjectionSystem`
- **Schema title:** Injection System
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/InjectionSystem.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `IontophoresisStimulator`
- **Schema title:** Iontophoresis Stimulator
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/IontophoresisStimulator.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `Laser`
- **Schema title:** Laser
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/Laser.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `LedDriver`
- **Schema title:** ledDriver
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/LedDriver.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `LightEmitter`
- **Schema title:** Light Emitter
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/LightEmitter.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `LightSensor`
- **Schema title:** Light Sensor
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/LightSensor.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `MagneticResonanceImagingSystem`
- **Schema title:** Magnetic Resonance Imaging System
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/MagneticResonanceImagingSystem.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `MagnetoencephalographySystem`
- **Schema title:** Magnetoencephalography System
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/MagnetoencephalographySystem.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `Magnetometer`
- **Schema title:** Magnetometer
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/Magnetometer.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `Microcontroller`
- **Schema title:** Microcontroller
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/Microcontroller.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `Micromanipulator`
- **Schema title:** Micromanipulator
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/Micromanipulator.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `Microphone`
- **Schema title:** Microphone
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/Microphone.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `Microscope`
- **Schema title:** Microscope
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/Microscope.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `Miniscope`
- **Schema title:** Miniscope
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/Miniscope.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `Monitor`
- **Schema title:** Monitor
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/Monitor.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `MotionTrackingSystem`
- **Schema title:** Motion Tracking System
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/MotionTrackingSystem.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `NoiseIsolationChamber`
- **Schema title:** NoiseIsolationChamber
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/NoiseIsolationChamber.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `OnePhotonMicroscope`
- **Schema title:** One-Photon Microscope
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/OnePhotonMicroscope.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `OphysRig`
- **Schema title:** Ophys rig
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/OphysRig.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `OpticalCoherenceTomography`
- **Schema title:** Optical Coherence Tomography
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/OpticalCoherenceTomography.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `Oscilloscope`
- **Schema title:** Oscilloscope
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/Oscilloscope.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `PerfusionSystem`
- **Schema title:** PerfusionSystem
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/PerfusionSystem.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `Photodetector`
- **Schema title:** Photodetector
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/Photodetector.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `PressureSensor`
- **Schema title:** Pressure Sensor
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/PressureSensor.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `RunningWheel`
- **Schema title:** Running Wheel
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/RunningWheel.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `SignalProcessingUnit`
- **Schema title:** Signal Processing Unit
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/SignalProcessingUnit.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `SingleBoardComputer`
- **Schema title:** SingleBoardComputer
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/SingleBoardComputer.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `SinglePhotonEmissionComputedTomography`
- **Schema title:** Single Photon Emission Computed Tomography
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/SinglePhotonEmissionComputedTomography.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `Speaker`
- **Schema title:** Speaker
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/Speaker.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `StereotaxicFrame`
- **Schema title:** Stereotaxic Frame
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/StereotaxicFrame.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `StimulationDevice`
- **Schema title:** Stimulation Device
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/StimulationDevice.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `SurgicalPowerTool`
- **Schema title:** Surgical Power Tool
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/SurgicalPowerTool.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `TemperatureSensor`
- **Schema title:** Temperature Sensor
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/TemperatureSensor.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `ThermalController`
- **Schema title:** Thermal Controller
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/ThermalController.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `ThreePhotonMicroscopy`
- **Schema title:** Three-Photon Microscopy
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/ThreePhotonMicroscopy.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `Treadmill`
- **Schema title:** Treadmill
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/Treadmill.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `TwoPhotonMicroscope`
- **Schema title:** Two-Photon Microscopy
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/TwoPhotonMicroscope.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |

### `UltrasoundImagingSystem`
- **Schema title:** Ultrasound Imaging System
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Equipment/UltrasoundImagingSystem.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| _No declared fields_ | object | no | — |
