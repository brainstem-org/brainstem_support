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
| `Format` | Digital file format (string; e.g., MP3, WAV). Determines features and compatibility |
| `Compression` | Type of audio compression applied (string). Affects file size and quality |
| `Bit depth` | Number of bits per audio sample (non-negative integer; default: 8 bits). Determines dynamic range and noise level of audio |
| `Codec` | Audio codec used for encoding (string). Affects compatibility and audio quality |
| `Number of channels` | Number of separate audio channels (non-negative integer ≥ 1; default: 2). Represents audio configuration (e.g., mono, stereo) |
| `Sampling rate (Hz)` | Frequency of audio sampling (float; measured in Hz). Determines temporal resolution of recording |
| `Number of samples` | Total count of audio samples (non-negative integer). Used with sampling rate to determine duration |

### Behavioral Tracking

Behavioral tracking data records the movement and procedures of subjects during experiments. This method monitors and records the movements or behaviors of subjects in response to specific conditions or stimuli, essential for understanding the neural basis of behavior, learning, and memory.

| Field | Description |
|:------|:------------|
| `Format` | Digital video/data format (string). Determines compatibility and features |
| `Compression` | Type of data compression used (string). Affects file size and quality |
| `Frame rate (Hz)` | Rate of behavioral data capture (float; measured in Hz). Affects smoothness and accuracy of motion analysis |
| `Number of frames` | Total captured frames (non-negative integer). Determines recording duration |
| `Vertical resolution` | Number of vertical pixels (non-negative integer). Affects vertical detail in tracking video |
| `Horizontal resolution` | Number of horizontal pixels (non-negative integer). Affects horizontal detail in tracking video |

## Electrophysiology

### Electroencephalography (EEG)

EEG data records electrical activity of the brain. The biosignals detected by EEG represent the postsynaptic potentials of pyramidal neurons in the neocortex and allocortex. It is typically non-invasive, with EEG electrodes placed along the scalp using the International 10–20 system or variations.

| Field | Description |
|:------|:------------|
| `Format` | Digital file format (string; e.g., EDF, BDF). Affects compatibility with analysis software |
| `Data-type` | Format of stored data (string; default: 'int16'). Affects precision and size |
| `Number of channels` | Count of EEG recording channels (non-negative integer). Determines spatial coverage |
| `Sampling rate (Hz)` | Sample frequency (float; default: 20000 Hz). Critical for temporal resolution |
| `Number of samples` | Total data points per channel (non-negative integer). Defines recording duration |
| `Least significant bit (μV/bit)` | Smallest detectable voltage change (float; measured in μV/bit). Affects amplitude resolution |
| `Electrode groups` | Groups of electrodes (array of objects with channels list and label). Organizes recording setup |
| `Channel tags` | Channel metadata (array of objects with tag name, channels, and groups). Enhanced data organization |

### Electroneurogram (ENG)

ENG data records electrical activity from peripheral nerves. An electroneurogram is a method used to visualize directly recorded electrical activity of neurons in the central nervous system (brain, spinal cord) or the peripheral nervous system (nerves, ganglions).

| Field | Description |
|:------|:------------|
| `Format` | Digital file format (string). Determines data organization and software compatibility |
| `Data-type` | Format of stored data (string; default: 'int16'). Affects precision and storage requirements |
| `Number of channels` | Count of recording channels (non-negative integer). Determines coverage of neural tissue |
| `Sampling rate (Hz)` | Sample frequency (float; default: 20000 Hz). Essential for capturing rapid neural signals |
| `Number of samples` | Total data points per channel (non-negative integer). Determines recording duration |
| `Least significant bit (μV/bit)` | Smallest detectable voltage change (float; measured in μV/bit). Critical for signal resolution |
| `Electrode groups` | Groups of electrodes (array of objects with channels list and label). Organizes recording configuration |
| `Channel tags` | Channel metadata (array of objects with tag name, channels, and groups). Enhances data organization |

### Extracellular Electrophysiology

Extracellular electrophysiology data records electrical activity from outside cells. In this technique, cells' electrical signals are recorded using electrodes outside the cell. The primary advantages include ease of obtaining recordings, ability to record from numerous neurons simultaneously, and capability to record over days and weeks.

