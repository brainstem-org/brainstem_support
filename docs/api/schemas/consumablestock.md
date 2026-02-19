---
layout: default
title: ConsumableStock
parent: Schemas
grand_parent: API
nav_order: 2
---

# ConsumableStock schemas
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## How to use this page

- Use this page when calling `/api/private/modules/consumablestock/`.
- Set `type` to one schema name from the list below.
- Send `details` that matches that schema exactly.
- Use this for inventory metadata keyed by consumable stock type.

## Quick type map

| Type value | Schema version | Required fields | Schema shape |
|:-----------|:---------------|:----------------|:-------------|
| `ChemicalReagent` | `1.2.0` | `chemicalType` | `object` |
| `ConsumableDevice` | `1.0.0` | `deviceClass` | `object` |
| `ImmunoReagent` | `1.1.0` | `reagentType` | `object` |
| `ImplantMaterial` | `1.0.0` | none | `object` |
| `OpticFiber` | `1.0.0` | none | `object` |
| `OpticalComponent` | `1.2.0` | `componentType` | `object` |
| `PharmacologicalAgent` | `1.1.0` | `pharmacologicalCategory` | `object` |
| `PhysiologicalSolution` | `1.1.0` | none | `object` |
| `SiliconProbe` | `1.0.0` | none | `object` |
| `SingleWireElectrode` | `1.1.0` | none | `object` |
| `SurgicalDisposable` | `1.0.0` | none | `object` |
| `TracerDye` | `1.2.0` | `dyeType` | `object` |
| `VirusSolution` | `1.1.1` | none | `object` |

## Examples

### ConsumableStock payload fragment
```json
{
  "type": "ChemicalReagent",
  "details": {
    "chemicalType": "Detergent"
  }
}
```

## Request pattern
```json
{
  "type": "ChemicalReagent",
  "details": {
    "chemicalType": "Detergent"
  }
}
```

## Schema reference

### `ChemicalReagent`
- **Schema title:** Chemical Reagent
- **Schema version:** `1.2.0`
- **Source:** `brainstem/schemas/ConsumableStock/ChemicalReagent.json`
- **Schema shape:** `object`
- **Required fields:** `chemicalType`

Example payload for this type:
```json
{
  "chemicalType": "Detergent"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `amount` | `string` | no | format="text" |
| `batchId` | `string` | no | format="text" |
| `chemicalType` | `string` | yes | enum=["Detergent", "Enzyme", "Fixative", "Indicator or pH Adjuster", "Salt or Buffer", "Solvent", "Stain or Dye", "Polymer or Resin", "Other"] |
| `compoundName` | `string` | no | format="text" |
| `concentration` | `string` | no | format="text" |
| `hazardInfo` | `string` | no | format="textarea" |
| `molecularWeight` | `object(value:number, unit:enum[g/mol, kDa, Da])` | no | format="numberUnit"; default={"unit": "g/mol"} |
| `purity` | `string` | no | format="text" |

### `ConsumableDevice`
- **Schema title:** Consumable Device
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/ConsumableStock/ConsumableDevice.json`
- **Schema shape:** `object`
- **Required fields:** `deviceClass`

Example payload for this type:
```json
{
  "deviceClass": "Headstage"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `compatibleWith` | `string` | no | format="text" |
| `connectivity` | `string` | no | format="text" |
| `deviceClass` | `string` | yes | enum=["Headstage", "Headstage Adapter", "Miniscope Baseplate", "Microdrive", "Drive Mount", "Fiber Cannula Assembly", "Commutator Adapter", "Thermal Interface Board", "Connector Assembly", "Custom Fixture", "Other"] |
| `dimensions` | `string` | no | format="text" |
| `experimentalUse` | `array` | no | — |
| `material` | `string` | no | format="text" |
| `productId` | `string` | no | format="text" |

### `ImmunoReagent`
- **Schema title:** Antibody or Immunoreagent
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/ConsumableStock/ImmunoReagent.json`
- **Schema shape:** `object`
- **Required fields:** `reagentType`

