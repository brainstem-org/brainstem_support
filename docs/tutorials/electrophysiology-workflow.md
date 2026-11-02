---
layout: default
title: Ephys Workflow
parent: Tutorials
nav_order: 8
---

# Ephys Workflow: Theta Maze with Sleep Sessions
{: .no_toc}

## Introduction

This tutorial walks through a complete electrophysiology experiment in BrainSTEM, from subject preparation to data analysis. We'll document a multi-day theta maze learning study with sleep sessions, demonstrating how to integrate subjects, procedures, behavioral assays, data acquisition, manipulations, and collections in a realistic research workflow.

**Experimental Design Overview:**
- **Subjects**: Rat cohort for spatial learning study
- **Setup**: Theta maze with ceiling-mounted camera and OptiTrack 3D tracking
- **Sessions**: Pre-behavior sleep → Theta maze behavior → Post-behavior sleep
- **Data**: Neuropixels recordings, behavioral video, 3D position tracking
- **Analysis**: Learning curves, replay detection, place cell analysis

{: .note }
> This tutorial assumes that the lab infrastructure is already set up (setups, equipment, inventories) as described in the [Setting Up Lab Infrastructure tutorial]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure).

## Part A: Project and Subject Setup

### Step 1: Creating the Research Project

First, we'll create a project to organize and provide context for our experimental work. The project submission is split in two steps. First, you fill in required details, after which you can add other details. Required fields are highlighted with an asterix (*) in the web interface and this tutorial. 

1. **Navigate to Projects**:
   - Go to *Projects*
   - Click *Add project*

