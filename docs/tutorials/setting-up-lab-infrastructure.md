---
layout: default
title: Lab Infrastructure
parent: Tutorials
nav_order: 4
---

# Setting Up Lab Infrastructure in BrainSTEM
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Before conducting experiments in BrainSTEM, we recommend you establish your lab's infrastructure. This tutorial covers creating and configuring the foundational elements that support your research workflows: **setups** with **equipment** and **inventories** with **consumable stocks**. Proper infrastructure setup ensures smooth experiment creation and maintains consistency across your lab.

## Understanding Lab Infrastructure Components

BrainSTEM's lab infrastructure consists of four interconnected components:

1. **Setups**: Physical experimental environments (behavioral setup, recording rigs, surgical stations)
2. **Equipment**: Hardware devices used in your setups
3. **Inventories**: Organizational systems for tracking lab resources
4. **Consumable Stocks**: Specific items and materials in your inventories

These components work together to provide the foundation for documenting procedures, behaviors, data acquisition, and manipulations.

## Behavioral Assays

Behavioral Assays are standardized experimental protocols (such as T-maze alternation, open field exploration, etc.) that are performed within a specific setup environment. In BrainSTEM, these are managed under *Personal Attributes → Behavioral Assays*.

For detailed instructions on creating, managing, and best practices for behavioral assays, see the dedicated tutorial: [Behavioral Assays]({{site.baseurl}}/tutorials/behavioral-assays).

{: .note }
> When planning your infrastructure, ensure that your setups have the correct **Setup type** for the behavioral assays you intend to use: a behavior can only combine a setup and an assay of the same setup type.

## Planning Your Infrastructure

### Before You Begin
{: .no_toc}

1. **Audit your physical spaces**: List experimental environments in your lab
2. **Inventory your equipment**: Document devices, instruments, and tools
3. **Catalog your supplies**: Identify consumables, probes, drugs, and other materials
4. **Define access permissions**: Determine which group members need access to what resources

### Infrastructure Hierarchy
{: .no_toc}

Understanding the relationships between components:

```
Setup (Physical Environment)
├── Equipment (Devices in that environment)
│   ├── Hardware device or consumable from the shared catalogs (the model)
│   └── Coordinates system (for positioning)
└── Used by → Procedures, Behaviors, Data acquisition, Manipulations

Inventory (Storage/Organization System)
└── Consumable stocks (your lots and batches of a catalog consumable)
    └── Used as → Material rows of procedures, specimen procedures and experimental interfaces
```

Consumables and hardware devices are shared catalogs maintained by all users (see [Submit Resources & Taxonomies]({{site.baseurl}}/tutorials/submit-resource-and-taxonomies)). Your setups, equipment, inventories and stocks are yours.

## Creating Setups

Setups represent your physical experimental environments. Each setup corresponds to a specific location or configuration where experiments are conducted.

### Step 1: Navigate to Setups
{: .no_toc}

1. Go to **Personal Attributes** → **Setups** in the left navigation menu
2. Click the **Add setup** button

