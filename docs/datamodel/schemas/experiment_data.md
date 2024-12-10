---
layout: default
title: Data acquisition types
parent: Schemas
grand_parent: Data model
nav_order: 2
---
# Data acquisition types
{: .no_toc}

A wide range of data acquisition methods are supported to capture various aspects of neuroscience experiments.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Audio and Behavioral Tracking

### Audio

Audio data acquisition captures sound recordings related to the experiment. Used in studies examining auditory processing, communication, and the effects of auditory stimuli on behavior or neural activity.

| Field | Description |
|:------|:------------|
| `Bit depth` | Bit depth of the audio recording |
| `Number of channels` | Number of audio channels |
| `Sampling rate (Hz)` | Sampling rate of the audio in Hertz |
| `Number of samples` | Total number of audio samples |
| `Codec` | Audio codec used for encoding |

### Behavioral Tracking

Behavioral tracking data records the movement and actions of subjects during experiments. This method monitors and records the movements or behaviors of subjects in response to specific conditions or stimuli, essential for understanding the neural basis of behavior, learning, and memory.

| Field | Description |
|:------|:------------|
| `Frame rate (Hz)` | Frame rate of the tracking data in Hertz |
| `Number of frames` | Total number of frames in the tracking data |
| `Vertical resolution` | Vertical resolution of the tracking images or video |
| `Horizontal resolution` | Horizontal resolution of the tracking images or video |

## Electrophysiology

### Electroencephalography (EEG)

EEG data records electrical activity of the brain. The biosignals detected by EEG represent the postsynaptic potentials of pyramidal neurons in the neocortex and allocortex. It is typically non-invasive, with EEG electrodes placed along the scalp using the International 10–20 system or variations. Electrocorticography, involving surgical placement of electrodes, is sometimes called "intracranial EEG". Clinical interpretation is performed by visual inspection or quantitative analysis.

| Field | Description |
|:------|:------------|
| `Data-type` | Data type used for EEG recording |
| `Number of channels` | Number of EEG channels |
| `Sampling rate (Hz)` | Sampling rate of the EEG in Hertz |
| `Number of samples` | Total number of EEG samples |
| `Least significant bit (μV/bit)` | Voltage represented by the least significant bit |
| `Electrode groups` | Groups of electrodes used in the recording |
| `Channel tags` | Tags associated with specific channels |

### Electroneurogram (ENG)

ENG data records electrical activity from peripheral nerves. An electroneurogram is a method used to visualize directly recorded electrical activity of neurons in the central nervous system (brain, spinal cord) or the peripheral nervous system (nerves, ganglions). Similar to an electromyogram (EMG), but focused on neural rather than muscular activity.

| Field | Description |
|:------|:------------|
| `Data-type` | Data type used for ENG recording |
| `Number of channels` | Number of ENG channels |
| `Sampling rate (Hz)` | Sampling rate of the ENG in Hertz |
| `Number of samples` | Total number of ENG samples |
| `Least significant bit (μV/bit)` | Voltage represented by the least significant bit |
| `Electrode groups` | Groups of electrodes used in the recording |
| `Channel tags` | Tags associated with specific channels |

### Extracellular Electrophysiology

Extracellular electrophysiology data records electrical activity from outside cells. In this technique, cells' electrical signals are recorded using electrodes outside the cell. The primary advantages include ease of obtaining recordings, ability to record from numerous neurons simultaneously, and capability to record over days and weeks.

| Field | Description |
|:------|:------------|
| `Data-type` | Data type used for extracellular recording |
| `Number of channels` | Number of recording channels |
| `Sampling rate (Hz)` | Sampling rate of the recording in Hertz |
| `Number of samples` | Total number of samples in the recording |
| `Least significant bit (μV/bit)` | Voltage represented by the least significant bit |
| `Electrode groups` | Groups of electrodes used in the recording |
| `Channel tags` | Tags associated with specific channels |

### Intracellular Electrophysiology

Intracellular electrophysiology data records electrical activity from inside cells. This technique inserts a glass microelectrode into a single cell (usually a neuron) to precisely measure its electrical activity (voltages across or currents passing through the cellular membranes).

