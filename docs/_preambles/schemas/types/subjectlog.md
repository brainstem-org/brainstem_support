<!-- Introductions for the SubjectLog schema types, used by scripts/build_reference_docs.py when the schema itself has no description. One "## group: <group name>" section per group (exact group name from the input), one "## <TypeCode>" section per type (exact code). -->

## group: Physical and Health Logs
Logs of body weight, physical condition, wellness and clinical welfare assessments.

## group: Consumption Logs
Logs of food and water intake.

## group: Deprivation Logs
Logs of food or water restriction periods and the protocol governing them.

## group: Housing Logs
Logs of a subject's housing location and cage conditions.

## group: Experimental Preparation Logs
Logs of handling, habituation and training that prepare a subject for experiments.

## group: Genetic Logs
Logs of genotyping results for a subject.

## group: Observation Logs
Logs of behavioral observations and sensory tests, including the Hargreaves and Von Frey nociception assays.

## FoodConsumption
Logs the amount of food a subject consumed, for tracking intake over time, for example during food restriction.

## FoodDeprivation
Logs periods of food restriction or deprivation, with the responsible person's name and phone number and the protocol governing the deprivation.

## GenericObservation
Logs a behavioral or other observation that no specific log type covers, with its category, a description and the number of repetitions.

## Genotyping
Logs a genotyping result for the subject, with the interpreted genotype, the sample used, assay or panel, confidence and per-locus calls.

## Habituation
Logs sessions habituating a subject before experiments, with the method used, such as tail lift, cupping or glove.

## Handling
Logs handling sessions, with the method used, such as tail lift, cupping or glove.

## HargreavesTest
Logs Hargreaves tests of thermal sensitivity, with stimulus location, paw withdrawal latency, cutoff latency, a 0 to 3 response score and the number of trials.

## Housing
Logs where and how a subject is housed, with location, cage ID and type, light cycle and enrichment.

## Monitoring
Logs routine monitoring of a subject, combining body weight, food and water consumed, body condition score and general health notes.

## TrainingSession
Logs a behavioral training session, with the task, setup, reinforcement type and performance level reached.

## VonFreyTest
Logs Von Frey tests of mechanical sensitivity, with stimulus location, filament force, a 0 to 3 response score and the number of repetitions.

## WaterConsumption
Logs the amount of water a subject consumed, for tracking intake over time, for example during water restriction.

## WaterDeprivation
Logs periods of water restriction or deprivation, with the responsible person's name and phone number and the protocol governing the deprivation.

## Weighing
Logs the subject's body weight. Use Monitoring to record weight together with consumption and health observations.

## WelfareCheck
Logs a clinical welfare assessment, with abnormal signs, condition and pain scores, condition of wound or implant sites, actions taken, the monitoring plan and whether a humane endpoint was met.

## Wellness
Logs a brief overall wellness status for the subject, such as good health, fair or poor.
