---
layout: default
title: Consumable stock
parent: Schemas
grand_parent: API
nav_order: 1
---

# Consumable stock schemas
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## ChemicalReagent
```
{
    "type": "object",
    "title": "Chemical Reagent",
    "options": {
        "compact": true
    },
    "additionalProperties": false,
    "properties": {
        "productId": {
            "title": "Product ID",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Catalog or supplier product code (e.g., 'T8787', 'P6148')."
            }
        },
        "compoundName": {
            "title": "Compound Name",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'Triton X-100', 'Paraformaldehyde'"
                },
                "infoText": "Name of the chemical (e.g., 'Triton X-100', 'Paraformaldehyde')."
            }
        },
        "chemicalType": {
            "title": "Chemical Type",
            "type": "string",
            "enum": [
                "Detergent",
                "Enzyme",
                "Fixative",
                "Indicator or pH Adjuster",
                "Salt or Buffer",
                "Solvent",
                "Stain or Dye",
                "Polymer or Resin",
                "Other"
            ],
            "options": {
                "infoText": "General classification of the reagent."
            }
        },
        "molecularWeight": {
            "title": "Molecular Weight (g/mol)",
            "brief": "weight",
            "units": "g/mol",
            "type": "number",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Molecular weight (measured in gram per mol')."
            }
        },
        "amount": {
            "title": "Amount",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., '500 mL', '2 gram', '50 tablets'"
                },
                "infoText": "Amount of the agent (e.g., '500 mL', '2 gram', '50 tablets')."
            }
        },
        "concentration": {
            "title": "Concentration / Strength",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., '4%', '1 M', '10X'"
                },
                "infoText": "If supplied in solution (e.g., '4%', '1 M', '10X')."
            }
        },
        "purity": {
            "title": "Purity / Grade",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "E.g., '\u226599%', 'Analytical grade', 'ACS reagent'."
            }
        },
        "hazardInfo": {
            "title": "Hazard Information",
            "type": "string",
            "format": "textarea",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'Toxic', 'Corrosive', 'Flammable'"
                },
                "infoText": "Optional summary of safety hazards or GHS classification."
            }
        }
    },
    "required": [
        "chemicalType"
    ]
}
```

## ConsumableDevice
```
{
    "type": "object",
    "title": "Consumable Device",
    "options": {
        "compact": true
    },
    "additionalProperties": false,
    "properties": {
        "productId": {
            "title": "Product ID",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Supplier or catalog identifier (e.g., 'DORIC_MFC_2x200')."
            }
        },
        "deviceClass": {
            "title": "Device Class",
            "brief": "class",
            "type": "string",
            "enum": [
                "Headstage",
                "Headstage Adapter",
                "Miniscope Baseplate",
                "Microdrive",
                "Drive Mount",
                "Fiber Cannula Assembly",
                "Commutator Adapter",
                "Thermal Interface Board",
                "Connector Assembly",
                "Custom Fixture",
                "Other"
            ],
            "options": {
                "infoText": "General class of device."
            }
        },
        "compatibleWith": {
            "title": "Compatible Systems",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'Neuropixels', 'Inscopix'"
                },
                "infoText": "E.g., 'Neuropixels', 'Inscopix', 'Open Ephys', 'Doric'."
            }
        },
        "dimensions": {
            "title": "Physical Dimensions",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., '1.25 mm ferrule, 5 mm length'"
                },
                "infoText": "Key geometry (e.g., '1.25 mm ferrule, 5 mm length')."
            }
        },
        "material": {
            "title": "Material",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'Stainless Steel', 'Zirconia', 'PEEK'"
                },
                "infoText": "Main material (e.g., stainless steel, zirconia, PEEK, plastic)."
            }
        },
        "connectivity": {
            "title": "Connectivity",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'LC/PC', 'Omnetics', 'pin header'"
                },
                "infoText": "Connector/interface type (e.g., 'LC/PC', 'Omnetics', 'pin header')."
            }
        },
        "experimentalUse": {
            "title": "Experimental Use Context",
            "brief": "use context",
            "type": "array",
            "items": {
                "type": "string",
                "enum": [
                    "Chronic Implantation",
                    "Acute Recording",
                    "Optogenetics",
                    "Imaging",
                    "Behavioral Interface",
                    "Other"
                ]
            },
            "uniqueItems": true,
            "options": {
                "infoText": "Intended or validated experimental uses."
            }
        }
    },
    "required": [
        "deviceClass"
    ]
}
```

