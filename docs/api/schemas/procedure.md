---
layout: default
title: Procedure
parent: Schemas
grand_parent: API
nav_order: 5
---

# Procedure schemas
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Anesthesia
```
{
    "type": "object",
    "title": "Anesthesia",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "anestheticAgent": {
            "title": "Anesthetic agent",
            "brief": "agent",
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
            ],
            "options": {
                "infoText": "Primary anesthetic agent used."
            }
        },
        "route": {
            "title": "Administration route",
            "brief": "route",
            "type": "string",
            "enum": [
                "Inhalation",
                "Intraperitoneal (IP)",
                "Intravenous (IV)",
                "Subcutaneous (SC)",
                "Intramuscular (IM)",
                "Oral",
                "Other"
            ],
            "options": {
                "infoText": "Route of anesthetic administration."
            }
        },
        "dosage": {
            "title": "Dosage",
            "brief": "dosage",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., '2% in 10% oxygen', '100 mg/kg'"
                },
                "infoText": "Dosage of the anesthetic agent (e.g., '2% in 10% oxygen', '100 mg/kg')."
            }
        },
        "depth": {
            "title": "Anesthetic depth",
            "brief": "depth",
            "type": "string",
            "enum": [
                "Light sedation",
                "Moderate sedation",
                "Deep sedation",
                "Surgical plane",
                "Other"
            ],
            "options": {
                "infoText": "Select the anesthetic depth achieved:\n\u2022 Light sedation: Minimal depression, animal is calm but responsive.\n\u2022 Moderate sedation: Reduced awareness, responds to strong stimuli.\n\u2022 Deep sedation: Unresponsive, diminished reflexes, not surgical depth.\n\u2022 Surgical plane: Full unconsciousness; no reaction to painful stimuli.\n\u2022 Other: Use if not fitting categories; specify in notes."
            }
        },
        "duration": {
            "title": "Duration (minutes)",
            "brief": "duration",
            "type": "number",
            "minimum": 0,
            "units": "min",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Duration of anesthesia in minutes."
            }
        },
        "endOfAnesthesia": {
            "title": "End of anesthesia",
            "brief": "end time",
            "type": "string",
            "format": "time",
            "options": {
                "infoText": "Time when anesthesia ended."
            }
        },
        "complications": {
            "title": "Complications",
            "brief": "complications",
            "type": "string",
            "format": "textarea",
            "options": {
                "infoText": "Any complications or adverse events that occurred during anesthesia."
            }
        },
        "recoveryTime": {
            "title": "Recovery time (minutes)",
            "brief": "recovery",
            "type": "number",
            "minimum": 0,
            "units": "min",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Time from end of anesthesia to return of righting reflex or normal activity."
            }
        },
        "monitoringMethod": {
            "type": "array",
            "title": "Monitoring methods",
            "brief": "monitoring",
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
            "format": "checkbox",
            "options": {
                "infoText": "Methods used to monitor anesthetic depth."
            }
        },
        "supportiveCare": {
            "type": "array",
            "title": "Supportive care",
            "brief": "support",
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
            "format": "checkbox",
            "options": {
                "infoText": "Supportive care provided during anesthesia."
            }
        }
    },
    "required": [
        "anestheticAgent",
        "route"
    ]
}
```

## AuditoryStimulation
```
{
    "type": "object",
    "title": "Auditory stimulation",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "stimulusTypes": {
            "title": "Stimulus types",
            "type": "array",
            "items": {
                "type": "string",
                "enum": [
                    "Tone",
                    "Click",
                    "White noise",
                    "Pink noise",
                    "Frequency sweep",
                    "Amplitude modulated",
                    "Pulse train",
                    "Chirp",
                    "Other"
                ]
            },
            "uniqueItems": true,
            "options": {
                "infoText": "Types of auditory stimuli used in this paradigm. Select one or more."
            }
        },
        "deliveryMethod": {
            "title": "Delivery method",
            "type": "string",
            "enum": [
                "Free-field speaker",
                "In-ear speaker",
                "Bone conduction",
                "Headphone",
                "Other"
            ],
            "options": {
                "infoText": "How the sound was delivered to the subject. Free-field speakers are most common in head-fixed setups."
            }
        },
        "stimulationContext": {
            "title": "Stimulation context",
            "type": "string",
            "enum": [
                "Passive",
                "Behavioral task",
                "Closed-loop",
                "Anesthetized",
                "Free behavior"
            ],
            "options": {
                "infoText": "Experimental context in which auditory stimulation was delivered."
            }
        },
        "paradigmDescription": {
            "title": "Paradigm description",
            "type": "string",
            "format": "textarea",
            "options": {
                "infoText": "Free-text description of the auditory stimulation paradigm: include stimulus timing, repetitions, device setup, etc."
            }
        }
    },
    "required": [
        "stimulusTypes"
    ]
}
```

## BarbiturateInjection
```
{
    "type": "object",
    "title": "Barbiturate injection",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "barbiturate": {
            "title": "Barbiturate type",
            "brief": "barbiturate",
            "type": "string",
            "enum": [
                "Pentobarbital",
                "Phenobarbital",
                "Secobarbital",
                "Barbital",
                "Commercial euthanasia solution",
                "Other"
            ],
            "options": {
                "infoText": "Type of barbiturate used for euthanasia."
            }
        },
        "concentration": {
            "title": "Concentration (mg/mL)",
            "brief": "concentration",
            "type": "number",
            "minimum": 0,
            "units": "mg/mL",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Concentration of the barbiturate solution."
            }
        },
        "dosage": {
            "title": "Dosage (mg/kg)",
            "brief": "dosage",
            "type": "number",
            "minimum": 0,
            "units": "mg/kg",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Dosage administered per kilogram of body weight."
            }
        },
        "route": {
            "title": "Administration route",
            "brief": "route",
            "type": "string",
            "enum": [
                "Intraperitoneal (IP)",
                "Intravenous (IV)",
                "Intracardiac",
                "Subcutaneous (SC)",
                "Other"
            ],
            "options": {
                "infoText": "Route of barbiturate administration."
            }
        },
        "volumeAdministered": {
            "title": "Volume administered (mL)",
            "brief": "volume",
            "type": "number",
            "minimum": 0,
            "units": "mL",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Total volume of barbiturate solution administered."
            }
        },
        "sedationAgent": {
            "title": "Sedation agent (if used)",
            "brief": "sedation agent",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., ketamine, isoflurane"
                },
                "infoText": "Sedation agent used prior to euthanasia (if applicable)."
            }
        },
        "timeToUnconsciousness": {
            "title": "Time to unconsciousness (seconds)",
            "brief": "unconscious",
            "type": "number",
            "minimum": 0,
            "units": "sec",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Observed time to loss of consciousness."
            }
        },
        "confirmationOfDeath": {
            "title": "Confirmation of death",
            "brief": "confirmation",
            "type": "array",
            "items": {
                "type": "string",
                "enum": [
                    "Absence of heartbeat",
                    "Absence of breathing",
                    "Absence of reflexes",
                    "Fixed dilated pupils",
                    "Loss of corneal reflex",
                    "Additional dose administered",
                    "Other"
                ]
            },
            "uniqueItems": true,
            "minItems": 0,
            "format": "checkbox",
            "options": {
                "infoText": "Methods used to confirm death."
            }
        }
    },
    "required": [
        "barbiturate",
        "route",
        "confirmationOfDeath"
    ]
}
```

## BehavioralTracking
```
{
    "type": "object",
    "title": "Behavioral tracking",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "trackingMethod": {
            "type": "string",
            "title": "Tracking Method",
            "brief": "Method",
            "enum": [
                "Markerless",
                "Marker-based",
                "Hybrid",
                "Manual scoring"
            ],
            "options": {
                "infoText": "The tracking method."
            }
        },
        "trackedFeatures": {
            "type": "array",
            "title": "Tracked Features",
            "brief": "Features",
            "items": {
                "type": "string",
                "enum": [
                    "Full body",
                    "Head position",
                    "Head direction",
                    "Limbs",
                    "Paws",
                    "Tail",
                    "Eyes",
                    "Whiskers",
                    "Markers",
                    "Rigid body",
                    "Other"
                ]
            },
            "uniqueItems": true,
            "options": {
                "infoText": "Body features being tracked."
            }
        }
    }
}
```

## BloodPressureSensorImplant
```
{
    "type": "object",
    "title": "Blood pressure sensor implant",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "sensorType": {
            "title": "Sensor type",
            "brief": "type",
            "type": "string",
            "enum": [
                "telemetric",
                "catheter-based",
                "fluid-filled",
                "fiber-optic",
                "other"
            ],
            "options": {
                "infoText": "Type of blood pressure sensor used."
            }
        },
        "implantSite": {
            "title": "Implant site",
            "brief": "site",
            "type": "string",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'Femoral artery', 'Carotid artery'"
                },
                "infoText": "Vascular or body location where the pressure sensor was implanted \u2014 e.g., 'Femoral artery','Carotid artery','Aorta','Ventral tail artery','Left ventricle'."
            }
        },
        "catheterMaterial": {
            "title": "Catheter material",
            "brief": "material",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., polyurethane, silicone, polyethylene, PVC"
                },
                "infoText": "Material used for the catheter or tubing connecting the pressure sensor to vasculature."
            }
        },
        "anchoringMethod": {
            "title": "Anchoring method",
            "brief": "anchoring",
            "type": "string",
            "enum": [
                "sutured",
                "subcutaneous tunnel",
                "tissue glue",
                "headcap",
                "cemented to skull",
                "other"
            ],
            "options": {
                "infoText": "How the sensor or catheter were secured in place to prevent movement."
            }
        },
        "sterilizationMethod": {
            "title": "Sterilization method",
            "brief": "sterilization",
            "type": "string",
            "enum": [
                "Autoclave",
                "Ethylene Oxide",
                "Alcohol",
                "Gamma Irradiation",
                "None"
            ],
            "options": {
                "infoText": "Sterilization technique used before implantation."
            }
        }
    },
    "required": [
        "sensorType",
        "anchoringMethod"
    ]
}
```

