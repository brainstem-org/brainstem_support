---
layout: default
title: Procedure types
parent: Schemas
grand_parent: Data model
nav_order: 4
---

# Procedure types
{: .no_toc}

Various procedure types are available for different experimental manipulations and interventions in neuroscience research.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Surgical Procedures

### Anesthesia

Administration of anesthetic agents to induce unconsciousness, sedation, or analgesia during experimental procedures.

| Field | Description |
|:------|:------------|
| `Anesthetic agent` | Required string. Options: Isoflurane, Sevoflurane, Ketamine, Ketamine + Xylazine, Ketamine + Dexmedetomidine, Pentobarbital, Urethane, Tribromoethanol (Avertin), Propofol, Other. Primary anesthetic agent used. |
| `Administration route` | Required string. Options: Inhalation, Intraperitoneal (IP), Intravenous (IV), Subcutaneous (SC), Intramuscular (IM), Oral, Other. Route of anesthetic administration. |
| `Dosage` | Optional string. Example: e.g., '2% in 10% oxygen', '100 mg/kg'. Dosage of the anesthetic agent (e.g., '2% in 10% oxygen', '100 mg/kg'). |
| `Anesthetic depth` | Optional string. Options: Light sedation, Moderate sedation, Deep sedation, Surgical plane, Other. Select the anesthetic depth achieved: • Light sedation: Minimal depression, animal is calm but responsive. • Moderate sedation: Reduced awareness, responds to strong stimuli. • Deep sedation: Unresponsive, diminished reflexes, not surgical depth. • Surgical plane: Full unconsciousness; no reaction to painful stimuli. • Other: Use if not fitting categories; specify in notes. |
| `Duration` | Optional number (≥ 0). Example: numeric. Duration of anesthesia. |
| `End of anesthesia` | Optional string; format time. Time when anesthesia ended. |
| `Complications` | Optional string; format textarea. Any complications or adverse events that occurred during anesthesia. |
| `Recovery time` | Optional number (≥ 0). Example: numeric. Time from end of anesthesia to return of righting reflex or normal activity. |
| `Monitoring methods` | Optional multi-select. Choices: Blood pressure, EEG, Heart rate, Pulse oximetry, Respiratory rate, Toe pinch reflex, None, Other. No duplicate selections. Methods used to monitor anesthetic depth. |
| `Supportive care` | Optional multi-select. Choices: Eye lubricant, Fluid therapy, Heating pad, Oxygen supplementation, None, Other. No duplicate selections. Supportive care provided during anesthesia. |

### Burr hole

A small circular hole drilled into the skull, often used for electrode insertion or to provide access for injections without removing a larger section of bone.

| Field | Description |
|:------|:------------|
| `Hole diameter` | Optional number (≥ 0). Example: numeric. Diameter of the burr hole. |
| `Purpose` | Optional string. Example: e.g., Electrode implantation, Access for injection. Primary purpose of creating the burr hole. |
| `Drill speed` | Optional number (≥ 0). Example: numeric. Speed of the drill in revolutions per minute. |
| `Cooling method` | Optional string. Options: Saline irrigation, Air cooling, None, Other. Method used to prevent overheating during drilling. |
| `Complications` | Optional string; format textarea. Any complications that occurred during the procedure, including bleeding, or damage to surrounding tissue. |

### Cranial window

A surgical procedure to create a transparent window in the skull, allowing for optical access to the brain for imaging or other experimental purposes.

| Field | Description |
|:------|:------------|
| `Surgical method` | Optional string. Example: e.g., 'surgical drill', 'bone saw', 'manual cutting'. Describe the surgical technique used to create the cranial window. Common methods include the use of a surgical drill, bone saw, automatic or manual cutting tools to remove a section of the skull. |
| `Shape of cranial window` | Optional string. Example: e.g., 'circular', 'square', 'elliptical'. Describe the shape of the cranial window performed, such as square, circular, elliptical, or other specific form. This helps in understanding the surgical approach and potential impact on the underlying brain tissue. |
| `Dimensions of cranial window` | Optional string. Example: e.g., '1.0 diameter × 4 length'. Dimensions of the window: length, width, diameter or thickness. |
| `Orientation of cranial window` | Optional string. Example: e.g., '45 degrees to the midline', 'parallel to the sagittal suture'. Describe the orientation of the cranial window relative to anatomical landmarks. This can include angle and direction, which are important for precise targeting and minimizing damage to critical areas. |

### Craniectomy

Involves the surgical removal of a portion of the skull to access the brain, without replacing the skull bone afterward. This procedure is often used in cases requiring prolonged brain access or to alleviate pressure after brain injury.

| Field | Description |
|:------|:------------|
| `Surgical method` | Optional string. Example: e.g., 'surgical drill', 'bone saw', 'manual cutting'. Describe the surgical technique used for the craniectomy. Common methods include the use of a surgical drill, bone saw, automatic or manual cutting tools to remove a section of the skull. |
| `Shape of craniectomy` | Optional string. Example: e.g., 'circular', 'square', 'oval', 'irregular'. Describe the shape of the craniectomy, such as square, circular, oval, or irregular. |
| `Dimensions of craniectomy` | Optional string. Example: e.g., '1.0 diameter × 4 length'. Dimensions of the craniectomy: length, width, or diameter. |
| `Orientation of craniectomy` | Optional string. Example: e.g., 'anterior-posterior', 'left-right', 'oblique'. Indicate the orientation of the craniectomy relative to major anatomical landmarks. |
| `Fatal outcome` | Optional boolean. Check this box if the craniectomy procedure results in a fatal outcome. |

### Craniotomy

A surgical procedure where part of the skull is temporarily removed to expose the brain for surgery or research purposes. The removed bone is typically replaced after the procedure, making it a temporary opening.

| Field | Description |
|:------|:------------|
| `Surgical method` | Optional string. Example: e.g., 'surgical drill', 'bone saw', 'manual cutting'. Describe the surgical technique used for the craniotomy. Common methods include the use of a surgical drill, bone saw, automatic or manual cutting tools to remove a section of the skull. |
| `Shape of craniotomy` | Optional string. Example: e.g., 'circular', 'square', 'elliptical'. Describe the shape of the craniotomy performed, such as square, circular, elliptical, or other specific form. This helps in understanding the surgical approach and potential impact on the underlying brain tissue. |
| `Dimensions of craniotomy` | Optional string. Example: e.g., '1.0 diameter × 4 length'. Dimensions of the craniotomy: length, width, or diameter. |
| `Orientation of craniotomy` | Optional string. Describe the orientation of the craniotomy relative to anatomical landmarks. This can include angle and direction, which are important for precise targeting and minimizing damage to critical areas. |
| `Fatal outcome` | Optional boolean. Check this box if the craniotomy procedure results in a fatal outcome. |

