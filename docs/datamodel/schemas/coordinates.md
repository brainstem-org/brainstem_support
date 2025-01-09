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
| `X coordinate (m)` | Absolute X coordinate in meters, representing horizontal positioning along a local reference frame (float) |
| `Y coordinate (m)` | Absolute Y coordinate in meters, representing vertical positioning along a local reference frame (float) |
| `Z coordinate (m)` | Absolute Z coordinate in meters, representing height (float) |
| `X angle (degrees)` | Rotational angle around the X axis, indicating tilt or elevation relative to the horizontal plane (float; range: -180° to 360°) |
| `Y angle (degrees)` | Rotational angle around the Y axis, indicating roll or sideways tilt relative to the vertical axis (float; range: -180° to 360°) |
| `Z angle (degrees)` | Rotational angle around the Z axis, indicating azimuth or orientation facing around the vertical axis (float; range: -180° to 360°) |

## Stereotaxic Bregma-Based Absolute Coordinates

Utilizes the Bregma point as a primary reference for absolute positioning within the skull. This system includes anteroposterior (AP), mediolateral (ML), and dorsoventral (DV) coordinates, along with their corresponding angles, enabling precise targeting and measurement from the Bregma landmark.
 
| Field  | Description |
|:-------|-------------|
| `AP coordinate (mm)` | Absolute Anterior-Posterior coordinate from a fixed point, in millimeters (float) |
| `ML coordinate (mm)` | Absolute Medial-Lateral coordinate from a fixed point, in millimeters (float) |
| `DV coordinate (mm)` | Dorsal-Ventral coordinate from a reference point, typically the brain surface, in millimeters (float) |
| `AP angle (degrees)` | Angle of the device or probe in the Anterior-Posterior direction (float; range: -180° to 360°) |
| `ML angle (degrees)` | Angle of the device or probe in the Medial-Lateral direction (float; range: -180° to 360°) |
| `DV angle (degrees)` | Angle of the device or probe in the Dorsal-Ventral direction (float; range: -180° to 360°) |

## Stereotaxic Bregma-Based Surface Coordinates with Depth

Measures coordinates from the surface of the brain at the Bregma point, incorporating depth and rotation adjustments. This system is particularly useful for applications where interventions or measurements need to accommodate the curvature of the brain's surface.

| Field  | Description |
|:-------|-------------|
| `AP coordinate (mm)` | Anterior-Posterior coordinate relative to Bregma, in millimeters (float) |
| `ML coordinate (mm)` | Medial-Lateral coordinate relative to Bregma, in millimeters (float) |
| `Depth (mm)` | Depth of the implant in the brain, measured from the surface (float) |
| `Rotation (degrees)` | Rotation of the implant around the insertion axis (float; range: -180° to 360°) |
| `AP angle (degrees)` | Angle adjustment in the Anterior-Posterior direction (float; range: -180° to 360°) |
| `ML angle (degrees)` | Angle adjustment in the Medial-Lateral direction (float; range: -180° to 360°) |

## Stereotaxic Lambda-Based Absolute Coordinates

Anchors measurements to the Lambda, a secondary cranial landmark, providing a set of absolute coordinates. Like the Bregma system, it includes AP, ML, and DV coordinates and their angles, offering an alternative reference point for varied experimental setups.

| Field  | Description |
|:-------|-------------|
| `AP coordinate (mm)` | Anterior-Posterior coordinate measured from Lambda (float). Lambda serves as a posterior reference point on the skull in rodent brain mappings. |
| `ML coordinate (mm)` | Medial-Lateral coordinate measured from the central line crossing Lambda (float). Used for precise lateral positioning of instruments. |
| `DV coordinate (mm)` | Dorsal-Ventral coordinate measured from the skull's surface at Lambda (float). Indicates depth for vertical placement of instruments. |
| `AP angle (degrees)` | Tilting angle in the Anterior-Posterior axis from Lambda (float; range: -180° to 360°). Used to adjust the probe or electrode's approach angle relative to the skull. |
| `ML angle (degrees)` | Tilting angle in the Medial-Lateral direction from Lambda (float; range: -180° to 360°). Adjusts for lateral tilt relative to the skull's central line. |
| `DV angle (degrees)` | Angular adjustment in the Dorsal-Ventral plane from Lambda (float; range: -180° to 360°). Used to orient instruments vertically. |

