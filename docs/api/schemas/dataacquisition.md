---
layout: default
title: Data acquisition
parent: Schemas
grand_parent: API
nav_order: 1
---

# Data acquisition schemas
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Audio
```
{
    "type": "object",
    "title": "Audio",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the audio file including the extension (e.g., 'track.mp3'). This identifies the file on storage media or file systems."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The file format or container type of the audio file (e.g., MP3, WAV, AAC). Different formats may support various features like metadata, compression, and copyright management."
            }
        },
        "compression": {
            "title": "Compression",
            "brief": "Compression",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Describes whether the audio is compressed losslessly or lossily, and the type of compression used if applicable. This affects audio quality and file size."
            }
        },
        "bitDepth": {
            "title": "Bit depth",
            "brief": "bit depth",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "default": 8,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of bits of information in each sample, which determines the dynamic range and noise level of the audio. Common values are 8, 16, 24, or 32 bits."
            }
        },
        "codec": {
            "title": "Codec",
            "brief": "codec",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The codec used to encode or decode the audio (e.g., FLAC, ALAC, Opus). The choice of codec affects compatibility with playback devices and audio quality."
            }
        },
        "nChannels": {
            "title": "Number of channels",
            "brief": "nChannels",
            "type": "integer",
            "units": "",
            "minimum": 1,
            "default": 2,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of separate audio channels (e.g., 1 for mono, 2 for stereo, more for surround sound configurations). This affects the spatial representation of sound."
            }
        },
        "sr": {
            "title": "Sampling rate (Hz)",
            "brief": "sr",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The sampling rate of the audio, in hertz, which is the number of samples of audio carried per second."
            }
        },
        "nSamples": {
            "title": "Number of samples",
            "brief": "nSamples",
            "units": "",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The total number of audio samples in the file. This number, along with the sampling rate, can determine the total duration of the audio."
            }
        }
    }
}
```

## BehavioralTracking
```
{
    "type": "object",
    "title": "BehavioralTracking",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the file containing behavioral tracking data, typically including the file extension (e.g., 'session1.avi')."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The video or data file format (e.g., MP4, AVI) used to store behavioral tracking information."
            }
        },
        "compression": {
            "title": "Compression",
            "brief": "compression",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Type of compression used to reduce the file size of the behavioral tracking data, if applicable."
            }
        },
        "frameRate": {
            "title": "Frame rate (Hz)",
            "brief": "frame rate",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The number of frames per second at which the behavioral data was recorded, affecting the smoothness and accuracy of motion analysis."
            }
        },
        "nFrames": {
            "title": "Number of frames",
            "brief": "nFrames",
            "units": "",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "Total number of frames included in the behavioral tracking session, which determines the total duration of the recorded data."
            }
        },
        "verticalResolution": {
            "title": "Vertical resolution",
            "brief": "vertical resolution",
            "units": "",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of vertical pixels in each frame, which affects the clarity and detail visible in the behavioral tracking video."
            }
        },
        "horizontalResolution": {
            "title": "Horizontal resolution",
            "brief": "horizontal resolution",
            "units": "",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of horizontal pixels in each frame, which affects the clarity and detail visible in the behavioral tracking video."
            }
        }
    }
}
```

## ComputedTomography
```
{
    "type": "object",
    "title": "ComputedTomography",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the file containing computed tomography scan data, usually including the file extension (e.g., 'scan.dcm'). This identifies the specific scan file for reference or analysis."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The digital file format of the CT images (e.g., DICOM). This format determines the compatibility with various viewing and processing software."
            }
        },
        "compression": {
            "title": "Compression",
            "brief": "compression",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Describes the type of data compression used for the CT images, if any, which can affect the file size and image quality."
            }
        },
        "frameRate": {
            "title": "Frame rate (Hz)",
            "brief": "frame rate",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The frame rate at which the CT scanner captures images per second. This is particularly relevant for dynamic studies such as perfusion scanning."
            }
        },
        "nFrames": {
            "title": "Number of frames",
            "brief": "nFrames",
            "units": "",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "Total number of image frames captured in a CT scan session. More frames can provide a more detailed view of the scanned area over time."
            }
        },
        "verticalResolution": {
            "title": "Vertical resolution",
            "brief": "vertical resolution",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the vertical dimension of each image, which affects the clarity and detail of the vertical aspects of the CT images."
            }
        },
        "horizontalResolution": {
            "title": "Horizontal resolution",
            "brief": "horizontal resolution",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the horizontal dimension of each image, impacting the sharpness and detail of the horizontal aspects of the CT images."
            }
        },
        "laserPower": {
            "title": "Laser power (mW)",
            "brief": "laser power",
            "units": "mW",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The power of the laser used, if applicable, in procedures associated with the CT scan, such as laser scanning CT, influencing the illumination and image clarity."
            }
        },
        "imagingDepth": {
            "title": "Imaging depth (\u00b5m)",
            "brief": "imaging depth",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The maximum depth at which the CT images provide usable data, important for understanding the penetration capability of the CT imaging."
            }
        }
    }
}
```

## ConfocalMicroscopy
```
{
    "type": "object",
    "title": "Confocal Microscopy",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the file containing confocal microscopy images, typically including the file extension (e.g., '.tif')."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The digital format of the confocal microscopy data (e.g., TIFF, JPEG, or specialized microscopy formats), which affects the compatibility with analysis software."
            }
        },
        "compression": {
            "title": "Compression",
            "brief": "compression",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Describes whether the image files are stored using lossless or lossy compression, which impacts file size and image quality."
            }
        },
        "verticalResolution": {
            "title": "Vertical resolution",
            "brief": "vertical resolution",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the vertical dimension of each image, influencing the level of detail and clarity in the image."
            }
        },
        "horizontalResolution": {
            "title": "Horizontal resolution",
            "brief": "horizontal resolution",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the horizontal dimension of each image, impacting the sharpness and granularity of the visual data."
            }
        },
        "frameRate": {
            "title": "Frame rate (Hz)",
            "brief": "frame rate",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The rate at which images are captured per second, important in time-lapse confocal microscopy to observe dynamic processes in live cells."
            }
        },
        "nFrames": {
            "title": "Number of frames",
            "brief": "nFrames",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The total number of image frames captured during the confocal microscopy session, providing insight into the extent and duration of the observation."
            }
        },
        "laserPower": {
            "title": "Laser power (mW)",
            "brief": "laser power",
            "units": "mW",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The power of the laser used in microscopy, which affects the intensity of light illuminating the sample and can influence the quality and depth of the images captured."
            }
        },
        "excitationWavelength": {
            "title": "Excitation wavelength (nm)",
            "brief": "excitation wavelength",
            "units": "nm",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The wavelength of light used to excite the fluorescent dyes within the sample, crucial for specific fluorescence imaging and contrast."
            }
        },
        "imagingDepth": {
            "title": "Imaging depth (\u00b5m)",
            "brief": "imaging depth",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The depth within the sample that can be effectively imaged, key for examining three-dimensional structures within thick biological specimens."
            }
        },
        "xVoxelSize": {
            "title": "Voxel size (X dimension)",
            "brief": "x voxel size x",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The size of a single voxel along the X-axis, determining the spatial resolution of the image in that dimension."
            }
        },
        "yVoxelSize": {
            "title": "Voxel size (Y dimension)",
            "brief": "voxel size y",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The size of a single voxel along the Y-axis, determining the spatial resolution of the image in that dimension."
            }
        },
        "zVoxelSize": {
            "title": "Voxel size (Z dimension)",
            "brief": "voxel size z",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The size of a single voxel along the Z-axis, determining the spatial resolution of the image in that dimension and the depth of field possible in the imagery."
            }
        }
    }
}
```

