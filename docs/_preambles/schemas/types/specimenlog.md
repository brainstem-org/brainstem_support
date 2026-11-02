<!-- Introductions for the SpecimenLog schema types, used by scripts/build_reference_docs.py when the schema itself has no description. One "## group: <group name>" section per group (exact group name from the input), one "## <TypeCode>" section per type (exact code). -->

## group: Health Logs
Logs of specimen health and viability assessments.

## group: Environmental Logs
Logs of the conditions around specimens, such as temperature, pH, oxygenation, CO₂ and humidity.

## group: Solution Logs
Logs of bath solutions and culture medium applied to specimens.

## group: Observation Logs
Free-form observations on specimens.

## BathSolution
Logs the bath solution applied to a specimen set, such as ACSF, with exchange type, volume, temperature, pH, osmolality, perfusion flow rate, oxygenation gas and the chamber used.

## CO2
Logs the CO₂ concentration of the incubator atmosphere holding a culture, with the incubator ID.

## CultureMediumChange
Logs a change of culture medium, with the replacement medium formulation, volume exchanged and any supplements added.

## GenericObservation
Logs a free-form observation on a specimen set when no specific log type fits.

## Humidity
Logs the relative humidity of the chamber atmosphere holding a culture, with the chamber ID.

## Oxygenation
Logs oxygenation of a bath or chamber, with the applied gas mixture and flow rate, measured dissolved oxygen or partial pressure, and the measurement method, location, device and calibration.

## PH
Logs a pH measurement of a bath, chamber or sample, with measurement temperature, method, location, device and calibration.

## SliceHealth
Logs an assessment of slice health, with overall rating, assessment method and scoring criteria, observed indicators, estimated viability, the context (e.g., before or after recording) and assessor blinding.

## Temperature
Logs a temperature measurement in a chamber, bath or specimen, with measurement location, method, device and calibration.

## ViabilityAssay
Logs a viability assay on cells or tissue, with the assay type, percent viability and total cell count.