### Headcap

Installation of a protective cap or cover over the skull, typically made of dental cement or other materials, to protect cranial implants and provide a stable platform for repeated experimental sessions.

| Field | Description |
|:------|:------------|
| `Material` | Optional string. Example: e.g., 'dental cement', 'acrylic', 'epoxy', 'UV-cured resin', 'titanium', 'stainless steel', 'plastic'. Material used to build the headcap, e.g., dental cement, acrylic, epoxy, UV-cured resin, titanium, stainless steel, or plastic. |
| `Shape` | Optional string. Example: e.g., 'hexagonal', 'square', 'oval', 'cylinder'. Geometrical shape or design (e.g. hexagonal, square, oval, cylinder). |
| `Construction Method` | Optional string. Options: manually built, custom-built, 3D-printed, milled, molded, other. How the headcap was constructed. |
| `Attachment Method` | Optional string. Options: dental cement, UV-cured resin, super glue, epoxy, screws, other. Method used to affix the headcap to the skull. |
| `Faraday Shielding` | Optional string. Options: none, conductive paint, copper mesh, aluminum foil, custom, unknown. Whether and how the headcap was shielded to reduce electrical noise. |
| `Skull Preparation` | Optional string. Example: e.g., 'cleaned', 'roughened', 'dried'. How the skull was prepared (e.g., cleaned, roughened, dried) before attachment. |
| `Headcap ID` | Optional string. A unique identifier for the headcap. |

### Head fixation

The process of immobilizing the head during experimental procedures, typically using a headpost or other fixation device, to ensure stability during recordings or behavioral tasks.

| Field | Description |
|:------|:------------|
| `Fixation methods` | Optional multi-select. Choices: Ear bars, Nose clamp, Tooth bar, Headpost clamp, Custom holder, Other. No duplicate selections. Methods used to the fixate head, typically using a stereotaxic frame or custom apparatus. |
| `Alignment` | Optional string. Example: e.g. 'bregma and lambda aligned; slight ML tilt to the left'. The alignment achieved in the fixation procedure (e.g. bregma and lambda aligned; slight ML tilt to the left). |
| `Fixation details` | Optional string. Example: e.g. 'steel ear bars and ML adjustment screws - firm fit, no movement'. Further details on the fixation method used, including materials (e.g. 'steel ear bars and ML adjustment screws - firm fit, no movement'). |
| `Topical anesthesia` | Optional string. Example: e.g. Lidocaine gel, EMLA cream, None. Topical anesthetic used at fixation points (e.g. Lidocaine gel, EMLA cream, None). |

### Headpost

A small post or bar attached to the skull that allows for stable head fixation during experimental procedures, enabling precise positioning and reducing movement artifacts.

| Field | Description |
|:------|:------------|
| `Material` | Optional string. Example: e.g., titanium, stainless steel, plastic. Material of the headpost, e.g., titanium, stainless steel, or plastic. |
| `Shape` | Optional string. Example: e.g., flat bar, U-frame, circular post. Geometrical shape or design (e.g., flat bar, U-frame, circular post). |
| `Construction method` | Optional string. Options: manually built, custom-built, 3D-printed, milled, other. How the headpost was constructed prior to implantation. |
| `Attachment method` | Optional string. Options: dental cement, super glue, epoxy, screws, other. Method used to affix the headpost to the skull. |
| `Skull preparation` | Optional string. Example: e.g., cleaning, roughening, drying. How the skull was prepared (e.g., cleaning, roughening, drying) before attachment. |
| `Headpost ID` | Optional string. A unique identifier for the headpost. |

## Implant Procedures

### Blood pressure sensor implant

Implantation of a sensor to continuously monitor blood pressure, typically for cardiovascular or autonomic nervous system studies.

| Field | Description |
|:------|:------------|
| `Sensor type` | Required string. Options: telemetric, catheter-based, fluid-filled, fiber-optic, other. Type of blood pressure sensor used. |
| `Implant site` | Optional string. Example: e.g., 'Femoral artery', 'Carotid artery'. Vascular or body location where the pressure sensor was implanted — e.g., 'Femoral artery','Carotid artery','Aorta','Ventral tail artery','Left ventricle'. |
| `Catheter material` | Optional string. Example: e.g., polyurethane, silicone, polyethylene, PVC. Material used for the catheter or tubing connecting the pressure sensor to vasculature. |
| `Anchoring method` | Required string. Options: sutured, subcutaneous tunnel, tissue glue, headcap, cemented to skull, other. How the sensor or catheter were secured in place to prevent movement. |
| `Sterilization method` | Optional string. Options: Autoclave, Ethylene Oxide, Alcohol, Gamma Irradiation, None. Sterilization technique used before implantation. |

### Breathing sensor implant

Implantation of a sensor to monitor respiratory patterns, useful for studying respiratory control or as a physiological monitoring tool.

| Field | Description |
|:------|:------------|
| `Sensor type` | Required string. Options: Piezoelectric sensor, Chest wall EMG, Intranasal thermocouple, Intranasal pressure sensor, Tracheal airflow sensor, Thoracic pressure sensor, Plethysmography cannula, Other. Type of breathing sensor used. |
| `Implant site` | Optional string. Example: e.g., Chest wall, Diaphragm, Nasal cavity. Anatomical location where the breathing sensor was implanted or attached — e.g., 'Chest wall', 'Diaphragm', 'Nasal cavity', 'Trachea', 'Pleural cavity', 'Subcutaneous (telemetry)', 'Other'. |
| `Wire or lead material` | Optional string. Example: e.g., stainless steel, silver, silver chloride, platinum, tungsten. Material used for connecting wires or leads (e.g., stainless steel, silver, silver chloride, platinum, tungsten). |
| `Anchoring method` | Required string. Options: sutured, tissue glue, subcutaneous tunnel, cemented to skull, headcap, custom mount, other. How the sensor or wires were fixed in place during implantation. |
| `Signal transmission` | Optional string. Options: tethered, wireless, telemetric, inductive, optical, other. Mode of signal transmission from the sensor to the acquisition device. |
| `Sterilization method` | Optional string. Options: Autoclave, Ethylene Oxide, Alcohol, Gamma Irradiation, None. Sterilization technique applied before implantation. |