## ImmunoReagent
```
{
    "type": "object",
    "title": "Antibody or Immunoreagent",
    "options": {
        "compact": true
    },
    "additionalProperties": false,
    "properties": {
        "productId": {
            "title": "Product ID",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Supplier product code or catalog number."
            }
        },
        "reagentType": {
            "title": "Reagent Type",
            "type": "string",
            "enum": [
                "Primary Antibody",
                "Secondary Antibody",
                "Fluorescent Label",
                "DNA Counterstain",
                "Other"
            ],
            "options": {
                "infoText": "General classification of the reagent."
            }
        },
        "hostSpecies": {
            "title": "Host Species",
            "type": "string",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'Rabbit', 'Mouse'"
                },
                "infoText": "Host in which the antibody was raised (e.g., 'Rabbit', 'Mouse')."
            }
        },
        "reactivity": {
            "title": "Reactivity Species",
            "type": "string",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'Rat', 'Mouse', 'Human'"
                },
                "infoText": "Species the antibody is reactive against (e.g., 'Rat', 'Mouse', 'Human')."
            }
        },
        "targetAntigen": {
            "title": "Target Antigen",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'GFAP', 'c-Fos', 'NeuN'"
                },
                "infoText": "What the reagent binds to (e.g., 'GFAP', 'c-Fos', 'NeuN')."
            }
        },
        "clonality": {
            "title": "Clonality",
            "type": "string",
            "enum": [
                "Monoclonal",
                "Polyclonal",
                "Recombinant",
                "Unknown"
            ],
            "options": {
                "infoText": "Whether the antibody is monoclonal or polyclonal."
            }
        },
        "conjugate": {
            "title": "Conjugated Fluorophore or Enzyme",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'Alexa Fluor 488', 'HRP', 'None'"
                },
                "infoText": "E.g., 'Alexa Fluor 488', 'HRP', 'None'."
            }
        },
        "amount": {
            "title": "Amount",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., '500 mL', '2 gram', '50 tablets'"
                },
                "infoText": "Amount of the agent (e.g., '500 mL', '2 gram', '50 tablets')."
            }
        },
        "dilution": {
            "title": "Dilution",
            "brief": "dilution",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., '1:500', '2 \u00b5g/mL'"
                },
                "infoText": "Dilution (e.g., '1:500', '2 \u00b5g/mL')."
            }
        },
        "application": {
            "title": "Validated Applications",
            "type": "array",
            "items": {
                "type": "string",
                "enum": [
                    "IHC",
                    "ICC",
                    "Western Blot",
                    "Flow Cytometry",
                    "Immunoprecipitation",
                    "Other"
                ]
            },
            "uniqueItems": true,
            "options": {
                "infoText": "Supported or validated experimental applications."
            }
        }
    },
    "required": [
        "reagentType"
    ]
}
```

