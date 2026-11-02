## Anatomical Reference Points

In neurosurgery or in research, it is important to define coordinates for where in the brain a surgical intervention will take place. These coordinates rely on anatomical markers that are uniform across individuals. There are two major anatomical markers on the dorsal surface of the brain that are formed when the plates of the skull fuse during development, and these markers are used to identify the location of various anatomical structures of the brain.

<img src="/assets/images/coordinates/bregma_and_lambda2.png" width="80%">

**Bregma**: the anatomical point on the skull at which the coronal suture (between frontal and parietal bones) is intersected perpendicularly by the sagittal suture (between left and right parietal bones).

**Lambda**: the meeting point of the sagittal suture (between left and right parietal bones) and the lambdoid suture (between parietal and occipital bones).

{: .note }
Both points serve as standard reference points for stereotaxic coordinates in neuroscience research.

## Stereotaxic Coordinate System Conventions

### Basic Coordinate System

{: .important }
All stereotaxic coordinate systems in BrainSTEM follow a right-handed coordinate system with the following conventions:

<img src="/assets/images/coordinates/coordinates2.png" width="60%">

* **AP (Anterior-Posterior) axis:**
   * Primary reference axis
   * Positive values are anterior to reference point
* **ML (Medial-Lateral) axis:**
   * Following right-hand rule relative to AP axis
   * Positive values are to the right (as seen from behind)
* **DV (Dorsal-Ventral) axis:**
   * Following right-hand rule
   * Positive values are ventral

### Angle Measurement System
By default, angles are defined by three rotations:
        1. The AP angle, rotating clockwise around ML
        2. The ML angle, rotating clockwise around AP
        3. The rotation angle, rotating clockwise around the object's depth axis

{: .warning }
Proper understanding and application of these angles is critical for accurate probe placement and experimental reproducibility.

All stereotaxic measurements use three angles to specify orientation:

**AP angle (Anterior-Posterior rotation):**

<img src="/assets/images/coordinates/AP_angle3.png" width="90%">

   * Measured as rotation from the vertical axis in the sagittal plane
   * 0° represents vertical along DV axis
   * Range: -180° to +180°
   * Positive values indicate anterior rotation
   * Example: +15° indicates probe tiltet 15° anteriorly from vertical

**ML angle (Medial-Lateral rotation):**

<img src="/assets/images/coordinates/ML_angle3.png" width="90%">

   * Measured as rotation from the vertical axis in the coronal plane
   * 0° represents vertical along DV axis
   * Range: -180° to +180°
   * Positive values indicate rightward/clockwise rotation (as seen from behind)
   * Example: +20° indicates probe tiltet 20° to the right from vertical

**Rotation angle (around probe axis):**

<img src="/assets/images/coordinates/rotation3.png" width="45%">

   * 0° when probe features align with the coronal plane
   * Range: -180° to +180° (or 0° to 360°)
   * Positive rotation is clockwise when viewed from above
