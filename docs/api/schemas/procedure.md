---
layout: default
title: Procedure
parent: Schemas
grand_parent: API
nav_order: 6
---

# Procedure schemas
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## How to use this page

- Use this page when calling `/api/private/modules/procedure/`.
- Set `type` to one schema name from the list below.
- Send `details` that matches that schema exactly.
- Procedure also requires `coordinates_system` + `coordinates_details`.

## Quick type map

| Type value | Schema version | Required fields | Schema shape |
|:-----------|:---------------|:----------------|:-------------|
| `Anesthesia` | `1.1.0` | `anestheticAgent`, `route` | `object` |
| `AuditoryStimulation` | `1.0.0` | `stimulusTypes` | `object` |
| `BarbiturateInjection` | `1.1.0` | `barbiturate`, `confirmationOfDeath`, `route` | `object` |
| `BehavioralTracking` | `1.0.0` | none | `object` |
| `BloodPressureSensorImplant` | `1.0.0` | `anchoringMethod`, `sensorType` | `object` |
| `BrainExtraction` | `1.1.0` | `extractionMethod`, `preservationMethod` | `object` |
| `BrainLesion` | `1.1.0` | none | `object` |
| `BrainSlice` | `1.1.0` | `orientation`, `thickness` | `object` |
| `BreathingSensorImplant` | `1.0.0` | `anchoringMethod`, `sensorType` | `object` |
| `BurrHole` | `1.1.0` | none | `object` |
| `CatheterImplant` | `1.0.0` | `targetSite` | `object` |
| `CervicalDislocation` | `1.0.0` | `confirmationOfDeath`, `dislocationMethod` | `object` |
| `Co2ChamberEuthanasia` | `1.1.0` | `co2Concentration`, `confirmationOfDeath`, `exposureDuration` | `object` |
| `CranialWindow` | `1.0.0` | none | `object` |
| `Craniectomy` | `1.0.0` | none | `object` |
| `Craniotomy` | `1.0.0` | none | `object` |
| `Cryosectioning` | `1.1.0` | `orientation`, `sectionThickness`, `temperature` | `object` |
| `Decapitation` | `1.0.0` | `decapitationMethod` | `object` |
| `EcgImplant` | `1.0.0` | `anchoringMethod` | `object` |
| `EegImplant` | `1.0.0` | `anchoringMethod`, `electrodeMaterial`, `electrodeType`, `wireCount` | `object` |
| `EmgImplant` | `1.0.0` | `implantMethod`, `wireCount` | `object` |
| `GenericImplant` | `1.0.0` | `implantType` | `object` |
| `GrinLensImplant` | `1.0.0` | none | `object` |
| `HeadFixation` | `1.0.0` | none | `object` |
| `Headcap` | `1.0.0` | none | `object` |
| `Headpost` | `1.0.0` | none | `object` |
| `InhalantOverdose` | `1.1.0` | none | `object` |
| `Injection` | `1.1.0` | none | `object` |
| `NerveCuffImplant` | `1.0.0` | `anchoringMethod`, `cuffType` | `object` |
| `OdorStimulation` | `1.0.0` | none | `object` |
| `OpticFiberImplant` | `1.0.0` | none | `object` |
| `PerfusionFixation` | `1.1.0` | none | `object` |
| `PrismImplant` | `1.0.0` | none | `object` |
| `ReferenceElectrodeImplant` | `1.1.0` | `electrodeCount`, `electrodeMaterial` | `object` |
| `SiliconProbeImplant` | `1.0.0` | none | `object` |
| `SingleWireElectrodeImplant` | `1.1.0` | `wireCount` | `object` |
| `TactileStimulation` | `1.0.0` | `stimulusTypes` | `object` |
| `TemperatureSensorImplant` | `1.0.0` | `anchoringMethod`, `sensorType` | `object` |
| `TetrodeWireElectrodeImplant` | `1.1.0` | `tetrodeCount` | `object` |
| `TissueClearing` | `1.1.0` | `clearingMethod` | `object` |
| `VibratomeSectioning` | `1.1.0` | `bladeType` | `object` |
| `VirusInjection` | `1.1.0` | none | `object` |
| `VisualStimulation` | `1.0.0` | `stimulusTypes` | `object` |

## Examples

### Procedure payload fragment
```json
{
  "type": "Anesthesia",
  "details": {
    "anestheticAgent": "Isoflurane",
    "route": "Inhalation"
  }
}
```

## Request pattern
```json
{
  "type": "Anesthesia",
  "details": {
    "anestheticAgent": "Isoflurane",
    "route": "Inhalation"
  }
}
```

## Schema reference