| Field | Description |
|:------|:------------|
| `Format` | Digital file format (string; e.g., Binary, HDF5). Affects data organization and compatibility |
| `Data-type` | Format of stored data (string; default: 'int16'). Affects precision and storage requirements |
| `Number of channels` | Count of recording channels (non-negative integer). Determines spatial sampling of neural tissue |
| `Sampling rate (Hz)` | Sample frequency (float; default: 20000 Hz). Critical for capturing neural spike timing |
| `Number of samples` | Total data points per channel (non-negative integer). Defines total recording duration |
| `Least significant bit (μV/bit)` | Smallest detectable voltage change (float; measured in μV/bit). Influences signal resolution |
| `Electrode groups` | Groups of electrodes (array of objects with channels list and label). Organizes recording setup |
| `Channel tags` | Channel metadata (array of objects). Includes tag name, channels, and group information |

### Intracellular Electrophysiology 

Intracellular electrophysiology data records electrical activity from inside cells. This technique inserts a glass microelectrode into a single cell (usually a neuron) to precisely measure its electrical activity (voltages across or currents passing through the cellular membranes).

| Field | Description |
|:------|:------------|
| `Format` | Digital file format (string; e.g., ABF, DAT). Determines data organization and compatibility |
| `Data-type` | Format of stored data (string; default: 'int16'). Determines precision and file size |
| `Sampling rate (Hz)` | Sample frequency (float). Essential for capturing membrane potential changes |
| `Number of channels` | Count of recording channels (non-negative integer). Typically fewer than extracellular |
| `Number of samples` | Total data points per channel (non-negative integer). Determines recording length |
| `Least significant bit (μV/bit)` | Smallest detectable voltage change (float; measured in μV/bit). Critical for signal resolution |

## Optical Imaging

### Fiber Photometry

Fiber photometry data records fluorescence signals from specific neural populations. It is a calcium imaging technique that captures 'bulk' or population-level calcium (Ca2+) activity from specific cell-types within a brain region or functional network to study neural circuits.

| Field | Description |
|:------|:------------|
| `Format` | Digital format (string; e.g., CSV). Determines data organization and compatibility |
| `Compression` | Data compression type (string). Affects file size and processing speed |
| `Frame rate (Hz)` | Signal sampling frequency (float; measured in Hz). Critical for temporal resolution |
| `Number of frames` | Total recorded frames (non-negative integer). Determines recording duration |
| `Laser power (mW)` | Excitation laser strength (float; measured in mW). Affects signal strength |
| `Excitation wavelength (nm)` | Excitation light wavelength (float; measured in nm). Matches fluorophore properties |

### Miniscope Microscopy

Miniscope microscopy data captures neural activity in freely behaving animals using miniature microscopes. These head-mounted microscopes are light enough for mice and rats to carry without significantly interfering with behavior. They are coupled with implanted gradient-refractive-index (GRIN) lenses or cortical windows for deep and superficial brain imaging.

| Field | Description |
|:------|:------------|
| `Format` | Digital format (string; e.g., AVI). Determines compatibility and features |
| `Compression` | Video compression type (string). Affects file size and quality |
| `Frame rate (Hz)` | Image capture frequency (float; measured in Hz). Critical for neural dynamics |
| `Number of frames` | Total recorded frames (non-negative integer). Defines recording duration |
| `Vertical resolution` | Pixels in vertical dimension (non-negative integer). Affects image detail |
| `Horizontal resolution` | Pixels in horizontal dimension (non-negative integer). Determines image clarity |
| `Laser power (mW)` | LED/laser illumination power (float; measured in mW). Affects image brightness |
| `Imaging depth (μm)` | Maximum imaging depth (float; measured in μm). Important for targeting |

### Confocal Microscopy

Confocal microscopy data captures high-resolution optical sections of samples. Most frequently called confocal laser scanning microscopy (CLSM) or laser scanning confocal microscopy (LSCM), it is an optical imaging technique that increases optical resolution and contrast using a spatial pinhole to block out-of-focus light in image formation.

| Field | Description |
|:------|:------------|
| `Format` | Digital format (string; e.g., TIFF). Determines compatibility and features |
| `Compression` | Data compression method (string). Affects file size and quality |
| `Vertical resolution` | Number of pixels in vertical dimension (non-negative integer). Affects image clarity |
| `Horizontal resolution` | Number of pixels in horizontal dimension (non-negative integer). Determines image sharpness |
| `Frame rate (Hz)` | Image capture frequency (float; measured in Hz). Important for time-lapse imaging |
| `Number of frames` | Total captured frames (non-negative integer). Defines recording duration |
| `Laser power (mW)` | Laser illumination strength (float; measured in mW). Affects image quality |
| `Excitation wavelength (nm)` | Wavelength of excitation light (float; measured in nm). Critical for fluorophore excitation |
| `Imaging depth (μm)` | Maximum imaging depth (float; measured in μm). Important for thick specimens |
| `Voxel size (X dimension)` | X-axis voxel size (float; measured in μm). Affects spatial resolution |
| `Voxel size (Y dimension)` | Y-axis voxel size (float; measured in μm). Impacts structural detail |
| `Voxel size (Z dimension)` | Z-axis voxel size (float; measured in μm). Critical for 3D reconstruction |

