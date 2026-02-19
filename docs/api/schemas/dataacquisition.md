---
layout: default
title: DataAcquisition
parent: Schemas
grand_parent: API
nav_order: 3
---

# DataAcquisition schemas
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## How to use this page

- Use this page when calling `/api/private/modules/dataacquisition/`.
- Set `type` to one schema name from the list below.
- Send `details` that matches that schema exactly.
- Pick one acquisition type in `type`, then send its matching `details` object.

## Quick type map

| Type value | Schema version | Required fields | Schema shape |
|:-----------|:---------------|:----------------|:-------------|
| `Audio` | `1.1.0` | none | `object` |
| `BehavioralTracking` | `1.1.0` | none | `object` |
| `ComputedTomography` | `1.1.0` | none | `object` |
| `ConfocalMicroscopy` | `1.1.0` | none | `object` |
| `Electroencephalography` | `1.1.0` | none | `object` |
| `Electroneurogram` | `1.1.0` | none | `object` |
| `ExtracellularEphys` | `1.1.0` | none | `object` |
| `FiberPhotometry` | `1.1.0` | none | `object` |
| `FunctionalMagneticResonanceImaging` | `1.1.0` | none | `object` |
| `FunctionalUltrasoundImaging` | `1.1.0` | none | `object` |
| `GeneralTimeSeries` | `1.1.0` | none | `object` |
| `IntracellularEphys` | `1.1.0` | none | `object` |
| `LightFieldMicroscopy` | `1.1.0` | none | `object` |
| `MagneticResonanceImaging` | `1.1.0` | none | `object` |
| `Magnetoencephalography` | `1.1.0` | none | `object` |
| `Miniscope` | `1.1.0` | none | `object` |
| `OpticalCoherenceTomography` | `1.1.0` | none | `object` |
| `PositronEmissionTomography` | `1.1.0` | none | `object` |
| `SinglePhotonEmissionComputedTomography` | `1.1.0` | none | `object` |
| `SinglePhotonMicroscopy` | `1.1.0` | none | `object` |
| `ThreePhotonMicroscopy` | `1.1.0` | none | `object` |
| `TwoPhotonMicroscopy` | `1.1.0` | none | `object` |
| `VideoTracking` | `1.1.0` | none | `object` |

## Examples

### DataAcquisition payload fragment
```json
{
  "type": "Audio",
  "details": {
    "fileName": "example",
    "format": "example",
    "compression": "example",
    "bitDepth": 8
  }
}
```

## Request pattern
```json
{
  "type": "Audio",
  "details": {
    "fileName": "example",
    "format": "example",
    "compression": "example",
    "bitDepth": 8
  }
}
```

## Schema reference

### `Audio`
- **Schema title:** Audio
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/Audio.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "compression": "example",
  "bitDepth": 8
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `bitDepth` | `integer` | no | minimum=0; default=8 |
| `codec` | `string` | no | format="text" |
| `compression` | `string` | no | format="text" |
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `nChannels` | `integer` | no | minimum=1; default=2 |
| `nSamples` | `integer` | no | minimum=0 |
| `sr` | `object(value:number, unit:enum[GHz, MHz, kHz, Hz])` | no | format="numberUnit"; default={"unit": "Hz"} |