### `Anesthesia`
- **Schema title:** Anesthesia
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Procedure/Anesthesia.json`
- **Schema shape:** `object`
- **Required fields:** `anestheticAgent`, `route`

Example payload for this type:
```json
{
  "anestheticAgent": "Isoflurane",
  "route": "Inhalation"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `anestheticAgent` | `string` | yes | enum=["Isoflurane", "Sevoflurane", "Ketamine", "Ketamine + Xylazine", "Ketamine + Dexmedetomidine", "Pentobarbital", "Urethane", "Tribromoethanol (Avertin)", "Propofol", "Other"] |
| `complications` | `string` | no | format="textarea" |
| `depth` | `string` | no | enum=["Light sedation", "Moderate sedation", "Deep sedation", "Surgical plane", "Other"] |
| `dosage` | `string` | no | format="text" |
| `duration` | `object(value:number, unit:enum[h, min, s, ms, µs])` | no | format="numberUnit"; default={"unit": "min"} |
| `endOfAnesthesia` | `string` | no | format="time" |
| `monitoringMethod` | `array` | no | format="checkbox"; minItems=0 |
| `recoveryTime` | `object(value:number, unit:enum[h, min, s, ms, µs])` | no | format="numberUnit"; default={"unit": "min"} |
| `route` | `string` | yes | enum=["Inhalation", "Intraperitoneal (IP)", "Intravenous (IV)", "Subcutaneous (SC)", "Intramuscular (IM)", "Oral", "Other"] |
| `supportiveCare` | `array` | no | format="checkbox"; minItems=0 |

### `AuditoryStimulation`
- **Schema title:** Auditory stimulation
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/AuditoryStimulation.json`
- **Schema shape:** `object`
- **Required fields:** `stimulusTypes`

Example payload for this type:
```json
{
  "stimulusTypes": []
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `deliveryMethod` | `string` | no | enum=["Free-field speaker", "In-ear speaker", "Bone conduction", "Headphone", "Other"] |
| `paradigmDescription` | `string` | no | format="textarea" |
| `stimulationContext` | `string` | no | enum=["Passive", "Behavioral task", "Closed-loop", "Anesthetized", "Free behavior"] |
| `stimulusTypes` | `array` | yes | — |

### `BarbiturateInjection`
- **Schema title:** Barbiturate injection
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Procedure/BarbiturateInjection.json`
- **Schema shape:** `object`
- **Required fields:** `barbiturate`, `confirmationOfDeath`, `route`

Example payload for this type:
```json
{
  "confirmationOfDeath": [],
  "route": "Intraperitoneal (IP)",
  "barbiturate": "Pentobarbital"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `barbiturate` | `string` | yes | enum=["Pentobarbital", "Phenobarbital", "Secobarbital", "Barbital", "Commercial euthanasia solution", "Other"] |
| `concentration` | `object(value:number, unit:enum[mg/mL, µg/mL, g/L, mg/L, µg/L])` | no | format="numberUnit"; default={"unit": "mg/mL"} |
| `confirmationOfDeath` | `array` | yes | format="checkbox"; minItems=0 |
| `dosage` | `object(value:number, unit:enum[mg/kg, µg/kg, g/kg])` | no | format="numberUnit"; default={"unit": "mg/kg"} |
| `route` | `string` | yes | enum=["Intraperitoneal (IP)", "Intravenous (IV)", "Intracardiac", "Subcutaneous (SC)", "Other"] |
| `sedationAgent` | `string` | no | format="text" |
| `timeToUnconsciousness` | `object(value:number, unit:enum[s, min, h, ms])` | no | format="numberUnit"; default={"unit": "s"} |
| `volumeAdministered` | `object(value:number, unit:enum[mL, L, µL, nL])` | no | format="numberUnit"; default={"unit": "mL"} |

### `BehavioralTracking`
- **Schema title:** Behavioral tracking
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/BehavioralTracking.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "trackingMethod": "Markerless",
  "trackedFeatures": []
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `trackedFeatures` | `array` | no | — |
| `trackingMethod` | `string` | no | enum=["Markerless", "Marker-based", "Hybrid", "Manual scoring"] |

### `BloodPressureSensorImplant`
- **Schema title:** Blood pressure sensor implant
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/BloodPressureSensorImplant.json`
- **Schema shape:** `object`
- **Required fields:** `anchoringMethod`, `sensorType`

Example payload for this type:
```json
{
  "sensorType": "telemetric",
  "anchoringMethod": "sutured"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `anchoringMethod` | `string` | yes | enum=["sutured", "subcutaneous tunnel", "tissue glue", "headcap", "cemented to skull", "other"] |
| `catheterMaterial` | `string` | no | format="text" |
| `implantSite` | `string` | no | — |
| `sensorType` | `string` | yes | enum=["telemetric", "catheter-based", "fluid-filled", "fiber-optic", "other"] |
| `sterilizationMethod` | `string` | no | enum=["Autoclave", "Ethylene Oxide", "Alcohol", "Gamma Irradiation", "None"] |

### `BrainExtraction`
- **Schema title:** Brain extraction
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Procedure/BrainExtraction.json`
- **Schema shape:** `object`
- **Required fields:** `extractionMethod`, `preservationMethod`

Example payload for this type:
```json
{
  "extractionMethod": "Complete removal",
  "preservationMethod": "Fresh (immediate use)"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `brainWeight` | `object(value:number, unit:enum[g, kg, mg, µg])` | no | format="numberUnit"; default={"unit": "g"} |
| `extractionMethod` | `string` | yes | enum=["Complete removal", "Partial removal", "Sectional removal", "Other"] |
| `fixationDuration` | `object(value:number, unit:enum[s, min, h, ms])` | no | format="numberUnit"; default={"unit": "h"} |
| `preservationMethod` | `string` | yes | enum=["Fresh (immediate use)", "Paraformaldehyde fixation", "Formalin fixation", "Flash freezing", "Liquid nitrogen", "Dry ice", "Other"] |
| `storageConditions` | `string` | no | format="text" |
| `timeToExtraction` | `object(value:number, unit:enum[s, min, h, ms])` | no | format="numberUnit"; default={"unit": "min"} |

### `BrainLesion`
- **Schema title:** Brain lesion
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Procedure/BrainLesion.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "lesionMethod": "example",
  "volume": {
    "unit": "µL",
    "value": 0
  },
  "fatalOutcome": false
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `fatalOutcome` | `boolean` | no | format="checkbox" |
| `lesionMethod` | `string` | no | format="text" |
| `volume` | `object(value:number, unit:enum[µL, mL, L, nL])` | no | format="numberUnit"; default={"unit": "µL"} |

### `BrainSlice`
- **Schema title:** Brain Slice
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Procedure/BrainSlice.json`
- **Schema shape:** `object`
- **Required fields:** `orientation`, `thickness`

Example payload for this type:
```json
{
  "thickness": {
    "unit": "µm",
    "value": 50
  },
  "orientation": "coronal"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `medium` | `string` | no | format="text" |
| `nSlices` | `integer` | no | minimum=0 |
| `orientation` | `string` | yes | enum=["coronal", "sagittal", "horizontal"]; default="coronal" |
| `thickness` | `object(value:number, unit:enum[µm, mm, nm, m])` | yes | format="numberUnit"; default={"unit": "µm", "value": 50} |
| `vibratomeBladeAngle` | `object(value:number, unit:enum[°])` | no | format="numberUnit"; default={"unit": "°"} |

### `BreathingSensorImplant`
- **Schema title:** Breathing sensor implant
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/BreathingSensorImplant.json`
- **Schema shape:** `object`
- **Required fields:** `anchoringMethod`, `sensorType`

Example payload for this type:
```json
{
  "sensorType": "Piezoelectric sensor",
  "anchoringMethod": "sutured"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `anchoringMethod` | `string` | yes | enum=["sutured", "tissue glue", "subcutaneous tunnel", "cemented to skull", "headcap", "custom mount", "other"] |
| `implantSite` | `string` | no | — |
| `sensorType` | `string` | yes | enum=["Piezoelectric sensor", "Chest wall EMG", "Intranasal thermocouple", "Intranasal pressure sensor", "Tracheal airflow sensor", "Thoracic pressure sensor", "Plethysmography cannula", "Other"] |
| `signalTransmission` | `string` | no | enum=["tethered", "wireless", "telemetric", "inductive", "optical", "other"] |
| `sterilizationMethod` | `string` | no | enum=["Autoclave", "Ethylene Oxide", "Alcohol", "Gamma Irradiation", "None"] |
| `wireMaterial` | `string` | no | format="text" |

### `BurrHole`
- **Schema title:** Burr hole
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Procedure/BurrHole.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "diameter": {
    "unit": "mm",
    "value": 0
  },
  "drillSpeed": {
    "unit": "RPM",
    "value": 0
  },
  "purpose": "example",
  "coolingMethod": "Saline irrigation"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `complications` | `string` | no | format="textarea" |
| `coolingMethod` | `string` | no | enum=["Saline irrigation", "Air cooling", "None", "Other"] |
| `diameter` | `object(value:number, unit:enum[mm, µm, cm, m])` | no | format="numberUnit"; default={"unit": "mm"} |
| `drillSpeed` | `object(value:number, unit:enum[RPM, Hz])` | no | format="numberUnit"; default={"unit": "RPM"} |
| `purpose` | `string` | no | — |

### `CatheterImplant`
- **Schema title:** Catheter implant
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/CatheterImplant.json`
- **Schema shape:** `object`
- **Required fields:** `targetSite`

Example payload for this type:
```json
{
  "targetSite": "jugular vein"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `catheterId` | `string` | no | format="text" |
| `catheterType` | `string` | no | format="text" |
| `externalPort` | `string` | no | enum=["head-mounted", "back-mounted", "tail-mounted", "subcutaneous", "none"] |
| `fixationMethod` | `string` | no | enum=["sutures", "dental cement", "epoxy", "tissue glue", "tunneled subcutaneously", "other"] |
| `material` | `string` | no | format="text" |
| `purpose` | `string` | no | enum=["infusion", "sampling", "pressure monitoring", "drug delivery", "other"] |
| `targetSite` | `string` | yes | enum=["jugular vein", "femoral vein", "carotid artery", "lateral ventricle", "third ventricle", "spinal cord (intrathecal)", "cisterna magna", "peritoneal cavity", "other"] |

### `CervicalDislocation`
- **Schema title:** Cervical dislocation
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/CervicalDislocation.json`
- **Schema shape:** `object`
- **Required fields:** `confirmationOfDeath`, `dislocationMethod`

Example payload for this type:
```json
{
  "confirmationOfDeath": [],
  "dislocationMethod": "Manual"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `anestheticAgent` | `string` | no | format="text" |
| `complications` | `string` | no | format="textarea" |
| `confirmationOfDeath` | `array` | yes | format="checkbox"; minItems=0 |
| `dislocationMethod` | `string` | yes | enum=["Manual", "Mechanical device", "Scissor method", "Other"] |

### `Co2ChamberEuthanasia`
- **Schema title:** CO₂ chamber euthanasia
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Procedure/Co2ChamberEuthanasia.json`
- **Schema shape:** `object`
- **Required fields:** `co2Concentration`, `confirmationOfDeath`, `exposureDuration`

Example payload for this type:
```json
{
  "confirmationOfDeath": [],
  "co2Concentration": {
    "unit": "%",
    "value": 0
  },
  "exposureDuration": {
    "unit": "min",
    "value": 0
  }
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `chamberVolume` | `object(value:number, unit:enum[L, mL, µL])` | no | format="numberUnit"; default={"unit": "L"} |
| `co2Concentration` | `object(value:number, unit:enum[%, ppm, ppb])` | yes | format="numberUnit"; default={"unit": "%"} |
| `confirmationOfDeath` | `array` | yes | format="checkbox"; minItems=0 |
| `exposureDuration` | `object(value:number, unit:enum[s, min, h, ms])` | yes | format="numberUnit"; default={"unit": "min"} |
| `flowRate` | `object(value:number, unit:enum[L/min, mL/min, L/s, mL/s])` | no | format="numberUnit"; default={"unit": "L/min"} |
| `gradualIntroduction` | `boolean` | no | format="checkbox" |
| `prefillingMethod` | `string` | no | enum=["Not prefilled", "Partially prefilled", "Fully prefilled", "Other"] |
| `timeToUnconsciousness` | `object(value:number, unit:enum[s, min, h, ms])` | no | format="numberUnit"; default={"unit": "s"} |

### `CranialWindow`
- **Schema title:** Cranial window
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/CranialWindow.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "surgicalMethod": "example",
  "shape": "example",
  "dimensions": "example",
  "orientation": "example"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `dimensions` | `string` | no | format="text" |
| `orientation` | `string` | no | format="text" |
| `shape` | `string` | no | format="text" |
| `surgicalMethod` | `string` | no | format="text" |

### `Craniectomy`
- **Schema title:** Craniectomy
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/Craniectomy.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "surgicalMethod": "example",
  "shape": "example",
  "dimensions": "example",
  "orientation": "example"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `dimensions` | `string` | no | format="text" |
| `fatalOutcome` | `boolean` | no | format="checkbox" |
| `orientation` | `string` | no | format="text" |
| `shape` | `string` | no | format="text" |
| `surgicalMethod` | `string` | no | format="text" |

### `Craniotomy`
- **Schema title:** Craniotomy
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/Craniotomy.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "surgicalMethod": "example",
  "shape": "example",
  "dimensions": "example",
  "orientation": "example"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `dimensions` | `string` | no | format="text" |
| `fatalOutcome` | `boolean` | no | format="checkbox" |
| `orientation` | `string` | no | format="text" |
| `shape` | `string` | no | format="text" |
| `surgicalMethod` | `string` | no | format="text" |

### `Cryosectioning`
- **Schema title:** Cryosectioning
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Procedure/Cryosectioning.json`
- **Schema shape:** `object`
- **Required fields:** `orientation`, `sectionThickness`, `temperature`

Example payload for this type:
```json
{
  "orientation": "Coronal",
  "sectionThickness": {
    "unit": "µm",
    "value": 40
  },
  "temperature": {
    "unit": "°C",
    "value": 0
  }
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `embeddingMedium` | `string` | no | enum=["OCT compound", "Tissue-Tek", "Cryomatrix", "Gelatin", "None", "Other"] |
| `numberOfSections` | `number` | no | minimum=0 |
| `orientation` | `string` | yes | enum=["Coronal", "Sagittal", "Horizontal", "Other"] |
| `sectionInterval` | `number` | no | minimum=1 |
| `sectionThickness` | `object(value:number, unit:enum[µm, mm, nm, m])` | yes | format="numberUnit"; default={"unit": "µm", "value": 40} |
| `serialSectioning` | `boolean` | no | format="checkbox" |
| `storageBuffer` | `string` | no | format="text" |
| `storageMethod` | `string` | no | enum=["Mounted on slides", "Free-floating in solution", "Stored in plates", "Other"] |
| `temperature` | `object(value:number, unit:enum[°C, K, °F])` | yes | format="numberUnit"; default={"unit": "°C", "value": 0} |

### `Decapitation`
- **Schema title:** Decapitation
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/Decapitation.json`
- **Schema shape:** `object`
- **Required fields:** `decapitationMethod`

Example payload for this type:
```json
{
  "decapitationMethod": "Guillotine"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `anestheticAgent` | `string` | no | format="text" |
| `complications` | `string` | no | format="textarea" |
| `decapitationMethod` | `string` | yes | enum=["Guillotine", "Sharp scissors", "Surgical blade", "Other"] |

### `EcgImplant`
- **Schema title:** ECG implant
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/EcgImplant.json`
- **Schema shape:** `object`
- **Required fields:** `anchoringMethod`

Example payload for this type:
```json
{
  "anchoringMethod": "sutured"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `anchoringMethod` | `string` | yes | enum=["sutured", "subcutaneous tunnel", "tissue glue", "headcap", "cemented to skull", "other"] |
| `implantSite` | `string` | no | — |
| `sterilizationMethod` | `string` | no | enum=["Autoclave", "Ethylene Oxide", "Alcohol", "Gamma Irradiation", "None"] |
| `wireCount` | `integer` | no | minimum=1 |
| `wireInsulation` | `string` | no | enum=["Teflon", "polyimide", "silicone", "none", "other"] |
| `wireMaterial` | `string` | no | format="text" |

### `EegImplant`
- **Schema title:** EEG implant
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/EegImplant.json`
- **Schema shape:** `object`
- **Required fields:** `anchoringMethod`, `electrodeMaterial`, `electrodeType`, `wireCount`

Example payload for this type:
```json
{
  "wireCount": 1,
  "electrodeType": "skull screw",
  "electrodeMaterial": "example",
  "anchoringMethod": "dental cement"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `anchoringMethod` | `string` | yes | enum=["dental cement", "screws", "acrylic", "UV-cured resin", "headcap", "other"] |
| `electrodeMaterial` | `string` | yes | format="text" |
| `electrodeType` | `string` | yes | enum=["skull screw", "flat wire", "disc", "custom", "other"] |
| `referencingScheme` | `string` | no | enum=["single reference", "common average", "bipolar", "differential", "other"] |
| `shielding` | `string` | no | enum=["none", "copper mesh", "conductive paint", "aluminum foil", "headcap integrated", "other"] |
| `sterilizationMethod` | `string` | no | enum=["Autoclave", "Ethylene Oxide", "Alcohol", "Gamma Irradiation", "None"] |
| `wireCount` | `integer` | yes | minimum=1; default=1 |

### `EmgImplant`
- **Schema title:** EMG implant
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/EmgImplant.json`
- **Schema shape:** `object`
- **Required fields:** `implantMethod`, `wireCount`

Example payload for this type:
```json
{
  "wireCount": 1,
  "implantMethod": "direct insertion"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `anchoringMethod` | `string` | no | enum=["sutured to muscle", "cemented to skull", "subcutaneous tunnel", "tissue glue", "headcap", "other"] |
| `implantMethod` | `string` | yes | enum=["direct insertion", "needle-guided", "tunneled subcutaneously", "sutured", "other"] |
| `muscleTargets` | `string` | no | — |
| `sterilizationMethod` | `string` | no | enum=["Autoclave", "Ethylene Oxide", "Alcohol", "Gamma Irradiation", "None"] |
| `wireCount` | `integer` | yes | minimum=1; default=1 |
| `wireInsulation` | `string` | no | enum=["Teflon", "polyimide", "silicone", "none", "other"] |
| `wireMaterial` | `string` | no | format="text" |

### `GenericImplant`
- **Schema title:** Generic implant
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/GenericImplant.json`
- **Schema shape:** `object`
- **Required fields:** `implantType`

Example payload for this type:
```json
{
  "implantType": "sensor"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `anchoringMethod` | `string` | no | enum=["sutured", "tissue glue", "subcutaneous tunnel", "dental cement", "headcap", "custom mount", "none", "other"] |
| `implantName` | `string` | no | format="text" |
| `implantType` | `string` | yes | enum=["sensor", "electrode", "optical device", "mechanical device", "fluidic device", "structural support", "other"] |
| `powerSource` | `string` | no | enum=["battery", "inductive", "wired", "passive", "none", "other"] |
| `signalTransmission` | `string` | no | enum=["tethered", "wireless", "telemetric", "optical", "none", "other"] |
| `sterilizationMethod` | `string` | no | enum=["Autoclave", "Ethylene Oxide", "Alcohol", "Gamma Irradiation", "None"] |

### `GrinLensImplant`
- **Schema title:** GRIN lens implant
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/GrinLensImplant.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "lensTipType": "example",
  "lensId": "example",
  "sterilizationMethod": "Autoclave",
  "mountingMethod": "Cement only"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `lensId` | `string` | no | format="text" |
| `lensTipType` | `string` | no | format="text" |
| `mountingMethod` | `string` | no | enum=["Cement only", "Cement + baseplate", "Headcap integrated", "Custom holder", "Other"] |
| `sterilizationMethod` | `string` | no | enum=["Autoclave", "Ethylene Oxide", "Gamma Irradiation", "Alcohol", "None"] |

### `HeadFixation`
- **Schema title:** Head Fixation
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/HeadFixation.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fixationMethod": [],
  "alignment": "example",
  "fixationDetails": "example",
  "topicalAnesthesia": "example"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `alignment` | `string` | no | — |
| `fixationDetails` | `string` | no | — |
| `fixationMethod` | `array` | no | minItems=0 |
| `topicalAnesthesia` | `string` | no | — |

### `Headcap`
- **Schema title:** Headcap
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/Headcap.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "material": "example",
  "shape": "example",
  "constructionMethod": "manually built",
  "attachmentMethod": "dental cement"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `attachmentMethod` | `string` | no | enum=["dental cement", "UV-cured resin", "super glue", "epoxy", "screws", "other"] |
| `constructionMethod` | `string` | no | enum=["manually built", "custom-built", "3D-printed", "milled", "molded", "other"] |
| `headcapId` | `string` | no | format="text" |
| `material` | `string` | no | format="text" |
| `shape` | `string` | no | format="text" |
| `shielding` | `string` | no | enum=["none", "conductive paint", "copper mesh", "aluminum foil", "custom", "unknown"] |
| `skullPreparation` | `string` | no | format="text" |

### `Headpost`
- **Schema title:** Headpost
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/Headpost.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "material": "example",
  "shape": "example",
  "constructionMethod": "manually built",
  "attachmentMethod": "dental cement"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `attachmentMethod` | `string` | no | enum=["dental cement", "super glue", "epoxy", "screws", "other"] |
| `constructionMethod` | `string` | no | enum=["manually built", "custom-built", "3D-printed", "milled", "other"] |
| `headpostId` | `string` | no | format="text" |
| `material` | `string` | no | format="text" |
| `shape` | `string` | no | format="text" |
| `skullPreparation` | `string` | no | format="text" |

### `InhalantOverdose`
- **Schema title:** Inhalant overdose
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Procedure/InhalantOverdose.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "anestheticAgent": "Isoflurane",
  "concentration": {
    "unit": "%",
    "value": 0
  },
  "oxygenFlowRate": {
    "unit": "L/min",
    "value": 0
  },
  "deliveryMethod": "Anesthesia chamber"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `anestheticAgent` | `string` | no | enum=["Isoflurane", "Sevoflurane", "Halothane", "Desflurane", "Enflurane", "Other"] |
| `concentration` | `object(value:number, unit:enum[%, L/min, mL/min, mL/s])` | no | format="numberUnit"; default={"unit": "%"} |
| `confirmationOfDeath` | `array` | no | format="checkbox"; minItems=0 |
| `deliveryMethod` | `string` | no | enum=["Anesthesia chamber", "Nose cone", "Intubation", "Bell jar", "Other"] |
| `exposureDuration` | `object(value:number, unit:enum[µs, ms, s, min, h])` | no | format="numberUnit"; default={"unit": "min"} |
| `oxygenFlowRate` | `object(value:number, unit:enum[%, L/min, mL/min, mL/s])` | no | format="numberUnit"; default={"unit": "L/min"} |
| `sedationAgent` | `string` | no | format="text" |
| `timeToUnconsciousness` | `object(value:number, unit:enum[µs, ms, s, min, h])` | no | format="numberUnit"; default={"unit": "s"} |

### `Injection`
- **Schema title:** Injection
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Procedure/Injection.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "injectionVolume": {
    "unit": "mL",
    "value": 0
  },
  "injectionRate": {
    "unit": "mL/s",
    "value": 0
  },
  "concentration": {
    "unit": "mg/mL",
    "value": 0
  },
  "injectionMethod": "Intracerebroventricular (ICV)"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `concentration` | `object(value:number, unit:enum[mg/mL, µg/mL, g/L, mg/L, µg/L, % w/v, % v/v, % w/w])` | no | format="numberUnit"; default={"unit": "mg/mL"} |
| `injectionMethod` | `string` | no | enum=["Intracerebroventricular (ICV)", "Intramuscular (IM)", "Intravenous (IV)", "Intradermal (ID)", "Subcutaneous (SC)", "Intracardiac (IC)", "Intraperitoneal (IP)", "Intrathecal (IT)", "Epidural", "Retro-orbital (RO)", "Intranasal (IN)", "Intra-articular", "Intravitreal", "Intralesional"] |
| `injectionProfile` | `string` | no | enum=["Bolus Injection", "Continuous Infusion", "Tapered Dose", "Intermittent Bolus", "Staggered Injection", "Ramp Infusion", "Burst Infusion", "Step Infusion", "Layered Dosing", "Titration"] |
| `injectionRate` | `object(value:number, unit:enum[mL/s, µL/s, mL/min, µL/min])` | no | format="numberUnit"; default={"unit": "mL/s"} |
| `injectionSide` | `string` | no | enum=["Left", "Right", "Midline", "Unknown"] |
| `injectionVolume` | `object(value:number, unit:enum[L, mL, µL, nL, pL])` | no | format="numberUnit"; default={"unit": "mL"} |

### `NerveCuffImplant`
- **Schema title:** Nerve cuff implant
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/NerveCuffImplant.json`
- **Schema shape:** `object`
- **Required fields:** `anchoringMethod`, `cuffType`

Example payload for this type:
```json
{
  "cuffType": "monopolar",
  "anchoringMethod": "suture to surrounding tissue"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `anchoringMethod` | `string` | yes | enum=["suture to surrounding tissue", "tissue glue", "self-closing cuff", "non-anchored (loose fit)", "subcutaneous tunnel", "other"] |
| `cuffMaterial` | `string` | no | format="text" |
| `cuffType` | `string` | yes | enum=["monopolar", "bipolar", "tripolar", "multi-contact", "split-ring", "spiral", "other"] |
| `electrodeMaterial` | `string` | no | format="text" |
| `signalTransmission` | `string` | no | enum=["tethered", "wireless", "telemetric", "optical", "none", "other"] |
| `sterilizationMethod` | `string` | no | enum=["Autoclave", "Ethylene Oxide", "Alcohol", "Gamma Irradiation", "None"] |
| `targetNerve` | `string` | no | — |
| `wireExitRoute` | `string` | no | enum=["subcutaneous tunnel to headcap", "abdominal connector", "dorsal skin exit", "wireless/inductive", "other"] |

### `OdorStimulation`
- **Schema title:** Odor stimulation
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/OdorStimulation.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "odorants": "example",
  "deliveryMethod": "Olfactometer",
  "carrierGas": "Air",
  "stimulationContext": "Passive"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `carrierGas` | `string` | no | enum=["Air", "O₂", "N₂", "CO₂", "Other"] |
| `deliveryMethod` | `string` | no | enum=["Olfactometer", "Manually pipetted", "Syringe injection", "Headspace exposure", "Cotton swab", "Other"] |
| `odorants` | `string` | no | — |
| `paradigmDescription` | `string` | no | format="textarea" |
| `stimulationContext` | `string` | no | enum=["Passive", "Behavioral task", "Closed-loop", "Anesthetized", "Free behavior"] |

### `OpticFiberImplant`
- **Schema title:** Optic fiber implant
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/OpticFiberImplant.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fiberTipShape": "example",
  "fiberId": "example",
  "sterilizationMethod": "Autoclave"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `fiberId` | `string` | no | format="text" |
| `fiberTipShape` | `string` | no | format="text" |
| `sterilizationMethod` | `string` | no | enum=["Autoclave", "Ethylene Oxide", "Gamma Irradiation", "Alcohol", "None"] |

### `PerfusionFixation`
- **Schema title:** Brain Perfusion Fixation
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Procedure/PerfusionFixation.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "perfusionMethod": "example",
  "volume": {
    "unit": "mL",
    "value": 0
  },
  "fatalOutcome": false
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `fatalOutcome` | `boolean` | no | format="checkbox" |
| `perfusionMethod` | `string` | no | format="text" |
| `volume` | `object(value:number, unit:enum[L, mL, µL, nL, pL])` | no | format="numberUnit"; default={"unit": "mL"} |

### `PrismImplant`
- **Schema title:** Prism implant
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/PrismImplant.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "prismId": "example",
  "sterilizationMethod": "Autoclave",
  "mountingMethod": "Cement only"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `mountingMethod` | `string` | no | enum=["Cement only", "Cement + baseplate", "Headcap integrated", "Custom holder", "Other"] |
| `prismId` | `string` | no | format="text" |
| `sterilizationMethod` | `string` | no | enum=["Autoclave", "Ethylene Oxide", "Gamma Irradiation", "Alcohol", "None"] |

### `ReferenceElectrodeImplant`
- **Schema title:** Reference electrode implant
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Procedure/ReferenceElectrodeImplant.json`
- **Schema shape:** `object`
- **Required fields:** `electrodeCount`, `electrodeMaterial`

Example payload for this type:
```json
{
  "electrodeCount": 1,
  "electrodeMaterial": "stainless steel"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `anchoringMethod` | `string` | no | enum=["dental cement", "tissue glue", "bone screw", "subcutaneous tunnel", "other"] |
| `electrodeCount` | `integer` | yes | minimum=1; default=1 |
| `electrodeDiameter` | `object(value:number, unit:enum[µm, mm, nm, m])` | no | format="numberUnit"; default={"unit": "µm"} |
| `electrodeMaterial` | `string` | yes | format="text"; default="stainless steel" |
| `impedance` | `object(value:number, unit:enum[kΩ, Ω, MΩ])` | no | format="numberUnit"; default={"unit": "kΩ"} |
| `placementSite` | `string` | no | format="text" |
| `sterilizationMethod` | `string` | no | enum=["Autoclave", "Ethylene Oxide", "Gamma Irradiation", "Alcohol", "None"] |

### `SiliconProbeImplant`
- **Schema title:** Silicon probe implant
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/SiliconProbeImplant.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "probeId": "example",
  "sterilizationMethod": "Autoclave"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `probeId` | `string` | no | format="text" |
| `sterilizationMethod` | `string` | no | enum=["Autoclave", "Ethylene Oxide", "Gamma Irradiation", "Alcohol", "None"] |

### `SingleWireElectrodeImplant`
- **Schema title:** Single wire electrode implant
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Procedure/SingleWireElectrodeImplant.json`
- **Schema shape:** `object`
- **Required fields:** `wireCount`

Example payload for this type:
```json
{
  "wireCount": 1
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `impedance` | `object(value:number, unit:enum[Ω, kΩ, MΩ])` | no | format="numberUnit"; default={"unit": "kΩ"} |
| `sterilizationMethod` | `string` | no | enum=["Autoclave", "Ethylene Oxide", "Gamma Irradiation", "Alcohol", "None"] |
| `wireCount` | `integer` | yes | minimum=0; default=1 |
| `wireDiameter` | `object(value:number, unit:enum[µm, mm, nm, m])` | no | format="numberUnit"; default={"unit": "µm"} |
| `wireMaterial` | `string` | no | format="text" |

### `TactileStimulation`
- **Schema title:** Tactile stimulation
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/TactileStimulation.json`
- **Schema shape:** `object`
- **Required fields:** `stimulusTypes`

Example payload for this type:
```json
{
  "stimulusTypes": []
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `deliveryMethod` | `string` | no | enum=["Manual (e.g., cotton swab)", "Piezo actuator", "Solenoid piston", "Air puff system", "Brush or probe", "Other"] |
| `paradigmDescription` | `string` | no | format="textarea" |
| `stimulationContext` | `string` | no | enum=["Passive", "Behavioral task", "Closed-loop", "Anesthetized", "Free behavior"] |
| `stimulationSite` | `string` | no | — |
| `stimulusTypes` | `array` | yes | — |

### `TemperatureSensorImplant`
- **Schema title:** Temperature sensor implant
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/TemperatureSensorImplant.json`
- **Schema shape:** `object`
- **Required fields:** `anchoringMethod`, `sensorType`

Example payload for this type:
```json
{
  "sensorType": "thermocouple",
  "anchoringMethod": "sutured"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `anchoringMethod` | `string` | yes | enum=["sutured", "tissue glue", "subcutaneous tunnel", "cemented to skull", "headcap", "free-floating", "other"] |
| `powerSource` | `string` | no | enum=["battery", "inductive", "wired", "passive", "none", "other"] |
| `sensorType` | `string` | yes | enum=["thermocouple", "thermistor", "digital IC", "telemetric sensor", "logger (passive)", "fiber-optic", "other"] |
| `signalTransmission` | `string` | no | enum=["tethered", "wireless", "telemetric", "optical", "logger (retrieved)", "none", "other"] |
| `sterilizationMethod` | `string` | no | enum=["Autoclave", "Ethylene Oxide", "Alcohol", "Gamma Irradiation", "None"] |
| `wireMaterial` | `string` | no | format="text" |

### `TetrodeWireElectrodeImplant`
- **Schema title:** Tetrode wire electrode implant
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Procedure/TetrodeWireElectrodeImplant.json`
- **Schema shape:** `object`
- **Required fields:** `tetrodeCount`

Example payload for this type:
```json
{
  "tetrodeCount": 1
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `nWiresTetrode` | `integer` | no | minimum=0; default=4 |
| `sterilizationMethod` | `string` | no | enum=["Autoclave", "Ethylene Oxide", "Gamma Irradiation", "Alcohol", "None"] |
| `tetrodeCount` | `integer` | yes | minimum=0; default=1 |
| `wireDiameter` | `object(value:number, unit:enum[µm, mm, nm, m])` | no | format="numberUnit"; default={"unit": "µm"} |
| `wireMaterial` | `string` | no | format="text" |

### `TissueClearing`
- **Schema title:** Tissue clearing
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Procedure/TissueClearing.json`
- **Schema shape:** `object`
- **Required fields:** `clearingMethod`

Example payload for this type:
```json
{
  "clearingMethod": "CLARITY"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `agitation` | `string` | no | enum=["Gentle shaking", "Rotation", "Static", "Other"] |
| `clearingDuration` | `object(value:number, unit:enum[µs, ms, s, min, h, days])` | no | format="numberUnit"; default={"unit": "days"} |
| `clearingMethod` | `string` | yes | enum=["CLARITY", "CUBIC", "3DISCO", "iDISCO+", "PACT", "ScaleS", "SeeDB", "BABB (Benzyl alcohol/Benzyl benzoate)", "Passive CLARITY", "Other"] |
| `complications` | `string` | no | format="textarea" |
| `fixationTime` | `object(value:number, unit:enum[µs, ms, s, min, h, days])` | no | format="numberUnit"; default={"unit": "h"} |
| `imagingCompatible` | `boolean` | no | format="checkbox" |
| `refractiveIndexMatching` | `string` | no | format="text" |
| `temperature` | `object(value:number, unit:enum[°C, K, °F])` | no | format="numberUnit"; default={"unit": "°C"} |
| `tissueType` | `string` | no | — |
| `transparency` | `string` | no | enum=["Complete", "Partial", "Poor", "Failed"] |

### `VibratomeSectioning`
- **Schema title:** Vibratome sectioning
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Procedure/VibratomeSectioning.json`
- **Schema shape:** `object`
- **Required fields:** `bladeType`

Example payload for this type:
```json
{
  "bladeType": "Disposable razor blade"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `amplitude` | `string` | no | enum=["Minimum", "Low", "Medium", "High", "Maximum"] |
| `bladeType` | `string` | yes | enum=["Disposable razor blade", "Steel blade", "Ceramic blade", "Sapphire blade", "Other"] |
| `buffer` | `string` | no | format="text" |
| `bufferTemperature` | `object(value:number, unit:enum[°C, K, °F])` | no | format="numberUnit"; default={"unit": "°C"} |
| `cuttingSpeed` | `string` | no | enum=["Very slow", "Slow", "Medium", "Fast", "Very fast"] |
| `frequency` | `object(value:number, unit:enum[Hz, kHz, MHz, GHz])` | no | format="numberUnit"; default={"unit": "Hz"} |
| `numberOfSections` | `number` | no | minimum=0 |
| `sectionQuality` | `string` | no | enum=["Excellent", "Good", "Fair", "Poor"] |
| `sectionThickness` | `object(value:number, unit:enum[µm, mm, nm, m])` | no | format="numberUnit"; default={"unit": "µm"} |
| `sectioningOrientation` | `string` | no | enum=["Coronal", "Sagittal", "Horizontal", "Other"] |
| `storageMethod` | `string` | no | enum=["Free-floating in buffer", "Mounted immediately", "Stored in multiwell plates", "Other"] |

### `VirusInjection`
- **Schema title:** Virus Injection
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/Procedure/VirusInjection.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "injectionVolume": {
    "unit": "nL",
    "value": 0
  },
  "injectionRate": {
    "unit": "nL/min",
    "value": 0
  },
  "titer": {
    "unit": "vg/mL",
    "value": 0
  },
  "injectionProfile": "Bolus Injection"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `injectionProfile` | `string` | no | enum=["Bolus Injection", "Continuous Infusion", "Tapered Dose", "Intermittent Bolus", "Staggered Injection", "Ramp Infusion", "Burst Infusion", "Step Infusion", "Layered Dosing", "Titration"] |
| `injectionRate` | `object(value:number, unit:enum[nL/min, µL/min, mL/min, nL/s, µL/s])` | no | format="numberUnit"; default={"unit": "nL/min"} |
| `injectionVolume` | `object(value:number, unit:enum[nL, µL, mL, L])` | no | format="numberUnit"; default={"unit": "nL"} |
| `titer` | `object(value:number, unit:enum[vg/mL, TU/mL, pfu/mL])` | no | format="numberUnit"; default={"unit": "vg/mL"} |

### `VisualStimulation`
- **Schema title:** Visual stimulation
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/Procedure/VisualStimulation.json`
- **Schema shape:** `object`
- **Required fields:** `stimulusTypes`

Example payload for this type:
```json
{
  "stimulusTypes": []
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `paradigmDescription` | `string` | no | format="textarea" |
| `presentationDevice` | `string` | no | enum=["Monitor", "LED panel", "Projector", "Head-mounted display", "Fiber-coupled light source", "Other"] |
| `stimulationContext` | `string` | no | enum=["Passive", "Behavioral task", "Closed-loop", "Anesthetized", "Free behavior"] |
| `stimulationPosition` | `string` | no | enum=["Contralateral", "Ipsilateral", "Bilateral", "Centered", "Surround", "Other", "Unknown"] |
| `stimulusTypes` | `array` | yes | — |
