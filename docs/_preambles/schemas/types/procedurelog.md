<!-- Introductions for the ProcedureLog schema types, used by scripts/build_reference_docs.py when the schema itself has no description. One "## group: <group name>" section per group (exact group name from the input), one "## <TypeCode>" section per type (exact code). -->

## Impedances
Logs electrode impedance measurements per channel, with impedance and phase values, unit and measurement frequency, for example to track an implant over days.

## LinearDisplacement
Logs the displacement of a movable implant at each log time, for example a probe advanced on a microdrive.

## TetrodeAdjustment
Logs adjustments of individual tetrodes on a drive, with one row per tetrode moved at each log time.
