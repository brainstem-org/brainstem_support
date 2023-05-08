---
layout: default
title: Experiment data
parent: Schemas
grand_parent: API
nav_order: 1
---

# Experiment data schemas
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
            "format": "text"
        },        
        "nChannels": {
            "title": "Number of channels",
            "brief": "channels",
            "type": "number",
            "minimum": 0,
            "default": 2
        },
        "sr": {
            "title": "Sampling rate (Hz)",
            "brief": "Hz",
            "type": "number",
            "minimum": 0
        },
        "nSamples": {
            "title": "Number of samples",
            "brief": "samples",
            "type": "number",
            "minimum": 0
        },
        "lsb": {
            "title": "Least significant bit (µV/bit)",
            "brief": "µV/bit",
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
    "nChannels": 8,
    "sr": 30000,
    "nSamples": {
        "title": "Number of samples",
        "brief": "samples",
        "type": "number",
        "minimum": 0
    },
    "lsb": {
        "title": "Least significant bit (µV/bit)",
        "brief": "µV/bit",
        "type": "number",
        "minimum": 0
    }
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
        "compression": {
            "title": "Compression",
            "brief": "Compression",
            "type": "string",
            "format": "text"
        },
        "frameRate": {
            "title": "Frame rate (Hz)",
            "brief": "Hz",
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
            "brief": "horzontal pixels",
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
        "sr": {
            "title": "Sampling rate (Hz)",
            "brief": "Hz",
            "type": "number",
            "minimum": 0
        },
        "nChannels": {
            "title": "Number of channels",
            "brief": "channels",
            "type": "number",
            "minimum": 0
        },
        "nSamples": {
            "title": "Number of samples",
            "brief": "samples",
            "type": "number",
            "minimum": 0
        },
        "lsb": {
            "title": "Least significant bit (µV/bit)",
            "brief": "µV/bit",
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
    "title": "Extracellular",
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
            "brief": "Hz",
            "type": "number",
            "minimum": 0,
            "default": 20000
        },        
        "nSamples": {
            "title": "Number of samples",
            "brief": "samples",
            "type": "number",
            "minimum": 0
        },
        "lsb": {
            "title": "Least significant bit (µV/bit)",
            "brief": "µV/bit",
            "type": "number",
            "minimum": 0
        },
        "electrodeGroups": {
          "type": "array",
          "format": "table",
          "title": "Electrode group",
          "options": {"compact": true, "disable_array_delete_last_row":true,"enable_array_copy":true,"disable_properties":false,"disable_edit_json":false,"disable_array_delete_all_rows":false},
          "items": {
            "type": "object",
            "title": "Electrode group",
            "properties": {
              "channels": {
                "type": "string",
                "title": "List of channels"
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
          "options": {"compact": true, "disable_array_delete_last_row":true,"enable_array_copy":true,"disable_properties":false,"disable_edit_json":false,"disable_array_delete_all_rows":false},
          "items": {
            "type": "object",
            "title": "Channel tag",
            "properties": {
              "tag": {
                "type": "string",
                "title": "Channel tag"
              },
              "channels": {
                "type": "string",
                "title": "List of channels"
              }
              ,
              "electrodeGroups": {
                "type": "string",
                "title": "Electrode groups"
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
            {"channels": "0,2", "label": "group1"}, 
            {"channels": "1,3,5", "label": "group2"}
        ], 
        "channelTags": [
            {"tag": "tag2", "channels": "1,3,5", "electrodeGroups": "group2"}, 
            {"tag": "tag1", "channels": "0,2", "electrodeGroups": "group1"}
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
        "sr": {
            "title": "Sampling rate (Hz)",
            "brief": "Hz",
            "type": "number",
            "minimum": 0
        },
        "nChannels": {
            "title": "Number of channels",
            "brief": "channels",
            "type": "number",
            "minimum": 0
        },
        "nSamples": {
            "title": "Number of samples",
            "brief": "samples",
            "type": "number",
            "minimum": 0
        },
        "lsb": {
            "title": "Least significant bit (µV/bit)",
            "brief": "µV/bit",
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
        "sr": {
            "title": "Sampling rate (Hz)",
            "brief": "Hz",
            "type": "number",
            "minimum": 0
        },
        "nChannels": {
            "title": "Number of channels",
            "brief": "channels",
            "type": "number",
            "minimum": 0
        },
        "nSamples": {
            "title": "Number of samples",
            "brief": "samples",
            "type": "number",
            "minimum": 0
        },
        "lsb": {
            "title": "Least significant bit (µV/bit)",
            "brief": "µV/bit",
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