### Catheter implant

Insertion of a catheter for drug delivery, fluid administration, or sampling of biological fluids.

| Field | Description |
|:------|:------------|
| `Target site` | Required string. Options: jugular vein, femoral vein, carotid artery, lateral ventricle, third ventricle, spinal cord (intrathecal), cisterna magna, peritoneal cavity, other. Anatomical target of the catheter. |
| `Catheter type` | Optional string. Example: e.g., PE-10, Silastic. Model or description of the catheter (e.g., PE-10, Silastic). |
| `Material` | Optional string. Example: e.g., PE (polyethylene), silicone, Teflon, polyurethane. Material of the catheter tubing. |
| `Purpose` | Optional string. Options: infusion, sampling, pressure monitoring, drug delivery, other. Primary purpose of the catheter implant. |
| `Fixation method` | Optional string. Options: sutures, dental cement, epoxy, tissue glue, tunneled subcutaneously, other. How the catheter was secured to the body or skull. |
| `External port` | Optional string. Options: head-mounted, back-mounted, tail-mounted, subcutaneous, none. Where the external port or connector was positioned. |
| `Catheter ID` | Optional string. Unique identifier if the catheter is tracked as a physical resource. |

### ECG implant (Electrocardiography)

Implantation of electrodes for recording electrical activity of the heart, used for cardiac monitoring during experiments.

| Field | Description |
|:------|:------------|
| `Wire count` | Optional integer (≥ 1). Example: integer. Number of ECG wires implanted. |
| `Wire material` | Optional string. Example: e.g., stainless steel, silver chloride, platinum, gold. Material used for ECG wire leads. |
| `Wire insulation type` | Optional string. Options: Teflon, polyimide, silicone, none, other. Insulation material covering the wire shaft, excluding the exposed recording tip. |
| `Implant site` | Optional string. Example: e.g., 'chest wall', 'right shoulder', 'left hindlimb', 'subcutaneous over heart'. Where the ECG electrodes were implanted — e.g., 'chest wall', 'right shoulder', 'left hindlimb', or 'subcutaneous over heart'. |
| `Anchoring method` | Required string. Options: sutured, subcutaneous tunnel, tissue glue, headcap, cemented to skull, other. How the ECG wires were fixed in place to prevent movement. |
| `Sterilization method` | Optional string. Options: Autoclave, Ethylene Oxide, Alcohol, Gamma Irradiation, None. Sterilization technique used for ECG components. |

### EEG implant (Electroencephalography)

Implantation of electrodes on or beneath the skull to record brain electrical activity, commonly used for sleep studies, seizure monitoring, and brain state analysis.

| Field | Description |
|:------|:------------|
| `Wire count` | Required integer (≥ 1); default 1. Example: integer. Number of electrodes used for EEG recording. |
| `Electrode type` | Required string. Options: skull screw, flat wire, disc, custom, other. Form factor of the EEG electrode, e.g., skull screws or flat metal contacts. |
| `Electrode material` | Required string. Example: e.g., stainless steel, silver chloride, platinum, gold, tungsten. Material used in the electrode. Common choices include stainless steel and Ag/AgCl. |
| `Referencing scheme` | Optional string. Options: single reference, common average, bipolar, differential, other. Type of referencing used in the EEG setup. |
| `Anchoring method` | Required string. Options: dental cement, screws, acrylic, UV-cured resin, headcap, other. How the EEG electrodes were secured in place. |
| `Faraday shielding` | Optional string. Options: none, copper mesh, conductive paint, aluminum foil, headcap integrated, other. Whether and how the EEG implant was shielded from external noise. |
| `Sterilization method` | Optional string. Options: Autoclave, Ethylene Oxide, Alcohol, Gamma Irradiation, None. How the EEG components were sterilized before implantation. |

### EMG implant (Electromyography)

Implantation of electrodes in muscles to record electrical activity associated with muscle contraction, used for motor control studies.

| Field | Description |
|:------|:------------|
| `Wire count` | Required integer (≥ 1); default 1. Example: integer. Number of implanted EMG wires (typically one or two per muscle). |
| `Wire material` | Optional string. Example: e.g., stainless steel, silver, platinum, nichrome. Material used for the EMG wires. Stainless steel is common in rodents. |
| `Wire insulation type` | Optional string. Options: Teflon, polyimide, silicone, none, other. Type of insulation around the wire shaft, except at exposed recording tip. |
| `Target muscles` | Optional string. Example: e.g., neck, diaphragm, masseter, forelimb biceps. List of muscles where EMG wires were implanted (e.g., neck, diaphragm, masseter, forelimb biceps). |
| `Implant method` | Required string. Options: direct insertion, needle-guided, tunneled subcutaneously, sutured, other. How the wire was placed into the muscle. |
| `Anchoring method` | Optional string. Options: sutured to muscle, cemented to skull, subcutaneous tunnel, tissue glue, headcap, other. How the wires were fixed to prevent displacement during recovery or recording. |
| `Sterilization method` | Optional string. Options: Autoclave, Ethylene Oxide, Alcohol, Gamma Irradiation, None. Sterilization technique applied before implantation. |

### GRIN (Gradient Index) lens implant

Implantation of a gradient index lens, typically used for deep brain calcium imaging in combination with miniature microscopes.

| Field | Description |
|:------|:------------|
| `Lens tip type` | Optional string. Example: e.g., flat, ground, polished, beveled. Describe the shape of the GRIN lens tip. Common values: flat, ground, polished, beveled. |
| `Lens ID` | Optional string. Unique identifier or batch number of the GRIN lens. The physical lens is tracked as a consumable. |
| `Sterilization method` | Optional string. Options: Autoclave, Ethylene Oxide, Gamma Irradiation, Alcohol, None. Method used to sterilize the GRIN lens before implantation. |
| `Mounting method` | Optional string. Options: Cement only, Cement + baseplate, Headcap integrated, Custom holder, Other. How the GRIN lens was secured in place after implantation. |

