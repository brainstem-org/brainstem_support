---
layout: default
title: 2P Imaging Workflow
parent: Tutorials
nav_order: 10
---

# Draft: Two-Photon Workflow: Visual Cortex Population Dynamics
{: .no_toc}

## Introduction - Note: this tutorial is still in a drafting state

This comprehensive tutorial walks through a complete two-photon calcium imaging experiment in BrainSTEM, from subject preparation to data analysis. We'll document a visual cortex population dynamics study with head-fixed mice, demonstrating how to integrate subjects, procedures, behavioral paradigms, data acquisition, manipulations, and collections in a realistic research workflow.

**Experimental Design Overview:**
- **Subjects**: Mouse cohort for visual cortex population imaging
- **Setup**: Head-fixed two-photon microscope with visual stimulus presentation
- **Sessions**: Cranial window surgery → Habituation → Visual stimulus sessions
- **Data**: Two-photon calcium imaging, visual stimuli, eye tracking
- **Analysis**: Population dynamics, stimulus response, retinotopy mapping

{: .note }
> This tutorial assumes you have already set up your lab infrastructure (setups, equipment, inventories) as described in the [Setting Up Lab Infrastructure tutorial]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure).

## Part A: Project and Subject Setup

### Step 1: Creating the Research Project

First, we'll create a project to organize our visual cortex imaging study.

1. **Navigate to Projects**:
   - Go to *Projects*
   - Click *Add project*

**[SCREENSHOT NEEDED: Project creation interface]**

2. **Configure Project Details**:

| Field | Value |
|-------|-------|
| **Name** | Visual Cortex Population Dynamics Study |
| **Description** | Investigating population-level neural dynamics in mouse visual cortex using two-photon calcium imaging during visual stimulus presentation. Study focuses on orientation selectivity, population correlations, and stimulus-response relationships in layer 2/3 neurons. |
| **Publications** | Related to ongoing visual cortex research |
| **Tags** | two-photon, visual-cortex, calcium-imaging, mice |
| **Authenticated Groups** | Select groups that should have access to this project |
| **Public Access** | No (keep project private to lab) |

{: .note }
> For two-photon imaging studies, include information about the calcium indicator, imaging parameters, and visual stimulus paradigms in the project description. Authenticated groups will get contribute permissions. You can add additional groups or change permissions in the manage page: Go to *Project detail page* → *Manage*

### Step 2: Adding Individual Subjects

Now we'll add individual mice that will participate in our imaging study.

1. **Navigate to Add Subject**:
   - Go to *Subjects* 
   - Click *Add subject*

**[SCREENSHOT NEEDED: Subject creation interface]**

2. **Subject Configuration Example**:

| Field | Value |
|-------|-------|
| **Name** | VC_M001 |
| **Projects** | Select: Visual Cortex Population Dynamics Study |
| **Sex** | Male |
| **Species** | Select: Mus musculus |
| **Strain** | Select: C57BL/6J |
| **Description** | Male C57BL/6J mouse for visual cortex two-photon calcium imaging study. Express GCaMP6f via viral injection. |
| **Genetic Line** | Wild type |
| **Birth Date** | 2024-06-15 |
| **Subject Identifier** | Ear punch: Left ear, position 2 |

**Repeat this process to create additional subjects:**
- VC_M002, VC_M003, VC_M004 (for a cohort of 4 mice)
- Use similar configurations but update IDs and ear punch patterns

{: .note }
> The additional subjects can be duplicated from the first subject. Go to the *Subject detail page of the first subject* → *Duplicate* 
> Fill in the new subject name and click Duplicate. After this you can alter other fields if necessary.

### Step 2b: Document Initial Housing and Weight

After creating subjects, document their housing conditions and initial weights using subject logs.

1. **Create Housing Log**:
   - Go to *Modules* → *Subject logs*
   - Click *Add subject log*

**Housing Log Configuration:**
| Field | Value |
|-------|-------|
| **Type** | Housing log |
| **Subject** | Select: VC_M001 |
| **Description** | Standard housing for imaging cohort mice |
| **Start and end time** | 2024-07-01 08:00:00 to 2024-12-31 18:00:00 |
| **Notes** | Single housed post-surgery. Standard mouse cages with enrichment. |

