<!-- Introductions for the Manipulation schema types, used by scripts/build_reference_docs.py when the schema itself has no description. One "## group: <group name>" section per group (exact group name from the input), one "## <TypeCode>" section per type (exact code). -->

## group: Optical, Thermal and Ultrasound Stimulation
Stimulation with light, temperature change or ultrasound, including optogenetic stimulation.

## group: Electrical and Magnetic Stimulation
Stimulation with electric currents or magnetic fields, through implanted electrodes, transcranially or by an applied field.

## group: Chemical and Pharmacological Perturbations
Delivery of drugs or other agents by injection, inhalation, superfusion, microperfusion or other liquid application.

## group: Sensory Stimulation
Presentation of auditory, visual, tactile, odor or combined sensory stimuli to the subject.

## AuditoryStimulation
Records sound stimuli presented during a session, with amplitude, base and modulation frequency, waveform profile, duration, duty cycle, repetitions and whether delivery was closed loop.

## DeepBrainStimulation
Records deep brain stimulation through implanted electrodes, with current amplitude, waveform profile, duration, duty cycle, repetitions, polarity and whether stimulation was closed loop.

## ElectricalStimulation
Records electrical stimulation not covered by the deep brain or transcranial types, such as microstimulation through an implanted or acute electrode, with voltage amplitude, waveform profile, duration, duty cycle, repetitions, polarity and closed-loop control.

## ElectromagneticFieldStimulation
Records exposure to an applied electromagnetic field, with field intensity, waveform, duration, duty cycle, repetitions, polarity and closed-loop control. Use transcranial magnetic stimulation for coil-based TMS protocols.

## LiquidPerturbation
Records delivery of a liquid agent, with concentration, volume, delivery profile, flow rate, repetitions and closed-loop control. Choose a more specific type for injection, superfusion or microperfusion.

## Microperfusion
Records local delivery of an agent into tissue by microperfusion, with concentration, volume, delivery profile, flow rate, repetitions and closed-loop control.

## MultisensoryStimulation
Records an event combining stimuli from several sensory modalities, with the modalities, their relative timing, overall duration, repetitions and whether timing or modality was adapted in closed loop.

## OdorStimulation
Records odor presentation, with odor concentration, flow rate, repetitions and whether presentation was locked to an inhalation phase.

## OptogeneticStimulation
Records light delivery to activate or silence opsin-expressing cells, with light power, wavelength, waveform profile, duration, duty cycle, repetitions and closed-loop control, and the optic fiber or LED interface it was delivered through.

## PharmacologicalInhalation
Records an agent administered by inhalation, with concentration, flow rate, volume, delivery profile, repetitions and closed-loop control.

## PharmacologicalInjection
Records a drug injection, with concentration, volume, injection method, flow rate, repetitions and closed-loop control.

## PharmacologicalSuperfusion
Records an agent applied by superfusion over tissue, as in slice experiments or over exposed cortex, with concentration, volume, profile, flow rate, repetitions and closed-loop control.

## TactileStimulation
Records touch or mechanical stimuli applied to the subject, with the contact type, stimulation site, force, duration, temporal profile, repetitions and closed-loop control.

## ThermalPerturbation
Records heating or cooling applied to the subject or tissue, with the temperature change from baseline, duration, profile, duty cycle, repetitions and closed-loop control.

## TranscranialElectricalStimulation
Records transcranial electrical stimulation, such as tDCS or tACS, with current amplitude, waveform, duration, duty cycle, repetitions, polarity and closed-loop control.

## TranscranialMagneticStimulation
Records transcranial magnetic stimulation, with intensity as a percentage of maximum stimulator output or in tesla, waveform, duration, duty cycle, repetitions and closed-loop control.

## UltrasoundStimulation
Records ultrasound neuromodulation, with peak acoustic pressure and intensity, duration, duty cycle, pulse profile, repetitions and closed-loop control.

## VisualStimulation
Records a visual stimulus presentation, with the stimulus types, position in the visual field, duration, repetitions and whether the stimulus adapted to the subject's behavior or physiology.