## Stereotaxic Lambda-Based Surface Coordinates with Depth

Similar to the Bregma brain surface system, but using Lambda as the reference. It includes coordinates adjusted to the brain's surface at Lambda, depth, and rotation, useful for targeting specific areas near the occipital part of the brain.

| Field  | Description |
|:-------|-------------|
| `AP coordinate (mm)` | Anterior-Posterior coordinate measured from the Lambda landmark (float). Lambda is used as a reference point at the posterior aspect of the skull. |
| `ML coordinate (mm)` | Medial-Lateral coordinate measured from the midline crossing Lambda (float). This measurement helps in positioning equipment laterally across the brain's hemisphere. |
| `Depth (mm)` | Vertical depth measured from the surface at the Lambda reference point (float). Indicates how deep into the brain tissue the instrument penetrates. |
| `Rotation (degrees)` | Rotation around the vertical axis through Lambda (float; range: -180° to 360°). This controls the azimuthal orientation of the probe or surgical tool. |
| `AP angle (degrees)` | Medial-Lateral tilting angle from Lambda (float; range: -180° to 360°). Used to adjust the lateral orientation of devices or surgical tools. |
| `ML angle (degrees)` | Rotation around the vertical axis through Lambda (float; range: -180° to 360°). Used to adjust the orientation of the instrument or device. |

## Stereotaxic XYZ Absolute Coordinates

A comprehensive three-dimensional coordinate system based on stereotaxic principles, using X, Y, and Z coordinates along with their corresponding angles. This system allows for precise navigation and localization within a stereotaxic frame, supporting complex brain mapping and intervention tasks.

| Field  | Description |
|:-------|-------------|
| `X coordinate (mm)` | Position along the left-right axis relative to a standardized reference point (float) |
| `Y coordinate (mm)` | Anterior-posterior position from a fixed reference point in the setup (float) |
| `Z coordinate (mm)` | Depth or vertical position relative to a surface or base level (float) |
| `X angle (degrees)` | Rotational angle about the X-axis (float; range: -180° to 360°). Adjusts the tilt of the instrument horizontally. |
| `Y angle (degrees)` | Rotational angle about the Y-axis (float; range: -180° to 360°). Used to orient the device in the anterior-posterior plane. |
| `Z angle (degrees)` | Rotational angle about the Z-axis (float; range: -180° to 360°). Adjusts the azimuth or directional facing of the setup. |

## Stereotaxic Surface XY Surface Coordinates with Depth

Focuses on two-dimensional positioning on the brain's surface, using X and Y coordinates and their angles. It also includes depth and rotation measurements, suitable for experiments requiring lateral and anteroposterior precision without full three-dimensional depth.

| Field  | Description |
|:-------|-------------|
| `X coordinate (mm)` | Horizontal position across the surface from a fixed central point (float) |
| `Y coordinate (mm)` | Vertical position along the surface from a fixed central point (float) |
| `X angle (degrees)` | Angle of tilt around the X-axis (float; range: -180° to 360°). Indicates inclination relative to the flat surface. |
| `Y angle (degrees)` | Angle of tilt around the Y-axis (float; range: -180° to 360°). Indicates lateral tilt relative to the central axis. |
| `Depth (mm)` | Perpendicular distance below the surface plane (float). Used for setting penetration depth. |
| `Rotation (degrees)` | Rotation around the vertical axis through the point of interest (float; range: -180° to 360°). Used for device orientation. |

## API access
The API allows for programmable access to Coordinates, enabling you to read, edit, and delete coordinates through the API. Learn more about the coordinates' fields and data structure on the [Coordinates API page]({{"api/schemas/coordinates/"|absolute_url}}).