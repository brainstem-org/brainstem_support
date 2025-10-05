---
layout: default
title: Procedure
parent: Schemas
grand_parent: API
nav_order: 1
---

# Procedure schemas
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Optic fiber implant
```
{
    "type": "object",
    "title": "Optic fiber implant",
    "properties": {
        "fiberTipShape": {
            "title": "Fiber tip shape",
            "type": "string",
            "format": "text",
            "default": "flat"
        }
    },
    "required": ["fiberTipShape"]
}
```

*Fiber tip shape* is a **required** field - **default** value set is `flat`.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "fiberTipShape": "flat"
}
```

## Silicon probe implant
```
{
    "type": "object",
    "title": "Silicon probe implant",
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{ }
```

## Single wire electrode
```
{
    "type": "object",
    "title": "Single wire electrode",
    "properties": {
        "wireCount": {
            "title": "Wire count",
            "type": "number",
            "minimum": 0,
            "default": 1
        },
        "wireDiameter": {
            "title": "Wire diameter (µm)",
            "type": "number",
            "minimum": 0
        },
        "wireMaterial": {
            "title": "Wire material",
            "type": "string",
            "format": "text"
        }
    },
    "required": ["wireCount"]
}
```

*Wire count* is a **required** field - **default** value set is `1`.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "wireCount": 4,
    "wireDiameter": 50,
    "wireMaterial": "Titanium",
    "rotation": 0,
    "apAngle": 15,
    "mlAngle": 15
}
```

## Tetrode wire electrode
```
{
    "type": "object",
    "title": "Tetrode wire electrode",
    "properties": {
        "tetrodeCount": {
            "title": "Tetrode count",
            "type": "integer",
            "minimum": 0,
            "default": 1
        },
        "nWiresTetrode": {
            "title": "Wires per tetrode",
            "type": "integer",
            "minimum": 0,
            "default": 4
        },
        "wireDiameter": {
            "title": "Wire diameter (µm)",
            "type": "number",
            "minimum": 0
        },
        "wireMaterial": {
            "title": "Wire material",
            "type": "string",
            "format": "text"
        }
    },
    "required": ["tetrodeCount"]
}
```

*Tetrode count* is a **required** field - **default** value set is `1`.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "tetrodeCount": 2,
    "nWiresTetrode": 4,
    "wireDiameter": 50,
    "wireMaterial": "Titanium"
}
```

## Anesthesia
```
{
    "type": "object",
    "title": "Anesthesia",
    "properties": {
        "anestheticAgent": {
            "title": "Anesthetic agent",
            "type": "string",
            "enum": [
                "Isoflurane",
                "Sevoflurane",
                "Ketamine",
                "Ketamine + Xylazine",
                "Ketamine + Dexmedetomidine",
                "Pentobarbital",
                "Urethane",
                "Tribromoethanol (Avertin)",
                "Propofol",
                "Other"
            ]
        },
        "route": {
            "title": "Administration route",
            "type": "string",
            "enum": [
                "Inhalation",
                "Intraperitoneal (IP)",
                "Intravenous (IV)",
                "Subcutaneous (SC)",
                "Intramuscular (IM)",
                "Oral",
                "Other"
            ]
        },
        "dosage": {
            "title": "Dosage",
            "type": "string",
            "format": "text"
        },
        "depth": {
            "title": "Anesthetic depth",
            "type": "string",
            "enum": [
                "Light sedation",
                "Moderate sedation",
                "Deep sedation",
                "Surgical plane",
                "Other"
            ]
        },
        "duration": {
            "title": "Duration (minutes)",
            "type": "number",
            "minimum": 0
        },
        "endOfAnesthesia": {
            "title": "End of anesthesia",
            "type": "string",
            "format": "time"
        },
        "complications": {
            "title": "Complications",
            "type": "string",
            "format": "textarea"
        },
        "recoveryTime": {
            "title": "Recovery time (minutes)",
            "type": "number",
            "minimum": 0
        },
        "monitoringMethod": {
            "type": "array",
            "title": "Monitoring methods",
            "items": {
                "type": "string",
                "enum": [
                    "Blood pressure",
                    "EEG",
                    "Heart rate",
                    "Pulse oximetry",
                    "Respiratory rate",
                    "Toe pinch reflex",
                    "None",
                    "Other"
                ]
            },
            "uniqueItems": true,
            "minItems": 0,
            "format": "checkbox"
        },
        "supportiveCare": {
            "type": "array",
            "title": "Supportive care",
            "items": {
                "type": "string",
                "enum": [
                    "Eye lubricant",
                    "Fluid therapy",
                    "Heating pad",
                    "Oxygen supplementation",
                    "None",
                    "Other"
                ]
            },
            "uniqueItems": true,
            "minItems": 0,
            "format": "checkbox"
        }
    },
    "required": ["anestheticAgent", "route"]
}
```

*Anesthetic agent* is a **required** field.
*Administration route* is a **required** field.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "anestheticAgent": "Isoflurane",
    "route": "Inhalation",
    "dosage": "2% in 10% oxygen",
    "depth": "Surgical plane",
    "duration": 120,
    "recoveryTime": 15,
    "monitoringMethod": ["Heart rate", "Respiratory rate", "Toe pinch reflex"],
    "supportiveCare": ["Eye lubricant", "Heating pad"]
}
```

## Auditory stimulation
```
{
    "type": "object",
    "title": "Auditory stimulation",
    "properties": {
        "stimulusType": {
            "title": "Stimulus type",
            "type": "string",
            "enum": [
                "Pure tone",
                "White noise",
                "Pink noise",
                "Broadband noise",
                "Click train",
                "Frequency sweep",
                "Natural sound",
                "Other"
            ]
        },
        "frequency": {
            "title": "Frequency (Hz)",
            "type": "number",
            "minimum": 0
        },
        "intensity": {
            "title": "Intensity (dB SPL)",
            "type": "number"
        },
        "duration": {
            "title": "Duration (ms)",
            "type": "number",
            "minimum": 0
        },
        "repetitionRate": {
            "title": "Repetition rate (Hz)",
            "type": "number",
            "minimum": 0
        },
        "ear": {
            "title": "Ear stimulated",
            "type": "string",
            "enum": ["Left", "Right", "Bilateral", "Both"]
        },
        "soundSource": {
            "title": "Sound source",
            "type": "string",
            "enum": ["Speaker", "Headphones", "Earphones", "Bone conduction", "Other"]
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "stimulusType": "Pure tone",
    "frequency": 8000,
    "intensity": 70,
    "duration": 100,
    "repetitionRate": 10,
    "ear": "Bilateral",
    "soundSource": "Speaker"
}
```

## Barbiturate injection
```
{
    "type": "object",
    "title": "Barbiturate injection",
    "properties": {
        "barbiturateType": {
            "title": "Barbiturate type",
            "type": "string",
            "enum": [
                "Pentobarbital",
                "Phenobarbital",
                "Thiopental",
                "Methohexital",
                "Other"
            ]
        },
        "dosage": {
            "title": "Dosage (mg/kg)",
            "type": "number",
            "minimum": 0
        },
        "concentration": {
            "title": "Concentration (mg/mL)",
            "type": "number",
            "minimum": 0
        },
        "volume": {
            "title": "Volume (mL)",
            "type": "number",
            "minimum": 0
        },
        "route": {
            "title": "Administration route",
            "type": "string",
            "enum": [
                "Intraperitoneal (IP)",
                "Intravenous (IV)",
                "Subcutaneous (SC)",
                "Intramuscular (IM)",
                "Other"
            ]
        },
        "injectionRate": {
            "title": "Injection rate (mL/s)",
            "type": "number",
            "minimum": 0
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "barbiturateType": "Pentobarbital",
    "dosage": 50,
    "concentration": 50,
    "volume": 1.0,
    "route": "Intraperitoneal (IP)",
    "injectionRate": 0.1
}
```