## BrainExtraction
```
{
    "type": "object",
    "title": "Brain extraction",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "extractionMethod": {
            "title": "Extraction method",
            "brief": "method",
            "type": "string",
            "enum": [
                "Complete removal",
                "Partial removal",
                "Sectional removal",
                "Other"
            ],
            "options": {
                "infoText": "Method used for brain extraction."
            }
        },
        "timeToExtraction": {
            "title": "Time to extraction (minutes)",
            "brief": "time to extraction",
            "type": "number",
            "minimum": 0,
            "units": "min",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Time from euthanasia to brain extraction in minutes. Important for tissue quality."
            }
        },
        "preservationMethod": {
            "title": "Preservation method",
            "brief": "preservation",
            "type": "string",
            "enum": [
                "Fresh (immediate use)",
                "Paraformaldehyde fixation",
                "Formalin fixation",
                "Flash freezing",
                "Liquid nitrogen",
                "Dry ice",
                "Other"
            ],
            "options": {
                "infoText": "Method used to preserve the extracted brain tissue."
            }
        },
        "fixationDuration": {
            "title": "Fixation duration (hours)",
            "brief": "fixation time",
            "type": "number",
            "minimum": 0,
            "units": "hours",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Duration of fixation in hours (if applicable)."
            }
        },
        "storageConditions": {
            "title": "Storage Conditions",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'Room temp', '4\u00b0C', 'Protect from light'"
                },
                "infoText": "E.g., 'Room temp', '4\u00b0C', 'Protect from light'."
            }
        },
        "brainWeight": {
            "title": "Brain weight (grams)",
            "brief": "weight",
            "type": "number",
            "minimum": 0,
            "units": "g",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Weight of the extracted brain in grams."
            }
        }
    },
    "required": [
        "extractionMethod",
        "preservationMethod"
    ]
}
```

## BrainLesion
```
{
    "type": "object",
    "title": "Brain lesion",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "lesionMethod": {
            "title": "Lesion method",
            "brief": "method",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., surgical, suction, chemical, thermal"
                },
                "infoText": "Specify the technique used to induce the brain lesion (e.g., surgical, suction, chemical, thermal, etc.)."
            }
        },
        "volume": {
            "title": "Volume of brain lesion (\u00b5L)",
            "brief": "volume",
            "type": "number",
            "units": "\u00b5L",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Enter the estimated or calculated volume of the brain lesion in microliters."
            }
        },
        "fatalOutcome": {
            "title": "Fatal outcome",
            "brief": "fatal outcome",
            "type": "boolean",
            "format": "checkbox",
            "options": {
                "infoText": "Check this box if the lesion results in a fatal outcome."
            }
        }
    },
    "required": []
}
```

## BrainSlice
```
{
    "type": "object",
    "title": "Brain Slice",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "thickness": {
            "title": "Thickness of slices (\u00b5m)",
            "brief": "thickness",
            "type": "number",
            "units": "\u00b5m",
            "minimum": 0,
            "default": 50,
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "The thickness of the brain slices in micrometers. Thinner slices are typically used for imaging purposes, while thicker slices may be used for electrophysiological recordings."
            }
        },
        "nSlices": {
            "title": "Number of slices",
            "brief": "count",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "Total number of slices obtained from the brain tissue."
            }
        },
        "orientation": {
            "title": "Orientation of slices",
            "brief": "orientation",
            "type": "string",
            "default": "coronal",
            "options": {
                "enum": [
                    "coronal",
                    "sagittal",
                    "horizontal"
                ],
                "infoText": "The orientation of the slices, such as coronal, sagittal, or horizontal. This determines the plane of sectioning relative to the brain's anatomical structure."
            }
        },
        "medium": {
            "title": "Medium used for slice",
            "brief": "medium",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., aCSF, preservation solution"
                },
                "infoText": "The medium in which the brain slices are preserved or maintained during and after slicing. Common mediums include artificial cerebrospinal fluid (aCSF) or specific preservation solutions."
            }
        },
        "vibratomeBladeAngle": {
            "title": "Vibratome blade angle (\u00b0)",
            "brief": "blade angle",
            "type": "number",
            "units": "\u00b0",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "The angle at which the vibratome blade is set to slice the brain tissue. Proper blade angle helps in achieving clean and precise cuts."
            }
        }
    },
    "required": [
        "thickness",
        "orientation"
    ]
}
```

## BreathingSensorImplant
```
{
    "type": "object",
    "title": "Breathing sensor implant",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "sensorType": {
            "title": "Sensor type",
            "brief": "type",
            "type": "string",
            "enum": [
                "Piezoelectric sensor",
                "Chest wall EMG",
                "Intranasal thermocouple",
                "Intranasal pressure sensor",
                "Tracheal airflow sensor",
                "Thoracic pressure sensor",
                "Plethysmography cannula",
                "Other"
            ],
            "options": {
                "infoText": "Type of breathing sensor used."
            }
        },
        "implantSite": {
            "title": "Implant site",
            "brief": "site",
            "type": "string",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., Chest wall, Diaphragm, Nasal cavity"
                },
                "infoText": "Anatomical location where the breathing sensor was implanted or attached \u2014 e.g., 'Chest wall', 'Diaphragm', 'Nasal cavity', 'Trachea', 'Pleural cavity', 'Subcutaneous (telemetry)', 'Other'."
            }
        },
        "wireMaterial": {
            "title": "Wire or lead material",
            "brief": "material",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., stainless steel, silver, silver chloride, platinum, tungsten"
                },
                "infoText": "Material used for connecting wires or leads (e.g., stainless steel, silver, silver chloride, platinum, tungsten)."
            }
        },
        "anchoringMethod": {
            "title": "Anchoring method",
            "brief": "anchoring",
            "type": "string",
            "enum": [
                "sutured",
                "tissue glue",
                "subcutaneous tunnel",
                "cemented to skull",
                "headcap",
                "custom mount",
                "other"
            ],
            "options": {
                "infoText": "How the sensor or wires were fixed in place during implantation."
            }
        },
        "signalTransmission": {
            "title": "Signal transmission",
            "brief": "transmission",
            "type": "string",
            "enum": [
                "tethered",
                "wireless",
                "telemetric",
                "inductive",
                "optical",
                "other"
            ],
            "options": {
                "infoText": "Mode of signal transmission from the sensor to the acquisition device."
            }
        },
        "sterilizationMethod": {
            "title": "Sterilization method",
            "brief": "sterilization",
            "type": "string",
            "enum": [
                "Autoclave",
                "Ethylene Oxide",
                "Alcohol",
                "Gamma Irradiation",
                "None"
            ],
            "options": {
                "infoText": "Sterilization technique applied before implantation."
            }
        }
    },
    "required": [
        "sensorType",
        "anchoringMethod"
    ]
}
```

## BurrHole
```
{
    "type": "object",
    "title": "Burr hole",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "diameter": {
            "title": "Hole diameter (mm)",
            "brief": "diameter",
            "type": "number",
            "minimum": 0,
            "units": "mm",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Diameter of the burr hole in millimeters."
            }
        },
        "purpose": {
            "title": "Purpose",
            "brief": "purpose",
            "type": "string",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., Electrode implantation, Access for injection"
                },
                "infoText": "Primary purpose of creating the burr hole."
            }
        },
        "drillSpeed": {
            "title": "Drill speed (RPM)",
            "brief": "speed",
            "type": "number",
            "minimum": 0,
            "units": "RPM",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Speed of the drill in revolutions per minute."
            }
        },
        "coolingMethod": {
            "title": "Cooling method",
            "brief": "cooling",
            "type": "string",
            "enum": [
                "Saline irrigation",
                "Air cooling",
                "None",
                "Other"
            ],
            "options": {
                "infoText": "Method used to prevent overheating during drilling."
            }
        },
        "complications": {
            "title": "Complications",
            "brief": "complications",
            "type": "string",
            "format": "textarea",
            "options": {
                "infoText": "Any complications that occurred during the procedure, including bleeding, or damage to surrounding tissue."
            }
        }
    },
    "required": []
}
```

## CatheterImplant
```
{
    "type": "object",
    "title": "Catheter implant",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "targetSite": {
            "title": "Target site",
            "brief": "target",
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
            ],
            "options": {
                "infoText": "Anatomical target of the catheter."
            }
        },
        "catheterType": {
            "title": "Catheter type",
            "brief": "type",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., PE-10, Silastic"
                },
                "infoText": "Model or description of the catheter (e.g., PE-10, Silastic)."
            }
        },
        "material": {
            "title": "Material",
            "brief": "material",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., PE (polyethylene), silicone, Teflon, polyurethane"
                },
                "infoText": "Material of the catheter tubing."
            }
        },
        "purpose": {
            "title": "Purpose",
            "brief": "purpose",
            "type": "string",
            "enum": [
                "infusion",
                "sampling",
                "pressure monitoring",
                "drug delivery",
                "other"
            ],
            "options": {
                "infoText": "Primary purpose of the catheter implant."
            }
        },
        "fixationMethod": {
            "title": "Fixation method",
            "brief": "fixation",
            "type": "string",
            "enum": [
                "sutures",
                "dental cement",
                "epoxy",
                "tissue glue",
                "tunneled subcutaneously",
                "other"
            ],
            "options": {
                "infoText": "How the catheter was secured to the body or skull."
            }
        },
        "externalPort": {
            "title": "External port",
            "brief": "external port",
            "type": "string",
            "enum": [
                "head-mounted",
                "back-mounted",
                "tail-mounted",
                "subcutaneous",
                "none"
            ],
            "options": {
                "infoText": "Where the external port or connector was positioned."
            }
        },
        "catheterId": {
            "title": "Catheter ID",
            "brief": "catheter ID",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Unique identifier if the catheter is tracked as a physical resource."
            }
        }
    },
    "required": [
        "targetSite"
    ]
}
```

