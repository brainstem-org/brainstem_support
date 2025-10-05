---
layout: default
title: Equipment
parent: Schemas
grand_parent: API
nav_order: 1
---

# Equipment schemas
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

## Amplifier
```
{
    "type": "object",
    "title": "Amplifier",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
        "productId": {
            "title": "Product ID",
            "type": "string",
            "format": "text",
            "brief": "product ID",
            "options": {"infoText": "A unique product identifier for the amplifier as defined by the supplier."}
        },
        "nChannels": {
            "title": "Number of Channels",
            "type": "number",
            "units": "",
            "minimum": 1,
            "brief": "nChannels",
            "options": {"infoText": "Number of input channels supported by the amplifier."}
        },
        "gain": {
            "title": "Gain Range",
            "type": "string",
            "format": "text",
            "brief": "gain",
            "options": {"infoText": "Amplification gain range (e.g., '1x - 10,000x', '1000x')."}
        },
        "bandwidth": {
            "title": "Bandwidth",
            "type": "string",
            "format": "text",
            "brief": "bandwidth",
            "options": {"infoText": "Frequency bandwidth of the amplifier (e.g., 'DC - 10 kHz', '0.1 Hz - 7.5 kHz')."}
        },
        "inputImpedance": {
            "title": "Input Impedance",
            "type": "string",
            "format": "text",
            "brief": "input impedance",
            "options": {"infoText": "Input impedance specification (e.g., '>10 GΩ', '1 MΩ')."}
        },
        "noiseLevel": {
            "title": "Noise Level",
            "type": "string",
            "format": "text",
            "brief": "noise",
            "options": {"infoText": "Noise level specification (e.g., '<3 µV RMS', '2.4 µV RMS')."}
        },
        "powerSupply": {
            "title": "Power Supply",
            "type": "string",
            "format": "text",
            "brief": "power",
            "options": {"infoText": "Power supply requirements (e.g., '+/- 15V', '5V USB', 'Battery')."}
        }
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "productId": "AMP-001",
    "nChannels": 32,
    "gain": "1x - 10,000x",
    "bandwidth": "0.1 Hz - 7.5 kHz",
    "inputImpedance": ">10 GΩ",
    "noiseLevel": "<3 µV RMS",
    "powerSupply": "+/- 15V"
}
```