Example payload for this type:
```json
{
  "reagentType": "Primary Antibody"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `amount` | `string` | no | format="text" |
| `application` | `array` | no | — |
| `batchId` | `string` | no | format="text" |
| `clonality` | `string` | no | enum=["Monoclonal", "Polyclonal", "Recombinant", "Unknown"] |
| `conjugate` | `string` | no | format="text" |
| `dilution` | `string` | no | format="text" |
| `hostSpecies` | `string` | no | — |
| `reactivity` | `string` | no | — |
| `reagentType` | `string` | yes | enum=["Primary Antibody", "Secondary Antibody", "Fluorescent Label", "DNA Counterstain", "Other"] |
| `targetAntigen` | `string` | no | format="text" |

### `ImplantMaterial`
- **Schema title:** Implant or fixation material
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/ConsumableStock/ImplantMaterial.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "batchId": "example",
  "amount": "example",
  "preparationInstructions": "example",
  "sterile": false
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `amount` | `string` | no | format="text" |
| `batchId` | `string` | no | format="text" |
| `preparationInstructions` | `string` | no | format="textarea" |
| `sterile` | `boolean` | no | format="checkbox" |

### `OpticFiber`
- **Schema title:** Optic fiber
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/ConsumableStock/OpticFiber.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "fiberIds": "example",
  "quantity": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `fiberIds` | `string` | no | format="text" |
| `quantity` | `integer` | no | minimum=0 |

### `OpticalComponent`
- **Schema title:** Optical Component
- **Schema version:** `1.2.0`
- **Source:** `brainstem/schemas/ConsumableStock/OpticalComponent.json`
- **Schema shape:** `object`
- **Required fields:** `componentType`

Example payload for this type:
```json
{
  "componentType": "GRIN Lens"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `coating` | `string` | no | format="text" |
| `componentType` | `string` | yes | enum=["GRIN Lens", "Cranial Window", "Cover Glass", "Microprism", "Beamsplitter", "Optical Filter", "Relay Lens", "Other"] |
| `dimensions` | `string` | no | format="text" |
| `experimentalUse` | `array` | no | — |
| `material` | `string` | no | format="text" |
| `productId` | `string` | no | format="text" |
| `sterile` | `boolean` | no | — |
| `wavelengthMax` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "nm"} |
| `wavelengthMin` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "nm"} |