## Electroencephalography
```
{
    "type": "object",
    "title": "Electroencephalography (EEG)",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the file containing EEG data, typically including the file extension (e.g., '.edf'). This file stores brain wave patterns recorded during EEG sessions."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The digital file format of the EEG data (e.g., EDF, BDF). This format determines how data is organized, stored, and how compatible it is with various EEG analysis software."
            }
        },
        "type": {
            "title": "Data-type",
            "brief": "type",
            "type": "string",
            "format": "text",
            "default": "int16",
            "options": {
                "infoText": "Specifies the data type used to store the EEG signals (e.g., 'int16' for 16-bit integers), which impacts the data's precision and storage size."
            }
        },
        "nChannels": {
            "title": "Number of channels",
            "brief": "nChannels",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of separate EEG channels recorded, indicating the number of different scalp locations from which electrical activity is recorded, influencing the spatial resolution of the brain activity mapping."
            }
        },
        "sr": {
            "title": "Sampling rate (Hz)",
            "brief": "sr",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "default": 20000,
            "options": {
                "infoText": "The frequency at which the EEG signals are sampled per second, crucial for capturing the temporal dynamics of brain activity. Higher rates provide more detailed time resolution."
            }
        },
        "nSamples": {
            "title": "Number of samples",
            "brief": "nSamples",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The total number of data points recorded per channel, which determines the total duration of the EEG recording when combined with the sampling rate."
            }
        },
        "lsb": {
            "title": "Least significant bit (\u00b5V/bit)",
            "brief": "lsb",
            "units": "\u00b5V/bit",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The smallest measurable change in voltage detectable by the EEG equipment, which affects the amplitude resolution of the recorded brain wave signals."
            }
        },
        "electrodeGroups": {
            "type": "array",
            "format": "table",
            "title": "Electrode groups",
            "options": {
                "compact": false,
                "disable_array_delete_last_row": true,
                "enable_array_copy": true,
                "disable_properties": false,
                "disable_edit_json": false,
                "disable_array_delete_all_rows": false
            },
            "items": {
                "type": "object",
                "title": "Electrode group",
                "no_additional_properties": true,
                "additionalProperties": false,
                "use_type_default_value": false,
                "options": {
                    "infoText": "Defines groups of electrodes that are typically used together for specific recording tasks or to capture activity from specific regions of the brain."
                },
                "properties": {
                    "channels": {
                        "type": "array",
                        "format": "comma-separated-integers",
                        "title": "List of channels",
                        "brief": "Channels",
                        "options": {
                            "inputAttributes": {
                                "placeholder": "comma-separated integers"
                            }
                        },
                        "items": {
                            "type": "integer",
                            "minimum": 0
                        }
                    },
                    "label": {
                        "type": "string",
                        "title": "Label",
                        "brief": "Label",
                        "options": {
                            "infoText": "A descriptive label for the electrode group, aiding in identifying the function or location of the group within the EEG setup."
                        }
                    }
                }
            }
        },
        "channelTags": {
            "type": "array",
            "format": "table",
            "title": "Channel tags",
            "options": {
                "compact": false,
                "disable_array_delete_last_row": true,
                "enable_array_copy": true,
                "disable_properties": false,
                "disable_edit_json": false,
                "disable_array_delete_all_rows": false
            },
            "items": {
                "type": "object",
                "title": "Channel tag",
                "no_additional_properties": true,
                "additionalProperties": false,
                "use_type_default_value": false,
                "options": {
                    "infoText": "Tags that provide additional information about specific channels, such as the type of data they record or their importance in a particular analysis."
                },
                "properties": {
                    "tag": {
                        "type": "string",
                        "title": "Channel tag",
                        "options": {
                            "infoText": "A tag that categorizes or adds metadata to channels, helping to identify their roles or characteristics in the EEG data."
                        }
                    },
                    "channels": {
                        "type": "array",
                        "format": "comma-separated-integers",
                        "title": "List of channels",
                        "brief": "Channels",
                        "items": {
                            "type": "integer",
                            "units": "",
                            "minimum": 0
                        }
                    },
                    "groups": {
                        "type": "array",
                        "format": "comma-separated-integers",
                        "title": "Electrode groups",
                        "brief": "Groups",
                        "items": {
                            "type": "integer",
                            "units": "",
                            "minimum": 0
                        }
                    }
                }
            }
        }
    }
}
```

## Electroneurogram
```
{
    "type": "object",
    "title": "Electroneurogram",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the file containing electroneurogram data, often indicating the type of neural activity recorded (e.g., 'nerve_activity.edf')."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The digital format of the electroneurogram data (e.g., CSV, EDF). This format dictates how the data can be accessed and analyzed using various software tools."
            }
        },
        "type": {
            "title": "Data-type",
            "brief": "type",
            "type": "string",
            "format": "text",
            "default": "int16",
            "options": {
                "infoText": "Specifies the data type used to store the electrical signals from nerve activity (e.g., 'int16' for 16-bit integers), affecting the precision and size of the data."
            }
        },
        "nChannels": {
            "title": "Number of channels",
            "brief": "nChannels",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of separate recording channels, each capturing signals from different nerves or different locations on a single nerve, enhancing the detail and scope of analysis."
            }
        },
        "sr": {
            "title": "Sampling rate (Hz)",
            "brief": "sr",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "default": 20000,
            "options": {
                "infoText": "The frequency at which the neural data is sampled, crucial for capturing the rapid electrical changes that occur during nerve activation."
            }
        },
        "nSamples": {
            "title": "Number of samples",
            "brief": "nSamples",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The total number of data points collected per channel, determining the total duration of the recording when combined with the sampling rate."
            }
        },
        "lsb": {
            "title": "Least significant bit (\u00b5V/bit)",
            "brief": "lsb",
            "units": "\u00b5V/bit",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The smallest detectable change in signal by the recording system, affecting the amplitude resolution of the neural activity measurements."
            }
        },
        "electrodeGroups": {
            "type": "array",
            "format": "table",
            "title": "Electrode groups",
            "options": {
                "compact": false,
                "disable_array_delete_last_row": true,
                "enable_array_copy": true,
                "disable_properties": false,
                "disable_edit_json": false,
                "disable_array_delete_all_rows": false
            },
            "items": {
                "type": "object",
                "title": "Electrode group",
                "options": {
                    "infoText": "Groups of electrodes organized by location or function, aiding in the structured recording and analysis of nerve signals."
                },
                "properties": {
                    "channels": {
                        "type": "array",
                        "format": "comma-separated-integers",
                        "title": "List of channels",
                        "brief": "Channels",
                        "items": {
                            "type": "integer",
                            "minimum": 0
                        }
                    },
                    "label": {
                        "type": "string",
                        "title": "Label",
                        "brief": "Label",
                        "options": {
                            "infoText": "A label identifying the electrode group, useful for referencing during analysis or reporting."
                        }
                    }
                }
            }
        },
        "channelTags": {
            "type": "array",
            "format": "table",
            "title": "Channel tags",
            "options": {
                "compact": false,
                "disable_array_delete_last_row": true,
                "enable_array_copy": true,
                "disable_properties": false,
                "disable_edit_json": false,
                "disable_array_delete_all rows": false
            },
            "items": {
                "type": "object",
                "title": "Channel tag",
                "options": {
                    "infoText": "Tags that categorize or annotate specific channels for enhanced data management and analysis."
                },
                "properties": {
                    "tag": {
                        "type": "string",
                        "title": "Channel tag",
                        "options": {
                            "infoText": "A descriptive tag providing additional information about the role or characteristics of a channel in the recording setup."
                        }
                    },
                    "channels": {
                        "type": "array",
                        "format": "comma-separated-integers",
                        "title": "List of channels",
                        "brief": "Channels",
                        "items": {
                            "type": "integer",
                            "minimum": 0
                        }
                    },
                    "groups": {
                        "type": "array",
                        "format": "comma-separated-integers",
                        "title": "Electrode groups",
                        "brief": "Groups",
                        "items": {
                            "type": "integer",
                            "minimum": 0
                        }
                    }
                }
            }
        }
    }
}
```

