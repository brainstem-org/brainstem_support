<!-- Introductions for the MaterialUsage schema types, used by scripts/build_reference_docs.py when the schema itself has no description. One "## group: <group name>" section per group (exact group name from the input), one "## <TypeCode>" section per type (exact code). -->

## group: Agents and drugs
Pharmacologically active substances given to a subject or applied to tissue, recorded with the amount of each agent itself rather than of the mixture it was part of.

## group: Fluids and vehicles
Fluids, carrier gases and vehicles that are administered or that carry an active agent, and additives mixed into such fluids.

## group: Biological and experimental payloads
Viral vectors, cells, tracers, particles and other components delivered into tissue, recorded with the titer, count, concentration or volume actually delivered.

## group: Devices
Implanted, inserted or attached devices for recording, stimulation, imaging, sensing or fluid delivery, recorded with their sterility and use-specific preparation.

## group: Components and supporting materials
Hardware and materials that hold, position, protect or fix an implant or specimen, such as cements, fasteners, microdrives, headcaps and slides.

## group: Reagents and labels
Reagents and labels used in histology and specimen processing, from fixation and antigen retrieval through blocking, immunolabeling, staining and clearing.

## group: Media and embedding
Media used to process, collect, store, cryoprotect, embed, mount or optically match tissue and specimens.

## group: Collection and supplies
Containers, additives and disposable supplies used to collect, process or handle a specimen or to support a surgery.

## group: Other
Materials that do not fit any of the specific roles.

## ActiveAgent
The pharmacologically active substance of a formulation given or applied in a procedure, when no more specific drug role fits, with this agent's own dose, concentration, dilution, volume or mass.

## AnestheticAgent
An anesthetic drug given for induction or maintenance, with this agent's own dose, concentration and volume, also when it is one component of a cocktail. A vaporizer setting for an inhaled agent belongs on the event, not here.

## Anticoagulant
An anticoagulant such as heparin used to keep blood, catheters or delivery lines from clotting, with the applied concentration, dilution and volume.

## HemostaticAgent
A material or agent applied to control bleeding, such as a gelatin sponge, bone wax or topical hemostat, with the amount or number of pieces used and how it was applied.

## InhaledEuthanasiaAgent
A gas or inhalant used for euthanasia, such as CO2 or an overdose of isoflurane, with the applied concentration, flow rate and duration of exposure.

## InjectedEuthanasiaAgent
An injectable drug used for euthanasia, such as a pentobarbital solution, with the applied dose, concentration, dilution, volume or mass.

## LesionAgent
A substance used to produce a chemical or excitotoxic lesion, such as ibotenic acid or 6-OHDA, with the applied dose, concentration, volume and application method.

## PharmacologicalAdjuvant
A substance added alongside the main agent to modify its effect or delivery, such as a vasoconstrictor or an enzyme, with its own dose, concentration or activity units per volume and the reason it was added.

## ReversalAgent
A drug given to reverse an anesthetic or sedative, such as atipamezole after medetomidine, with the applied dose, concentration and volume, the dose it was chosen against, and whether reversal was meant to be full or partial.

## SupportiveAgent
A drug given for supportive or perioperative care, such as an analgesic, anti-inflammatory, antibiotic or ophthalmic ointment, with the applied dose, concentration, dilution, volume or mass.

## CellSuspension
A suspension of cells delivered into tissue, for example for transplantation, with the applied cell count and concentration, viability before application, volume and passage number of cultured cells.

## DeliveredComponent
One component of an injected or infused formulation when no more specific payload role fits, with its applied dose, concentration, volume, mass or count and its fraction of the final formulation.

## NeuralTracer
An anterograde or retrograde tracer delivered into tissue to label neuronal projections, with the applied concentration, dilution, volume or mass and the application method, such as pressure injection or iontophoresis.

## ParticleSuspension
A suspension of particles, such as fluorescent microspheres or nanoparticles, delivered into tissue, with the applied particle concentration or count, particle size and volume.

## ViralComponent
A viral vector in the formulation actually injected, with the applied volume, dilution and the effective titer delivered, which can differ from the stock titer.

## CollectionAdditive
A substance added to a collection tube or medium at collection, such as an anticoagulant or protease inhibitor, with the applied concentration, dilution, volume or mass.

## CollectionContainer
A tube, vial, cassette or other container used to collect or hold a specimen, with the number used, sterility and any preparation.

## ProcessingSupply
A disposable item used in specimen processing, such as a filter, needle or blade, with the number used, sterility, sterilization or disinfection method and size or gauge.