## OpticalComponent
```
{
    "type": "object",
    "title": "Optical Component",
    "options": {
        "compact": true
    },
    "additionalProperties": false,
    "properties": {
        "productId": {
            "title": "Product ID",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Supplier or catalog ID (e.g., 'GRIN1234', 'MP-0.5mm')."
            }
        },
        "componentType": {
            "title": "Optical Component Type",
            "type": "string",
            "enum": [
                "GRIN Lens",
                "Cranial Window",
                "Cover Glass",
                "Microprism",
                "Beamsplitter",
                "Optical Filter",
                "Relay Lens",
                "Other"
            ],
            "options": {
                "infoText": "General class of optical element."
            }
        },
        "material": {
            "title": "Material",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'glass', 'quartz'"
                },
                "infoText": "E.g., glass, quartz, sapphire, polymer."
            }
        },
        "dimensions": {
            "title": "Physical Dimensions",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., '1.0 mm diameter \u00d7 4 mm length'"
                },
                "infoText": "E.g., '1.0 mm diameter \u00d7 4 mm length', '3\u00d73\u00d71 mm prism'."
            }
        },
        "coating": {
            "title": "Surface Coating",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'anti-reflective', 'hydrophobic'"
                },
                "infoText": "E.g., anti-reflective, hydrophobic, no coating."
            }
        },
        "wavelengthMin": {
            "title": "Wavelength minimum (nm)",
            "type": "number",
            "units": "nm",
            "minimum": 0,
            "brief": "wavelength min",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "The minimum wavelength of light (in nanometers) that the optic component is designed to handle."
            }
        },
        "wavelengthMax": {
            "title": "Wavelength maximum (nm)",
            "type": "number",
            "units": "nm",
            "minimum": 0,
            "brief": "wavelength max",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "The maximum wavelength of light (in nanometers) that the optic component can handle."
            }
        },
        "sterility": {
            "title": "Sterile When Delivered",
            "type": "boolean",
            "options": {
                "infoText": "Was this item provided sterile by the manufacturer?"
            }
        },
        "experimentalUse": {
            "title": "Experimental Use Context",
            "type": "array",
            "items": {
                "type": "string",
                "enum": [
                    "Chronic Imaging",
                    "Widefield Imaging",
                    "Two-Photon Imaging",
                    "Optogenetics",
                    "Histology",
                    "Other"
                ]
            },
            "uniqueItems": true,
            "options": {
                "infoText": "Contexts in which this component is typically used."
            }
        }
    },
    "required": [
        "componentType"
    ]
}
```

## OpticFiber
```
{
    "type": "object",
    "title": "Optic fiber",
    "options": {
        "compact": true
    },
    "additionalProperties": false,
    "properties": {
        "fiberIds": {
            "title": "Fiber IDs",
            "type": "string",
            "format": "text",
            "brief": "fiber IDs",
            "options": {
                "infoText": "A unique identifier for each optic fiber."
            }
        },
        "quantity": {
            "title": "Quantity of optic fibers",
            "type": "integer",
            "minimum": 0,
            "brief": "quantity",
            "units": "",
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The quantity of optic fibers in the batch."
            }
        }
    }
}
```

## PharmacologicalAgent
```
{
    "type": "object",
    "title": "Pharmacological Agent",
    "options": {
        "compact": true
    },
    "additionalProperties": false,
    "properties": {
        "productId": {
            "title": "Product ID",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Catalog or supplier ID (e.g., 'C2128')."
            }
        },
        "activeIngredient": {
            "title": "Active Ingredient",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'Ketamine', 'Buprenorphine', 'Isoflurane'"
                },
                "infoText": "Primary pharmacologically active substance (e.g., 'Ketamine', 'Buprenorphine','Isoflurane')."
            }
        },
        "amount": {
            "title": "Amount",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., '500 mL', '2 gram', '50 tablets'"
                },
                "infoText": "Amount of the agent (e.g., '500 mL', '2 gram', '50 tablets')."
            }
        },
        "concentration": {
            "title": "Concentration",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., '10 mg/mL', '0.1%', '50 \u00b5g/tablet'"
                },
                "infoText": "Stated strength of the active ingredient (e.g., '10 mg/mL', '0.1%', '50 \u00b5g/tablet')."
            }
        },
        "dosageForm": {
            "title": "Dosage Form",
            "type": "string",
            "enum": [
                "Solution",
                "Suspension",
                "Tablet",
                "Capsule",
                "Injection",
                "Topical",
                "Patch",
                "Other"
            ],
            "options": {
                "infoText": "Physical form in which the drug is supplied."
            }
        },
        "routeOfAdministration": {
            "title": "Route of Administration",
            "type": "string",
            "enum": [
                "Intraperitoneal (IP)",
                "Intravenous (IV)",
                "Subcutaneous (SC)",
                "Oral",
                "Topical",
                "Inhalation",
                "Intracerebral",
                "Other"
            ],
            "options": {
                "infoText": "Typical method of administration in experiments."
            }
        },
        "pharmacologicalCategory": {
            "title": "Pharmacological Category",
            "type": "string",
            "enum": [
                "Analgesic",
                "Anesthetic",
                "Antibiotic",
                "Neuroactive",
                "Recreational",
                "Vehicle",
                "Experimental",
                "Other"
            ],
            "options": {
                "infoText": "Broad category of action or use."
            }
        },
        "pharmacologicalClass": {
            "title": "Pharmacological Class",
            "brief": "class",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'NSAID', 'GABA agonist', 'NMDA antagonist'"
                },
                "infoText": "Mechanistic or therapeutic class (e.g., 'NSAID', 'GABA agonist', 'NMDA antagonist')."
            }
        },
        "formulation": {
            "title": "Formulation",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "List of excipients, solvents, or carriers (e.g., 'in 10% DMSO + saline')."
            }
        },
        "purity": {
            "title": "Purity / Grade",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "E.g., '\u226598%', 'USP', 'Analytical grade'."
            }
        },
        "experimentalUse": {
            "title": "Experimental Use Context",
            "type": "array",
            "items": {
                "type": "string",
                "enum": [
                    "Surgical",
                    "Behavioral",
                    "Electrophysiology",
                    "Histology",
                    "Imaging",
                    "Other"
                ]
            },
            "uniqueItems": true,
            "options": {
                "infoText": "Contexts in which this agent is typically used."
            }
        }
    },
    "required": [
        "pharmacologicalCategory"
    ]
}
```

