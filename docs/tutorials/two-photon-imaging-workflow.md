---
layout: default
title: 2P Imaging Workflow
parent: Tutorials
nav_order: 14
---

# Two-Photon Imaging Workflow: Visual Cortex Population Dynamics
{: .no_toc}

This tutorial records a two-photon calcium imaging experiment in BrainSTEM from the first mouse to the analysis-ready collection: a project and a cohort, the virus injection and the cranial window with the experimental interface it creates, a habituation session, imaging sessions with visual stimuli and eye tracking, and the collection that groups them. At the end you can load the imaging acquisitions of every session through the API.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Prerequisites

- Your lab infrastructure is set up as in [Setting Up Lab Infrastructure]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure): a surgical setup with a stereotaxic frame, an imaging setup of setup type **Head-fixed passive platform** with the microscope, the stimulus monitor and the eye camera as equipment, and an inventory with the virus stock, coverslips and dental cement as consumable stocks.
- You are a Contributor of the project's group (see [Manage Groups]({{site.baseurl}}/tutorials/managing-groups)).
- The [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow) explains the same building blocks for a probe implant; this tutorial follows its structure and only spells out what differs for imaging.

Required fields are marked with an asterisk (*) in the web interface and in the tables below.

## Part A: Project and Subject Setup

### Step 1: Create the project

1. Go to **Projects** and click **Add project**.
2. Fill in the first step of the form:

| Field | Value |
|-------|-------|
| **Name** * | Visual Cortex Population Dynamics Study |
| **Authenticated groups** | Select the groups that should have access |

3. Click **Create and continue**, then add the rest:

| Field | Value |
|-------|-------|
| **Description** | Population dynamics in mouse visual cortex measured with two-photon calcium imaging during visual stimulation: orientation selectivity, population correlations and retinotopy in layer 2/3. |
| **Tags** | two-photon, visual-cortex, calcium-imaging, mice |
| **Project visibility** | Private |

