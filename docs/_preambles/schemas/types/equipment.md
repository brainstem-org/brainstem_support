<!-- Introductions for the Equipment schema types, used by scripts/build_reference_docs.py when the schema itself has no description. One "## group: <group name>" section per group (exact group name from the input), one "## <TypeCode>" section per type (exact code). -->

## group: Data acquisition
Equipment that records neural, physiological, behavioral or environmental signals and images, from amplifiers, cameras and sensors to complete recording rigs and imaging scanners.

## group: Behavioral and stimulation tools
Equipment that delivers sensory, optical or electrical stimuli to subjects or supports behavioral tasks and locomotion.

## group: Surgical equipment
Equipment used during surgery and other invasive procedures, including anesthesia, stereotaxic positioning, injection, perfusion and drilling.

## group: Environmental controllers
Equipment that controls or isolates the experimental environment, such as temperature, humidity, vibration and acoustic noise.

## group: Miscellaneous
General laboratory, computing and support equipment that does not belong to a more specific group.

## Amplifier
An amplifier unit installed in a setup that amplifies and filters electrophysiological signals before digitization. Record the physical unit, normally linked to its catalog hardware device, together with its configuration in that setup.

## AnesthesiaSystem
An anesthesia system in a setup, such as an isoflurane vaporizer with induction chamber and nose cone, used to induce and maintain anesthesia during surgery or experiments. Records the specific unit and its configuration in that setup.

## AntiVibrationTable
An anti-vibration (optical) table that supports a setup and isolates it from floor vibrations, as used for electrophysiology, imaging and optics. Records the specific table and its configuration in that setup.

## BehaviorRig
An integrated behavioral apparatus in a setup, such as an operant chamber, maze or head-fixed task station, documented as a single unit. Choose it when the rig is tracked as a whole rather than as separate components.

## BiosafetyCabinet
A biosafety cabinet providing a ventilated, filtered enclosure for handling viral vectors, cell cultures and other biological materials. Records the specific cabinet and its configuration in the setup.

## Camera
A camera installed in a setup for video recording of behavior or for image acquisition, for example on a microscope. Records the specific unit and its configuration in that setup, such as placement and acquisition settings.

## Computer
A desktop or workstation computer in a setup that runs acquisition, stimulus-control or analysis software. Small embedded boards are documented as single-board computers or microcontrollers instead.

## DataAcquisitionSystem
A data acquisition system installed in a setup that digitizes and records analog and digital signals, such as a DAQ board or a multichannel recording system. Records the specific unit and its configuration in that setup.

## DrugDeliverySystem
A system in a setup that administers drugs or other compounds to a subject, for example an infusion pump or a cannula-based delivery system. Records the specific unit and its configuration in that setup.

## ElectroencephalographySystem
An EEG system installed in a setup for recording electrical brain activity from scalp or skull-surface electrodes. Records the specific unit and its configuration in that setup.

## ElectromyographyMachine
An EMG system installed in a setup for recording the electrical activity of muscles. Records the specific unit and its configuration in that setup.

## ElectronicComponent
An individual electronic part or module used in a setup, such as a connector, switch, relay, filter or custom circuit board. Use it for electronics that no more specific equipment type describes.

## EphysRig
An integrated electrophysiology rig, such as a patch-clamp or extracellular recording station, documented as a single unit in a setup. Choose it when the rig is tracked as a whole rather than as separate amplifiers, manipulators and acquisition hardware.

## FiberPhotometrySystem
A fiber photometry system installed in a setup that delivers excitation light through an implanted optical fiber and records fluorescence from genetically encoded indicators. Records the specific unit and its configuration in that setup.

## FloatingAirPlatform
A platform supported on a cushion of air, for example an air-lifted arena in which a head-fixed animal navigates or an air-floated surface that isolates equipment from vibration. Records the specific unit and its configuration in the setup.

## ForcePlate
A force plate installed in a setup that measures ground reaction forces, for example to quantify gait, posture or startle responses. Records the specific unit and its configuration in that setup.

## FumeHood
A fume hood providing a ventilated enclosure for working with volatile chemicals, such as fixatives and solvents. Records the specific unit and its location in the lab.

## GlassMicropipettePuller
A micropipette puller used to fabricate glass pipettes for patch clamp, sharp-electrode recording or microinjection. Records the specific unit and its configuration, such as the pulling program in use.

## HumidityController
A device that regulates humidity in a setup, housing area or recording enclosure. Records the specific unit and its configuration in that setup.

## HumiditySensor
A sensor installed in a setup that measures relative humidity to monitor experimental or housing conditions. Records the specific unit and its configuration in that setup.

## InjectionSystem
An injection system, such as a nanoliter injector or microsyringe pump, used to deliver viral vectors, tracers or drugs into tissue during surgery. Records the specific unit and its configuration in that setup.

## IontophoresisStimulator
A current source in a setup used for iontophoretic application of drugs or tracers through a micropipette. Records the specific unit and its configuration in that setup.

## Laser
A laser installed in a setup, used for example for optogenetic stimulation, photostimulation or as an imaging light source. Records the specific unit and its configuration in that setup, such as wavelength and output power settings.

## LedDriver
A driver that powers and modulates LEDs in a setup, for example to generate light pulses for optogenetic stimulation. Records the specific unit and its configuration in that setup.

## LightEmitter
An LED or other non-laser light source in a setup, used for example for optogenetic stimulation, visual stimulation or illumination. Records the specific unit and its configuration in that setup.

