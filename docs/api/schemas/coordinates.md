---
layout: default
title: Coordinates
parent: Schemas
grand_parent: API
nav_order: 1
---

# Coordinates systems schemas
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## CCF_XYZ_Absolute
```
{
    "type": "object",
    "title": "Common Coordinate Framework XYZ Absolute Coordinates",
    "options": {
        "compact": true
    },
    "additionalProperties": false,
    "properties": {
        "x": {
            "title": "X coordinate (mm)",
            "brief": "X",
            "units": "mm",
            "type": "number",
            "options": {
                "infoText": "X coordinate in millimeters, representing the position along the left-right axis relative to a standardized reference point."
            }
        },
        "xAngle": {
            "title": "X angle (\u00b0)",
            "brief": "X angle",
            "units": "\u00b0",
            "type": "number",
            "minimum": -180,
            "maximum": 360,
            "options": {
                "infoText": "Rotational angle about the X-axis, in degrees, adjusting the tilt of the instrument or probe horizontally."
            }
        },
        "y": {
            "title": "Y coordinate (mm)",
            "brief": "Y",
            "units": "mm",
            "type": "number",
            "options": {
                "infoText": "Y coordinate in millimeters, indicating the anterior-posterior position from a fixed reference point in the setup."
            }
        },
        "yAngle": {
            "title": "Y angle (\u00b0)",
            "brief": "Y angle",
            "units": "\u00b0",
            "type": "number",
            "minimum": -180,
            "maximum": 360,
            "options": {
                "infoText": "Rotational angle about the Y-axis, in degrees, used to orient the probe or device in the anterior-posterior plane."
            }
        },
        "z": {
            "title": "Z coordinate (mm)",
            "brief": "Z",
            "units": "mm",
            "type": "number",
            "options": {
                "infoText": "Z coordinate in millimeters, representing the depth or vertical position relative to a surface or base level."
            }
        },
        "zAngle": {
            "title": "Z angle (\u00b0)",
            "brief": "Z angle",
            "units": "\u00b0",
            "type": "number",
            "minimum": -180,
            "maximum": 360,
            "options": {
                "infoText": "Rotational angle about the Z-axis, in degrees, adjusting the azimuth or directional facing of the setup."
            }
        }
    }
}
```

## External_XYZ_Absolute
```
{
    "type": "object",
    "title": "External XYZ Coordinates with Angles",
    "options": {
        "compact": true
    },
    "additionalProperties": false,
    "properties": {
        "x": {
            "title": "X coordinate (m)",
            "brief": "X",
            "units": "m",
            "type": "number",
            "options": {
                "infoText": "Absolute X coordinate in meters, representing horizontal positioning along a local reference frame."
            }
        },
        "xAngle": {
            "title": "X angle (\u00b0)",
            "brief": "X angle",
            "units": "\u00b0",
            "type": "number",
            "minimum": -180,
            "maximum": 360,
            "options": {
                "infoText": "Rotational angle around the X axis, in degrees, indicating tilt or elevation relative to the horizontal plane."
            }
        },
        "y": {
            "title": "Y coordinate (m)",
            "brief": "Y",
            "units": "m",
            "type": "number",
            "options": {
                "infoText": "Absolute Y coordinate in meters, representing vertical positioning along a local reference frame."
            }
        },
        "yAngle": {
            "title": "Y angle (\u00b0)",
            "brief": "Y angle",
            "units": "\u00b0",
            "type": "number",
            "minimum": -180,
            "maximum": 360,
            "options": {
                "infoText": "Rotational angle around the Y axis, in degrees, indicating roll or sideways tilt relative to the vertical axis."
            }
        },
        "z": {
            "title": "Z coordinate (m)",
            "brief": "Z",
            "units": "m",
            "type": "number",
            "options": {
                "infoText": "Absolute Z coordinate in meters,representing height."
            }
        },
        "zAngle": {
            "title": "Z angle (\u00b0)",
            "brief": "Z angle",
            "units": "\u00b0",
            "type": "number",
            "minimum": -180,
            "maximum": 360,
            "options": {
                "infoText": "Rotational angle around the Z axis, in degrees, indicating azimuth or orientation facing around the vertical axis."
            }
        }
    }
}
```