## ExtracellularEphys
```
{
    "type": "object",
    "title": "Extracellular Electrophysiology",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the file containing extracellular electrophysiological data, typically including the file extension (e.g., '.dat'). This data records the electrical activity from outside of cells, often in neural tissue."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The digital format of the extracellular electrophysiology data (e.g., Binary, HDF5). This affects how the data can be accessed and analyzed using various software tools."
            }
        },
        "type": {
            "title": "Data-type",
            "brief": "type",
            "type": "string",
            "format": "text",
            "default": "int16",
            "options": {
                "infoText": "Specifies the data type used to store the electrical signals (e.g., 'int16' for 16-bit integers), affecting the precision and size of the data."
            }
        },
        "nChannels": {
            "title": "Number of channels",
            "brief": "nChannels",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of separate recording channels, each capturing signals from different parts of the extracellular space, influencing the spatial resolution of the activity mapping."
            }
        },
        "sr": {
            "title": "Sampling rate (Hz)",
            "brief": "sr",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "default": 20000,
            "options": {
                "inputAttributes": {
                    "placeholder": "number"
                },
                "infoText": "The frequency at which the electrical signals are sampled per second, crucial for capturing the rapid changes that occur in neuronal activity."
            }
        },
        "nSamples": {
            "title": "Number of samples",
            "brief": "nSamples",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The total number of data points collected per channel, which determines the total duration of the recording when combined with the sampling rate."
            }
        },
        "lsb": {
            "title": "Least significant bit (\u00b5V/bit)",
            "brief": "lsb",
            "units": "\u00b5V/bit",
            "type": "number",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "number"
                },
                "infoText": "The smallest detectable change in voltage by the recording equipment, influencing the resolution and sensitivity of the measurements."
            }
        },
        "electrodeGroups": {
            "type": "array",
            "format": "table",
            "title": "Electrode groups",
            "no_additional_properties": true,
            "additionalProperties": false,
            "use_type_default_value": false,
            "options": {
                "compact": false,
                "disable_array_delete_last_row": true,
                "enable_array_copy": true,
                "disable_properties": false,
                "disable_edit_json": false,
                "disable_array_delete_all_rows": false
            },
            "items": {
                "type": "object",
                "no_additional_properties": true,
                "additionalProperties": false,
                "use_type_default_value": false,
                "title": "Electrode group",
                "options": {
                    "infoText": "Groups of electrodes that are typically used together or configured to record from a specific anatomical area or circuit within the brain or nervous system."
                },
                "properties": {
                    "channels": {
                        "type": "array",
                        "format": "comma-separated-integers",
                        "title": "List of channels",
                        "brief": "Channels",
                        "items": {
                            "type": "integer",
                            "units": "",
                            "minimum": 0
                        }
                    },
                    "label": {
                        "type": "string",
                        "title": "Label",
                        "brief": "Label",
                        "options": {
                            "infoText": "A descriptive label for the electrode group, aiding in identifying the function or location of the group within the electrophysiological setup."
                        }
                    }
                }
            }
        },
        "channelTags": {
            "type": "array",
            "format": "table",
            "title": "Channel tags",
            "options": {
                "compact": false,
                "disable_array_delete_last_row": true,
                "enable_array_copy": true,
                "disable_properties": false,
                "disable_edit_json": false,
                "disable_array_delete_all_rows": false
            },
            "items": {
                "type": "object",
                "no_additional_properties": true,
                "additionalProperties": false,
                "use_type_default_value": false,
                "title": "Channel tag",
                "options": {
                    "infoText": "Tags that categorize or provide additional metadata about specific channels, enhancing data management and analysis."
                },
                "properties": {
                    "tag": {
                        "type": "string",
                        "title": "Channel tag",
                        "options": {
                            "infoText": "A descriptive tag providing additional information about the role or characteristics of a channel in the recording setup."
                        }
                    },
                    "channels": {
                        "type": "array",
                        "format": "comma-separated-integers",
                        "title": "List of channels",
                        "brief": "Channels",
                        "items": {
                            "type": "integer",
                            "units": "",
                            "minimum": 0
                        }
                    },
                    "groups": {
                        "type": "array",
                        "format": "comma-separated-integers",
                        "title": "Electrode groups",
                        "brief": "Groups",
                        "items": {
                            "type": "integer",
                            "units": "",
                            "minimum": 0
                        }
                    }
                }
            }
        }
    }
}
```

## FiberPhotometry
```
{
    "type": "object",
    "title": "Fiber Photometry",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the file containing fiber photometry data, typically including the file extension (e.g., '.csv'). This file contains time-series data of fluorescent signals recorded from specific brain regions."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The digital format of the fiber photometry data (e.g., CSV, TXT), affecting how data is stored, accessed, and analyzed."
            }
        },
        "compression": {
            "title": "Compression",
            "brief": "compression",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Describes any compression applied to the fiber photometry data files, which can impact file size and potentially affect data quality and processing speed."
            }
        },
        "frameRate": {
            "title": "Frame rate (Hz)",
            "brief": "frame rate",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The rate at which fluorescent signal data is recorded, measured in frames per second. Higher frame rates allow for more detailed temporal analysis of changes in neural activity."
            }
        },
        "nFrames": {
            "title": "Number of frames",
            "brief": "nFrames",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The total number of recorded frames, which determines the overall duration of the fluorescence recording."
            }
        },
        "laserPower": {
            "title": "Laser power (mW)",
            "brief": "laser power",
            "units": "mW",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The power of the laser used during the fiber photometry recording, measured in milliwatts. Laser power affects the intensity of the excitation light and can influence the fluorescence signal strength."
            }
        },
        "excitationWavelength": {
            "title": "Excitation wavelength (nm)",
            "brief": "excitation wavelength",
            "units": "nm",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The wavelength of light used to excite the fluorescent dye or protein in the study, measured in nanometers. Specific wavelengths are chosen based on the properties of the fluorescent markers used."
            }
        }
    }
}
```