## SurgicalSupply
A disposable item used during surgery, such as a suture, swab or drape, recorded with the number used.

## AdhesiveSealant
A glue, dental or bone cement, or sealant used to secure an implant or seal tissue, with the amount used, mixing ratio, application method and area, and curing method, duration and temperature.

## Baseplate
A baseplate fixed to the skull or headcap to which a removable device, such as a head-mounted miniature microscope, is attached.

## Coating
A coating applied to a device or component before use, such as a lipophilic dye on a probe shank, with the coated area, application method, concentration and number of coats.

## ConnectorComponent
A connector, interface board, adapter or cable used to link an implanted device to the acquisition system, with the number used and its sterility, sterilization or disinfection method.

## Fastener
A bone screw, anchor pin or other fastener used to secure an implant or headcap, with the number and size used, sterility and any preparation.

## FixedPositioningAssembly
A fixed carrier or shuttle that holds a device at a set position without a movable drive, with how the device is attached, how the carrier is fixed, whether the device can be recovered, and sterility.

## HeadcapAssembly
A prefabricated or assembled headcap that protects and holds implants on the skull, with its sterility and any surface treatment or coating.

## ManualMicrodrive
A manually adjusted microdrive that advances an implanted device, such as a screw-driven drive for tetrodes or a silicon probe, with drive mechanism, travel range, travel per turn, retractability, recovery, attachment and sterility.

## MotorizedMicrodrive
A motor-driven microdrive that advances an implanted device, with its control mode, travel range, step size, movement rate, retractability, recovery, attachment and sterility.

## MountingComponent
A glass slide, coverslip or other support used to mount a tissue section or specimen, with the number used, preparation and application method.

## Obturator
A removable insert, such as a dummy cannula or stylet, that keeps a guide cannula or port patent between uses, with the number used, sterility and preparation.

## OtherComponent
A supporting component that does not fit any of the specific component roles, with the number used, sterility, surface treatment and preparation.

## ShieldingMaterial
A material used to shield an implant electrically or optically, such as conductive paint, copper mesh or light-blocking material, with the amount or number of pieces used and how it was applied.

## BloodPressureSensor
A blood-pressure sensor or telemetry transmitter implanted or attached to measure arterial or venous pressure, with its sterility and any surface treatment.

## Cannula
A guide or infusion cannula implanted or inserted for drug or fluid delivery, with its sterility and tip preparation.

## Catheter
A vascular or other catheter placed for infusion or sampling, with its sterility and preparation of its ends.

## CranialWindow
A glass or polymer window placed over a craniotomy for optical access, with its sterility and any surface treatment or coating.

## EcogArray
An ECoG array placed on the cortical surface for electrocorticography, with the number used, sterility, preparation and any surface treatment.

## ElectrodeAssembly
An assembled set of electrodes, such as a tetrode bundle or multi-wire array, with the number of whole assemblies used, sterility and any surface treatment.

## FluidDeliveryLine
Tubing or a line connecting a pump or syringe to a cannula or catheter, with its dead, priming and flush volumes, end preparation and sterility.

## GenericDevice
A device that does not fit any of the specific device roles, with the number used, sterility, surface treatment and preparation.

## GrinLens
A gradient-index (GRIN) lens implanted for deep-brain imaging, with its sterility, tip preparation and shape, and any surface treatment.

## GroundElectrode
An electrode, screw or wire used as the electrical ground for a recording or stimulation, with the number used, sterility, tip preparation and surface treatment.

## Headpost
A headpost or head plate fixed to the skull for head restraint, with its sterility and any surface treatment.

## MicrodialysisProbe
A microdialysis probe used to sample or deliver substances in extracellular fluid, with its priming volume, membrane preparation, measured relative recovery and sterility.

## MultiElectrodeArray
A planar or penetrating multi-electrode array, such as a Utah array or a culture MEA, with its preparation, treatment of the array or contacts, and sterility.

## NerveCuff
A cuff electrode placed around a peripheral nerve for recording or stimulation, with its sterility and any surface treatment.

## OpticFiber
An optic fiber implant or patch fiber used for optogenetic stimulation or fiber photometry, with the prepared length, tip preparation and shape, surface treatment and sterility.

## OsmoticPump
An osmotic minipump implanted to deliver a solution continuously over days or weeks.

## PatchPipette
A glass pipette used for patch-clamp or juxtacellular recording, with its tip preparation, such as fire polishing, any coating and sterility.

## Prism
A microprism implanted or placed for optical access to a tissue plane, with its sterility and any surface treatment.

## ReferenceElectrode
An electrode, screw or wire used as the recording reference, with the number used, sterility, tip preparation and surface treatment.