## Stereotaxic_BregmaAbsolute
```
{
    "type": "object",
    "title": "Stereotaxic Bregma-Based Absolute Coordinates",
    "options": {
        "compact": true
    },
    "additionalProperties": false,
    "properties": {
        "apCoordinate": {
            "title": "AP coordinate (mm)",
            "brief": "AP",
            "units": "mm",
            "type": "number",
            "options": {
                "infoText": "Absolute Anterior-Posterior coordinate from a fixed point, in millimeters."
            }
        },
        "apAngle": {
            "title": "AP angle (\u00b0)",
            "brief": "AP angle",
            "units": "\u00b0",
            "type": "number",
            "minimum": -180,
            "maximum": 360,
            "options": {
                "infoText": "Angle of the device or probe in the Anterior-Posterior direction, in degrees."
            }
        },
        "mlCoordinate": {
            "title": "ML coordinate (mm)",
            "brief": "ML",
            "units": "mm",
            "type": "number",
            "options": {
                "infoText": "Absolute Medial-Lateral coordinate from a fixed point, in millimeters."
            }
        },
        "mlAngle": {
            "title": "ML angle (\u00b0)",
            "brief": "ML angle",
            "units": "\u00b0",
            "type": "number",
            "minimum": -180,
            "maximum": 360,
            "options": {
                "infoText": "Angle of the device or probe in the Medial-Lateral direction, in degrees."
            }
        },
        "dvCoordinate": {
            "title": "DV coordinate (mm)",
            "brief": "DV",
            "units": "mm",
            "type": "number",
            "options": {
                "infoText": "Dorsal-Ventral coordinate from a reference point, typically the brain surface, in millimeters."
            }
        },
        "dvAngle": {
            "title": "DV angle (\u00b0)",
            "brief": "DV angle",
            "units": "\u00b0",
            "type": "number",
            "minimum": -180,
            "maximum": 360,
            "options": {
                "infoText": "Angle of the device or probe in the Dorsal-Ventral direction, in degrees."
            }
        }
    }
}
```

## Stereotaxic_BregmaBrainSurface
```
{
    "type": "object",
    "title": "Stereotaxic Bregma-Based Surface Coordinates with Depth",
    "options": {
        "compact": true
    },
    "additionalProperties": false,
    "properties": {
        "apCoordinate": {
            "title": "AP coordinate (mm)",
            "brief": "AP",
            "units": "mm",
            "type": "number",
            "options": {
                "infoText": "Anterior-Posterior coordinate relative to Bregma, in millimeters."
            }
        },
        "apAngle": {
            "title": "AP angle (\u00b0)",
            "brief": "AP angle",
            "units": "\u00b0",
            "type": "number",
            "minimum": -180,
            "maximum": 360,
            "options": {
                "infoText": "Angle adjustment in the Anterior-Posterior direction, in degrees."
            }
        },
        "mlCoordinate": {
            "title": "ML coordinate (mm)",
            "brief": "ML",
            "units": "mm",
            "type": "number",
            "options": {
                "infoText": "Medial-Lateral coordinate relative to Bregma, in millimeters."
            }
        },
        "mlAngle": {
            "title": "ML angle (\u00b0)",
            "brief": "ML angle",
            "units": "\u00b0",
            "type": "number",
            "minimum": -180,
            "maximum": 360,
            "options": {
                "infoText": "Angle adjustment in the Medial-Lateral direction, in degrees."
            }
        },
        "depth": {
            "title": "Depth (mm)",
            "brief": "depth",
            "units": "mm",
            "type": "number",
            "options": {
                "infoText": "Depth of the implant in the brain, measured from the surface, in millimeters."
            }
        },
        "rotation": {
            "title": "Rotation (\u00b0)",
            "brief": "rotation",
            "units": "\u00b0",
            "type": "number",
            "minimum": -180,
            "maximum": 360,
            "options": {
                "infoText": "Rotation of the implant around the insertion axis, in degrees."
            }
        }
    }
}
```