### Nerve cuff implant

Placement of a cuff electrode around a peripheral nerve for stimulation or recording of neural activity.

| Field | Description |
|:------|:------------|
| `Cuff type` | Required string. Options: monopolar, bipolar, tripolar, multi-contact, split-ring, spiral, other. Configuration and geometry of the cuff. Common types include bipolar and tripolar configurations. |
| `Target nerve` | Optional string. Example: e.g., sciatic, vagus, median. Name or anatomical label of the nerve the cuff was implanted on (e.g., 'sciatic', 'vagus', 'median', 'hypoglossal'). |
| `Cuff material` | Optional string. Example: e.g., silicone, polyimide, PDMS, polyurethane. Base material used for the body of the nerve cuff (e.g., silicone tubing or flexible polymer). |
| `Electrode material` | Optional string. Example: e.g., platinum, platinum-iridium, silver, stainless steel. Material of the embedded electrode contacts inside the nerve cuff. |
| `Anchoring method` | Required string. Options: suture to surrounding tissue, tissue glue, self-closing cuff, non-anchored (loose fit), subcutaneous tunnel, other. How the cuff was fixed around or near the nerve to prevent displacement. |
| `Wire exit route` | Optional string. Options: subcutaneous tunnel to headcap, abdominal connector, dorsal skin exit, wireless/inductive, other. How the lead wires exited the body or were routed for connection to recording/stimulation equipment. |
| `Signal transmission` | Optional string. Options: tethered, wireless, telemetric, optical, none, other. How the signal was transmitted to external devices (e.g., via headstage cable, telemetry). |
| `Sterilization method` | Optional string. Options: Autoclave, Ethylene Oxide, Alcohol, Gamma Irradiation, None. Sterilization technique used prior to implantation. |

### Optic fiber implant

Involves the surgical implantation of an optic fiber into the brain, often used in optogenetics research to manipulate or record neuronal activity with light.

| Field | Description |
|:------|:------------|
| `Fiber tip shape` | Optional string. Example: e.g., flat, angled, rounded. Specify the shape of the tip. Common shapes include flat, angled, or rounded. |
| `Fiber ID` | Optional string. A unique identifier for the optic fiber. |
| `Sterilization method` | Optional string. Options: Autoclave, Ethylene Oxide, Gamma Irradiation, Alcohol, None. Sterilization method for ensuring the implant is safe for implantation. |

### Prism implant

Implantation of a prism for optical access to brain regions that are difficult to image directly, used in imaging studies.

| Field | Description |
|:------|:------------|
| `Prism ID` | Optional string. Unique identifier for the physical prism (e.g., serial number or batch). The prism itself is tracked as a consumable. |
| `Sterilization method` | Optional string. Options: Autoclave, Ethylene Oxide, Gamma Irradiation, Alcohol, None. Method used to sterilize the prism before implantation. |
| `Mounting method` | Optional string. Options: Cement only, Cement + baseplate, Headcap integrated, Custom holder, Other. How the prism was secured in place after implantation. |

### Reference electrode implant

Implantation of a reference electrode used as a voltage reference point for electrophysiological recordings.

| Field | Description |
|:------|:------------|
| `Electrode count` | Required integer (≥ 1); default 1. Example: integer. Number of electrodes in the reference electrode assembly. Typically 1, but multiple electrodes may be used for redundancy or averaging. |
| `Electrode material` | Required string; default stainless steel. Example: e.g., stainless steel, silver chloride, platinum, gold, tungsten. Material of the electrode. Common choices include stainless steel and silver chloride. This influences biocompatibility and stability of reference signals. |
| `Electrode diameter` | Optional number (≥ 0). Example: numeric. Diameter of electrode. Affects flexibility, durability, and impedance. |
| `Impedance` | Optional number (≥ 0). Example: numeric. Approximate impedance of the reference electrode at 1 kHz. Lower is typically preferred for stable referencing. |
| `Placement site` | Optional string. Example: e.g., cerebellum, skull surface, contralateral cortex, subcutaneous. Where the reference electrode was implanted or placed (e.g., cerebellum, skull surface, contralateral cortex, subcutaneous). |
| `Anchoring method` | Optional string. Options: dental cement, tissue glue, bone screw, subcutaneous tunnel, other. How the reference electrode was secured in place. |
| `Sterilization method` | Optional string. Options: Autoclave, Ethylene Oxide, Gamma Irradiation, Alcohol, None. Sterilization method used before implantation. Important for reducing infection risk without degrading the electrode. |

### Silicon probe implant

Involves the implantation of a silicon probe, a device equipped with multiple recording sites, into the brain. Silicon probes are used for high-density recording of neural activity.

| Field | Description |
|:------|:------------|
| `Probe ID` | Optional string. A unique identifier for the silicon probe. |
| `Sterilization method` | Optional string. Options: Autoclave, Ethylene Oxide, Gamma Irradiation, Alcohol, None. Suitable sterilization technique for ensuring the electrode is safe for implantation. |

### Single wire electrode implant

Refers to the implantation of a single wire electrode into the brain, used for recording electrical activity from or stimulating specific neurons or brain areas.

| Field | Description |
|:------|:------------|
| `Wire count` | Required integer (≥ 0); default 1. Example: integer. Number of wires used in the electrode assembly. |
| `Wire diameter` | Optional number (≥ 0). Example: numeric. The diameter of the electrode wire. Wire diameter affects the electrode's impedance and recording or stimulation capabilities. |
| `Wire material` | Optional string. Example: e.g., stainless steel, platinum, gold. Common materials include stainless steel, platinum-iridium, and gold. Material choice affects biocompatibility, conductivity, and overall performance of the electrode. |
| `Impedance` | Optional number. Example: numeric. The electrical impedance of the electrode, critical for matching with recording equipment and optimizing signal-to-noise ratio. |
| `Sterilization method` | Optional string. Options: Autoclave, Ethylene Oxide, Gamma Irradiation, Alcohol, None. Choose suitable sterilization technique for ensuring the electrode is safe for implantation without damaging its integrity. |

### Temperature sensor implant

Implantation of a temperature sensor for monitoring body or brain temperature during experiments.

