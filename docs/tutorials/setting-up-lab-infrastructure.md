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
> When planning your infrastructure, ensure that your setups have the correct environment type for the behavioral assays you intend to use.

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
│   ├── Hardware devices (specific models/brands)
│   └── Coordinates systems (for positioning)
└── Associated with → Procedures, Behaviors, Data acquisition

Inventory (Storage/Organization System)
└── Consumable Stocks (Specific items)
    └── Associated with → Procedures
```

## Creating Setups

Setups represent your physical experimental environments. Each setup corresponds to a specific location or configuration where experiments are conducted.

### Step 1: Navigate to Setups
{: .no_toc}

1. Go to **Personal Attributes** → **Setups** in the left navigation menu
2. Click the **Add setup** button

### Step 2: Configure Basic Setup Information
{: .no_toc}

**Fill in the essential details:**

| Field | Instructions |
|-------|-------------|
| **Name** | Use descriptive, standardized names (e.g., "Behavior Room A", "Surgery Station 1", "2P Imaging Rig", "Head-fixed Linear Track") |
| **Environment Type** | Select appropriate category: Behavioral environments (T-maze, Open field, Barnes maze, Linear track), Recording environments (Head-fixed disc, Homecage, Custom rigs), or Surgical environments (Surgical table) |
| **Authenticated Groups** | Select groups that should have access to this setup |
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
| **Setup Type** | T-maze |
| **Description** | Behavioral testing room with automated T-maze system for spatial memory tasks. Located in Room 302B, Neuroscience Building |
| **Public Access** | No |
| **Specifications** | ArmLength: "45 cm", StemLength: "50 cm", CorridorWidth: "10 cm" |

{: .note }
> Use consistent naming conventions across your lab. This makes setups easier to find and select during experiment creation.

## Adding Equipment to Setups

Equipment represents the devices and instruments within your setups. Each piece of equipment belongs to a specific setup and can be used in procedures, data acquisition, and manipulations.

### Step 1: Navigate to Equipment
{: .no_toc}

1. Go to **Modules** → **Equipment**
2. Click the **Add equipment** button

### Step 2: Configure Equipment Basics
{: .no_toc}

| Field | Instructions |
|-------|-------------|
| **Name** | Use specific, identifiable names (Good: "Intan RHD2000 #1", "Behavior Camera Main", "LED Driver Ch1-4"; Avoid: "Recording device", "Camera", "Light") |
| **Setup** | Select the setup where this equipment is located |
| **Hardware Device** | Choose from the resources database or submit new devices |
| **Coordinates System** | Define how this equipment's position is measured (Common: "External_XYZ_Absolute") |

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
| **Setup** | Select: Open Field Arena |
| **Hardware Device** | Intan RHD2000 USB interface board |
| **Type** | DataAcquisitionSystem |

{: .important }
> Link equipment to appropriate hardware devices in the resources database. If your specific model isn't available, submit it for approval first.

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
| **Authenticated Groups** | Groups that can access and modify this inventory |
| **Public Access** | Usually False for lab inventories |

### Step 3: Inventory Setup Example
{: .no_toc}

| Field | Value |
|-------|-------|
| **Name** | Neural Electrode Inventory |
| **Description** | Storage for all neural recording electrodes and probes. Located in Room 302, Cabinet B. Handle with anti-static precautions. Contact: Lab Manager for restocking. |
| **Authenticated Groups** | Electrophysiology Team, Lab Managers |

## Adding Consumable Stocks

Consumable stocks are the specific items within your inventories. These are the actual materials that get used in procedures and need to be tracked for experimental documentation.

### Step 1: Navigate to Consumable Stocks
{: .no_toc}

1. Go to **Modules** → **Consumable stocks**
2. Click **Add consumable stock**

### Step 2: Configure Stock Information
{: .no_toc}

| Field Category | Field | Description |
|----------------|--------|-------------|
| **Basic Information** | Name | Specific, identifiable descriptions |
| | Inventory | Select the appropriate inventory category |
| | Consumable | Choose from resources database or submit new items |
| **Tracking Details** | Lot number | Manufacturer's batch identifier |
| | Supplier | Where the item was purchased |
| | Cost | For budget tracking and planning |
| **Storage Information** | Storage location | Specific location within the inventory |
| | Storage conditions | Temperature, humidity, special requirements |
| | Expiration date | If applicable |
| **Usage Information** | Intended use | Specific experimental applications |
| | Notes | Special handling, preparation, or usage instructions |

### Step 3: Consumable Stock Example
{: .no_toc}

| Field | Value |
|-------|-------|
| **Type** | SiliconProbe |
| **Inventory** | Select: Neural Electrode Inventory |
| **Consumable** | NeuroNexus A1x32-Poly2 |
| **Acquisition Date** | 2024-01-15 |
| **Storage Location** | Cabinet B, Slot 15, Anti-static tube #A1x32-15 |
| **Storage Conditions** | Room temperature, anti-static protection |
| **Intended Use** | Chronic hippocampal recordings in behaving mice |
| **Cost** | $1,200 |
| **Notes** | Pre-cleaned with 70% ethanol. Handle with non-magnetic forceps only. Sterilize with EtO gas before implantation. |

## Permission Management

Proper permission management ensures that the right people have access to the right resources while maintaining security and organization.

BrainSTEM infrastructure uses four permission levels for setups and inventories and thereby inherited to equipment and consumable stocks:

| Permission Level | Capabilities |
|-----------------|-------------|
| **Members** | View details<br>Read-only access<br>**Cannot** modify or create infrastructure |
| **Contributors** | All Member permissions<br>Create and modify associated equipment and consumable stocks. <br>Select setups and equipment when creating experiments<br>Select inventory and consumable stocks when creating experiments<br>**Cannot** modify setup settings or manage permissions |
| **Managers** | All Contributor permissions<br>Manage permissions for others<br>Configure setup specifications<br>**Cannot** delete infrastructure or transfer ownership |
| **Owners** | All Manager permissions<br>Full control over setups and equipment<br>Delete infrastructure components<br>Transfer ownership to other users<br>Complete administrative control |

**Best Practices for Assigning Permissions**:
- **Owners**: PI, lab manager, or senior lab members with equipment responsibility
- **Managers**: Postdocs or experienced graduate students who primarily use specific rigs
- **Contributors**: Lab members who regularly use the equipment for their research
- **Members**: All lab members who might occasionally need read access

### Group-Based Access
{: .no_toc}

**Recommended Group Structure**:
```
Lab Members (Basic access to most lab resources)
├── Graduate Students (Access to setups and equipment for their projects)
├── Postdocs (Broader access, can manage equipment in their research areas)
├── Lab Manager (Administrative access, inventory management)
├── PI and Senior Staff (Full ownership and administrative control)
└── Technique-Specific Groups (Optional, for specialized equipment)
    ├── Electrophysiology Users (Access to recording equipment and probes)
    ├── Imaging Users (Access to microscopes and imaging supplies)
    └── Behavior Users (Access to behavioral setups and paradigms)
