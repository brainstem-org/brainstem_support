---
layout: default
title: Ephys Workflow
parent: Tutorials
nav_order: 9
---

# Ephys Workflow: Theta Maze with Sleep Sessions
{: .no_toc}

## Introduction

This tutorial walks through a complete electrophysiology experiment in BrainSTEM, from subject preparation to data analysis. We'll document a multi-day theta maze learning study with sleep sessions, demonstrating how to integrate subjects, procedures, behavioral paradigms, data acquisition, manipulations, and collections in a realistic research workflow.

**Experimental Design Overview:**
- **Subjects**: Rat cohort for spatial learning study
- **Setup**: Theta maze with ceiling-mounted camera and OptiTrack 3D tracking
- **Sessions**: Pre-behavior sleep → Theta maze behavior → Post-behavior sleep
- **Data**: Neuropixels recordings, behavioral video, 3D position tracking
- **Analysis**: Learning curves, replay detection, place cell analysis

{: .note }
> This tutorial assumes you have already set up your lab infrastructure (setups, equipment, inventories) as described in the [Setting Up Lab Infrastructure tutorial]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure).

## Part A: Project and Subject Setup

### Step 1: Creating the Research Project

First, we'll create a project to organize and provide context for our experimental work. The project submission is split in two steps. First, you fill in required details, after which you can add other details. Required fields are highlighted with an asterix (*) in the web interface and this tutorial. 

1. **Navigate to Projects**:
   - Go to *Projects*
   - Click *Add project*

![Project creation interface](/assets/images/tutorials/ephys/add_project.png)

**[SCREENSHOT NEEDED: Project creation interface]**

2. **Configure Project Details**:

| Field | Value |
|-------|-------|
| **Name** * | Theta Maze Spatial Learning Study |
| **Description** | Investigating hippocampal place cell dynamics and memory consolidation during spatial learning using theta maze behavioral paradigm with simultaneous Neuropixels recordings in freely moving rats. |
| **Authenticated Groups** | Select groups that should have access to this project |
| **Public Access** | No (keep project private to lab) |

{: .note }
> Once submitted other details can be added. Additional project details like PI name, funding source, IACUC protocol numbers, and timeline information can be included in the project description or managed through your lab's separate project management systems. Authenticated groups will get contribute permissions. You can add additional groups or change permissions in the manage page: Go to *Project detail page* → *Manage*

### Step 2: Adding Individual Subjects

Now we'll add individual rats that will participate in our study.

1. **Navigate to Add Subject**:
   - Go to *Subjects* 
   - Click *Add subject*

![Subject creation form](/assets/images/tutorials/ephys/add_subject.png)

2. **Subject Configuration Example**:

| Field | Value |
|-------|-------|
| **Name** * | TM_R001 |
| **Projects** * | Select: Theta Maze Spatial Learning Study |
| **Sex** * | Male |
| **Species** * | Select: Rattus norvegicus |
| **Strain** * | Select: Long-Evans |
| **Description** | Male Long-Evans rat for theta maze spatial learning study with Neuropixels recordings |
| **Genetic Line** | Wild type |
| **Birth Date** | 2024-05-01 |
| **Subject Identifier** | Red-001 (ear tag number) |

**Repeat this process to create additional subjects:**
- TM_R002, TM_R003, TM_R004 (for a cohort of 4 rats)
- Use similar configurations but update IDs, ear tags

{: .note }
> The additional subjects can be duplicated from the first subject. Go to the *Subject detail page of the first subject* → *Duplicate* 
> Fill in the new subject name and click Duplicate. After this you can alter other fields if necessary.

### Step 2b: Document Initial Housing and Weight

After creating subjects, document their housing conditions and initial weights using subject logs.

1. **Create Housing Log**:
   - Go to *Subject logs* (below Subjects)
   - Click *Add subject log*

**Housing Log Configuration:**

| Field | Value |
|-------|-------|
| **Type** | Housing log |
| **Subject** | Select: TM_R001 |
| **Description** | Initial housing assignment for experimental cohort |

**Type-specific Details:**

| Field | Value |
|-------|-------|
| **Start and end time** | 2024-08-01 08:00:00 to 2024-12-31 18:00:00 |
| **Notes** | Pair-housed with TM_R002. Standard rat cages with enrichment. |
| **Location** | Animal Facility Room 204 |
| **Cage ID** | Cage_A1_pair |
| **Cage type** | NexGen Rat 1800 |
| **Light cycle** | 12:12 light-dark cycle (lights on 07:00) |
| **Enrichment** | Paper tubes, wooden chew blocks |

{: .note }
> Only the start time is required, so you can leave the end time blank.

2. **Create Initial Weighing Log**:

**Weighing Log Configuration:**

| Field | Value |
|-------|-------|
| **Type** | Weighing log |
| **Subject** | Select: TM_R001 |

