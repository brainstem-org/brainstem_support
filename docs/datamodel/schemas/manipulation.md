---
layout: default
title: Manipulation types
parent: Schemas
grand_parent: Data model
nav_order: 3
---

# Manipulation types
{: .no_toc}

Various manipulation types are available to modulate neural activity, study brain function, and potentially treat neurological and psychiatric disorders.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Electrical and Magnetic Stimulation

### Deep brain stimulation (DBS)

A neurosurgical procedure that involves implanting electrodes in specific areas of the brain to deliver electrical impulses. It's used to treat a variety of neurological conditions, including Parkinson's disease and essential tremor.

| Field | Description |
|:------|:------------|
| `Amplitude (A)` | The intensity of the electrical stimulus applied (float; measured in amperes). Determines the strength of the stimulus |
| `Duration (s)` | The length of time each stimulation lasts (float, ≥ 0; measured in seconds). Affects the total exposure |
| `Stimulation profile` | The pattern or waveform of the electrical signal (string; enum). Options include: Amplitude Modulated, Biphasic, Burst, Chirp, etc. Each designed to target specific neural mechanisms |
| `Duty cycle` | The proportion of one period during which stimulation is active (float, ≥ 0; fraction). Affects overall stimulation intensity |
| `Repetitions` | Number of times the stimulation cycle is repeated (integer, ≥ 0). More repetitions can enhance therapeutic effects |
| `Injection polarity` | The polarity of the stimulation (string). Specifies whether anodal or cathodal, influencing current flow direction |
| `Closed loop` | Whether the system uses real-time feedback (boolean). Enables dynamic adjustment of parameters based on neural response |

### Electrical stimulation

The application of electrical currents to neurons or neural tissues to activate or inhibit neural activity. This broad category includes both invasive methods like intracortical microstimulation and non-invasive approaches.

| Field | Description |
|:------|:------------|
| `Amplitude (V)` | The magnitude of the electrical voltage applied (float; measured in volts). Determines the strength of the stimulus |
| `Duration (s)` | Length of time for which stimulation is applied (float, ≥ 0; measured in seconds). Affects therapeutic efficacy and safety |
| `Stimulation profile` | The pattern or waveform of the electrical signal (string; enum). Options include: Amplitude Modulated, Biphasic, Burst, Chirp, etc. Each designed to achieve specific physiological responses |
| `Duty cycle` | The proportion of the stimulation cycle during which stimulus is active (float, ≥ 0; fraction). Affects total energy delivered during therapy |
| `Repetitions` | Number of times the stimulation is repeated (integer, ≥ 0). More repetitions can increase effects but also risk of adverse reactions |
| `Injection polarity` | Direction of current flow in the stimulation (string). Important for achieving desired effect on neural tissues |
| `Closed loop` | Whether parameters adjust based on real-time feedback (boolean). Enhances precision and safety of the treatment |

### Electromagnetic field stimulation

Involves the use of magnetic or electric fields to modulate neuronal activity. This non-invasive method can influence brain function and is studied for therapeutic potential in psychiatric and neurological disorders.

| Field | Description |
|:------|:------------|
| `Amplitude (V)` | The intensity of the electromagnetic field applied (float; measured in volts/meter). Determines the strength of the electromagnetic influence |
| `Duration (s)` | Length of time the field is applied (float, ≥ 0; measured in seconds). Duration impacts therapeutic efficacy and safety |
| `Stimulation profile` | The waveform of the electromagnetic field (string; enum). Options include: Amplitude Modulated, Biphasic, Burst, Chirp, etc. Different profiles target specific cellular mechanisms |
| `Duty cycle` | Proportion of time the field is active (float, ≥ 0; fraction). Affects the total energy delivered and influences treatment outcome |
| `Repetitions` | Number of field application cycles (integer, ≥ 0). Higher repetitions may increase efficacy but also risk of adverse effects |
| `Injection polarity` | Polarity of the electromagnetic field (string). Affects direction of ion flow and neuronal excitation |
| `Closed loop` | Whether field parameters adjust based on feedback (boolean). Enhances safety and efficacy through dynamic optimization |

### Transcranial Electrical Stimulation

A non-invasive method that applies electrical currents through the scalp and skull to modulate neuronal activity in the brain, used for research and therapeutic purposes.