### Light Field Microscopy (LFM)

LFM data captures 3D information in a single shot using an array of microlenses. This scanning-free 3-dimensional microscopic imaging method is based on the theory of light field, allowing sub-second (~10 Hz) large volumetric imaging ([~0.1 to 1 mm]3) with ~1 μm spatial resolution in conditions of weak scattering and semi-transparence.

| Field | Description |
|:------|:------------|
| `Format` | Digital format (string; e.g., TIFF). Affects data compatibility and features |
| `Compression` | Data compression method (string). Impacts file size and quality |
| `Vertical resolution` | Number of pixels in vertical dimension (non-negative integer). Affects image detail |
| `Horizontal resolution` | Number of pixels in horizontal dimension (non-negative integer). Impacts image clarity |
| `Frame rate (Hz)` | Image capture frequency (float; measured in Hz). Critical for dynamic studies |
| `Number of frames` | Total captured frames (non-negative integer). Determines acquisition duration |
| `Laser power (mW)` | Laser illumination power (float; measured in mW). Affects penetration depth |
| `Excitation wavelength (nm)` | Excitation light wavelength (float; measured in nm). Optimized for sample properties |
| `Imaging depth (μm)` | Maximum imaging depth (float; measured in μm). Important for thick specimens |
| `Voxel size (X dimension)` | X-axis voxel size (float; measured in μm). Determines spatial resolution |
| `Voxel size (Y dimension)` | Y-axis voxel size (float; measured in μm). Affects structural detail |
| `Voxel size (Z dimension)` | Z-axis voxel size (float; measured in μm). Critical for 3D reconstruction |


### Single-Photon Microscopy

Single-photon microscopy data captures fluorescence images using single-photon excitation. This imaging technique allows for the visualization of cellular and subcellular structures in living tissue with high spatial resolution.

| Field | Description |
|:------|:------------|
| `Format` | Digital format (string; e.g., TIFF). Affects compatibility |
| `Compression` | Data compression method (string). Impacts file size and quality |
| `Vertical resolution` | Number of pixels vertically (non-negative integer). Affects image detail |
| `Horizontal resolution` | Number of pixels horizontally (non-negative integer). Impacts image clarity |
| `Frame rate (Hz)` | Image capture frequency (float; measured in Hz). Important for time-lapse |
| `Number of frames` | Total captured frames (non-negative integer). Determines recording length |
| `Laser power (mW)` | Excitation laser strength (float; measured in mW). Critical for signal |
| `Excitation wavelength (nm)` | Excitation light wavelength (float; measured in nm). Matches fluorophores |
| `Imaging depth (μm)` | Maximum imaging depth (float; measured in μm). Limited by scattering |
| `Voxel size (X dimension)` | X-axis voxel size (float; measured in μm). Affects resolution |
| `Voxel size (Y dimension)` | Y-axis voxel size (float; measured in μm). Determines detail |
| `Voxel size (Z dimension)` | Z-axis voxel size (float; measured in μm). Important for 3D |

### Two-Photon Microscopy

Two-photon microscopy data captures high-resolution images of living tissue using two-photon excitation. This fluorescence imaging technique is particularly well-suited to image scattering living tissue of up to about one millimeter in thickness. Unlike traditional fluorescence microscopy, where the excitation wavelength is shorter than the emission wavelength, two-photon excitation requires simultaneous excitation by two photons with longer wavelength than the emitted light.

| Field | Description |
|:------|:------------|
| `Format` | Digital format (string). Determines data organization |
| `Compression` | Data compression type (string). Affects storage efficiency |
| `Vertical resolution` | Number of pixels vertically (non-negative integer). Affects image clarity |
| `Horizontal resolution` | Number of pixels horizontally (non-negative integer). Determines detail |
| `Frame rate (Hz)` | Image capture frequency (float; measured in Hz). For dynamic imaging |
| `Number of frames` | Total captured frames (non-negative integer). Recording duration |
| `Laser power (mW)` | Two-photon laser power (float; measured in mW). Critical for excitation |
| `Excitation wavelength (nm)` | Excitation wavelength (float; measured in nm). Typically infrared |
| `Imaging depth (μm)` | Maximum imaging depth (float; measured in μm). Superior to single-photon |
| `Voxel size (X dimension)` | X-axis voxel size (float; measured in μm). Spatial resolution |
| `Voxel size (Y dimension)` | Y-axis voxel size (float; measured in μm). Detail level |
| `Voxel size (Z dimension)` | Z-axis voxel size (float; measured in μm). Depth resolution |