## PhysiologicalSolution
```
{
    "type": "object",
    "title": "Physiological Solution",
    "options": {
        "compact": true
    },
    "additionalProperties": false,
    "properties": {
        "solutionName": {
            "title": "Solution Name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Descriptive name of the solution (e.g., 'PBS', 'Saline + Tween 80')."
            }
        },
        "composition": {
            "title": "Composition",
            "type": "string",
            "format": "textarea",
            "options": {
                "infoText": "Full recipe or formula (e.g., '0.9% NaCl in H2O', 'aCSF with 10 mM HEPES')."
            }
        },
        "amount": {
            "title": "Amount",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., '500 mL', '2 gram', '50 tablets'"
                },
                "infoText": "Amount of the agent (e.g., '500 mL', '2 gram', '50 tablets')."
            }
        },
        "pH": {
            "title": "Target pH value",
            "brief": "pH",
            "type": "number",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Target pH value as numeric value (e.g., '7.4')."
            }
        },
        "osmolality": {
            "title": "Osmolality",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "In mOsm/kg, if known (e.g., '300 mOsm')."
            }
        },
        "preparationInstructions": {
            "title": "Preparation Instructions",
            "brief": "preparation",
            "type": "string",
            "format": "textarea",
            "options": {
                "infoText": "Steps for preparing or dissolving the solution (e.g., buffer components, filter sterilization)."
            }
        },
        "sterility": {
            "title": "Sterile",
            "brief": "sterile",
            "type": "boolean",
            "options": {
                "infoText": "Was the solution prepared or delivered sterile?"
            }
        },
        "purpose": {
            "title": "Purpose / Use",
            "type": "array",
            "items": {
                "type": "string",
                "enum": [
                    "Vehicle",
                    "Perfusion",
                    "Fixation",
                    "Dissection",
                    "Buffering",
                    "Storage",
                    "Slice Preparation",
                    "Other"
                ]
            },
            "uniqueItems": true,
            "options": {
                "infoText": "What is the primary use case for this solution?"
            }
        }
    },
    "required": []
}
```

## SiliconProbe
```
{
    "type": "object",
    "title": "Silicon probe",
    "options": {
        "compact": true
    },
    "additionalProperties": false,
    "properties": {
        "probeIds": {
            "title": "Probe IDs",
            "type": "string",
            "format": "text",
            "brief": "probe IDs",
            "options": {
                "infoText": "A unique identifier for each silicon probe."
            }
        },
        "quantity": {
            "title": "Quantity of probes",
            "type": "integer",
            "minimum": 0,
            "brief": "quantity",
            "units": "",
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The quantity of probes in the batch."
            }
        }
    }
}
```

## SingleWireElectrode
```
{
    "type": "object",
    "title": "Single wire electrode",
    "options": {
        "compact": true
    },
    "additionalProperties": false,
    "properties": {
        "wireIds": {
            "title": "Wire IDs",
            "type": "string",
            "format": "text",
            "brief": "wire IDs",
            "options": {
                "infoText": "A unique identifier for the wire electrode as defined by the supplier."
            }
        },
        "quantity": {
            "title": "Quantity of electrodes",
            "type": "integer",
            "minimum": 0,
            "brief": "quantity",
            "units": "",
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The quantity of electrodes."
            }
        },
        "length": {
            "title": "Length (mm)",
            "type": "number",
            "brief": "length",
            "units": "mm",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "The length of the wire in millimeters."
            }
        }
    }
}
```