| Field | Description |
|:------|:------------|
| `Amplitude (mA)` | The intensity of the electrical current applied (float; measured in milliamperes). Influences the depth and effect of stimulation |
| `Duration (s)` | Length of time each stimulation session lasts (float, ≥ 0; measured in seconds). Affects how long brain regions are stimulated |
| `Stimulation profile` | The pattern or waveform of the electrical signal (string; enum). Options include: Amplitude Modulated, Biphasic, Burst, etc. Different profiles achieve varying neurological effects |
| `Duty cycle` | The proportion of stimulation 'on' time to total cycle time (float, ≥ 0; fraction). Affects the therapy's effectiveness and comfort |
| `Repetitions` | Number of times the stimulation cycle is repeated (integer, ≥ 0). Multiple repetitions can enhance stimulation effects |
| `Injection polarity` | Direction of current flow in the stimulation (string). Important for targeting specific brain regions |
| `Closed loop` | Whether parameters adjust based on feedback (boolean). Enables adaptive stimulation based on neural response |

### Transcranial Magnetic Stimulation (TMS)

A non-invasive technique that uses magnetic fields to induce electrical currents in the brain, capable of modulating neural activity and used for both research and treatment of various neurological and psychiatric conditions.

| Field | Description |
|:------|:------------|
| `Amplitude (mA)` | The intensity of the magnetic stimulation (float; measured in milliamperes). Determines the strength of induced currents |
| `Duration (s)` | Length of time each stimulation pulse lasts (float, ≥ 0; measured in seconds). Critical for protocol effectiveness |
| `Stimulation profile` | The pattern of magnetic pulses (string; enum). Options include: Amplitude Modulated, Burst, Single Pulse, etc. Different patterns target specific neural processes |
| `Duty cycle` | The proportion of active stimulation time (float, ≥ 0; fraction). Affects overall stimulation dosage and safety |
| `Repetitions` | Number of stimulation cycles delivered (integer, ≥ 0). Multiple cycles can enhance therapeutic effects |
| `Injection polarity` | Direction of the induced current flow (string). Determines the orientation of neural activation |
| `Closed loop` | Whether stimulation adjusts based on neural feedback (boolean). Enables precise control of neural modulation |

## Optical, Thermal, and Ultrasound Stimulation

### Optogenetic stimulation

Uses light to control neurons that have been genetically modified to express light-sensitive ion channels. This precise method enables the activation or inhibition of specific neuronal populations with high temporal resolution.

| Field | Description |
|:------|:------------|
| `Power (mW)` | Output power of the light source (float; measured in milliwatts). Affects the intensity and efficacy of stimulation |
| `Amplitude (A)` | Peak amplitude of the light signal (float; measured in amperes). Influences activation threshold of optogenetic actuators |
| `Stimulation profile` | Pattern or waveform of the light used (string; enum). Options include: Amplitude Modulated, Biphasic, Burst, etc. Critical for achieving specific responses |
| `Duration (s)` | Length of time each light stimulation lasts (float, ≥ 0; measured in seconds). Crucial for timing channel activation/deactivation |
| `Duty cycle` | Fraction of period during which light is active (float, ≥ 0; fraction). Impacts temporal dynamics of light exposure |
| `Repetitions` | Number of times the stimulation is repeated (integer, ≥ 0). Important for protocols requiring multiple activations |
| `Wavelength (nm)` | Wavelength of the light used (float; measured in nanometers). Selected based on optogenetic actuator properties |
| `Closed loop` | Whether parameters adjust based on feedback (boolean). Enables precise control based on neural response |

### Thermal perturbation

The application of heat or cold to neural tissue to study the effects of temperature changes on neural activity, function, or structural integrity.

| Field | Description |
|:------|:------------|
| `Amplitude (°C)` | Maximum change in temperature from baseline (float; measured in Celsius). Defines intensity of thermal stimulus |
| `Duration (s)` | Length of time thermal stimulus is applied (float, ≥ 0; measured in seconds). Affects tissue response and safety |
| `Thermal profile` | Pattern of temperature variation (string; enum). Options include: Step Function, Ramp, etc. Influences thermal response |
| `Duty cycle` | Fraction of period during which stimulus is active (float, ≥ 0; fraction). Important for cyclic thermal tests |
| `Repetitions` | Number of thermal cycles applied (integer, ≥ 0). Critical for studying repeated exposure effects |
| `Closed loop` | Whether temperature adjusts based on feedback (boolean). Maintains precise temperature control |

