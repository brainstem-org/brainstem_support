<!-- Introductions for the Procedure schema types, used by scripts/build_reference_docs.py when the schema itself has no description. One "## group: <group name>" section per group (exact group name from the input), one "## <TypeCode>" section per type (exact code). -->

## group: Anesthesia, Drug and Fluid Administration
Administration of anesthetics, sedatives, analgesics, antibiotics, anti-inflammatories, fluids and other substances to a subject, whether as clinical care or as the experimental treatment.

## group: Surgical Procedures
Surgical steps on the skull and head, such as burr holes, craniotomies, cranial windows, head fixation, headposts, headcaps and baseplating.

## group: Implant Procedures
Placement of a device in or on the subject, such as recording electrodes, probes, optical implants, cannulas, catheters and physiological sensors; saving one creates an experimental interface for the implanted device.

## group: Injection and Infusion Procedures
Targeted delivery of solutions or viral vectors into the brain or body, with target coordinates where relevant.

## group: Sample Collection Procedures
Collection of blood or tissue samples from a living or dead subject for downstream analysis.

## group: Brain and Tissue Procedures
Procedures that lesion, fix or remove brain tissue, including brain lesions, perfusion fixation and brain extraction.

## group: Endpoint Procedures (Euthanasia)
Methods used to euthanize a subject, such as barbiturate or inhalant overdose, CO₂ exposure, cervical dislocation and decapitation.

## Analgesic
Records the administration of an analgesic, with volume, route and whether it was given to prevent expected pain or to treat pain already present.

## Anesthesia
Records a general anesthetic episode, with the depth reached, end time, total duration and recovery time, plus one row per monitored parameter and any supportive care given.

## AntiInflammatory
Records the administration of an anti-inflammatory agent, with volume, route, whether it was preventive or therapeutic, and whether it served as clinical care or as the experimental treatment.

## Antibiotic
Records the administration of an antibiotic, with volume, route and indication, distinguishing prophylaxis, treatment of an observed problem and use as the experimental manipulation itself.

## BarbiturateInjection
Documents euthanasia by barbiturate overdose, with solution concentration, dose per kilogram, route, volume, time to unconsciousness and the methods used to confirm death.

## Baseplating
Documents fixing a baseplate to the skull or headcap to dock a head-mounted miniature microscope, typically over a previously implanted GRIN lens or prism.

## BloodCollection
Records a blood sample taken from the subject, with collection site and method, approximate volume, intended downstream use, storage conditions and whether the sample was taken post mortem.

## BloodPressureSensorImplant
Documents implantation of a blood pressure sensor, with sensor type, vascular or body implant site, catheter material, anchoring and sterilization.

## BrainExtraction
Records removal of the brain after euthanasia, with extraction method, time from euthanasia to extraction, brain weight, preservation and fixation duration, and storage conditions.

## BrainLesion
Records an intentional brain lesion, with the technique used (e.g., surgical, suction, chemical or thermal) and the estimated or calculated lesion volume.

## BreathingSensorImplant
Documents implantation or attachment of a sensor for monitoring respiration, with sensor type, implant site, lead material, anchoring, signal transmission and sterilization.

## BurrHole
Records drilling of a small opening in the skull, with hole diameter, drill speed, purpose, cooling method and the state the dura was left in.

## CannulaImplant
Documents implantation of a cannula for infusion or other access, with target site, type, gauge, length, laterality, purpose and fixation, and whether an obturator or dummy cannula was inserted.

## CatheterImplant
Documents implantation of an indwelling catheter, with anatomical target, catheter model and material, purpose, fixation, position of the external port and device identifier.

## CervicalDislocation
Documents euthanasia by cervical dislocation, with the method used and how death was confirmed.

## Co2ChamberEuthanasia
Documents euthanasia by CO₂ exposure in a chamber, with concentration, flow rate, exposure duration, chamber volume and prefilling, whether CO₂ was introduced gradually, time to unconsciousness and confirmation of death.

## CranialWindow
Documents creation of a cranial window for optical access to the brain, with the surgical method and the window's shape, dimensions and orientation relative to anatomical landmarks.

## Craniectomy
Records removal of a portion of the skull without replacing the bone, with surgical method, shape, dimensions, orientation relative to landmarks and how the dura was handled.

## Craniotomy
Records an opening of the skull to expose the brain, with surgical method, shape, dimensions, orientation relative to anatomical landmarks and how the dura was handled.

## Decapitation
Documents decapitation of the subject, with the method or instrument used.