### `BehavioralTracking`
- **Schema title:** BehavioralTracking
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/BehavioralTracking.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "compression": "example",
  "nFrames": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `compression` | `string` | no | format="text" |
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `frameRate` | `object(value:number, unit:enum[GHz, MHz, kHz, Hz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `horizontalResolution` | `integer` | no | minimum=0 |
| `nFrames` | `integer` | no | minimum=0 |
| `verticalResolution` | `integer` | no | minimum=0 |

### `ComputedTomography`
- **Schema title:** ComputedTomography
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/ComputedTomography.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "compression": "example",
  "nFrames": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `compression` | `string` | no | format="text" |
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `frameRate` | `object(value:number, unit:enum[GHz, MHz, kHz, Hz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `horizontalResolution` | `integer` | no | minimum=0 |
| `imagingDepth` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `laserPower` | `object(value:number, unit:enum[kW, W, mW, µW])` | no | format="numberUnit"; default={"unit": "mW"} |
| `nFrames` | `integer` | no | minimum=0 |
| `verticalResolution` | `integer` | no | minimum=0 |

### `ConfocalMicroscopy`
- **Schema title:** Confocal Microscopy
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/ConfocalMicroscopy.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "compression": "example",
  "verticalResolution": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `compression` | `string` | no | format="text" |
| `excitationWavelength` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "nm"} |
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `frameRate` | `object(value:number, unit:enum[GHz, MHz, kHz, Hz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `horizontalResolution` | `integer` | no | minimum=0 |
| `imagingDepth` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `laserPower` | `object(value:number, unit:enum[kW, W, mW, µW])` | no | format="numberUnit"; default={"unit": "mW"} |
| `nFrames` | `integer` | no | minimum=0 |
| `verticalResolution` | `integer` | no | minimum=0 |
| `xVoxelSize` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `yVoxelSize` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `zVoxelSize` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |

### `Electroencephalography`
- **Schema title:** Electroencephalography (EEG)
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/Electroencephalography.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "type": "int16",
  "nChannels": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `channelTags` | `array` | no | format="table" |
| `electrodeGroups` | `array` | no | format="table" |
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `lsb` | `object(value:number, unit:enum[V, mV, µV, nV])` | no | format="numberUnit"; default={"unit": "µV"} |
| `nChannels` | `integer` | no | minimum=0 |
| `nSamples` | `integer` | no | minimum=0 |
| `sr` | `object(value:number, unit:enum[GHz, MHz, kHz, Hz])` | no | format="numberUnit"; default={"unit": "Hz", "value": 20000} |
| `type` | `string` | no | format="text"; default="int16" |

### `Electroneurogram`
- **Schema title:** Electroneurogram
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/Electroneurogram.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "type": "int16",
  "nChannels": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `channelTags` | `array` | no | format="table" |
| `electrodeGroups` | `array` | no | format="table" |
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `lsb` | `object(value:number, unit:enum[V, mV, µV, nV])` | no | format="numberUnit"; default={"unit": "µV"} |
| `nChannels` | `integer` | no | minimum=0 |
| `nSamples` | `integer` | no | minimum=0 |
| `sr` | `object(value:number, unit:enum[GHz, MHz, kHz, Hz])` | no | format="numberUnit"; default={"unit": "Hz", "value": 20000} |
| `type` | `string` | no | format="text"; default="int16" |

### `ExtracellularEphys`
- **Schema title:** Extracellular Electrophysiology
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/ExtracellularEphys.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "type": "int16",
  "nChannels": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `channelTags` | `array` | no | format="table" |
| `electrodeGroups` | `array` | no | format="table" |
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `lsb` | `object(value:number, unit:enum[V, mV, µV, nV])` | no | format="numberUnit"; default={"unit": "µV"} |
| `nChannels` | `integer` | no | minimum=0 |
| `nSamples` | `integer` | no | minimum=0 |
| `sr` | `object(value:number, unit:enum[GHz, MHz, kHz, Hz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `type` | `string` | no | format="text"; default="int16" |

### `FiberPhotometry`
- **Schema title:** Fiber Photometry
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/FiberPhotometry.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "compression": "example",
  "nFrames": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `compression` | `string` | no | format="text" |
| `excitationWavelength` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "nm"} |
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `frameRate` | `object(value:number, unit:enum[GHz, MHz, kHz, Hz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `laserPower` | `object(value:number, unit:enum[kW, W, mW, µW])` | no | format="numberUnit"; default={"unit": "mW"} |
| `nFrames` | `integer` | no | minimum=0 |

### `FunctionalMagneticResonanceImaging`
- **Schema title:** Functional Magnetic Resonance Imaging
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/FunctionalMagneticResonanceImaging.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "compression": "example",
  "nFrames": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `compression` | `string` | no | format="text" |
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `frameRate` | `object(value:number, unit:enum[GHz, MHz, kHz, Hz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `horizontalResolution` | `integer` | no | minimum=0 |
| `imagingDepth` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `laserPower` | `object(value:number, unit:enum[kW, W, mW, µW])` | no | format="numberUnit"; default={"unit": "mW"} |
| `nFrames` | `integer` | no | minimum=0 |
| `verticalResolution` | `integer` | no | minimum=0 |

### `FunctionalUltrasoundImaging`
- **Schema title:** Functional Ultrasound Imaging
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/FunctionalUltrasoundImaging.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "compression": "example",
  "nFrames": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `compression` | `string` | no | format="text" |
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `frameRate` | `object(value:number, unit:enum[GHz, MHz, kHz, Hz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `horizontalResolution` | `integer` | no | minimum=0 |
| `imagingDepth` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `laserPower` | `object(value:number, unit:enum[kW, W, mW, µW])` | no | format="numberUnit"; default={"unit": "mW"} |
| `nFrames` | `integer` | no | minimum=0 |
| `verticalResolution` | `integer` | no | minimum=0 |

### `GeneralTimeSeries`
- **Schema title:** General Time Series
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/GeneralTimeSeries.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "type": "int16",
  "nChannels": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `channelTags` | `array` | no | format="table" |
| `electrodeGroups` | `array` | no | format="table" |
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `lsb` | `object(value:number, unit:enum[V, mV, µV, nV])` | no | format="numberUnit"; default={"unit": "µV"} |
| `nChannels` | `integer` | no | minimum=0 |
| `nSamples` | `integer` | no | minimum=0 |
| `sr` | `object(value:number, unit:enum[GHz, MHz, kHz, Hz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `type` | `string` | no | format="text"; default="int16" |

### `IntracellularEphys`
- **Schema title:** Intracellular Electrophysiology
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/IntracellularEphys.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "type": "int16",
  "nChannels": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `lsb` | `object(value:number, unit:enum[V, mV, µV, nV])` | no | format="numberUnit"; default={"unit": "µV"} |
| `nChannels` | `integer` | no | minimum=0 |
| `nSamples` | `integer` | no | minimum=0 |
| `sr` | `object(value:number, unit:enum[GHz, MHz, kHz, Hz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `type` | `string` | no | format="text"; default="int16" |

### `LightFieldMicroscopy`
- **Schema title:** Light Field Microscopy
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/LightFieldMicroscopy.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "compression": "example",
  "verticalResolution": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `compression` | `string` | no | format="text" |
| `excitationWavelength` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "nm"} |
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `frameRate` | `object(value:number, unit:enum[GHz, MHz, kHz, Hz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `horizontalResolution` | `integer` | no | minimum=0 |
| `imagingDepth` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `laserPower` | `object(value:number, unit:enum[kW, W, mW, µW])` | no | format="numberUnit"; default={"unit": "mW"} |
| `nFrames` | `integer` | no | minimum=0 |
| `verticalResolution` | `integer` | no | minimum=0 |
| `xVoxelSize` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `yVoxelSize` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `zVoxelSize` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |

### `MagneticResonanceImaging`
- **Schema title:** Magnetic Resonance Imaging
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/MagneticResonanceImaging.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "compression": "example",
  "nFrames": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `compression` | `string` | no | format="text" |
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `frameRate` | `object(value:number, unit:enum[Hz, kHz, MHz, GHz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `horizontalResolution` | `integer` | no | minimum=0 |
| `imagingDepth` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "mm"} |
| `magneticFieldStrength` | `object(value:number, unit:enum[T, mT, µT])` | no | format="numberUnit"; default={"unit": "T"} |
| `nFrames` | `integer` | no | minimum=0 |
| `verticalResolution` | `integer` | no | minimum=0 |

### `Magnetoencephalography`
- **Schema title:** Magnetoencephalography
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/Magnetoencephalography.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "compression": "example",
  "nFrames": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `compression` | `string` | no | format="text" |
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `frameRate` | `object(value:number, unit:enum[GHz, MHz, kHz, Hz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `horizontalResolution` | `integer` | no | minimum=0 |
| `imagingDepth` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `laserPower` | `object(value:number, unit:enum[kW, W, mW, µW])` | no | format="numberUnit"; default={"unit": "mW"} |
| `nFrames` | `integer` | no | minimum=0 |
| `verticalResolution` | `integer` | no | minimum=0 |

### `Miniscope`
- **Schema title:** Miniscope Microscopy
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/Miniscope.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "compression": "example",
  "nFrames": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `compression` | `string` | no | format="text" |
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `frameRate` | `object(value:number, unit:enum[GHz, MHz, kHz, Hz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `horizontalResolution` | `integer` | no | minimum=0 |
| `imagingDepth` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `laserPower` | `object(value:number, unit:enum[kW, W, mW, µW])` | no | format="numberUnit"; default={"unit": "mW"} |
| `nFrames` | `integer` | no | minimum=0 |
| `verticalResolution` | `integer` | no | minimum=0 |

### `OpticalCoherenceTomography`
- **Schema title:** Optical Coherence Tomography (OCT)
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/OpticalCoherenceTomography.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "compression": "example",
  "verticalResolution": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `averages` | `integer` | no | minimum=0 |
| `axialResolution` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `bandwidth` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "nm"} |
| `centerWavelength` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "nm"} |
| `compression` | `string` | no | format="text" |
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `frameRate` | `object(value:number, unit:enum[GHz, MHz, kHz, Hz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `horizontalResolution` | `integer` | no | minimum=0 |
| `imagingDepth` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `lateralResolution` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `nFrames` | `integer` | no | minimum=0 |
| `scanArea` | `object(value:number, unit:enum[m², cm², mm², µm², nm²])` | no | format="numberUnit"; default={"unit": "mm²"} |
| `scanPattern` | `string` | no | format="text" |
| `verticalResolution` | `integer` | no | minimum=0 |

### `PositronEmissionTomography`
- **Schema title:** Positron Emission Tomography
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/PositronEmissionTomography.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "compression": "example",
  "nFrames": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `compression` | `string` | no | format="text" |
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `frameRate` | `object(value:number, unit:enum[GHz, MHz, kHz, Hz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `horizontalResolution` | `integer` | no | minimum=0 |
| `imagingDepth` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `laserPower` | `object(value:number, unit:enum[kW, W, mW, µW])` | no | format="numberUnit"; default={"unit": "mW"} |
| `nFrames` | `integer` | no | minimum=0 |
| `verticalResolution` | `integer` | no | minimum=0 |

### `SinglePhotonEmissionComputedTomography`
- **Schema title:** Single Photon Emission Computed Tomography
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/SinglePhotonEmissionComputedTomography.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "compression": "example",
  "nFrames": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `compression` | `string` | no | format="text" |
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `frameRate` | `object(value:number, unit:enum[GHz, MHz, kHz, Hz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `horizontalResolution` | `integer` | no | minimum=0 |
| `imagingDepth` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `laserPower` | `object(value:number, unit:enum[kW, W, mW, µW])` | no | format="numberUnit"; default={"unit": "mW"} |
| `nFrames` | `integer` | no | minimum=0 |
| `verticalResolution` | `integer` | no | minimum=0 |

### `SinglePhotonMicroscopy`
- **Schema title:** Single-Photon Microscopy
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/SinglePhotonMicroscopy.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "compression": "example",
  "verticalResolution": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `compression` | `string` | no | format="text" |
| `excitationWavelength` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "nm"} |
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `frameRate` | `object(value:number, unit:enum[GHz, MHz, kHz, Hz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `horizontalResolution` | `integer` | no | minimum=0 |
| `imagingDepth` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `laserPower` | `object(value:number, unit:enum[kW, W, mW, µW])` | no | format="numberUnit"; default={"unit": "mW"} |
| `nFrames` | `integer` | no | minimum=0 |
| `verticalResolution` | `integer` | no | minimum=0 |
| `xVoxelSize` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `yVoxelSize` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `zVoxelSize` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |

### `ThreePhotonMicroscopy`
- **Schema title:** Three-Photon Microscopy
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/ThreePhotonMicroscopy.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "compression": "example",
  "verticalResolution": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `compression` | `string` | no | format="text" |
| `excitationWavelength` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "nm"} |
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `frameRate` | `object(value:number, unit:enum[GHz, MHz, kHz, Hz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `horizontalResolution` | `integer` | no | minimum=0 |
| `imagingDepth` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `laserPower` | `object(value:number, unit:enum[kW, W, mW, µW])` | no | format="numberUnit"; default={"unit": "mW"} |
| `nFrames` | `integer` | no | minimum=0 |
| `verticalResolution` | `integer` | no | minimum=0 |
| `xVoxelSize` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `yVoxelSize` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `zVoxelSize` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |

### `TwoPhotonMicroscopy`
- **Schema title:** Two-Photon Microscopy
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/TwoPhotonMicroscopy.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "compression": "example",
  "verticalResolution": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `compression` | `string` | no | format="text" |
| `excitationWavelength` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "nm"} |
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `frameRate` | `object(value:number, unit:enum[GHz, MHz, kHz, Hz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `horizontalResolution` | `integer` | no | minimum=0 |
| `imagingDepth` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `laserPower` | `object(value:number, unit:enum[kW, W, mW, µW])` | no | format="numberUnit"; default={"unit": "mW"} |
| `nFrames` | `integer` | no | minimum=0 |
| `verticalResolution` | `integer` | no | minimum=0 |
| `xVoxelSize` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `yVoxelSize` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |
| `zVoxelSize` | `object(value:number, unit:enum[m, cm, mm, µm, nm])` | no | format="numberUnit"; default={"unit": "µm"} |

### `VideoTracking`
- **Schema title:** Video Tracking
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/DataAcquisition/VideoTracking.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fileName": "example",
  "format": "example",
  "compression": "example",
  "nFrames": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `compression` | `string` | no | format="text" |
| `fileName` | `string` | no | format="text" |
| `format` | `string` | no | format="text" |
| `frameRate` | `object(value:number, unit:enum[GHz, MHz, kHz, Hz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `horizontalResolution` | `integer` | no | minimum=0 |
| `nFrames` | `integer` | no | minimum=0 |
| `verticalResolution` | `integer` | no | minimum=0 |
