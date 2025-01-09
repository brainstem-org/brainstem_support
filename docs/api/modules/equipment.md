---
layout: default
title: Equipment
parent: Modules
grand_parent: API
nav_order: 4
---

# Equipment API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `type` | string **[required]**. *See options below* |
| `setup` | related experimental setup ID formatted as a string **[required]** |
| `notes` | string [max length: 500] |
| `date_time` | string containing date (e.g. "2023-03-22") |
| `consumable` | related consumable ID formatted as a string |
| `hardwaredevice` | related hardware device ID formatted as a string |
| `coordinates_system` | string **[required]**. *See options below* |
| `coordinates_details` | JSON object. *See accepted schemas below* |


## Types of equipment

### Data acquisition
- `Amplifier`: Amplifier
- `Camera`, Camera
- `DataAcquisitionSystem`: Data acquisition system
- `ElectroencephalographySystem`: Electroencephalography system (EEG)
- `ElectromyographyMachine`: Electromyography machine
- `EphysRig`: Ephys rig
- `FiberPhotometrySystem`: Fiber photometry system
- `ForcePlate`: Force plate
- `HumiditySensor`: Humidity sensor
- `LightSensor`: Light sensor
- `MagneticResonanceImagingSystem`: Magnetic resonance imaging (MRI) system
- `MagnetoencephalographySystem`: Magnetoencephalography (MEG) system
- `Magnetometer`: Magnetometer
- `Microphone`: Microphone
- `Miniscope`: Miniscope
- `MotionTrackingSystem`: Motion tracking system
- `OphysRig`: Ophys rig
- `OpticalCoherenceTomography`: Optical Coherence Tomography (OCT)
- `Oscilloscope`: Oscilloscope
- `Photodetector`: Photodetector
- `SignalProcessingUnit`: Signal processing unit
- `SinglePhotonEmissionComputedTomography`: Single-photon emission computed tomography (SPECT)
- `TemperatureSensor`: Temperature sensor
- `UltrasoundImagingSystem`: Ultrasound imaging system

### Behavioral and stimulation tools
- `BehaviorRig`: Behavior rig
- `IontophoresisStimulator`: Iontophoresis stimulator
- `Laser`: Laser
- `LedDriver`: LED Driver
- `LightEmitter`: Light emitter
- `RunningWheel`: Running Wheel
- `Speaker`: Speaker
- `StimulationDevice`: Stimulation device
- `Treadmill`: Treadmill

### Environmental controllers
- `AntiVibrationTable`: Anti-vibration table
- `FloatingAirPlatform`: Floating air platform
- `HumidityController`: Humidity controller
- `NoiseIsolationChamber`: Noise isolation chamber
- `ThermalController`: Thermal controller

### Surgical equipment
- `AnesthesiaSystem`: Anesthesia system
- `InjectionSystem`: Injection system
- `Micromanipulator`: Micromanipulator
- `Microscope`: Microscope
- `StereotaxicFrame`: Stereotaxic frame
- `SurgicalPowerTool`: Surgical power tool
- `PerfusionSystem`: Perfusion system

### Miscellaneous
- `BiosafetyCabinet`: Biosafety cabinet
- `Computer`: Computer
- `ElectronicComponent`: Electronic component
- `FumeHood`: Fume hood
- `GlassMicropipettePuller`: Glass micropipette puller
- `Microcontroller`: Microcontroller (e.g. Arduino)
- `Monitor`: Monitor
- `SingleBoardComputer`: Single-board computer (e.g. Raspberry Pi)


### Coordinates system options
These are the available `coordinates_system` options for Equipment:

- `External_XYZ_Absolute`: External XYZ Coordinates with Angles