## Anesthesia system
```
{
    "type": "object",
    "title": "Anesthesia system",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Anti-vibration table
```
{
    "type": "object",
    "title": "Anti-vibration table",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Behavior rig
```
{
    "type": "object",
    "title": "Behavior rig",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Biosafety cabinet
```
{
    "type": "object",
    "title": "Biosafety cabinet",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
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

## Camera
```
{
    "type": "object",
    "title": "Camera",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Computer
```
{
    "type": "object",
    "title": "Computer",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Data acquisition system
```
{
    "type": "object",
    "title": "Data acquisition system",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Electroencephalography system
```
{
    "type": "object",
    "title": "Electroencephalography system",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Electromyography machine
```
{
    "type": "object",
    "title": "Electromyography machine",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Electronic component
```
{
    "type": "object",
    "title": "Electronic component",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Ephys rig
```
{
    "type": "object",
    "title": "Ephys rig",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## External identifiers
```
{
    "type": "object",
    "title": "External identifiers",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
        "RRID": {
            "title": "RRID",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Research Resource Identifier (RRID) for the equipment."
            }
        },
        "catalogNumber": {
            "title": "Catalog Number",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Supplier catalog number."
            }
        },
        "serialNumber": {
            "title": "Serial Number",
            "type": "string",
            "format": "text",
            "options": {
                "infoText": "Unique serial number for the specific device."
            }
        }
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "RRID": "RRID:SCR_000001",
    "catalogNumber": "CAT-12345",
    "serialNumber": "SN-67890"
}
```

## Fiber photometry system
```
{
    "type": "object",
    "title": "Fiber photometry system",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Floating air platform
```
{
    "type": "object",
    "title": "Floating air platform",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Force plate
```
{
    "type": "object",
    "title": "Force plate",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Fume hood
```
{
    "type": "object",
    "title": "Fume hood",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Glass micropipette puller
```
{
    "type": "object",
    "title": "Glass micropipette puller",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Humidity controller
```
{
    "type": "object",
    "title": "Humidity controller",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Humidity sensor
```
{
    "type": "object",
    "title": "Humidity sensor",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Injection system
```
{
    "type": "object",
    "title": "Injection system",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Iontophoresis stimulator
```
{
    "type": "object",
    "title": "Iontophoresis stimulator",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Laser
```
{
    "type": "object",
    "title": "Laser",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## LED driver
```
{
    "type": "object",
    "title": "LED driver",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Light emitter
```
{
    "type": "object",
    "title": "Light emitter",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Light sensor
```
{
    "type": "object",
    "title": "Light sensor",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
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
      "brief": "type",
      "type": "string",
      "format": "text",
      "default": "int16"
    },
    "nChannels": {
      "title": "Number of channels",
      "brief": "nChannels",
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

## Magnetic resonance imaging system
```
{
    "type": "object",
    "title": "Magnetic resonance imaging system",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Magnetoencephalography system
```
{
    "type": "object",
    "title": "Magnetoencephalography system",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Magnetometer
```
{
    "type": "object",
    "title": "Magnetometer",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Microcontroller
```
{
    "type": "object",
    "title": "Microcontroller",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Micromanipulator
```
{
    "type": "object",
    "title": "Micromanipulator",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Microphone
```
{
    "type": "object",
    "title": "Microphone",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Microscope
```
{
    "type": "object",
    "title": "Microscope",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Miniscope
```
{
    "type": "object",
    "title": "Miniscope",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Monitor
```
{
    "type": "object",
    "title": "Monitor",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Motion tracking system
```
{
    "type": "object",
    "title": "Motion tracking system",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Noise isolation chamber
```
{
    "type": "object",
    "title": "Noise isolation chamber",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Ophys rig
```
{
    "type": "object",
    "title": "Ophys rig",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Optical coherence tomography
```
{
    "type": "object",
    "title": "Optical coherence tomography",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Oscilloscope
```
{
    "type": "object",
    "title": "Oscilloscope",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Perfusion system
```
{
    "type": "object",
    "title": "Perfusion system",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Photodetector
```
{
    "type": "object",
    "title": "Photodetector",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Running wheel
```
{
    "type": "object",
    "title": "Running wheel",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Signal processing unit
```
{
    "type": "object",
    "title": "Signal processing unit",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Single board computer
```
{
    "type": "object",
    "title": "Single board computer",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Single photon emission computed tomography
```
{
    "type": "object",
    "title": "Single photon emission computed tomography",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Speaker
```
{
    "type": "object",
    "title": "Speaker",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Stereotaxic frame
```
{
    "type": "object",
    "title": "Stereotaxic frame",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Stimulation device
```
{
    "type": "object",
    "title": "Stimulation device",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Surgical power tool
```
{
    "type": "object",
    "title": "Surgical power tool",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Temperature sensor
```
{
    "type": "object",
    "title": "Temperature sensor",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Thermal controller
```
{
    "type": "object",
    "title": "Thermal controller",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Treadmill
```
{
    "type": "object",
    "title": "Treadmill",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Ultrasound imaging system
```
{
    "type": "object",
    "title": "Ultrasound imaging system",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Chemical reagent
```
{
  "type": "object",
  "title": "Chemical Reagent",
  "options": { "compact": true },
  "additionalProperties": false,
  "properties": {
    "productId": {
      "title": "Product ID",
      "type": "string",
      "format": "text",
      "options": {
        "infoText": "Catalog or supplier product code (e.g., 'T8787', 'P6148')."
      }
    },
    "compoundName": {
      "title": "Compound Name",
      "type": "string",
      "format": "text",
      "options": {
        "inputAttributes": { "placeholder": "e.g., 'Triton X-100', 'Paraformaldehyde'" },
        "infoText": "Name of the chemical (e.g., 'Triton X-100', 'Paraformaldehyde')."
      }
    },
    "chemicalType": {
      "title": "Chemical Type",
      "type": "string",
      "enum": [
        "Fixative",
        "Detergent",
        "Salt or Buffer",
        "Solvent",
        "Stain or Dye",
        "Indicator or pH Adjuster",
        "Polymer or Resin",
        "Other"
      ],
      "options": {
        "infoText": "General classification of the reagent."
      }
    },
    "concentration": {
      "title": "Concentration / Strength",
      "brief": "concentration",
      "type": "string",
      "format": "text",
      "options": {
        "inputAttributes": { "placeholder": "e.g., '4%', '1 M', '10X'" },
        "infoText": "If supplied in solution (e.g., '4%', '1 M', '10X')."
      }
    },
    "molecularWeight": {
      "title": "Molecular Weight (g/mol)",
      "brief": "weight",
      "units": "g/mol",
      "type": "number",
      "minimum": 0,
      "options": {
        "inputAttributes": { "placeholder": "numeric" },
        "infoText": "Molecular weight (measured in gram per mol')."
      }
    },
    "purity": {
      "title": "Purity / Grade",
      "type": "string",
      "format": "text",
      "options": {
        "inputAttributes": { "placeholder": "e.g., '≥99%', 'Analytical grade', 'ACS reagent'" },
        "infoText": "E.g., '≥99%', 'Analytical grade', 'ACS reagent'."
      }
    },
    "storageConditions": {
      "title": "Storage Conditions",
      "type": "string",
      "format": "text",
      "options": {
        "inputAttributes": { "placeholder": "e.g., 'Room temp', '4°C', 'Protect from light'" },
        "infoText": "E.g., 'Room temp', '4°C', 'Protect from light'."
      }
    },
    "hazardInfo": {
      "title": "Hazard Information",
      "type": "string",
      "format": "text",
      "options": {
        "inputAttributes": { "placeholder": "e.g., 'Toxic', 'Corrosive', 'Flammable'" },
        "infoText": "Optional summary of safety hazards or GHS classification."
      }
    },
    "experimentalUse": {
      "title": "Experimental Use Context",
      "brief": "experimental use",
      "type": "string",
      "format": "textarea",
      "options": {
        "inputAttributes": { "placeholder": "e.g., 'Perfusion, Fixation', 'Staining'" },
        "infoText": "Typical use cases for the reagent in experimental workflows (e.g. Perfusion, Fixation, Staining,   Buffering)"
      }
    }
  },
  "required": ["chemicalType"]
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "productId": "T8787",
    "compoundName": "Triton X-100",
    "chemicalType": "Detergent",
    "concentration": "10%",
    "molecularWeight": 624.0,
    "purity": "≥99%",
    "storageConditions": "Room temp",
    "hazardInfo": "Irritant",
    "experimentalUse": "Cell permeabilization, Solubilization"
}
```

## Consumable device
```
{
    "type": "object",
    "title": "Consumable device",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Immuno reagent
```
{
    "type": "object",
    "title": "Immuno reagent",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Optical component
```
{
    "type": "object",
    "title": "Optical component",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Optic fiber design
```
{
    "type": "object",
    "title": "Optic fiber design",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Pharmacological agent
```
{
    "type": "object",
    "title": "Pharmacological agent",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Physiological solution
```
{
    "type": "object",
    "title": "Physiological solution",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Silicon probe design
```
{
    "type": "object",
    "title": "Silicon probe design",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Single wire electrode
```
{
    "type": "object",
    "title": "Single wire electrode",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Tracer dye
```
{
    "type": "object",
    "title": "Tracer dye",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```

## Virus construct
```
{
    "type": "object",
    "title": "Virus construct",
    "options": {"compact": true},
    "additionalProperties": false,
    "properties": {
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{}
```