### Ultrasound stimulation

Utilizes high-frequency sound waves to non-invasively modulate neural activity. This method has potential applications in both research and clinical settings for mapping brain function and treating neurological disorders.

| Field | Description |
|:------|:------------|
| `Amplitude (V)` | Intensity of ultrasound waves (float; measured in volts). Determines stimulation strength and penetration depth |
| `Duration (s)` | Length of time ultrasound is applied (float, ≥ 0; measured in seconds). Influences therapeutic outcomes |
| `Duty cycle` | Ratio of 'on' time to total period (float, ≥ 0; fraction). Impacts intensity and treatment effect |
| `Stimulation profile` | Pattern of ultrasound waves used (string; enum). Options include: Continuous Wave, Pulsed, etc. Affects biological impact |
| `Repetitions` | Number of ultrasound cycles (integer, ≥ 0). Affects cumulative dose and efficacy |
| `Injection polarity` | Orientation of ultrasound wave propagation (string). Determines direction of mechanical forces |
| `Closed loop` | Whether parameters adjust based on feedback (boolean). Enables dynamic response to physiological changes |

## Chemical and Pharmacological Perturbations

### Liquid perturbation

Introduces liquids into the brain environment to study the effects of various substances or to physically disrupt brain activity. This can include the injection of drugs, solutions, or other compounds.

| Field | Description |
|:------|:------------|
| `Liquid agent` | Type or name of the liquid agent used (string). Specifies the drug, nutrient solution, or compound |
| `Concentration (mg/mL)` | Concentration of the liquid agent (float, ≥ 0; measured in mg/mL). Crucial for ensuring desired potency |
| `Volume (µL)` | Total volume administered (float, ≥ 0; measured in microliters). Determines quantity of agent delivered |
| `Perturbation profile` | Method of liquid delivery (string; enum). Options include: Bolus Injection, Continuous Infusion, etc. Affects system impact |
| `Repetitions` | Number of perturbation cycles (integer, ≥ 0). Important for multiple dosage protocols |
| `Flow rate (µL/min)` | Rate of liquid agent administration (float; measured in µL/min). Influences spread and effect timing |
| `Closed loop` | Whether delivery adjusts based on feedback (boolean). Enables automated flow adjustment |

### Micro perfusion

A technique that allows the localized delivery of substances directly to a targeted area of the brain through a fine cannula, enabling the study of the effects of drugs or other agents on specific brain regions.

| Field | Description |
|:------|:------------|
| `Liquid agent` | Type or name of the perfusion agent (string). Specifies the drug, dye, or solution used |
| `Concentration (mg/mL)` | Concentration of the agent (float, ≥ 0; measured in mg/mL). Critical for physiological impact |
| `Volume (µL)` | Total volume perfused (float, ≥ 0; measured in microliters). Determines extent of tissue exposure |
| `Perturbation profile` | Method of perfusion delivery (string; enum). Options include: Continuous, Pulsed, etc. Affects distribution |
| `Repetitions` | Number of perfusion cycles (integer, ≥ 0). Important for repeated exposure studies |
| `Flow rate (µL/min)` | Rate of agent delivery (float; measured in µL/min). Controls speed and spread of agent |
| `Closed loop` | Whether perfusion adjusts with feedback (boolean). Enables automated delivery control |

### Pharmacological injection

The direct injection of drugs or other substances into the body or directly into brain tissue to study their effects on neural activity, brain function, or behavior.

| Field | Description |
|:------|:------------|
| `Liquid agent` | Type or name of the drug/compound (string). Specifies the pharmacological agent used |
| `Concentration (mg/mL)` | Concentration of active ingredient (float, ≥ 0; measured in mg/mL). Essential for dosing accuracy |
| `Volume (µL)` | Total injection volume (float, ≥ 0; measured in microliters). Critical for precise administration |
| `Injection profile` | Method of drug delivery (string; enum). Options include: Bolus, Continuous, etc. Affects pharmacokinetics |
| `Repetitions` | Number of injections (integer, ≥ 0). Important for multiple dose protocols |
| `Flow rate (µL/min)` | Rate of injection (float; measured in µL/min). Influences absorption and effect onset |
| `Closed loop` | Whether delivery adjusts with feedback (boolean). Enables automated dose optimization |