## DrugAdministration
Records administration of a substance that no dedicated drug or fluid type covers, with purpose, route, volume and whether it was given as supportive care or as the experimental treatment.

## EcgImplant
Documents implantation of electrodes for recording the electrocardiogram, with wire count, material and insulation, implant site, anchoring and sterilization.

## EcogImplant
Documents placement of an electrocorticography array on the dura, brain surface or bone, with dura handling, skull preparation, array adhesion, ground and reference placement and fixation of the skull-borne assembly.

## EegImplant
Documents implantation of EEG electrodes, such as skull screws or flat contacts, with electrode count, type and material, anchoring, Faraday shielding and sterilization.

## EmgImplant
Documents implantation of EMG wires into one or more muscles, with wire count, material and insulation, target muscles, implant method, anchoring and sterilization.

## FluidTherapy
Records fluid administration for a clinical indication, with total volume, route, delivery profile and infusion rate, number of injection sites and fluid temperature.

## GenericImplant
Documents an implant that no specific implant type covers, such as a custom probe or prototype sensor, with its category, description, insertion rate, anchoring, signal transmission, power source and sterilization.

## GrinLensImplant
Documents implantation of a gradient-index (GRIN) lens for imaging deep brain structures, with insertion rate and how the lens was mounted.

## HeadFixation
Records how the subject's head was fixed during a procedure, typically in a stereotaxic frame, with the fixation method, the alignment achieved (e.g., bregma and lambda level) and materials used.

## Headcap
Documents construction and attachment of a headcap on the skull, with material, shape, construction and attachment method, skull preparation, Faraday shielding and device identifier.

## Headpost
Documents implantation of a headpost for head-fixed experiments, with material, shape, construction, skull preparation, attachment method and device identifier.

## InhalantOverdose
Documents euthanasia by overdose of an inhaled anesthetic, with agent concentration, carrier gas flow, delivery method, exposure duration, time to unconsciousness and confirmation of death.

## Injection
Records an injection of a solution such as a tracer, dye or pharmacological agent, with volume, rate, concentration, method, injection profile and target side. Use Virus injection for viral vectors.

## LocalAnesthetic
Records a local or topical anesthetic placed at a site, with volume, placement technique, site and side, guidance method, dwell time and the observed block effectiveness.

## NerveCuffImplant
Documents implantation of a cuff electrode on a peripheral nerve, such as the sciatic or vagus nerve, with cuff configuration and materials, anchoring, wire exit route and signal transmission.

## OpticFiberImplant
Documents implantation of an optic fiber, for example for optogenetic stimulation or fiber photometry, with dura handling, insertion rate, skull preparation and fixation of the assembly.

## PerfusionFixation
Documents perfusion of wash and fixative solutions through the circulation, with vascular access route, scope, drive and pressure, the phases delivered, signs of completion, failure modes and confirmation of death.

## PrismImplant
Documents implantation of a microprism for optical imaging, with device identifier, insertion rate, sterilization and how the prism was mounted.

## ReferenceElectrodeImplant
Documents implantation of a dedicated reference electrode, with electrode count, material, diameter and impedance, placement site (e.g., cerebellum or skull surface), insertion rate and anchoring.

## Sedative
Records administration of a sedative, with volume, route, delivery profile and rate, the sedation level reached, its duration and recovery time, plus monitoring and supportive care. Use Anesthesia when a surgical plane was reached.

## SiliconProbeImplant
Documents implantation of a silicon probe for extracellular recording, with dura handling, insertion rate, ground and reference placement and how the assembly was fixed to the skull.

## SingleWireElectrodeImplant
Documents implantation of single-wire electrodes for recording or stimulation, with wire count, diameter and material, impedance, insertion rate and sterilization.

## TemperatureSensorImplant
Documents implantation of a temperature sensor, such as a thermocouple, telemetry sensor or passive logger, with lead material, anchoring, signal transmission, power source and sterilization.

## TetrodeWireElectrodeImplant
Documents implantation of a tetrode or stereotrode drive, with tetrode count and wires per tetrode as built, dura handling, insertion rate, ground and reference placement and fixation of the drive.

## TissueCollection
Records collection of a tissue sample, such as a tail tip, with source site, method, length or mass, intended use, preservation and whether it was taken post mortem.

## VirusInjection
Records injection of a viral vector, with volume, rate and injection profile, route (intraparenchymal or systemic), insertion rate and the dwell time before the injector was withdrawn.