![A project's form once created: name, project visibility and description; Online repositories and User roles are separate tabs.]({{site.baseurl}}/assets/images/screenshots/2p-add-project.png)
{: .screenshot }
*A project's form once created: name, project visibility and description; Online repositories and User roles are separate tabs.*

{: .note }
> The groups you select get Contributor access. Change roles later with **Manage** on the project page (see [Manage Projects]({{site.baseurl}}/tutorials/managing-projects)).

### Step 2: Add the subjects

1. Go to **Subjects** and click **Add subject**.
2. Fill in:

| Field | Value |
|-------|-------|
| **Name** * | VC_M001 |
| **Projects** * | Select: Visual Cortex Population Dynamics Study |
| **Sex** * | Male |
| **Species** * | Select: Mus musculus |
| **Strain** | Select: C57BL/6J (only strains of the chosen species are listed) |
| **Status** * | Active |
| **Description** | Male C57BL/6J mouse for two-photon imaging of visual cortex. GCaMP6f expressed by viral injection. |
| **Genetic Line** | Wild type |
| **Birth Date** | 2024-06-15 |
| **Subject Identifier** | Ear punch: left ear, position 2 |

![The Add subject form filled in for VC_M001: name, project, sex, species Mus musculus with strain C57BL/6J, and status Active (the demo project stands in for the tutorial's).]({{site.baseurl}}/assets/images/screenshots/2p-add-subject.png)
{: .screenshot }
*The Add subject form filled in for VC_M001: name, project, sex, species Mus musculus with strain C57BL/6J, and status Active (the demo project stands in for the tutorial's).*

3. Repeat for VC_M002, VC_M003 and VC_M004, or open VC_M001 and click **Duplicate**: enter the new name, choose which procedures and logs to copy, click **Check copy** and then **Duplicate**. **Copy as a plan** marks the copies as planned, which suits animals that are not yet enrolled.

### Step 2b: Record housing and weight

Subject logs follow housing and health over time. Go to **Subject logs** (below Subjects) and click **Add subject log**.

**Housing log:**

| Field | Value |
|-------|-------|
| **Type** | Housing log |
| **Subject** | Select: VC_M001 |
| **Description** | Standard housing for the imaging cohort |

Type-specific details:

| Field | Value |
|-------|-------|
| **Start and end time** | 2024-07-01 08:00:00 (end time can stay empty) |
| **Location** | Animal Facility Room 105 |
| **Cage ID** | Cage_B3_single |
| **Cage type** | Standard mouse cage |
| **Light cycle** | 12:12 light-dark cycle (lights on 06:00) |
| **Enrichment** | Paper nesting material, plastic igloo |

**Monitoring log** (weight and condition):

| Field | Value |
|-------|-------|
| **Type** | Monitoring log |
| **Subject** | Select: VC_M001 |

Type-specific details:

| Field | Value |
|-------|-------|
| **Date and time** | 2024-07-01 09:00:00 |
| **Weight** | 24.5 g |
| **Body condition score (1-5)** | 3 - Ideal |
| **Health observations** | Pre-surgery baseline. Animal healthy and active. |

### Step 3: Create the cohort

1. Go to **Cohorts** (below Subjects) and click **Add cohort**.
2. Fill in:

| Field | Value |
|-------|-------|
| **Name** | VC_Imaging_Cohort_1 |
| **Project** | Select: Visual Cortex Population Dynamics Study |
| **Subjects** | Select: VC_M001, VC_M002, VC_M003, VC_M004 |
| **Description** | First cohort for the visual cortex imaging study. 4 male C57BL/6J mice, age-matched, viral GCaMP6f expression. Single housed after surgery, 12:12 light cycle, standard chow ad libitum. |
| **Tags** | visual-cortex, two-photon, gcamp6f |

### Step 4: Check the imaging setup

Open **Personal attributes** → **Equipment** and filter by your imaging setup. The sessions below refer to this equipment:

- the two-photon microscope (equipment type **Microscope**, linked to the hardware device from the catalog),
- the stimulus monitor (**Monitor**) and the computer that drives it (**Computer**),
- the eye tracking camera (**Camera**).

The surgical setup holds the stereotaxic frame (**Stereotaxic frame**) and the drill (**Surgical power tool**).

## Part B: Surgical Procedures

### Step 5: Virus injection

A procedure records the event with its type, date, coordinates, target regions and the **materials** it used.

1. Open subject VC_M001 and add a procedure from the subject page, or go to **Subjects** → **Procedures** → **Add procedure** → **Create blank**.
2. Fill in:

| Field | Value |
|-------|-------|
| **Type** * | Virus injection |
| **Subject** * | Select: VC_M001 |
| **Status** * | Performed |
| **Date and time of the procedure** | 2024-07-15 10:00:00 |
| **Equipment** | Select: Stereotaxic Frame (from the surgical setup) |
| **Protocol** | Select your injection protocol, if you keep one |
| **Atlas** | Allen Mouse Common Coordinate Framework |
| **Target regions** | Type to search and select the primary visual area (VISp) |
| **Coordinates** | Stereotaxic Bregma-Based Surface Coordinates with Depth |
| **Notes** | AAV injection for GCaMP6f expression in V1. Three weeks for expression before the window. |

Coordinate details:

| Field | Value |
|-------|-------|
| **AP coordinate** | -3.0 mm |
| **ML coordinate** | +2.5 mm |
| **Depth** | 0.3 mm (layer 2/3, from the brain surface) |
| **AP angle** | 0° |
| **ML angle** | 0° |

Click **View coordinates** to check the injection site in the Allen CCF before saving (see [Atlases and coordinates]({{site.baseurl}}/webinterface/atlases-and-coordinates/)). Record the second hemisphere as a second procedure.

3. Type-specific **Details**:

| Field | Value |
|-------|-------|
| **Injection volume** | 500 nL |
| **Injection rate** | 100 nL/min |
| **Injection profile** | Bolus injection |
| **Injection route** | Intraparenchymal |
| **Post-infusion dwell** | 5 min |

4. **Materials** tab: click **+ Add material** and add the rows the type takes.

| Material role | Material source | Value |
|---------------|-----------------|-------|
| **Viral-vector preparation** (required) | Consumable stock | Inventory *Viral Vectors*, stock *AAV1-syn-GCaMP6f* |
| **Vehicle** | Manual entry | Sterile PBS |

The row's details hold the **Applied volume** and the **Effective delivered titer** of this injection. Only stock with status Available or Reserved is offered; the row keeps a copy of the stock's details (catalog item, lot, dates), so the record stays readable if the inventory changes later.

![The Materials tab of a virus injection from the demo data: a viral-vector preparation (AAV-CAG-jGCaMP8f-WPRE from Addgene, a GCaMP indicator like the tutorial's GCaMP6f) from the inventory and the injection syringe.]({{site.baseurl}}/assets/images/screenshots/2p-virus-injection-materials.png)
{: .screenshot }
*The Materials tab of a virus injection from the demo data: a viral-vector preparation (AAV-CAG-jGCaMP8f-WPRE from Addgene, a GCaMP indicator like the tutorial's GCaMP6f) from the inventory and the injection syringe.*

5. Click **Save**. A virus injection creates no experimental interface; the expressed indicator is reached through the subject's procedure history.

{: .note }
> Anesthesia and analgesia are their own procedures (**Anesthesia** with the required **Anesthetic agent** material and the stages **Induction** and **Maintenance**; **Analgesic** with its **Active agent**). Group them with the injection in a **procedure episode** to record one perioperative event with severity and recovery outcome; see Step 5b of the [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow).

### Step 6: Cranial window

Three weeks later, record the window. Saving a **Cranial window** procedure also creates the **experimental interface** (the window) that the imaging acquisitions refer to.

1. Add a procedure on VC_M001 as in Step 5 and fill in:

| Field | Value |
|-------|-------|
| **Type** * | Cranial window |
| **Subject** * | Select: VC_M001 |
| **Status** * | Performed |
| **Date and time of the procedure** | 2024-08-05 09:00:00 |
| **Equipment** | Select: Stereotaxic Frame, Dental Drill |
| **Atlas** | Allen Mouse Common Coordinate Framework |
| **Target regions** | Primary visual area (VISp) |
| **Coordinates** | Stereotaxic Bregma-Based Surface Coordinates with Depth |
| **Notes** | 3 mm window over binocular V1, dura intact, sealed with a 3 mm glass coverslip. Head plate attached with dental cement. |

2. Type-specific **Details**:

| Field | Value |
|-------|-------|
| **Surgical method** | Craniotomy with dental drill, coverslip glued to the skull |
| **Shape of cranial window** | Circular |
| **Dimensions of cranial window** | 3 mm diameter, 0.15 mm thick |
| **Orientation of cranial window** | Centered on the injection site, parallel to the skull surface |

3. **Materials** tab:

| Material role | Material source | Value |
|---------------|-----------------|-------|
| **Cranial window** (required) | Consumable stock | Inventory *Surgical Supplies*, stock *Glass coverslip 3 mm* (an *Optical component* stock) |
| **Adhesive, cement, or sealant** | Consumable stock | *Dental cement* |
| **Surgical supply** | Manual entry | Gelfoam |

4. Click **Save**. The notice on the form announces that saving creates a *Cranial window* experimental interface from this procedure. Afterwards the interface *VC_M001 \| Cranial window* appears on the procedure's **Experimental interfaces** tab and under **Sessions** → **Experimental interfaces**, with persistence "Chronic / persistent". Edit the procedure, not the interface, to change its coordinates or the coverslip material; name, persistence, removal date and notes belong to the interface.

![The experimental interface a cranial window procedure created: subject, interface type, persistence, setup, equipment, atlas and target region.]({{site.baseurl}}/assets/images/screenshots/2p-cranial-window-interface.png)
{: .screenshot }
*The experimental interface a cranial window procedure created: subject, interface type, persistence, setup, equipment, atlas and target region.*

Record the head plate as a separate **Headpost** procedure (required material **Headpost**, details **Material**, **Shape**, **Construction method** and **Attachment method**). It creates a *Headpost* interface of its own.

{: .note }
> If you record a procedure before the surgery, set **Status** to *Planned*; the page shows an orange **Planned** pill and no interface is created yet. Click **Mark as performed** after the surgery; the interface is created at that point. See [Planning]({{site.baseurl}}/webinterface/planning/).

## Part C: Imaging Sessions

### Step 7: Habituation session

Start with head-fixation habituation, recorded as a session with a behavior and no imaging.

1. Create the behavioral assay once (**Personal attributes** → **Behavioral assays** → **Add behavioral assay**; see [Behavioral Assays]({{site.baseurl}}/tutorials/behavioral-assays)):

| Field | Value |
|-------|-------|
| **Behavioral assay name** | Head-fixation habituation |
| **Setup type** | Head-fixed passive platform (the setup type of your imaging setup) |
| **Behavioral paradigm** | Select the habituation paradigm, or add one under **Taxonomies** → **Behavioral paradigms** |
| **Authenticated groups** | Select your lab groups |
| **Description** | Habituation to head fixation under the microscope. 30-minute sessions with increasing duration, neutral gray screen, water rewards for calm behavior. |
| **Behavioral assay visibility** | Private |

2. Go to **Sessions** and click **Add session**:

| Field | Value |
|-------|-------|
| **Name** * | VC_M001_Day1_Habituation |
| **Session type** * | Subject |
| **Projects** * | Select: Visual Cortex Population Dynamics Study |
| **Subjects** | Select: VC_M001 |
| **Status** * | Performed |
| **Description** | Head-fixation habituation under the microscope, no imaging. |
| **Date and time onset** | 2024-08-19 14:00:00 |
| **Tags** | habituation, head-fixation |
| **Data storage** | Select: Imaging Server (see [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage)) |

3. On the **Behavior** tab add a behavior:

| Field | Value |
|-------|-------|
| **Subjects** | Select: VC_M001 |
| **Setup** | Select: your imaging setup |
| **Behavioral assay** | Select: Head-fixation habituation |

{: .note }
> Sessions have no setup, duration or behavioral assay fields of their own. The setup and assay are recorded on the behavior, and the assay must have the same setup type as the setup. A session can also be created as *Planned* and marked performed later.

### Step 8: Visual stimulation imaging session

The main session combines imaging, the stimulus log and eye tracking. Every data acquisition names the **experimental interface** the signal passed through, so first create the two interfaces that no procedure creates.

1. **Interfaces for the monitor and the eye camera** (once per subject). Go to **Sessions** → **Experimental interfaces** → **Add experimental interface**:

| Field | Visual display | Eye camera |
|-------|----------------|------------|
| **Name** * | VC_M001 visual display | VC_M001 eye camera |
| **Type** * | Visual stimulator | Camera |
| **Target type** | Subject | Subject |
| **Subject** | VC_M001 | VC_M001 |
| **Persistence** * | Chronic / persistent | Chronic / persistent |
| **Equipment** | Stimulus monitor | Eye tracking camera |
| **Details** | **Presentation device** Monitor, **Stimulus position** Contralateral, **Stimulation context** Passive | **View** Right eye, **Frame rate (Hz)** 60 |

Equipment-backed interface types take no materials. Reuse both interfaces in every session of this mouse.

2. Create the session:

| Field | Value |
|-------|-------|
| **Name** * | VC_M001_Day1_DriftingGratings |
| **Session type** * | Subject |
| **Projects** * | Select: Visual Cortex Population Dynamics Study |
| **Subjects** | Select: VC_M001 |
| **Status** * | Performed |
| **Description** | Two-photon calcium imaging during drifting gratings. 8 orientations (0° to 315° in 45° steps), 2 s stimulus, 4 s interval, 10 repeats each, randomized. Screen at 25 cm. |
| **Date and time onset** | 2024-08-20 15:00:00 |
| **Tags** | imaging, drifting-gratings |
| **Data storage** | Select: Imaging Server |
| **Name used in storage** | vc_m001_day1_gratings |

![The Add session form filled in for VC_M001_Day1_DriftingGratings: session type Subject, project, subject and status (the demo project and mouse M03 stand in for the tutorial's).]({{site.baseurl}}/assets/images/screenshots/2p-session-form.png)
{: .screenshot }
*The Add session form filled in for VC_M001_Day1_DriftingGratings: session type Subject, project, subject and status (the demo project and mouse M03 stand in for the tutorial's).*

3. On the **Data acquisition** tab add three acquisitions.

**Two-photon imaging:**

| Field | Value |
|-------|-------|
| **Type** * | Two-Photon Microscopy |
| **Experimental interfaces** * | Select: VC_M001 \| Cranial window |
| **Equipment** | Select: Two-photon microscope |
| **Notes** | Single plane in layer 2/3, 920 nm excitation for GCaMP6f. |

Type-specific details:

| Field | Value |
|-------|-------|
| **File name** | VC_M001_Day1_DriftingGratings_plane1.tif |
| **Format** | TIFF |
| **Compression** | LZW |
| **Vertical resolution** | 512 |
| **Horizontal resolution** | 512 |
| **Number of frames** | 46500 |
| **Frame rate** | 15.5 Hz |
| **Laser power** | 25 mW |
| **Excitation wavelength** | 920 nm |
| **Imaging depth** | 150 µm |
| **Voxel size (X dimension)** | 0.65 µm |
| **Voxel size (Y dimension)** | 0.65 µm |

**Stimulus log:**

| Field | Value |
|-------|-------|
| **Type** * | General time-series |
| **Experimental interfaces** * | Select: VC_M001 visual display |
| **Equipment** | Select: Stimulus computer |
| **Notes** | Stimulus timing and parameters, one row per frame. |

Type-specific details: **Format** CSV, **Data-type** float32, **Number of channels** 3, **Sampling rate** 60 Hz, **Number of samples** 108000.

**Eye tracking:**

| Field | Value |
|-------|-------|
| **Type** * | Video Tracking |
| **Experimental interfaces** * | Select: VC_M001 eye camera |
| **Equipment** | Select: Eye tracking camera |
| **Notes** | Pupil tracking during stimulation. |

Type-specific details: **Format** AVI, **Compression** H.264, **Frame rate** 60 Hz, **Number of frames** 108000, **Vertical resolution** 480, **Horizontal resolution** 640.

{: .note }
> The **Experimental interfaces** field is required and only offers interfaces of subjects in the session's projects. Acquisitions refer to the cranial window interface, not to the procedure; the virus injection is found through the subject.

![The Data acquisition tab of a two-photon session: a Video Tracking entry and, second, a Two-Photon Microscopy entry recorded through the cranial window interface]({{site.baseurl}}/assets/images/screenshots/2p-data-acquisition-tab.png)
{: .screenshot }
*The Data acquisition tab of a two-photon session from the demo data (SAMPLE M03 Mirabel - Acquisition 01): a Video Tracking entry and, below it, the session's second data acquisition, a Two-Photon Microscopy entry recorded through the cranial window interface. Your gratings session lists the entries you added.*

4. On the **Epochs** tab add the epochs and drag the acquisitions from **Link to epochs** onto them:

| Epoch name | Start | End | Description |
|------------|-------|-----|-------------|
| **Baseline** | 00:00:00 | 00:05:00 | Gray screen |
| **Stimulus_presentation** | 00:05:00 | 00:30:00 | Drifting gratings, 8 orientations × 10 repeats |
| **Post_stimulus** | 00:30:00 | 00:35:00 | Gray screen |

**Start** and **End** are relative to the session onset (hh:mm:ss or seconds). A data acquisition can belong to one epoch only; the session's **Timeline** shows the result.

### Step 9: Retinotopy session

Repeat Step 8 for a mapping session; the interfaces already exist.

| Field | Value |
|-------|-------|
| **Name** * | VC_M001_Day2_RetinotopyMapping |
| **Session type** * | Subject |
| **Projects** * | Select: Visual Cortex Population Dynamics Study |
| **Subjects** | Select: VC_M001 |
| **Status** * | Performed |
| **Description** | Retinotopic mapping with moving bars: white bars on black, 4 directions, 2° width, 0.5°/s, full-screen sweeps. |
| **Date and time onset** | 2024-08-21 15:30:00 |
| **Tags** | retinotopy, mapping |
| **Data storage** | Select: Imaging Server |

Add the **Two-Photon Microscopy** acquisition on *VC_M001 \| Cranial window* with the same imaging details as Day 1 (**Number of frames** 31000, **Laser power** 28 mW), and the stimulus log on *VC_M001 visual display*.

### Step 10: Multi-plane session

Create a third session, *VC_M001_Day3_MultiPlane*, as in Step 8. Imaging at two depths is recorded as two **Two-Photon Microscopy** acquisitions on the same interface, one per plane:

| Field | Plane 1 | Plane 2 |
|-------|---------|---------|
| **File name** | VC_M001_Day3_plane1.tif | VC_M001_Day3_plane2.tif |
| **Imaging depth** | 150 µm | 250 µm |
| **Laser power** | 25 mW | 35 mW |
| **Notes** | Layer 2/3 | Layer 4, higher power for depth |

The remaining details (resolution, frame rate, wavelength, voxel size) are the same as in Step 8. Save the first acquisition as a template with **Create Template** and use **Create from template** for the second; only the depth, power and file name change.

### Step 11: Optogenetic manipulation (optional)

For imaging combined with optogenetics, add a **Manipulation** to the session:

| Field | Value |
|-------|-------|
| **Type** * | Optogenetic stimulation |
| **Experimental interfaces** * | Select: VC_M001 \| Optic fiber implant |
| **Equipment** | Select: Blue LED system |
| **Notes** | ChR2 activation during stimulus presentation. |

Type-specific details (a table with one row per stimulation pattern):

| Field | Value |
|-------|-------|
| **Power** | 5 mW |
| **Profile** | Square |
| **Duration** | 2 s |
| **Duty cycle** | 0.5 |
| **Repetitions** | 20 |
| **Wavelength** | 473 nm |
| **Closed loop** | Unchecked |

{: .note }
> Manipulations link to experimental interfaces, not procedures. The optic fiber interface comes from an **Optic fiber implant** procedure (required material **Implanted optic fiber**) and the ChR2 virus from a second **Virus injection**, both recorded as in Steps 5 and 6.

## Part D: Health and Organization

### Step 12: Welfare checks

After the surgeries and after each imaging day, add a subject log of type **Welfare check** on VC_M001:

| Field | Value |
|-------|-------|
| **Date and time** | 2024-08-20 18:00:00 |
| **Condition & demeanour (0-4)** | 0 - Bright, alert, responsive (normal) |
| **Procedure / wound site type** | Implant site (headcap, connector, electrode, fibre…) |
| **Site observation** | Window clear, head plate firm, no inflammation. |
| **Actions taken** | None |

Welfare checks and monitoring logs can also be added from a procedure episode page, with a **Phase** such as *Recovery* or *Follow-up*.

### Step 13: Create the collection

Go to **Collections** (below Sessions) and click **Add collection**:

| Field | Value |
|-------|-------|
| **Name** | VC_M001_Orientation_Tuning_Week1 |
| **Project** | Select: Visual Cortex Population Dynamics Study |
| **Sessions** | Select: VC_M001_Day1_DriftingGratings, VC_M001_Day2_RetinotopyMapping, VC_M001_Day3_MultiPlane |
| **Description** | First week of orientation tuning and retinotopy for VC_M001: single-plane and two-plane imaging with drifting gratings and moving bars. |
| **Tags** | orientation-tuning, retinotopy, week1 |

### Step 14: Load the imaging records from the API

With the [Python API tool]({{site.baseurl}}/tools/python-api-tool/):

```python
from brainstem_api_tools import BrainstemClient

client = BrainstemClient()

# Step 1: Resolve the project name to its id
projects = client.load('project',
                       filters={'name': 'Visual Cortex Population Dynamics Study'}).json()
project_id = projects['projects'][0]['id']

# Step 2: Every session of the project
sessions = client.load('session', filters={'projects': project_id},
                       load_all=True)['sessions']
session_ids = [s['id'] for s in sessions]

# Step 3: The two-photon acquisitions per session, with the interfaces they used
imaging = []
for sid in session_ids:
    resp = client.load('dataacquisition',
                       filters={'session': sid, 'type': 'TwoPhotonMicroscopy'},
                       include=['interfaces']).json()
    imaging.extend(resp.get('data_acquisitions', []))

# Step 4: The cranial window interfaces and the procedures that created them
windows = client.load('experimentalinterface',
                      filters={'type': 'CranialWindow'}, load_all=True)['experimentalinterfaces']

# Export the whole project (format 2.1 JSON) for NWB conversion
export = client.export_project(project_id)
```

Planned sessions and procedures are left out of API lists unless you filter on `status`, for example `client.load('session', filters={'status': 'planned'})`.

## Next steps

- **Probe implants instead of windows**: the [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow) records a silicon probe implant with the same procedure, interface and session records.
- **Data files**: link the sessions to the imaging server and build file paths from the API with [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage).
- **Data model**: [Procedures]({{site.baseurl}}/datamodel/modules/procedure/), [Experimental interfaces]({{site.baseurl}}/datamodel/modules/experimentalinterface/), [Data acquisition]({{site.baseurl}}/datamodel/modules/dataacquisition/) and the [data acquisition types]({{site.baseurl}}/datamodel/schemas/dataacquisition/) with every field of **Two-Photon Microscopy**.
- **Scripting**: the [Python API tool]({{site.baseurl}}/tools/python-api-tool/) and [MATLAB API tool]({{site.baseurl}}/tools/matlab-api-tool/).
- **Share**: make the project and the behavioral assay public with [Share data publicly]({{site.baseurl}}/tutorials/sharing-project-publicly).
- **Export to NWB**: [Exporting to NWB]({{site.baseurl}}/tutorials/exporting-to-nwb) writes the cranial window, the virus injection and the imaging acquisitions as metadata.