## LightSensor
A sensor installed in a setup that measures light intensity or optical power, such as an ambient light sensor or optical power meter. Records the specific unit and its configuration in that setup.

## MagneticResonanceImagingSystem
An MRI scanner used for structural or functional imaging of subjects. Records the specific system and its configuration at the facility or setup where it is installed.

## MagnetoencephalographySystem
An MEG system used to record the magnetic fields generated by neural activity. Records the specific system and its configuration at the facility or setup where it is installed.

## Magnetometer
A magnetometer installed in a setup that measures magnetic fields, for example for head-orientation tracking or for monitoring the magnetic environment. Records the specific unit and its configuration in that setup.

## Microcontroller
A microcontroller board, such as an Arduino, used in a setup for task control, triggering, synchronization or sensor readout. Records the specific unit and its configuration in that setup, such as the firmware it runs.

## Micromanipulator
A micromanipulator that positions electrodes, pipettes or optical fibers with micrometer precision, mounted on a stereotaxic frame or recording rig. Records the specific unit and its configuration in that setup.

## Microphone
A microphone installed in a setup for recording sound, such as animal vocalizations including ultrasonic calls. Records the specific unit and its configuration in that setup, such as placement.

## Microscope
A microscope in a setup that is not covered by the one-, two- or three-photon microscope types, such as a widefield, confocal or dissection microscope. Records the specific unit and its configuration in that setup.

## Miniscope
A head-mounted miniature microscope for imaging neural activity in freely moving animals. Records the specific unit and its configuration in that setup.

## Monitor
A display in a setup, used for presenting visual stimuli or for operating acquisition software. Records the specific unit and its configuration in that setup, such as position relative to the subject.

## MotionTrackingSystem
A motion tracking system installed in a setup that records the position or posture of subjects, for example with infrared cameras and markers. Records the specific system and its configuration in that setup.

## NoiseIsolationChamber
A sound-attenuating chamber that shields a setup from external acoustic noise and, often, light and electrical interference. Records the specific chamber and its configuration in the setup.

## OnePhotonMicroscope
A one-photon (single-photon excitation) microscope, such as a widefield fluorescence system, used for imaging in a setup. Records the specific unit and its configuration in that setup.

## OphysRig
An integrated optical physiology rig, such as an imaging station combining microscope, light sources and acquisition hardware, documented as a single unit in a setup. Choose it when the rig is tracked as a whole rather than as separate components.

## OpticalCoherenceTomography
An optical coherence tomography system used for depth-resolved, label-free imaging of tissue. Records the specific system and its configuration in that setup.

## Oscilloscope
An oscilloscope in a setup used to display and measure electrical signals, for example to monitor recordings or verify stimulus waveforms. Records the specific unit and its configuration in that setup.

## PerfusionSystem
A perfusion system that delivers fluids through tissue or a preparation, for example for transcardial perfusion or slice superfusion. Records the specific unit and its configuration in that setup.

## Photodetector
A photodetector, such as a photodiode or photomultiplier tube, that converts light into an electrical signal for recording in a setup. Records the specific unit and its configuration in that setup.

## PressureSensor
A sensor installed in a setup that measures pressure, for example respiration, air puffs or fluid-line pressure. Records the specific unit and its configuration in that setup.

## RunningWheel
A running wheel in a setup on which a subject runs, often with an encoder to measure locomotion. Records the specific unit and its configuration in that setup.

## SignalProcessingUnit
A hardware unit in a setup that filters, conditions or processes signals, for example in real time for closed-loop experiments. Records the specific unit and its configuration in that setup.

## SingleBoardComputer
A single-board computer, such as a Raspberry Pi, used in a setup for task control, camera acquisition or data logging. Records the specific unit and its configuration in that setup.

## SinglePhotonEmissionComputedTomography
A SPECT scanner used for imaging the distribution of gamma-emitting radiotracers in a subject. Records the specific system and its configuration at the facility or setup where it is installed.

## Speaker
A speaker in a setup used to deliver auditory stimuli, such as tones, noise or ultrasonic sounds. Records the specific unit and its configuration in that setup, such as placement.

## StereotaxicFrame
A stereotaxic frame that holds the subject's head in a fixed coordinate system for targeting brain regions during surgery or acute experiments. Records the specific frame and its configuration in that setup.

## StimulationDevice
A stimulator in a setup, such as an electrical stimulus generator or stimulus isolator, that delivers stimuli to a subject or tissue. Use it for stimulation hardware that no more specific equipment type describes.

## SurgicalPowerTool
A powered surgical tool, such as a dental drill, used for craniotomies and other surgical procedures. Records the specific unit and its configuration in that setup.

## TemperatureSensor
A sensor installed in a setup that measures temperature, for example body temperature during surgery or the temperature of a bath or enclosure. Records the specific unit and its configuration in that setup.

## ThermalController
A temperature controller, such as a heating pad with feedback control or a bath heater, that maintains the subject's or preparation's temperature. Records the specific unit and its configuration in that setup.

## ThreePhotonMicroscopy
A three-photon microscope used for deep-tissue imaging in a setup. Records the specific unit and its configuration in that setup.

## Treadmill
A treadmill in a setup on which a subject walks or runs, either motorized or freely driven, often head-fixed. Records the specific unit and its configuration in that setup.

## TwoPhotonMicroscope
A two-photon microscope used for imaging in scattering tissue, for example calcium imaging of neural activity in vivo. Records the specific unit and its configuration in that setup.

## UltrasoundImagingSystem
An ultrasound imaging system, used for example for functional ultrasound or anatomical imaging. Records the specific system and its configuration in that setup.
