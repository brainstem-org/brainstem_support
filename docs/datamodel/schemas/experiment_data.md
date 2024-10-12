---
layout: default
title: Experiment data types
parent: Schemas
grand_parent: Data model
nav_order: 2
---

# Experiment data types
{: .no_toc}

A wide range of data acquisition methods are supported to capture various aspects of neuroscience experiments.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Audio

Audio experiment data captures sound recordings related to the experiment.

| Field | Description |
|:------|:------------|
| `Bit depth` | Bit depth of the audio recording |
| `Number of channels` | Number of audio channels |
| `Sampling rate (Hz)` | Sampling rate of the audio in Hertz |
| `Number of samples` | Total number of audio samples |
| `Codec` | Audio codec used for encoding |

## Behavioral Tracking

Behavioral tracking data records the movement and actions of subjects during experiments.

| Field | Description |
|:------|:------------|
| `Frame rate (Hz)` | Frame rate of the tracking data in Hertz |
| `Number of frames` | Total number of frames in the tracking data |
| `Vertical resolution` | Vertical resolution of the tracking images or video |
| `Horizontal resolution` | Horizontal resolution of the tracking images or video |

## Computed Tomography (CT)

CT data provides detailed cross-sectional images of the subject.

| Field | Description |
|:------|:------------|
| `Frame rate (Hz)` | Frame rate of the CT acquisition in Hertz |
| `Number of frames` | Total number of frames in the CT data |
| `Vertical resolution` | Vertical resolution of the CT images |
| `Horizontal resolution` | Horizontal resolution of the CT images |
| `Imaging depth (μm)` | Depth of imaging in micrometers |
| `Laser power (mW)` | Laser power used in milliwatts |

## Confocal Microscopy

Confocal microscopy data captures high-resolution optical sections of samples.

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

## Electroencephalography (EEG)

EEG data records electrical activity of the brain.

| Field | Description |
|:------|:------------|
| `Data-type` | Data type used for EEG recording |
| `Number of channels` | Number of EEG channels |
| `Sampling rate (Hz)` | Sampling rate of the EEG in Hertz |
| `Number of samples` | Total number of EEG samples |
| `Least significant bit (μV/bit)` | Voltage represented by the least significant bit |
| `Electrode groups` | Groups of electrodes used in the recording |
| `Channel tags` | Tags associated with specific channels |

## Electroneurogram (ENG)

ENG data records electrical activity from peripheral nerves.

| Field | Description |
|:------|:------------|
| `Data-type` | Data type used for ENG recording |
| `Number of channels` | Number of ENG channels |
| `Sampling rate (Hz)` | Sampling rate of the ENG in Hertz |
| `Number of samples` | Total number of ENG samples |
| `Least significant bit (μV/bit)` | Voltage represented by the least significant bit |
| `Electrode groups` | Groups of electrodes used in the recording |
| `Channel tags` | Tags associated with specific channels |

## Extracellular Electrophysiology

Extracellular electrophysiology data records electrical activity from outside cells.

| Field | Description |
|:------|:------------|
| `Data-type` | Data type used for extracellular recording |
| `Number of channels` | Number of recording channels |
| `Sampling rate (Hz)` | Sampling rate of the recording in Hertz |
| `Number of samples` | Total number of samples in the recording |
| `Least significant bit (μV/bit)` | Voltage represented by the least significant bit |
| `Electrode groups` | Groups of electrodes used in the recording |
| `Channel tags` | Tags associated with specific channels |

## Fiber Photometry

Fiber photometry data records fluorescence signals from specific neural populations.

| Field | Description |
|:------|:------------|
| `Frame rate (Hz)` | Frame rate of the photometry acquisition in Hertz |
| `Number of frames` | Total number of frames in the photometry data |
| `Laser power (mW)` | Laser power used in milliwatts |
| `Excitation wavelength (nm)` | Excitation wavelength used in nanometers |

## Functional Magnetic Resonance Imaging (fMRI)

fMRI data measures brain activity by detecting changes in blood oxygenation and flow.

| Field | Description |
|:------|:------------|
| `Frame rate (Hz)` | Frame rate of the fMRI acquisition in Hertz |
| `Number of frames` | Total number of frames in the fMRI data |
| `Vertical resolution` | Vertical resolution of the fMRI images |
| `Horizontal resolution` | Horizontal resolution of the fMRI images |
| `Imaging depth (μm)` | Depth of imaging in micrometers |
| `Laser power (mW)` | Laser power used in milliwatts (if applicable) |

## Functional Ultrasound Imaging (fUS)

fUS data captures brain activity through changes in blood flow using ultrasound.

| Field | Description |
|:------|:------------|
| `Frame rate (Hz)` | Frame rate of the fUS acquisition in Hertz |
| `Number of frames` | Total number of frames in the fUS data |
| `Vertical resolution` | Vertical resolution of the fUS images |
| `Horizontal resolution` | Horizontal resolution of the fUS images |
| `Imaging depth (μm)` | Depth of imaging in micrometers |
| `Laser power (mW)` | Laser power used in milliwatts (if applicable) |

