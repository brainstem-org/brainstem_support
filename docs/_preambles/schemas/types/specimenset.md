<!-- Introductions for the SpecimenSet schema types, used by scripts/build_reference_docs.py when the schema itself has no description. One "## group: <group name>" section per group (exact group name from the input), one "## <TypeCode>" section per type (exact code). -->

## Culture
Describes a culture of cells or tissue, such as organotypic slices on inserts, with how it was established, format, day 0 event, growth surface and coating, medium, incubator settings and termination reason.

## OrganoidBatch
Describes a production run of organoids, which may span several vessels, with batch ID, day 0 event, differentiation protocol type, culture format, agitation, medium and incubator settings.

## Other
Describes a set of ex-vivo material that none of the other specimen set types fits.

## SectionSeries
Describes a series of sections cut from the same tissue, with cutting plane, the axis and origin used to position sections, default thickness, sections per slide and the slide box or plate holding the series.

## SliceSeries
Describes a series of living slices, such as acute brain slices, with cutting plane, the axis and origin used to position slices, default thickness and the holding solution.

## WellPlate
Describes a multi-well plate or chambered slide, with its label, format, edge-well handling, coating and incubator settings. Individual wells are recorded as Well specimens.

## WholeTissue
Describes an intact tissue or organ kept whole, such as an extracted brain, with the label of its container when held in one.