| Field | Description |
|:------|:------------|
| `Data-type` | Data type used for intracellular recording |
| `Sampling rate (Hz)` | Sampling rate of the recording in Hertz |
| `Number of channels` | Number of recording channels |
| `Number of samples` | Total number of samples in the recording |
| `Least significant bit (μV/bit)` | Voltage represented by the least significant bit |

## Optical Imaging

### Confocal Microscopy

Confocal microscopy data captures high-resolution optical sections of samples. Most frequently called confocal laser scanning microscopy (CLSM) or laser scanning confocal microscopy (LSCM), it is an optical imaging technique that increases optical resolution and contrast using a spatial pinhole to block out-of-focus light in image formation. Capturing multiple two-dimensional images at different depths enables the reconstruction of three-dimensional structures (optical sectioning) within an object.

| Field | Description |
|:------|:------------|
| `Vertical resolution` | Vertical resolution of the confocal images |
| `Horizontal resolution` | Horizontal resolution of the confocal images |
| `Frame rate (Hz)` | Frame rate of the confocal acquisition in Hertz |
| `Number of frames` | Total number of frames in the confocal data |
| `Laser power (mW)` | Laser power used in milliwatts |
| `Excitation wavelength (nm)` | Excitation wavelength used in nanometers |
| `Imaging depth (μm)` | Depth of imaging in micrometers |
| `Voxel size (X dimension)` | Voxel size in the X dimension |
| `Voxel size (Y dimension)` | Voxel size in the Y dimension |
| `Voxel size (Z dimension)` | Voxel size in the Z dimension |

### Fiber Photometry

Fiber photometry data records fluorescence signals from specific neural populations. It is a calcium imaging technique that captures 'bulk' or population-level calcium (Ca2+) activity from specific cell-types within a brain region or functional network to study neural circuits.

| Field | Description |
|:------|:------------|
| `Frame rate (Hz)` | Frame rate of the photometry acquisition in Hertz |
| `Number of frames` | Total number of frames in the photometry data |
| `Laser power (mW)` | Laser power used in milliwatts |
| `Excitation wavelength (nm)` | Excitation wavelength used in nanometers |

### Light Field Microscopy (LFM)

LFM data captures 3D information in a single shot using an array of microlenses. This scanning-free 3-dimensional microscopic imaging method is based on the theory of light field, allowing sub-second (~10 Hz) large volumetric imaging ([~0.1 to 1 mm]3) with ~1 μm spatial resolution in conditions of weak scattering and semi-transparence.

| Field | Description |
|:------|:------------|
| `Vertical resolution` | Vertical resolution of the LFM images |
| `Horizontal resolution` | Horizontal resolution of the LFM images |
| `Frame rate (Hz)` | Frame rate of the LFM acquisition in Hertz |
| `Number of frames` | Total number of frames in the LFM data |
| `Laser power (mW)` | Laser power used in milliwatts |
| `Excitation wavelength (nm)` | Excitation wavelength used in nanometers |
| `Imaging depth (μm)` | Depth of imaging in micrometers |
| `Voxel size (X dimension)` | Voxel size in the X dimension |
| `Voxel size (Y dimension)` | Voxel size in the Y dimension |
| `Voxel size (Z dimension)` | Voxel size in the Z dimension |

### Miniscope Microscopy

Miniscope microscopy data captures neural activity in freely behaving animals using miniature microscopes. These head-mounted microscopes are light enough for mice and rats to carry without significantly interfering with behavior. They are coupled with implanted gradient-refractive-index (GRIN) lenses or cortical windows for deep and superficial brain imaging.

| Field | Description |
|:------|:------------|
| `Frame rate (Hz)` | Frame rate of the miniscope acquisition in Hertz |
| `Number of frames` | Total number of frames in the miniscope data |
| `Vertical resolution` | Vertical resolution of the miniscope images |
| `Horizontal resolution` | Horizontal resolution of the miniscope images |
| `Laser power (mW)` | Laser power used in milliwatts |
| `Imaging depth (μm)` | Depth of imaging in micrometers |

### Single-Photon Microscopy

Single-photon microscopy data captures fluorescence images using single-photon excitation. This imaging technique allows for the visualization of cellular and subcellular structures in living tissue with high spatial resolution.