**Type-specific Details:**
| Field | Value |
|-------|-------|
| **Location** | Animal Facility Room 105 |
| **Cage ID** | Cage_B3_single |
| **Cage type** | Standard mouse cage (32×18×14 cm) |
| **Light cycle** | 12:12 light-dark cycle (lights on 06:00) |
| **Enrichment** | Paper nesting material, plastic igloo |

2. **Create Initial Weighing Log**:

**Weighing Log Configuration:**
| Field | Value |
|-------|-------|
| **Type** | Weighing log |
| **Subject** | Select: VC_M001 |
| **Description** | Baseline weight before surgical procedures |
| **Date and time** | 2024-07-01 09:00:00 |
| **Notes** | Pre-surgery baseline weight. Animal healthy and active. |

**Type-specific Details:**
| Field | Value |
|-------|-------|
| **Weight (grams)** | 24.5 |

### Step 3: Creating the Experimental Cohort

After creating individual subjects, group them into a cohort for experimental organization.

1. **Navigate to Cohorts**:
   - Go to *Personal Attributes* → *Cohorts*
   - Click *Add cohort*

**[SCREENSHOT NEEDED: Cohort creation interface]**

2. **Configure Cohort Details**:

| Field | Value |
|-------|-------|
| **Name** | VC_Imaging_Cohort_1 |
| **Project** | Select: Visual Cortex Population Dynamics Study |
| **Subjects** | Select: VC_M001, VC_M002, VC_M003, VC_M004 |
| **Description** | First experimental cohort for visual cortex two-photon imaging study. 4 male C57BL/6J mice, age-matched, with viral GCaMP6f expression. Single housed post-surgery, 12:12 light cycle, standard chow ad libitum. |
| **Tags** | visual-cortex, two-photon, gcamp6f, male-mice |

**[ILLUSTRATION NEEDED: Flowchart showing project → subjects → cohort → experiment relationship]**

### Step 4: Equipment and Setup Verification

Verify your two-photon imaging setup includes all necessary equipment:

**[SCREENSHOT NEEDED: Equipment list view filtered by imaging setup]**

**Required Equipment**:
- Two-photon microscope system (Bruker/Thorlabs)
- Ti:Sapphire laser (Mai Tai, Chameleon)
- High-speed scanning system (resonant/galvo)
- Photo-multiplier tubes (PMTs)
- Head-fixation apparatus
- Visual stimulus presentation system
- Eye tracking camera
- Temperature control system

## Part B: Surgical Procedures and Preparation

### Step 5: Viral Injection Procedure

Document the viral injection for calcium indicator expression.

1. **Navigate to Procedures**:
   - Go to *Modules* → *Procedures*
   - Click *Add procedure*

**[SCREENSHOT NEEDED: Procedure creation interface]**

2. **Viral Injection Configuration**:

**Basic Information:**
| Field | Value |
|-------|-------|
| **Type** | Virus injection |
| **Subject** | Select: VC_M001 |
| **Date and time** | 2024-07-15 10:00:00 |
| **Setup** | Select: Surgical Station |
| **Equipment** | Select: Stereotaxic Frame |
| **Inventory** | Select: Viral Vectors |
| **Consumable Stock** | Select: AAV1-syn-GCaMP6f |
| **Atlas** | Allen Mouse Brain Atlas |
| **Brain Region** | Visual cortex V1 |
| **Coordinate System** | Stereotaxic Bregma-Based Absolute Coordinates |
| **Notes** | Bilateral AAV injection for GCaMP6f expression in V1. Anesthesia: Isoflurane 2.0% for 45 minutes. Recovery: 3 weeks for expression. |

**Coordinate Details (Type-specific fields):**
| Field | Value |
|-------|-------|
| **AP (mm)** | -3.0 |
| **ML (mm)** | ±2.5 (bilateral) |
| **DV (mm)** | -0.3 (layer 2/3) |
| **AP Angle** | 0° |
| **ML Angle** | 0° |

**Injection Details:**
| Parameter | Value |
|-----------|-------|
| **Injection volume (nL)** | 500 |
| **Injection rate (nL/min)** | 100 |
| **Titer (units/mL)** | 1×10^13 |
| **Titer unit** | vg/mL |
| **Injection profile** | Bolus Injection |