| Field | Description |
|:------|:------------|
| `Sensor type` | Required string. Options: thermocouple, thermistor, digital IC, telemetric sensor, logger (passive), fiber-optic, other. Type of temperature sensor implanted. Examples include thermocouples, telemetry sensors, or passive loggers. |
| `Wire or lead material` | Optional string. Example: e.g., copper, constantan, platinum, stainless steel. Material of the sensor leads, if applicable. Thermocouples often use copper or constantan. |
| `Anchoring method` | Required string. Options: sutured, tissue glue, subcutaneous tunnel, cemented to skull, headcap, free-floating, other. How the sensor or wires were secured at the implantation site. |
| `Signal transmission` | Optional string. Options: tethered, wireless, telemetric, optical, logger (retrieved), none, other. How temperature data is retrieved. 'Logger (retrieved)' refers to onboard storage until post hoc download. |
| `Power source` | Optional string. Options: battery, inductive, wired, passive, none, other. How the temperature sensor is powered, if applicable. |
| `Sterilization method` | Optional string. Options: Autoclave, Ethylene Oxide, Alcohol, Gamma Irradiation, None. Sterilization technique used before implantation. |

### Tetrode wire electrode implant

The implantation of a tetrode, a device made of four intertwined wire electrodes, into the brain. Tetrodes allow for the recording of electrical signals from multiple neurons simultaneously.

| Field | Description |
|:------|:------------|
| `Tetrode count` | Required integer (≥ 0); default 1. Example: integer. Number of tetrodes in the assembly. Each tetrode is typically used to record from different brain regions or to provide redundancy and spatial resolution in neural recordings. |
| `Wires per tetrode` | Optional integer (≥ 0); default 4. Example: integer. Number of wires that make up each tetrode. Standard tetrodes consist of four wires twisted together, which allows for precise spatial discrimination of neuronal signals. |
| `Wire diameter` | Optional number (≥ 0). Example: numeric. The diameter of each wire. This affects the impedance of the electrode and is crucial for determining the quality and sensitivity of the recordings. |
| `Wire material` | Optional string. Example: e.g., stainless steel, platinum, nichrome. Material used for the wires. Common materials include platinum-iridium, stainless steel, and nichrome. The choice of material affects the durability, flexibility, and biocompatibility of the electrode. |
| `Sterilization method` | Optional string. Options: Autoclave, Ethylene Oxide, Gamma Irradiation, Alcohol, None. Choose suitable sterilization technique for ensuring the electrode is safe for implantation without damaging its integrity. |

### Generic implant

A flexible procedure type for implants that don't fit into other specific categories, allowing custom documentation of various implant types.

| Field | Description |
|:------|:------------|
| `Implant type` | Required string. Options: sensor, electrode, optical device, mechanical device, fluidic device, structural support, other. General category or function of the implant. This helps classify the implant for downstream filtering and interpretation. |
| `Implant name or description` | Optional string. A short name or description of the implant (e.g., 'custom probe', 'prototype sensor', 'flex circuit'). |
| `Anchoring method` | Optional string. Options: sutured, tissue glue, subcutaneous tunnel, dental cement, headcap, custom mount, none, other. How the implant was secured in place. |
| `Signal transmission` | Optional string. Options: tethered, wireless, telemetric, optical, none, other. How the implant communicates data (if applicable). |
| `Power source` | Optional string. Options: battery, inductive, wired, passive, none, other. How the implant is powered, if relevant. |
| `Sterilization method` | Optional string. Options: Autoclave, Ethylene Oxide, Alcohol, Gamma Irradiation, None. Sterilization technique used prior to implantation. |

## Injection and Infusion Procedures

### Injection

General injection procedure for administering substances into the brain or body, with various routes of administration available.

| Field | Description |
|:------|:------------|
| `Injection volume` | Optional number (≥ 0). Example: numeric. The total volume of the solution to be injected. |
| `Injection rate` | Optional number (≥ 0). Example: numeric. Rate at which the solution is injected. |
| `Injection Method` | Optional string. Options: Intracerebroventricular (ICV), Intramuscular (IM), Intravenous (IV), Intradermal (ID), Subcutaneous (SC), Intracardiac (IC), Intraperitoneal (IP), Intrathecal (IT), Epidural, Retro-orbital (RO), Intranasal (IN), Intra-articular, Intravitreal, Intralesional. Defines the injection method. |
| `Concentration of solution` | Optional number (≥ 0). Example: numeric. The concentration of the injected solution. Enter only if the concentration differs from the concentration of the solution. |
| `Injection profile` | Optional string. Options: Bolus Injection, Continuous Infusion, Tapered Dose, Intermittent Bolus, Staggered Injection, Ramp Infusion, Burst Infusion, Step Infusion, Layered Dosing, Titration. Describes the injection profile. |
| `Injection side (brain hemisphere or body side)` | Optional string. Options: Left, Right, Midline, Unknown. Which side of the brain or body the injection targets. |

### Virus injection

Involves injecting a virus into the brain, typically to deliver genetic material for research purposes, such as gene therapy experiments or to manipulate gene expression in specific brain regions. Typically performed with a small glass capillary.

| Field | Description |
|:------|:------------|
| `Injection volume` | Optional number (≥ 0). Example: numeric. The total volume of the viral solution to be injected. |
| `Injection rate` | Optional number (≥ 0). Example: numeric. Rate at which the viral solution is injected. Controlling the injection rate is essential for preventing tissue damage and ensuring uniform distribution of the virus. |
| `Titer of virus solution` | Optional number (≥ 0). Example: numeric. The titer of the injected virus solution. Enter only if the titer differs from the titer of the virus solution. |
| `Titer unit of virus solution` | Optional string. Options: vg/mL, TU/mL, pfu/mL. vg/mL: Viral genomes; TU/mL: Transducing units; pfu/mL: Plaque forming units. |
| `Injection profile` | Optional string. Options: Bolus Injection, Continuous Infusion, Tapered Dose, Intermittent Bolus, Staggered Injection, Ramp Infusion, Burst Infusion, Step Infusion, Layered Dosing, Titration. Describes the injection profile of the virus delivery. |

## Brain and Tissue Procedures

### Brain extraction

Removal of the brain from the skull, typically performed post-mortem for ex vivo analysis, tissue processing, or histological examination.