```

## Best Practices

### Naming Conventions
{: .no_toc}

- **Setups**: Include location and be specific (e.g., "Room302_TmazeBehavior", "HeadFixed_2P_VR")
- **Equipment**: Include model and serial number (e.g., "IntanRHD2000_SN1234")
- **Inventories**: Include storage info (e.g., "Probes_RoomTemp", "Viruses_Minus80")
- **Consumable Stocks**: Include lot numbers and concentrations where applicable

### Documentation and Maintenance
{: .no_toc}

- Include technical specifications, calibration status, and safety considerations in descriptions
- Specify physical locations, storage conditions, and responsible contacts
- Update consumable stock levels monthly, review equipment quarterly, audit permissions annually
- Document modifications, update permissions when roles change, and archive rather than delete old equipment

## Integration with Experimental Workflows

### Using Infrastructure in Procedures
{: .no_toc}

When creating procedures, your infrastructure components become available:
- **Setups** provide the location context
- **Equipment** specifies tools used (stereotaxic frames, injection systems)
- **Consumable stocks** track materials consumed (probes, viruses, drugs)

### Using Infrastructure in Sessions
{: .no_toc}

Your setup determines available:
- **Equipment** for data acquisition modules
- **Behavioral Assays** compatible with the environment type

## Troubleshooting

**Setup not available**: Verify authentication permissions and environment type compatibility

**Equipment missing from dropdowns**: Confirm correct setup assignment, equipment type alignment, and permission matching

**Consumable stock access issues**: Check group membership and owner/manager permissions

## Next Steps

With your lab infrastructure in place, you're ready to move on to experimental workflows:

- **Start with experimental design**: Learn about [Behavioral Assays]({{site.baseurl}}/tutorials/behavioral-assays) to define standardized experimental protocols that use your setups
- **Set up data management**: Configure [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage) to link your metadata to actual data files stored on your systems
- **Organize team access**: Set up [Managing Groups]({{site.baseurl}}/tutorials/managing-groups) and [Managing Projects]({{site.baseurl}}/tutorials/managing-projects) to properly organize team access to your infrastructure
- **Explore complete workflows**: Follow the [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow)<!-- or [Two-Photon Imaging Workflow]({{site.baseurl}}/tutorials/two-photon-imaging-workflow)--> tutorial for end-to-end experimental documentation
- **Contribute to the platform**: Use [Submit Resources & Taxonomies]({{site.baseurl}}/tutorials/submit-resource-and-taxonomies) to add any missing equipment or consumable types to the BrainSTEM database