### Step 6: Cranial Window Surgery

Document the cranial window implantation procedure.

**Cranial Window Procedure Configuration:**

**Basic Information:**
| Field | Value |
|-------|-------|
| **Type** | Cranial window |
| **Subject** | Select: VC_M001 |
| **Date and time** | 2024-08-05 09:00:00 |
| **Setup** | Select: Surgical Station |
| **Equipment** | Select: Dental Drill, Stereotaxic Frame |
| **Inventory** | Select: Surgical Supplies |
| **Consumable Stock** | Select: Glass coverslip 3mm, Dental cement |
| **Atlas** | Allen Mouse Brain Atlas |
| **Brain Region** | Visual cortex V1 |
| **Notes** | 3mm diameter cranial window over binocular V1. Dura removed, sealed with 3mm glass coverslip. Dental cement head-plate attachment for head-fixation. |
| **Coordinate System** | Stereotaxic Bregma-Based Absolute Coordinates |

**Window Specifications:**
| Parameter | Value |
|-----------|-------|
| **Method of cranial window** | Surgical drill |
| **Shape of cranial window** | Circular |
| **Length of cranial window (µm)** | 3000 |
| **Width of cranial window (µm)** | 3000 |
| **Thickness of cranial window (µm)** | 150 |
| **Orientation of cranial window** | 0° relative to midline |

{: .note }
> Allow 1-2 weeks recovery before starting imaging sessions. Monitor for inflammation or coverslip clarity issues.

**[ILLUSTRATION NEEDED: Cranial window placement diagram showing V1 location]**

## Part C: Two-Photon Imaging Sessions

### Step 7: Habituation Session

Start with habituation to head-fixation and imaging setup.

1. **Navigate to Sessions**:
   - Go to *Modules* → *Sessions*
   - Click *Add session*

**[SCREENSHOT NEEDED: Session creation form for imaging]**

2. **Habituation Session Configuration**:

**Basic Session Information:**
| Field | Value |
|-------|-------|
| **Name** | VC_M001_Day1_Habituation |
| **Projects** | Select: Visual Cortex Population Dynamics Study |
| **Description** | Head-fixation habituation session. No imaging, just acclimatization to setup and handling procedures. |
| **Date_time_onset** | 2024-08-19 14:00:00 |
| **Tags** | habituation, head-fixation, baseline |
| **Data_storage** | /data/two-photon/vc_m001/ |

**Behavioral Paradigm - Head Fixation:**
| Field | Value |
|-------|-------|
| **Name** | Head Fixation Habituation |
| **Environment Type** | Head-fixed setup |
| **Authenticated Groups** | Select your lab groups |
| **Description** | Habituation protocol for head-fixed two-photon imaging. 30-minute sessions with gradual increase in duration. Neutral gray screen, no visual stimuli. Water rewards for calm behavior. |
| **Public Access** | No |

{: .note }
> Habituation sessions are crucial for reducing stress and motion artifacts in subsequent imaging sessions.

### Step 8: Visual Stimulus Imaging Session

The main experimental session combining visual stimulation with two-photon imaging.

**[SCREENSHOT NEEDED: Two-photon imaging session interface]**

1. **Visual Paradigm Setup**:

| Field | Value |
|-------|-------|
| **Name** | Drifting Gratings Visual Stimuli |
| **Environment Type** | Head-fixed visual display |
| **Authenticated Groups** | Select your lab groups |
| **Description** | Drifting sine-wave gratings presented at 8 orientations (0°-315°, 45° steps). Each stimulus 2s duration, 4s inter-stimulus interval. 10 repeats per orientation, randomized presentation order. Screen distance 25cm, stimulus size 20° visual angle. |
| **Public Access** | No |

2. **Complete Session Configuration**:

**Basic Session Information:**
| Field | Value |
|-------|-------|
| **Name** | VC_M001_Day1_DriftingGratings |
| **Projects** | Select: Visual Cortex Population Dynamics Study |
| **Description** | Two-photon calcium imaging during drifting grating visual stimuli presentation |
| **Date_time_onset** | 2024-08-20 15:00:00 |
| **Tags** | imaging, visual-stimuli, drifting-gratings |
| **Data_storage** | /data/two-photon/vc_m001/ |

