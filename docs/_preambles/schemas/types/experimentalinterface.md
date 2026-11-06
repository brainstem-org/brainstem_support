<!-- Introductions for the ExperimentalInterface schema types, used by scripts/build_reference_docs.py when the schema itself has no description. One "## group: <group name>" section per group (exact group name from the input), one "## <TypeCode>" section per type (exact code). -->

## group: Electrophysiology
Electrodes, arrays and pipettes that record electrical activity from neurons, nerves, muscle or heart, together with the ground and reference electrodes these recordings need.

## group: Optical
Optical access and light-path hardware, such as cranial windows, GRIN lenses, prisms, optic fibers, objectives, miniscopes and widefield macroscopes.

## group: Stimulation
Devices that deliver electrical, optical, magnetic, thermal or ultrasound stimulation, or present auditory, odor, tactile and visual stimuli.

## group: Delivery
Lines, cannulas, catheters, pumps and perfusion systems through which drugs or solutions reach the subject or tissue.

## group: Physiological monitoring
Sensors that monitor the subject's physiological state, such as respiration and blood pressure.

## group: Behavioral and Environmental
Sensors that observe the subject or its surroundings without contacting tissue, such as cameras, microphones and tracking systems.

## group: Assemblies
Structural hardware fixed to the skull that holds, protects or connects other interfaces, such as headposts and headcaps.

## group: Generic
A fallback for interface hardware that no specific interface type covers.

## AuditoryStimulator
Describes how sound stimuli reached the subject: the stimulus types, the delivery method such as free-field speakers, the experimental context and the stimulation paradigm. Choose it for any setup that presents auditory stimuli during a session.

## BathPerfusion
Records the perfusion system supplying solution to an ex-vivo preparation in a recording chamber, with the solution composition, flow rate and temperature at the chamber. Use it for slice or explant experiments with continuous bath exchange.

## BloodPressureSensor
Represents a sensor that monitors the subject's blood pressure, such as an implanted telemetry catheter or an arterial pressure transducer.

## Camera
Records a camera that images the subject or its environment, with its view and configured frame rate. Use it for behavioral and tracking video; imaging optics such as miniscopes and objectives have their own types.

## Catheter
Records an installed catheter, such as an intravenous or intraperitoneal line, with its route and gauge. Use it for vascular or body-cavity access; local delivery into tissue through an implanted cannula has its own type.

## CranialWindow
Records a transparent window installed over the brain for chronic optical access, with the window material and diameter. Imaging acquisitions made through the window can name it, so its location travels with the data.

## DrugDeliveryLine
Records a line that carries a drug or solution to the subject, with its route and dead volume. Use it for infusion tubing where the volume retained in the line matters for dosing.

## ECG
Records electrodes placed to measure the electrocardiogram, with the lead configuration and electrode layout.

## ECoG
Records an electrocorticography grid or strip on the cortex, with the tissue layer it rests on (dura, exposed brain surface or bone) and how its reference is wired. Use it for surface arrays rather than penetrating probes.

## EEG
Records EEG electrodes on the scalp or skull, with the electrode layout and number of configured channels.

## EMG
Records electrodes placed in or on a muscle to measure electromyographic activity, with the target muscle and electrode layout, for example neck EMG for sleep scoring.

## GRINLens
Records an implanted gradient-index lens that relays images from deep tissue to a miniscope or objective, with the protrusion of the lens top above the skull at the implant site.

## Generic
Use when no specific interface type fits the hardware. Captures an identifier for the interface configuration and free-text notes on configuration details.

## GroundElectrode
Records the electrode that grounds an electrophysiology recording, with the anatomical or apparatus site where it is placed, such as a skull screw over the cerebellum.

## Headcap
Records the protective assembly built on the skull around implanted devices, with its final shape or design, shielding and connector and port configuration.

## Headpost
Represents a headpost or head plate fixed to the skull for head fixation.

## InjectionCannula
Records an implanted guide or injection cannula used to deliver substances to a target, with its gauge and delivery target. Use it for repeated local infusions through a chronic implant.