### `PharmacologicalAgent`
- **Schema title:** Pharmacological Agent
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/ConsumableStock/PharmacologicalAgent.json`
- **Schema shape:** `object`
- **Required fields:** `pharmacologicalCategory`

Example payload for this type:
```json
{
  "pharmacologicalCategory": "Analgesic"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `activeIngredient` | `string` | no | format="text" |
| `amount` | `string` | no | format="text" |
| `batchId` | `string` | no | format="text" |
| `concentration` | `string` | no | format="text" |
| `dosageForm` | `string` | no | enum=["Solution", "Suspension", "Tablet", "Capsule", "Injection", "Topical", "Patch", "Other"] |
| `experimentalUse` | `array` | no | — |
| `formulation` | `string` | no | format="text" |
| `pharmacologicalCategory` | `string` | yes | enum=["Analgesic", "Anesthetic", "Antibiotic", "Neuroactive", "Recreational", "Vehicle", "Experimental", "Other"] |
| `pharmacologicalClass` | `string` | no | format="text" |
| `purity` | `string` | no | format="text" |
| `routeOfAdministration` | `string` | no | enum=["Intraperitoneal (IP)", "Intravenous (IV)", "Subcutaneous (SC)", "Oral", "Topical", "Inhalation", "Intracerebral", "Other"] |

### `PhysiologicalSolution`
- **Schema title:** Physiological Solution
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/ConsumableStock/PhysiologicalSolution.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "solutionName": "example",
  "composition": "example",
  "amount": "example",
  "pH": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `amount` | `string` | no | format="text" |
| `composition` | `string` | no | format="textarea" |
| `osmolality` | `string` | no | format="text" |
| `pH` | `number` | no | minimum=0 |
| `preparationInstructions` | `string` | no | format="textarea" |
| `purpose` | `array` | no | — |
| `solutionName` | `string` | no | format="text" |
| `sterile` | `boolean` | no | — |

### `SiliconProbe`
- **Schema title:** Silicon probe
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/ConsumableStock/SiliconProbe.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "probeIds": "example",
  "quantity": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `probeIds` | `string` | no | format="text" |
| `quantity` | `integer` | no | minimum=0 |

### `SingleWireElectrode`
- **Schema title:** Single wire electrode
- **Schema version:** `1.1.0`
- **Source:** `brainstem/schemas/ConsumableStock/SingleWireElectrode.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "wireIds": "example",
  "quantity": 0,
  "length": {
    "unit": "mm",
    "value": 0
  }
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `length` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "mm"} |
| `quantity` | `integer` | no | minimum=0 |
| `wireIds` | `string` | no | format="text" |

### `SurgicalDisposable`
- **Schema title:** Surgical disposable
- **Schema version:** `1.0.0`
- **Source:** `brainstem/schemas/ConsumableStock/SurgicalDisposable.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "batchId": "example",
  "quantity": 0,
  "sterile": false
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `batchId` | `string` | no | format="text" |
| `quantity` | `integer` | no | minimum=0 |
| `sterile` | `boolean` | no | format="checkbox" |

### `TracerDye`
- **Schema title:** Tracer or Dye
- **Schema version:** `1.2.0`
- **Source:** `brainstem/schemas/ConsumableStock/TracerDye.json`
- **Schema shape:** `object`
- **Required fields:** `dyeType`

Example payload for this type:
```json
{
  "dyeType": "Fluorescent Tracer"
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `amount` | `string` | no | format="text" |
| `batchId` | `string` | no | format="text" |
| `dyeType` | `string` | yes | enum=["Fluorescent Tracer", "Lipophilic Dye", "Retrograde Tracer", "Anterograde Tracer", "Histological Dye", "Vital Stain", "Injection Marker", "Other"] |
| `emissionPeak` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "nm"} |
| `excitationPeak` | `object(value:number, unit:enum[nm, µm, mm, m])` | no | format="numberUnit"; default={"unit": "nm"} |
| `experimentalUse` | `array` | no | — |
| `fluorophore` | `string` | no | format="text" |
| `preparationInstructions` | `string` | no | format="textarea" |
| `routeOfApplication` | `string` | no | enum=["Injection", "Perfusion", "Topical", "Incubation", "Other"] |
| `solvent` | `string` | no | format="text" |

### `VirusSolution`
- **Schema title:** Virus construct
- **Schema version:** `1.1.1`
- **Source:** `brainstem/schemas/ConsumableStock/VirusSolution.json`
- **Schema shape:** `object`
- **Required fields:** none

Example payload for this type:
```json
{
  "batchId": "example",
  "titer": {
    "unit": "vg/mL",
    "value": 0
  },
  "volume": {
    "unit": "mL",
    "value": 0
  },
  "aliquotCount": 0
}
```

| Field | Expected value | Required | Constraints/format |
|:------|:---------------|:---------|:-------------------|
| `aliquotCount` | `integer` | no | minimum=0 |
| `aliquotVolume` | `object(value:number, unit:enum[nL, µL, mL, L])` | no | format="numberUnit"; default={"unit": "µL"} |
| `batchId` | `string` | no | format="text" |
| `titer` | `object(value:number, unit:enum[vg/mL, TU/mL, pfu/mL])` | no | format="numberUnit"; default={"unit": "vg/mL"} |
| `volume` | `object(value:number, unit:enum[nL, µL, mL, L])` | no | format="numberUnit"; default={"unit": "mL"} |