### Three-Photon Microscopy

Three-photon microscopy data captures high-resolution images of living tissue using three-photon excitation, allowing for deeper tissue penetration. This high-resolution fluorescence microscopy is based on nonlinear excitation effect. Different from two-photon excitation microscopy, it uses three exciting photons, with the fluorescent dyes emitting one photon whose energy is slightly smaller than three times the energy of each incident photon.

| Field | Description |
|:------|:------------|
| `Format` | Digital format (string). Determines data organization |
| `Compression` | Data compression type (string). Affects storage efficiency |
| `Vertical resolution` | Number of pixels vertically (non-negative integer). Affects image detail |
| `Horizontal resolution` | Number of pixels horizontally (non-negative integer). Determines clarity |
| `Frame rate (Hz)` | Image capture frequency (float; measured in Hz). For dynamic studies |
| `Number of frames` | Total captured frames (non-negative integer). Defines recording duration |
| `Laser power (mW)` | Three-photon laser power (float; measured in mW). Critical for deep imaging |
| `Excitation wavelength (nm)` | Excitation wavelength (float; measured in nm). Typically far infrared |
| `Imaging depth (μm)` | Maximum imaging depth (float; measured in μm). Superior penetration |
| `Voxel size (X dimension)` | X-axis voxel size (float; measured in μm). Spatial resolution |
| `Voxel size (Y dimension)` | Y-axis voxel size (float; measured in μm). Detail level |
| `Voxel size (Z dimension)` | Z-axis voxel size (float; measured in μm). Depth resolution |

## Magnetic and Functional Imaging

### Magnetic Resonance Imaging (MRI)

MRI data provides detailed anatomical images of the brain and body. MRI scanners use strong magnetic fields, magnetic field gradients, and radio waves to generate images of the organs in the body. Unlike computed tomography (CT) and positron emission tomography (PET) scans, MRI does not involve X-rays or ionizing radiation.

| Field | Description |
|:------|:------------|
| `Format` | Digital format (string; e.g., DICOM). Data organization |
| `Compression` | Compression method (string). Storage efficiency |
| `Frame rate (Hz)` | Image acquisition speed (float; measured in Hz). For dynamic studies |
| `Number of frames` | Total image frames (non-negative integer). Scan duration |
| `Vertical resolution` | Vertical pixels (non-negative integer). Image detail |
| `Horizontal resolution` | Horizontal pixels (non-negative integer). Spatial clarity |

### Functional Magnetic Resonance Imaging (fMRI)

fMRI data measures brain activity by detecting changes in blood flow. This technique relies on the fact that cerebral blood flow and neuronal activation are coupled, allowing for the visualization of brain activity patterns during various tasks or states.

| Field | Description |
|:------|:------------|
| `Format` | Digital format (string; e.g., NIfTI, DICOM). Affects compatibility |
| `Compression` | Data compression method (string). Impacts file size |
| `Frame rate (Hz)` | Image acquisition rate (float; measured in Hz). Temporal resolution |
| `Number of frames` | Total acquired frames (non-negative integer). Experiment duration |
| `Vertical resolution` | Vertical pixels (non-negative integer). Affects image detail |
| `Horizontal resolution` | Horizontal pixels (non-negative integer). Determines image clarity |

### Magnetoencephalography (MEG)

MEG data records magnetic fields produced by electrical currents in the brain. It is a functional neuroimaging technique that uses very sensitive magnetometers, typically SQUIDs (superconducting quantum interference devices), while SERF (spin exchange relaxation-free) magnetometers are being investigated for future machines.

| Field | Description |
|:------|:------------|
| `Format` | Digital format (string; e.g., FIFF). Data organization |
| `Compression` | Data compression (string). Storage efficiency |
| `Frame rate (Hz)` | Sampling frequency (float; measured in Hz). Temporal resolution |
| `Number of frames` | Total data points (non-negative integer). Recording duration |

## Tomography and Ultrasound

### Computed Tomography (CT)