## LEDArray
Records an array of LEDs used for optical stimulation, with peak emission wavelength, LED count and pitch, maximum power per LED and the targeted opsin.

## MicroperfusionLine
Records a line for local microperfusion of a solution into tissue, with its configured flow rate and the solution it carries.

## Microphone
Records a microphone capturing sound from the subject or setup, such as ultrasonic vocalizations, with its placement and sampling rate.

## MicroscopeObjective
Records the objective used to image the subject or specimen, with magnification, numerical aperture and working distance. Use it for benchtop systems such as two-photon or confocal microscopes.

## Miniscope
Records a head-mounted miniature microscope, with its field of view and frame rate. It is typically mounted over a GRIN lens, prism or cranial window.

## MultiElectrodeArray
Records a multi-electrode array, for example a planar MEA under a slice or culture, with electrode count, pitch and diameter, the substrate type and the reference configuration.

## NerveCuff
Records a cuff electrode placed around a peripheral nerve, with the nerve, number of contacts and cuff size.

## Olfactometer
Describes how odors were delivered to the subject, with the delivery method, the experimental context and the stimulation paradigm. Use it for computer-controlled olfactometers and other odor delivery setups.

## OpticFiber
Records an implanted optic fiber for optogenetic stimulation or fiber photometry, with the output power measured from the finished assembly on the bench before implantation.

## OsmoticPump
Records an implanted osmotic pump for continuous drug delivery, with the delivered agent, nominal flow rate, reservoir volume and expected delivery duration.

## PatchPipette
Records a pipette used for patch-clamp recording, with the patch configuration, pipette resistance in the bath and the seal resistance achieved.

## Prism
Records an implanted microprism that redirects the optical path for imaging, for example to view cortical layers in a vertical plane.

## ReferenceElectrode
Records the electrode that serves as the reference for an electrophysiology recording, with the anatomical or apparatus site where it is placed.

## RespiratorySensor
Represents a sensor that monitors the subject's breathing, such as a nasal thermistor, thermocouple, pressure sensor or plethysmograph.

## SiliconProbe
Records an implanted or acutely inserted silicon probe, such as a Neuropixels or multishank probe, with active channel count, configured shank count and reference configuration. Recordings name the probe, so its target region and coordinates travel with the data.

## SingleWireElectrode
Records a single-wire electrode, for example for local field potential or multiunit recording, with its wire material and impedance.

## StimulatingElectrode
Records an electrode used to deliver electrical stimulation, with the number of active contacts and the stimulation mode it supports. Use it for microstimulation and deep brain stimulation electrodes.

## TMSCoil
Records a transcranial magnetic stimulation coil, with the coil type and its position and orientation relative to the target.

## TactileStimulator
Describes how tactile stimuli were applied, with the stimulus types, the stimulated site such as the whisker pad or hindpaw, the delivery method, the experimental context and the stimulation paradigm.

## TargetSpecimens
Lists the specimens an ex-vivo interface targets, with each specimen's role relative to the interface and notes on the association.

## Tetrode
Records a set of tetrodes, for example in a microdrive, with the number of tetrodes and the wire material.

## ThermalProbe
Records a probe that heats, cools or measures the temperature of tissue or the subject, with its operating or measurement temperature range and the contact site.

## TrackingSystem
Records a system that tracks the subject's position or movement, with the sensing method and the markers or features it tracks. Use it for motion capture and marker- or LED-based tracking.

## TungstenMicroelectrode
Records a tungsten microelectrode for single-unit recording, with impedance at 1 kHz, tip and shaft diameter and the reference configuration.

## UltrasoundTransducer
Records a transducer used for ultrasound stimulation, with its center frequency and focal geometry or distance.

## VisualStimulator
Describes how visual stimuli were presented, with the stimulus types, presentation device, position in the visual field, experimental context and stimulation paradigm.

## WidefieldMacroscope
Records a widefield fluorescence macroscope for mesoscale imaging, with objective magnification, field of view, excitation and emission wavelengths, frame rate and the fluorescent indicator imaged.