**Type-specific Details:**

| Field | Value |
|-------|-------|
| **Weight (grams)** | 385 |
| **Date and time** | 2024-08-01 09:00:00 |
| **Notes** | Pre-experiment baseline weight. Animal healthy and active. |

### Step 3: Creating the Experimental Cohort

After creating individual subjects, we can group them into a cohort for experimental organization.

1. **Navigate to Cohorts**:
   - Go to *Cohorts* (below Subjects)
   - Click *Add cohort*

![Cohort creation form](/assets/images/tutorials/ephys/add_cohort.png)

2. **Configure Cohort Details**:

| Field | Value |
|-------|-------|
| **Name** | TM_Learning_Cohort_1 |
| **Project** | Select: Theta Maze Spatial Learning Study |
| **Subjects** | Select: TM_R001, TM_R002, TM_R003, TM_R004 |
| **Description** | First experimental cohort for theta maze spatial learning study. 4 male Long-Evans rats, age-matched littermates, trained on alternation task with Neuropixels recordings. Pair housed, 12:12 light cycle, food restricted to 85% body weight during training. |
| **Tags** | theta maze, spatial learning, neuropixels, male rats |

**[ILLUSTRATION NEEDED: Flowchart showing project → subjects → cohort → experiment relationship]**

### Step 4: Equipment and Setup Verification

Verify your theta maze setup includes all necessary equipment:

![Equipment list view filtered by setup](/assets/images/tutorials/ephys/equipment_list.png)

**Required Equipment**:
- Neuropixels data acquisition system (IMEC - Neuropixels OneBox)
- Ceiling-mounted camera for behavioral tracking (Basler - acA640-90uc)
- OptiTrack motion capture system for 3D head tracking (6+ cameras OptiTrack - Flex 13)

### Step 5: Neuropixels Probe Implantation Procedure

Document the surgical procedure for Neuropixels probe implantation.

1. **Navigate to Procedures**:
   - Go to *Subjects* (below Subjects)
   - Click Edit for subject *TM_R001*

![Procedure view](/assets/images/tutorials/ephys/subject_procedure_view.png)

2. **Procedure Configuration**:

**Basic Information:**

| Field | Value |
|-------|-------|
| **Type** | Silicon probe implant |
| **Subject** | Select: TM_R001 |
| **Date and Time** | 2024-08-15 10:00:00 |
| **Setup** | Select: Surgical Station |
| **Equipment** | Select: Stereotaxic Frame |
| **Inventory** | Select: Neural Electrode Inventory |
| **Consumable Stock** | Select: Neuropixels 2.0 probe |
| **Atlas** | Allen Mouse Brain Atlas |
| **Brain Region** | HIP: Hippocampal region |
| **Notes** | Chronic Neuropixels probe implantation targeting CA1/CA3 hippocampus. |
| **Coordinates System** | Stereotaxic Bregma-Based Surface Coordinates with Depth |

**Coordinate Details:**

| Field | Value |
|-------|-------|
| **AP coordinate (mm)** | -3.5 |
| **ML coordinate (mm)** | +2.5 |
| **DV coordinate (mm)** | 2.0 (initial insertion depth) |
| **AP angle** | 0° |
| **ML angle** | 0° |
| **Rotation** | 0° |

{: .note }
> Probe specifications (Neuropixels 2.0: 960 total sites, 384 recording sites, 20 μm spacing, etc.) are documented in the consumable stock entry, not in the procedure record. You can also document the Isoflurane anesthesia, Head fixation, Craniotomy, and the Headcap, but we will leave that out for brevity.

**[ILLUSTRATION NEEDED: Brain atlas diagram showing electrode placement coordinates]**

## Part B: Multi-Session Experimental Workflow

### Step 6: Pre-Behavior Sleep Session

After recovery, we begin with a baseline sleep recording.

1. **Navigate to Sessions**:
   - Go to *Sessions*
   - Click *Add session*

**[SCREENSHOT NEEDED: Session creation form]**

2. **Sleep Session Configuration**:

**Basic Session Information:**

| Field | Value |
|-------|-------|
| **Name** | TM_R001_Day1_PreSleep_Baseline |
| **Projects** | Select: Theta Maze Spatial Learning Study |
| **Description** | Baseline sleep recording before theta maze training. 4-hour session to capture natural sleep-wake cycles and establish baseline neural activity patterns. |
| **Date_time_onset** | 2024-08-22 09:00:00 |
| **Tags** | baseline, sleep, pre-training, neuropixels |

{: .note }
> Sessions don't have subject, setup, duration, or behavioral paradigm fields directly. These are specified in the Behavior, Data acquisition and Epoch tabs within the session.

**Data Acquisition - Extracellular Recording:**

