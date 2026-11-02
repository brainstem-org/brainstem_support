<!-- Introductions for the Consumable schema types, used by scripts/build_reference_docs.py when the schema itself has no description. One "## group: <group name>" section per group (exact group name from the input), one "## <TypeCode>" section per type (exact code). -->

## group: Device-Linked Consumables
Recording, stimulation and optical hardware that is implanted, mounted on a subject or attached to a rig, together with the connectors and electrode materials that link it to the acquisition system.

## group: Reagents and Solutions
Chemicals, drugs, biologicals, solutions and gases that are administered to subjects or used to prepare and process tissue.

## group: Surgical Consumables
Materials and disposables used during surgery to fix, close or support implants, from cements and screws to sutures and blades.

## AdhesiveCement
A glue, dental or bone cement, or sealant used to secure implants or close tissue, with its mixing requirements, curing method, working time and biocompatibility.

## ChemicalReagent
A general laboratory chemical such as a detergent, salt or buffer component, with compound name, strength, purity, molecular weight and hazards. Use Histology reagent instead for fixatives, clearing, embedding and mounting media.

## ConnectorComponent
Interconnect hardware such as an electrode interface board, connector, adapter or commutator, identified by connector family, contact count and gender, with compatible devices and mass for headcap load.

## ConsumableDevice
A subject-mounted assembly, such as a fiber-optic cannula, described by device class, compatible systems, dimensions, material and connector type. Use Connector component for interconnect hardware.

## EcogArrayDesign
A surface electrode grid or strip design for electrocorticography, with contact count and layout, contact size and material, pitch, substrate and body geometry, and optionally the full contact coordinates, tails, openings and package options.

## ElectrodeComponent
A loose contact or wire supplied for building or completing an electrode, such as a reference or ground wire, with its intended role, physical form, conductor and insulation material, diameter and nominal impedance.

## FastenerAnchor
A bone screw, pin or other anchor used to secure an implant or headcap, with thread size, length, head type and material, and whether it is conductive (relevant when it serves as a reference or ground) and biocompatible.

## HistologyReagent
A tissue-processing reagent such as a fixative, clearing agent, embedding or mounting medium, with its processing role, composition, concentration as supplied, refractive index, pH and hazard information.

## ImmunoReagent
An antibody or related immunoreagent, with target antigen, host and reactive species, clonality, conjugated fluorophore or enzyme, validated applications and recommended dilution.

## ImplantMaterial
Structural hardware used to build or fix an implant, with its category, preparation steps, storage conditions and biocompatibility. Use Adhesive or cement for bonding materials and Fastener or anchor for screws and pins.

## MedicalGas
A medical or carrier gas such as oxygen, medical air or carbogen, with its composition for blended gases, purity or regulatory grade, and how it is supplied to the rig.

## OpticFiberDesign
An optical fiber specification for optogenetics or fiber photometry, with numerical aperture, transmitted wavelength range, fiber type, and core, cladding and coating diameters and materials.

## OpticalComponent
A passive optical element such as a GRIN lens, prism or window, with material, dimensions, surface coating, wavelength range and sterility as supplied.

## PharmacologicalAgent
A drug product such as an anesthetic, analgesic or receptor ligand, with active ingredient, strength, dosage form, typical route of administration, pharmacological category and class, and formulation.

## PhysiologicalSolution
A solution formulated for use with living tissue, such as saline, PBS or aCSF, with its composition, target pH, osmolality, preparation steps and sterility.

## SiliconProbeDesign
A silicon probe design for extracellular recording, with shank count and geometry, recording-site count, layout, shape, material and pitch, and optionally per-shank details, site groups, site coordinates, reference contacts and package options.

## SingleWireElectrode
A single wire used as an electrode, such as a stainless steel, tungsten or platinum-iridium microwire, with its conductor material, insulation, and wire and insulation diameters.

## SurgicalDisposable
A single-use surgical item such as a suture, needle, blade or swab, with its category, material, distinguishing specification such as size or gauge, and sterility.

## TracerDye
A dye or neuronal tracer used for labeling, such as an anterograde or retrograde tracer or lipophilic dye, with its fluorophore, excitation and emission peaks, route of application, solvent and preparation.

## VirusConstruct
A recombinant viral vector design, such as an AAV carrying a GCaMP or opsin transgene, with virus type, capsid, promoter, gene of interest, reporter and other genetic elements.
