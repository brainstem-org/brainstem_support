---
layout: default
title: Coordinates systems
parent: Schemas
grand_parent: Data model
nav_order: 1
---

# Coordinates systems
{: .no_toc}

Several coordinate systems are available for flexibly describing targets of procedures and locations.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## External XYZ Coordinates with Angles

A three-dimensional Cartesian coordinate system using absolute positions relative to an external reference point. It includes specific coordinates (X, Y, Z) and angles (X angle, Y angle, Z angle) to describe orientation and position in space, making it ideal for precise, global positioning tasks in research and clinical settings.

| Field  | Description |
|:-------|-------------|
| `X coordinate (m)` | Absolute X coordinate in meters, representing horizontal positioning along a local reference frame. |
| `Y coordinate (m)` | Absolute Y coordinate in meters, representing vertical positioning along a local reference frame. |
| `Z coordinate (m)` | Absolute Z coordinate in meters,representing height. |
| `X angle (degrees)` | Rotational angle around the X axis, in degrees, indicating tilt or elevation relative to the horizontal plane. |
| `Y angle (degrees)` | Rotational angle around the Y axis, in degrees, indicating roll or sideways tilt relative to the vertical axis. |
| `Z angle (degrees)` | Rotational angle around the Z axis, in degrees, indicating azimuth or orientation facing around the vertical axis. |

## Stereotaxic Bregma-Based Absolute Coordinates

Utilizes the Bregma point as a primary reference for absolute positioning within the skull. This system includes anteroposterior (AP), mediolateral (ML), and dorsoventral (DV) coordinates, along with their corresponding angles, enabling precise targeting and measurement from the Bregma landmark.
 
| Field  | Description |
|:-------|-------------|
| `AP coordinate (mm)` | Absolute Anterior-Posterior coordinate from a fixed point, in millimeters. |
| `ML coordinate (mm)` | Absolute Medial-Lateral coordinate from a fixed point, in millimeters. |
| `DV coordinate (mm)` | Dorsal-Ventral coordinate from a reference point, typically the brain surface, in millimeters. |
| `AP angle (degrees)` | Angle of the device or probe in the Anterior-Posterior direction, in degrees. |
| `ML angle (degrees)` | Angle of the device or probe in the Medial-Lateral direction, in degrees. |
| `DV angle (degrees)` | Angle of the device or probe in the Dorsal-Ventral direction, in degrees. |

## Stereotaxic Bregma-Based Surface Coordinates with Depth

Measures coordinates from the surface of the brain at the Bregma point, incorporating depth and rotation adjustments. This system is particularly useful for applications where interventions or measurements need to accommodate the curvature of the brain's surface.

| Field  | Description |
|:-------|-------------|
| `AP coordinate (mm)` | Anterior-Posterior coordinate relative to Bregma, in millimeters. |
| `ML coordinate (mm)` | Medial-Lateral coordinate relative to Bregma, in millimeters. |
| `Depth (mm)` | Depth of the implant in the brain, measured from the surface, in millimeters. |
| `Rotation (degrees)` | Angle adjustment in the Anterior-Posterior direction, in degrees |
| `AP angle (degrees)` | Angle adjustment in the Medial-Lateral direction, in degrees. |
| `ML angle (degrees)` | Rotation of the implant around the insertion axis, in degrees. |

## Stereotaxic Lambda-Based Absolute Coordinates

Anchors measurements to the Lambda, a secondary cranial landmark, providing a set of absolute coordinates. Like the Bregma system, it includes AP, ML, and DV coordinates and their angles, offering an alternative reference point for varied experimental setups.

| Field  | Description |
|:-------|-------------|
| `AP coordinate (mm)` | Anterior-Posterior coordinate measured from Lambda, in millimeters. Lambda serves as a posterior reference point on the skull in rodent brain mappings. |
| `ML coordinate (mm)` | Medial-Lateral coordinate measured from the central line crossing Lambda, in millimeters. Used for precise lateral positioning of instruments. |
| `DV coordinate (mm)` | Dorsal-Ventral coordinate measured from the skull's surface at Lambda, in millimeters. Indicates depth for vertical placement of instruments. |
| `AP angle (degrees)` | Tilting angle in the Anterior-Posterior axis from Lambda, in degrees. Used to adjust the probe or electrode's approach angle relative to the skull. |
| `ML angle (degrees)` | Tilting angle in the Medial-Lateral direction from Lambda, in degrees. Adjusts for lateral tilt relative to the skull's central line. |
| `DV angle (degrees)` | Angular adjustment in the Dorsal-Ventral plane from Lambda, in degrees. Used to orient instruments vertically. |