### Pharmacological superfusion

A technique where drugs are applied directly to neural tissues or cells in a controlled manner, often using a perfusion system, allowing for the study of drug effects on neural activity in vitro.

| Field | Description |
|:------|:------------|
| `Liquid agent` | Type or name of superfusion agent (string). Specifies the chemical or drug applied |
| `Concentration (mg/mL)` | Agent concentration in solution (float, ≥ 0; measured in mg/mL). Critical for biological effect |
| `Volume (µL)` | Total volume used (float, ≥ 0; measured in microliters). Determines exposure extent |
| `Superfusion profile` | Method of application (string; enum). Options include: Continuous, Pulsed, etc. Affects tissue exposure |
| `Repetitions` | Number of application cycles (integer, ≥ 0). Important for repeated exposure protocols |
| `Flow rate (µL/min)` | Rate of agent application (float; measured in µL/min). Controls delivery speed and coverage |
| `Closed loop` | Whether parameters adjust with feedback (boolean). Enables automated flow control |

### Pharmacological inhalation

Involves the administration of drugs in vapor form so that they are inhaled and absorbed through the lungs, affecting the brain. This method is used to study the effects of inhaled substances on neural activity and behavior.

| Field | Description |
|:------|:------------|
| `Liquid agent` | Type or name of inhalation agent (string). Specifies the substance being administered |
| `Concentration (mg/mL)` | Agent concentration in mixture (float, ≥ 0; measured in mg/mL). Crucial for dosing |
| `Stimulation profile` | Pattern of inhalation delivery (string; enum). Options include: Continuous, Pulsed, etc. Affects absorption |
| `Flow rate (µL/min)` | Rate of agent delivery (float; measured in µL/min). Controls administration speed |
| `Volume (µL)` | Total agent volume (float, ≥ 0; measured in microliters). Important for dose calculation |
| `Repetitions` | Number of inhalation cycles (integer, ≥ 0). Important for multiple dose protocols |
| `Analgesic` | Whether agent has pain-relieving properties (string). Details analgesic effects |
| `Sedative` | Whether agent has sedative properties (string). Details sedative components |
| `Closed loop` | Whether delivery adjusts with feedback (boolean). Enables automated dose control |

## Sensory Stimulation

### Odor stimulation

Odor stimulation is the controlled application of olfactory stimuli to investigate neural mechanisms of smell perception, cognitive processing, and brain activity. This technique explores how chemical compounds interact with sensory systems, providing insights into olfactory perception, memory.

| Field | Description |
|:------|:------------|
| `Odor presented` | Specific chemical or compound administered (string). Identifies the stimulus |
| `Concentration (mg/mL)` | Odor concentration in the delivery medium (float; ≥ 0). Determines stimulus intensity |
| `Flow rate (mL/min)` | Rate of odor delivery (float; ≥ 0). Affects exposure and dispersion |
| `Repetitions` | Number of odor presentations (integer, ≥ 0). Important for repeated exposure protocols |
| `Inhalation phase` | Specific respiratory cycle for odor delivery (string; enum). Allows precise timing |
| `Closed loop` | Whether parameters adjust with physiological feedback (boolean). Enables adaptive delivery |


### Sound stimulation

The use of auditory stimuli to influence brain activity and study the neural mechanisms of hearing, perception, and cognition, as well as the therapeutic effects of sound.

| Field | Description |
|:------|:------------|
| `Amplitude (dB)` | Sound pressure level (float; measured in decibels). Determines stimulus loudness |
| `Duration (s)` | Length of sound presentation (float, ≥ 0; measured in seconds). Affects exposure time |
| `Stimulation profile` | Pattern of sound delivery (string; enum). Options include: Pure Tone, White Noise, etc. Affects neural response |
| `Duty cycle` | Ratio of sound-on to total period (float, ≥ 0; fraction). Important for patterned stimuli |
| `Repetitions` | Number of sound presentations (integer, ≥ 0). Critical for studying repeated exposure |
| `Closed loop` | Whether parameters adjust with feedback (boolean). Enables adaptive sound delivery |

## API access

The API allows for programmable access to Manipulations, enabling you to read, edit, and delete manipulations through the API. Learn more about the manipulations' fields and data structure on the [Manipulation API page]({{"api/schemas/manipulation/"|absolute_url}}).