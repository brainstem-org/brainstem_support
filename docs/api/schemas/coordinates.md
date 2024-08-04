---
layout: default
title: Coordinates
parent: Schemas
grand_parent: API
nav_order: 1
---

# Coordinates schemas
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## External XYZ absolute
```
{
    "type": "object",
    "title": "External XYZ absolute",
    "properties": {
        "x": {
            "title": "X coordinate (m)",
            "brief": "Y",
            "units": "mm",
            "type": "number"

        },
        "y": {
            "title": "Y coordinate (m)",
            "brief": "Y",
            "units": "mm",
            "type": "number"
        },
        "z": {
            "title": "Z coordinate (m)",
            "brief": "Z",
            "units": "mm",
            "type": "number"
        },
        "xAngle": {
            "title": "X angle (degrees)",
            "brief": "X angle",
            "units": "degrees",
            "type": "number"
        },
        "yAngle": {
            "title": "Y angle (degrees)",
            "brief": "Y angle",
            "units": "degrees",
            "type": "number"
        },
         "zAngle": {
            "title": "Z angle (degrees)",
            "brief": "Z angle",
            "units": "degrees",
            "type": "number"
        }
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "x": 0,
    "y": 0,
    "z": 1,
    "xAngle": 37,
    "yAngle": 21,
    "zAngle": 23
}
```

## Stereotaxic Bregma absolute
```
{
    "type": "object",
    "title": "Stereotaxic Bregma absolute",
    "properties": {
        "apCoordinate": {
            "title": "AP coordinate (mm)",
            "brief": "AP",
            "type": "number"
        },
        "mlCoordinate": {
            "title": "ML coordinate (mm)",
            "brief": "ML",
            "type": "number"
        },
        "dvCoordinate": {
            "title": "DV coordinate (mm)",
            "brief": "DV",
            "type": "number"
        },
        "apAngle": {
            "title": "AP angle (degrees)",
            "brief": "AP angle",
            "type": "number"
        },
        "mlAngle": {
            "title": "ML angle (degrees)",
            "brief": "ML angle",
            "type": "number"
        },
        "dvAngle": {
            "title": "DV angle (degrees)",
            "brief": "DV angle",
            "type": "number"
        }
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "apCoordinate": 4.7,
    "mlCoordinate": 4,
    "dvCoordinate": 23.2,
    "apAngle": 5,
    "mlAngle": 5,
    "dvAngle": 0
}
```

## Stereotaxic Bregma brain surface
```
{
    "type": "object",
    "title": "Stereotaxic Bregma brain surface",
    "properties": {
        "apCoordinate": {
            "title": "AP coordinate (mm)",
            "brief": "AP",
            "type": "number"
        },
        "mlCoordinate": {
            "title": "ML coordinate (mm)",
            "brief": "ML",
            "type": "number"
        },
        "depth": {
            "title": "Depth (mm)",
            "brief": "Depth",
            "type": "number"
        },
        "rotation": {
            "title": "Rotation (degrees)",
            "brief": "Rotation",
            "type": "number"
        },
        "apAngle": {
            "title": "AP angle (degrees)",
            "brief": "AP angle",
            "type": "number"
        },
        "mlAngle": {
            "title": "ML angle (degrees)",
            "brief": "ML angle",
            "type": "number"
        }
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "apCoordinate": 0.4,
    "mlCoordinate": 1.1,
    "depth": 12,
    "rotation": 0,
    "apAngle": 15,
    "mlAngle": 15
}
```

## Stereotaxic Lambda absolute
```
{
    "type": "object",
    "title": "Stereotaxic Lambda absolute",
    "properties": {
        "apCoordinate": {
            "title": "AP coordinate (mm)",
            "brief": "AP",
            "type": "number"
        },
        "mlCoordinate": {
            "title": "ML coordinate (mm)",
            "brief": "ML",
            "type": "number"
        },
        "dvCoordinate": {
            "title": "DV coordinate (mm)",
            "brief": "DV",
            "type": "number"
        },
        "apAngle": {
            "title": "AP angle (degrees)",
            "brief": "AP angle",
            "type": "number"
        },
        "mlAngle": {
            "title": "ML angle (degrees)",
            "brief": "ML angle",
            "type": "number"
        },
        "dvAngle": {
            "title": "DV angle (degrees)",
            "brief": "CV angle",
            "type": "number"
        }
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "apCoordinate": 4.7,
    "mlCoordinate": 4,
    "dvCoordinate": 23.2,
    "apAngle": 5,
    "mlAngle": 5,
    "dvAngle": 0
}
```

## Stereotaxic Lambda brain surface
```
{
    "type": "object",
    "title": "Stereotaxic Lambda brain surface",
    "properties": {
        "apCoordinate": {
            "title": "AP coordinate (mm)",
            "brief": "AP",
            "type": "number" 
        },
        "mlCoordinate": {
            "title": "ML coordinate (mm)",
            "brief": "ML",
            "type": "number"
        },
        "depth": {
            "title": "Depth (mm)",
            "brief": "Depth",
            "type": "number"
        },
        "rotation": {
            "title": "Rotation (degrees)",
            "brief": "Rotation",
            "type": "number"
        },
        "apAngle": {
            "title": "AP angle (degrees)",
            "brief": "AP angle",
            "type": "number"
        },
        "mlAngle": {
            "title": "ML angle (degrees)",
            "brief": "ML angle",
            "type": "number"
        }
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "apCoordinate": 0.4,
    "mlCoordinate": 1.1,
    "depth": 12,
    "rotation": 0,
    "apAngle": 15,
    "mlAngle": 15
}
```

## Stereotaxic XY surface
```
{
    "type": "object",
    "title": "Stereotaxic XY surface",
    "properties": {
        "x": {
            "title": "X coordinate (mm)",
            "brief": "X",
            "type": "number"
        },
        "y": {
            "title": "Y coordinate (mm)",
            "brief": "Y",
            "type": "number"
        },
        "xAngle": {
            "title": "X angle (degrees)",
            "brief": "X angle",
            "type": "number"
        },
        "yAngle": {
            "title": "Y angle (degrees)",
            "brief": "Y angle",
            "type": "number"
        },
        "depth": {
            "title": "Depth (mm)",
            "brief": "Depth",
            "type": "number"
        },
        "rotation": {
            "title": "Rotation (degrees)",
            "brief": "Rotation",
            "type": "number"
        }
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "x": 0, 
    "y": 4, 
    "xAngle": 30, 
    "yAngle": 15, 
    "depth": 0.1, 
    "rotation": 10
}
```

## Stereotaxic XYZ absolute
```
{
    "type": "object",
    "title": "Stereotaxic XYZ absolute",
    "properties": {
        "x": {
            "title": "X coordinate (mm)",
            "brief": "X",
            "type": "number"
        },
        "y": {
            "title": "Y coordinate (mm)",
            "brief": "Y",
            "type": "number"
        },
        "z": {
            "title": "Z coordinate (mm)",
            "brief": "Z",
            "type": "number"
        },
        "xAngle": {
            "title": "X angle (degrees)",
            "brief": "X angle",
            "type": "number"
        },
        "yAngle": {
            "title": "Y angle (degrees)",
            "brief": "Y angle",
            "type": "number"
        },
         "zAngle": {
            "title": "Z angle (degrees)",
            "brief": "Z angle",
            "type": "number"
        }
    }
}
```

### Example of JSON according to this schema
{: .no_toc}
```
{
    "x": 0,
    "y": 0,
    "z": 1,
    "xAngle": 37,
    "yAngle": 21,
    "zAngle": 23
}
```