| Setting | Value |
|---------|-------|
| **Type** | Extracellular Electrophysiology |
| **Subject procedures** | Select: TM_R001 : Silicon probe implant : Neuropixels Implantation |
| **Setup** | Select: Sleep Recording Box |
| **Equipment** | Select: Neuropixels System |
| **File name** | TM_R001_Day1_PreSleep_Baseline.dat |
| **Format** | Binary |
| **Data-type** | int16 |
| **Number of channels** | 384 |
| **Sampling rate (Hz)** | 30000 |
| **Least significant bit (μV/bit)** | 0.195 |

**Data Acquisition - Video:**

| Setting | Value |
|---------|-------|
| **Session** | Select: TM_R001_Day1_PreSleep |
| **Type** | Video Tracking |
| **Procedures** | Select: TM_R001 : Silicon probe implant : Neuropixels Implantation |
| **Setup** | Select: Sleep Recording Box |
| **Equipment** | Select: Sleep Box Camera |
| **Notes** | Sleep state monitoring |

**Session Epochs:**

| Epoch Name | Start (min) | Duration (min) | Description |
|------------|-------------|----------------|-------------|
| **Habituation** | 0 | 30 | Adaptation to recording environment |
| **Baseline_recording** | 30 | 210 | Continuous sleep/wake recording (3.5 hours) |

**[SCREENSHOT NEEDED: Session configuration interface showing data acquisition modules]**

### Step 7: Theta Maze Behavioral Session

The main experimental session combining behavior with neural recording.

**[SCREENSHOT NEEDED: Behavioral paradigm selection interface]**

1. **Behavioral Paradigm Setup**:

| Field | Value |
|-------|-------|
| **Name** | Theta Maze Alternation Task |
| **Environment Type** | Theta maze |
| **Authenticated Groups** | Select your lab groups |
| **Description** | Forced alternation task in theta maze. Rats navigate alternating left/right arms to receive food rewards. Trial duration 180s, inter-trial interval 45s, total 40 trials per session. Performance criteria: 80% correct, minimum 15 trials for learning threshold. |
| **Public Access** | No |

2. **Complete Session Configuration**:

**Basic Session Information:**

| Field | Value |
|-------|-------|
| **Name** | TM_R001_Day1_ThetaMaze_Training1 |
| **Projects** | Select: Theta Maze Spatial Learning Study |
| **Description** | First day theta maze behavioral training with Neuropixels recording |
| **Date_time_onset** | 2024-08-22 14:00:00 |
| **Tags** | behavior, theta-maze, training, day1 |
| **Data_storage** | /data/neuropixels/tm_r001/ |

**Data Acquisition - Extracellular Recording:**

| Setting | Value |
|---------|-------|
| **Session** | Select: TM_R001_Day1_Behavior |
| **Type** | Extracellular Electrophysiology |
| **Procedures** | Select: Neuropixels Implantation |
| **Setup** | Select: Theta Maze Rig |
| **Equipment** | Select: Neuropixels System |
| **Format** | Binary |
| **Data-type** | int16 |
| **Number of channels** | 384 |
| **Sampling rate (Hz)** | 30000 |
| **Number of samples** | 216000000 |
| **Least significant bit (μV/bit)** | 0.195 |

**Data Acquisition - Video:**

| Setting | Value |
|---------|-------|
| **Session** | Select: TM_R001_Day1_Behavior |
| **Type** | Video |
| **Procedures** | Select: Neuropixels Implantation |
| **Setup** | Select: Theta Maze Rig |
| **Equipment** | Select: Ceiling Camera |
| **Notes** | Behavioral video recording with LED tracking |

**Data Acquisition - Position Tracking:**

| Setting | Value |
|---------|-------|
| **Session** | Select: TM_R001_Day1_Behavior |
| **Type** | Behavioral Tracking |
| **Procedures** | Select: Neuropixels Implantation |
| **Setup** | Select: Theta Maze Rig |
| **Equipment** | Select: OptiTrack System |
| **Notes** | Head and body position tracking with LED markers |

**Session Epochs:**

| Epoch Name | Start (min) | Duration (min) | Description |
|------------|-------------|----------------|-------------|
| **Pre_task_baseline** | 0 | 10 | Open field exploration before task |
| **Training_trials** | 10 | 60 | Forced alternation training trials (longer for rats) |
| **Free_choice_trials** | 70 | 40 | Free choice alternation test (longer for rats) |
| **Post_task_rest** | 110 | 10 | Rest period after task completion |

**[SCREENSHOT NEEDED: Session interface showing multiple data acquisition modules and epochs]**

### Step 8: Adding Manipulations (Optional)

For experiments with optogenetic or pharmacological manipulations.

**[SCREENSHOT NEEDED: Manipulation creation interface]**

**Manipulation Configuration:**

**Basic Information:**