| Field | Description |
|:------|:------------|
| `Extraction method` | Required string. Options: Complete removal, Partial removal, Sectional removal, Other. Method used for brain extraction. |
| `Time to extraction` | Optional number (≥ 0). Example: numeric. Time from euthanasia to brain extraction. Important for tissue quality. |
| `Preservation method` | Required string. Options: Fresh (immediate use), Paraformaldehyde fixation, Formalin fixation, Flash freezing, Liquid nitrogen, Dry ice, Other. Method used to preserve the extracted brain tissue. |
| `Fixation duration` | Optional number (≥ 0). Example: numeric. Duration of fixation (if applicable). |
| `Storage Conditions` | Optional string. Example: e.g., 'Room temp', '4°C', 'Protect from light'. E.g., 'Room temp', '4°C', 'Protect from light'. |
| `Brain weight` | Optional number (≥ 0). Example: numeric. Weight of the extracted brain. |

### Brain lesion

A surgical procedure that intentionally damages or destroys brain tissue to study the functions of specific brain areas. Lesions can help identify the roles of different brain regions in behavior and cognition.

| Field | Description |
|:------|:------------|
| `Lesion method` | Optional string. Example: e.g., surgical, suction, chemical, thermal. Specify the technique used to induce the brain lesion (e.g., surgical, suction, chemical, thermal, etc.). |
| `Volume of brain lesion` | Optional number (≥ 0). Example: numeric. Enter the estimated or calculated volume of the brain lesion. |
| `Fatal outcome` | Optional boolean. Check this box if the lesion results in a fatal outcome. |

### Brain slice

Refers to ex vivo preparations obtained by sectioning brain tissue into thin slices. These slices are used for various types of experiments, including electrophysiological recordings and pharmacological studies.

| Field | Description |
|:------|:------------|
| `Thickness of slices` | Required number (≥ 0); default 50. Example: numeric. The thickness of the brain slices. Thinner slices are typically used for imaging purposes, while thicker slices may be used for electrophysiological recordings. |
| `Number of slices` | Optional integer (≥ 0). Example: integer. Total number of slices obtained from the brain tissue. |
| `Orientation of slices` | Required string; default coronal. Options: coronal, sagittal, horizontal. The orientation of the slices, such as coronal, sagittal, or horizontal. This determines the plane of sectioning relative to the brain's anatomical structure. |
| `Medium used for slice` | Optional string. Example: e.g., aCSF, preservation solution. The medium in which the brain slices are preserved or maintained during and after slicing. Common mediums include artificial cerebrospinal fluid (aCSF) or specific preservation solutions. |
| `Vibratome blade angle` | Optional number (≥ 0). Example: numeric. The angle at which the vibratome blade is set to slice the brain tissue. Proper blade angle helps in achieving clean and precise cuts. |

### Cryosectioning

Sectioning of frozen tissue using a cryostat, commonly used for preparing tissue sections for histology, immunohistochemistry, or in situ hybridization.

| Field | Description |
|:------|:------------|
| `Section thickness` | Required number (≥ 0); default 40. Example: numeric. Thickness of each section. |
| `Cutting temperature` | Required number; default 0. Example: numeric. Temperature at which sectioning was performed. |
| `Embedding medium` | Optional string. Options: OCT compound, Tissue-Tek, Cryomatrix, Gelatin, None, Other. Medium used to embed the tissue for sectioning. |
| `Sectioning orientation` | Required string. Options: Coronal, Sagittal, Horizontal, Other. Anatomical plane of sectioning. |
| `Number of sections` | Optional number (≥ 0). Example: numeric. Total number of sections obtained. |
| `Serial sectioning` | Optional boolean. Check if sections were collected serially (every section saved). |
| `Section interval` | Optional number (≥ 1). Example: e.g., 1 for every section, 3 for every 3rd section. Interval for section collection (e.g., 1 = every section, 3 = every 3rd section). |
| `Section storage method` | Optional string. Options: Mounted on slides, Free-floating in solution, Stored in plates, Other. Method used to store the sections after cutting. |
| `Storage buffer/solution` | Optional string. Example: e.g., PBS, cryoprotectant solution. Buffer or solution used to store sections. |

### Perfusion fixation

A technique for preserving brain tissue where a fixative solution is pumped through the circulatory system to stabilize and preserve tissue structure. This method is essential for preparing brain specimens for microscopic examination.

| Field | Description |
|:------|:------------|
| `Perfusion method` | Optional string. Example: e.g., transcardial, intracardiac, intracranial. Describe the perfusion method used for fixation. |
| `Perfusion volume` | Optional number (≥ 0). Example: numeric. Specify the total volume of fixative solution used. Adequate volume ensures complete perfusion and fixation of brain tissue, which is critical for preserving tissue architecture and molecular integrity. |
| `Fatal outcome` | Optional boolean. Check this box if the perfusion method results in a fatal outcome for the subject. |

### Tissue clearing

Chemical treatment of tissue to make it optically transparent, allowing for deep imaging of intact tissue samples without physical sectioning.

| Field | Description |
|:------|:------------|
| `Clearing method` | Required string. Options: CLARITY, CUBIC, 3DISCO, iDISCO+, PACT, ScaleS, SeeDB, BABB (Benzyl alcohol/Benzyl benzoate), Passive CLARITY, Other. Tissue clearing protocol used. |
| `Tissue type` | Optional string. Example: e.g., 'Whole brain', 'Brain slice', 'Spinal cord'. Type of tissue being cleared. |
| `Fixation time` | Optional number (≥ 0). Example: numeric. Duration of tissue fixation before clearing. |
| `Clearing duration` | Optional number (≥ 0). Example: numeric. Total time required for tissue clearing. |
| `Clearing temperature` | Optional number. Example: e.g., 37, 25. Temperature at which clearing was performed. |
| `Agitation method` | Optional string. Options: Gentle shaking, Rotation, Static, Other. Method of agitation during clearing process. |
| `Refractive index matching solution` | Optional string. Example: e.g., DBE, BABB, 2,2'-thiodiethanol. Solution used for final refractive index matching. |
| `Transparency achieved` | Optional string. Options: Complete, Partial, Poor, Failed. Level of tissue transparency achieved. |
| `Imaging compatible` | Optional boolean. Check if tissue is suitable for subsequent imaging. |
| `Complications/Issues` | Optional string; format textarea. Any issues encountered during the clearing process. |