## Behavioral tracking
```
{
    "type": "object",
    "title": "Behavioral tracking",
    "properties": {
        "trackingMethod": {
            "title": "Tracking method",
            "type": "string",
            "enum": [
                "Video tracking",
                "RFID tracking",
                "Infrared tracking",
                "Ultrasonic tracking",
                "Magnetic tracking",
                "Accelerometer",
                "Gyroscope",
                "Other"
            ]
        },
        "trackingSystem": {
            "title": "Tracking system",
            "type": "string",
            "format": "text"
        },
        "trackingDuration": {
            "title": "Tracking duration (minutes)",
            "type": "number",
            "minimum": 0
        },
        "samplingRate": {
            "title": "Sampling rate (Hz)",
            "type": "number",
            "minimum": 0
        },
        "trackingEnvironment": {
            "title": "Tracking environment",
            "type": "string",
            "enum": [
                "Open field",
                "Home cage",
                "Maze",
                "Treadmill",
                "Running wheel",
                "Other"
            ]
        },
        "animalState": {
            "title": "Animal state",
            "type": "string",
            "enum": [
                "Awake",
                "Anesthetized",
                "Sleeping",
                "Head-fixed",
                "Freely moving",
                "Other"
            ]
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "trackingMethod": "Video tracking",
    "trackingSystem": "DeepLabCut",
    "trackingDuration": 30,
    "samplingRate": 30,
    "trackingEnvironment": "Open field",
    "animalState": "Freely moving"
}
```

## Blood pressure sensor implant
```
{
    "type": "object",
    "title": "Blood pressure sensor implant",
    "properties": {
        "sensorType": {
            "title": "Sensor type",
            "type": "string",
            "enum": [
                "Telemetry",
                "Catheter-based",
                "Non-invasive cuff",
                "Implantable pressure transducer",
                "Other"
            ]
        },
        "sensorModel": {
            "title": "Sensor model",
            "type": "string",
            "format": "text"
        },
        "implantationSite": {
            "title": "Implantation site",
            "type": "string",
            "enum": [
                "Carotid artery",
                "Femoral artery",
                "Aortic arch",
                "Left ventricle",
                "Tail artery",
                "Other"
            ]
        },
        "calibrationMethod": {
            "title": "Calibration method",
            "type": "string",
            "enum": [
                "Zero pressure",
                "Known pressure",
                "In vivo calibration",
                "Factory calibrated",
                "Other"
            ]
        },
        "recordingDuration": {
            "title": "Recording duration (days)",
            "type": "number",
            "minimum": 0
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "sensorType": "Telemetry",
    "sensorModel": "PA-C10",
    "implantationSite": "Carotid artery",
    "calibrationMethod": "Factory calibrated",
    "recordingDuration": 30
}
```

## Brain extraction
```
{
    "type": "object",
    "title": "Brain extraction",
    "properties": {
        "extractionMethod": {
            "title": "Extraction method",
            "type": "string",
            "enum": [
                "Standard extraction",
                "Rapid extraction",
                "Perfusion-fixed extraction",
                "Fresh extraction",
                "Other"
            ]
        },
        "fixationMethod": {
            "title": "Fixation method",
            "type": "string",
            "enum": [
                "Perfusion fixation",
                "Immersion fixation",
                "Fresh (no fixation)",
                "Other"
            ]
        },
        "fixative": {
            "title": "Fixative used",
            "type": "string",
            "enum": [
                "Paraformaldehyde (PFA)",
                "Formalin",
                "Glutaraldehyde",
                "Paraformaldehyde + Glutaraldehyde",
                "Other"
            ]
        },
        "fixativeConcentration": {
            "title": "Fixative concentration (%)",
            "type": "number",
            "minimum": 0
        },
        "postFixationTime": {
            "title": "Post-fixation time (hours)",
            "type": "number",
            "minimum": 0
        },
        "storageSolution": {
            "title": "Storage solution",
            "type": "string",
            "enum": [
                "PBS",
                "Cryoprotectant",
                "Formalin",
                "Other"
            ]
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "extractionMethod": "Perfusion-fixed extraction",
    "fixationMethod": "Perfusion fixation",
    "fixative": "Paraformaldehyde (PFA)",
    "fixativeConcentration": 4,
    "postFixationTime": 24,
    "storageSolution": "PBS"
}
```

## Brain lesion
```
{
    "type": "object",
    "title": "Brain lesion",
    "properties": {
        "lesionMethod": {
            "title": "Lesion method",
            "type": "string",
            "enum": [
                "Chemical",
                "Electrical",
                "Mechanical",
                "Thermal",
                "Laser",
                "Optogenetic",
                "Other"
            ]
        },
        "lesionAgent": {
            "title": "Lesion agent",
            "type": "string",
            "format": "text"
        },
        "targetRegion": {
            "title": "Target region",
            "type": "string",
            "format": "text"
        },
        "lesionSize": {
            "title": "Lesion size (mm)",
            "type": "number",
            "minimum": 0
        },
        "lesionDuration": {
            "title": "Lesion duration (minutes)",
            "type": "number",
            "minimum": 0
        },
        "intensity": {
            "title": "Intensity",
            "type": "number"
        },
        "coordinates": {
            "title": "Coordinates",
            "type": "string",
            "format": "text"
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "lesionMethod": "Chemical",
    "lesionAgent": "Ibotenic acid",
    "targetRegion": "Hippocampus",
    "lesionSize": 0.5,
    "lesionDuration": 10,
    "coordinates": "AP: -2.0 mm, ML: ±1.5 mm, DV: -1.8 mm"
}
```

## Brain slice
```
{
    "type": "object",
    "title": "Brain slice",
    "properties": {
        "sliceMethod": {
            "title": "Slice method",
            "type": "string",
            "enum": [
                "Vibratome",
                "Tissue chopper",
                "Microtome",
                "Other"
            ]
        },
        "sliceThickness": {
            "title": "Slice thickness (μm)",
            "type": "number",
            "minimum": 0
        },
        "sliceOrientation": {
            "title": "Slice orientation",
            "type": "string",
            "enum": [
                "Coronal",
                "Sagittal",
                "Horizontal",
                "Oblique",
                "Other"
            ]
        },
        "sliceLocation": {
            "title": "Slice location",
            "type": "string",
            "format": "text"
        },
        "cuttingSolution": {
            "title": "Cutting solution",
            "type": "string",
            "enum": [
                "Sucrose-based ACSF",
                "NMDG-based ACSF",
                "Standard ACSF",
                "Other"
            ]
        },
        "temperature": {
            "title": "Temperature (°C)",
            "type": "number"
        },
        "recoveryTime": {
            "title": "Recovery time (minutes)",
            "type": "number",
            "minimum": 0
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "sliceMethod": "Vibratome",
    "sliceThickness": 300,
    "sliceOrientation": "Coronal",
    "sliceLocation": "Visual cortex",
    "cuttingSolution": "Sucrose-based ACSF",
    "temperature": 4,
    "recoveryTime": 30
}
```

