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
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text"
        },
        "format": {
            "title": "Format",
             "brief": "format",
            "type": "string",
            "format": "text"
        },
        "type": {
            "title": "Data-type",
            "brief": "type",
            "type": "string",
            "format": "text"
        },
        "compression": {
            "title": "Compression",
            "brief": "Compression",
            "type": "string",
            "format": "text"
        },
        "bitDepth": {
            "title": "Bit depth",
            "brief": "bit depth",
            "type": "integer",
            "minimum": 0,
            "default": 8
        },
        "codec": {
            "title": "Codec",
            "brief": "codec",
            "type": "string",
            "format": "text"
        },
        "nChannels": {
            "title": "Number of channels",
            "brief": "nChannels",
            "type": "integer",
            "minimum": 1,
            "default": 2
        },
        "sr": {
            "title": "Sampling rate (Hz)",
            "brief": "sr",
            "type": "number",
            "minimum": 0
        },
        "nSamples": {
            "title": "Number of samples",
            "brief": "nSamples",
            "type": "number",
            "minimum": 0
        },
        "lsb": {
            "title": "Least significant bit (µV/bit)",
            "brief": "lsb",
            "type": "number",
            "minimum": 0
        }
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "fileName": "recording.mp3",
    "format": "MP3",
    "type": "int16",
    "compression": "None",
    "bitDepth": 16,
    "codec": "FLAC",
    "nChannels": 8,
    "sr": 30000,
    "nSamples": 600000,
    "lsb": 0.5
}
```


## Behavioral tracking
```
{
    "type": "object",
    "title": "BehavioralTracking",
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text"
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text"
        },
        "compression": {
            "title": "Compression",
            "brief": "Compression",
            "type": "string",
            "format": "text"
        },
        "frameRate": {
            "title": "Frame rate (Hz)",
            "brief": "sr",
            "type": "number",
            "minimum": 0
        },
        "nFrames": {
            "title": "Number of frames",
            "brief": "frames",
            "type": "number",
            "minimum": 0
        },
        "verticalResolution": {
            "title": "Vertical resolution",
            "brief": "vertical pixels",
            "type": "number",
            "minimum": 0
        },
        "horizontalResolution": {
            "title": "Horizontal resolution",
            "brief": "horizontal pixels",
            "type": "number",
            "minimum": 0
        }
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "fileName": "tracking.mp4",
    "format": "MP4",
    "compression": "H.264",
    "frameRate": 60,
    "nFrames": 600,
    "verticalResolution": 1080,
    "horizontalResolution": 1980
}
```

## Electroneurogram
```
{
    "type": "object",
    "title": "Electroneurogram",
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text"
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text"
        },
        "type": {
            "title": "Data-type",
            "brief": "type",
            "type": "string",
            "format": "text",
            "default": "int16"
        },
        "sr": {
            "title": "Sampling rate (Hz)",
            "brief": "sr",
            "type": "number",
            "minimum": 0
        },
        "nChannels": {
            "title": "Number of channels",
            "brief": "nChannels",
            "type": "number",
            "minimum": 0
        },
        "nSamples": {
            "title": "Number of samples",
            "brief": "nSamples",
            "type": "number",
            "minimum": 0
        },
        "lsb": {
            "title": "Least significant bit (µV/bit)",
            "brief": "lsb",
            "type": "number",
            "minimum": 0
        }
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "fileName": "output.dat",
    "format": "DAT",
    "type": "int16",
    "sr": 30000,
    "nChannels": 8,
    "nSamples": 45000000,
    "lsb": 0
}
```

## Extracellular
```
{
  "type": "object",
  "title": "Extracellular Electrophysiology",
  "options": {
    "compact": "true"
  },
  "properties": {
    "fileName": {
      "title": "File name",
      "brief": "File name",
      "type": "string",
      "format": "text"
    },
    "format": {
      "title": "Format",
      "brief": "Format",
      "type": "string",
      "format": "text"
    },
    "type": {
      "title": "Data-type",
      "brief": "Data-type",
      "type": "string",
      "format": "text",
      "default": "int16"
    },
    "nChannels": {
      "title": "Number of channels",
      "brief": "channels",
      "type": "number",
      "minimum": 0
    },
    "sr": {
      "title": "Sampling rate (Hz)",
      "brief": "sr",
      "type": "number",
      "minimum": 0,
      "default": 20000
    },
    "nSamples": {
      "title": "Number of samples",
      "brief": "nSamples",
      "type": "number",
      "minimum": 0
    },
    "lsb": {
      "title": "Least significant bit (µV/bit)",
      "brief": "lsb",
      "type": "number",
      "minimum": 0
    },
    "electrodeGroups": {
      "type": "array",
      "format": "table",
      "title": "Electrode group",
      "options": {
        "compact": true,
        "disable_array_delete_last_row": true,
        "enable_array_copy": true,
        "disable_properties": false,
        "disable_edit_json": false,
        "disable_array_delete_all_rows": false
      },
      "items": {
        "type": "object",
        "title": "Electrode group",
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
            "type": "string"
          }
        }
      }
    },
    "channelTags": {
      "type": "array",
      "format": "table",
      "title": "Channel tag",
      "options": {
        "compact": true,
        "disable_array_delete_last_row": true,
        "enable_array_copy": true,
        "disable_properties": false,
        "disable_edit_json": false,
        "disable_array_delete_all_rows": false
      },
      "items": {
        "type": "object",
        "title": "Channel tag",
        "properties": {
          "tag": {
            "type": "string",
            "title": "Channel tag"
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

### Example of JSON according to this schema
{: .no_toc}
```
{
        "fileName": "output.dat",
        "format": "DAT",
        "type": "int16",
        "sr": 30000,
        "nChannels": 8,
        "nSamples": 45000000,
        "lsb": 0,
        "electrodeGroups": [
            {"channels": [0,2], "label": "group1"}, 
            {"channels": [1,3,5], "label": "group2"}
        ], 
        "channelTags": [
            {"tag": "tag2", "channels": [1,3,5], "electrodeGroups": "group2"}, 
            {"tag": "tag1", "channels": [0,2], "electrodeGroups": "group1"}
        ]
    }
```

## General time series
```
{
    "type": "object",
    "title": "GeneralTimeSeries",
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text"
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text"
        },
        "type": {
            "title": "Data-type",
            "brief": "type",
            "type": "string",
            "format": "text",
            "default": "int16"
        },
        "sr": {
            "title": "Sampling rate (Hz)",
            "brief": "sr",
            "type": "number",
            "minimum": 0
        },
        "nChannels": {
            "title": "Number of channels",
            "brief": "nChannels",
            "type": "number",
            "minimum": 0
        },
        "nSamples": {
            "title": "Number of samples",
            "brief": "nSamples",
            "type": "number",
            "minimum": 0
        },
        "lsb": {
            "title": "Least significant bit (µV/bit)",
            "brief": "lsb",
            "type": "number",
            "minimum": 0
        }
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "fileName": "output.dat",
    "format": "DAT",
    "type": "int16",
    "sr": 30000,
    "nChannels": 8,
    "nSamples": 45000000,
    "lsb": 0
}
```

## Intracellular
```
{
    "type": "object",
    "title": "Intracellular",
    "properties": {
        "fileName": {
            "title": "File name",
            "brief": "file name",
            "type": "string",
            "format": "text"
        },
        "format": {
            "title": "Format",
            "brief": "format",
            "type": "string",
            "format": "text"
        },
        "type": {
            "title": "Data-type",
            "brief": "type",
            "type": "string",
            "format": "text",
            "default": "int16"
        },
        "sr": {
            "title": "Sampling rate (Hz)",
            "brief": "sr",
            "type": "number",
            "minimum": 0
        },
        "nChannels": {
            "title": "Number of channels",
            "brief": "nChannels",
            "type": "number",
            "minimum": 0
        },
        "nSamples": {
            "title": "Number of samples",
            "brief": "nSamples",
            "type": "number",
            "minimum": 0
        },
        "lsb": {
            "title": "Least significant bit (µV/bit)",
            "brief": "lsb",
            "type": "number",
            "minimum": 0
        }
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "fileName": "output.dat",
    "format": "DAT",
    "type": "int16",
    "sr": 30000,
    "nChannels": 2,
    "nSamples": 45000000,
    "lsb": 0
}
```

## Computed tomography
```
{
  "type": "object",
  "title": "ComputedTomography",
  "properties": {
    "fileName": {
      "title": "File name",
      "brief": "file name",
      "type": "string",
      "format": "text"
    },
    "format": {
      "title": "Format",
      "brief": "format",
      "type": "string",
      "format": "text"
    },
    "compression": {
      "title": "Compression",
      "brief": "compression",
      "type": "string",
      "format": "text"
    },
    "frameRate": {
      "title": "Frame rate (Hz)",
      "brief": "frame rate",
      "type": "number",
      "minimum": 0
    },
    "nFrames": {
      "title": "Number of frames",
      "brief": "nFrames",
      "type": "integer",
      "minimum": 0
    },
    "verticalResolution": {
      "title": "Vertical resolution",
      "brief": "vertical resolution",
      "type": "integer",
      "minimum": 0
    },
    "horizontalResolution": {
      "title": "Horizontal resolution",
      "brief": "horizontal resolution",
      "type": "integer",
      "minimum": 0
    },
    "laserPower": {
      "title": "Laser power (mW)",
      "brief": "laser power",
      "type": "number",
      "minimum": 0
    },
    "imagingDepth": {
      "title": "Imaging depth (µm)",
      "brief": "imaging depth",
      "type": "number",
      "minimum": 0
    }
  }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
  "fileName": "scan.dcm",
  "format": "DICOM",
  "compression": "lossless",
  "frameRate": 30,
  "nFrames": 500,
  "verticalResolution": 512,
  "horizontalResolution": 512,
  "laserPower": 50,
  "imagingDepth": 10000
}
```

## Confocal microscopy
```
{
  "type": "object",
  "title": "Confocal Microscopy",
  "properties": {
    "fileName": {
      "title": "File name",
      "brief": "file name",
      "type": "string",
      "format": "text"
    },
    "format": {
      "title": "Format",
      "brief": "format",
      "type": "string",
      "format": "text"
    },
    "compression": {
      "title": "Compression",
      "brief": "compression",
      "type": "string",
      "format": "text"
    },
    "verticalResolution": {
      "title": "Vertical resolution",
      "brief": "vertical resolution",
      "type": "integer",
      "minimum": 0
    },
    "horizontalResolution": {
      "title": "Horizontal resolution",
      "brief": "horizontal resolution",
      "type": "integer",
      "minimum": 0
    },
    "frameRate": {
      "title": "Frame rate (Hz)",
      "brief": "frame rate",
      "type": "number",
      "minimum": 0
    },
    "nFrames": {
      "title": "Number of frames",
      "brief": "nFrames",
      "type": "integer",
      "minimum": 0
    },
    "laserPower": {
      "title": "Laser power (mW)",
      "brief": "laser power",
      "type": "number",
      "minimum": 0
    },
    "excitationWavelength": {
      "title": "Excitation wavelength (nm)",
      "brief": "excitation wavelength",
      "type": "number",
      "minimum": 0
    },
    "imagingDepth": {
      "title": "Imaging depth (µm)",
      "brief": "imaging depth",
      "type": "number",
      "minimum": 0
    },
    "xVoxelSize": {
      "title": "Voxel size (X dimension)",
      "brief": "x voxel size x",
      "type": "number",
      "minimum": 0
    },
    "yVoxelSize": {
      "title": "Voxel size (Y dimension)",
      "brief": "voxel size y",
      "type": "number",
      "minimum": 0
    },
    "zVoxelSize": {
      "title": "Voxel size (Z dimension)",
      "brief": "voxel size z",
      "type": "number",
      "minimum": 0
    }
  }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
  "fileName": "cell_image.tif",
  "format": "TIFF",
  "compression": "lossless",
  "verticalResolution": 1024,
  "horizontalResolution": 1024,
  "frameRate": 5,
  "nFrames": 100,
  "laserPower": 25,
  "excitationWavelength": 488,
  "imagingDepth": 50,
  "xVoxelSize": 0.5,
  "yVoxelSize": 0.5,
  "zVoxelSize": 1.0
}
```

## Electroencephalography
```
{
  "type": "object",
  "title": "Electroencephalography (EEG)",
  "properties": {
    "fileName": {
      "title": "File name",
      "brief": "file name",
      "type": "string",
      "format": "text"
    },
    "format": {
      "title": "Format",
      "brief": "format",
      "type": "string",
      "format": "text"
    },
    "type": {
      "title": "Data-type",
      "brief": "type",
      "type": "string",
      "format": "text",
      "default": "int16"
    },
    "nChannels": {
      "title": "Number of channels",
      "brief": "nChannels",
      "type": "integer",
      "minimum": 0
    },
    "sr": {
      "title": "Sampling rate (Hz)",
      "brief": "sr",
      "type": "number",
      "minimum": 0,
      "default": 20000
    },
    "nSamples": {
      "title": "Number of samples",
      "brief": "nSamples",
      "type": "integer",
      "minimum": 0
    },
    "lsb": {
      "title": "Least significant bit (µV/bit)",
      "brief": "lsb",
      "type": "number",
      "minimum": 0
    },
    "electrodeGroups": {
      "type": "array",
      "format": "table",
      "title": "Electrode groups",
      "items": {
        "type": "object",
        "title": "Electrode group",
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
            "brief": "Label"
          }
        }
      }
    },
    "channelTags": {
      "type": "array",
      "format": "table",
      "title": "Channel tags",
      "items": {
        "type": "object",
        "title": "Channel tag",
        "properties": {
          "tag": {
            "type": "string",
            "title": "Channel tag"
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

### Example of JSON according to this schema
{: .no_toc}
```
{
  "fileName": "eeg_recording.edf",
  "format": "EDF",
  "type": "int16",
  "nChannels": 32,
  "sr": 500,
  "nSamples": 150000,
  "lsb": 0.5,
  "electrodeGroups": [
    {"channels": [0,1,2,3], "label": "frontal"},
    {"channels": [4,5,6,7], "label": "parietal"}
  ],
  "channelTags": [
    {"tag": "reference", "channels": [0], "groups": [0]},
    {"tag": "ground", "channels": [31], "groups": [1]}
  ]
}
```

## Fiber photometry
```
{
  "type": "object",
  "title": "Fiber Photometry",
  "properties": {
    "fileName": {
      "title": "File name",
      "brief": "file name",
      "type": "string",
      "format": "text"
    },
    "format": {
      "title": "Format",
      "brief": "format",
      "type": "string",
      "format": "text"
    },
    "compression": {
      "title": "Compression",
      "brief": "compression",
      "type": "string",
      "format": "text"
    },
    "frameRate": {
      "title": "Frame rate (Hz)",
      "brief": "frame rate",
      "type": "number",
      "minimum": 0
    },
    "nFrames": {
      "title": "Number of frames",
      "brief": "nFrames",
      "type": "integer",
      "minimum": 0
    },
    "laserPower": {
      "title": "Laser power (mW)",
      "brief": "laser power",
      "type": "number",
      "minimum": 0
    },
    "excitationWavelength": {
      "title": "Excitation wavelength (nm)",
      "brief": "excitation wavelength",
      "type": "number",
      "minimum": 0
    }
  }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
  "fileName": "photometry.csv",
  "format": "CSV",
  "compression": "none",
  "frameRate": 100,
  "nFrames": 60000,
  "laserPower": 15,
  "excitationWavelength": 470
}
```

## Functional magnetic resonance imaging
```
{
  "type": "object",
  "title": "Functional Magnetic Resonance Imaging",
  "properties": {
    "fileName": {
      "title": "File name",
      "brief": "file name",
      "type": "string",
      "format": "text"
    },
    "format": {
      "title": "Format",
      "brief": "format",
      "type": "string",
      "format": "text"
    },
    "compression": {
      "title": "Compression",
      "brief": "compression",
      "type": "string",
      "format": "text"
    },
    "frameRate": {
      "title": "Frame rate (Hz)",
      "brief": "frame rate",
      "type": "number",
      "minimum": 0
    },
    "nFrames": {
      "title": "Number of frames",
      "brief": "nFrames",
      "type": "integer",
      "minimum": 0
    },
    "verticalResolution": {
      "title": "Vertical resolution",
      "brief": "vertical resolution",
      "type": "integer",
      "minimum": 0
    },
    "horizontalResolution": {
      "title": "Horizontal resolution",
      "brief": "horizontal resolution",
      "type": "integer",
      "minimum": 0
    },
    "laserPower": {
      "title": "Laser power (mW)",
      "brief": "laser power",
      "type": "number",
      "minimum": 0
    },
    "imagingDepth": {
      "title": "Imaging depth (µm)",
      "brief": "imaging depth",
      "type": "number",
      "minimum": 0
    }
  }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
  "fileName": "fmri_scan.nii",
  "format": "NIfTI",
  "compression": "gzip",
  "frameRate": 0.5,
  "nFrames": 300,
  "verticalResolution": 64,
  "horizontalResolution": 64,
  "laserPower": 0,
  "imagingDepth": 50000
}
```

## Functional ultrasound imaging
```
{
  "type": "object",
  "title": "Functional Ultrasound Imaging",
  "properties": {
    "fileName": {
      "title": "File name",
      "brief": "file name",
      "type": "string",
      "format": "text"
    },
    "format": {
      "title": "Format",
      "brief": "format",
      "type": "string",
      "format": "text"
    },
    "compression": {
      "title": "Compression",
      "brief": "compression",
      "type": "string",
      "format": "text"
    },
    "frameRate": {
      "title": "Frame rate (Hz)",
      "brief": "frame rate",
      "type": "number",
      "minimum": 0
    },
    "nFrames": {
      "title": "Number of frames",
      "brief": "nFrames",
      "type": "integer",
      "minimum": 0
    },
    "verticalResolution": {
      "title": "Vertical resolution",
      "brief": "vertical resolution",
      "type": "integer",
      "minimum": 0
    },
    "horizontalResolution": {
      "title": "Horizontal resolution",
      "brief": "horizontal resolution",
      "type": "integer",
      "minimum": 0
    },
    "laserPower": {
      "title": "Laser power (mW)",
      "brief": "laser power",
      "type": "number",
      "minimum": 0
    },
    "imagingDepth": {
      "title": "Imaging depth (µm)",
      "brief": "imaging depth",
      "type": "number",
      "minimum": 0
    }
  }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
  "fileName": "ultrasound_scan.fus",
  "format": "DICOM",
  "compression": "none",
  "frameRate": 500,
  "nFrames": 5000,
  "verticalResolution": 256,
  "horizontalResolution": 256,
  "laserPower": 10,
  "imagingDepth": 8000
}
```

## Light field microscopy
```
{
  "type": "object",
  "title": "Light Field Microscopy",
  "properties": {
    "fileName": {
      "title": "File name",
      "brief": "file name",
      "type": "string",
      "format": "text"
    },
    "format": {
      "title": "Format",
      "brief": "format",
      "type": "string",
      "format": "text"
    },
    "compression": {
      "title": "Compression",
      "brief": "compression",
      "type": "string",
      "format": "text"
    },
    "verticalResolution": {
      "title": "Vertical resolution",
      "brief": "vertical resolution",
      "type": "integer",
      "minimum": 0
    },
    "horizontalResolution": {
      "title": "Horizontal resolution",
      "brief": "horizontal resolution",
      "type": "integer",
      "minimum": 0
    },
    "frameRate": {
      "title": "Frame rate (Hz)",
      "brief": "frame rate",
      "type": "number",
      "minimum": 0
    },
    "nFrames": {
      "title": "Number of frames",
      "brief": "nFrames",
      "type": "integer",
      "minimum": 0
    },
    "laserPower": {
      "title": "Laser power (mW)",
      "brief": "laser power",
      "type": "number",
      "minimum": 0
    },
    "excitationWavelength": {
      "title": "Excitation wavelength (nm)",
      "brief": "excitation wavelength",
      "type": "number",
      "minimum": 0
    },
    "imagingDepth": {
      "title": "Imaging depth (µm)",
      "brief": "imaging depth",
      "type": "number",
      "minimum": 0
    },
    "xVoxelSize": {
      "title": "Voxel size (X dimension)",
      "brief": "x voxel size",
      "type": "number",
      "minimum": 0
    },
    "yVoxelSize": {
      "title": "Voxel size (Y dimension)",
      "brief": "y voxel size",
      "type": "number",
      "minimum": 0
    },
    "zVoxelSize": {
      "title": "Voxel size (Z dimension)",
      "brief": "z voxel size",
      "type": "number",
      "minimum": 0
    }
  }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
  "fileName": "lightfield_data.lfp",
  "format": "TIFF",
  "compression": "none",
  "verticalResolution": 2048,
  "horizontalResolution": 2048,
  "frameRate": 10,
  "nFrames": 500,
  "laserPower": 30,
  "excitationWavelength": 560,
  "imagingDepth": 100,
  "xVoxelSize": 0.2,
  "yVoxelSize": 0.2,
  "zVoxelSize": 0.5
}
```

## Magnetic resonance imaging
```
{
  "type": "object",
  "title": "Magnetic Resonance Imaging",
  "properties": {
    "fileName": {
      "title": "File name",
      "brief": "file name",
      "type": "string",
      "format": "text"
    },
    "format": {
      "title": "Format",
      "brief": "format",
      "type": "string",
      "format": "text"
    },
    "compression": {
      "title": "Compression",
      "brief": "compression",
      "type": "string",
      "format": "text"
    },
    "frameRate": {
      "title": "Frame rate (Hz)",
      "brief": "frame rate",
      "type": "number",
      "minimum": 0
    },
    "nFrames": {
      "title": "Number of frames",
      "brief": "nFrames",
      "type": "integer",
      "minimum": 0
    },
    "verticalResolution": {
      "title": "Vertical resolution",
      "brief": "vertical resolution",
      "type": "integer",
      "minimum": 0
    },
    "horizontalResolution": {
      "title": "Horizontal resolution",
      "brief": "horizontal resolution",
      "type": "integer",
      "minimum": 0
    },
    "laserPower": {
      "title": "Laser power (mW)",
      "brief": "laser power",
      "type": "number",
      "minimum": 0
    },
    "imagingDepth": {
      "title": "Imaging depth (µm)",
      "brief": "imaging depth",
      "type": "number",
      "minimum": 0
    }
  }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
  "fileName": "mri_scan.nii",
  "format": "NIfTI",
  "compression": "gzip",
  "frameRate": 0.5,
  "nFrames": 200,
  "verticalResolution": 128,
  "horizontalResolution": 128,
  "laserPower": 0,
  "imagingDepth": 100000
}
```

## Magnetoencephalography
```
{
  "type": "object",
  "title": "Magnetoencephalography",
  "properties": {
    "fileName": {
      "title": "File name",
      "brief": "file name",
      "type": "string",
      "format": "text"
    },
    "format": {
      "title": "Format",
      "brief": "format",
      "type": "string",
      "format": "text"
    },
    "compression": {
      "title": "Compression",
      "brief": "compression",
      "type": "string",
      "format": "text"
    },
    "frameRate": {
      "title": "Frame rate (Hz)",
      "brief": "frame rate",
      "type": "number",
      "minimum": 0
    },
    "nFrames": {
      "title": "Number of frames",
      "brief": "nFrames",
      "type": "integer",
      "minimum": 0
    },
    "verticalResolution": {
      "title": "Vertical resolution",
      "brief": "vertical resolution",
      "type": "integer",
      "minimum": 0
    },
    "horizontalResolution": {
      "title": "Horizontal resolution",
      "brief": "horizontal resolution",
      "type": "integer",
      "minimum": 0
    },
    "laserPower": {
      "title": "Laser power (mW)",
      "brief": "laser power",
      "type": "number",
      "minimum": 0
    },
    "imagingDepth": {
      "title": "Imaging depth (µm)",
      "brief": "imaging depth",
      "type": "number",
      "minimum": 0
    }
  }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
  "fileName": "meg_recording.fif",
  "format": "FIFF",
  "compression": "none",
  "frameRate": 1000,
  "nFrames": 120000,
  "verticalResolution": 306,
  "horizontalResolution": 306,
  "laserPower": 0,
  "imagingDepth": 50000
}
```

## Miniscope microscopy
```
{
  "type": "object",
  "title": "Miniscope Microscopy",
  "properties": {
    "fileName": {
      "title": "File name",
      "brief": "file name",
      "type": "string",
      "format": "text"
    },
    "format": {
      "title": "Format",
      "brief": "format",
      "type": "string",
      "format": "text"
    },
    "compression": {
      "title": "Compression",
      "brief": "compression",
      "type": "string",
      "format": "text"
    },
    "frameRate": {
      "title": "Frame rate (Hz)",
      "brief": "frame rate",
      "type": "number",
      "minimum": 0
    },
    "nFrames": {
      "title": "Number of frames",
      "brief": "nFrames",
      "type": "integer",
      "minimum": 0
    },
    "verticalResolution": {
      "title": "Vertical resolution",
      "brief": "vertical resolution",
      "type": "integer",
      "minimum": 0
    },
    "horizontalResolution": {
      "title": "Horizontal resolution",
      "brief": "horizontal resolution",
      "type": "integer",
      "minimum": 0
    },
    "laserPower": {
      "title": "Laser power (mW)",
      "brief": "laser power",
      "type": "number",
      "minimum": 0
    },
    "imagingDepth": {
      "title": "Imaging depth (µm)",
      "brief": "imaging depth",
      "type": "number",
      "minimum": 0
    }
  }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
  "fileName": "miniscope_recording.avi",
  "format": "AVI",
  "compression": "MJPEG",
  "frameRate": 30,
  "nFrames": 18000,
  "verticalResolution": 600,
  "horizontalResolution": 800,
  "laserPower": 5,
  "imagingDepth": 150
}
```

## Optical coherence tomography
```
{
  "type": "object",
  "title": "Optical Coherence Tomography (OCT)",
  "properties": {
    "fileName": {
      "title": "File name",
      "brief": "file name",
      "type": "string",
      "format": "text"
    },
    "format": {
      "title": "Format",
      "brief": "format",
      "type": "string",
      "format": "text"
    },
    "compression": {
      "title": "Compression",
      "brief": "compression",
      "type": "string",
      "format": "text"
    },
    "verticalResolution": {
      "title": "Vertical resolution",
      "brief": "vertical resolution",
      "type": "integer",
      "minimum": 0
    },
    "horizontalResolution": {
      "title": "Horizontal resolution",
      "brief": "horizontal resolution",
      "type": "integer",
      "minimum": 0
    },
    "frameRate": {
      "title": "Frame rate (Hz)",
      "brief": "frame rate",
      "type": "number",
      "minimum": 0
    },
    "nFrames": {
      "title": "Number of frames",
      "brief": "nFrames",
      "type": "integer",
      "minimum": 0
    },
    "centerWavelength": {
      "title": "Center wavelength (nm)",
      "brief": "center wavelength",
      "type": "number",
      "minimum": 0
    },
    "bandwidth": {
      "title": "Bandwidth (nm)",
      "brief": "bandwidth",
      "type": "number",
      "minimum": 0
    },
    "imagingDepth": {
      "title": "Imaging depth (µm)",
      "brief": "imaging depth",
      "type": "number",
      "minimum": 0
    },
    "axialResolution": {
      "title": "Axial resolution (µm)",
      "brief": "axial resolution",
      "type": "number",
      "minimum": 0
    },
    "lateralResolution": {
      "title": "Lateral resolution (µm)",
      "brief": "lateral resolution",
      "type": "number",
      "minimum": 0
    },
    "scanPattern": {
      "title": "Scan pattern",
      "brief": "scan pattern",
      "type": "string",
      "format": "text"
    },
    "scanArea": {
      "title": "Scan area (mm²)",
      "brief": "scan area",
      "type": "number",
      "minimum": 0
    },
    "averages": {
      "title": "Number of averages",
      "brief": "averages",
      "type": "integer",
      "minimum": 0
    }
  }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
  "fileName": "oct_scan.dcm",
  "format": "DICOM",
  "compression": "none",
  "verticalResolution": 512,
  "horizontalResolution": 1024,
  "frameRate": 100,
  "nFrames": 2000,
  "centerWavelength": 1300,
  "bandwidth": 100,
  "imagingDepth": 2000,
  "axialResolution": 10,
  "lateralResolution": 15,
  "scanPattern": "raster",
  "scanArea": 25,
  "averages": 2
}
```

## Positron emission tomography
```
{
  "type": "object",
  "title": "Positron Emission Tomography",
  "properties": {
    "fileName": {
      "title": "File name",
      "brief": "file name",
      "type": "string",
      "format": "text"
    },
    "format": {
      "title": "Format",
      "brief": "format",
      "type": "string",
      "format": "text"
    },
    "compression": {
      "title": "Compression",
      "brief": "compression",
      "type": "string",
      "format": "text"
    },
    "frameRate": {
      "title": "Frame rate (Hz)",
      "brief": "frameRate",
      "type": "number",
      "minimum": 0
    },
    "nFrames": {
      "title": "Number of frames",
      "brief": "nFrames",
      "type": "integer",
      "minimum": 0
    },
    "verticalResolution": {
      "title": "Vertical resolution",
      "brief": "vertical resolution",
      "type": "integer",
      "minimum": 0
    },
    "horizontalResolution": {
      "title": "Horizontal resolution",
      "brief": "horizontal resolution",
      "type": "integer",
      "minimum": 0
    },
    "laserPower": {
      "title": "Laser power (mW)",
      "brief": "laserPower",
      "type": "number",
      "minimum": 0
    },
    "imagingDepth": {
      "title": "Imaging depth (µm)",
      "brief": "imagingDepth",
      "type": "number",
      "minimum": 0
    }
  }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
  "fileName": "pet_scan.nii",
  "format": "NIfTI",
  "compression": "gzip",
  "frameRate": 0.1,
  "nFrames": 60,
  "verticalResolution": 128,
  "horizontalResolution": 128,
  "laserPower": 0,
  "imagingDepth": 200000
}
```

## Single photon emission computed tomography
```
{
  "type": "object",
  "title": "Single Photon Emission Computed Tomography",
  "properties": {
    "fileName": {
      "title": "File name",
      "brief": "file name",
      "type": "string",
      "format": "text"
    },
    "format": {
      "title": "Format",
      "brief": "format",
      "type": "string",
      "format": "text"
    },
    "compression": {
      "title": "Compression",
      "brief": "compression",
      "type": "string",
      "format": "text"
    },
    "frameRate": {
      "title": "Frame rate (Hz)",
      "brief": "frame rate",
      "type": "number",
      "minimum": 0
    },
    "nFrames": {
      "title": "Number of frames",
      "brief": "nFrames",
      "type": "integer",
      "minimum": 0
    },
    "verticalResolution": {
      "title": "Vertical resolution",
      "brief": "vertical resolution",
      "type": "integer",
      "minimum": 0
    },
    "horizontalResolution": {
      "title": "Horizontal resolution",
      "brief": "horizontal resolution",
      "type": "integer",
      "minimum": 0
    },
    "laserPower": {
      "title": "Laser power (mW)",
      "brief": "laser power",
      "type": "number",
      "minimum": 0
    },
    "imagingDepth": {
      "title": "Imaging depth (µm)",
      "brief": "imaging depth",
      "type": "number",
      "minimum": 0
    }
  }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
  "fileName": "spect_scan.dcm",
  "format": "DICOM",
  "compression": "none",
  "frameRate": 0.05,
  "nFrames": 120,
  "verticalResolution": 128,
  "horizontalResolution": 128,
  "laserPower": 0,
  "imagingDepth": 200000
}
```

## Single photon microscopy
```
{
  "type": "object",
  "title": "Single-Photon Microscopy",
  "properties": {
    "fileName": {
      "title": "File name",
      "brief": "file name",
      "type": "string",
      "format": "text"
    },
    "format": {
      "title": "Format",
      "brief": "format",
      "type": "string",
      "format": "text"
    },
    "compression": {
      "title": "Compression",
      "brief": "compression",
      "type": "string",
      "format": "text"
    },
    "verticalResolution": {
      "title": "Vertical resolution",
      "brief": "vertical resolution",
      "type": "integer",
      "minimum": 0
    },
    "horizontalResolution": {
      "title": "Horizontal resolution",
      "brief": "horizontal resolution",
      "type": "integer",
      "minimum": 0
    },
    "frameRate": {
      "title": "Frame rate (Hz)",
      "brief": "frame rate",
      "type": "number",
      "minimum": 0
    },
    "nFrames": {
      "title": "Number of frames",
      "brief": "nFrames",
      "type": "integer",
      "minimum": 0
    },
    "laserPower": {
      "title": "Laser power (mW)",
      "brief": "laser power",
      "type": "number",
      "minimum": 0
    },
    "excitationWavelength": {
      "title": "Excitation wavelength (nm)",
      "brief": "excitation wavelength",
      "type": "number",
      "minimum": 0
    },
    "imagingDepth": {
      "title": "Imaging depth (µm)",
      "brief": "imaging depth",
      "type": "number",
      "minimum": 0
    },
    "xVoxelSize": {
      "title": "Voxel size (X dimension)",
      "brief": "x voxel size x",
      "type": "number",
      "minimum": 0
    },
    "yVoxelSize": {
      "title": "Voxel size (Y dimension)",
      "brief": "voxel size y",
      "type": "number",
      "minimum": 0
    },
    "zVoxelSize": {
      "title": "Voxel size (Z dimension)",
      "brief": "voxel size z",
      "type": "number",
      "minimum": 0
    }
  }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
  "fileName": "singlephoton_image.tif",
  "format": "TIFF",
  "compression": "none",
  "verticalResolution": 2048,
  "horizontalResolution": 2048,
  "frameRate": 5,
  "nFrames": 100,
  "laserPower": 10,
  "excitationWavelength": 488,
  "imagingDepth": 50,
  "xVoxelSize": 0.1,
  "yVoxelSize": 0.1,
  "zVoxelSize": 0.3
}
```

## Three photon microscopy
```
{
  "type": "object",
  "title": "Three-Photon Microscopy",
  "properties": {
    "fileName": {
      "title": "File name",
      "brief": "file name",
      "type": "string",
      "format": "text"
    },
    "format": {
      "title": "Format",
      "brief": "format",
      "type": "string",
      "format": "text"
    },
    "compression": {
      "title": "Compression",
      "brief": "compression",
      "type": "string",
      "format": "text"
    },
    "verticalResolution": {
      "title": "Vertical resolution",
      "brief": "vertical resolution",
      "type": "integer",
      "minimum": 0
    },
    "horizontalResolution": {
      "title": "Horizontal resolution",
      "brief": "horizontal resolution",
      "type": "integer",
      "minimum": 0
    },
    "frameRate": {
      "title": "Frame rate (Hz)",
      "brief": "frame rate",
      "type": "number",
      "minimum": 0
    },
    "nFrames": {
      "title": "Number of frames",
      "brief": "nFrames",
      "type": "integer",
      "minimum": 0
    },
    "laserPower": {
      "title": "Laser power (mW)",
      "brief": "laser power",
      "type": "number",
      "minimum": 0
    },
    "excitationWavelength": {
      "title": "Excitation wavelength (nm)",
      "brief": "excitation wavelength",
      "type": "number",
      "minimum": 0
    },
    "imagingDepth": {
      "title": "Imaging depth (µm)",
      "brief": "imaging depth",
      "type": "number",
      "minimum": 0
    },
    "xVoxelSize": {
      "title": "Voxel size (X dimension)",
      "brief": "x voxel size x",
      "type": "number",
      "minimum": 0
    },
    "yVoxelSize": {
      "title": "Voxel size (Y dimension)",
      "brief": "voxel size y",
      "type": "number",
      "minimum": 0
    },
    "zVoxelSize": {
      "title": "Voxel size (Z dimension)",
      "brief": "voxel size z",
      "type": "number",
      "minimum": 0
    }
  }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
  "fileName": "threephoton_image.tif",
  "format": "TIFF",
  "compression": "none",
  "verticalResolution": 1024,
  "horizontalResolution": 1024,
  "frameRate": 2,
  "nFrames": 50,
  "laserPower": 50,
  "excitationWavelength": 1300,
  "imagingDepth": 1000,
  "xVoxelSize": 0.3,
  "yVoxelSize": 0.3,
  "zVoxelSize": 1.0
}
```

## Two photon microscopy
```
{
  "type": "object",
  "title": "Two-Photon Microscopy",
  "properties": {
    "fileName": {
      "title": "File name",
      "brief": "file name",
      "type": "string",
      "format": "text"
    },
    "format": {
      "title": "Format",
      "brief": "format",
      "type": "string",
      "format": "text"
    },
    "compression": {
      "title": "Compression",
      "brief": "compression",
      "type": "string",
      "format": "text"
    },
    "verticalResolution": {
      "title": "Vertical resolution",
      "brief": "vertical resolution",
      "type": "integer",
      "minimum": 0
    },
    "horizontalResolution": {
      "title": "Horizontal resolution",
      "brief": "horizontal resolution",
      "type": "integer",
      "minimum": 0
    },
    "frameRate": {
      "title": "Frame rate (Hz)",
      "brief": "frame rate",
      "type": "number",
      "minimum": 0
    },
    "nFrames": {
      "title": "Number of frames",
      "brief": "nFrames",
      "type": "integer",
      "minimum": 0
    },
    "laserPower": {
      "title": "Laser power (mW)",
      "brief": "laser power",
      "type": "number",
      "minimum": 0
    },
    "excitationWavelength": {
      "title": "Excitation wavelength (nm)",
      "brief": "excitation wavelength",
      "type": "number",
      "minimum": 0
    },
    "imagingDepth": {
      "title": "Imaging depth (µm)",
      "brief": "imaging depth",
      "type": "number",
      "minimum": 0
    },
    "xVoxelSize": {
      "title": "Voxel size (X dimension)",
      "brief": "x voxel size x",
      "type": "number",
      "minimum": 0
    },
    "yVoxelSize": {
      "title": "Voxel size (Y dimension)",
      "brief": "voxel size y",
      "type": "number",
      "minimum": 0
    },
    "zVoxelSize": {
      "title": "Voxel size (Z dimension)",
      "brief": "voxel size z",
      "type": "number",
      "minimum": 0
    }
  }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
  "fileName": "twophoton_image.tif",
  "format": "TIFF",
  "compression": "none",
  "verticalResolution": 512,
  "horizontalResolution": 512,
  "frameRate": 10,
  "nFrames": 200,
  "laserPower": 30,
  "excitationWavelength": 920,
  "imagingDepth": 500,
  "xVoxelSize": 0.2,
  "yVoxelSize": 0.2,
  "zVoxelSize": 0.8
}
```

## Video tracking
```
{
  "type": "object",
  "title": "Video Tracking",
  "properties": {
    "fileName": {
      "title": "File name",
      "brief": "file name",
      "type": "string",
      "format": "text"
    },
    "format": {
      "title": "Format",
      "brief": "format",
      "type": "string",
      "format": "text"
    },
    "compression": {
      "title": "Compression",
      "brief": "compression",
      "type": "string",
      "format": "text"
    },
    "frameRate": {
      "title": "Frame rate (Hz)",
      "brief": "frame rate",
      "type": "number",
      "minimum": 0
    },
    "nFrames": {
      "title": "Number of frames",
      "brief": "nFrames",
      "type": "integer",
      "minimum": 0
    },
    "verticalResolution": {
      "title": "Vertical resolution",
      "brief": "vertical resolution",
      "type": "integer",
      "minimum": 0
    },
    "horizontalResolution": {
      "title": "Horizontal resolution",
      "brief": "horizontal resolution",
      "type": "integer",
      "minimum": 0
    }
  }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
  "fileName": "behavioral_tracking.mp4",
  "format": "MP4",
  "compression": "H.264",
  "frameRate": 30,
  "nFrames": 9000,
  "verticalResolution": 1080,
  "horizontalResolution": 1920
}
```