## CervicalDislocation
```
{
    "type": "object",
    "title": "Cervical dislocation",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "dislocationMethod": {
            "title": "Method of dislocation",
            "brief": "method",
            "type": "string",
            "enum": [
                "Manual",
                "Mechanical device",
                "Scissor method",
                "Other"
            ],
            "options": {
                "infoText": "Method used for cervical dislocation."
            }
        },
        "anestheticAgent": {
            "title": "Anesthetic agent (if used)",
            "brief": "agent",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., CO\u2082, isoflurane"
                },
                "infoText": "Anesthetic agent used prior to euthanasia (if applicable)."
            }
        },
        "confirmationOfDeath": {
            "title": "Confirmation of death",
            "brief": "confirmation",
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
            "format": "checkbox",
            "options": {
                "infoText": "Methods used to confirm death."
            }
        },
        "complications": {
            "title": "Complications",
            "brief": "complications",
            "type": "string",
            "format": "textarea",
            "options": {
                "infoText": "Any complications or issues encountered during the procedure."
            }
        }
    },
    "required": [
        "dislocationMethod",
        "confirmationOfDeath"
    ]
}
```

## Co2ChamberEuthanasia
```
{
    "type": "object",
    "title": "CO\u2082 chamber euthanasia",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "co2Concentration": {
            "title": "CO\u2082 concentration (%)",
            "brief": "CO\u2082",
            "type": "number",
            "minimum": 0,
            "default": 30,
            "maximum": 100,
            "units": "%",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 30% or 70%"
                },
                "infoText": "Concentration of CO\u2082 used in the chamber."
            }
        },
        "flowRate": {
            "title": "CO\u2082 flow rate (L/min)",
            "brief": "flow rate",
            "type": "number",
            "minimum": 0,
            "units": "L/min",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Rate of CO\u2082 flow into the chamber."
            }
        },
        "gradualIntroduction": {
            "title": "Gradual CO\u2082 introduction",
            "brief": "gradual",
            "type": "boolean",
            "format": "checkbox",
            "options": {
                "infoText": "Check if CO\u2082 was introduced gradually (recommended for animal welfare)."
            }
        },
        "prefillingMethod": {
            "title": "Chamber prefilling",
            "brief": "prefilling",
            "type": "string",
            "enum": [
                "Not prefilled",
                "Partially prefilled",
                "Fully prefilled",
                "Other"
            ],
            "options": {
                "infoText": "Method of chamber prefilling with CO\u2082."
            }
        },
        "exposureDuration": {
            "title": "Exposure duration (minutes)",
            "brief": "exposure",
            "type": "number",
            "minimum": 0,
            "default": 5,
            "units": "min",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Duration of CO\u2082 exposure."
            }
        },
        "timeToUnconsciousness": {
            "title": "Time to unconsciousness (seconds)",
            "brief": "unconscious",
            "type": "number",
            "minimum": 0,
            "units": "sec",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Observed time to loss of consciousness."
            }
        },
        "confirmationOfDeath": {
            "title": "Confirmation of death",
            "brief": "confirmation",
            "type": "array",
            "items": {
                "type": "string",
                "enum": [
                    "Absence of heartbeat",
                    "Absence of breathing",
                    "Absence of reflexes",
                    "Fixed dilated pupils",
                    "Loss of corneal reflex",
                    "Continued CO\u2082 exposure",
                    "Other"
                ]
            },
            "uniqueItems": true,
            "minItems": 0,
            "format": "checkbox",
            "options": {
                "infoText": "Methods used to confirm death."
            }
        },
        "chamberVolume": {
            "title": "Chamber volume (L)",
            "brief": "volume",
            "type": "number",
            "minimum": 0,
            "units": "L",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Volume of the euthanasia chamber."
            }
        }
    },
    "required": [
        "co2Concentration",
        "exposureDuration",
        "confirmationOfDeath"
    ]
}
```

## CranialWindow
```
{
    "type": "object",
    "title": "Cranial window",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "surgicalMethod": {
            "title": "Surgical method",
            "brief": "method",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'surgical drill', 'bone saw', 'manual cutting'"
                },
                "infoText": "Describe the surgical technique used to create the cranial window. Common methods include the use of a surgical drill, bone saw, automatic or manual cutting tools to remove a section of the skull."
            }
        },
        "shape": {
            "title": "Shape of cranial window",
            "brief": "shape",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'circular', 'square', 'elliptical'"
                },
                "infoText": "Describe the shape of the cranial window performed, such as square, circular, elliptical, or other specific form. This helps in understanding the surgical approach and potential impact on the underlying brain tissue."
            }
        },
        "dimensions": {
            "title": "Dimensions of cranial window",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., '1.0 mm diameter \u00d7 4 mm length'"
                },
                "infoText": "Dimensions of the window: length, width, diameter or thickness. E.g., '1.0 mm diameter \u00d7 4 mm length'."
            }
        },
        "orientation": {
            "title": "Orientation of cranial window",
            "brief": "orientation",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., '45 degrees to the midline', 'parallel to the sagittal suture'"
                },
                "infoText": "Describe the orientation of the cranial window relative to anatomical landmarks. This can include angle and direction, which are important for precise targeting and minimizing damage to critical areas."
            }
        }
    },
    "required": []
}
```

## Craniectomy
```
{
    "type": "object",
    "title": "Craniectomy",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "surgicalMethod": {
            "title": "Surgical method",
            "brief": "method",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'surgical drill', 'bone saw', 'manual cutting'"
                },
                "infoText": "Describe the surgical technique used for the craniectomy. Common methods include the use of a surgical drill, bone saw, automatic or manual cutting tools to remove a section of the skull."
            }
        },
        "shape": {
            "title": "Shape of craniectomy",
            "brief": "shape",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'circular', 'square', 'oval', 'irregular'"
                },
                "infoText": "Describe the shape of the craniectomy, such as square, circular, oval, or irregular."
            }
        },
        "dimensions": {
            "title": "Dimensions of craniectomy",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., '1.0 mm diameter \u00d7 4 mm length'"
                },
                "infoText": "Dimensions of the craniectomy: length, width, or diameter. E.g., '1.0 mm diameter \u00d7 4 mm length'."
            }
        },
        "orientation": {
            "title": "Orientation of craniectomy",
            "brief": "orientation",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'anterior-posterior', 'left-right', 'oblique'"
                },
                "infoText": "Indicate the orientation of the craniectomy relative to major anatomical landmarks."
            }
        },
        "fatalOutcome": {
            "title": "Fatal outcome",
            "brief": "fatal outcome",
            "type": "boolean",
            "format": "checkbox",
            "options": {
                "infoText": "Check this box if the craniectomy procedure results in a fatal outcome."
            }
        }
    },
    "required": []
}
```

## Craniotomy
```
{
    "type": "object",
    "title": "Craniotomy",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "surgicalMethod": {
            "title": "Surgical method",
            "brief": "method",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'surgical drill', 'bone saw', 'manual cutting'"
                },
                "infoText": "Describe the surgical technique used for the craniotomy. Common methods include the use of a surgical drill, bone saw, automatic or manual cutting tools to remove a section of the skull."
            }
        },
        "shape": {
            "title": "Shape of craniotomy",
            "brief": "shape",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'circular', 'square', 'elliptical'"
                },
                "infoText": "Describe the shape of the craniotomy performed, such as square, circular, elliptical, or other specific form. This helps in understanding the surgical approach and potential impact on the underlying brain tissue."
            }
        },
        "dimensions": {
            "title": "Dimensions of craniotomy",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., '1.0 mm diameter \u00d7 4 mm length'"
                },
                "infoText": "Dimensions of the craniotomy: length, width, or diameter. E.g., '1.0 mm diameter \u00d7 4 mm length'."
            }
        },
        "orientation": {
            "title": "Orientation of craniotomy",
            "brief": "orientation",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Describe the orientation of the craniotomy relative to anatomical landmarks. This can include angle and direction, which are important for precise targeting and minimizing damage to critical areas."
            }
        },
        "fatalOutcome": {
            "title": "Fatal outcome",
            "brief": "fatal outcome",
            "type": "boolean",
            "format": "checkbox",
            "options": {
                "infoText": "Check this box if the craniectomy procedure results in a fatal outcome."
            }
        }
    },
    "required": []
}
```