### Vibratome sectioning

Sectioning of live or fixed brain tissue using a vibrating blade (vibratome), producing relatively thick sections that maintain better tissue integrity than other sectioning methods.

| Field | Description |
|:------|:------------|
| `Section thickness` | Optional number (≥ 0). Example: numeric. Thickness of each section. |
| `Blade type` | Required string. Options: Disposable razor blade, Steel blade, Ceramic blade, Sapphire blade, Other. Type of blade used for sectioning. |
| `Cutting speed` | Optional string. Options: Very slow, Slow, Medium, Fast, Very fast. Speed setting for the vibratome blade. |
| `Vibration frequency` | Optional number (≥ 0). Example: numeric. Vibration frequency of the blade. |
| `Vibration amplitude` | Optional string. Options: Minimum, Low, Medium, High, Maximum. Amplitude setting for blade vibration. |
| `Sectioning orientation` | Optional string. Options: Coronal, Sagittal, Horizontal, Other. Anatomical plane of sectioning. |
| `Cutting buffer` | Optional string. Example: e.g., ACSF, PBS, Tris buffer. Buffer solution used during sectioning. |
| `Buffer temperature` | Optional number. Example: e.g., 4, 23. Temperature of the cutting buffer. |
| `Number of sections` | Optional number (≥ 0). Example: numeric. Total number of sections obtained. |
| `Section quality` | Optional string. Options: Excellent, Good, Fair, Poor. Overall quality of the sections obtained. |
| `Section storage method` | Optional string. Options: Free-floating in buffer, Mounted immediately, Stored in multiwell plates, Other. Method used to store sections after cutting. |

## Endpoint Procedures (Euthanasia)

### Cervical dislocation

A physical method of euthanasia that causes rapid loss of consciousness and death by dislocating the cervical vertebrae, disrupting the spinal cord and blood flow to the brain.

| Field | Description |
|:------|:------------|
| `Method of dislocation` | Required string. Options: Manual, Mechanical device, Scissor method, Other. Method used for cervical dislocation. |
| `Anesthetic agent (if used)` | Optional string. Example: e.g., CO₂, isoflurane. Anesthetic agent used prior to euthanasia (if applicable). |
| `Confirmation of death` | Required multi-select. Choices: Absence of heartbeat, Absence of breathing, Absence of reflexes, Fixed dilated pupils, Loss of corneal reflex, Other. No duplicate selections. Methods used to confirm death. |
| `Complications` | Optional string; format textarea. Any complications or issues encountered during the procedure. |

### Decapitation

Rapid separation of the head from the body, typically performed under anesthesia, for procedures requiring immediate brain extraction or tissue preservation.

| Field | Description |
|:------|:------------|
| `Decapitation Method` | Required string. Options: Guillotine, Sharp scissors, Surgical blade, Other. Method/instrument used for decapitation. |
| `Anesthetic agent (if used)` | Optional string. Example: e.g., CO₂, isoflurane, ketamine. Anesthetic agent used prior to euthanasia (if applicable). |
| `Complications` | Optional string; format textarea. Any complications or issues encountered during the procedure. |

### CO₂ chamber euthanasia

Euthanasia by gradual exposure to carbon dioxide gas, which induces loss of consciousness followed by death through hypoxia.

| Field | Description |
|:------|:------------|
| `CO₂ concentration` | Required number (≥ 0, ≤ 100); default 30. Example: e.g., 30% or 70%. Concentration of CO₂ used in the chamber. |
| `CO₂ flow rate` | Optional number (≥ 0). Example: numeric. Rate of CO₂ flow into the chamber. |
| `Gradual CO₂ introduction` | Optional boolean. Check if CO₂ was introduced gradually (recommended for animal welfare). |
| `Chamber prefilling` | Optional string. Options: Not prefilled, Partially prefilled, Fully prefilled, Other. Method of chamber prefilling with CO₂. |
| `Exposure duration` | Required number (≥ 0); default 5. Example: numeric. Duration of CO₂ exposure. |
| `Time to unconsciousness` | Optional number (≥ 0). Example: numeric. Observed time to loss of consciousness. |
| `Confirmation of death` | Required multi-select. Choices: Absence of heartbeat, Absence of breathing, Absence of reflexes, Fixed dilated pupils, Loss of corneal reflex, Continued CO₂ exposure, Other. No duplicate selections. Methods used to confirm death. |
| `Chamber volume` | Optional number (≥ 0). Example: numeric. Volume of the euthanasia chamber. |

### Barbiturate injection

Administration of an overdose of barbiturate anesthetic, typically pentobarbital, causing rapid loss of consciousness followed by respiratory and cardiac arrest.

| Field | Description |
|:------|:------------|
| `Barbiturate type` | Required string. Options: Pentobarbital, Phenobarbital, Secobarbital, Barbital, Commercial euthanasia solution, Other. Type of barbiturate used for euthanasia. |
| `Concentration` | Optional number (≥ 0). Example: numeric. Concentration of the barbiturate solution. |
| `Dosage` | Optional number (≥ 0). Example: numeric. Dosage administered per kilogram of body weight. |
| `Administration route` | Required string. Options: Intraperitoneal (IP), Intravenous (IV), Intracardiac, Subcutaneous (SC), Other. Route of barbiturate administration. |
| `Volume administered` | Optional number (≥ 0). Example: numeric. Total volume of barbiturate solution administered. |
| `Sedation agent (if used)` | Optional string. Example: e.g., ketamine, isoflurane. Sedation agent used prior to euthanasia (if applicable). |
| `Time to unconsciousness` | Optional number (≥ 0). Example: numeric. Observed time to loss of consciousness. |
| `Confirmation of death` | Required multi-select. Choices: Absence of heartbeat, Absence of breathing, Absence of reflexes, Fixed dilated pupils, Loss of corneal reflex, Additional dose administered, Other. No duplicate selections. Methods used to confirm death. |

### Inhalant overdose

Euthanasia through administration of an overdose of volatile anesthetic agents such as isoflurane or sevoflurane.