## Stereotaxic Lambda-Based Surface Coordinates with Depth

Similar to the Bregma brain surface system, but using Lambda as the reference. It includes coordinates adjusted to the brain's surface at Lambda, depth, and rotation, useful for targeting specific areas near the occipital part of the brain.

| Field  | Description |
|:-------|-------------|
| `AP coordinate (mm)` | Anterior-Posterior coordinate measured from the Lambda landmark, in millimeters. Lambda is used as a reference point at the posterior aspect of the skull. |
| `ML coordinate (mm)` | Medial-Lateral coordinate measured from the midline crossing Lambda, in millimeters. This measurement helps in positioning equipment laterally across the brain's hemisphere. |
| `Depth (mm)` | Vertical depth measured from the surface at the Lambda reference point, in millimeters. Indicates how deep into the brain tissue the instrument penetrates. |
| `Rotation (degrees)` | Angle of tilt in the Anterior-Posterior direction from the Lambda reference point, in degrees, used to align the probe or electrode with respect to the brain's longitudinal axis. |
| `AP angle (degrees)` | Medial-Lateral tilting angle from Lambda, in degrees, adjusting the lateral orientation of devices or surgical tools. |
| `ML angle (degrees)` | Rotation around the vertical axis through Lambda, in degrees. This controls the azimuthal orientation of the probe or surgical tool. |

## Stereotaxic XYZ Absolute Coordinates

A comprehensive three-dimensional coordinate system based on stereotaxic principles, using X, Y, and Z coordinates along with their corresponding angles. This system allows for precise navigation and localization within a stereotaxic frame, supporting complex brain mapping and intervention tasks.

| Field  | Description |
|:-------|-------------|
| `X coordinate (mm)` | X coordinate in millimeters, representing the position along the left-right axis relative to a standardized reference point. |
| `Y coordinate (mm)` | Y coordinate in millimeters, indicating the anterior-posterior position from a fixed reference point in the setup. |
| `Z coordinate (mm)` | Z coordinate in millimeters, representing the depth or vertical position relative to a surface or base level. |
| `X angle (degrees)` | Rotational angle about the X-axis, in degrees, adjusting the tilt of the instrument or probe horizontally. |
| `Y angle (degrees)` | Rotational angle about the Y-axis, in degrees, used to orient the probe or device in the anterior-posterior plane. |
| `Z angle (degrees)` | Rotational angle about the Z-axis, in degrees, adjusting the azimuth or directional facing of the setup |

## Stereotaxic Surface XY Surface Coordinates with Depth

Focuses on two-dimensional positioning on the brain's surface, using X and Y coordinates and their angles. It also includes depth and rotation measurements, suitable for experiments requiring lateral and anteroposterior precision without full three-dimensional depth.

| Field  | Description |
|:-------|-------------|
| `X coordinate (mm)` | X coordinate in millimeters, measuring horizontal position across the surface from a fixed central or reference point. |
| `Y coordinate (mm)` | Y coordinate in millimeters, measuring vertical position along the surface from a fixed central or reference point. |
| `X angle (degrees)` | Angle of tilt around the X-axis, in degrees, indicating the inclination or elevation relative to the flat surface. |
| `Y angle (degrees)` | Angle of tilt around the Y-axis, in degrees, indicating the lateral tilt relative to the central axis of the surface. |
| `Depth (mm)` | Depth in millimeters, measuring the perpendicular distance below the surface plane, used for setting the penetration depth of an instrument. |
| `Rotation (degrees)` | Rotation around the vertical axis through the point of interest, in degrees, used to adjust the orientation of the instrument or device. |

## Coordinates API access
The API allows for programmable access to Coordinates, enabling you to read, edit, and delete coordinates through the API. Learn more about the coordinates' fields and data structure on the [Coordinates API page]({{"api/modules/coordinates/"|absolute_url}}).