## Cryosectioning
```
{
    "type": "object",
    "title": "Cryosectioning",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "sectionThickness": {
            "title": "Section thickness (\u00b5m)",
            "brief": "thickness",
            "type": "number",
            "minimum": 0,
            "units": "\u00b5m",
            "default": 40,
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Thickness of each section in micrometers."
            }
        },
        "temperature": {
            "title": "Cutting temperature (\u00b0C)",
            "brief": "temperature",
            "type": "number",
            "default": 0,
            "units": "\u00b0C",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Temperature at which sectioning was performed."
            }
        },
        "embeddingMedium": {
            "title": "Embedding medium",
            "brief": "embedding",
            "type": "string",
            "enum": [
                "OCT compound",
                "Tissue-Tek",
                "Cryomatrix",
                "Gelatin",
                "None",
                "Other"
            ],
            "options": {
                "infoText": "Medium used to embed the tissue for sectioning."
            }
        },
        "orientation": {
            "title": "Sectioning orientation",
            "brief": "orientation",
            "type": "string",
            "enum": [
                "Coronal",
                "Sagittal",
                "Horizontal",
                "Other"
            ],
            "options": {
                "infoText": "Anatomical plane of sectioning."
            }
        },
        "numberOfSections": {
            "title": "Number of sections",
            "brief": "sections",
            "type": "number",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Total number of sections obtained."
            }
        },
        "serialSectioning": {
            "title": "Serial sectioning",
            "brief": "serial",
            "type": "boolean",
            "format": "checkbox",
            "options": {
                "infoText": "Check if sections were collected serially (every section saved)."
            }
        },
        "sectionInterval": {
            "title": "Section interval",
            "brief": "interval",
            "type": "number",
            "minimum": 1,
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 1 for every section, 3 for every 3rd section"
                },
                "infoText": "Interval for section collection (e.g., 1 = every section, 3 = every 3rd section)."
            }
        },
        "storageMethod": {
            "title": "Section storage method",
            "brief": "storage",
            "type": "string",
            "enum": [
                "Mounted on slides",
                "Free-floating in solution",
                "Stored in plates",
                "Other"
            ],
            "options": {
                "infoText": "Method used to store the sections after cutting."
            }
        },
        "storageBuffer": {
            "title": "Storage buffer/solution",
            "brief": "buffer",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., PBS, cryoprotectant solution"
                },
                "infoText": "Buffer or solution used to store sections."
            }
        }
    },
    "required": [
        "sectionThickness",
        "temperature",
        "orientation"
    ]
}
```

## Decapitation
```
{
    "type": "object",
    "title": "Decapitation",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "decapitationMethod": {
            "title": "Decapitation Method",
            "brief": "method",
            "type": "string",
            "enum": [
                "Guillotine",
                "Sharp scissors",
                "Surgical blade",
                "Other"
            ],
            "options": {
                "infoText": "Method/instrument used for decapitation."
            }
        },
        "anestheticAgent": {
            "title": "Anesthetic agent (if used)",
            "brief": "agent",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., CO\u2082, isoflurane, ketamine"
                },
                "infoText": "Anesthetic agent used prior to euthanasia (if applicable)."
            }
        },
        "complications": {
            "title": "Complications",
            "brief": "complications",
            "type": "string",
            "format": "textarea",
            "options": {
                "infoText": "Any complications or issues encountered during the procedure."
            }
        }
    },
    "required": [
        "decapitationMethod"
    ]
}
```

## EcgImplant
```
{
    "type": "object",
    "title": "ECG implant",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "wireCount": {
            "title": "Wire count",
            "brief": "wires",
            "type": "integer",
            "minimum": 1,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "Number of ECG wires implanted."
            }
        },
        "wireMaterial": {
            "title": "Wire material",
            "brief": "material",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., stainless steel, silver chloride, platinum, gold"
                },
                "infoText": "Material used for ECG wire leads."
            }
        },
        "wireInsulation": {
            "title": "Wire insulation type",
            "brief": "insulation",
            "type": "string",
            "enum": [
                "Teflon",
                "polyimide",
                "silicone",
                "none",
                "other"
            ],
            "options": {
                "infoText": "Insulation material covering the wire shaft, excluding the exposed recording tip."
            }
        },
        "implantSite": {
            "title": "Implant site",
            "brief": "site",
            "type": "string",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'chest wall', 'right shoulder', 'left hindlimb', 'subcutaneous over heart'"
                },
                "infoText": "Where the ECG electrodes were implanted \u2014 e.g., 'chest wall', 'right shoulder', 'left hindlimb', or 'subcutaneous over heart'."
            }
        },
        "anchoringMethod": {
            "title": "Anchoring method",
            "brief": "anchoring",
            "type": "string",
            "enum": [
                "sutured",
                "subcutaneous tunnel",
                "tissue glue",
                "headcap",
                "cemented to skull",
                "other"
            ],
            "options": {
                "infoText": "How the ECG wires were fixed in place to prevent movement."
            }
        },
        "sterilizationMethod": {
            "title": "Sterilization method",
            "brief": "sterilization",
            "type": "string",
            "enum": [
                "Autoclave",
                "Ethylene Oxide",
                "Alcohol",
                "Gamma Irradiation",
                "None"
            ],
            "options": {
                "infoText": "Sterilization technique used for ECG components."
            }
        }
    },
    "required": [
        "anchoringMethod"
    ]
}
```

## EegImplant
```
{
    "type": "object",
    "title": "EEG implant",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "wireCount": {
            "title": "Wire count",
            "brief": "wires",
            "type": "integer",
            "minimum": 1,
            "default": 1,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "Number of electrodes used for EEG recording."
            }
        },
        "electrodeType": {
            "title": "Electrode type",
            "brief": "type",
            "type": "string",
            "enum": [
                "skull screw",
                "flat wire",
                "disc",
                "custom",
                "other"
            ],
            "options": {
                "infoText": "Form factor of the EEG electrode, e.g., skull screws or flat metal contacts."
            }
        },
        "electrodeMaterial": {
            "title": "Electrode material",
            "brief": "material",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., stainless steel, silver chloride, platinum, gold, tugnsten"
                },
                "infoText": "Material used in the electrode. Common choices include stainless steel and Ag/AgCl."
            }
        },
        "referencingScheme": {
            "title": "Referencing scheme",
            "brief": "referencing",
            "type": "string",
            "enum": [
                "single reference",
                "common average",
                "bipolar",
                "differential",
                "other"
            ],
            "options": {
                "infoText": "Type of referencing used in the EEG setup."
            }
        },
        "anchoringMethod": {
            "title": "Anchoring method",
            "brief": "anchoring",
            "type": "string",
            "enum": [
                "dental cement",
                "screws",
                "acrylic",
                "UV-cured resin",
                "headcap",
                "other"
            ],
            "options": {
                "infoText": "How the EEG electrodes were secured in place."
            }
        },
        "shielding": {
            "title": "Faraday shielding",
            "brief": "shielding",
            "type": "string",
            "enum": [
                "none",
                "copper mesh",
                "conductive paint",
                "aluminum foil",
                "headcap integrated",
                "other"
            ],
            "options": {
                "infoText": "Whether and how the EEG implant was shielded from external noise."
            }
        },
        "sterilizationMethod": {
            "title": "Sterilization method",
            "brief": "sterilization",
            "type": "string",
            "enum": [
                "Autoclave",
                "Ethylene Oxide",
                "Alcohol",
                "Gamma Irradiation",
                "None"
            ],
            "options": {
                "infoText": "How the EEG components were sterilized before implantation."
            }
        }
    },
    "required": [
        "wireCount",
        "electrodeType",
        "electrodeMaterial",
        "anchoringMethod"
    ]
}
```

## EmgImplant
```
{
    "type": "object",
    "title": "EMG implant",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "wireCount": {
            "title": "Wire count",
            "brief": "wires",
            "type": "integer",
            "minimum": 1,
            "default": 1,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "Number of implanted EMG wires (typically one or two per muscle)."
            }
        },
        "wireMaterial": {
            "title": "Wire material",
            "brief": "material",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., stainless steel, silver, platinum, nichrome"
                },
                "infoText": "Material used for the EMG wires. Stainless steel is common in rodents."
            }
        },
        "wireInsulation": {
            "title": "Wire insulation type",
            "brief": "insulation",
            "type": "string",
            "enum": [
                "Teflon",
                "polyimide",
                "silicone",
                "none",
                "other"
            ],
            "options": {
                "infoText": "Type of insulation around the wire shaft, except at exposed recording tip."
            }
        },
        "muscleTargets": {
            "title": "Target muscles",
            "brief": "targets",
            "type": "string",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., neck, diaphragm, masseter, forelimb biceps"
                },
                "infoText": "List of muscles where EMG wires were implanted (e.g., neck, diaphragm, masseter, forelimb biceps)."
            }
        },
        "implantMethod": {
            "title": "Implant method",
            "brief": "method",
            "type": "string",
            "enum": [
                "direct insertion",
                "needle-guided",
                "tunneled subcutaneously",
                "sutured",
                "other"
            ],
            "options": {
                "infoText": "How the wire was placed into the muscle."
            }
        },
        "anchoringMethod": {
            "title": "Anchoring method",
            "brief": "anchoring",
            "type": "string",
            "enum": [
                "sutured to muscle",
                "cemented to skull",
                "subcutaneous tunnel",
                "tissue glue",
                "headcap",
                "other"
            ],
            "options": {
                "infoText": "How the wires were fixed to prevent displacement during recovery or recording."
            }
        },
        "sterilizationMethod": {
            "title": "Sterilization method",
            "brief": "sterilization",
            "type": "string",
            "enum": [
                "Autoclave",
                "Ethylene Oxide",
                "Alcohol",
                "Gamma Irradiation",
                "None"
            ],
            "options": {
                "infoText": "Sterilization technique applied before implantation."
            }
        }
    },
    "required": [
        "wireCount",
        "implantMethod"
    ]
}
```

## GenericImplant
```
{
    "type": "object",
    "title": "Generic implant",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "implantType": {
            "title": "Implant type",
            "brief": "type",
            "type": "string",
            "enum": [
                "sensor",
                "electrode",
                "optical device",
                "mechanical device",
                "fluidic device",
                "structural support",
                "other"
            ],
            "options": {
                "infoText": "General category or function of the implant. This helps classify the implant for downstream filtering and interpretation."
            }
        },
        "implantName": {
            "title": "Implant name or description",
            "brief": "name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "A short name or description of the implant (e.g., 'custom probe', 'prototype sensor', 'flex circuit')."
            }
        },
        "anchoringMethod": {
            "title": "Anchoring method",
            "brief": "anchoring",
            "type": "string",
            "enum": [
                "sutured",
                "tissue glue",
                "subcutaneous tunnel",
                "dental cement",
                "headcap",
                "custom mount",
                "none",
                "other"
            ],
            "options": {
                "infoText": "How the implant was secured in place."
            }
        },
        "signalTransmission": {
            "title": "Signal transmission",
            "brief": "transmission",
            "type": "string",
            "enum": [
                "tethered",
                "wireless",
                "telemetric",
                "optical",
                "none",
                "other"
            ],
            "options": {
                "infoText": "How the implant communicates data (if applicable)."
            }
        },
        "powerSource": {
            "title": "Power source",
            "brief": "power",
            "type": "string",
            "enum": [
                "battery",
                "inductive",
                "wired",
                "passive",
                "none",
                "other"
            ],
            "options": {
                "infoText": "How the implant is powered, if relevant."
            }
        },
        "sterilizationMethod": {
            "title": "Sterilization method",
            "brief": "sterilization",
            "type": "string",
            "enum": [
                "Autoclave",
                "Ethylene Oxide",
                "Alcohol",
                "Gamma Irradiation",
                "None"
            ],
            "options": {
                "infoText": "Sterilization technique used prior to implantation."
            }
        }
    },
    "required": [
        "implantType"
    ]
}
```