## FunctionalMagneticResonanceImaging
```
{
    "type": "object",
    "title": "Functional Magnetic Resonance Imaging",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the file containing fMRI data, typically including the file extension (e.g., '.nii'). This data represents brain activity by detecting changes in blood flow."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The digital format of the fMRI data (e.g., NIfTI, DICOM), which affects the accessibility and compatibility with various imaging analysis software."
            }
        },
        "compression": {
            "title": "Compression",
            "brief": "compression",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Describes any compression applied to the fMRI data files, which can impact file size and potentially affect data quality and processing speed."
            }
        },
        "frameRate": {
            "title": "Frame rate (Hz)",
            "brief": "frame rate",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The rate at which fMRI images are captured, measured in frames per second. Important for studies involving time-series analysis of brain activity."
            }
        },
        "nFrames": {
            "title": "Number of frames",
            "brief": "nFrames",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The total number of image frames, which determines the overall duration of the fMRI scan and the temporal resolution of the brain activity data."
            }
        },
        "verticalResolution": {
            "title": "Vertical resolution",
            "brief": "vertical resolution",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the vertical dimension of each image frame. Higher resolution allows for more detailed visualization of brain structures."
            }
        },
        "horizontalResolution": {
            "title": "Horizontal resolution",
            "brief": "horizontal resolution",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the horizontal dimension of each image frame. Like vertical resolution, it affects the clarity and detail of the displayed brain activity."
            }
        },
        "laserPower": {
            "title": "Laser power (mW)",
            "brief": "laser power",
            "units": "mW",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The power of the laser used, if applicable, in laser-enhanced fMRI procedures. This setting influences the intensity of light used during imaging."
            }
        },
        "imagingDepth": {
            "title": "Imaging depth (\u00b5m)",
            "brief": "imaging depth",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The depth within the brain that the fMRI can effectively image, important for targeting specific brain structures or layers."
            }
        }
    }
}
```

## FunctionalUltrasoundImaging
```
{
    "type": "object",
    "title": "Functional Ultrasound Imaging",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the file containing functional ultrasound imaging data, typically including the file extension (e.g., '.fus'). This file stores dynamic blood flow images within the brain or other organs."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The digital format of the functional ultrasound imaging data (e.g., DICOM, proprietary formats), which affects the accessibility and compatibility with various imaging analysis software."
            }
        },
        "compression": {
            "title": "Compression",
            "brief": "compression",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Describes any compression applied to the ultrasound data files, which can impact file size and potentially affect data quality and processing speed."
            }
        },
        "frameRate": {
            "title": "Frame rate (Hz)",
            "brief": "frame rate",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The rate at which ultrasound images are captured, measured in frames per second. This is crucial for capturing dynamic changes in blood flow and other physiological parameters."
            }
        },
        "nFrames": {
            "title": "Number of frames",
            "brief": "nFrames",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The total number of image frames captured during the ultrasound session. This number determines the overall duration of the imaging data and is critical for time-series analysis."
            }
        },
        "verticalResolution": {
            "title": "Vertical resolution",
            "brief": "vertical resolution",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the vertical dimension of each image, affecting the clarity and detail of the imaging data."
            }
        },
        "horizontalResolution": {
            "title": "Horizontal resolution",
            "brief": "horizontal resolution",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the horizontal dimension of each image. Higher resolution allows for better visualization of physiological structures and flow patterns."
            }
        },
        "laserPower": {
            "title": "Laser power (mW)",
            "brief": "laser power",
            "units": "mW",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The power of the laser used in laser-enhanced ultrasound imaging. This setting influences the intensity and penetration of the ultrasound waves."
            }
        },
        "imagingDepth": {
            "title": "Imaging depth (\u00b5m)",
            "brief": "imaging depth",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The depth within the tissue that the ultrasound can effectively image. This is crucial for targeting specific anatomical features or regions within the organ being studied."
            }
        }
    }
}
```

## GeneralTimeSeries
```
{
    "type": "object",
    "title": "General Time Series",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the file containing time series data, typically including the file extension (e.g., '.csv'). This file stores a series of data points indexed in time order."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The digital format of the time series data (e.g., CSV, JSON), which affects how the data can be accessed, processed, and analyzed."
            }
        },
        "type": {
            "title": "Data-type",
            "brief": "type",
            "type": "string",
            "format": "text",
            "default": "int16",
            "options": {
                "infoText": "Specifies the data type used to store the time series values (e.g., 'int16' for 16-bit integers), influencing data precision and storage size."
            }
        },
        "nChannels": {
            "title": "Number of channels",
            "brief": "nChannels",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of separate data channels recorded, each possibly representing different variables or sensors, enhancing the complexity and multidimensionality."
            }
        },
        "sr": {
            "title": "Sampling rate (Hz)",
            "brief": "sr",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "default": 20000,
            "options": {
                "infoText": "The frequency at which data points are recorded per second, crucial for determining the temporal resolution of the time series."
            }
        },
        "nSamples": {
            "title": "Number of samples",
            "brief": "nSamples",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The total number of data points recorded, defining the length of the time series."
            }
        },
        "lsb": {
            "title": "Least significant bit (\u00b5V/bit)",
            "brief": "lsb",
            "units": "\u00b5V/bit",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The smallest measurable change in data by the recording system, impacting the amplitude resolution of the recorded signals."
            }
        },
        "electrodeGroups": {
            "type": "array",
            "format": "table",
            "title": "Electrode groups",
            "no_additional_properties": true,
            "additionalProperties": false,
            "use_type_default_value": false,
            "options": {
                "compact": false,
                "disable_array_delete_last_row": true,
                "enable_array_copy": true,
                "disable_properties": false,
                "disable_edit_json": false,
                "disable_array_delete_all_rows": false
            },
            "items": {
                "type": "object",
                "title": "Electrode group",
                "no_additional_properties": true,
                "additionalProperties": false,
                "use_type_default_value": false,
                "properties": {
                    "channels": {
                        "type": "array",
                        "format": "comma-separated-integers",
                        "title": "List of channels",
                        "brief": "Channels",
                        "items": {
                            "type": "integer",
                            "minimum": 0
                        }
                    },
                    "label": {
                        "type": "string",
                        "title": "Label",
                        "brief": "Label",
                        "options": {
                            "infoText": "A label for the electrode group, helping to categorize or identify the group based on its function or location."
                        }
                    }
                }
            }
        },
        "channelTags": {
            "type": "array",
            "format": "table",
            "title": "Channel tags",
            "options": {
                "compact": false,
                "disable_array_delete_last_row": true,
                "enable_array_copy": true,
                "disable_properties": false,
                "disable_edit_json": false,
                "disable_array_delete_all_rows": false
            },
            "items": {
                "type": "object",
                "title": "Channel tag",
                "no_additional_properties": true,
                "additionalProperties": false,
                "use_type_default_value": false,
                "properties": {
                    "tag": {
                        "type": "string",
                        "title": "Channel tag",
                        "options": {
                            "infoText": "A tag providing additional information or categorization for the channels, useful in data analysis and interpretation."
                        }
                    },
                    "channels": {
                        "type": "array",
                        "format": "comma-separated-integers",
                        "title": "List of channels",
                        "brief": "Channels",
                        "items": {
                            "type": "integer",
                            "minimum": 0
                        }
                    },
                    "groups": {
                        "type": "array",
                        "format": "comma-separated-integers",
                        "title": "Electrode groups",
                        "brief": "Groups",
                        "items": {
                            "type": "integer",
                            "minimum": 0
                        }
                    }
                }
            }
        }
    }
}
```

