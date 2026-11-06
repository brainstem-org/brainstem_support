<!-- Introductions for the SpecimenProcedure schema types, used by scripts/build_reference_docs.py when the schema itself has no description. One "## group: <group name>" section per group (exact group name from the input), one "## <TypeCode>" section per type (exact code). -->

## group: Preparation
Initial handling of ex-vivo material, such as dissecting tissue for further processing.

## group: Fixation and Preservation
Steps that fix, embed or cryopreserve specimens to preserve tissue for later processing.

## group: Sectioning
Cutting of tissue into sections or slices on a cryostat, vibratome, microtome or similar instrument.

## group: Tissue Processing
Chemical processing steps that prepare tissue for embedding, clearing or imaging, such as dehydration.

## group: Labeling and Staining
Steps that label or stain molecular and structural targets in a specimen, including antigen retrieval, blocking, immunolabeling, in situ hybridization, dye loading, staining and washes.

## group: Clearing and Mounting
Rendering tissue transparent and mounting specimens for imaging.

## group: Generic
Specimen interventions that no specific specimen procedure type describes.

## AntigenRetrieval
Records an antigen retrieval step that unmasks epitopes before immunolabeling, with the retrieval method, temperature and duration.

## Blocking
Records a blocking step that reduces nonspecific antibody binding before labeling, with its duration and temperature.

## Cryopreservation
Records cryoprotection or freezing of specimens, for example sucrose infiltration followed by freezing, for storage or cryosectioning.

## Cryosectioning
Records a cutting event on a cryostat, with nominal section thickness, cutting plane, number of sections, whether every section was retained, the series sampling interval, collection method and blade settings.

## Dehydration
Records dehydration of tissue, typically through a graded alcohol or solvent series, before embedding, clearing or coverslipping.

## Dissection
Records dissection of tissue from a specimen, with the instrument used, temperature and duration.

## DyeLoading
Records loading of cells or tissue with a dye, for example a calcium indicator or a tracer.

## Embedding
Records embedding of tissue in a supporting medium, such as agarose, paraffin, OCT compound or resin, before sectioning.

## Fixation
Records immersion fixation of a specimen in a fixative such as paraformaldehyde. Fixation by vascular perfusion of the subject is recorded as a Brain perfusion fixation procedure.

## GenericIntervention
Records an intervention on a specimen that no specific specimen procedure type covers, described in the lab's own words.

## Immunolabeling
Records antibody-based labeling of a specimen, including whether it was labeled free-floating, slide-mounted or as a whole mount.

## InSituHybridization
Records in situ hybridization to detect target transcripts in a specimen, with the hybridization chemistry used.

## Mounting
Records mounting of specimens onto slides or in a mounting medium, for example coverslipping sections for microscopy.

## Sectioning
Records a cutting event on a vibratome, microtome or similar instrument, with nominal thickness, cutting plane, number of sections, blade angle and speed, and vibration settings. Use Cryosectioning for cryostat cuts.

## Staining
Records histological or chemical staining of a specimen, such as a Nissl stain, as distinct from immunolabeling or in situ hybridization.

## TissueClearing
Records clearing of tissue to render it transparent for volumetric imaging, with the clearing method family, such as solvent-based iDISCO+ or 3DISCO.

## WashStep
Records a wash between processing or labeling steps, for example buffer rinses that remove unbound reagent.