## GrinLensImplant
```
{
    "type": "object",
    "title": "GRIN lens implant",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "lensTipType": {
            "title": "Lens tip type",
            "brief": "tip type",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., flat, ground, polished, beveled"
                },
                "infoText": "Describe the shape of the GRIN lens tip. Common values: flat, ground, polished, beveled."
            }
        },
        "lensId": {
            "title": "Lens ID",
            "brief": "lens ID",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Unique identifier or batch number of the GRIN lens. The physical lens is tracked as a consumable."
            }
        },
        "sterilizationMethod": {
            "title": "Sterilization method",
            "brief": "sterilization",
            "type": "string",
            "enum": [
                "Autoclave",
                "Ethylene Oxide",
                "Gamma Irradiation",
                "Alcohol",
                "None"
            ],
            "options": {
                "infoText": "Method used to sterilize the GRIN lens before implantation."
            }
        },
        "mountingMethod": {
            "title": "Mounting method",
            "brief": "mounting",
            "type": "string",
            "enum": [
                "Cement only",
                "Cement + baseplate",
                "Headcap integrated",
                "Custom holder",
                "Other"
            ],
            "options": {
                "infoText": "How the GRIN lens was secured in place after implantation."
            }
        }
    },
    "required": []
}
```

## Headcap
```
{
    "type": "object",
    "title": "Headcap",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "material": {
            "title": "Material",
            "brief": "material",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'dental cement', 'acrylic', 'epoxy', 'UV-cured resin', 'titanium', 'stainless steel', 'plastic'"
                },
                "infoText": "Material used to build the headcap, e.g., dental cement, acrylic, epoxy, UV-cured resin, titanium, stainless steel, or plastic."
            }
        },
        "shape": {
            "title": "Shape",
            "type": "string",
            "format": "text",
            "brief": "shape of headcap",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'hexagonal', 'square', 'oval', 'cylinder'"
                },
                "infoText": "Geometrical shape or design (e.g. hexagonal, square, oval, cylinder)."
            }
        },
        "constructionMethod": {
            "title": "Construction Method",
            "type": "string",
            "enum": [
                "manually built",
                "custom-built",
                "3D-printed",
                "milled",
                "molded",
                "other"
            ],
            "brief": "construction method",
            "options": {
                "infoText": "How the headcap was constructed."
            }
        },
        "attachmentMethod": {
            "title": "Attachment Method",
            "type": "string",
            "enum": [
                "dental cement",
                "UV-cured resin",
                "super glue",
                "epoxy",
                "screws",
                "other"
            ],
            "brief": "attachment method",
            "options": {
                "infoText": "Method used to affix the headcap to the skull."
            }
        },
        "shielding": {
            "title": "Faraday Shielding",
            "brief": "shielding",
            "type": "string",
            "enum": [
                "none",
                "conductive paint",
                "copper mesh",
                "aluminum foil",
                "custom",
                "unknown"
            ],
            "options": {
                "infoText": "Whether and how the headcap was shielded to reduce electrical noise."
            }
        },
        "skullPreparation": {
            "title": "Skull Preparation",
            "type": "string",
            "format": "text",
            "brief": "skull prep.",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'cleaned', 'roughened', 'dried'"
                },
                "infoText": "How the skull was prepared (e.g., cleaned, roughened, dried) before attachment."
            }
        },
        "headcapId": {
            "title": "Headcap ID",
            "type": "string",
            "format": "text",
            "brief": "headcap ID",
            "options": {
                "infoText": "A unique identifier for the headcap."
            }
        }
    },
    "required": []
}
```

## HeadFixation
```
{
    "type": "object",
    "title": "Head Fixation",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fixationMethod": {
            "type": "array",
            "title": "Fixation methods",
            "brief": "fixation",
            "items": {
                "type": "string",
                "enum": [
                    "Ear bars",
                    "Nose clamp",
                    "Tooth bar",
                    "Headpost clamp",
                    "Custom holder",
                    "Other"
                ]
            },
            "uniqueItems": true,
            "minItems": 0,
            "options": {
                "infoText": "Methods used to the fixate head, typically using a stereotaxic frame or custom apparatus."
            }
        },
        "alignment": {
            "title": "Alignment",
            "type": "string",
            "brief": "alignment",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g. 'bregma and lambda aligned; slight ML tilt to the left'"
                },
                "infoText": "The alignment achieved in the fixation procedure (e.g. bregma and lambda aligned; slight ML tilt to the left)"
            }
        },
        "fixatioDetails": {
            "title": "Fixation details",
            "type": "string",
            "brief": "details",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g. 'steel ear bars and ML adjustment screws - firm fit, no movement'"
                },
                "infoText": "Further details on the fixation method used, including materials (e.g. 'steel ear bars and ML adjustment screws - firm fit, no movement')"
            }
        },
        "topicalAnesthesia": {
            "title": "Topical anesthesia",
            "type": "string",
            "brief": "topical anesthesia",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g. Lidocaine gel, EMLA cream, None"
                },
                "infoText": "Topical anesthetic used at fixation points (e.g. Lidocaine gel, EMLA cream, None)."
            }
        }
    },
    "required": []
}
```

## Headpost
```
{
    "type": "object",
    "title": "Headpost",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "material": {
            "title": "Material",
            "brief": "material",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., titanium, stainless steel, plastic"
                },
                "infoText": "Material of the headpost, e.g., titanium, stainless steel, or plastic."
            }
        },
        "shape": {
            "title": "Shape",
            "type": "string",
            "format": "text",
            "brief": "shape",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., flat bar, U-frame, circular post"
                },
                "infoText": "Geometrical shape or design (e.g., flat bar, U-frame, circular post)."
            }
        },
        "constructionMethod": {
            "title": "Construction method",
            "type": "string",
            "enum": [
                "manually built",
                "custom-built",
                "3D-printed",
                "milled",
                "other"
            ],
            "brief": "construction method",
            "options": {
                "infoText": "How the headpost was constructed prior to implantation."
            }
        },
        "attachmentMethod": {
            "title": "Attachment method",
            "type": "string",
            "enum": [
                "dental cement",
                "super glue",
                "epoxy",
                "screws",
                "other"
            ],
            "brief": "attachment method",
            "options": {
                "infoText": "Method used to affix the headpost to the skull."
            }
        },
        "skullPreparation": {
            "title": "Skull preparation",
            "type": "string",
            "format": "text",
            "brief": "skull prep.",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., cleaning, roughening, drying"
                },
                "infoText": "How the skull was prepared (e.g., cleaning, roughening, drying) before attachment."
            }
        },
        "headpostId": {
            "title": "Headpost ID",
            "type": "string",
            "format": "text",
            "brief": "headpost ID",
            "options": {
                "infoText": "A unique identifier for the headpost."
            }
        }
    },
    "required": []
}
```

## InhalantOverdose
```
{
    "type": "object",
    "title": "Inhalant overdose",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "anestheticAgent": {
            "title": "Anesthetic agent",
            "brief": "agent",
            "type": "string",
            "enum": [
                "Isoflurane",
                "Sevoflurane",
                "Halothane",
                "Desflurane",
                "Enflurane",
                "Other"
            ],
            "options": {
                "infoText": "Inhalant anesthetic used for overdose euthanasia."
            }
        },
        "concentration": {
            "title": "Concentration (%)",
            "brief": "concentration",
            "type": "number",
            "minimum": 0,
            "maximum": 100,
            "units": "%",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 5-8"
                },
                "infoText": "Concentration of anesthetic agent used."
            }
        },
        "deliveryMethod": {
            "title": "Delivery method",
            "brief": "delivery",
            "type": "string",
            "enum": [
                "Anesthesia chamber",
                "Nose cone",
                "Intubation",
                "Bell jar",
                "Other"
            ],
            "options": {
                "infoText": "Method used to deliver the anesthetic agent."
            }
        },
        "oxygenFlowRate": {
            "title": "Oxygen flow rate (L/min)",
            "brief": "O\u2082 flow",
            "type": "number",
            "minimum": 0,
            "units": "L/min",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Flow rate of oxygen carrier gas."
            }
        },
        "exposureDuration": {
            "title": "Exposure duration (minutes)",
            "brief": "exposure",
            "type": "number",
            "minimum": 0,
            "units": "min",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Duration of anesthetic exposure."
            }
        },
        "timeToUnconsciousness": {
            "title": "Time to unconsciousness (seconds)",
            "brief": "unconscious",
            "type": "number",
            "minimum": 0,
            "units": "sec",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Observed time to loss of consciousness."
            }
        },
        "sedationAgent": {
            "title": "Sedation agent (if used)",
            "brief": "sedation agent",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., CO\u2082, ketamine"
                },
                "infoText": "Sedation agent used prior to inhalant overdose (if applicable)."
            }
        },
        "confirmationOfDeath": {
            "title": "Confirmation of death",
            "brief": "confirmation",
            "type": "array",
            "items": {
                "type": "string",
                "enum": [
                    "Absence of heartbeat",
                    "Absence of breathing",
                    "Absence of reflexes",
                    "Fixed dilated pupils",
                    "Loss of corneal reflex",
                    "Continued anesthetic exposure",
                    "Other"
                ]
            },
            "uniqueItems": true,
            "minItems": 0,
            "format": "checkbox",
            "options": {
                "infoText": "Methods used to confirm death."
            }
        }
    },
    "required": []
}
```