| Field | Description |
|:------|:------------|
| `Vertical resolution` | Vertical resolution of the microscopy images |
| `Horizontal resolution` | Horizontal resolution of the microscopy images |
| `Frame rate (Hz)` | Frame rate of the microscopy acquisition in Hertz |
| `Number of frames` | Total number of frames in the microscopy data |
| `Laser power (mW)` | Laser power used in milliwatts |
| `Excitation wavelength (nm)` | Excitation wavelength used in nanometers |
| `Imaging depth (μm)` | Depth of imaging in micrometers |
| `Voxel size (X dimension)` | Voxel size in the X dimension |
| `Voxel size (Y dimension)` | Voxel size in the Y dimension |
| `Voxel size (Z dimension)` | Voxel size in the Z dimension |

### Two-Photon Microscopy

Two-photon microscopy data captures high-resolution images of living tissue using two-photon excitation. This fluorescence imaging technique is particularly well-suited to image scattering living tissue of up to about one millimeter in thickness. Unlike traditional fluorescence microscopy, where the excitation wavelength is shorter than the emission wavelength, two-photon excitation requires simultaneous excitation by two photons with longer wavelength than the emitted light.

| Field | Description |
|:------|:------------|
| `Vertical resolution` | Vertical resolution of the microscopy images |
| `Horizontal resolution` | Horizontal resolution of the microscopy images |
| `Frame rate (Hz)` | Frame rate of the microscopy acquisition in Hertz |
| `Number of frames` | Total number of frames in the microscopy data |
| `Laser power (mW)` | Laser power used in milliwatts |
| `Excitation wavelength (nm)` | Excitation wavelength used in nanometers |
| `Imaging depth (μm)` | Depth of imaging in micrometers |
| `Voxel size (X dimension)` | Voxel size in the X dimension |
| `Voxel size (Y dimension)` | Voxel size in the Y dimension |
| `Voxel size (Z dimension)` | Voxel size in the Z dimension |

### Three-Photon Microscopy

Three-photon microscopy data captures high-resolution images of living tissue using three-photon excitation, allowing for deeper tissue penetration. This high-resolution fluorescence microscopy is based on nonlinear excitation effect. Different from two-photon excitation microscopy, it uses three exciting photons, with the fluorescent dyes emitting one photon whose energy is slightly smaller than three times the energy of each incident photon. The use of near-infrared light results in less tissue scattering effect, providing higher resolution than conventional microscopy.

| Field | Description |
|:------|:------------|
| `Vertical resolution` | Vertical resolution of the microscopy images |
| `Horizontal resolution` | Horizontal resolution of the microscopy images |
| `Frame rate (Hz)` | Frame rate of the microscopy acquisition in Hertz |
| `Number of frames` | Total number of frames in the microscopy data |
| `Laser power (mW)` | Laser power used in milliwatts |
| `Excitation wavelength (nm)` | Excitation wavelength used in nanometers |
| `Imaging depth (μm)` | Depth of imaging in micrometers |
| `Voxel size (X dimension)` | Voxel size in the X dimension |
| `Voxel size (Y dimension)` | Voxel size in the Y dimension |
| `Voxel size (Z dimension)` | Voxel size in the Z dimension |

## Magnetic and Functional Imaging

### Functional Magnetic Resonance Imaging (fMRI)

fMRI data measures brain activity by detecting changes in blood flow. This technique relies on the fact that cerebral blood flow and neuronal activation are coupled, allowing for the visualization of brain activity patterns during various tasks or states.

| Field | Description |
|:------|:------------|
| `Frame rate (Hz)` | Frame rate of the fMRI acquisition in Hertz |
| `Number of frames` | Total number of frames in the fMRI data |
| `Vertical resolution` | Vertical resolution of the fMRI images |
| `Horizontal resolution` | Horizontal resolution of the fMRI images |
| `Imaging depth (μm)` | Depth of imaging in micrometers |
| `Laser power (mW)` | Laser power used in milliwatts (if applicable) |

### Magnetic Resonance Imaging (MRI)

MRI data provides detailed anatomical images of the brain and body. MRI scanners use strong magnetic fields, magnetic field gradients, and radio waves to generate images of the organs in the body. Unlike computed tomography (CT) and positron emission tomography (PET) scans, MRI does not involve X-rays or ionizing radiation.

| Field | Description |
|:------|:------------|
| `Frame rate (Hz)` | Frame rate of the MRI acquisition in Hertz |
| `Number of frames` | Total number of frames in the MRI data |
| `Vertical resolution` | Vertical resolution of the MRI images |
| `Horizontal resolution` | Horizontal resolution of the MRI images |
| `Imaging depth (μm)` | Depth of imaging in micrometers |
| `Laser power (mW)` | Laser power used in milliwatts (if applicable) |