## IntracellularEphys
```
{
    "type": "object",
    "title": "Intracellular Electrophysiology",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the file containing intracellular electrophysiology data, usually including the file extension (e.g., '.abf' for Axon Binary File). This file records electrical activities from within neurons."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The digital format of the intracellular electrophysiology data (e.g., ABF, DAT), which determines how data is organized, stored, and how compatible it is with various analysis software."
            }
        },
        "type": {
            "title": "Data-type",
            "brief": "type",
            "type": "string",
            "format": "text",
            "default": "int16",
            "options": {
                "infoText": "Specifies the data type used to store the electrical signals (e.g., 'int16' for 16-bit integers), affecting the precision and size of the data."
            }
        },
        "sr": {
            "title": "Sampling rate (Hz)",
            "brief": "sr",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The frequency at which the electrical signals inside the neuron are sampled per second, crucial for capturing the rapid changes in voltage that occur during neuronal activity."
            }
        },
        "nChannels": {
            "title": "Number of channels",
            "brief": "nChannels",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of separate recording channels, each possibly recording from different cells or different parts of a cell, providing a comprehensive view of neural activity."
            }
        },
        "nSamples": {
            "title": "Number of samples",
            "brief": "nSamples",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The total number of data points collected per channel, defining the duration and extent of the recording session when combined with the sampling rate."
            }
        },
        "lsb": {
            "title": "Least significant bit (\u00b5V/bit)",
            "brief": "lsb",
            "units": "\u00b5V/bit",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The smallest detectable change in signal by the recording system, impacting the amplitude resolution of the recorded signals and hence the detail of neuronal activity that can be analyzed."
            }
        }
    }
}
```

## LightFieldMicroscopy
```
{
    "type": "object",
    "title": "Light Field Microscopy",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the file containing light field microscopy data, typically including the file extension (e.g., '.lfp'). This file contains multidimensional data that enables the capture of both spatial and angular information."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The digital format of the light field microscopy data (e.g., TIFF, proprietary formats), which affects the accessibility and compatibility with various imaging analysis software."
            }
        },
        "compression": {
            "title": "Compression",
            "brief": "compression",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Describes any compression applied to the microscopy data files, which can impact file size and potentially affect data quality and processing speed."
            }
        },
        "verticalResolution": {
            "title": "Vertical resolution",
            "brief": "vertical resolution",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the vertical dimension of each image, affecting the clarity and detail of the captured images."
            }
        },
        "horizontalResolution": {
            "title": "Horizontal resolution",
            "brief": "horizontal resolution",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the horizontal dimension of each image. High resolution is crucial for detailed visualization of microscopic structures."
            }
        },
        "frameRate": {
            "title": "Frame rate (Hz)",
            "brief": "frame rate",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The rate at which images are captured per second, important for dynamic studies where motion within the sample is analyzed over time."
            }
        },
        "nFrames": {
            "title": "Number of frames",
            "brief": "nFrames",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The total number of recorded frames, which determines the overall duration of the imaging data and is critical for time-series analysis."
            }
        },
        "laserPower": {
            "title": "Laser power (mW)",
            "brief": "laser power",
            "units": "mW",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The power of the laser used during imaging, which affects the intensity of the illumination and can influence the quality of the captured images."
            }
        },
        "excitationWavelength": {
            "title": "Excitation wavelength (nm)",
            "brief": "excitation wavelength",
            "units": "nm",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The wavelength of light used to excite the samples, selected based on the optical properties of the sample and the specific fluorescent dyes used."
            }
        },
        "imagingDepth": {
            "title": "Imaging depth (\u00b5m)",
            "brief": "imaging depth",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The depth within the sample that can be effectively imaged, crucial for studies involving thick specimens or tissues."
            }
        },
        "xVoxelSize": {
            "title": "Voxel size (X dimension)",
            "brief": "x voxel size",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The size of a single voxel along the X-axis, which affects the spatial resolution of the image in that dimension."
            }
        },
        "yVoxelSize": {
            "title": "Voxel size (Y dimension)",
            "brief": "y voxel size",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The size of a single voxel along the Y-axis, influencing the spatial resolution of the image in that dimension and the detail of structural data."
            }
        },
        "zVoxelSize": {
            "title": "Voxel size (Z dimension)",
            "brief": "z voxel size",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The size of a single voxel along the Z-axis, determining the depth resolution of the image and aiding in three-dimensional reconstructions."
            }
        }
    }
}
```

## MagneticResonanceImaging
```
{
    "type": "object",
    "title": "Magnetic Resonance Imaging",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the file containing MRI data, typically including the file extension (e.g., '.nii' for NIfTI files). This file stores detailed images of organs and tissues."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The digital format of the MRI data (e.g., DICOM, NIfTI), which determines how data is organized, stored, and how compatible it is with various imaging analysis software."
            }
        },
        "compression": {
            "title": "Compression",
            "brief": "compression",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Describes any compression applied to the MRI data files, which can impact file size and potentially affect data quality and processing speed."
            }
        },
        "frameRate": {
            "title": "Frame rate (Hz)",
            "brief": "frame rate",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The rate at which MRI images are captured, measured in frames per second. This is crucial for dynamic studies, such as functional MRI, where changes over time are analyzed."
            }
        },
        "nFrames": {
            "title": "Number of frames",
            "brief": "nFrames",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The total number of recorded frames, which determines the overall duration of the MRI scan and is critical for time-series analysis in functional MRI studies."
            }
        },
        "verticalResolution": {
            "title": "Vertical resolution",
            "brief": "vertical resolution",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the vertical dimension of each image, affecting the clarity and detail of the anatomical structures visualized."
            }
        },
        "horizontalResolution": {
            "title": "Horizontal resolution",
            "brief": "horizontal resolution",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the horizontal dimension of each image, which is crucial for accurately capturing the fine details of the tissues and structures being studied."
            }
        },
        "laserPower": {
            "title": "Laser power (mW)",
            "brief": "laser power",
            "units": "mW",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The power of the laser used, if applicable, in laser-enhanced MRI procedures. This setting influences the intensity and penetration of the MRI imaging."
            }
        },
        "imagingDepth": {
            "title": "Imaging depth (\u00b5m)",
            "brief": "imaging depth",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The depth within the body that the MRI can effectively image, important for targeting specific organs or tissues for detailed examination."
            }
        }
    }
}
```

