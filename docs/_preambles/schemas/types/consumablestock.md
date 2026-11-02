<!-- Introductions for the ConsumableStock schema types, used by scripts/build_reference_docs.py when the schema itself has no description. One "## group: <group name>" section per group (exact group name from the input), one "## <TypeCode>" section per type (exact code). -->

## group: Device-Linked Consumables
Lots and individually identified items of recording, stimulation and optical hardware, connectors and electrode materials held in a lab inventory.

## group: Reagents and Solutions
Lots of chemicals, drugs, biologicals, solutions and gases held in a lab inventory, with the values of the lot as received or prepared.

## group: Surgical Consumables
Lots of cements, fasteners, implant materials and surgical disposables held in a lab inventory, with quantity and sterility.

## AdhesiveCement
A lot of glue, cement or sealant, recording the batch number, amount held, the mixing ratio actually used when it differs from the catalog default, preparation steps and sterility.

## ChemicalReagent
A lot of a general laboratory chemical, recording the batch number, amount held, strength, purity and hazard information. Use Histology reagent for fixatives, clearing, embedding and mounting media.

## ConnectorComponent
A lot of connectors, interface boards, adapters or cables, recording the batch number, number of items and, for hand-assembled parts, who built them.

## ConsumableDevice
A subject-mounted assembly held in inventory, such as a set of fiber-optic cannulas, recording its device class, compatible systems, dimensions, material and connector type. Use Connector component for interconnect hardware.

## EcogArray
A lot of ECoG arrays of one design, listing the identifier of each array so an individual array can be traced from inventory into a subject.

## ElectrodeComponent
A lot of loose contacts or spooled wire for building electrodes, recording the batch number, quantity or length held, impedance measured for the lot and sterility.

## FastenerAnchor
A lot of bone screws, pins or anchors, recording the batch number, number of items and sterility.

## HistologyReagent
A lot of fixative, clearing agent, embedding or mounting medium, purchased or made up in the lab, recording the batch number, amount, concentration and measured pH, plus preparation date and method for freshly prepared reagents.

## ImmunoReagent
A lot of an antibody or immunoreagent, recording the batch number, target antigen, host and reactive species, clonality, conjugate, amount held and working dilution.

## ImplantMaterial
A lot of structural implant hardware, recording the batch number, amount held, preparation steps and sterility.

## MedicalGas
A gas cylinder or delivered batch of medical or carrier gas, recording the cylinder serial number or batch ID, cylinder size or remaining contents, and regulator delivery pressure or flow.

## OpticFiber
A lot of optic fibers or fiber implants of one design, listing the identifier of each fiber so an individual implant can be traced from inventory into a subject.

## OpticalComponent
Passive optical elements held in inventory, such as GRIN lenses, prisms or windows, recording their type, material, dimensions, coating, wavelength range and sterility.

## PharmacologicalAgent
A lot of a drug, recording the batch number, active ingredient, amount held, strength, dosage form, formulation and purity.

## PhysiologicalSolution
A batch of saline, PBS, aCSF or another physiological solution, purchased or prepared in the lab, recording composition, amount, pH, osmolality, preparation steps and sterility.

## SiliconProbe
A lot of silicon probes of one design, listing the identifier of each probe so an individual probe can be traced from inventory into a subject.

## SingleWireElectrode
A lot of single-wire electrodes, listing the identifier of each wire, the number of electrodes and the wire length.

## SurgicalDisposable
A lot of sutures, needles, blades or other single-use surgical items, recording the batch number, number of items and sterility.

## TracerDye
A lot of a dye or neuronal tracer, recording the batch number, fluorophore, excitation and emission peaks, amount held, solvent and preparation steps.

## VirusSolution
A lot of viral vector, recording the batch number, titer as received or prepared, available volume, and the number and volume of aliquots.