CT data provides detailed cross-sectional images of the subject. A computed tomography scan (formerly called computed axial tomography scan or CAT scan) is a medical imaging technique used to obtain detailed internal images of the body.

| Field | Description |
|:------|:------------|
| `Format` | Digital format (string; e.g., DICOM). Determines compatibility |
| `Compression` | Data compression method (string). Storage efficiency |
| `Frame rate (Hz)` | Scan acquisition rate (float; measured in Hz). Temporal resolution |
| `Number of frames` | Total scan frames (non-negative integer). Acquisition duration |
| `Vertical resolution` | Vertical pixels (non-negative integer). Image detail level |
| `Horizontal resolution` | Horizontal pixels (non-negative integer). Spatial resolution |
| `Imaging depth (μm)` | Depth measurement (float; measured in μm). Penetration capability |

### Positron Emission Tomography (PET)

PET data provides functional images of metabolic processes in the body. This functional imaging technique uses radioactive substances known as radiotracers to visualize and measure changes in metabolic processes, blood flow, regional chemical composition, and absorption. Different tracers are used for various imaging purposes, depending on the target process within the body.

| Field | Description |
|:------|:------------|
| `Format` | Digital format (string; e.g., DICOM). Data organization standard |
| `Compression` | Compression method (string). Affects storage size |
| `Frame rate (Hz)` | Acquisition rate (float; measured in Hz). For dynamic studies |
| `Number of frames` | Total data frames (non-negative integer). Scan duration |
| `Vertical resolution` | Vertical pixels (non-negative integer). Image detail |
| `Horizontal resolution` | Horizontal pixels (non-negative integer). Spatial clarity |

### Single-photon emission computed tomography (SPECT)

SPECT data provides 3D images of radioactive tracer distribution in the body. It is a nuclear medicine tomographic imaging technique using gamma rays, similar to conventional nuclear medicine planar imaging using a gamma camera (scintigraphy), but able to provide true 3D information.

| Field | Description |
|:------|:------------|
| `Format` | Digital format (string; e.g., DICOM). Data structure standard |
| `Compression` | Compression method (string). File size optimization |
| `Frame rate (Hz)` | Image acquisition rate (float; measured in Hz). Temporal detail |
| `Number of frames` | Total acquired frames (non-negative integer). Study duration |
| `Vertical resolution` | Vertical pixels (non-negative integer). Image resolution |
| `Horizontal resolution` | Horizontal pixels (non-negative integer). Spatial detail |

### Functional Ultrasound Imaging (fUS)

fUS data captures brain activity through changes in blood flow using ultrasound. A medical ultrasound imaging technique for detecting or measuring changes in neural activities or metabolism, typically through measuring blood flow or hemodynamic changes. The method can be seen as an extension of Doppler imaging.

| Field | Description |
|:------|:------------|
| `Format` | Digital format (string). Data organization standard |
| `Compression` | Compression type (string). Storage optimization |
| `Frame rate (Hz)` | Ultrasound acquisition rate (float; measured in Hz). Temporal resolution |
| `Number of frames` | Total recorded frames (non-negative integer). Recording duration |
| `Vertical resolution` | Vertical pixels (non-negative integer). Image detail |
| `Horizontal resolution` | Horizontal pixels (non-negative integer). Spatial clarity |
| `Imaging depth (μm)` | Penetration depth (float; measured in μm). Tissue reach |

## General Time Series

General time series data represents any sequential measurements indexed by time. This format is versatile and can accommodate various types of continuous recordings that don't fit into more specific categories.

| Field | Description |
|:------|:------------|
| `Format` | Digital format (string; e.g., CSV, JSON). Determines data organization and compatibility |
| `Data-type` | Format of stored data (string; default: 'int16'). Affects precision and storage |
| `Number of channels` | Count of recording channels (non-negative integer). Multidimensional data streams |
| `Sampling rate (Hz)` | Sample frequency (float; default: 20000 Hz). Temporal resolution |
| `Number of samples` | Total data points per channel (non-negative integer). Recording duration |
| `Least significant bit (μV/bit)` | Smallest detectable change (float; measured in μV/bit). Signal resolution |
| `Electrode groups` | Groups of channels (array of objects with channels list and label). Data organization |
| `Channel tags` | Channel metadata (array of objects with tag name and channels). Enhanced organization |

## API access

The API allows for programmable access to Data acquisition, enabling you to read, edit, and delete Data acquisition through the API. Learn more about the Data acquisition' fields and data structure on the [Data acquisition API page]({{"api/schemas/dataacquisition/"|absolute_url}}).