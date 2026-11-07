---
layout: default
title: Lab Infrastructure
parent: Tutorials
nav_order: 3
---

# Setting Up Lab Infrastructure in BrainSTEM
{: .no_toc}

This tutorial creates the lab infrastructure that the [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow) uses: three **setups** (Theta Maze Rig, Sleep Recording Box, Surgical Station), the **equipment** in them, and an **inventory** with a **consumable stock** of Neuropixels 2.0 probes. At the end, every procedure, behavior and data acquisition you document can select these entries instead of describing the rig and the probe again.

**Prerequisites**: an account in a lab group (see [Manage Groups]({{site.baseurl}}/tutorials/managing-groups)).

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## How the pieces fit together

A **setup** is a place where experiments run, and its **equipment** is the devices installed in it:

[![A setup is built as a setup type and holds its equipment, and each piece of equipment can name its model in the shared catalog. Procedures, specimen procedures, experimental interfaces, data acquisitions and manipulations name the equipment they used; a behavior names the whole setup.]({{site.baseurl}}/assets/images/diagrams/setup-hub-setup.svg)]({{site.baseurl}}/assets/images/diagrams/setup-hub-setup.svg)
*A setup is built as a setup type and holds its equipment, and each piece of equipment can name its model in the shared catalog. Procedures, specimen procedures, experimental interfaces, data acquisitions and manipulations name the equipment they used; a behavior names the whole setup.*

An **inventory** is where your lab keeps materials, and a **consumable stock** is one lot of a catalog consumable in it. Procedures, specimen procedures and experimental interfaces use stock in their material rows:

[![A material usage row records what was actually applied; it points at a lot in your inventory, at the shared catalog entry, or at a manual entry, and sits on a procedure, specimen procedure or experimental interface.]({{site.baseurl}}/assets/images/diagrams/material-chain.svg)]({{site.baseurl}}/assets/images/diagrams/material-chain.svg)
*A material usage row records what was actually applied; it points at a lot in your inventory, at the shared catalog entry, or at a manual entry, and sits on a procedure, specimen procedure or experimental interface.*

A setup has a **setup type** (Theta maze, Sleepbox, Surgical table, ...). A [behavioral assay]({{site.baseurl}}/tutorials/behavioral-assays) has one too.

{: .important }
> A session's behavior can only combine a setup and a behavioral assay of the same setup type. Give the assay the setup type of the rig it runs on, or the behavior form refuses the pair.

Equipment and stock point to entries of the shared catalogs: a **hardware device** or a **consumable**. The catalogs are maintained by all users (see [Resources & Taxonomies]({{site.baseurl}}/tutorials/submit-resource-and-taxonomies)); your setups, equipment, inventories and stock are your lab's own.

## Step 1: Create the setups