## General time-series

General time-series data represents any time-based measurements not covered by other specific types.

| Field | Description |
|:------|:------------|
| `Data-type` | Data type used for the time-series |
| `Number of channels` | Number of channels in the time-series |
| `Sampling rate (Hz)` | Sampling rate of the time-series in Hertz |
| `Number of samples` | Total number of samples in the time-series |
| `Least significant bit (μV/bit)` | Value represented by the least significant bit |
| `Electrode groups` | Groups of electrodes used (if applicable) |
| `Channel tags` | Tags associated with specific channels |

## Intracellular Electrophysiology

Intracellular electrophysiology data records electrical activity from inside cells.

| Field | Description |
|:------|:------------|
| `Data-type` | Data type used for intracellular recording |
| `Sampling rate (Hz)` | Sampling rate of the recording in Hertz |
| `Number of channels` | Number of recording channels |
| `Number of samples` | Total number of samples in the recording |
| `Least significant bit (μV/bit)` | Voltage represented by the least significant bit |

## Light Field Microscopy (LFM)

LFM data captures 3D information in a single shot using an array of microlenses.

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

## Magnetic Resonance Imaging (MRI)

MRI data provides detailed anatomical images of the brain and body.

| Field | Description |
|:------|:------------|
| `Frame rate (Hz)` | Frame rate of the MRI acquisition in Hertz |
| `Number of frames` | Total number of frames in the MRI data |
| `Vertical resolution` | Vertical resolution of the MRI images |
| `Horizontal resolution` | Horizontal resolution of the MRI images |
| `Imaging depth (μm)` | Depth of imaging in micrometers |
| `Laser power (mW)` | Laser power used in milliwatts (if applicable) |

## Magnetoencephalography (MEG)

MEG data records magnetic fields produced by electrical currents in the brain.

| Field | Description |
|:------|:------------|
| `Frame rate (Hz)` | Frame rate of the MEG acquisition in Hertz |
| `Number of frames` | Total number of frames in the MEG data |
| `Vertical resolution` | Vertical resolution of the MEG sensors |
| `Horizontal resolution` | Horizontal resolution of the MEG sensors |
| `Laser power (mW)` | Laser power used in milliwatts (if applicable) |
| `Imaging depth (μm)` | Depth of imaging in micrometers (if applicable) |

## Miniscope Microscopy

Miniscope microscopy data captures neural activity in freely behaving animals using miniature microscopes.

| Field | Description |
|:------|:------------|
| `Frame rate (Hz)` | Frame rate of the miniscope acquisition in Hertz |
| `Number of frames` | Total number of frames in the miniscope data |
| `Vertical resolution` | Vertical resolution of the miniscope images |
| `Horizontal resolution` | Horizontal resolution of the miniscope images |
| `Laser power (mW)` | Laser power used in milliwatts |
| `Imaging depth (μm)` | Depth of imaging in micrometers |

## Positron Emission Tomography (PET)

PET data provides functional images of metabolic processes in the body.

| Field | Description |
|:------|:------------|
| `Frame rate (Hz)` | Frame rate of the PET acquisition in Hertz |
| `Number of frames` | Total number of frames in the PET data |
| `Vertical resolution` | Vertical resolution of the PET images |
| `Horizontal resolution` | Horizontal resolution of the PET images |
| `Imaging depth (μm)` | Depth of imaging in micrometers |
| `Laser power (mW)` | Laser power used in milliwatts (if applicable) |

## Single-photon emission computed tomography (SPECT)

SPECT data provides 3D images of radioactive tracer distribution in the body.

| Field | Description |
|:------|:------------|
| `Frame rate (Hz)` | Frame rate of the SPECT acquisition in Hertz |
| `Number of frames` | Total number of frames in the SPECT data |
| `Vertical resolution` | Vertical resolution of the SPECT images |
| `Horizontal resolution` | Horizontal resolution of the SPECT images |
| `Imaging depth (μm)` | Depth of imaging in micrometers |
| `Laser power (mW)` | Laser power used in milliwatts (if applicable) |

## Single-Photon Microscopy

Single-photon microscopy data captures fluorescence images using single-photon excitation.

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

## Two-Photon Microscopy

Two-photon microscopy data captures high-resolution images of living tissue using two-photon excitation.

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

## Three-Photon Microscopy

Three-photon microscopy data captures high-resolution images of living tissue using three-photon excitation, allowing for deeper tissue penetration.

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

## Experiment data API access

The API allows for programmable access to Experiment data, enabling you to read, edit, and delete Experiment data through the API. Learn more about the Experiment data' fields and data structure on the [Experiment data API page]({{"api/modules/experimentdata/"|absolute_url}}).