## TracerDye
```
{
    "type": "object",
    "title": "Tracer or Dye",
    "options": {
        "compact": true
    },
    "additionalProperties": false,
    "properties": {
        "productId": {
            "title": "Product ID",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Catalog number or supplier reference (e.g., 'D282', 'F347')."
            }
        },
        "dyeType": {
            "title": "Type of Dye or Tracer",
            "type": "string",
            "enum": [
                "Fluorescent Tracer",
                "Lipophilic Dye",
                "Retrograde Tracer",
                "Anterograde Tracer",
                "Histological Dye",
                "Vital Stain",
                "Injection Marker",
                "Other"
            ],
            "options": {
                "infoText": "Function or classification of the dye/tracer."
            }
        },
        "fluorophore": {
            "title": "Fluorophore",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'Alexa Fluor 555', 'FITC'"
                },
                "infoText": "Fluorophore or spectral tag used (e.g., 'Alexa Fluor 555', 'FITC')."
            }
        },
        "routeOfApplication": {
            "title": "Route of Application",
            "type": "string",
            "enum": [
                "Injection",
                "Perfusion",
                "Topical",
                "Incubation",
                "Other"
            ],
            "options": {
                "infoText": "How the dye is typically applied."
            }
        },
        "excitationPeak": {
            "title": "Excitation Peak (nm)",
            "type": "number",
            "units": "nm",
            "minimum": 0,
            "brief": "excitation",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Peak wavelength for excitation (e.g., 550 nm)."
            }
        },
        "emissionPeak": {
            "title": "Emission Peak (nm)",
            "type": "number",
            "units": "nm",
            "minimum": 0,
            "brief": "emission",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "Peak wavelength for emission (e.g., 665 nm)."
            }
        },
        "amount": {
            "title": "Amount",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., '500 mL', '2 gram'"
                },
                "infoText": "Amount of the agent (e.g., '500 mL', '2 gram')."
            }
        },
        "solvent": {
            "title": "Solvent / Vehicle",
            "type": "string",
            "format": "text",
            "options": {
                "inputAttributes": {
                    "placeholder": "e.g., 'DMSO', 'Saline', 'Ethanol'"
                },
                "infoText": "Solvent used for preparation (e.g., 'DMSO', 'Saline', 'Ethanol')."
            }
        },
        "preparationInstructions": {
            "title": "Preparation Instructions",
            "type": "string",
            "format": "textarea",
            "options": {
                "infoText": "Preparation or dilution steps before application."
            }
        },
        "experimentalUse": {
            "title": "Experimental Use Context",
            "brief": "use context",
            "type": "array",
            "items": {
                "type": "string",
                "enum": [
                    "Circuit Tracing",
                    "Histology",
                    "Injection Visualization",
                    "Vital Staining",
                    "Other"
                ]
            },
            "uniqueItems": true,
            "options": {
                "infoText": "Typical applications of this tracer or dye."
            }
        }
    },
    "required": [
        "dyeType"
    ]
}
```

## VirusSolution
```
{
    "type": "object",
    "title": "Virus construct",
    "options": {
        "compact": true
    },
    "additionalProperties": false,
    "properties": {
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
                "infoText": "The titer of the virus solution. In units per milliliter"
            }
        },
        "titerUnit": {
            "title": "Titer unit of virus solution",
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
        "volume": {
            "title": "Volume of virus solution (mL)",
            "type": "number",
            "minimum": 0,
            "brief": "volume",
            "units": "mL",
            "options": {
                "inputAttributes": {
                    "placeholder": "numeric"
                },
                "infoText": "The volume of the virus solution."
            }
        },
        "aliquotCount": {
            "title": "The number of aliquots",
            "type": "integer",
            "minimum": 0,
            "brief": "aliquots",
            "units": "",
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of aliquots."
            }
        },
        "aliquotVolume": {
            "title": "The volume per aliquot (\u00b5L)",
            "type": "number",
            "minimum": 0,
            "brief": "volume",
            "units": "\u00b5L",
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The volume of each aliquot in micro liters."
            }
        }
    }
}
```

