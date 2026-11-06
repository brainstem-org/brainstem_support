<!-- Introductions for the Specimen schema types, used by scripts/build_reference_docs.py when the schema itself has no description. One "## group: <group name>" section per group (exact group name from the input), one "## <TypeCode>" section per type (exact code). -->

## CultureItem
Represents a single vessel or coverslip of a culture, such as a dish, flask or tube, with cell line, container, passage and population doubling counts, and experimental condition.

## Organoid
Represents a single organoid, with the cell line or primary preparation it came from and its own container label once it no longer shares a dish.

## Other
Represents an item of a specimen set when no other specimen type fits, described by a short label and its container ID.

## Section
Represents a single tissue section of a section series, with its cut order, thickness where it differs from the series, position along the series axis and how it was obtained, and its slide and position on the slide.

## Slice
Represents a single slice of a slice series, with its cut order, thickness where it differs from the series, position along the series axis and its own container.

## TissuePiece
Represents a discrete piece of tissue, such as a dissected region or biopsy, with its type, largest dimension, mass and container label.

## Well
Represents a single well of a well plate, with its plate address, cell line, experimental condition, role in the plate design and any reason for exclusion from analysis.