## Magnetoencephalography
```
{
    "type": "object",
    "title": "Magnetoencephalography",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the file containing magnetoencephalography data, usually including the file extension (e.g., '.fif' for FIFF files). This file captures the magnetic fields produced by neural activity."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The digital format of the MEG data (e.g., FIFF, DICOM), which determines how data is organized, stored, and how compatible it is with various analysis software."
            }
        },
        "compression": {
            "title": "Compression",
            "brief": "compression",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Describes any compression applied to the MEG data files, which can impact file size and potentially affect data quality and processing speed."
            }
        },
        "frameRate": {
            "title": "Frame rate (Hz)",
            "brief": "frame rate",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The rate at which MEG data is sampled, measured in frames per second. Crucial for capturing the rapid temporal dynamics of brain activity."
            }
        },
        "nFrames": {
            "title": "Number of frames",
            "brief": "nFrames",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The total number of frames recorded, determining the overall duration of the MEG recording session and the temporal resolution of the data."
            }
        },
        "verticalResolution": {
            "title": "Vertical resolution",
            "brief": "vertical resolution",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The resolution of the sensor array in the vertical dimension, which impacts the precision of spatial localization of brain activity."
            }
        },
        "horizontalResolution": {
            "title": "Horizontal resolution",
            "brief": "horizontal resolution",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The resolution of the sensor array in the horizontal dimension, important for detailed spatial mapping of neural activity across the scalp."
            }
        },
        "laserPower": {
            "title": "Laser power (mW)",
            "brief": "laser power",
            "units": "mW",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "Laser power is generally not applicable to MEG, as MEG does not use lasers for imaging. This field may be a placeholder or error in the schema."
            }
        },
        "imagingDepth": {
            "title": "Imaging depth (\u00b5m)",
            "brief": "imaging depth",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "Imaging depth refers to how deep the sensors can detect magnetic fields within the brain. Unlike other imaging techniques, MEG has a whole-head coverage and detects superficial and deeper brain activity based on the strength and orientation of the neural currents."
            }
        }
    }
}
```

## Miniscope
```
{
    "type": "object",
    "title": "Miniscope Microscopy",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the file containing Miniscope microscopy data, often including the file extension (e.g., '.avi' for video files). Miniscope refers to a miniature, head-mounted microscope used primarily in freely moving animals."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The digital format of the Miniscope data (e.g., AVI, MOV), which affects the accessibility and compatibility with various imaging analysis software."
            }
        },
        "compression": {
            "title": "Compression",
            "brief": "compression",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Describes any compression applied to the microscopy video files, which can impact file size and potentially affect video quality and processing speed."
            }
        },
        "frameRate": {
            "title": "Frame rate (Hz)",
            "brief": "frame rate",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The rate at which video frames are captured, measured in frames per second. Crucial for capturing the dynamic processes at cellular resolution in real time."
            }
        },
        "nFrames": {
            "title": "Number of frames",
            "brief": "nFrames",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The total number of frames captured during the recording session, which determines the overall length of the video and the duration of the observed biological processes."
            }
        },
        "verticalResolution": {
            "title": "Vertical resolution",
            "brief": "vertical resolution",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the vertical dimension of each frame, affecting the image quality and the detail visible in the video."
            }
        },
        "horizontalResolution": {
            "title": "Horizontal resolution",
            "brief": "horizontal resolution",
            "type": "integer",
            "minimum": 0,
            "units": "",
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the horizontal dimension of each frame, crucial for accurately capturing detailed features of the observed specimen."
            }
        },
        "laserPower": {
            "title": "Laser power (mW)",
            "brief": "laser power",
            "units": "mW",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The power of the laser used during imaging, influencing the intensity and depth of illumination, which is vital for enhancing image clarity and contrast in fluorescence-based applications."
            }
        },
        "imagingDepth": {
            "title": "Imaging depth (\u00b5m)",
            "brief": "imaging depth",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The depth within the tissue that the Miniscope can effectively image. This is crucial for targeting specific layers of neural circuits in the brain or other tissues."
            }
        }
    }
}
```

## OpticalCoherenceTomography
```
{
    "type": "object",
    "title": "Optical Coherence Tomography (OCT)",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the file containing optical coherence tomography data, typically including the file extension. OCT files store high-resolution cross-sectional images of tissue microstructure."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The digital format of the OCT data (e.g., DICOM, OCT native format, TIFF), which determines data organization, storage structure, and compatibility with analysis software."
            }
        },
        "compression": {
            "title": "Compression",
            "brief": "compression",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Describes any compression applied to the OCT image files to reduce file size while preserving image quality for accurate analysis."
            }
        },
        "verticalResolution": {
            "title": "Vertical resolution",
            "brief": "vertical resolution",
            "units": "",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the vertical dimension of each OCT image, affecting the quality and detail of depth information in the tomographic images."
            }
        },
        "horizontalResolution": {
            "title": "Horizontal resolution",
            "brief": "horizontal resolution",
            "units": "",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the horizontal dimension of each OCT image, determining the lateral resolution and detail captured across the scanning area."
            }
        },
        "frameRate": {
            "title": "Frame rate (Hz)",
            "brief": "frame rate",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The rate at which OCT images are captured, measured in frames per second. Higher frame rates enable real-time imaging and capture of dynamic processes."
            }
        },
        "nFrames": {
            "title": "Number of frames",
            "brief": "nFrames",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The total number of frames captured during the OCT imaging session, determining the temporal resolution and duration of the acquired data."
            }
        },
        "centerWavelength": {
            "title": "Center wavelength (nm)",
            "brief": "center wavelength",
            "units": "nm",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The central wavelength of the light source used in OCT, typically in the near-infrared range (800-1300 nm), which affects tissue penetration depth and image contrast."
            }
        },
        "bandwidth": {
            "title": "Bandwidth (nm)",
            "brief": "bandwidth",
            "units": "nm",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The spectral bandwidth of the OCT light source, which determines the axial resolution of the system. Broader bandwidth provides better axial resolution."
            }
        },
        "imagingDepth": {
            "title": "Imaging depth (\u00b5m)",
            "brief": "imaging depth",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The maximum depth within the tissue that the OCT system can effectively image, typically ranging from hundreds of micrometers to a few millimeters depending on tissue properties."
            }
        },
        "axialResolution": {
            "title": "Axial resolution (\u00b5m)",
            "brief": "axial resolution",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The resolution along the depth direction (z-axis), determining the ability to distinguish between closely spaced structures in the depth dimension."
            }
        },
        "lateralResolution": {
            "title": "Lateral resolution (\u00b5m)",
            "brief": "lateral resolution",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The resolution in the scanning plane (x-y axes), determining the ability to distinguish between closely spaced features in the lateral dimensions."
            }
        },
        "scanPattern": {
            "title": "Scan pattern",
            "brief": "scan pattern",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The scanning pattern used for OCT imaging (e.g., raster scan, circular scan, radial scan), which affects the coverage area and acquisition speed."
            }
        },
        "scanArea": {
            "title": "Scan area (mm\u00b2)",
            "brief": "scan area",
            "units": "mm\u00b2",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The total area covered by the OCT scan, typically measured in square millimeters, defining the field of view for the imaging session."
            }
        },
        "averages": {
            "title": "Number of averages",
            "brief": "averages",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of repeat measurements averaged to improve signal-to-noise ratio and image quality, with more averages providing cleaner but slower acquisition."
            }
        }
    }
}
```