**Data Acquisition - Two-Photon Imaging:**
| Setting | Value |
|---------|-------|
| **Session** | Select: VC_M001_Day1_DriftingGratings |
| **Type** | Two-Photon Microscopy |
| **Procedures** | Select: Cranial Window, Viral Injection |
| **Setup** | Select: 2P Imaging Rig |
| **Equipment** | Select: Two-Photon Microscope |
| **Notes** | Single plane imaging at 150μm depth in layer 2/3. GCaMP6f expression, 920nm excitation optimal for this indicator. |

**Type-specific Details:**
| Field | Value |
|---------|-------|
| **Format** | TIFF |
| **Compression** | LZW |
| **Vertical resolution** | 512 |
| **Horizontal resolution** | 512 |
| **Frame rate (Hz)** | 15.5 |
| **Number of frames** | 46500 |
| **Laser power (mW)** | 25 |
| **Excitation wavelength (nm)** | 920 |
| **Imaging depth (μm)** | 150 |
| **Voxel size (X dimension)** | 0.65 |
| **Voxel size (Y dimension)** | 0.65 |
| **Voxel size (Z dimension)** | N/A |

**Data Acquisition - Visual Stimuli:**
| Setting | Value |
|---------|-------|
| **Session** | Select: VC_M001_Day1_DriftingGratings |
| **Type** | General Time-Series |
| **Procedures** | Select: Cranial Window |
| **Setup** | Select: 2P Imaging Rig |
| **Equipment** | Select: Stimulus Computer |
| **Notes** | Visual stimulus timing and parameters. Drifting gratings, 8 orientations, 10 repeats each. |

**Type-specific Details:**
| Field | Value |
|---------|-------|
| **Format** | CSV |
| **Data-type** | float32 |
| **Number of channels** | 3 |
| **Sampling rate (Hz)** | 60 |
| **Number of samples** | 108000 |

**Data Acquisition - Eye Tracking:**
| Setting | Value |
|---------|-------|
| **Session** | Select: VC_M001_Day1_DriftingGratings |
| **Type** | Behavioral Tracking |
| **Procedures** | Select: Cranial Window |
| **Setup** | Select: 2P Imaging Rig |
| **Equipment** | Select: Eye Tracking Camera |
| **Notes** | Pupil tracking during visual stimulation. 60fps capture for pupil dilation analysis. |

**Type-specific Details:**
| Field | Value |
|---------|-------|
| **Format** | AVI |
| **Compression** | H.264 |
| **Frame rate (Hz)** | 60 |
| **Number of frames** | 108000 |
| **Vertical resolution** | 480 |
| **Horizontal resolution** | 640 |

**Session Epochs:**
| Epoch Name | Start (min) | Duration (min) | Description |
|------------|-------------|----------------|-------------|
| **Baseline** | 0 | 5 | Gray screen baseline recording |
| **Stimulus_presentation** | 5 | 25 | Drifting grating stimuli (8 orientations × 10 repeats) |
| **Post_stimulus** | 30 | 5 | Post-stimulus baseline recording |

**[SCREENSHOT NEEDED: Two-photon imaging interface showing real-time calcium signals]**

### Step 9: Retinotopy Mapping Session

Create a session for visual field mapping.

**Retinotopy Session Configuration:**

**Basic Session Information:**
| Field | Value |
|-------|-------|
| **Name** | VC_M001_Day2_RetinotopyMapping |
| **Projects** | Select: Visual Cortex Population Dynamics Study |
| **Description** | Retinotopic mapping using moving bar stimuli to determine visual field organization |
| **Date_time_onset** | 2024-08-21 15:30:00 |
| **Tags** | retinotopy, mapping, visual-field |
| **Data_storage** | /data/two-photon/vc_m001/ |

**Visual Paradigm:**
| Field | Value |
|-------|-------|
| **Name** | Retinotopic Bar Mapping |
| **Environment Type** | Head-fixed visual display |
| **Description** | Moving bar stimuli for retinotopic mapping. White bars on black background, 4 directions (horizontal/vertical), 2° width, 0.5°/s speed. Full screen sweep in each direction. |
| **Public Access** | No |

