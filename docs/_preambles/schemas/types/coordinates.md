<!-- Introductions for the Coordinates schema types, used by scripts/build_reference_docs.py when the schema itself has no description. One "## group: <group name>" section per group (exact group name from the input), one "## <TypeCode>" section per type (exact code). -->

## BMA_XYZ_Absolute
Absolute position in Brain/MINDS Marmoset Atlas 2.0 space, measured from the atlas origin between the commissures (not ear bar zero), with +X anatomical right, +Y anterior and +Z superior, plus AP and ML tilts and an axial roll. Use it for marmoset targets.

## CCF_XYZ_Absolute
Absolute position in Allen Mouse CCFv3 space, measured from the anterior-superior-left origin with +X posterior, +Y ventral and +Z right, plus two tilts and an axial roll. Use it for mouse targets planned in or registered to the Allen atlas.

## ContainerGrid_RC
Location in a multiwell plate or gridded container, given as a well ID (A1 top-left, rows increasing back or down, columns increasing right) and an X/Y offset from the well center. Use it for specimens held in labware wells.

## ContainerLocal_XYZ
Position in an XYZ frame attached to a container, with a declared origin and a mapping of container +X, +Y and +Z to the preparation or setup. Use it when a location is best given relative to the container rather than the specimen.

## External_XYZ_Euler
Position in a declared external reference frame, such as a rig or stage frame, whose origin, axes, handedness and unrotated pose are defined in the record, with orientation as fixed-frame X, Y then Z rotations. Use it when no anatomical or atlas frame applies.

## JRC2018U_XYZ_Absolute
Absolute position in the JRC2018 Unisex Drosophila brain template, measured from the volume corner with +X toward the fly's left, +Y ventral and +Z posterior (anterior-view stack convention), plus two tilts and an axial roll. Use it for fly brain targets.

## Landmark_APMLDV_Absolute
Absolute AP/ML/DV position from a declared landmark that defines all three zeros and axes, with +AP anterior, +ML anatomical right and +DV ventral, plus AP and ML tilts and an axial rotation. Use it for landmarks other than Bregma and Lambda, such as the obex, interaural zero, the anterior commissure or the center of a cranial window.

## Landmark_APML_SurfaceDepth
Insertion point given as AP/ML from a declared landmark (+AP anterior, +ML anatomical right) plus a non-negative insertion depth along the final approach axis from a declared surface. Use it for landmark-referenced insertions where depth is measured from the contacted surface.

## MNI152_XYZ_Absolute
Absolute position in MNI152 ICBM 2009c human template space, measured from the anterior-commissure origin with +X anatomical right, +Y anterior and +Z superior, plus AP and ML tilts and an axial roll. Use it for human targets in MNI space.

## MapZebrain_XYZ_Absolute
Absolute position in the mapzebrain larval zebrafish atlas, measured from the volume corner with +X anatomical right, +Y posterior and +Z superior, plus two tilts and an axial roll. Use it for larval zebrafish brain targets.

## NMT_XYZ_Absolute
Absolute position in NIMH Macaque Template v2 space, measured from ear bar zero with +X anatomical right, +Y anterior and +Z superior, plus AP and ML tilts and an axial roll. Use it for macaque targets in NMT v2.

## SpecimenSurface_XY
Two-dimensional position on a specimen surface, with a declared origin, a mapping of specimen directions to +X and +Y and a clockwise in-plane rotation. Use it for surface locations on ex-vivo specimens, such as slices or whole mounts, where depth is not needed.

## SpecimenSurface_XYDepth
Insertion point on a specimen surface, given as X/Y from a declared origin, plus insertion depth from a declared surface and an axial rotation. Use it for electrodes or pipettes entering an ex-vivo specimen from its surface.

## SpecimenVolume_XYZ
Three-dimensional position within a specimen, with a declared origin, a mapping of specimen directions to +X, +Y and +Z, and orientation as fixed-frame X, Y then Z rotations. Use it for locations inside cleared tissue, explants or other volumetric specimens.

## Spinal_RCMLDV_Absolute
Absolute spinal position from an origin on the cord central axis at a declared segment or vertebral level, with +RC rostral along the cord centerline, +ML right of midline and +DV ventral, plus RC and ML tilts and an axial rotation.

## Spinal_RCML_SurfaceDepth
Spinal insertion point given as RC/ML from a declared segment or vertebral reference (+RC rostral, +ML right of midline) plus a non-negative insertion depth from a declared surface. Use it for spinal injections or electrode insertions with depth measured from the contacted surface.

## Stereotaxic_BregmaAbsolute
Absolute AP/ML/DV position measured from Bregma, with +AP anterior, +ML anatomical right and +DV ventral, plus AP and ML tilts and an axial rotation. Use it when DV is given from Bregma rather than as depth from the brain surface.

## Stereotaxic_BregmaBrainSurface
Insertion point given as AP/ML from Bregma (+AP anterior, +ML anatomical right) plus a non-negative depth along the final approach axis from brain-surface contact, not from the skull. Use it when depth is measured from where the device touches the brain.

## Stereotaxic_LambdaAbsolute
Absolute AP/ML/DV position measured from Lambda, with +AP anterior, +ML anatomical right and +DV ventral, plus AP and ML tilts and an axial rotation. Use it when DV is given from Lambda rather than as depth from the brain surface.

## Stereotaxic_LambdaBrainSurface
Insertion point given as AP/ML from Lambda (+AP anterior, +ML anatomical right) plus a non-negative depth along the final approach axis from brain-surface contact, not from the skull. Use it when depth is measured from where the device touches the brain.

## WHS_XYZ_Absolute
Absolute position in Waxholm Space rat brain atlas v4, measured from the WHS origin with +X anatomical right, +Y anterior and +Z superior, plus AP and ML tilts and an axial roll. Use it for rat targets in WHS space.