## Injection
```
{
    "type": "object",
    "title": "Injection",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "injectionVolume": {
            "title": "Injection volume (mL)",
            "brief": "volume",
            "units": "mL",
            "type": "number",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "The total volume of the solution to be injected, measured in milliliter."
            }
        },
        "injectionRate": {
            "title": "Injection rate (mL/s)",
            "brief": "rate",
            "units": "mL/s",
            "type": "number",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Rate at which the solution is injected, expressed in milliliters per second."
            }
        },
        "injectionMethod": {
            "title": "Injection Method",
            "brief": "injection method",
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
            ],
            "descriptions": {
                "Intracerebroventricular (ICV)": "Injection into the brain's ventricles for central nervous system delivery.",
                "Intramuscular (IM)": "Injection into muscle tissue, often used for vaccines or slow absorption.",
                "Intravenous (IV)": "Injection into a vein for immediate systemic circulation.",
                "Intradermal (ID)": "Injection into the dermis, often for allergy tests or certain vaccines.",
                "Subcutaneous (SC)": "Injection under the skin for slower absorption.",
                "Intracardiac (IC)": "Injection into the heart, often for emergencies or experimental settings.",
                "Intraperitoneal (IP)": "Injection into the peritoneal cavity, commonly used in animal studies.",
                "Intrathecal (IT)": "Injection into the spinal canal to deliver drugs to the cerebrospinal fluid.",
                "Epidural": "Injection into the epidural space around the spinal cord, often for pain management.",
                "Retro-orbital (RO)": "Injection through the eye's orbital sinus, commonly in small animal research.",
                "Intranasal (IN)": "Delivery through nasal passages, allowing non-invasive central nervous system access.",
                "Intra-articular": "Injection into a joint, used for conditions affecting joint health.",
                "Intravitreal": "Injection into the eye's vitreous humor for treating certain eye conditions.",
                "Intralesional": "Injection directly into a lesion, often used in dermatology and oncology."
            },
            "options": {
                "infoText": "Defines the injection method."
            }
        },
        "concentration": {
            "title": "Concentration of solution (mg/mL)",
            "type": "number",
            "minimum": 0,
            "brief": "concentration",
            "units": "mg/mL",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "The concentration of the injected solution. Enter only if the concentration differs from the concentration of the solution. In milligram per milliliter."
            }
        },
        "injectionProfile": {
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
                "infoText": "Describes the injection profile."
            }
        },
        "injectionSide": {
            "title": "Injection side (brain hemisphere or body side)",
            "brief": "side",
            "type": "string",
            "enum": [
                "Left",
                "Right",
                "Midline",
                "Unknown"
            ],
            "options": {
                "infoText": "Which side of the brain or body the injection targets."
            }
        }
    },
    "required": []
}
```

## NerveCuffImplant
```
{
    "type": "object",
    "title": "Nerve cuff implant",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "cuffType": {
            "title": "Cuff type",
            "brief": "type",
            "type": "string",
            "enum": [
                "monopolar",
                "bipolar",
                "tripolar",
                "multi-contact",
                "split-ring",
                "spiral",
                "other"
            ],
            "options": {
                "infoText": "Configuration and geometry of the cuff. Common types include bipolar and tripolar configurations."
            }
        },
        "targetNerve": {
            "title": "Target nerve",
            "brief": "nerve",
            "type": "string",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., sciatic, vagus, median"
                },
                "infoText": "Name or anatomical label of the nerve the cuff was implanted on (e.g., 'sciatic', 'vagus', 'median', 'hypoglossal')."
            }
        },
        "cuffMaterial": {
            "title": "Cuff material",
            "brief": "material",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., silicone, polyimide, PDMS, polyurethane"
                },
                "infoText": "Base material used for the body of the nerve cuff (e.g., silicone tubing or flexible polymer)."
            }
        },
        "electrodeMaterial": {
            "title": "Electrode material",
            "brief": "electrode",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., platinum, platinum-iridium, silver, stainless steel"
                },
                "infoText": "Material of the embedded electrode contacts inside the nerve cuff."
            }
        },
        "anchoringMethod": {
            "title": "Anchoring method",
            "brief": "anchoring",
            "type": "string",
            "enum": [
                "suture to surrounding tissue",
                "tissue glue",
                "self-closing cuff",
                "non-anchored (loose fit)",
                "subcutaneous tunnel",
                "other"
            ],
            "options": {
                "infoText": "How the cuff was fixed around or near the nerve to prevent displacement."
            }
        },
        "wireExitRoute": {
            "title": "Wire exit route",
            "brief": "exit route",
            "type": "string",
            "enum": [
                "subcutaneous tunnel to headcap",
                "abdominal connector",
                "dorsal skin exit",
                "wireless/inductive",
                "other"
            ],
            "options": {
                "infoText": "How the lead wires exited the body or were routed for connection to recording/stimulation equipment."
            }
        },
        "signalTransmission": {
            "title": "Signal transmission",
            "brief": "transmission",
            "type": "string",
            "enum": [
                "tethered",
                "wireless",
                "telemetric",
                "optical",
                "none",
                "other"
            ],
            "options": {
                "infoText": "How the signal was transmitted to external devices (e.g., via headstage cable, telemetry)."
            }
        },
        "sterilizationMethod": {
            "title": "Sterilization method",
            "brief": "sterilization",
            "type": "string",
            "enum": [
                "Autoclave",
                "Ethylene Oxide",
                "Alcohol",
                "Gamma Irradiation",
                "None"
            ],
            "options": {
                "infoText": "Sterilization technique used prior to implantation."
            }
        }
    },
    "required": [
        "cuffType",
        "anchoringMethod"
    ]
}
```

## OdorStimulation
```
{
    "type": "object",
    "title": "Odor stimulation",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "odorants": {
            "title": "Odorants used",
            "type": "string",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., isoamyl acetate, limonene, mineral oil control"
                },
                "infoText": "List the names or identifiers of odorants used in the stimulation paradigm (e.g., isoamyl acetate, limonene, mineral oil control)."
            }
        },
        "deliveryMethod": {
            "title": "Delivery method",
            "type": "string",
            "enum": [
                "Olfactometer",
                "Manually pipetted",
                "Syringe injection",
                "Headspace exposure",
                "Cotton swab",
                "Other"
            ],
            "options": {
                "infoText": "How the odor was delivered to the subject. Use 'Olfactometer' for computer-controlled systems."
            }
        },
        "carrierGas": {
            "title": "Carrier gas",
            "type": "string",
            "enum": [
                "Air",
                "O\u2082",
                "N\u2082",
                "CO\u2082",
                "Other"
            ],
            "options": {
                "infoText": "Type of gas used to carry the odorant into the delivery stream (if applicable)."
            }
        },
        "stimulationContext": {
            "title": "Stimulation context",
            "type": "string",
            "enum": [
                "Passive",
                "Behavioral task",
                "Closed-loop",
                "Anesthetized",
                "Free behavior"
            ],
            "options": {
                "infoText": "Experimental context in which odor stimulation occurred."
            }
        },
        "paradigmDescription": {
            "title": "Paradigm description",
            "type": "string",
            "format": "textarea",
            "options": {
                "infoText": "Free-text description of the stimulation paradigm, including stimulus timing, delivery parameters, and experimental goals."
            }
        }
    },
    "required": []
}
```

## OpticFiberImplant
```
{
    "type": "object",
    "title": "Optic fiber implant",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fiberTipShape": {
            "title": "Fiber tip shape",
            "brief": "tip shape",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., flat, angled, rounded"
                },
                "infoText": "Specify the shape of the tip. Common shapes include flat, angled, or rounded."
            }
        },
        "fiberId": {
            "title": "Fiber ID",
            "type": "string",
            "format": "text",
            "brief": "fiber ID",
            "options": {
                "infoText": "A unique identifier for the optic fiber."
            }
        },
        "sterilizationMethod": {
            "title": "Sterilization method",
            "type": "string",
            "enum": [
                "Autoclave",
                "Ethylene Oxide",
                "Gamma Irradiation",
                "Alcohol",
                "None"
            ],
            "brief": "sterilization",
            "options": {
                "infoText": "Sterilization method for ensuring the implant is safe for implantation."
            }
        }
    },
    "required": []
}
```

## PerfusionFixation
```
{
    "type": "object",
    "title": "Brain Perfusion Fixation",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "perfusionMethod": {
            "title": "Perfusion method",
            "brief": "method",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., transcardial, intracardiac, intracranial"
                },
                "infoText": "Describe the perfusion method used for fixation."
            }
        },
        "volume": {
            "title": "Perfusion volume (mL)",
            "brief": "volume",
            "type": "number",
            "units": "mL",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Specify the total volume of fixative solution used in milliliters. Adequate volume ensures complete perfusion and fixation of brain tissue, which is critical for preserving tissue architecture and molecular integrity."
            }
        },
        "fatalOutcome": {
            "title": "Fatal outcome",
            "brief": "fatal outcome",
            "type": "boolean",
            "format": "checkbox",
            "options": {
                "infoText": "Check this box if the perfusion method results in a fatal outcome for the subject."
            }
        }
    },
    "required": []
}
```