**Data Acquisition - Two-Photon Imaging:**
| Setting | Value |
|---------|-------|
| **Session** | Select: VC_M001_Day2_RetinotopyMapping |
| **Type** | Two-Photon Microscopy |
| **Procedures** | Select: Cranial Window, Viral Injection |
| **Setup** | Select: 2P Imaging Rig |
| **Equipment** | Select: Two-Photon Microscope |
| **Notes** | Same imaging parameters as orientation session for consistency |

**Type-specific Details:**
| Field | Value |
|---------|-------|
| **Format** | TIFF |
| **Compression** | LZW |
| **Vertical resolution** | 512 |
| **Horizontal resolution** | 512 |
| **Frame rate (Hz)** | 15.5 |
| **Number of frames** | 31000 |
| **Laser power (mW)** | 28 |
| **Excitation wavelength (nm)** | 920 |
| **Imaging depth (μm)** | 150 |
| **Voxel size (X dimension)** | 0.65 |
| **Voxel size (Y dimension)** | 0.65 |
| **Voxel size (Z dimension)** | N/A |

## Part D: Advanced Imaging Features

### Step 10: Multi-Depth Imaging Session

Document sessions with z-stack or multiple imaging planes.

**Multi-Depth Session Configuration:**

**Basic Session Information:**
| Field | Value |
|-------|-------|
| **Name** | VC_M001_Day3_MultiDepth_Orientation |
| **Projects** | Select: Visual Cortex Population Dynamics Study |
| **Description** | Multi-depth two-photon imaging across cortical layers during orientation stimuli |
| **Date_time_onset** | 2024-08-22 14:00:00 |
| **Tags** | multi-depth, layers, orientation |
| **Data_storage** | /data/two-photon/vc_m001/ |

**Data Acquisition - Layer 2/3:**
| Setting | Value |
|---------|-------|
| **Session** | Select: VC_M001_Day3_MultiDepth_Orientation |
| **Type** | Two-Photon Microscopy |
| **Procedures** | Select: Cranial Window, Viral Injection |
| **Setup** | Select: 2P Imaging Rig |
| **Equipment** | Select: Two-Photon Microscope |
| **Notes** | Layer 2/3 imaging plane |

**Type-specific Details (Layer 2/3):**
| Field | Value |
|---------|-------|
| **Format** | TIFF |
| **Compression** | LZW |
| **Vertical resolution** | 512 |
| **Horizontal resolution** | 512 |
| **Frame rate (Hz)** | 15.5 |
| **Number of frames** | 46500 |
| **Laser power (mW)** | 25 |
| **Excitation wavelength (nm)** | 920 |
| **Imaging depth (μm)** | 150 |
| **Voxel size (X dimension)** | 0.65 |
| **Voxel size (Y dimension)** | 0.65 |
| **Voxel size (Z dimension)** | N/A |

**Data Acquisition - Layer 4:**
| Setting | Value |
|---------|-------|
| **Session** | Select: VC_M001_Day3_MultiDepth_Orientation |
| **Type** | Two-Photon Microscopy |
| **Procedures** | Select: Cranial Window, Viral Injection |
| **Setup** | Select: 2P Imaging Rig |
| **Equipment** | Select: Two-Photon Microscope |
| **Notes** | Layer 4 imaging plane - increased laser power for deeper imaging |

**Type-specific Details (Layer 4):**
| Field | Value |
|---------|-------|
| **Format** | TIFF |
| **Compression** | LZW |
| **Vertical resolution** | 512 |
| **Horizontal resolution** | 512 |
| **Frame rate (Hz)** | 15.5 |
| **Number of frames** | 46500 |
| **Laser power (mW)** | 35 |
| **Excitation wavelength (nm)** | 920 |
| **Imaging depth (μm)** | 250 |
| **Voxel size (X dimension)** | 0.65 |
| **Voxel size (Y dimension)** | 0.65 |
| **Voxel size (Z dimension)** | N/A |

### Step 11: Adding Optogenetic Manipulations (Optional)

For experiments combining imaging with optogenetic perturbations.

**[SCREENSHOT NEEDED: Manipulation configuration for optogenetics]**

**Optogenetic Manipulation Configuration:**