## Stereotaxic_LambdaAbsolute
```
{
    "type": "object",
    "title": "Stereotaxic Lambda-Based Absolute Coordinates",
    "options": {
        "compact": true
    },
    "additionalProperties": false,
    "properties": {
        "apCoordinate": {
            "title": "AP coordinate (mm)",
            "brief": "AP",
            "units": "mm",
            "type": "number",
            "options": {
                "infoText": "Anterior-Posterior coordinate measured from Lambda, in millimeters. Lambda serves as a posterior reference point on the skull in rodent brain mappings."
            }
        },
        "apAngle": {
            "title": "AP angle (\u00b0)",
            "brief": "AP angle",
            "units": "\u00b0",
            "type": "number",
            "minimum": -180,
            "maximum": 360,
            "options": {
                "infoText": "Tilting angle in the Anterior-Posterior axis from Lambda, in degrees. Used to adjust the probe or electrode's approach angle relative to the skull."
            }
        },
        "mlCoordinate": {
            "title": "ML coordinate (mm)",
            "brief": "ML",
            "units": "mm",
            "type": "number",
            "options": {
                "infoText": "Medial-Lateral coordinate measured from the central line crossing Lambda, in millimeters. Used for precise lateral positioning of instruments."
            }
        },
        "mlAngle": {
            "title": "ML angle (\u00b0)",
            "brief": "ML angle",
            "units": "\u00b0",
            "type": "number",
            "minimum": -180,
            "maximum": 360,
            "options": {
                "infoText": "Tilting angle in the Medial-Lateral direction from Lambda, in degrees. Adjusts for lateral tilt relative to the skull's central line."
            }
        },
        "dvCoordinate": {
            "title": "DV coordinate (mm)",
            "brief": "DV",
            "units": "mm",
            "type": "number",
            "options": {
                "infoText": "Dorsal-Ventral coordinate measured from the skull's surface at Lambda, in millimeters. Indicates depth for vertical placement of instruments."
            }
        },
        "dvAngle": {
            "title": "DV angle (\u00b0)",
            "brief": "DV angle",
            "units": "\u00b0",
            "type": "number",
            "minimum": -180,
            "maximum": 360,
            "options": {
                "infoText": "Angular adjustment in the Dorsal-Ventral plane from Lambda, in degrees. Used to orient instruments vertically."
            }
        }
    }
}
```

## Stereotaxic_LambdaBrainSurface
```
{
    "type": "object",
    "title": "Stereotaxic Lambda-Based Surface Coordinates with Depth",
    "options": {
        "compact": true
    },
    "additionalProperties": false,
    "properties": {
        "apCoordinate": {
            "title": "AP coordinate (mm)",
            "brief": "AP",
            "units": "mm",
            "type": "number",
            "options": {
                "infoText": "Anterior-Posterior coordinate measured from the Lambda landmark, in millimeters. Lambda is used as a reference point at the posterior aspect of the skull."
            }
        },
        "apAngle": {
            "title": "AP angle (\u00b0)",
            "brief": "AP angle",
            "units": "\u00b0",
            "type": "number",
            "minimum": -180,
            "maximum": 360,
            "options": {
                "infoText": "Angle of tilt in the Anterior-Posterior direction from the Lambda reference point, in degrees, used to align the probe or electrode with respect to the brain's longitudinal axis."
            }
        },
        "mlCoordinate": {
            "title": "ML coordinate (mm)",
            "brief": "ML",
            "units": "mm",
            "type": "number",
            "options": {
                "infoText": "Medial-Lateral coordinate measured from the midline crossing Lambda, in millimeters. This measurement helps in positioning equipment laterally across the brain's hemisphere."
            }
        },
        "mlAngle": {
            "title": "ML angle (\u00b0)",
            "brief": "ML angle",
            "units": "\u00b0",
            "type": "number",
            "minimum": -180,
            "maximum": 360,
            "options": {
                "infoText": "Medial-Lateral tilting angle from Lambda, in degrees, adjusting the lateral orientation of devices or surgical tools."
            }
        },
        "depth": {
            "title": "Depth (mm)",
            "brief": "depth",
            "units": "mm",
            "type": "number",
            "options": {
                "infoText": "Vertical depth measured from the surface at the Lambda reference point, in millimeters. Indicates how deep into the brain tissue the instrument penetrates."
            }
        },
        "rotation": {
            "title": "Rotation (\u00b0)",
            "brief": "rotation",
            "units": "\u00b0",
            "type": "number",
            "minimum": -180,
            "maximum": 360,
            "options": {
                "infoText": "Rotation around the vertical axis through Lambda, in degrees. This controls the azimuthal orientation of the probe or surgical tool."
            }
        }
    }
}
```