| Field | Value |
|-------|-------|
| **Session** | Select: TM_R001_Day1_Behavior |
| **Type** | Optogenetic stimulation |
| **Procedures** | Select: Neuropixels Implantation |
| **Setup** | Select: Theta Maze Rig |
| **Equipment** | Select: Yellow Laser System |
| **Notes** | PV interneuron silencing during choice trials |

**Type-specific Details:**

| Parameter | Value |
|-----------|-------|
| **Power (mW)** | 10.0 |
| **Amplitude (A)** | 0.5 |
| **Stimulation profile** | Continuous |
| **Duration (s)** | 0.5 |
| **Duty cycle** | 1.0 |
| **Repetitions** | 40 |
| **Wavelength (nm)** | 589 |
| **Closed loop** | false |

### Step 9: Post-Behavior Sleep Session

Capture sleep-dependent replay and consolidation.

**Post-Sleep Session Configuration:**

**Basic Session Information:**

| Field | Value |
|-------|-------|
| **Name** | TM_R001_Day1_PostSleep_Consolidation |
| **Projects** | Select: Theta Maze Spatial Learning Study |
| **Description** | Post-behavior sleep session for memory consolidation recording |
| **Date_time_onset** | 2024-08-22 16:00:00 |
| **Tags** | postsleep, consolidation, replay |
| **Data_storage** | /data/neuropixels/tm_r001/ |

**Data Acquisition - Extracellular Recording:**

| Setting | Value |
|---------|-------|
| **Session** | Select: TM_R001_Day1_PostSleep_Consolidation |
| **Type** | Extracellular Electrophysiology |
| **Procedures** | Select: Neuropixels Implantation |
| **Setup** | Select: Sleep Recording Box |
| **Equipment** | Select: Neuropixels System |
| **Format** | Binary |
| **Data-type** | int16 |
| **Number of channels** | 384 |
| **Sampling rate (Hz)** | 30000 |
| **Number of samples** | 648000000 |

**Session Epochs:**

| Epoch Name | Start (min) | Duration (min) | Description |
|------------|-------------|----------------|-------------|
| **Post_behavior_rest** | 0 | 60 | Immediate post-behavior period |
| **Sleep_recording** | 60 | 300 | Extended sleep/replay recording (5 hours) |

## Part C: Data Organization and API access

### Step 10: Creating Collections

Group related sessions for analysis and organization.

**[SCREENSHOT NEEDED: Collection creation interface]**

**Collection Configuration:**

| Field | Value |
|-------|-------|
| **Name** | TM_R001_Learning_Week1 |
| **Project** | Select: Theta Maze Spatial Learning Study |
| **Sessions** | Select: TM_R001_Day1_PreSleep_Baseline, TM_R001_Day1_ThetaMaze_Training1, TM_R001_Day1_PostSleep_Consolidation |
| **Description** | First week of theta maze training for subject TM_R001. Collection includes presleep baseline, behavioral training session, and postsleep consolidation recording. |
| **Tags** | learning, spatial_memory, hippocampus, week1, place_cells |

### Step 11: API Data Access for Analysis

Access your experimental data programmatically for analysis.

```python
from brainstem_api_client import BrainstemClient

client = BrainstemClient()

# Get all sessions for a subject
subject_sessions = client.load_model('session', 
                                   filters={'subject__name': 'TM_R001'}).json()

# Get behavioral performance data
behavior_data = client.load_model('behavioralparadigm',
                                filters={'session__subject__name': 'TM_R001'}).json()

# Get neural data file paths
neural_files = client.load_model('dataacquisition',
                               filters={'session__subject__name': 'TM_R001',
                                      'type': 'Extracellular'}).json()

# Download specific session data
session_data = client.load_model('session', filters={'name': 'tm_r001_day1_behavior_id'})
```

## Next Steps

After completing this comprehensive electrophysiology workflow, consider these logical progressions:

- **Explore complementary techniques**: Review the [Two-Photon Imaging Workflow tutorial]({{site.baseurl}}/tutorials/two-photon-imaging-workflow) to learn how to combine electrophysiology with optical imaging approaches
- **Access data programmatically**: Master the [Python API tool]({{site.baseurl}}/tutorials/python-api-tool) or [MATLAB API tool]({{site.baseurl}}/tutorials/matlab-api-tool) to automate analysis workflows for your large-scale electrophysiology datasets
- **Understand behavioral documentation**: Review [Behavioral Paradigms]({{site.baseurl}}/tutorials/behavioral-paradigms) to understand how behavioral protocols are documented and standardized across experiments
- **Optimize data management**: Learn about [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage) to efficiently organize and access your large electrophysiology datasets with proper file linking
- **Enable data sharing**: Use [Sharing Project Publicly]({{site.baseurl}}/tutorials/sharing-project-publicly) to make your electrophysiology datasets available to the research community for collaborative analysis and meta-studies