| Field | Description |
|:------|:------------|
| `Anesthetic agent` | Optional string. Options: Isoflurane, Sevoflurane, Halothane, Desflurane, Enflurane, Other. Inhalant anesthetic used for overdose euthanasia. |
| `Concentration` | Optional number (≥ 0, ≤ 100). Example: e.g., 5-8. Concentration of anesthetic agent used. |
| `Delivery method` | Optional string. Options: Anesthesia chamber, Nose cone, Intubation, Bell jar, Other. Method used to deliver the anesthetic agent. |
| `Oxygen flow rate` | Optional number (≥ 0). Example: numeric. Flow rate of oxygen carrier gas. |
| `Exposure duration` | Optional number (≥ 0). Example: numeric. Duration of anesthetic exposure. |
| `Time to unconsciousness` | Optional number (≥ 0). Example: numeric. Observed time to loss of consciousness. |
| `Sedation agent (if used)` | Optional string. Example: e.g., CO₂, ketamine. Sedation agent used prior to inhalant overdose (if applicable). |
| `Confirmation of death` | Optional multi-select. Choices: Absence of heartbeat, Absence of breathing, Absence of reflexes, Fixed dilated pupils, Loss of corneal reflex, Continued anesthetic exposure, Other. No duplicate selections. Methods used to confirm death. |

## Abstract Procedures

These procedures represent experimental manipulations and stimulations rather than surgical interventions.

### Auditory stimulation

Presentation of sound stimuli during experiments, used for studying auditory processing, attention, or behavior.

| Field | Description |
|:------|:------------|
| `Stimulus types` | Required multi-select. Choices: Tone, Click, White noise, Pink noise, Frequency sweep, Amplitude modulated, Pulse train, Chirp, Other. No duplicate selections. Types of auditory stimuli used in this paradigm. Select one or more. |
| `Delivery method` | Optional string. Options: Free-field speaker, In-ear speaker, Bone conduction, Headphone, Other. How the sound was delivered to the subject. Free-field speakers are most common in head-fixed setups. |
| `Stimulation context` | Optional string. Options: Passive, Behavioral task, Closed-loop, Anesthetized, Free behavior. Experimental context in which auditory stimulation was delivered. |
| `Paradigm description` | Optional string; format textarea. Free-text description of the auditory stimulation paradigm: include stimulus timing, repetitions, device setup, etc. |

### Behavioral tracking

Monitoring and recording of animal behavior, position, or movement during experimental sessions.

| Field | Description |
|:------|:------------|
| `Tracking Method` | Optional string. Options: Markerless, Marker-based, Hybrid, Manual scoring. The tracking method. |
| `Tracked Features` | Optional multi-select. Choices: Full body, Head position, Head direction, Limbs, Paws, Tail, Eyes, Whiskers, Markers, Rigid body, Other. No duplicate selections. Body features being tracked. |

### Odor stimulation

Delivery of odorants for studying olfactory processing, learning, or odor-guided behavior.

| Field | Description |
|:------|:------------|
| `Odorants used` | Optional string. Example: e.g., isoamyl acetate, limonene, mineral oil control. List the names or identifiers of odorants used in the stimulation paradigm (e.g., isoamyl acetate, limonene, mineral oil control). |
| `Delivery method` | Optional string. Options: Olfactometer, Manually pipetted, Syringe injection, Headspace exposure, Cotton swab, Other. How the odor was delivered to the subject. Use 'Olfactometer' for computer-controlled systems. |
| `Carrier gas` | Optional string. Options: Air, O₂, N₂, CO₂, Other. Type of gas used to carry the odorant into the delivery stream (if applicable). |
| `Stimulation context` | Optional string. Options: Passive, Behavioral task, Closed-loop, Anesthetized, Free behavior. Experimental context in which odor stimulation occurred. |
| `Paradigm description` | Optional string; format textarea. Free-text description of the stimulation paradigm, including stimulus timing, delivery parameters, and experimental goals. |

### Tactile stimulation

Application of touch or mechanical stimuli to study somatosensory processing or behavior.

| Field | Description |
|:------|:------------|
| `Stimulation types` | Required multi-select. Choices: Whisker poke, Whisker deflection, Air puff, Brush, Vibration, Pressure pad, Cotton swab, Other. No duplicate selections. Select the types of tactile stimuli used in the paradigm. Multiple types can be listed if applicable. |
| `Stimulation site` | Optional string. The anatomical region where tactile stimuli were applied (e.g., 'whisker pad', 'hindpaw', 'tail'). |
| `Delivery method` | Optional string. Options: Manual (e.g., cotton swab), Piezo actuator, Solenoid piston, Air puff system, Brush or probe, Other. The method or device used to deliver the tactile stimulus to the subject. |
| `Stimulation context` | Optional string. Options: Passive, Behavioral task, Closed-loop, Anesthetized, Free behavior. Experimental context in which tactile stimulation occurred. |
| `Paradigm description` | Optional string; format textarea. Free-text description of the tactile stimulation paradigm, including stimulus timing, frequency, devices used, and behavioral conditions. |

### Visual stimulation

Presentation of visual stimuli during experiments, used for studying visual processing, attention, or visually guided behavior.

| Field | Description |
|:------|:------------|
| `Stimulus types` | Required multi-select. Choices: Gratings, Natural images, LED flashes, Checkerboard, Full-field flashes, Moving bars, Flicker, Other. No duplicate selections. Select the visual stimulus types used in this paradigm. Multiple types may be selected. |
| `Presentation device` | Optional string. Options: Monitor, LED panel, Projector, Head-mounted display, Fiber-coupled light source, Other. Device or method used to present the visual stimuli to the subject. |
| `Stimulus position` | Optional string. Options: Contralateral, Ipsilateral, Bilateral, Centered, Surround, Other, Unknown. Relative visual field position where the stimulus was presented with respect to the subject. |
| `Stimulation context` | Optional string. Options: Passive, Behavioral task, Closed-loop, Anesthetized, Free behavior. Experimental condition in which visual stimulation occurred. |
| `Paradigm description` | Optional string; format textarea. Free-text description of the visual stimulation paradigm, including stimulus sequence, timing, and behavioral relevance. |

## Coordinates

For all procedure types, coordinates are specified using the following [Coordinates systems]({{"datamodel/schemas/coordinates/"|absolute_url}}).

## API access

The API allows for programmable access to Procedures, enabling you to read, edit, and delete procedures through the API. Learn more about the procedures' fields and data structure on the [Procedure API page]({{"api/schemas/procedure/"|absolute_url}}).