A detailed list of the accepted schemas for the `coordinates_details` field, related to each `coordinates_system`, can be found in the [Coordinates schemas page]({{"api/schemas/coordinates/"|absolute_url}}).


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/equipment
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('equipment')
```

### Response example
{: .no_toc}

```
{'equipment': [
    {
        'id': 'f79d84c8-6bec-40e3-b18a-5b25e57f4a09',
        'type': 'TetrodeWireElectrode',
        'notes': 'First implant',
        'setup': '0f87c229-6769-4854-83a5-c71e154246b8',
        'date_time': None,
        'consumable': 'a5f29099-2758-4163-a8e4-e5e2898e57b2',
        'hardwaredevice': None,
        'details': {
            'tetrodeCount': 1,
            'nWiresTetrode': 4,
            'wireDiameter': 33.9,
            'wireMaterial': 'tunsgten'
        },
        'coordinates_system': 'External_XYZ_Absolute',
        'coordinates_details': {
            'apCoordinate': 1.0
        }
    },
    {
        'id': 'a18dd2b1-6393-468c-9424-1bc77b9e4976',
        'type': 'TetrodeWireElectrode',
        'notes': 'Second implant',
        'setup': '0f87c229-6769-4854-83a5-c71e154246b8',
        'date_time': None,
        'consumable': None,
        'hardwaredevice': None,
        'details': {
            'tetrodeCount': 1,
            'nWiresTetrode': 4,
            'wireDiameter': 33.9,
            'wireMaterial': 'tunsgten'
        },
        'coordinates_system': 'External_XYZ_Absolute',
        'coordinates_details': {
            'x': 1.0,
            'y': 0.0,
            'xAngle': 2.0
        }
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/modules/equipment
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("equipment",  data={
    "type": "OpticFiberImplant",
    "setup": "0f87c229-6769-4854-83a5-c71e154246b8",
    "notes": "some text",
    "details": {"fiberTipShape": "flat"},
    "coordinates_system": "External_XYZ_Absolute",
    "coordinates_details": {
                "x": 1.0,
                "y": 2.0,
                "z": 3.0,
                "xAngle": 4.0,
                "yAngle": 5.0,
                "zAngle": 6.0
            }
    }
)
```

### Response example
{: .no_toc}

```
{'equipment': {
    'id': 'd37c9255-d5ae-47d9-b6e1-4ec760c200fb',
    'type': 'OpticFiberImplant',
    'notes': 'some text',
    'setup': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'consumable': None,
    'hardwaredevice': None,
    'details': {'fiberTipShape': 'flat'},
    'coordinates_system': 'External_XYZ_Absolute',
    'coordinates_details': {
                "x": 1.0,
                "y": 2.0,
                "z": 3.0,
                "xAngle": 4.0,
                "yAngle": 5.0,
                "zAngle": 6.0
            }
    }
}
```


## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/equipment/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('equipment', id='d37c9255-d5ae-47d9-b6e1-4ec760c200fb')
```

### Response example
{: .no_toc}

```
{'equipment': {
    'id': 'd37c9255-d5ae-47d9-b6e1-4ec760c200fb',
    'type': 'OpticFiberImplant',
    'notes': 'some text',
    'setup': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'consumable': None,
    'hardwaredevice': None,
    'details': {'fiberTipShape': 'flat'},
    'coordinates_system': 'External_XYZ_Absolute',
    'coordinates_details': : {
                "x": 1.0,
                "y": 2.0,
                "z": 3.0,
                "xAngle": 4.0,
                "yAngle": 5.0,
                "zAngle": 6.0
            }
    }
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/equipment/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("equipment", id="d37c9255-d5ae-47d9-b6e1-4ec760c200fb", data={"notes": "new text"})
```

### Response example
{: .no_toc}

```
{'equipment': {
    'id': 'd37c9255-d5ae-47d9-b6e1-4ec760c200fb',
    'type': 'OpticFiberImplant',
    'notes': 'new text',
    'setup': '0f87c229-6769-4854-83a5-c71e154246b8',
    'date_time': None,
    'consumable': None,
    'hardwaredevice': None,
    'details': {'fiberTipShape': 'flat'},
    'coordinates_system': 'External_XYZ_Absolute',
    'coordinates_details': : {
                "x": 1.0,
                "y": 2.0,
                "z": 3.0,
                "xAngle": 4.0,
                "yAngle": 5.0,
                "zAngle": 6.0
            }
    }
}
```

## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/modules/equipment/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("equipment", id="d37c9255-d5ae-47d9-b6e1-4ec760c200fb")
```