![A setup's form: name, setup category and type, location, visibility, description, image and specifications; its equipment is a separate tab.]({{site.baseurl}}/assets/images/screenshots/setup-form.png)
{: .screenshot }
*A setup's form: name, setup category and type, location, visibility, description, image and specifications; its equipment is a separate tab.*

1. Go to **Personal attributes** → **Setups** and click **Add setup**.
2. Enter the **Setup name** "Theta Maze Rig".
3. Select the **Setup category** "Freely Moving Awake". The **Setup type** list stays disabled until a category is selected, and then lists only the setup types of that category.
4. Select the **Setup type** "Theta maze".
5. In **Authenticated groups**, select your lab group. The groups you select get Contributor access to the setup.
6. Click **Save**. The setup's edit page opens. Fill in the **Location** (for example "Room 302B, Neuroscience Building"), a **Description** and, under **Specifications**, the dimensions of the maze (for example "Arm length" "45 cm"). Leave **Setup visibility** on **Private** and click **Save**.

Repeat for the other two setups:

| Setup name | Setup category | Setup type |
|------------|----------------|------------|
| Theta Maze Rig | Freely Moving Awake | Theta maze |
| Sleep Recording Box | Freely Moving Awake | Sleepbox |
| Surgical Station | Anesthetized In Vivo | Surgical table |

The setup categories are In Vitro, Ex Vivo, Anesthetized In Vivo, Head-Fixed Awake, Restrained Awake, Freely Moving Awake and Unknown. The setup types of each category are listed on the [Setup types]({{site.baseurl}}/datamodel/taxonomies/setuptype/) page. If yours is missing, add it under **Taxonomies** → **Setup types** (see [Resources & Taxonomies]({{site.baseurl}}/tutorials/submit-resource-and-taxonomies)). All setup fields are described on the [Setups]({{site.baseurl}}/datamodel/personal_attributes/setup/) page.

## Step 2: Add equipment to the setups

![An equipment entry's form: an amplifier in a setup, with its hardware device, date and coordinates.]({{site.baseurl}}/assets/images/screenshots/equipment-form.png)
{: .screenshot }
*An equipment entry's form: an amplifier in a setup, with its hardware device, date and coordinates.*

1. Go to **Personal attributes** → **Setups** → **Equipment** and click **Add equipment**.
2. Enter the **Equipment name** "Neuropixels System", select the **Type of equipment** "Data acquisition system" and the **Setup** "Theta Maze Rig".
3. Select the device's catalog entry: a **Hardware device supplier** and then its **Hardware device**. For a device-like catalog consumable (an optic fiber design, for example), select the **Supplier** and **Consumable** instead.
4. Click **Save**.

Add the rest of the equipment the same way:

| Equipment name | Type of equipment | Setup |
|----------------|-------------------|-------|
| Neuropixels System | Data acquisition system | Theta Maze Rig |
| OptiTrack System | Motion tracking system | Theta Maze Rig |
| Neuropixels System | Data acquisition system | Sleep Recording Box |
| Sleep Box Camera | Camera | Sleep Recording Box |
| Stereotaxic Frame | Stereotaxic frame | Surgical Station |

An equipment entry belongs to one setup, so a recording system used in two setups gets one entry in each. All equipment fields, including the coordinates, are described on the [Equipment]({{site.baseurl}}/datamodel/modules/equipment/) page.

If your device is not in the catalog, add it under **Resources** → **Hardware devices** with **Lookup RRID** (see [Resources & Taxonomies]({{site.baseurl}}/tutorials/submit-resource-and-taxonomies)). You can select your pending entry right away.

## Step 3: Create an inventory

1. Go to **Personal attributes** → **Inventories** and click **Add inventory**.
2. Enter the **Inventory name** "Neural Electrode Inventory" and select your lab group in **Authenticated groups**.
3. Click **Save**. On the edit page, fill in the **Location** (for example "Room 302, Cabinet B") and a **Description** with the storage and handling notes. Leave **Inventory visibility** on **Private** and click **Save**.

Field definitions are on the [Inventories]({{site.baseurl}}/datamodel/personal_attributes/inventory/) page.

## Step 4: Add a consumable stock

![A consumable stock entry's form (here a NeuroNexus silicon probe from the demo data): inventory, dates, status, storage and the type-specific details.]({{site.baseurl}}/assets/images/screenshots/consumable-stock-form.png)
{: .screenshot }
*A consumable stock entry's form (here a NeuroNexus silicon probe from the demo data): inventory, dates, status, storage and the type-specific details.*

1. Go to **Personal attributes** → **Inventories** → **Consumable stocks** and click **Add consumable stock**.
2. Select the **Type of consumable stock** "Silicon probe" and the **Inventory** "Neural Electrode Inventory".
3. Select the **Consumable supplier** "IMEC" and then the **Consumable**, for example "Neuropixels 2.0 multishank probe (NP2013)". The list offers only consumables that match the stock type. Before choosing, you can check the probe's shank layout in the [Probe catalog]({{site.baseurl}}/webinterface/probe-catalog/).
4. Leave **Status** on **Available**, add the **Acquisition date** and **Storage location** if you track them, and click **Save**.

The stock is listed as "Silicon probe : Neuropixels 2.0 multishank probe (NP2013) - IMEC". The Electrophysiology Workflow calls it the Neuropixels 2.0 probe stock. All stock fields and the status values are described on the [Consumable stocks]({{site.baseurl}}/datamodel/modules/consumablestock/) page.

{: .important }
> Only stock with the status **Available** or **Reserved** is offered when a procedure records a material. BrainSTEM does not count stock down: set the status by hand when a lot is used up.

The dashboard widgets **Inventory status** and **Expiring stock** summarize your inventories; add them on the dashboard with **Add widget** (see [Dashboard]({{site.baseurl}}/webinterface/dashboard/)).

## End state

You now have three setups with their equipment, and an inventory holding one Neuropixels 2.0 probe stock. They appear in the **Setup**, **Equipment** and **Material source** lists of the forms where you document procedures and sessions:

- A procedure selects **Equipment** (the Stereotaxic Frame) and takes stock as the **Material source** of a material row. An implant procedure turns its device material into an **experimental interface** that sessions refer to.
- A session's behavior selects a setup and a behavioral assay of the same setup type. Its data acquisitions and manipulations select equipment and an experimental interface.

## Sharing access

The groups selected in **Authenticated groups** get Contributor access. To give other users or groups access, open the setup or inventory and click **Manage**; you need Manager on it. Equipment follows its setup and consumable stock follows its inventory. See [Permissions]({{site.baseurl}}/datamodel/permissions/#personal-attribute-permissions).

## Naming conventions

- **Setups**: the place and the task, for example "Theta Maze Rig" or "Room302 Sleep Box".
- **Equipment**: the device, with a serial number when you have several, for example "Neuropixels System SN1234".
- **Inventories**: what is stored and where, for example "Viruses -80 °C".

## Troubleshooting

**Setup missing in a behavior**: check that you have at least Contributor access to the setup, and that the setup and the behavioral assay have the same **Setup type**.

**Setup type list is empty**: select a **Setup category** first; the list shows only the types of that category.

**Equipment missing in a dropdown**: check that it belongs to the setup you expect and that you have access to that setup.

**Stock missing as a material source**: check its **Status** (only Available and Reserved are offered) and your access to its inventory.

## Next steps

- **Next:** [Behavioral Assays]({{site.baseurl}}/tutorials/behavioral-assays): create the theta-maze alternation assay that runs on the Theta Maze Rig.
- [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage): describe where the recordings are stored.
- Data model: [Setups]({{site.baseurl}}/datamodel/personal_attributes/setup/), [Equipment]({{site.baseurl}}/datamodel/modules/equipment/), [Inventories]({{site.baseurl}}/datamodel/personal_attributes/inventory/), [Consumable stocks]({{site.baseurl}}/datamodel/modules/consumablestock/) and [Templates]({{site.baseurl}}/datamodel/modules/templates/) for repeated procedures.
- [Ex vivo workflow]({{site.baseurl}}/tutorials/specimen-workflow): uses stock (fixatives, antibodies) as material rows of specimen procedures.