## Breathing sensor implant
```
{
    "type": "object",
    "title": "Breathing sensor implant",
    "properties": {
        "sensorType": {
            "title": "Sensor type",
            "type": "string",
            "enum": [
                "Thermistor",
                "Pressure sensor",
                "Piezoelectric sensor",
                "Optical sensor",
                "Capacitive sensor",
                "Other"
            ]
        },
        "sensorModel": {
            "title": "Sensor model",
            "type": "string",
            "format": "text"
        },
        "implantationSite": {
            "title": "Implantation site",
            "type": "string",
            "enum": [
                "Nostril",
                "Chest wall",
                "Diaphragm",
                "Trachea",
                "Other"
            ]
        },
        "placementMethod": {
            "title": "Placement method",
            "type": "string",
            "enum": [
                "Surgical implantation",
                "Adhesive attachment",
                "External placement",
                "Other"
            ]
        },
        "calibrationRequired": {
            "title": "Calibration required",
            "type": "boolean"
        },
        "recordingDuration": {
            "title": "Recording duration (days)",
            "type": "number",
            "minimum": 0
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "sensorType": "Thermistor",
    "sensorModel": "TH-10",
    "implantationSite": "Nostril",
    "placementMethod": "Adhesive attachment",
    "calibrationRequired": true,
    "recordingDuration": 7
}
```

## Burr hole
```
{
    "type": "object",
    "title": "Burr hole",
    "properties": {
        "drillBitSize": {
            "title": "Drill bit size (mm)",
            "type": "number",
            "minimum": 0
        },
        "holeDiameter": {
            "title": "Hole diameter (mm)",
            "type": "number",
            "minimum": 0
        },
        "coordinates": {
            "title": "Coordinates",
            "type": "string",
            "format": "text"
        },
        "targetStructure": {
            "title": "Target structure",
            "type": "string",
            "format": "text"
        },
        "drillingMethod": {
            "title": "Drilling method",
            "type": "string",
            "enum": [
                "Hand drill",
                "Electric drill",
                "Micro-drill",
                "Other"
            ]
        },
        "duraIntact": {
            "title": "Dura intact",
            "type": "boolean"
        },
        "hemostasisMethod": {
            "title": "Hemostasis method",
            "type": "string",
            "enum": [
                "Bone wax",
                "Gelfoam",
                "Cautery",
                "Pressure",
                "Other"
            ]
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "drillBitSize": 0.5,
    "holeDiameter": 0.5,
    "coordinates": "AP: -2.0 mm, ML: +2.0 mm",
    "targetStructure": "Primary motor cortex",
    "drillingMethod": "Micro-drill",
    "duraIntact": true,
    "hemostasisMethod": "Bone wax"
}
```

## Catheter implant
```
{
    "type": "object",
    "title": "Catheter implant",
    "properties": {
        "targetSite": {
            "title": "Target site",
            "type": "string",
            "enum": [
                "jugular vein",
                "femoral vein",
                "carotid artery",
                "lateral ventricle",
                "third ventricle",
                "spinal cord (intrathecal)",
                "cisterna magna",
                "peritoneal cavity",
                "other"
            ]
        },
        "catheterType": {
            "title": "Catheter type",
            "type": "string",
            "format": "text"
        },
        "material": {
            "title": "Material",
            "type": "string",
            "format": "text"
        },
        "purpose": {
            "title": "Purpose",
            "type": "string",
            "enum": ["infusion", "sampling", "pressure monitoring", "drug delivery", "other"]
        },
        "fixationMethod": {
            "title": "Fixation method",
            "type": "string",
            "enum": ["sutures", "dental cement", "epoxy", "tissue glue", "tunneled subcutaneously", "other"]
        },
        "externalPort": {
            "title": "External port",
            "type": "string",
            "enum": ["head-mounted", "back-mounted", "tail-mounted", "subcutaneous", "none"]
        },
        "catheterId": {
            "title": "Catheter ID",
            "type": "string",
            "format": "text"
        }
    },
    "required": ["targetSite"]
}
```

*Target site* is a **required** field.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "targetSite": "jugular vein",
    "catheterType": "PE-10",
    "material": "PE (polyethylene)",
    "purpose": "infusion",
    "fixationMethod": "sutures",
    "externalPort": "head-mounted",
    "catheterId": "CAT-001"
}
```

## Cervical dislocation
```
{
    "type": "object",
    "title": "Cervical dislocation",
    "properties": {
        "dislocationMethod": {
            "title": "Method of dislocation",
            "type": "string",
            "enum": [
                "Manual",
                "Mechanical device",
                "Scissor method",
                "Other"
            ]
        },
        "anestheticAgent": {
            "title": "Anesthetic agent (if used)",
            "type": "string",
            "format": "text"
        },
        "confirmationOfDeath": {
            "title": "Confirmation of death",
            "type": "array",
            "items": {
                "type": "string",
                "enum": [
                    "Absence of heartbeat",
                    "Absence of breathing",
                    "Absence of reflexes",
                    "Fixed dilated pupils",
                    "Loss of corneal reflex",
                    "Other"
                ]
            },
            "uniqueItems": true,
            "minItems": 0,
            "format": "checkbox"
        },
        "complications": {
            "title": "Complications",
            "type": "string",
            "format": "textarea"
        }
    },
    "required": ["dislocationMethod", "confirmationOfDeath"]
}
```

*Method of dislocation* is a **required** field.
*Confirmation of death* is a **required** field.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "dislocationMethod": "Manual",
    "anestheticAgent": "CO₂",
    "confirmationOfDeath": ["Absence of heartbeat", "Absence of breathing", "Fixed dilated pupils"],
    "complications": "None"
}
```

## CO₂ chamber euthanasia
```
{
    "type": "object",
    "title": "CO₂ chamber euthanasia",
    "properties": {
        "co2Concentration": {
            "title": "CO₂ concentration (%)",
            "type": "number",
            "minimum": 0,
            "default": 30,
            "maximum": 100
        },
        "flowRate": {
            "title": "CO₂ flow rate (L/min)",
            "type": "number",
            "minimum": 0
        },
        "gradualIntroduction": {
            "title": "Gradual CO₂ introduction",
            "type": "boolean",
            "format": "checkbox"
        },
        "prefillingMethod": {
            "title": "Chamber prefilling",
            "type": "string",
            "enum": [
                "Not prefilled",
                "Partially prefilled",
                "Fully prefilled",
                "Other"
            ]
        },
        "exposureDuration": {
            "title": "Exposure duration (minutes)",
            "type": "number",
            "minimum": 0,
            "default": 5
        },
        "timeToUnconsciousness": {
            "title": "Time to unconsciousness (seconds)",
            "type": "number",
            "minimum": 0
        },
        "confirmationOfDeath": {
            "title": "Confirmation of death",
            "type": "array",
            "items": {
                "type": "string",
                "enum": [
                    "Absence of heartbeat",
                    "Absence of breathing",
                    "Absence of reflexes",
                    "Fixed dilated pupils",
                    "Loss of corneal reflex",
                    "Continued CO₂ exposure",
                    "Other"
                ]
            },
            "uniqueItems": true,
            "minItems": 0,
            "format": "checkbox"
        },
        "chamberVolume": {
            "title": "Chamber volume (L)",
            "type": "number",
            "minimum": 0
        }
    },
    "required": ["co2Concentration", "exposureDuration", "confirmationOfDeath"]
}
```