## PrismImplant
```
{
    "type": "object",
    "title": "Prism implant",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "prismId": {
            "title": "Prism ID",
            "brief": "prism ID",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Unique identifier for the physical prism (e.g., serial number or batch). The prism itself is tracked as a consumable."
            }
        },
        "sterilizationMethod": {
            "title": "Sterilization method",
            "brief": "sterilization",
            "type": "string",
            "enum": [
                "Autoclave",
                "Ethylene Oxide",
                "Gamma Irradiation",
                "Alcohol",
                "None"
            ],
            "options": {
                "infoText": "Method used to sterilize the prism before implantation."
            }
        },
        "mountingMethod": {
            "title": "Mounting method",
            "brief": "mounting",
            "type": "string",
            "enum": [
                "Cement only",
                "Cement + baseplate",
                "Headcap integrated",
                "Custom holder",
                "Other"
            ],
            "options": {
                "infoText": "How the prism was secured in place after implantation."
            }
        }
    },
    "required": []
}
```

## ReferenceElectrodeImplant
```
{
    "type": "object",
    "title": "Reference electrode implant",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "electrodeCount": {
            "title": "Electrode count",
            "brief": "electrode #",
            "units": "",
            "type": "integer",
            "minimum": 1,
            "default": 1,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "Number of electrodes in the reference electrode assembly. Typically 1, but multiple electrodes may be used for redundancy or averaging."
            }
        },
        "electrodeMaterial": {
            "title": "Electrode material",
            "brief": "material",
            "type": "string",
            "format": "text",
            "default": "stainless steel",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., stainless steel, silver chloride, platinum, gold, tungsten"
                },
                "infoText": "Material of the electrode. Common choices include stainless steel and silver chloride. This influences biocompatibility and stability of reference signals."
            }
        },
        "electrodeDiameter": {
            "title": "Electrode diameter (\u00b5m)",
            "brief": "diameter",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Diameter of electrode in micrometers. Affects flexibility, durability, and impedance."
            }
        },
        "impedance": {
            "title": "Impedance (k\u03a9)",
            "type": "number",
            "units": "k\u03a9",
            "brief": "impedance",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Approximate impedance of the reference electrode at 1 kHz. Lower is typically preferred for stable referencing."
            }
        },
        "placementSite": {
            "title": "Placement site",
            "brief": "placement",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., cerebellum, skull surface, contralateral cortex, subcutaneous"
                },
                "infoText": "Where the reference electrode was implanted or placed (e.g., cerebellum, skull surface, contralateral cortex, subcutaneous)."
            }
        },
        "anchoringMethod": {
            "title": "Anchoring method",
            "brief": "anchoring",
            "type": "string",
            "enum": [
                "dental cement",
                "tissue glue",
                "bone screw",
                "subcutaneous tunnel",
                "other"
            ],
            "options": {
                "infoText": "How the reference electrode was secured in place."
            }
        },
        "sterilizationMethod": {
            "title": "Sterilization method",
            "type": "string",
            "enum": [
                "Autoclave",
                "Ethylene Oxide",
                "Gamma Irradiation",
                "Alcohol",
                "None"
            ],
            "brief": "sterilization",
            "options": {
                "infoText": "Sterilization method used before implantation. Important for reducing infection risk without degrading the electrode."
            }
        }
    },
    "required": [
        "electrodeCount",
        "electrodeMaterial"
    ]
}
```

## SiliconProbeImplant
```
{
    "type": "object",
    "title": "Silicon probe implant",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "probeId": {
            "title": "Probe ID",
            "type": "string",
            "format": "text",
            "brief": "probe ID",
            "options": {
                "infoText": "A unique identifier for the silicon probe."
            }
        },
        "sterilizationMethod": {
            "title": "Sterilization method",
            "type": "string",
            "enum": [
                "Autoclave",
                "Ethylene Oxide",
                "Gamma Irradiation",
                "Alcohol",
                "None"
            ],
            "brief": "sterilization",
            "options": {
                "infoText": "Suitable sterilization technique for ensuring the electrode is safe for implantation."
            }
        }
    }
}
```

## SingleWireElectrodeImplant
```
{
    "type": "object",
    "title": "Single wire electrode implant",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "wireCount": {
            "title": "Wire count",
            "brief": "wires",
            "units": "",
            "type": "integer",
            "minimum": 0,
            "default": 1,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "Number of wires used in the electrode assembly."
            }
        },
        "wireDiameter": {
            "title": "Wire diameter (\u00b5m)",
            "brief": "diameter",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "The diameter of the electrode wire in micrometers. Wire diameter affects the electrode's impedance and recording or stimulation capabilities."
            }
        },
        "wireMaterial": {
            "title": "Wire material",
            "brief": "material",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., stainless steel, platinum, gold"
                },
                "infoText": "Common materials include stainless steel, platinum-iridium, and gold. Material choice affects biocompatibility, conductivity, and overall performance of the electrode."
            }
        },
        "impedance": {
            "title": "Impedance (kOhms)",
            "type": "number",
            "units": "kOhms",
            "brief": "impedance",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "The electrical impedance of the electrode, critical for matching with recording equipment and optimizing signal-to-noise ratio."
            }
        },
        "sterilizationMethod": {
            "title": "Sterilization method",
            "type": "string",
            "enum": [
                "Autoclave",
                "Ethylene Oxide",
                "Gamma Irradiation",
                "Alcohol",
                "None"
            ],
            "brief": "sterilization",
            "options": {
                "infoText": "Choose suitable sterilization technique for ensuring the electrode is safe for implantation without damaging its integrity."
            }
        }
    },
    "required": [
        "wireCount"
    ]
}
```

## TactileStimulation
```
{
    "type": "object",
    "title": "Tactile stimulation",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "stimulusTypes": {
            "title": "Stimulation types",
            "type": "array",
            "items": {
                "type": "string",
                "enum": [
                    "Whisker poke",
                    "Whisker deflection",
                    "Air puff",
                    "Brush",
                    "Vibration",
                    "Pressure pad",
                    "Cotton swab",
                    "Other"
                ]
            },
            "uniqueItems": true,
            "options": {
                "infoText": "Select the types of tactile stimuli used in the paradigm. Multiple types can be listed if applicable."
            }
        },
        "stimulationSite": {
            "title": "Stimulation site",
            "type": "string",
            "options": {
                "infoText": "The anatomical region where tactile stimuli were applied (e.g., 'whisker pad', 'hindpaw', 'tail')."
            }
        },
        "deliveryMethod": {
            "title": "Delivery method",
            "type": "string",
            "enum": [
                "Manual (e.g., cotton swab)",
                "Piezo actuator",
                "Solenoid piston",
                "Air puff system",
                "Brush or probe",
                "Other"
            ],
            "options": {
                "infoText": "The method or device used to deliver the tactile stimulus to the subject."
            }
        },
        "stimulationContext": {
            "title": "Stimulation context",
            "type": "string",
            "enum": [
                "Passive",
                "Behavioral task",
                "Closed-loop",
                "Anesthetized",
                "Free behavior"
            ],
            "options": {
                "infoText": "Experimental context in which tactile stimulation occurred."
            }
        },
        "paradigmDescription": {
            "title": "Paradigm description",
            "type": "string",
            "format": "textarea",
            "options": {
                "infoText": "Free-text description of the tactile stimulation paradigm, including stimulus timing, frequency, devices used, and behavioral conditions."
            }
        }
    },
    "required": [
        "stimulusTypes"
    ]
}
```

## TemperatureSensorImplant
```
{
    "type": "object",
    "title": "Temperature sensor implant",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "sensorType": {
            "title": "Sensor type",
            "brief": "type",
            "type": "string",
            "enum": [
                "thermocouple",
                "thermistor",
                "digital IC",
                "telemetric sensor",
                "logger (passive)",
                "fiber-optic",
                "other"
            ],
            "options": {
                "infoText": "Type of temperature sensor implanted. Examples include thermocouples, telemetry sensors, or passive loggers."
            }
        },
        "wireMaterial": {
            "title": "Wire or lead material",
            "brief": "material",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., copper, constantan, platinum, stainless steel"
                },
                "infoText": "Material of the sensor leads, if applicable. Thermocouples often use copper or constantan."
            }
        },
        "anchoringMethod": {
            "title": "Anchoring method",
            "brief": "anchoring",
            "type": "string",
            "enum": [
                "sutured",
                "tissue glue",
                "subcutaneous tunnel",
                "cemented to skull",
                "headcap",
                "free-floating",
                "other"
            ],
            "options": {
                "infoText": "How the sensor or wires were secured at the implantation site."
            }
        },
        "signalTransmission": {
            "title": "Signal transmission",
            "brief": "transmission",
            "type": "string",
            "enum": [
                "tethered",
                "wireless",
                "telemetric",
                "optical",
                "logger (retrieved)",
                "none",
                "other"
            ],
            "options": {
                "infoText": "How temperature data is retrieved. 'Logger (retrieved)' refers to onboard storage until post hoc download."
            }
        },
        "powerSource": {
            "title": "Power source",
            "brief": "power",
            "type": "string",
            "enum": [
                "battery",
                "inductive",
                "wired",
                "passive",
                "none",
                "other"
            ],
            "options": {
                "infoText": "How the temperature sensor is powered, if applicable."
            }
        },
        "sterilizationMethod": {
            "title": "Sterilization method",
            "brief": "sterilization",
            "type": "string",
            "enum": [
                "Autoclave",
                "Ethylene Oxide",
                "Alcohol",
                "Gamma Irradiation",
                "None"
            ],
            "options": {
                "infoText": "Sterilization technique used before implantation."
            }
        }
    },
    "required": [
        "sensorType",
        "anchoringMethod"
    ]
}
```