## PositronEmissionTomography
```
{
    "type": "object",
    "title": "Positron Emission Tomography",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the file containing PET scan data, typically including the file extension (e.g., '.pet'). PET scans are advanced imaging tests that show how organs and tissues are functioning."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The digital format of the PET scan data (e.g., DICOM), which determines how data is organized, stored, and how compatible it is with various imaging analysis software."
            }
        },
        "compression": {
            "title": "Compression",
            "brief": "compression",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Describes any compression applied to the PET scan data files, which can impact file size and potentially affect data quality and processing speed."
            }
        },
        "frameRate": {
            "title": "Frame rate (Hz)",
            "brief": "frameRate",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The rate at which PET scan images are captured, measured in frames per second. This is crucial for capturing dynamic changes in tracer distribution and metabolism over time."
            }
        },
        "nFrames": {
            "title": "Number of frames",
            "brief": "nFrames",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The total number of frames captured during the PET scan, which determines the overall duration of the scan and is critical for time-series analysis of metabolic activity."
            }
        },
        "verticalResolution": {
            "title": "Vertical resolution",
            "brief": "vertical resolution",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the vertical dimension of each image, affecting the clarity and detail of the anatomical and functional visualization."
            }
        },
        "horizontalResolution": {
            "title": "Horizontal resolution",
            "brief": "horizontal resolution",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the horizontal dimension of each image, which is crucial for accurately capturing detailed features of metabolic and physiological processes."
            }
        },
        "laserPower": {
            "title": "Laser power (mW)",
            "brief": "laserPower",
            "units": "mW",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "Laser power is not applicable to PET imaging as it does not use lasers for imaging. This field may be a placeholder or error in the schema."
            }
        },
        "imagingDepth": {
            "title": "Imaging depth (\u00b5m)",
            "brief": "imagingDepth",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "In PET imaging, imaging depth is not measured in micrometers but is rather about the penetration of the gamma rays emitted by the radiotracers, which can image the entire body or targeted organs."
            }
        }
    }
}
```

## SinglePhotonEmissionComputedTomography
```
{
    "type": "object",
    "title": "Single Photon Emission Computed Tomography",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the file containing SPECT imaging data, usually including the file extension (e.g., '.dcm' for DICOM files). SPECT is used to visualize metabolic processes in the body by injecting a radioactive tracer."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The digital format of the SPECT scan data (e.g., DICOM), which determines how data is organized, stored, and how compatible it is with various imaging analysis software."
            }
        },
        "compression": {
            "title": "Compression",
            "brief": "compression",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Describes any compression applied to the SPECT scan data files, which can impact file size and potentially affect data quality and processing speed."
            }
        },
        "frameRate": {
            "title": "Frame rate (Hz)",
            "brief": "frame rate",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The rate at which SPECT images are captured, measured in frames per second. This is crucial for capturing dynamic changes in tracer distribution and metabolism over time."
            }
        },
        "nFrames": {
            "title": "Number of frames",
            "brief": "nFrames",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The total number of frames captured during the SPECT scan, which determines the overall duration of the scan and is critical for time-series analysis of metabolic activity."
            }
        },
        "verticalResolution": {
            "title": "Vertical resolution",
            "brief": "vertical resolution",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the vertical dimension of each image, affecting the clarity and detail of the anatomical and functional visualization."
            }
        },
        "horizontalResolution": {
            "title": "Horizontal resolution",
            "brief": "horizontal resolution",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the horizontal dimension of each image, which is crucial for accurately capturing detailed features of metabolic and physiological processes."
            }
        },
        "laserPower": {
            "title": "Laser power (mW)",
            "brief": "laser power",
            "units": "mW",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "Laser power is generally not applicable to SPECT as it does not use lasers for imaging. This field may be a placeholder or error in the schema."
            }
        },
        "imagingDepth": {
            "title": "Imaging depth (\u00b5m)",
            "brief": "imaging depth",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "In SPECT imaging, imaging depth is not measured in micrometers but is rather about the penetration of gamma rays emitted by the radiotracers, which can image the entire body or targeted organs."
            }
        }
    }
}
```

## SinglePhotonMicroscopy
```
{
    "type": "object",
    "title": "Single-Photon Microscopy",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the file containing single-photon microscopy data, typically including the file extension (e.g., '.tif' for TIFF files). This type of microscopy is used for high-resolution imaging, especially in biological tissues."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The digital format of the single-photon microscopy data (e.g., TIFF, JPEG), which affects the accessibility and compatibility with various imaging analysis software."
            }
        },
        "compression": {
            "title": "Compression",
            "brief": "compression",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Describes any compression applied to the microscopy image files, which can impact file size and potentially affect image quality and processing speed."
            }
        },
        "verticalResolution": {
            "title": "Vertical resolution",
            "brief": "vertical resolution",
            "units": "",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the vertical dimension of each image, affecting the image quality and the detail visible in the microscopy data."
            }
        },
        "horizontalResolution": {
            "title": "Horizontal resolution",
            "brief": "horizontal resolution",
            "units": "",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the horizontal dimension of each image, crucial for accurately capturing detailed features of the observed specimen."
            }
        },
        "frameRate": {
            "title": "Frame rate (Hz)",
            "brief": "frame rate",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The rate at which images are captured, measured in frames per second. Crucial for capturing dynamic processes at cellular resolution in real time."
            }
        },
        "nFrames": {
            "title": "Number of frames",
            "brief": "nFrames",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The total number of frames captured during the recording session, which determines the overall length of the video and the duration of the observed biological processes."
            }
        },
        "laserPower": {
            "title": "Laser power (mW)",
            "brief": "laser power",
            "units": "mW",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The power of the laser used during imaging, influencing the intensity and depth of illumination, which is vital for enhancing image clarity and contrast in fluorescence-based applications."
            }
        },
        "excitationWavelength": {
            "title": "Excitation wavelength (nm)",
            "brief": "excitation wavelength",
            "units": "nm",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The wavelength of light used to excite the samples, selected based on the optical properties of the sample and the specific fluorescent dyes used."
            }
        },
        "imagingDepth": {
            "title": "Imaging depth (\u00b5m)",
            "brief": "imaging depth",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The depth within the sample that the microscope can effectively image. This is crucial for targeting specific layers of cellular structures in the tissue."
            }
        },
        "xVoxelSize": {
            "title": "Voxel size (X dimension)",
            "brief": "x voxel size x",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The size of a single voxel along the X-axis, which affects the spatial resolution of the image in that dimension."
            }
        },
        "yVoxelSize": {
            "title": "Voxel size (Y dimension)",
            "brief": "voxel size y",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The size of a single voxel along the Y-axis, influencing the spatial resolution of the image in that dimension and the detail of structural data."
            }
        },
        "zVoxelSize": {
            "title": "Voxel size (Z dimension)",
            "brief": "voxel size z",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The size of a single voxel along the Z-axis, determining the depth resolution of the image and aiding in three-dimensional reconstructions."
            }
        }
    }
}
```