*CO₂ concentration* is a **required** field - **default** value set is `30`.
*Exposure duration* is a **required** field - **default** value set is `5`.
*Confirmation of death* is a **required** field.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "co2Concentration": 70,
    "flowRate": 2.5,
    "gradualIntroduction": true,
    "prefillingMethod": "Not prefilled",
    "exposureDuration": 10,
    "timeToUnconsciousness": 45,
    "confirmationOfDeath": ["Absence of heartbeat", "Absence of breathing", "Fixed dilated pupils"],
    "chamberVolume": 5.0
}
```

## Cranial window
```
{
    "type": "object",
    "title": "Cranial window",
    "properties": {
        "windowType": {
            "title": "Window type",
            "type": "string",
            "enum": [
                "Glass coverslip",
                "Glass window",
                "GRIN lens window",
                "Reinforced window",
                "Other"
            ]
        },
        "windowMaterial": {
            "title": "Window material",
            "type": "string",
            "enum": [
                "Glass",
                "Quartz",
                "Sapphire",
                "GRIN lens",
                "Other"
            ]
        },
        "windowSize": {
            "title": "Window size (mm)",
            "type": "string",
            "format": "text"
        },
        "windowShape": {
            "title": "Window shape",
            "type": "string",
            "enum": [
                "Circular",
                "Square",
                "Rectangular",
                "Oval",
                "Other"
            ]
        },
        "thickness": {
            "title": "Thickness (mm)",
            "type": "number",
            "minimum": 0
        },
        "sealingMethod": {
            "title": "Sealing method",
            "type": "string",
            "enum": [
                "Dental acrylic",
                "Cerebond",
                "Silicone sealant",
                "Vaseline",
                "Other"
            ]
        },
        "reinforcement": {
            "title": "Reinforcement used",
            "type": "boolean"
        },
        "durability": {
            "title": "Expected durability (days)",
            "type": "number",
            "minimum": 0
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "windowType": "Glass coverslip",
    "windowMaterial": "Glass",
    "windowSize": "3mm diameter",
    "windowShape": "Circular",
    "thickness": 0.15,
    "sealingMethod": "Dental acrylic",
    "reinforcement": false,
    "durability": 30
}
```

## Craniectomy
```
{
    "type": "object",
    "title": "Craniectomy",
    "properties": {
        "surgicalMethod": {
            "title": "Surgical method",
            "type": "string",
            "format": "text"
        },
        "shape": {
            "title": "Shape of craniectomy",
            "type": "string",
            "format": "text"
        },
        "dimensions": {
            "title": "Dimensions of craniectomy",
            "type": "string",
            "format": "text"
        },
        "orientation": {
            "title": "Orientation of craniectomy",
            "type": "string",
            "format": "text"
        },
        "fatalOutcome": {
            "title": "Fatal outcome",
            "type": "boolean",
            "format": "checkbox"
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "surgicalMethod": "surgical drill",
    "shape": "circular",
    "dimensions": "1.0 mm diameter",
    "orientation": "anterior-posterior",
    "fatalOutcome": false
}
```

## Craniotomy
```
{
    "type": "object",
    "title": "Craniotomy",
    "properties": {
        "boneFlapSize": {
            "title": "Bone flap size (mm)",
            "type": "string",
            "format": "text"
        },
        "boneFlapShape": {
            "title": "Bone flap shape",
            "type": "string",
            "enum": [
                "Circular",
                "Square",
                "Rectangular",
                "Oval",
                "Other"
            ]
        },
        "cuttingMethod": {
            "title": "Cutting method",
            "type": "string",
            "enum": [
                "High-speed drill",
                "Micro-saw",
                "Cranial perforator",
                "Other"
            ]
        },
        "boneFlapReplaced": {
            "title": "Bone flap replaced",
            "type": "boolean"
        },
        "fixationMethod": {
            "title": "Fixation method",
            "type": "string",
            "enum": [
                "Plates and screws",
                "Wire fixation",
                "Dental acrylic",
                "Tissue glue",
                "None",
                "Other"
            ]
        },
        "duraHandling": {
            "title": "Dura handling",
            "type": "string",
            "enum": [
                "Intact",
                "Incised",
                "Removed",
                "Patched",
                "Other"
            ]
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "boneFlapSize": "4mm × 4mm",
    "boneFlapShape": "Square",
    "cuttingMethod": "High-speed drill",
    "boneFlapReplaced": true,
    "fixationMethod": "Plates and screws",
    "duraHandling": "Incised"
}
```

## Cryosectioning
```
{
    "type": "object",
    "title": "Cryosectioning",
    "properties": {
        "sectioningTemperature": {
            "title": "Sectioning temperature (°C)",
            "type": "number"
        },
        "sectionThickness": {
            "title": "Section thickness (μm)",
            "type": "number",
            "minimum": 0
        },
        "cuttingSpeed": {
            "title": "Cutting speed",
            "type": "string",
            "enum": [
                "Slow",
                "Medium",
                "Fast",
                "Other"
            ]
        },
        "specimenEmbedding": {
            "title": "Specimen embedding medium",
            "type": "string",
            "enum": [
                "OCT compound",
                "Gelatin",
                "Agarose",
                "None",
                "Other"
            ]
        },
        "sectionOrientation": {
            "title": "Section orientation",
            "type": "string",
            "enum": [
                "Coronal",
                "Sagittal",
                "Horizontal",
                "Oblique",
                "Other"
            ]
        },
        "collectionMethod": {
            "title": "Collection method",
            "type": "string",
            "enum": [
                "Direct slide mounting",
                "Floatation bath",
                "Tape transfer",
                "Other"
            ]
        },
        "storageMethod": {
            "title": "Storage method",
            "type": "string",
            "enum": [
                "Room temperature",
            "Refrigerated",
            "Frozen",
            "Other"
            ]
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "sectioningTemperature": -20,
    "sectionThickness": 30,
    "cuttingSpeed": "Medium",
    "specimenEmbedding": "OCT compound",
    "sectionOrientation": "Coronal",
    "collectionMethod": "Direct slide mounting",
    "storageMethod": "Frozen"
}
```

## Decapitation
```
{
    "type": "object",
    "title": "Decapitation",
    "properties": {
        "method": {
            "title": "Method",
            "type": "string",
            "enum": [
                "Guillotine",
                "Scissors",
                "Blade",
                "Other"
            ]
        },
        "anestheticAgent": {
            "title": "Anesthetic agent (if used)",
            "type": "string",
            "format": "text"
        },
        "confirmationOfDeath": {
            "title": "Confirmation of death",
            "type": "array",
            "items": {
                "type": "string",
                "enum": [
                    "Absence of heartbeat",
                    "Absence of breathing",
                    "Absence of reflexes",
                    "Fixed dilated pupils",
                    "Loss of corneal reflex",
                    "Other"
                ]
            },
            "uniqueItems": true,
            "minItems": 0,
            "format": "checkbox"
        },
        "complications": {
            "title": "Complications",
            "type": "string",
            "format": "textarea"
        }
    },
    "required": ["method", "confirmationOfDeath"]
}
```

*Method* is a **required** field.
*Confirmation of death* is a **required** field.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "method": "Guillotine",
    "anestheticAgent": "Isoflurane",
    "confirmationOfDeath": ["Absence of heartbeat", "Absence of breathing", "Fixed dilated pupils"],
    "complications": "None"
}
```

## ECG implant
```
{
    "type": "object",
    "title": "ECG implant",
    "properties": {
        "electrodeType": {
            "title": "Electrode type",
            "type": "string",
            "enum": [
                "Subcutaneous needle",
                "Surface electrode",
                "Telemetry electrode",
                "Implantable electrode",
                "Other"
            ]
        },
        "electrodePlacement": {
            "title": "Electrode placement",
            "type": "string",
            "enum": [
                "Lead I (bipolar)",
                "Lead II (bipolar)",
                "Lead III (bipolar)",
                "Precordial leads",
                "Custom configuration",
                "Other"
            ]
        },
        "electrodeMaterial": {
            "title": "Electrode material",
            "type": "string",
            "enum": [
                "Stainless steel",
                "Platinum",
                "Gold",
                "Silver",
                "Ag/AgCl",
                "Other"
            ]
        },
        "implantationMethod": {
            "title": "Implantation method",
            "type": "string",
            "enum": [
                "Surgical implantation",
                "Subcutaneous placement",
                "Telemetry device",
                "Other"
            ]
        },
        "telemetryDevice": {
            "title": "Telemetry device",
            "type": "boolean"
        },
        "deviceModel": {
            "title": "Device model",
            "type": "string",
            "format": "text"
        },
        "recordingDuration": {
            "title": "Recording duration (days)",
            "type": "number",
            "minimum": 0
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "electrodeType": "Subcutaneous needle",
    "electrodePlacement": "Lead II (bipolar)",
    "electrodeMaterial": "Stainless steel",
    "implantationMethod": "Subcutaneous placement",
    "telemetryDevice": false,
    "deviceModel": "ECG-100",
    "recordingDuration": 7
}
```

## EEG implant
```
{
    "type": "object",
    "title": "EEG implant",
    "properties": {
        "electrodeType": {
            "title": "Electrode type",
            "type": "string",
            "enum": [
                "Surface electrode",
                "Depth electrode",
                "Screw electrode",
                "Microelectrode",
                "Other"
            ]
        },
        "electrodeCount": {
            "title": "Number of electrodes",
            "type": "integer",
            "minimum": 1
        },
        "electrodeMaterial": {
            "title": "Electrode material",
            "type": "string",
            "enum": [
                "Stainless steel",
                "Platinum",
                "Gold",
                "Tungsten",
                "Other"
            ]
        },
        "placementCoordinates": {
            "title": "Placement coordinates",
            "type": "string",
            "format": "text"
        },
        "referenceElectrode": {
            "title": "Reference electrode location",
            "type": "string",
            "enum": [
                "Cerebellum",
                "Frontal bone",
                "Nasal bone",
                "Occipital bone",
                "Other"
            ]
        },
        "groundElectrode": {
            "title": "Ground electrode location",
            "type": "string",
            "enum": [
                "Cerebellum",
                "Frontal bone",
                "Nasal bone",
                "Occipital bone",
                "Other"
            ]
        },
        "recordingSystem": {
            "title": "Recording system",
            "type": "string",
            "format": "text"
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "electrodeType": "Screw electrode",
    "electrodeCount": 4,
    "electrodeMaterial": "Stainless steel",
    "placementCoordinates": "AP: -2.0, ML: ±2.0, DV: -1.0",
    "referenceElectrode": "Cerebellum",
    "groundElectrode": "Cerebellum",
    "recordingSystem": "Plexon"
}
```

## EMG implant
```
{
    "type": "object",
    "title": "EMG implant",
    "properties": {
        "electrodeType": {
            "title": "Electrode type",
            "type": "string",
            "enum": [
                "Fine wire electrode",
                "Needle electrode",
                "Surface electrode",
                "Patch electrode",
                "Other"
            ]
        },
        "targetMuscle": {
            "title": "Target muscle",
            "type": "string",
            "format": "text"
        },
        "electrodeMaterial": {
            "title": "Electrode material",
            "type": "string",
            "enum": [
                "Stainless steel",
                "Platinum",
                "Gold",
                "Tungsten",
                "Other"
            ]
        },
        "wireDiameter": {
            "title": "Wire diameter (μm)",
            "type": "number",
            "minimum": 0
        },
        "placementMethod": {
            "title": "Placement method",
            "type": "string",
            "enum": [
                "Percutaneous insertion",
                "Surgical implantation",
                "Surface attachment",
                "Other"
            ]
        },
        "recordingSystem": {
            "title": "Recording system",
            "type": "string",
            "format": "text"
        },
        "signalType": {
            "title": "Signal type",
            "type": "string",
            "enum": [
                "Bipolar",
                "Unipolar",
                "Differential",
                "Other"
            ]
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "electrodeType": "Fine wire electrode",
    "targetMuscle": "Gastrocnemius",
    "electrodeMaterial": "Stainless steel",
    "wireDiameter": 50,
    "placementMethod": "Percutaneous insertion",
    "recordingSystem": "Intan",
    "signalType": "Bipolar"
}
```

## Generic implant
```
{
    "type": "object",
    "title": "Generic implant",
    "properties": {
        "implantType": {
            "title": "Implant type",
            "type": "string",
            "format": "text"
        },
        "implantMaterial": {
            "title": "Implant material",
            "type": "string",
            "format": "text"
        },
        "implantDimensions": {
            "title": "Implant dimensions",
            "type": "string",
            "format": "text"
        },
        "implantationSite": {
            "title": "Implantation site",
            "type": "string",
            "format": "text"
        },
        "fixationMethod": {
            "title": "Fixation method",
            "type": "string",
            "enum": [
                "Sutures",
                "Dental cement",
                "Epoxy",
                "Tissue glue",
                "Screws",
                "Other"
            ]
        },
        "biocompatibility": {
            "title": "Biocompatibility",
            "type": "string",
            "enum": [
                "Biocompatible",
                "Non-biocompatible",
                "Unknown",
                "Other"
            ]
        },
        "function": {
            "title": "Implant function",
            "type": "string",
            "format": "text"
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "implantType": "Custom electrode array",
    "implantMaterial": "Silicone and platinum",
    "implantDimensions": "2mm × 1mm × 0.5mm",
    "implantationSite": "Motor cortex",
    "fixationMethod": "Dental cement",
    "biocompatibility": "Biocompatible",
    "function": "Neural recording"
}
```

## GRIN lens implant
```
{
    "type": "object",
    "title": "GRIN lens implant",
    "properties": {
        "lensDiameter": {
            "title": "Lens diameter (mm)",
            "type": "number",
            "minimum": 0
        },
        "lensLength": {
            "title": "Lens length (mm)",
            "type": "number",
            "minimum": 0
        },
        "numericalAperture": {
            "title": "Numerical aperture",
            "type": "number",
            "minimum": 0
        },
        "workingDistance": {
            "title": "Working distance (mm)",
            "type": "number",
            "minimum": 0"
        },
        "implantationDepth": {
            "title": "Implantation depth (mm)",
            "type": "number",
            "minimum": 0"
        },
        "targetRegion": {
            "title": "Target region",
            "type": "string",
            "format": "text"
        },
        "fixationMethod": {
            "title": "Fixation method",
            "type": "string",
            "enum": [
                "Dental cement",
                "Screws",
                "Tissue glue",
                "Other"
            ]
        },
        "protectiveCover": {
            "title": "Protective cover used",
            "type": "boolean"
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "lensDiameter": 0.5,
    "lensLength": 4.0,
    "numericalAperture": 0.5,
    "workingDistance": 0.25,
    "implantationDepth": 1.5,
    "targetRegion": "Visual cortex",
    "fixationMethod": "Dental cement",
    "protectiveCover": true
}
```

## Headcap
```
{
    "type": "object",
    "title": "Headcap",
    "properties": {
        "headcapMaterial": {
            "title": "Headcap material",
            "type": "string",
            "enum": [
                "Dental acrylic",
                "Light-cured acrylic",
                "Polymethyl methacrylate (PMMA)",
                "Other"
            ]
        },
        "attachmentMethod": {
            "title": "Attachment method",
            "type": "string",
            "enum": [
                "Screws",
                "Bone cement",
                "Tissue glue",
                "Other"
            ]
        },
        "screwCount": {
            "title": "Number of screws",
            "type": "integer",
            "minimum": 0"
        },
        "screwType": {
            "title": "Screw type",
            "type": "string",
            "enum": [
                "Bone screw",
                "Jeweler's screw",
                "Micro screw",
                "Other"
            ]
        },
        "reinforcement": {
            "title": "Reinforcement used",
            "type": "boolean"
        },
        "reinforcementMaterial": {
            "title": "Reinforcement material",
            "type": "string",
            "enum": [
                "Mesh",
                "Wire",
                "Fibers",
                "Other"
            ]
        },
        "durability": {
            "title": "Expected durability (days)",
            "type": "number",
            "minimum": 0"
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "headcapMaterial": "Dental acrylic",
    "attachmentMethod": "Screws",
    "screwCount": 3,
    "screwType": "Bone screw",
    "reinforcement": true,
    "reinforcementMaterial": "Mesh",
    "durability": 60
}
```

## Head fixation
```
{
    "type": "object",
    "title": "Head fixation",
    "properties": {
        "fixationMethod": {
            "title": "Fixation method",
            "type": "string",
            "enum": [
                "Head plate",
                "Headpost",
                "Ear bars",
                "Nose clamp",
                "Other"
            ]
        },
        "plateType": {
            "title": "Plate type",
            "type": "string",
            "enum": [
                "Metal plate",
                "Plastic plate",
                "Custom design",
                "Other"
            ]
        },
        "plateDimensions": {
            "title": "Plate dimensions",
            "type": "string",
            "format": "text"
        },
        "attachmentMethod": {
            "title": "Attachment method",
            "type": "string",
            "enum": [
                "Screws",
                "Dental cement",
                "Tissue glue",
                "Other"
            ]
        },
        "positioning": {
            "title": "Positioning relative to bregma",
            "type": "string",
            "format": "text"
        },
        "angleAdjustment": {
            "title": "Angle adjustment",
            "type": "boolean"
        },
        "angleRange": {
            "title": "Angle adjustment range (degrees)",
            "type": "string",
            "format": "text"
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "fixationMethod": "Head plate",
    "plateType": "Metal plate",
    "plateDimensions": "10mm × 6mm × 1mm",
    "attachmentMethod": "Screws",
    "positioning": "Centered on lambda",
    "angleAdjustment": true,
    "angleRange": "±30 degrees"
}
```

## Headpost
```
{
    "type": "object",
    "title": "Headpost",
    "properties": {
        "postMaterial": {
            "title": "Post material",
            "type": "string",
            "enum": [
                "Stainless steel",
                "Titanium",
                "Aluminum",
                "Plastic",
                "Other"
            ]
        },
        "postDimensions": {
            "title": "Post dimensions",
            "type": "string",
            "format": "text"
        },
        "postShape": {
            "title": "Post shape",
            "type": "string",
            "enum": [
                "Cylindrical",
                "Rectangular",
                "L-shaped",
                "T-shaped",
                "Other"
            ]
        },
        "attachmentMethod": {
            "title": "Attachment method",
            "type": "string",
            "enum": [
                "Screws",
                "Dental cement",
                "Tissue glue",
                "Other"
            ]
        },
        "mountingSurface": {
            "title": "Mounting surface",
            "type": "string",
            "enum": [
                "Flat",
                "Angled",
                "Curved",
                "Other"
            ]
        },
        "threadSize": {
            "title": "Thread size",
            "type": "string",
            "format": "text"
        },
        "weight": {
            "title": "Weight (g)",
            "type": "number",
            "minimum": 0"
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "postMaterial": "Titanium",
    "postDimensions": "5mm height × 3mm diameter",
    "postShape": "Cylindrical",
    "attachmentMethod": "Screws",
    "mountingSurface": "Flat",
    "threadSize": "M2",
    "weight": 0.5
}
```

## Inhalant overdose
```
{
    "type": "object",
    "title": "Inhalant overdose",
    "properties": {
        "agent": {
            "title": "Inhalant agent",
            "type": "string",
            "enum": [
                "Isoflurane",
                "Sevoflurane",
                "Halothane",
                "Enflurane",
                "Other"
            ]
        },
        "concentration": {
            "title": "Concentration (%)",
            "type": "number",
            "minimum": 0"
        },
        "administrationMethod": {
            "title": "Administration method",
            "type": "string",
            "enum": [
                "Induction chamber",
                "Face mask",
                "Nose cone",
                "Other"
            ]
        },
        "flowRate": {
            "title": "Flow rate (L/min)",
            "type": "number",
            "minimum": 0"
        },
        "exposureDuration": {
            "title": "Exposure duration (minutes)",
            "type": "number",
            "minimum": 0"
        },
        "confirmationOfDeath": {
            "title": "Confirmation of death",
            "type": "array",
            "items": {
                "type": "string",
                "enum": [
                    "Absence of heartbeat",
                    "Absence of breathing",
                    "Absence of reflexes",
                    "Fixed dilated pupils",
                    "Loss of corneal reflex",
                    "Other"
                ]
            },
            "uniqueItems": true,
            "minItems": 0,
            "format": "checkbox"
        },
        "complications": {
            "title": "Complications",
            "type": "string",
            "format": "textarea"
        }
    },
    "required": ["agent", "confirmationOfDeath"]
}
```

*Inhalant agent* is a **required** field.
*Confirmation of death* is a **required** field.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "agent": "Isoflurane",
    "concentration": 5,
    "administrationMethod": "Induction chamber",
    "flowRate": 2.0,
    "exposureDuration": 10,
    "confirmationOfDeath": ["Absence of heartbeat", "Absence of breathing", "Fixed dilated pupils"],
    "complications": "None"
}
```

## Injection
```
{
    "type": "object",
    "title": "Injection",
    "properties": {
        "injectionVolume": {
            "title": "Injection volume (mL)",
            "type": "number",
            "minimum": 0"
        },
        "injectionRate": {
            "title": "Injection rate (mL/s)",
            "type": "number",
            "minimum": 0"
        },
        "injectionMethod": {
            "title": "Injection Method",
            "type": "string",
            "enum": [
                "Intracerebroventricular (ICV)",
                "Intramuscular (IM)",
                "Intravenous (IV)",
                "Intradermal (ID)",
                "Subcutaneous (SC)",
                "Intracardiac (IC)",
                "Intraperitoneal (IP)",
                "Intrathecal (IT)",
                "Epidural",
                "Retro-orbital (RO)",
                "Intranasal (IN)",
                "Intra-articular",
                "Intravitreal",
                "Intralesional"
            ]
        },
        "concentration": {
            "title": "Concentration of solution (mg/mL)",
            "type": "number",
            "minimum": 0"
        },
        "injectionProfile": {
            "title": "Injection profile",
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
            ]
        },
        "injectionSide": {
            "title": "Injection side (brain hemisphere or body side)",
            "type": "string",
            "enum": ["Left", "Right", "Midline", "Unknown"]
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "injectionVolume": 0.1,
    "injectionRate": 0.01,
    "injectionMethod": "Intraperitoneal (IP)",
    "concentration": 1.0,
    "injectionProfile": "Bolus Injection",
    "injectionSide": "Midline"
}
```

## Nerve cuff implant
```
{
    "type": "object",
    "title": "Nerve cuff implant",
    "properties": {
        "nerveTarget": {
            "title": "Target nerve",
            "type": "string",
            "format": "text"
        },
        "cuffType": {
            "title": "Cuff type",
            "type": "string",
            "enum": [
                "Cylindrical cuff",
                "Flat cuff",
                "Spiral cuff",
                "Split cuff",
                "Other"
            ]
        },
        "cuffMaterial": {
            "title": "Cuff material",
            "type": "string",
            "enum": [
                "Silicone",
                "Polyurethane",
                "PTFE",
                "Other"
            ]
        },
        "cuffDiameter": {
            "title": "Cuff inner diameter (mm)",
            "type": "number",
            "minimum": 0"
        },
        "cuffLength": {
            "title": "Cuff length (mm)",
            "type": "number",
            "minimum": 0"
        },
        "electrodeConfiguration": {
            "title": "Electrode configuration",
            "type": "string",
            "enum": [
                "Bipolar",
                "Tripolar",
                "Multipolar",
                "Monopolar",
                "Other"
            ]
        },
        "electrodeMaterial": {
            "title": "Electrode material",
            "type": "string",
            "enum": [
                "Platinum",
                "Iridium",
                "Stainless steel",
                "Other"
            ]
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "nerveTarget": "Sciatic nerve",
    "cuffType": "Cylindrical cuff",
    "cuffMaterial": "Silicone",
    "cuffDiameter": 1.0,
    "cuffLength": 3.0,
    "electrodeConfiguration": "Bipolar",
    "electrodeMaterial": "Platinum"
}
```

## Odor stimulation
```
{
    "type": "object",
    "title": "Odor stimulation",
    "properties": {
        "odorant": {
            "title": "Odorant",
            "type": "string",
            "format": "text"
        },
        "odorantType": {
            "title": "Odorant type",
            "type": "string",
            "enum": [
                "Pure chemical",
                "Natural extract",
                "Essential oil",
                "Synthetic odor",
                "Other"
            ]
        },
        "concentration": {
            "title": "Concentration",
            "type": "string",
            "format": "text"
        },
        "diluent": {
            "title": "Diluent",
            "type": "string",
            "enum": [
                "Mineral oil",
                "Water",
                "Ethanol",
                "Air",
                "Other"
            ]
        },
        "deliveryMethod": {
            "title": "Delivery method",
            "type": "string",
            "enum": [
                "Olfactometer",
                "Direct application",
                "Airflow",
                "Nebulizer",
                "Other"
            ]
        },
        "duration": {
            "title": "Stimulation duration (seconds)",
            "type": "number",
            "minimum": 0"
        },
        "flowRate": {
            "title": "Flow rate (L/min)",
            "type": "number",
            "minimum": 0"
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "odorant": "Isoamyl acetate",
    "odorantType": "Pure chemical",
    "concentration": "1% v/v",
    "diluent": "Mineral oil",
    "deliveryMethod": "Olfactometer",
    "duration": 2,
    "flowRate": 1.0
}
```

## Perfusion fixation
```
{
    "type": "object",
    "title": "Perfusion fixation",
    "properties": {
        "fixative": {
            "title": "Primary fixative",
            "type": "string",
            "enum": [
                "Paraformaldehyde (PFA)",
                "Formalin",
                "Glutaraldehyde",
                "Paraformaldehyde + Glutaraldehyde",
                "Other"
            ]
        },
        "primaryConcentration": {
            "title": "Primary fixative concentration (%)",
            "type": "number",
            "minimum": 0"
        },
        "secondaryFixative": {
            "title": "Secondary fixative",
            "type": "string",
            "enum": [
                "None",
                "Glutaraldehyde",
                "Paraformaldehyde",
                "Other"
            ]
        },
        "secondaryConcentration": {
            "title": "Secondary fixative concentration (%)",
            "type": "number",
            "minimum": 0"
        },
        "buffer": {
            "title": "Buffer solution",
            "type": "string",
            "enum": [
                "Phosphate buffer (PBS)",
                "Cacodylate buffer",
                "HEPES buffer",
                "Other"
            ]
        },
        "pH": {
            "title": "pH",
            "type": "number"
        },
        "perfusionPressure": {
            "title": "Perfusion pressure (mmHg)",
            "type": "number",
            "minimum": 0"
        },
        "perfusionVolume": {
            "title": "Total perfusion volume (mL)",
            "type": "number",
            "minimum": 0"
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "fixative": "Paraformaldehyde (PFA)",
    "primaryConcentration": 4,
    "secondaryFixative": "None",
    "secondaryConcentration": 0,
    "buffer": "Phosphate buffer (PBS)",
    "pH": 7.4,
    "perfusionPressure": 120,
    "perfusionVolume": 50
}
```

## Prism implant
```
{
    "type": "object",
    "title": "Prism implant",
    "properties": {
        "prismType": {
            "title": "Prism type",
            "type": "string",
            "enum": [
                "Right angle prism",
                "Retroreflector prism",
                "Custom prism",
                "Other"
            ]
        },
        "prismMaterial": {
            "title": "Prism material",
            "type": "string",
            "enum": [
                "Glass",
                "BK7 glass",
                "Fused silica",
                "Acrylic",
                "Other"
            ]
        },
        "prismDimensions": {
            "title": "Prism dimensions",
            "type": "string",
            "format": "text"
        },
        "implantationDepth": {
            "title": "Implantation depth (mm)",
            "type": "number",
            "minimum": 0"
        },
        "targetRegion": {
            "title": "Target region",
            "type": "string",
            "format": "text"
        },
        "fixationMethod": {
            "title": "Fixation method",
            "type": "string",
            "enum": [
                "Dental cement",
                "Screws",
                "Tissue glue",
                "Other"
            ]
        },
        "protectiveCover": {
            "title": "Protective cover used",
            "type": "boolean"
        },
        "angleAdjustment": {
            "title": "Angle adjustment capability",
            "type": "boolean"
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "prismType": "Right angle prism",
    "prismMaterial": "BK7 glass",
    "prismDimensions": "1mm × 1mm × 1mm",
    "implantationDepth": 0.5,
    "targetRegion": "Visual cortex",
    "fixationMethod": "Dental cement",
    "protectiveCover": true,
    "angleAdjustment": false
}
```

## Reference electrode implant
```
{
    "type": "object",
    "title": "Reference electrode implant",
    "properties": {
        "electrodeType": {
            "title": "Electrode type",
            "type": "string",
            "enum": [
                "Screw electrode",
                "Wire electrode",
                "Surface electrode",
                "Ag/AgCl electrode",
                "Other"
            ]
        },
        "electrodeMaterial": {
            "title": "Electrode material",
            "type": "string",
            "enum": [
                "Stainless steel",
                "Silver",
                "Platinum",
                "Ag/AgCl",
                "Other"
            ]
        },
        "implantationSite": {
            "title": "Implantation site",
            "type": "string",
            "enum": [
                "Cerebellum",
                "Frontal bone",
                "Nasal bone",
                "Occipital bone",
                "Muscle",
                "Other"
            ]
        },
        "placementMethod": {
            "title": "Placement method",
            "type": "string",
            "enum": [
                "Screw insertion",
                "Subcutaneous placement",
                "Surface attachment",
                "Other"
            ]
        },
        "referenceType": {
            "title": "Reference type",
            "type": "string",
            "enum": [
                "Ground",
                "Reference",
                "Ground and reference",
                "Other"
            ]
        },
        "impedance": {
            "title": "Impedance (kΩ)",
            "type": "number",
            "minimum": 0"
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "electrodeType": "Screw electrode",
    "electrodeMaterial": "Stainless steel",
    "implantationSite": "Cerebellum",
    "placementMethod": "Screw insertion",
    "referenceType": "Reference",
    "impedance": 10
}
```

## Tactile stimulation
```
{
    "type": "object",
    "title": "Tactile stimulation",
    "properties": {
        "stimulusType": {
            "title": "Stimulus type",
            "type": "string",
            "enum": [
                "Air puff",
                "Brush stroke",
                "Vibration",
                "Pressure",
                "Pinprick",
                "Other"
            ]
        },
        "stimulusLocation": {
            "title": "Stimulus location",
            "type": "string",
            "format": "text"
        },
        "intensity": {
            "title": "Intensity",
            "type": "string",
            "format": "text"
        },
        "frequency": {
            "title": "Frequency (Hz)",
            "type": "number",
            "minimum": 0"
        },
        "duration": {
            "title": "Stimulation duration (ms)",
            "type": "number",
            "minimum": 0"
        },
        "stimulusDevice": {
            "title": "Stimulus device",
            "type": "string",
            "format": "text"
        },
        "stimulusDirection": {
            "title": "Stimulus direction",
            "type": "string",
            "enum": [
                "Dorsal-ventral",
                "Ventral-dorsal",
                "Medial-lateral",
                "Lateral-medial",
                "Other"
            ]
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "stimulusType": "Air puff",
    "stimulusLocation": "Right whisker pad",
    "intensity": "Medium pressure",
    "frequency": 1,
    "duration": 100,
    "stimulusDevice": "Picospritzer",
    "stimulusDirection": "Dorsal-ventral"
}
```

## Temperature sensor implant
```
{
    "type": "object",
    "title": "Temperature sensor implant",
    "properties": {
        "sensorType": {
            "title": "Sensor type",
            "type": "string",
            "enum": [
                "Thermistor",
                "Thermocouple",
                "RTD",
                "Fiber optic temperature sensor",
                "Other"
            ]
        },
        "sensorModel": {
            "title": "Sensor model",
            "type": "string",
            "format": "text"
        },
        "implantationSite": {
            "title": "Implantation site",
            "type": "string",
            "enum": [
                "Brain",
                "Muscle",
                "Subcutaneous",
                "Peritoneal cavity",
                "Other"
            ]
        },
        "placementMethod": {
            "title": "Placement method",
            "type": "string",
            "enum": [
                "Surgical implantation",
                "Subcutaneous placement",
                "Intramuscular injection",
                "Other"
            ]
        },
        "temperatureRange": {
            "title": "Temperature range (°C)",
            "type": "string",
            "format": "text"
        },
        "accuracy": {
            "title": "Accuracy (°C)",
            "type": "number"
        },
        "recordingDuration": {
            "title": "Recording duration (days)",
            "type": "number",
            "minimum": 0"
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "sensorType": "Thermistor",
    "sensorModel": "NTC 10K",
    "implantationSite": "Brain",
    "placementMethod": "Surgical implantation",
    "temperatureRange": "35-45°C",
    "accuracy": 0.1,
    "recordingDuration": 30
}
```

## Tissue clearing
```
{
    "type": "object",
    "title": "Tissue clearing",
    "properties": {
        "clearingMethod": {
            "title": "Clearing method",
            "type": "string",
            "enum": [
                "CLARITY",
                "iDISCO",
                "CUBIC",
                "SeeDB",
                "Scale",
                "3DISCO",
                "Other"
            ]
        },
        "tissueType": {
            "title": "Tissue type",
            "type": "string",
            "format": "text"
        },
        "tissueThickness": {
            "title": "Tissue thickness (mm)",
            "type": "number",
            "minimum": 0"
        },
        "clearingDuration": {
            "title": "Clearing duration (days)",
            "type": "number",
            "minimum": 0"
        },
        "clearingTemperature": {
            "title": "Clearing temperature (°C)",
            "type": "number"
        },
        "indexMatchingSolution": {
            "title": "Index matching solution",
            "type": "string",
            "enum": [
                "RIMS",
                "ECi",
                "BABB",
                "DBE",
                "Other"
            ]
        },
        "finalTransparency": {
            "title": "Final transparency assessment",
            "type": "string",
            "enum": [
                "Fully transparent",
                "Partially transparent",
                "Opaque",
                "Other"
            ]
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "clearingMethod": "iDISCO",
    "tissueType": "Mouse brain",
    "tissueThickness": 10,
    "clearingDuration": 7,
    "clearingTemperature": 37,
    "indexMatchingSolution": "DBE",
    "finalTransparency": "Fully transparent"
}
```

## Vibratome sectioning
```
{
    "type": "object",
    "title": "Vibratome sectioning",
    "properties": {
        "sectionThickness": {
            "title": "Section thickness (μm)",
            "type": "number",
            "minimum": 0"
        },
        "sectionSpeed": {
            "title": "Section speed (mm/s)",
            "type": "number",
            "minimum": 0"
        },
        "vibrationAmplitude": {
            "title": "Vibration amplitude",
            "type": "string",
            "enum": [
                "Low",
                "Medium",
                "High",
                "Other"
            ]
        },
        "bladeAngle": {
            "title": "Blade angle (degrees)",
            "type": "number",
            "minimum": 0",
            "maximum": 90"
        },
        "cuttingSolution": {
            "title": "Cutting solution",
            "type": "string",
            "enum": [
                "Ice-cold ACSF",
                "Sucrose solution",
                "PBS",
                "Other"
            ]
        },
        "sectionOrientation": {
            "title": "Section orientation",
            "type": "string",
            "enum": [
                "Coronal",
                "Sagittal",
                "Horizontal",
                "Oblique",
                "Other"
            ]
        },
        "temperature": {
            "title": "Temperature (°C)",
            "type": "number"
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "sectionThickness": 400,
    "sectionSpeed": 0.05,
    "vibrationAmplitude": "Medium",
    "bladeAngle": 15,
    "cuttingSolution": "Ice-cold ACSF",
    "sectionOrientation": "Coronal",
    "temperature": 4
}
```

## Visual stimulation
```
{
    "type": "object",
    "title": "Visual stimulation",
    "properties": {
        "stimulusType": {
            "title": "Stimulus type",
            "type": "string",
            "enum": [
                "Flashing light",
                "Moving bar",
                "Grating",
                "Natural scene",
                "Full-field flash",
                "Patterned light",
                "Other"
            ]
        },
        "stimulusPattern": {
            "title": "Stimulus pattern",
            "type": "string",
            "format": "text"
        },
        "spatialFrequency": {
            "title": "Spatial frequency (cycles/degree)",
            "type": "number",
            "minimum": 0"
        },
        "temporalFrequency": {
            "title": "Temporal frequency (Hz)",
            "type": "number",
            "minimum": 0"
        },
        "contrast": {
            "title": "Contrast (%)",
            "type": "number",
            "minimum": 0,
            "maximum": 100"
        },
        "duration": {
            "title": "Stimulation duration (ms)",
            "type": "number",
            "minimum": 0"
        },
        "visualField": {
            "title": "Visual field stimulated",
            "type": "string",
            "enum": [
                "Central",
                "Peripheral",
                "Full field",
                "Upper visual field",
                "Lower visual field",
                "Other"
            ]
        },
        "stimulusDevice": {
            "title": "Stimulus device",
            "type": "string",
            "enum": [
                "Monitor",
                "LED array",
                "Projector",
                "OLED screen",
                "Other"
            ]
        }
    },
    "required": []
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "stimulusType": "Grating",
    "stimulusPattern": "Sinusoidal grating",
    "spatialFrequency": 0.1,
    "temporalFrequency": 2,
    "contrast": 80,
    "duration": 1000,
    "visualField": "Full field",
    "stimulusDevice": "Monitor"
}
```

## Virus injection
```
{
    "type": "object",
    "title": "Virus injection",
    "properties": {
        "injectionVolume": {
            "title": "Injection volume (nL)",
            "type": "number",
            "minimum": 0,
            "default": "0"
        },
        "injectionRate": {
            "title": "Injection Rate (nL/s)",
            "type": "number"
        },
        "injectionSchema": {
            "title": "Injection schema",
            "type": "string",
            "enum": ["Gradual","Pulses","unknown"]
        }
    },
    "required": ["injectionVolume"]
}
```

*Injection volume* is a **required** field - **default** value set is `0`.

### Example of JSON according to this schema
{: .no_toc}
```
{
    "injectionVolume": 100,
    "injectionRate": 50,
    "injectionSchema": "Gradual"
}
```