![A setup's form: name, setup category and type, location, visibility, description, image and specifications; its equipment is a separate tab.]({{site.baseurl}}/assets/images/screenshots/setup-form.png)
{: .screenshot }
*A setup's form: name, setup category and type, location, visibility, description, image and specifications; its equipment is a separate tab.*

### Step 2: Configure Basic Setup Information
{: .no_toc}

**Fill in the essential details:**

| Field | Instructions |
|-------|-------------|
| **Name** | Use descriptive, standardized names (e.g., "Behavior Room A", "Surgery Station 1", "2P Imaging Rig", "Head-fixed Linear Track") |
| **Setup type** | Select appropriate category: Behavioral environments (T-maze, Open field, Barnes maze, Linear track), Recording environments (Head-fixed disc, Homecage, Custom rigs), or Surgical environments (Surgical table) |
| **Authenticated groups** | Select groups that should have access to this setup |
| **Location** | The room or building where the setup stands |
| **Setup visibility** | **Private** (default) or **Public** |
| **Description** | Provide comprehensive details including: Physical location (room number, building), Setup purpose and capabilities, Special requirements or restrictions, Contact person for technical issues |

### Step 3: Define Specifications
{: .no_toc}

Add relevant specifications for your setup. Specifications can be a string or a number. Common examples:

**Behavioral mazes**: Arm lengths, corridor widths, platform sizes  
**Recording rigs**: Stage dimensions, working distances  
**Surgical stations**: Table dimensions, reach distances

**Example specification:**

| Dimension | Value |
|-----------|-------|
| **Length** | "20 cm" |
| **Width** | "50 cm" |

### Step 4: Setup Example
{: .no_toc}

#### Behavioral Setup: "T-maze Behavior Room"
{: .no_toc}

| Field | Value |
|-------|-------|
| **Name** | T-maze Behavior Room |
| **Setup type** | T-maze |
| **Description** | Behavioral testing room with automated T-maze system for spatial memory tasks. Located in Room 302B, Neuroscience Building |
| **Setup visibility** | Private |
| **Specifications** | ArmLength: "45 cm", StemLength: "50 cm", CorridorWidth: "10 cm" |

{: .note }
> Use consistent naming conventions across your lab. This makes setups easier to find and select during experiment creation.

## Adding Equipment to Setups

Equipment represents the devices and instruments within your setups. Each piece of equipment belongs to a specific setup and can be used in procedures, data acquisition, and manipulations.

### Step 1: Navigate to Equipment
{: .no_toc}

1. Go to **Personal attributes** → **Equipment**
2. Click the **Add equipment** button

![An equipment entry's form: an amplifier in a setup, with its hardware device, date and coordinates.]({{site.baseurl}}/assets/images/screenshots/equipment-form.png)
{: .screenshot }
*An equipment entry's form: an amplifier in a setup, with its hardware device, date and coordinates.*

### Step 2: Configure Equipment Basics
{: .no_toc}

| Field | Instructions |
|-------|-------------|
| **Name** | Use specific, identifiable names (Good: "Intan RHD2000 #1", "Behavior Camera Main", "LED Driver Ch1-4"; Avoid: "Recording device", "Camera", "Light") |
| **Type** | The equipment type (data acquisition system, camera, laser, stereotaxic frame, ...) |
| **Setup** | Select the setup where this equipment is located |
| **Hardware device** or **Consumable** | Link the catalog entry that describes the model: a **hardware device** for instruments (amplifiers, cameras, microscopes) or a **consumable** for device-like items kept in the catalog (for example an optic fiber design or an electrode component). Use one of the two. |
| **Coordinates** | How this equipment's position is described; the default is "External XYZ Coordinates with Euler Orientation" |

### Step 3: Common Equipment Types
{: .no_toc}

**Data Acquisition**: Recording systems (Intan, Plexon), imaging systems (two-photon microscopes, miniscopes), behavioral cameras, motion tracking systems

**Stimulation**: Optogenetic systems (LED drivers, lasers), electrical stimulation equipment (stimulus isolators, function generators)

**Surgical**: Stereotaxic systems, micromanipulators, injection pumps, drill systems

### Step 4: Equipment Configuration Example
{: .no_toc}

| Field | Value |
|-------|-------|
| **Name** | Intan RHD2000 System #1 |
| **Type** | Data acquisition system |
| **Setup** | Select: Open Field Arena |
| **Hardware device** | Intan RHD2000 USB interface board |

{: .important }
> Link equipment to the matching hardware device in the shared catalog. If your model isn't there, add it with **Lookup RRID** (see [Submit Resources & Taxonomies]({{site.baseurl}}/tutorials/submit-resource-and-taxonomies)); you can use your pending entry right away.

## Setting Up Inventories

Inventories help organize and track consumable resources in your lab. They provide structure for managing supplies and ensure proper accounting of materials used in experiments.

### Step 1: Create Inventory Categories
{: .no_toc}

Navigate to **Personal Attributes** → **Inventories** and create logical groupings:

#### Common Inventory Categories
{: .no_toc}

Organize inventories by material type (Neural Probes, Viral Vectors, Pharmacological Agents), storage location (Freezer -80°C, Refrigerator 4°C), or experiment type (Electrophysiology Supplies, Optogenetics Materials).

### Step 2: Configure Inventory Details
{: .no_toc}

**For each inventory:**

| Field | Instructions |
|-------|-------------|
| **Name** | Clear, descriptive identification (Examples: "Silicon Probe Storage", "AAV Virus Stocks", "Behavioral Supplies RT") |
| **Description** | Include important details: Physical location and access requirements, Storage conditions and handling notes, Responsible person or contact, Special safety considerations |
| **Authenticated groups** | Groups that can access and modify this inventory |
| **Visibility** | Usually left on **Private** for lab inventories |

### Step 3: Inventory Setup Example
{: .no_toc}

| Field | Value |
|-------|-------|
| **Name** | Neural Electrode Inventory |
| **Description** | Storage for all neural recording electrodes and probes. Located in Room 302, Cabinet B. Handle with anti-static precautions. Contact: Lab Manager for restocking. |
| **Authenticated groups** | Electrophysiology Team, Lab Managers |

## Adding Consumable Stocks

Consumable stocks are the specific items within your inventories. These are the actual materials that get used in procedures and need to be tracked for experimental documentation.

### Step 1: Navigate to Consumable Stocks
{: .no_toc}

1. Go to **Personal attributes** → **Consumable stocks**
2. Click **Add consumable stock**

![A consumable stock entry's form: a NeuroNexus silicon probe (A1x32-6mm-50-177) in stock, with its inventory, dates, status, storage and the type-specific details.]({{site.baseurl}}/assets/images/screenshots/consumable-stock-form.png)
{: .screenshot }
*A consumable stock entry's form: a NeuroNexus silicon probe (A1x32-6mm-50-177) in stock, with its inventory, dates, status, storage and the type-specific details.*

### Step 2: Configure Stock Information
{: .no_toc}

| Field Category | Field | Description |
|----------------|--------|-------------|
| **Basic Information** | Type | The stock type (Silicon probe, Virus solution, Pharmacological agent, Antibody or immunoreagent, ...). It mirrors the consumable catalog types. |
| | Inventory | Select the appropriate inventory |
| | Consumable | The catalog entry this stock is a lot of. The list is limited to consumables of the matching type; filter by **Supplier** first, or add a missing consumable with the **+** button |
| | Status | Availability of the lot (see below) |
| **Tracking Details** | Acquisition date | When the lot arrived |
| | Expiration date | If applicable; the status switches to Expired automatically after this date |
| | Cost | For budget tracking and planning |
| **Storage Information** | Storage location | Specific location within the inventory |
| | Storage conditions | Temperature, humidity, special requirements |
| **Usage Information** | Intended use | Specific experimental applications |
| | Notes | Special handling, preparation, or usage instructions |
| **Details** | Type-specific fields | Lot number, concentration, titer, and other properties of this lot as received |

**Status values**: Available, In use, Reserved, Depleted, Used, Failed/Broken, Expired, Maintenance, Discontinued, Unknown. Only stock that is **Available** or **Reserved** is offered when a procedure records a material. Quantities are not decremented automatically; update the status by hand when a lot is used up. The stock page lists where the lot was used ("Used in", "Material type", "Use details").

### Step 3: Consumable Stock Example
{: .no_toc}

| Field | Value |
|-------|-------|
| **Type** | Silicon probe |
| **Inventory** | Select: Neural Electrode Inventory |
| **Supplier** | NeuroNexus (optional filter) |
| **Consumable** | NeuroNexus A1x32-Poly2 (a *Silicon probe design* from the catalog) |
| **Status** | Available |
| **Acquisition date** | 2024-01-15 |
| **Storage location** | Cabinet B, Slot 15, Anti-static tube #A1x32-15 |
| **Storage conditions** | Room temperature, anti-static protection |
| **Intended use** | Chronic hippocampal recordings in behaving mice |
| **Cost** | $1,200 |
| **Notes** | Pre-cleaned with 70% ethanol. Handle with non-magnetic forceps only. Sterilize with EtO gas before implantation. |

### Picking a probe design from the catalog
{: .no_toc}

Silicon probe and ECoG array designs are imported from vendor catalogs (NeuroNexus, ATLAS Neuroengineering, Cambridge Neurotech, IMEC Neuropixels; Blackrock Neurotech, NeuroNexus, PMT Corporation and others for ECoG). Open **Resources** → **Consumables**, filter by **Consumable type** "Silicon probe design" and supplier, and check the **Probe schematic** on the design's page: it shows the shank layout and site positions drawn from the catalog geometry. The same geometry draws the shanks in the coordinate viewer once the probe is implanted. See [Probe catalog]({{site.baseurl}}/webinterface/probe-catalog/).

### Keeping an eye on stock
{: .no_toc}

The dashboard widgets **Inventory status** and **Expiring stock** (next 30 days) summarize your inventories. Add them with **Add widget** → **Manage widgets**.

## Templates for Repeated Configurations

Procedures, specimen procedures, experimental interfaces, data acquisitions, manipulations and procedure episodes can be saved as **templates**, and so can single material rows.

1. Open the record you want to reuse and click **Create Template** on its details page (or **Save as material template** on a material card).
2. Give the template a name and, optionally, share it with projects; otherwise it stays personal. Templates shared with a public project are public.
3. Next time, choose **Add ...** → **Create from template** in the list, or **Use template** inside a form. The template fills type, details, coordinates, equipment, target regions, stages and materials; subject, date and stock lots are left for you.

Manage all templates under **Tools** → **Templates**. Stock-backed material rows become catalog rows in a template, so the lot is chosen again at use.

## Permission Management

Proper permission management ensures that the right people have access to the right resources while maintaining security and organization.

BrainSTEM infrastructure uses four permission levels for setups and inventories and thereby inherited to equipment and consumable stocks:

| Permission Level | Capabilities |
|-----------------|-------------|
| **Members** | View details<br>Read-only access<br>**Cannot** modify or create infrastructure |
| **Contributors** | All Member permissions<br>Create and modify associated equipment and consumable stocks. <br>Select setups and equipment when creating experiments<br>Select inventory and consumable stocks when creating experiments<br>**Cannot** modify setup settings or manage permissions |
| **Managers** | All Contributor permissions<br>Manage permissions for others<br>Configure setup specifications<br>**Cannot** delete infrastructure or transfer ownership |
| **Owners** | All Manager permissions<br>Full control over setups and equipment<br>Delete infrastructure components<br>Transfer ownership to other users<br>Complete administrative control |

Permissions are set on the setup or inventory with **Manage** on its details page, in the same way as for projects (see [Manage Projects]({{site.baseurl}}/tutorials/managing-projects) and the [permissions page]({{site.baseurl}}/datamodel/permissions/)). The groups you select in **Authenticated groups** when creating the entry get Contributor access.

## Naming Conventions

- **Setups**: Include location and be specific (e.g., "Room302_TmazeBehavior", "HeadFixed_2P_VR")
- **Equipment**: Include model and serial number (e.g., "IntanRHD2000_SN1234")
- **Inventories**: Include storage info (e.g., "Probes_RoomTemp", "Viruses_Minus80")
- **Consumable Stocks**: Include lot numbers and concentrations where applicable

## Integration with Experimental Workflows

### Using Infrastructure in Procedures
{: .no_toc}

When creating procedures, your infrastructure components become available:
- **Equipment** specifies tools used (stereotaxic frames, injection systems); the setup follows from the equipment
- **Consumable stocks** are selected as the **Material source** of a material row (probes, viruses, drugs). Each procedure type declares which material roles it takes and which are required; the row keeps a copy of the stock's details (catalog item, lot, dates, storage location), so the record stays readable if the inventory changes
- An **implant** procedure turns its device material into an **experimental interface** that sessions refer to

### Using Infrastructure in Sessions
{: .no_toc}

Your setup determines available:
- **Equipment** for data acquisition and manipulation modules
- **Behavioral assays** compatible with the setup type

Data acquisitions and manipulations also name the **experimental interface** the signal passed through: an implanted device, or an interface you create for a camera or stimulator and reuse across sessions.

## Troubleshooting

**Setup not available**: Verify your group permissions on the setup, and that the setup and the behavioral assay have the same **Setup type**

**Equipment missing from dropdowns**: Confirm correct setup assignment, equipment type alignment, and permission matching

**Consumable stock access issues**: Check group membership and owner/manager permissions

## Next Steps

With your lab infrastructure in place, you're ready to move on to experimental workflows:

- **Start with experimental design**: Learn about [Behavioral Assays]({{site.baseurl}}/tutorials/behavioral-assays) to define standardized experimental protocols that use your setups
- **Set up data management**: Configure [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage) to link your metadata to actual data files stored on your systems
- **Organize team access**: Set up [Managing Groups]({{site.baseurl}}/tutorials/managing-groups) and [Managing Projects]({{site.baseurl}}/tutorials/managing-projects) to properly organize team access to your infrastructure
- **Explore complete workflows**: Follow the [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow) or [Two-Photon Imaging Workflow]({{site.baseurl}}/tutorials/two-photon-imaging-workflow) tutorial for end-to-end experimental documentation
- **Contribute to the platform**: Use [Submit Resources & Taxonomies]({{site.baseurl}}/tutorials/submit-resource-and-taxonomies) to add any missing hardware devices or consumables to the BrainSTEM catalogs
- **Go ex vivo**: The [Ex vivo workflow]({{site.baseurl}}/tutorials/specimen-workflow) uses the same stocks (fixatives, antibodies) as material rows of specimen procedures