## ThreePhotonMicroscopy
```
{
    "type": "object",
    "title": "Three-Photon Microscopy",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the file containing three-photon microscopy data, often including the file extension. This file stores high-resolution images that allow for deeper tissue penetration with reduced scattering, particularly useful in neurological studies."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The digital format of the three-photon microscopy data (e.g., TIFF, JPEG), which affects how data is organized, stored, and the compatibility with various imaging analysis software."
            }
        },
        "compression": {
            "title": "Compression",
            "brief": "compression",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Describes any compression applied to the microscopy image files, which can impact file size and potentially affect image quality and processing speed."
            }
        },
        "verticalResolution": {
            "title": "Vertical resolution",
            "brief": "vertical resolution",
            "units": "",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the vertical dimension of each image, affecting the image quality and the detail visible in the microscopy data."
            }
        },
        "horizontalResolution": {
            "title": "Horizontal resolution",
            "brief": "horizontal resolution",
            "units": "",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the horizontal dimension of each image, crucial for accurately capturing detailed features of the observed specimen."
            }
        },
        "frameRate": {
            "title": "Frame rate (Hz)",
            "brief": "frame rate",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The rate at which images are captured, measured in frames per second. Important for studies involving dynamic biological processes."
            }
        },
        "nFrames": {
            "title": "Number of frames",
            "brief": "nFrames",
            "units": "",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The total number of frames captured during the imaging session, which determines the overall length of the video and the duration of the observed biological processes."
            }
        },
        "laserPower": {
            "title": "Laser power (mW)",
            "brief": "laser power",
            "units": "mW",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The power of the laser used during imaging, which is crucial for three-photon excitation to achieve effective depth penetration and image clarity."
            }
        },
        "excitationWavelength": {
            "title": "Excitation wavelength (nm)",
            "brief": "excitation wavelength",
            "units": "nm",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The wavelength of light used to excite the samples, crucial for achieving efficient three-photon excitation and optimizing fluorescence emission from deep tissue structures."
            }
        },
        "imagingDepth": {
            "title": "Imaging depth (\u00b5m)",
            "brief": "imaging depth",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The depth within the sample that the microscope can effectively image, particularly important in three-photon microscopy for deep tissue imaging with minimal light scattering."
            }
        },
        "xVoxelSize": {
            "title": "Voxel size (X dimension)",
            "brief": "x voxel size x",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The size of a single voxel along the X-axis, which affects the spatial resolution of the image in that dimension."
            }
        },
        "yVoxelSize": {
            "title": "Voxel size (Y dimension)",
            "brief": "voxel size y",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The size of a single voxel along the Y-axis, influencing the spatial resolution of the image in that dimension and the detail of structural data."
            }
        },
        "zVoxelSize": {
            "title": "Voxel size (Z dimension)",
            "brief": "voxel size z",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The size of a single voxel along the Z-axis, determining the depth resolution of the image and aiding in three-dimensional reconstructions."
            }
        }
    }
}
```

## TwoPhotonMicroscopy
```
{
    "type": "object",
    "title": "Two-Photon Microscopy",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the file containing two-photon microscopy data, typically including the file extension. This file stores high-resolution images capable of deep tissue penetration with minimal photodamage."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The digital format of the two-photon microscopy data (e.g., TIFF, JPEG), which determines how data is organized, stored, and the compatibility with various imaging analysis software."
            }
        },
        "compression": {
            "title": "Compression",
            "brief": "compression",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Describes any compression applied to the microscopy image files, which can impact file size and potentially affect image quality and processing speed."
            }
        },
        "verticalResolution": {
            "title": "Vertical resolution",
            "brief": "vertical resolution",
            "units": "",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the vertical dimension of each image, affecting the image quality and the detail visible in the microscopy data."
            }
        },
        "horizontalResolution": {
            "title": "Horizontal resolution",
            "brief": "horizontal resolution",
            "units": "",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of pixels in the horizontal dimension of each image, crucial for accurately capturing detailed features of the observed specimen."
            }
        },
        "frameRate": {
            "title": "Frame rate (Hz)",
            "brief": "frame rate",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The rate at which images are captured, measured in frames per second. Important for studies involving dynamic biological processes."
            }
        },
        "nFrames": {
            "title": "Number of frames",
            "brief": "nFrames",
            "type": "integer",
            "units": "",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The total number of frames captured during the imaging session, which determines the overall length of the video and the duration of the observed biological processes."
            }
        },
        "laserPower": {
            "title": "Laser power (mW)",
            "brief": "laser power",
            "units": "mW",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The power of the laser used during imaging, crucial for two-photon excitation to achieve effective depth penetration and image clarity."
            }
        },
        "excitationWavelength": {
            "title": "Excitation wavelength (nm)",
            "brief": "excitation wavelength",
            "units": "nm",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The wavelength of light used to excite the samples, crucial for achieving efficient two-photon excitation and optimizing fluorescence emission from deep tissue structures."
            }
        },
        "imagingDepth": {
            "title": "Imaging depth (\u00b5m)",
            "brief": "imaging depth",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The depth within the sample that the microscope can effectively image, particularly important for deep tissue imaging with minimal light scattering."
            }
        },
        "xVoxelSize": {
            "title": "Voxel size (X dimension)",
            "brief": "x voxel size x",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The size of a single voxel along the X-axis, which affects the spatial resolution of the image in that dimension."
            }
        },
        "yVoxelSize": {
            "title": "Voxel size (Y dimension)",
            "brief": "voxel size y",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The size of a single voxel along the Y-axis, influencing the spatial resolution of the image in that dimension and the detail of structural data."
            }
        },
        "zVoxelSize": {
            "title": "Voxel size (Z dimension)",
            "brief": "voxel size z",
            "units": "\u00b5m",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The size of a single voxel along the Z-axis, determining the depth resolution of the image and aiding in three-dimensional reconstructions."
            }
        }
    }
}
```

## VideoTracking
```
{
    "type": "object",
    "title": "Video Tracking",
    "options": {
        "compact": true,
        "no_additional_properties": true,
        "additionalProperties": false,
        "use_type_default_value": false
    },
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The name of the file containing behavioral tracking data, typically including the file extension (e.g., 'session1.avi')."
            }
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "The video or data file format (e.g., MP4, AVI) used to store behavioral tracking information."
            }
        },
        "compression": {
            "title": "Compression",
            "brief": "compression",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Type of compression used to reduce the file size of the behavioral tracking data, if applicable."
            }
        },
        "frameRate": {
            "title": "Frame rate (Hz)",
            "brief": "frame rate",
            "units": "Hz",
            "type": "number",
            "minimum": 0,
            "options": {
                "infoText": "The number of frames per second at which the behavioral data was recorded, affecting the smoothness and accuracy of motion analysis."
            }
        },
        "nFrames": {
            "title": "Number of frames",
            "brief": "nFrames",
            "units": "",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "Total number of frames included in the behavioral tracking session, which determines the total duration of the recorded data."
            }
        },
        "verticalResolution": {
            "title": "Vertical resolution",
            "brief": "vertical resolution",
            "units": "",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of vertical pixels in each frame, which affects the clarity and detail visible in the behavioral tracking video."
            }
        },
        "horizontalResolution": {
            "title": "Horizontal resolution",
            "brief": "horizontal resolution",
            "units": "",
            "type": "integer",
            "minimum": 0,
            "options": {
                "inputAttributes": {
                    "placeholder": "integer"
                },
                "infoText": "The number of horizontal pixels in each frame, which affects the clarity and detail visible in the behavioral tracking video."
            }
        }
    }
}
```