## RespiratorySensor
A sensor used to monitor breathing, such as a thermocouple, pressure sensor or chest belt, with its sterility and any surface treatment.

## SiliconProbe
A silicon probe inserted or implanted for extracellular recording, with its sterility and sterilization or disinfection method.

## SingleWireElectrode
A single-wire electrode used for recording or stimulation, with its tip preparation, surface treatment and sterility.

## StimulatingElectrode
An electrode used to deliver electrical stimulation, with its tip preparation, surface treatment and sterility.

## TemperatureSensor
A thermistor, thermocouple or other probe used to measure body or tissue temperature, with its sterility and any surface treatment.

## AdministeredFluid
A fluid given to a subject, such as saline or lactated Ringer's for fluid support, with the volume of this fluid given.

## CarrierGas
The gas that carries an inhaled anesthetic or is supplied for breathing, such as oxygen or medical air, with the applied flow rate and concentration.

## FluidAdditive
A substance added to a fluid, such as drinking water or a perfusion reservoir, with the concentration reached after mixing, the amount added, and whether an equal volume was withdrawn first.

## IrrigationSolution
A solution used to rinse or keep tissue moist during a procedure, such as sterile saline or aCSF, with the applied concentration, dilution and volume.

## Vehicle
The solvent or carrier in which an active agent is dissolved or suspended, such as saline, DMSO or cyclodextrin, with the amount used and its pH, osmolality and sterilization as prepared.

## Cryoprotectant
A cryoprotective solution, such as sucrose or glycerol, used to protect tissue before freezing or sectioning, with the applied concentration, dilution and volume.

## EmbeddingMedium
A medium in which tissue is embedded for sectioning, such as paraffin, agarose or OCT, with the amount used, preparation and application method.

## IndexMatchingMedium
A medium matched to the refractive index of cleared tissue or of the objective for imaging, with the applied concentration, volume, preparation and application method.

## Medium
A medium used to collect or process tissue or cells when no more specific media role fits, such as culture medium or ice-cold cutting solution, with the applied concentration, dilution and volume.

## MountingMedium
A medium used to mount sections under a coverslip, with or without antifade or a nuclear counterstain, with the applied volume, concentration, preparation and application method.

## StorageMedium
A medium in which tissue or specimens are stored, such as PBS with sodium azide or an antifreeze solution, with the applied concentration, dilution and volume.

## Other
A material that fits none of the specific roles, with the amount or number used, preparation and application method. Choose a specific role whenever one applies.

## BlockingReagent
A reagent used to block nonspecific binding before labeling, such as normal serum or BSA, with the applied concentration, dilution and volume.

## Buffer
A buffer used during specimen processing, such as PBS or Tris-buffered saline, with the applied concentration, dilution and volume.

## ClearingReagent
A reagent used to render tissue optically transparent, as in CLARITY, iDISCO or CUBIC protocols, with the applied concentration, dilution, volume and application method.

## DehydrationReagent
A reagent used to dehydrate tissue, such as a graded ethanol or methanol series, with the applied concentration, dilution and volume.

## DetectionReagent
A reagent used to detect or amplify a label, such as an avidin-biotin complex, DAB substrate or tyramide amplification reagent, with the applied concentration, dilution and volume.

## Fixative
A fixative used to preserve tissue, such as paraformaldehyde for perfusion or immersion fixation, with the applied concentration, dilution and volume.

## HybridizationProbe
A nucleic acid probe used for in situ hybridization, such as an RNAscope or FISH probe, with the applied concentration, dilution and volume.

## PermeabilizationReagent
A reagent used to permeabilize tissue or cell membranes for labeling, such as Triton X-100 or saponin, with the applied concentration, dilution and volume.

## PrimaryLabel
A primary antibody or other immunolabeling reagent that binds the target directly, with the working concentration or dilution and volume applied.

## ProcessingReagent
A reagent used in specimen processing when no more specific reagent role fits, with the applied concentration, dilution, volume or mass and application method.

## RetrievalReagent
A reagent used for antigen or epitope retrieval, such as citrate buffer for heat-induced retrieval, with the applied concentration, dilution and volume.

## SecondaryLabel
A secondary antibody or other reagent that binds the primary label, typically conjugated to a fluorophore or enzyme, with the working concentration or dilution and volume applied.

## StainDye
A histological stain or dye, such as Nissl, DAPI or hematoxylin, with the applied concentration, dilution, volume or mass and application method.

## WashSolution
A solution used to rinse tissue between processing steps, such as PBS or PBS with Tween, with the applied concentration, dilution and volume.