## TetrodeWireElectrodeImplant
```
{
    "type": "object",
    "title": "Tetrode wire electrode implant",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "tetrodeCount": {
            "title": "Tetrode count",
            "brief": "count",
            "units": "",
            "type": "integer",
            "minimum": 0,
            "default": 1,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "Number of tetrodes in the assembly. Each tetrode is typically used to record from different brain regions or to provide redundancy and spatial resolution in neural recordings."
            }
        },
        "nWiresTetrode": {
            "title": "Wires per tetrode",
            "brief": "wires/tetrode",
            "units": "",
            "type": "integer",
            "minimum": 0,
            "default": 4,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "Number of wires that make up each tetrode. Standard tetrodes consist of four wires twisted together, which allows for precise spatial discrimination of neuronal signals."
            }
        },
        "wireDiameter": {
            "title": "Wire diameter (\u00b5m)",
            "brief": "diameter",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "The diameter of each wire in micrometers. This affects the impedance of the electrode and is crucial for determining the quality and sensitivity of the recordings."
            }
        },
        "wireMaterial": {
            "title": "Wire material",
            "brief": "material",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., stainless steel, platinum, nichrome"
                },
                "infoText": "Material used for the wires. Common materials include platinum-iridium, stainless steel, and nichrome. The choice of material affects the durability, flexibility, and biocompatibility of the electrode."
            }
        },
        "sterilizationMethod": {
            "title": "Sterilization method",
            "type": "string",
            "enum": [
                "Autoclave",
                "Ethylene Oxide",
                "Gamma Irradiation",
                "Alcohol",
                "None"
            ],
            "brief": "sterilization",
            "options": {
                "infoText": "Choose suitable sterilization technique for ensuring the electrode is safe for implantation without damaging its integrity."
            }
        }
    },
    "required": [
        "tetrodeCount"
    ]
}
```

## TissueClearing
```
{
    "type": "object",
    "title": "Tissue clearing",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "clearingMethod": {
            "title": "Clearing method",
            "brief": "method",
            "type": "string",
            "enum": [
                "CLARITY",
                "CUBIC",
                "3DISCO",
                "iDISCO+",
                "PACT",
                "ScaleS",
                "SeeDB",
                "BABB (Benzyl alcohol/Benzyl benzoate)",
                "Passive CLARITY",
                "Other"
            ],
            "options": {
                "infoText": "Tissue clearing protocol used."
            }
        },
        "tissueType": {
            "title": "Tissue type",
            "brief": "tissue",
            "type": "string",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'Whole brain', 'Brain slice', 'Spinal cord'"
                },
                "infoText": "Type of tissue being cleared."
            }
        },
        "fixationTime": {
            "title": "Fixation time (hours)",
            "brief": "fixation",
            "type": "number",
            "minimum": 0,
            "units": "hours",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Duration of tissue fixation before clearing."
            }
        },
        "clearingDuration": {
            "title": "Clearing duration (days)",
            "brief": "clearing time",
            "type": "number",
            "minimum": 0,
            "units": "days",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Total time required for tissue clearing."
            }
        },
        "temperature": {
            "title": "Clearing temperature (\u00b0C)",
            "brief": "temperature",
            "type": "number",
            "units": "\u00b0C",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 37, 25"
                },
                "infoText": "Temperature at which clearing was performed."
            }
        },
        "agitation": {
            "title": "Agitation method",
            "brief": "agitation",
            "type": "string",
            "enum": [
                "Gentle shaking",
                "Rotation",
                "Static",
                "Other"
            ],
            "options": {
                "infoText": "Method of agitation during clearing process."
            }
        },
        "refractiveIndexMatching": {
            "title": "Refractive index matching solution",
            "brief": "RI matching",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., DBE, BABB, 2,2'-thiodiethanol"
                },
                "infoText": "Solution used for final refractive index matching."
            }
        },
        "transparency": {
            "title": "Transparency achieved",
            "brief": "transparency",
            "type": "string",
            "enum": [
                "Complete",
                "Partial",
                "Poor",
                "Failed"
            ],
            "options": {
                "infoText": "Level of tissue transparency achieved."
            }
        },
        "imagingCompatible": {
            "title": "Imaging compatible",
            "brief": "imaging",
            "type": "boolean",
            "format": "checkbox",
            "options": {
                "infoText": "Check if tissue is suitable for subsequent imaging."
            }
        },
        "complications": {
            "title": "Complications/Issues",
            "brief": "issues",
            "type": "string",
            "format": "textarea",
            "options": {
                "infoText": "Any issues encountered during the clearing process."
            }
        }
    },
    "required": [
        "clearingMethod"
    ]
}
```

## VibratomeSectioning
```
{
    "type": "object",
    "title": "Vibratome sectioning",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "sectionThickness": {
            "title": "Section thickness (\u00b5m)",
            "brief": "thickness",
            "type": "number",
            "minimum": 0,
            "units": "\u00b5m",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Thickness of each section in micrometers."
            }
        },
        "bladeType": {
            "title": "Blade type",
            "brief": "blade",
            "type": "string",
            "enum": [
                "Disposable razor blade",
                "Steel blade",
                "Ceramic blade",
                "Sapphire blade",
                "Other"
            ],
            "options": {
                "infoText": "Type of blade used for sectioning."
            }
        },
        "cuttingSpeed": {
            "title": "Cutting speed",
            "brief": "speed",
            "type": "string",
            "enum": [
                "Very slow",
                "Slow",
                "Medium",
                "Fast",
                "Very fast"
            ],
            "options": {
                "infoText": "Speed setting for the vibratome blade."
            }
        },
        "frequency": {
            "title": "Vibration frequency (Hz)",
            "brief": "frequency",
            "type": "number",
            "minimum": 0,
            "units": "Hz",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Vibration frequency of the blade in Hertz."
            }
        },
        "amplitude": {
            "title": "Vibration amplitude",
            "brief": "amplitude",
            "type": "string",
            "enum": [
                "Minimum",
                "Low",
                "Medium",
                "High",
                "Maximum"
            ],
            "options": {
                "infoText": "Amplitude setting for blade vibration."
            }
        },
        "sectioningOrientation": {
            "title": "Sectioning orientation",
            "brief": "orientation",
            "type": "string",
            "enum": [
                "Coronal",
                "Sagittal",
                "Horizontal",
                "Other"
            ],
            "options": {
                "infoText": "Anatomical plane of sectioning."
            }
        },
        "buffer": {
            "title": "Cutting buffer",
            "brief": "buffer",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., ACSF, PBS, Tris buffer"
                },
                "infoText": "Buffer solution used during sectioning."
            }
        },
        "bufferTemperature": {
            "title": "Buffer temperature (\u00b0C)",
            "brief": "temperature",
            "type": "number",
            "units": "\u00b0C",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 4, 23"
                },
                "infoText": "Temperature of the cutting buffer."
            }
        },
        "numberOfSections": {
            "title": "Number of sections",
            "brief": "sections",
            "type": "number",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Total number of sections obtained."
            }
        },
        "sectionQuality": {
            "title": "Section quality",
            "brief": "quality",
            "type": "string",
            "enum": [
                "Excellent",
                "Good",
                "Fair",
                "Poor"
            ],
            "options": {
                "infoText": "Overall quality of the sections obtained."
            }
        },
        "storageMethod": {
            "title": "Section storage method",
            "brief": "storage",
            "type": "string",
            "enum": [
                "Free-floating in buffer",
                "Mounted immediately",
                "Stored in multiwell plates",
                "Other"
            ],
            "options": {
                "infoText": "Method used to store sections after cutting."
            }
        }
    },
    "required": [
        "bladeType"
    ]
}
```

## VirusInjection
```
{
    "type": "object",
    "title": "Virus Injection",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "injectionVolume": {
            "title": "Injection volume (nL)",
            "brief": "volume",
            "units": "nL",
            "type": "number",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "The total volume of the viral solution to be injected, measured in nanoliters."
            }
        },
        "injectionRate": {
            "title": "Injection rate (nL/min)",
            "brief": "rate",
            "units": "nL/min",
            "type": "number",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Rate at which the viral solution is injected, expressed in nanoliters per minute. Controlling the injection rate is essential for preventing tissue damage and ensuring uniform distribution of the virus."
            }
        },
        "titer": {
            "title": "Titer of virus solution (units/mL)",
            "type": "number",
            "minimum": 0,
            "brief": "titer",
            "units": "units/mL",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "The titer of the injected virus solution. Enter only if the titer differs from the titer of the virus solution. In units per milliliter."
            }
        },
        "titerUnit": {
            "title": "Titer unit of virus solution (units/mL)",
            "type": "string",
            "enum": [
                "vg/mL",
                "TU/mL",
                "pfu/mL"
            ],
            "brief": "titer unit",
            "options": {
                "infoText": "vg/mL: Viral genomes per milliliter; TU/mL: Transducing units per milliliter; pfu/mL: Plaque forming units per milliliter."
            }
        },
        "injectionProfile": {
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
                "infoText": "Describes the injection profile of the virus delivery."
            }
        }
    },
    "required": []
}
```

## VisualStimulation
```
{
    "type": "object",
    "title": "Visual stimulation",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
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
                "infoText": "Select the visual stimulus types used in this paradigm. Multiple types may be selected."
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
                "infoText": "Device or method used to present the visual stimuli to the subject."
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
                "infoText": "Relative visual field position where the stimulus was presented with respect to the subject."
            }
        },
        "stimulationContext": {
            "title": "Stimulation context",
            "type": "string",
            "enum": [
                "Passive",
                "Behavioral task",
                "Closed-loop",
                "Anesthetized",
                "Free behavior"
            ],
            "options": {
                "infoText": "Experimental condition in which visual stimulation occurred."
            }
        },
        "paradigmDescription": {
            "title": "Paradigm description",
            "type": "string",
            "format": "textarea",
            "options": {
                "infoText": "Free-text description of the visual stimulation paradigm, including stimulus sequence, timing, and behavioral relevance."
            }
        }
    },
    "required": [
        "stimulusTypes"
    ]
}
```