![A project's form once created: name, project visibility and description; Online repositories and User roles are separate tabs.]({{site.baseurl}}/assets/images/screenshots/ephys-add-project.png)
{: .screenshot }
*A project's form once created: name, project visibility and description; Online repositories and User roles are separate tabs.*

2. **Configure Project Details**:

| Field | Value |
|-------|-------|
| **Name** * | Theta Maze Spatial Learning Study |
| **Description** | Investigating hippocampal place cell dynamics and memory consolidation during spatial learning using theta maze behavioral assay with simultaneous Neuropixels recordings in freely moving rats. |
| **Authenticated groups** | Select groups that should have access to this project |
| **Project visibility** | Private (keep the project private to the lab) |

{: .note }
> Once submitted other details can be added. Additional project details like PI name, funding source, IACUC protocol numbers, and timeline information can be included in the project description or managed through your lab's separate project management systems. Authenticated groups will get contribute permissions. You can add additional groups or change permissions in the manage page: Go to *Project detail page* → *Manage*

### Step 2: Adding Individual Subjects

Now we'll add individual rats that will participate in our study.

1. **Navigate to Add Subject**:
   - Go to *Subjects* 
   - Click *Add subject*

![The Add subject form filled in for TM_R001: name, project, sex, species Rattus norvegicus with strain Long-Evans, and status Active (the demo project stands in for the tutorial's).]({{site.baseurl}}/assets/images/screenshots/ephys-add-subject.png)
{: .screenshot }
*The Add subject form filled in for TM_R001: name, project, sex, species Rattus norvegicus with strain Long-Evans, and status Active (the demo project stands in for the tutorial's).*

2. **Subject Configuration Example**:

| Field | Value |
|-------|-------|
| **Name** * | TM_R001 |
| **Projects** * | Select: Theta Maze Spatial Learning Study |
| **Sex** * | Male |
| **Species** * | Select: Rattus norvegicus |
| **Strain** | Select: Long-Evans (optional; the list only shows strains of the chosen species) |
| **Status** * | Active |
| **Description** | Male Long-Evans rat for theta maze spatial learning study with Neuropixels recordings |
| **Genetic Line** | Wild type |
| **Birth Date** | 2024-05-01 |
| **Subject Identifier** | Red-001 (ear tag number) |

**Repeat this process to create additional subjects:**
- TM_R002, TM_R003, TM_R004 (for a cohort of 4 rats)
- Use similar configurations but update IDs, ear tags

{: .note }
> The additional subjects can be duplicated from the first subject. Go to the *Subject detail page of the first subject* → *Duplicate*.
> Fill in the new subject name, choose which procedures and logs to copy, click **Check copy** and then **Duplicate**. **Copy as a plan** marks everything copied as planned, which suits animals that are not yet enrolled. Interfaces (the physical implant) are never copied.

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

![A cohort's form: name, project and the rat subjects it groups.]({{site.baseurl}}/assets/images/screenshots/ephys-add-cohort.png)
{: .screenshot }
*A cohort's form: name, project and the rat subjects it groups.*


2. **Configure Cohort Details**:

| Field | Value |
|-------|-------|
| **Name** | TM_Learning_Cohort_1 |
| **Project** | Select: Theta Maze Spatial Learning Study |
| **Subjects** | Select: TM_R001, TM_R002, TM_R003, TM_R004 |
| **Description** | First experimental cohort for theta maze spatial learning study. 4 male Long-Evans rats, age-matched littermates, trained on alternation task with Neuropixels recordings. Pair housed, 12:12 light cycle, food restricted to 85% body weight during training. |
| **Tags** | theta maze, spatial learning, neuropixels, male rats |


### Step 4: Equipment and Setup Verification

Verify your theta maze setup includes all necessary equipment:

**Required Equipment**:
- Neuropixels data acquisition system (IMEC - Neuropixels OneBox)
- Ceiling-mounted camera for behavioral tracking (Basler - acA640-90uc)
- OptiTrack motion capture system for 3D head tracking (6+ cameras OptiTrack - Flex 13)

### Step 5: Neuropixels Probe Implantation Procedure

Document the surgical procedure for Neuropixels probe implantation. A procedure records the event: its type, date, coordinates, target regions, and the **materials** it used. Saving an implant procedure also creates the **experimental interface** (the implanted probe) that sessions refer to later.

1. **Navigate to Procedures**:
   - Go to *Subjects*
   - Open subject *TM_R001* and click *Edit*; procedures are added from the subject page, or from *Subjects* → *Procedures* → *Add procedure* → *Create blank*

![The Procedures tab of a subject's page (here rat R06 Carol): each procedure with its details and its Edit, Duplicate, Template, Delete and API buttons]({{site.baseurl}}/assets/images/screenshots/ephys-subject-procedures.png)
{: .screenshot }
*The Procedures tab of a subject's page (here rat R06 Carol): each procedure with its details and its Edit, Duplicate, Template, Delete and API buttons*


2. **Procedure Configuration**:

**Basic Information:**

| Field | Value |
|-------|-------|
| **Type** * | Silicon probe implant |
| **Subject** * | Select: TM_R001 |
| **Status** * | Performed |
| **Date and time of the procedure** | 2024-08-15 10:00:00 |
| **Equipment** | Select: Stereotaxic Frame (from the Surgical Station setup) |
| **Protocol** | Select your implantation protocol, if you keep one |
| **Atlas** | Waxholm Space Sprague Dawley Rat Brain Atlas |
| **Target regions** | Type to search regions and select the hippocampal CA1 region |
| **Notes** | Chronic Neuropixels probe implantation targeting CA1/CA3 hippocampus. |
| **Coordinates** | Stereotaxic Bregma-Based Surface Coordinates with Depth |

![A silicon probe implant's form: type, date, subject, episode, setup and equipment, atlas and target regions, licenses, protocol, performed by and status.]({{site.baseurl}}/assets/images/screenshots/ephys-procedure-form.png)
{: .screenshot }
*A silicon probe implant's form: type, date, subject, episode, setup and equipment, atlas and target regions, licenses, protocol, performed by and status.*

{% include walkthrough.html slug="ephys-procedure-materials" caption="The Materials tab of a silicon probe implant: its material rows, and the Add material menu listing the roles this procedure type accepts." %}


**Coordinate Details:**

| Field | Value |
|-------|-------|
| **AP coordinate** | -3.5 mm |
| **ML coordinate** | +2.5 mm |
| **Depth** | 2.0 mm (from the brain surface) |
| **AP angle** | 0° |
| **ML angle** | 0° |
| **Rotation** | 0° |

Click **View coordinates** to preview the entry point and implantation track in the atlas. The viewer offers 3D, coronal, sagittal and horizontal views and draws the probe shanks from the linked probe design. It is available for species with a volumetric atlas, such as mouse (Allen CCF) and rat (Waxholm Space), once the subject, a supported coordinate system and the required coordinate values are filled in. See [Atlases and coordinates]({{site.baseurl}}/webinterface/atlases-and-coordinates/).

3. **Materials** tab:

The former single "Consumable stock" field has been replaced by material rows. Each procedure type declares which material roles it accepts; for a silicon probe implant the **Silicon probe** row is required.

   - Click **+ Add material** and choose **Silicon probe**.
   - Choose the **Material source**: **Consumable stock** (select the **Inventory** *Neural Electrode Inventory* and the **Consumable stock** *Neuropixels 2.0 probe*; only stock with status Available or Reserved is offered), **Consumable** (the catalog design when you have no stock entry), or **Manual entry** (a name and specification).
   - Add further rows as used: **Adhesive, cement, or sealant** for the dental cement, **Anchor screw, pin, or fastener** for skull screws, **Surgical supply** for disposables.

A stock-backed row keeps a copy of the stock's details at the time of use (catalog item, lot, dates, storage location), so the procedure stays readable if the inventory changes later. Stock quantities are not decremented; set the stock's **Status** by hand when it is used up.

{: .note }
> Probe specifications (Neuropixels 2.0: 960 total sites, 384 recording sites, 20 μm spacing, etc.) are documented in the catalog design and the consumable stock entry, not in the procedure record. Silicon probe designs from NeuroNexus, ATLAS Neuroengineering, Cambridge Neurotech and IMEC are already in the catalog; see [Setting Up Lab Infrastructure]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure).

4. **Save**. A notice on the form announces: "Saving creates a/an Silicon probe experimental interface from this procedure. Its type, coordinates, installed date, equipment, target regions and device materials then follow this procedure." After saving, the interface *TM_R001 | Silicon probe implant* appears on the procedure's **Experimental interfaces** tab and under *Sessions* → *Experimental interfaces*. Its persistence is "Chronic / persistent". Edit the procedure, not the interface, to change coordinates or the probe; name, persistence, removal date and notes belong to the interface.

{: .note }
> If you record the procedure before surgery, set **Status** to *Planned*. The page then shows an orange **Planned** pill and no interface is created yet. Click **Mark as performed** after the surgery; the date must be set and the interface is created at that point. See [Planning]({{site.baseurl}}/webinterface/planning/).

### Step 5b: Grouping the surgery into a procedure episode (optional)

Anesthesia, analgesia and the implant itself are separate procedures. A **procedure episode** groups them into one perioperative event with personnel, severity and recovery outcome.

1. Go to *Subjects* → *Procedures* and open the episode section, or create the episode first and use **Link existing** to attach procedures.
2. Record the companion procedures on TM_R001:
   - **Anesthesia**: required material **Anesthetic agent** (isoflurane from stock), optional **Carrier gas**; stages **Induction** and **Maintenance** with their conditions.
   - **Analgesic**: route and the **Active agent** material.
   - **Craniotomy** and **Headcap** as further procedures of the same episode.
3. Set the episode's **Status** to *Active* during surgery and *Complete* once end date, recovery outcome and a named responsible person are recorded.

The episode page offers quick **Weighing** and **Welfare check** logs with a **Phase** (Pre-procedure, Recovery, Follow-up, and so on).

## Part B: Multi-Session Experimental Workflow

### Step 6: Pre-Behavior Sleep Session

After recovery, we begin with a baseline sleep recording.

1. **Navigate to Sessions**:
   - Go to *Sessions*
   - Click *Add session*

![The Add session form filled in for TM_R001_Day1_PreSleep_Baseline: session type Subject, project, subject and status (the demo project and rat R01 stand in for the tutorial's).]({{site.baseurl}}/assets/images/screenshots/ephys-session-form.png)
{: .screenshot }
*The Add session form filled in for TM_R001_Day1_PreSleep_Baseline: session type Subject, project, subject and status (the demo project and rat R01 stand in for the tutorial's).*

2. **Sleep Session Configuration**:

**Basic Session Information:**

| Field | Value |
|-------|-------|
| **Name** * | TM_R001_Day1_PreSleep_Baseline |
| **Session type** * | Subject |
| **Projects** * | Select: Theta Maze Spatial Learning Study |
| **Subjects** | Select: TM_R001 |
| **Status** * | Performed |
| **Description** | Baseline sleep recording before theta maze training. 4-hour session to capture natural sleep-wake cycles and establish baseline neural activity patterns. |
| **Date and time onset** | 2024-08-22 09:00:00 |
| **Tags** | baseline, sleep, pre-training, neuropixels |

{: .note }
> Sessions have no setup, duration or behavioral assay fields. Those are specified in the Behavior, Data acquisition and Epoch tabs within the session. A session can also be created as *Planned* and marked performed later.

**Data Acquisition - Extracellular Recording:**

| Setting | Value |
|---------|-------|
| **Type** * | Extracellular Electrophysiology |
| **Experimental interfaces** * | Select: TM_R001 \| Silicon probe implant |
| **Equipment** | Select: Neuropixels System (from the Sleep Recording Box setup) |
| **File name** | TM_R001_Day1_PreSleep_Baseline.dat |
| **Format** | Binary |
| **Data-type** | int16 |
| **Number of channels** | 384 |
| **Sampling rate (Hz)** | 30000 |
| **Least significant bit (μV/bit)** | 0.195 |

**Data Acquisition - Video:**

| Setting | Value |
|---------|-------|
| **Session** | Select: TM_R001_Day1_PreSleep_Baseline |
| **Type** * | Video Tracking |
| **Experimental interfaces** * | Select: Sleep Box Camera (a *Camera* interface; see note) |
| **Equipment** | Select: Sleep Box Camera |
| **Notes** | Sleep state monitoring |

{: .note }
> Every data acquisition names the **experimental interfaces** the signal passed through; the field is required and only offers interfaces of subjects (or specimen sets) in the session's projects. Implanted devices get their interface from the implant procedure. For equipment such as cameras, create an interface of type *Camera* once (*Sessions* → *Experimental interfaces* → *Add experimental interface*, target the subject, link the equipment) and reuse it in every session. Equipment-backed interface types take no materials.


**Session Epochs:**

| Epoch Name | Start | End | Description |
|------------|-------|-----|-------------|
| **Habituation** | 00:00:00 | 00:30:00 | Adaptation to recording environment |
| **Baseline_recording** | 00:30:00 | 04:00:00 | Continuous sleep/wake recording (3.5 hours) |

![The Data acquisition tab of a saved session (here rat R02's Reversal 01): a Video Tracking entry and, below it, the session's second data acquisition, an Extracellular Electrophysiology entry with its setup, equipment and experimental interface]({{site.baseurl}}/assets/images/screenshots/ephys-session-data-acquisition.png)
{: .screenshot }
*The Data acquisition tab of a saved session (here rat R02's Reversal 01): a Video Tracking entry and, below it, the session's second data acquisition, an Extracellular Electrophysiology entry with its setup, equipment and experimental interface*

### Step 7: Theta Maze Behavioral Session

The main experimental session combining behavior with neural recording.

1. **Behavioral Assay Setup** (**Personal attributes** → **Behavioral assays** → **Add behavioral assay**; see [Behavioral Assays]({{site.baseurl}}/tutorials/behavioral-assays)):

| Field | Value |
|-------|-------|
| **Behavioral assay name** | Theta Maze Alternation Task |
| **Setup type** | Theta maze (the same setup type as the Theta Maze Rig setup) |
| **Behavioral paradigm** | Select the alternation paradigm |
| **Authenticated groups** | Select your lab groups |
| **Description** | Forced alternation task in theta maze. Rats navigate alternating left/right arms to receive food rewards. Trial duration 180s, inter-trial interval 45s, total 40 trials per session. Performance criteria: 80% correct, minimum 15 trials for learning threshold. |
| **Behavioral assay visibility** | Private |

2. **Complete Session Configuration**:

**Basic Session Information:**

| Field | Value |
|-------|-------|
| **Name** * | TM_R001_Day1_ThetaMaze_Training1 |
| **Session type** * | Subject |
| **Projects** * | Select: Theta Maze Spatial Learning Study |
| **Subjects** | Select: TM_R001 |
| **Status** * | Performed |
| **Description** | First day theta maze behavioral training with Neuropixels recording |
| **Date and time onset** | 2024-08-22 14:00:00 |
| **Tags** | behavior, theta-maze, training, day1 |
| **Data storage** | Select: Lab Server (see [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage)) |
| **Name used in storage** | tm_r001_day1_training1 |

**Behavior:**

| Field | Value |
|-------|-------|
| **Subjects** | Select: TM_R001 |
| **Setup** | Select: Theta Maze Rig |
| **Behavioral assay** | Select: Theta Maze Alternation Task |

![The Behaviors tab of a saved session (here rat R02's Reversal 01): each behavior names its subjects, behavioral assay and setup]({{site.baseurl}}/assets/images/screenshots/ephys-behavior-tab.png)
{: .screenshot }
*The Behaviors tab of a saved session (here rat R02's Reversal 01): each behavior names its subjects, behavioral assay and setup*

**Data Acquisition - Extracellular Recording:**

| Setting | Value |
|---------|-------|
| **Session** | Select: TM_R001_Day1_ThetaMaze_Training1 |
| **Type** * | Extracellular Electrophysiology |
| **Experimental interfaces** * | Select: TM_R001 \| Silicon probe implant |
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
| **Session** | Select: TM_R001_Day1_ThetaMaze_Training1 |
| **Type** * | Video Tracking |
| **Experimental interfaces** * | Select: Ceiling Camera (*Camera* interface) |
| **Equipment** | Select: Ceiling Camera |
| **Notes** | Behavioral video recording with LED tracking |

**Data Acquisition - Position Tracking:**

| Setting | Value |
|---------|-------|
| **Session** | Select: TM_R001_Day1_ThetaMaze_Training1 |
| **Type** * | Behavioral Tracking |
| **Experimental interfaces** * | Select: OptiTrack (*Tracking system* interface) |
| **Equipment** | Select: OptiTrack System |
| **Notes** | Head and body position tracking with LED markers |

**Session Epochs:**

| Epoch Name | Start | End | Description |
|------------|-------|-----|-------------|
| **Pre_task_baseline** | 00:00:00 | 00:10:00 | Open field exploration before task |
| **Training_trials** | 00:10:00 | 01:10:00 | Forced alternation training trials (longer for rats) |
| **Free_choice_trials** | 01:10:00 | 01:50:00 | Free choice alternation test (longer for rats) |
| **Post_task_rest** | 01:50:00 | 02:00:00 | Rest period after task completion |

Epoch **Start** and **End** are given relative to the session start (hh:mm:ss or seconds). On the **Epochs** tab, drag the behavior, data acquisitions and manipulations from **Link to epochs** onto the epoch they belong to; a data acquisition can belong to one epoch only. The **Timeline** on the session's **Epochs** tab shows the result.

![The Epochs tab of a saved session (here rat R02's Reversal 01): the timeline of its three epochs with their behavior, data acquisitions and manipulation, and the epochs table below]({{site.baseurl}}/assets/images/screenshots/ephys-epochs-tab.png)
{: .screenshot }
*The Epochs tab of a saved session (here rat R02's Reversal 01): the timeline of its three epochs with their behavior, data acquisitions and manipulation, and the epochs table below*

### Step 8: Adding Manipulations (Optional)

For experiments with optogenetic or pharmacological manipulations.

![An example manipulation form, here an auditory stimulation in rat R06's Reversal 01 session, with its setup, equipment and the type-specific details table; an optogenetic stimulation has its own details.]({{site.baseurl}}/assets/images/screenshots/ephys-manipulation-form.png)
{: .screenshot }
*An example manipulation form, here an auditory stimulation in rat R06's Reversal 01 session, with its setup, equipment and the type-specific details table; an optogenetic stimulation has its own details.*

**Manipulation Configuration:**

**Basic Information:**

| Field | Value |
|-------|-------|
| **Session** | Select: TM_R001_Day1_ThetaMaze_Training1 |
| **Type** * | Optogenetic stimulation |
| **Experimental interfaces** * | Select: TM_R001 \| Optic fiber implant |
| **Equipment** | Select: Yellow Laser System |
| **Notes** | PV interneuron silencing during choice trials |

{: .note }
> Manipulations link to experimental interfaces, not procedures. The optic fiber interface comes from an *Optic fiber implant* procedure on TM_R001 (required material: **Implanted optic fiber**), recorded like the probe implant in Step 5. The virus that expresses the opsin is a *Virus injection* procedure with a **Viral-vector preparation** material row.

**Type-specific Details:**

| Parameter | Value |
|-----------|-------|
| **Power** | 10 mW |
| **Profile** | Square |
| **Duration** | 0.5 s |
| **Duty cycle** | 1.0 |
| **Repetitions** | 40 |
| **Wavelength** | 589 nm |
| **Closed loop** | Unchecked |

The details of an optogenetic stimulation are a table: add one row per stimulation pattern used in the session.

### Step 9: Post-Behavior Sleep Session

Capture sleep-dependent replay and consolidation.

**Post-Sleep Session Configuration:**

**Basic Session Information:**

| Field | Value |
|-------|-------|
| **Name** * | TM_R001_Day1_PostSleep_Consolidation |
| **Session type** * | Subject |
| **Projects** * | Select: Theta Maze Spatial Learning Study |
| **Subjects** | Select: TM_R001 |
| **Status** * | Performed |
| **Description** | Post-behavior sleep session for memory consolidation recording |
| **Date and time onset** | 2024-08-22 16:00:00 |
| **Tags** | postsleep, consolidation, replay |
| **Data storage** | Select: Lab Server |

**Data Acquisition - Extracellular Recording:**

| Setting | Value |
|---------|-------|
| **Session** | Select: TM_R001_Day1_PostSleep_Consolidation |
| **Type** * | Extracellular Electrophysiology |
| **Experimental interfaces** * | Select: TM_R001 \| Silicon probe implant |
| **Equipment** | Select: Neuropixels System |
| **Format** | Binary |
| **Data-type** | int16 |
| **Number of channels** | 384 |
| **Sampling rate (Hz)** | 30000 |
| **Number of samples** | 648000000 |

**Session Epochs:**

| Epoch Name | Start | End | Description |
|------------|-------|-----|-------------|
| **Post_behavior_rest** | 00:00:00 | 01:00:00 | Immediate post-behavior period |
| **Sleep_recording** | 01:00:00 | 06:00:00 | Extended sleep/replay recording (5 hours) |

## Part C: Data Organization and API access

### Step 10: Creating Collections

Group related sessions for analysis and organization.

![A collection's form: the project and the sessions it groups.]({{site.baseurl}}/assets/images/screenshots/ephys-collection-form.png)
{: .screenshot }
*A collection's form: the project and the sessions it groups.*

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
from brainstem_api_tools import BrainstemClient

client = BrainstemClient()

# Step 1: Resolve subject name to its UUID
subjects = client.load('subject', filters={'name': 'TM_R001'}).json()
subject_id = subjects['subjects'][0]['id']

# Step 2: Sessions name their subjects directly
sessions = client.load('session',
                       filters={'subjects': subject_id},
                       load_all=True)['sessions']   # load_all returns the decoded JSON
session_ids = [s['id'] for s in sessions]

# Step 3: Neural data acquisition records per session, with the interfaces they used
neural_files = []
for sid in session_ids:
    resp = client.load('dataacquisition',
                       filters={'session': sid, 'type': 'ExtracellularEphys'},
                       include=['interfaces']).json()
    neural_files.extend(resp.get('data_acquisitions', []))

# Step 4: The implant procedure and its material usage rows (the probe, cement, screws)
procedures = client.load('procedure',
                         filters={'subject': subject_id, 'type': 'SiliconProbeImplant'}).json()
procedure_id = procedures['procedures'][0]['id']
probe_materials = client.load('materialusage', filters={'procedure': procedure_id},
                              load_all=True)['materialusages']

# Load a specific session by name
session_data = client.load('session',
                           filters={'name': 'TM_R001_Day1_ThetaMaze_Training1'}).json()

# Export the whole project (format 2.1 JSON) for NWB conversion
export = client.export_project(sessions[0]['projects'][0])
```

Planned sessions and procedures are left out of API lists unless you filter on `status`, for example `client.load('session', filters={'status': 'planned'})`.

## Next Steps

After completing this comprehensive electrophysiology workflow, consider these logical progressions:

- **Explore an imaging workflow**: The [Two-Photon Imaging Workflow]({{site.baseurl}}/tutorials/two-photon-imaging-workflow) records a virus injection, a cranial window and imaging sessions with the same building blocks
- **Access data programmatically**: Master the [Python API tool]({{site.baseurl}}/tools/python-api-tool) or [MATLAB API tool]({{site.baseurl}}/tools/matlab-api-tool) to automate analysis workflows for your large-scale electrophysiology datasets
- **Understand behavioral documentation**: Review [Behavioral Assays]({{site.baseurl}}/tutorials/behavioral-assays) to understand how behavioral protocols are documented and standardized across experiments
- **Optimize data management**: Learn about [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage) to efficiently organize and access your large electrophysiology datasets with proper file linking
- **Enable data sharing**: Use [Sharing Project Publicly]({{site.baseurl}}/tutorials/sharing-project-publicly) to make your electrophysiology datasets available to the research community for collaborative analysis and meta-studies
- **Export to NWB**: Follow [Exporting to NWB]({{site.baseurl}}/tutorials/exporting-to-nwb) to turn the sessions into NWB files with the probe, electrode group and surgery metadata filled in from these records