**Basic Information:**
| Field | Value |
|-------|-------|
| **Session** | Select: VC_M001_Day4_OptoStim |
| **Type** | Optogenetic stimulation |
| **Procedures** | Select: Viral Injection (ChR2), Cranial Window |
| **Setup** | Select: 2P Imaging Rig |
| **Equipment** | Select: Blue LED System |
| **Notes** | ChR2 activation during visual stimuli presentation |

**Type-specific Details:**
| Parameter | Value |
|-----------|-------|
| **Power (mW)** | 5.0 |
| **Amplitude (A)** | 0.2 |
| **Stimulation profile** | Biphasic |
| **Duration (s)** | 2.0 |
| **Duty cycle** | 0.5 |
| **Repetitions** | 20 |
| **Wavelength (nm)** | 473 |
| **Closed loop** | false |

## Part E: Data Organization and Analysis Integration

### Step 12: Subject Health Monitoring

Track post-surgical recovery and imaging session performance.

**[SCREENSHOT NEEDED: Subject log for imaging studies]**

**Wellness Log Configuration:**
| Field | Value |
|-------|-------|
| **Type** | Wellness log |
| **Subject** | Select: VC_M001 |
| **Description** | Post-surgical recovery and imaging session monitoring |
| **Date and time** | 2024-08-20 18:00:00 |
| **Notes** | Excellent imaging session. Clear cranial window, strong GCaMP signals, minimal motion artifacts. Animal alert and responsive. |

**Type-specific Details:**
| Field | Value |
|-------|-------|
| **Wellness** | Excellent - active, responsive, clear window |

### Step 13: Creating Collections for Analysis

Group related imaging sessions for comprehensive analysis.

**[SCREENSHOT NEEDED: Collection creation for imaging data]**

**Collection Configuration:**

| Field | Value |
|-------|-------|
| **Name** | VC_M001_Orientation_Tuning_Week1 |
| **Project** | Select: Visual Cortex Population Dynamics Study |
| **Sessions** | Select: VC_M001_Day1_DriftingGratings, VC_M001_Day2_RetinotopyMapping, VC_M001_Day3_MultiDepth_Orientation |
| **Description** | First week orientation tuning and retinotopy sessions for VC_M001. Includes single-plane and multi-depth imaging with drifting gratings and retinotopic mapping stimuli. |
| **Tags** | orientation-tuning, retinotopy, calcium-imaging, week1 |

### Step 14: API Data Access for Analysis

Access your imaging data programmatically for analysis.

```python
from brainstem_api_client import BrainstemClient
import numpy as np
import matplotlib.pyplot as plt

client = BrainstemClient()

# Get all imaging sessions for a subject
imaging_sessions = client.load_model('session', 
                                   filters={'projects__name': 'Visual Cortex Population Dynamics Study'}).json()

# Get two-photon data acquisition details
imaging_data = client.load_model('dataacquisition',
                               filters={'session__projects__name': 'Visual Cortex Population Dynamics Study',
                                      'type': 'Two-Photon Microscopy'}).json()

# Download specific imaging session data
session_data = client.download_session_data('vc_m001_day1_gratings_id')
```

## Next Steps

After completing this comprehensive two-photon imaging workflow, consider these logical progressions:

- **Cross-Modal Experiments**: Review the [Electrophysiology Workflow tutorial]({{site.baseurl}}/tutorials/electrophysiology-workflow) to learn how to combine two-photon imaging with simultaneous electrophysiology recordings for comprehensive neural circuit analysis
- **Data Storage Optimization**: Learn about [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage) to efficiently organize and access your large imaging datasets
- **API Integration**: Master the [Python API tool]({{site.baseurl}}/tutorials/python-api-tool) or [MATLAB API tool]({{site.baseurl}}/tutorials/matlab-api-tool) tutorials to programmatically access your imaging data for automated analysis workflows
- **Behavioral Integration**: Explore [Behavioral Paradigms]({{site.baseurl}}/tutorials/behavioral-paradigms) to understand how to combine imaging with more complex behavioral tasks
- **Data Sharing and Collaboration**: Learn about [Sharing Project Publicly]({{site.baseurl}}/tutorials/sharing-project-publicly) to make your imaging datasets available to the research community and enable collaborative analysis