### Magnetoencephalography (MEG)

MEG data records magnetic fields produced by electrical currents in the brain. It is a functional neuroimaging technique that uses very sensitive magnetometers, typically SQUIDs (superconducting quantum interference devices), while SERF (spin exchange relaxation-free) magnetometers are being investigated for future machines.

| Field | Description |
|:------|:------------|
| `Frame rate (Hz)` | Frame rate of the MEG acquisition in Hertz |
| `Number of frames` | Total number of frames in the MEG data |
| `Vertical resolution` | Vertical resolution of the MEG sensors |
| `Horizontal resolution` | Horizontal resolution of the MEG sensors |
| `Laser power (mW)` | Laser power used in milliwatts (if applicable) |
| `Imaging depth (μm)` | Depth of imaging in micrometers (if applicable) |

## Tomography and Ultrasound

### Computed Tomography (CT)

CT data provides detailed cross-sectional images of the subject. A computed tomography scan (formerly called computed axial tomography scan or CAT scan) is a medical imaging technique used to obtain detailed internal images of the body.

| Field | Description |
|:------|:------------|
| `Frame rate (Hz)` | Frame rate of the CT acquisition in Hertz |
| `Number of frames` | Total number of frames in the CT data |
| `Vertical resolution` | Vertical resolution of the CT images |
| `Horizontal resolution` | Horizontal resolution of the CT images |
| `Imaging depth (μm)` | Depth of imaging in micrometers |
| `Laser power (mW)` | Laser power used in milliwatts |

### Positron Emission Tomography (PET)

PET data provides functional images of metabolic processes in the body. This functional imaging technique uses radioactive substances known as radiotracers to visualize and measure changes in metabolic processes, blood flow, regional chemical composition, and absorption. Different tracers are used for various imaging purposes, depending on the target process within the body.

| Field | Description |
|:------|:------------|
| `Frame rate (Hz)` | Frame rate of the PET acquisition in Hertz |
| `Number of frames` | Total number of frames in the PET data |
| `Vertical resolution` | Vertical resolution of the PET images |
| `Horizontal resolution` | Horizontal resolution of the PET images |
| `Imaging depth (μm)` | Depth of imaging in micrometers |
| `Laser power (mW)` | Laser power used in milliwatts (if applicable) |

### Single-photon emission computed tomography (SPECT)

SPECT data provides 3D images of radioactive tracer distribution in the body. It is a nuclear medicine tomographic imaging technique using gamma rays, similar to conventional nuclear medicine planar imaging using a gamma camera (scintigraphy), but able to provide true 3D information.

| Field | Description |
|:------|:------------|
| `Frame rate (Hz)` | Frame rate of the SPECT acquisition in Hertz |
| `Number of frames` | Total number of frames in the SPECT data |
| `Vertical resolution` | Vertical resolution of the SPECT images |
| `Horizontal resolution` | Horizontal resolution of the SPECT images |
| `Imaging depth (μm)` | Depth of imaging in micrometers |
| `Laser power (mW)` | Laser power used in milliwatts (if applicable) |

### Functional Ultrasound Imaging (fUS)

fUS data captures brain activity through changes in blood flow using ultrasound. A medical ultrasound imaging technique for detecting or measuring changes in neural activities or metabolism, typically through measuring blood flow or hemodynamic changes. The method can be seen as an extension of Doppler imaging.

| Field | Description |
|:------|:------------|
| `Frame rate (Hz)` | Frame rate of the fUS acquisition in Hertz |
| `Number of frames` | Total number of frames in the fUS data |
| `Vertical resolution` | Vertical resolution of the fUS images |
| `Horizontal resolution` | Horizontal resolution of the fUS images |
| `Imaging depth (μm)` | Depth of imaging in micrometers |
| `Laser power (mW)` | Laser power used in milliwatts (if applicable) |

## Data acquisition API access

The API allows for programmable access to Data acquisition, enabling you to read, edit, and delete Data acquisition through the API. Learn more about the Data acquisition' fields and data structure on the [Data acquisition API page]({{"api/modules/experimentdata/"|absolute_url}}).