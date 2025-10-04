---
layout: default
title: Setting Up Lab Infrastructure
parent: Tutorials
nav_order: 8
---

# Setting Up Lab Infrastructure in BrainSTEM
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Before conducting experiments in BrainSTEM, we recommend you establish your lab's infrastructure. This tutorial covers creating and configuring the foundational elements that support your research workflows: setups with equipment and inventories with consumable stocks. Proper infrastructure setup ensures smooth experiment creation and maintains consistency across your lab.

## Understanding Lab Infrastructure Components

BrainSTEM's lab infrastructure consists of four interconnected components:

1. **Setups**: Physical experimental environments (behavior rooms, recording rigs, surgical stations)
2. **Equipment**: Devices and instruments within your setups
3. **Inventories**: Organizational systems for tracking lab resources
4. **Consumable Stocks**: Specific items and materials in your inventories

These components work together to provide the foundation for documenting procedures, behaviors, data acquisition, and manipulations.

## Behavioral Paradigms

Behavioral paradigms are standardized experimental protocols (such as T-maze alternation, open field exploration, etc.) that are performed within a specific setup environment. In BrainSTEM, these are managed under *Personal Attributes → Behavioral Paradigms*.

For detailed instructions on creating, managing, and best practices for behavioral paradigms, see the dedicated tutorial: [Behavioral Paradigms]({{site.baseurl}}/tutorials/behavioral-paradigms).

{: .note }
> When planning your infrastructure, ensure that your setups have the correct environment type for the behavioral paradigms you intend to use.

## Planning Your Infrastructure

### Before You Begin

1. **Audit your physical spaces**: List experimental environments in your lab
2. **Inventory your equipment**: Document devices, instruments, and tools
3. **Catalog your supplies**: Identify consumables, probes, drugs, and other materials
4. **Define access permissions**: Determine which group members need access to what resources

### Infrastructure Hierarchy

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

1. Go to *Personal Attributes* → *Setups* in the left navigation menu
2. Click the *Add setup* button

### Step 2: Configure Basic Setup Information

**Fill in the essential details:**

| Field | Instructions |
|-------|-------------|
| **Name** | Use descriptive, standardized names (e.g., "Behavior Room A", "Surgery Station 1", "2P Imaging Rig", "Head-fixed Linear Track") |
| **Environment Type** | Select appropriate category: Behavioral environments (T-maze, Open field, Barnes maze, Linear track), Recording environments (Head-fixed disc, Homecage, Custom rigs), or Surgical environments (Surgical table) |
| **Authenticated Groups** | Select groups that should have access to this setup |
| **Description** | Provide comprehensive details including: Physical location (room number, building), Setup purpose and capabilities, Special requirements or restrictions, Contact person for technical issues |

### Step 3: Define Physical Dimensions

Add relevant measurements for your setup using the physical dimensions configuration. Common examples:

**Behavioral mazes**: Arm lengths, corridor widths, platform sizes  
**Recording rigs**: Stage dimensions, working distances  
**Surgical stations**: Table dimensions, reach distances

**Example Dimension Entry:**
| Dimension | Value | Unit |
|-----------|-------|------|
| **Length** | 20 | cm |
| **Width** | 50 | cm |

### Step 4: Setup Examples by Type

#### Behavioral Setup Example: "T-maze Behavior Room"

**Basic Configuration:**
| Field | Value |
|-------|-------|
| **Name** | T-maze Behavior Room |
| **Setup Type** | T-maze (Environment type from BrainSTEM options) |
| **Description** | Behavioral testing room with automated T-maze system for spatial memory tasks. Located in Room 302B, Neuroscience Building |
| **Public Access** | No |

**Physical Dimensions:**
| Dimension | Value | Unit |
|-----------|-------|------|
| **Arm Length** | 45 | cm |
| **Stem Length** | 50 | cm |
| **Corridor Width** | 10 | cm |

#### Recording Setup Example: "2P Imaging Rig"

**Basic Configuration:**
| Field | Value |
|-------|-------|
| **Name** | 2P Imaging Rig |
| **Setup Type** | Head-fixed disc |
| **Description** | Two-photon microscope with head-fixed recording capability and virtual reality system. Requires dark room conditions, temperature controlled. |
| **Public Access** | No |

**Physical Dimensions:**
| Dimension | Value | Unit |
|-----------|-------|------|
| **Stage Travel** | 25 | mm |
| **Working Distance** | 2 | mm |
| **Field of View** | 512 | μm x 512 μm |

#### Surgical Setup Example: "Surgical Table Station"

**Basic Configuration:**
| Field | Value |
|-------|-------|
| **Name** | Surgical Table Station |
| **Setup Type** | Surgical setup |
| **Description** | Dedicated surgical table for anesthetized in vivo procedures, equipped with stereotaxic frame and warming pad. Located in Surgery Suite 2. |
| **Public Access** | No |

**Physical Dimensions:**
| Dimension | Value | Unit |
|-----------|-------|------|
| **Table Length** | 120 | cm |
| **Table Width** | 60 | cm |
| **Height** | 90 | cm |

{: .note }
> Use consistent naming conventions across your lab. This makes setups easier to find and select during experiment creation.

## Adding Equipment to Setups

Equipment represents the devices and instruments within your setups. Each piece of equipment belongs to a specific setup and can be used in procedures, data acquisition, and manipulations.

### Step 1: Navigate to Equipment

1. Go to *Modules* → *Equipment*
2. Click the *Add equipment* button

### Step 2: Configure Equipment Basics

| Field | Instructions |
|-------|-------------|
| **Name** | Use specific, identifiable names (Good: "Intan RHD2000 #1", "Behavior Camera Main", "LED Driver Ch1-4"; Avoid: "Recording device", "Camera", "Light") |
| **Setup** | Select the setup where this equipment is located |
| **Hardware Device** | Choose from the resources database or submit new devices |
| **Coordinates System** | Define how this equipment's position is measured (Common: "External_XYZ_Absolute") |

### Step 3: Equipment Categories and Examples

#### Data Acquisition Equipment

**Electrophysiology**:
- Intan Recording Controllers (RHD2000, RHX series)
- Amplifiers (A-M Systems, Molecular Devices)
- Signal processors and filters

**Imaging Systems**:
- Two-photon microscopes (Bruker, Thorlabs)
- Miniscopes (UCLA Miniscope)
- High-speed cameras (FLIR, Basler)

**Behavioral Monitoring**:
- Overhead cameras for behavior tracking
- Force sensors and load cells
- Motion detection systems

#### Stimulation Equipment

**Optogenetics**:
- LED drivers and controllers
- Laser systems

**Electrical Stimulation**:
- Stimulus isolators (A-M Systems, Grass)
- Function generators
- Current sources

#### Surgical Equipment

**Stereotaxic Systems**:
- Stereotaxic frames (David Kopf, Stoelting)
- Micromanipulators (Sutter, Luigs & Neumann)
- Drill systems and burr sets

**Injection Systems**:
- Microsyringe pumps (Harvard Apparatus)
- Glass pipette pullers (Sutter P-1000)
- Injection needles and syringes

### Step 4: Equipment Configuration Examples

#### Example 1: Recording System
| Field | Value |
|-------|-------|
| **Name** | Intan RHD2000 System #1 |
| **Setup** | Select: Open Field Arena |
| **Hardware Device** | Intan RHD2000 USB interface board |
| **Type** | DataAcquisitionSystem |

#### Example 2: Behavioral Camera
| Field | Value |
|-------|-------|
| **Name** | Overhead Behavior Camera |
| **Setup** | Select: Open Field Arena |
| **Hardware Device** | Basler acA1300-200uc |
| **Type** | Camera |

#### Example 3: Optogenetic System
| Field | Value |
|-------|-------|
| **Name** | Opto driver |
| **Setup** | Select: Open Field Arena |
| **Hardware Device** | Tucker-Davis RZ10X Lux-I/O Processor |
| **Type** | DataAcquisitionSystem |

{: .important }
> Link equipment to appropriate hardware devices in the resources database. If your specific model isn't available, submit it for approval first.

## Setting Up Inventories

Inventories help organize and track consumable resources in your lab. They provide structure for managing supplies and ensure proper accounting of materials used in experiments.

### Step 1: Create Inventory Categories

Navigate to *Personal Attributes* → *Inventories* and create logical groupings:

#### Common Inventory Categories

**By Material Type**:
- "Neural Probes" - Silicon probes, tetrodes, single electrodes
- "Viral Vectors" - AAV, lentivirus, optogenetic constructs  
- "Pharmacological Agents" - Drugs, anesthetics, analgesics
- "Surgical Supplies" - Sutures, needles, glass pipettes

**By Storage Location**:
- "Freezer -80°C" - Virus stocks, some drugs
- "Freezer -20°C" - Aliquoted solutions
- "Refrigerator 4°C" - Working solutions, antibodies
- "Room Temperature Storage" - Hardware, disposables

**By Experiment Type**:
- "Electrophysiology Supplies"
- "Optogenetics Materials" 
- "Behavioral Equipment"
- "Imaging Reagents"

### Step 2: Configure Inventory Details

**For each inventory:**

| Field | Instructions |
|-------|-------------|
| **Name** | Clear, descriptive identification (Examples: "Silicon Probe Storage", "AAV Virus Stocks", "Behavioral Supplies RT") |
| **Description** | Include important details: Physical location and access requirements, Storage conditions and handling notes, Responsible person or contact, Special safety considerations |
| **Authenticated Groups** | Groups that can access and modify this inventory |
| **Public Access** | Usually False for lab inventories |

### Step 3: Inventory Setup Examples

#### Example 1: Probe Storage
| Field | Value |
|-------|-------|
| **Name** | Neural Electrode Inventory |
| **Description** | Storage for all neural recording electrodes and probes. Located in Room 302, Cabinet B. Handle with anti-static precautions. Contact: Lab Manager for restocking. |
| **Location** | Room 302, Cabinet B, ESD-safe storage |
| **Groups** | Electrophysiology Team, Lab Managers, Buzsaki Lab |

#### Example 2: Virus Storage
| Field | Value |
|-------|-------|
| **Name** | Viral Vector Stocks -80°C |
| **Description** | AAV and lentiviral constructs for optogenetics and tracing. Stored in -80°C freezer, Bay 3. Biosafety Level 2 protocols required. Track aliquots and avoid freeze-thaw cycles. |
| **Location** | -80°C Freezer, Bay 3, Boxes V1-V10 |
| **Groups** | Surgery Team, Viral Core Users, Tsien Lab |

## Adding Consumable Stocks

Consumable stocks are the specific items within your inventories. These are the actual materials that get used in procedures and need to be tracked for experimental documentation.

### Step 1: Navigate to Consumable Stocks

1. Go to *Modules* → *Consumable stocks*
2. Click *Add consumable stock*

### Step 2: Configure Stock Information

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

### Step 3: Consumable Stock Examples

#### Example 1: Silicon Probe

**Basic Information:**
| Field | Value |
|-------|-------|
| **Type** | SiliconProbe |
| **Inventory** | Select: Neural Electrode Inventory |
| **Consumable** | NeuroNexus A1x32-Poly2 |
| **Acquisition Date** | 2024-01-15 |

**Storage & Tracking:**
| Field | Value |
|-------|-------|
| **Storage Location** | Cabinet B, Slot 15, Anti-static tube #A1x32-15 |
| **Storage Conditions** | Room temperature, anti-static protection, desiccant pack |
| **Intended Use** | Chronic hippocampal recordings in behaving mice |
| **Cost** | $1,200 |

**Additional Details:**
- **Probe ID**: NN2024-0456-A1x32-15
- **Quantity**: 1
- **Notes**: Pre-cleaned with 70% ethanol. Handle with non-magnetic forceps only. Sterilize with EtO gas before implantation.

#### Example 2: Viral Vector

**Basic Information:**
| Field | Value |
|-------|-------|
| **Type** | VirusSolution |
| **Inventory** | Select: Viral Vector Stocks |
| **Consumable** | AAV-DJ-ChR2-EYFP |
| **Acquisition Date** | 2024-02-01 |
| **Expiration Date** | 2026-12-15 |

**Storage & Tracking:**
| Field | Value |
|-------|-------|
| **Storage Location** | -80°C Freezer, Bay 3, Box V3, Position A4 |
| **Storage Conditions** | Store at -80°C, avoid freeze-thaw cycles, transport on dry ice |
| **Intended Use** | Optogenetic stimulation of excitatory neurons in mouse cortex |
| **Cost** | $450 |

**Viral Vector Details:**
| Parameter | Value |
|-----------|-------|
| **Titer** | 1.2 × 10¹³ vg/mL |
| **Volume** | 1.0 mL |
| **Aliquot Count** | 20 |
| **Aliquot Volume** | 50 μL each |

**Notes**: AAV-DJ-hSyn-ChR2(H134R)-EYFP from Stanford Gene Vector and Virus Core. Aliquoted on 2024-02-01. Each aliquot contains ~6 × 10¹¹ GC. Dilute in sterile PBS to desired injection concentration (typically 1:10 to 1:50). Thaw on ice 15-20 minutes before use. Never refreeze thawed aliquots. Biosafety Level 2 protocols required. Lot #VV2024-089.

#### Example 3: Pharmaceutical

**Basic Information:**
| Field | Value |
|-------|-------|
| **Type** | ChemicalReagent |
| **Inventory** | Select: Controlled Substances Inventory |
| **Consumable** | Ketamine HCl |
| **Acquisition Date** | 2024-01-10 |
| **Expiration Date** | 2025-01-10 |

**Storage & Tracking:**
| Field | Value |
|-------|-------|
| **Storage Location** | Controlled substances safe, refrigerated |
| **Storage Conditions** | Store at 2-8°C in locked safe |
| **Intended Use** | Anesthesia for surgical procedures |
| **Cost** | $85 |

**Notes**: DEA Schedule III. Record all usage for compliance. 100mg/mL, 10mL vial.

## Permission Management

Proper permission management ensures that the right people have access to the right resources while maintaining security and organization.

### Setup and Equipment Permissions

**Four Permission Levels**:
1. **Members**: Read-only access, can view and select in experiments
2. **Contributors**: Can create and modify associated equipment
3. **Managers**: Can modify setup/equipment details and manage permissions
4. **Owners**: Full control including deletion and ownership transfer

**Best Practices**:
- **Setup Owners**: PI, lab manager, or senior lab members with equipment responsibility
- **Setup Managers**: Postdocs or experienced graduate students who primarily use specific rigs
- **Contributors**: Lab members who regularly use the equipment for their research
- **Members**: All lab members who might occasionally need access

### Inventory and Stock Permissions

**Access Control Strategy**:
- **Expensive/Sensitive Equipment**: Limited to trained users (e.g., two-photon microscopes, specialized recording systems)
- **Common Lab Supplies**: Broad access for all lab members (basic consumables, standard tools)
- **Controlled Substances**: Restricted to authorized personnel only (drugs, viral vectors)
- **Technique-Specific Items**: Access based on training and project needs (electrophysiology probes, imaging dyes)
- **Shared Equipment**: Consider training requirements and scheduling protocols

### Group-Based Access

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

## Best Practices and Conventions

### Naming Conventions

**Setups**:
- Include location: "Room302_TmaxeBehavior", "Surgery_Station1"
- Be specific: "HeadFixed_2P_VR" not just "Microscope"

**Equipment**:
- Include model and serial: "IntanRHD2000_SN1234"
- Use sequential numbering: "BehaviorCamera_01", "BehaviorCamera_02"

**Inventories**:
- Clear categories: "Probes_RoomTemp", "Viruses_Minus80"
- Include storage info: "Drugs_ControlledSafe", "Disposables_Cabinet3"

**Consumable Stocks**:
- Include lot numbers: "AAV_ChR2_Lot089"
- Specify concentrations: "Ketamine_100mgml_Vial3"

### Documentation Standards

**Equipment Descriptions Should Include**:
- Technical specifications (channels, resolution, power)
- Calibration status and procedures
- Maintenance schedules and contacts
- Safety considerations and restrictions

**Inventory Descriptions Should Include**:
- Physical location with specific details
- Storage conditions and requirements
- Access procedures and restrictions
- Responsible persons and contacts

### Maintenance and Updates

**Regular Review Schedule**:
- **Monthly**: Update consumable stock levels and expirations
- **Quarterly**: Review equipment status and calibrations
- **Annually**: Audit inventory organization and permissions

**Change Management**:
- Document equipment modifications or replacements
- Update permissions when lab members change roles
- Archive old/retired equipment rather than deleting
- Maintain chain of custody for controlled substances

## Integration with Experimental Workflows

### Using Infrastructure in Procedures

When creating procedures, your infrastructure components become available:
- **Setups** provide the location context
- **Equipment** specifies tools used (stereotaxic frames, injection systems)
- **Consumable stocks** track materials consumed (probes, viruses, drugs)

### Using Infrastructure in Sessions

Your setup determines available:
- **Equipment** for data acquisition modules
- **Behavioral paradigms** compatible with the environment type
- **Associated consumables** for tracking usage

### API Integration

Access your infrastructure programmatically:

```python
from brainstem_api_client import BrainstemClient

client = BrainstemClient()

# Get all setups for planning experiments
setups = client.load_model('setup').json()

# Find equipment in a specific setup
equipment = client.load_model('equipment', 
                            filters={'setup__name': 'Behavior Room A'}).json()

# Check consumable stock levels
stocks = client.load_model('consumablestock',
                         filters={'inventory__name': 'Neural Probes'}).json()
```

## Troubleshooting Common Issues

### Setup Not Available in Session Creation

**Problem**: Cannot select setup when creating behaviors or data acquisition

**Solutions**:
- Verify you are authenticated to use the setup
- Check that setup has appropriate environment type for your needs
- Ensure the setup is saved and properly configured

### Equipment Missing from Dropdowns

**Problem**: Equipment doesn't appear when creating procedures or modules

**Solutions**:
- Confirm equipment is assigned to the correct setup
- Confirm the equipment type is aligned with the type of procedure, data acquisition or manipulation.
- Verify permissions match between session projects and equipment
- Check that hardware device is properly linked

### Consumable Stock Access Issues

**Problem**: Cannot access or modify consumable stocks

**Solutions**:
- Verify group membership for inventory access
- Check owner/manager permissions for modification rights
- Ensure consumable is linked to correct inventory

### Permission Synchronization

**Problem**: Changes to permissions don't take effect immediately

**Solutions**:
- Check group membership at multiple levels (setup, inventory, project)
- Contact administrators for permission inheritance issues

## Advanced Configuration

### Shared Resource Management

For equipment shared across multiple labs:

- Use group-based permissions for cross-lab access
- Create separate inventories for shared vs. lab-specific items
- Establish clear protocols for scheduling and maintenance

### Custom Environment Types

For specialized setups not covered by standard environment types:
- Submit any missing environment types to BrainSTEM administrators
- Use "Other" environment type with detailed descriptions
- Document custom specifications in setup descriptions

By following this tutorial, you'll establish a robust infrastructure foundation that supports efficient experiment creation, accurate resource tracking, and seamless collaboration within your lab. Proper infrastructure setup is an investment that pays dividends in experimental productivity and data organization.

## Next Steps

With your lab infrastructure in place, you're ready to move on to experimental workflows:

- **Start with experimental design**: Learn about [Behavioral Paradigms]({{site.baseurl}}/tutorials/behavioral-paradigms) to define standardized experimental protocols that use your setups
- **Set up data management**: Configure [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage) to link your metadata to actual data files stored on your systems
- **Organize team access**: Set up [Managing Groups]({{site.baseurl}}/tutorials/managing-groups) and [Managing Projects]({{site.baseurl}}/tutorials/managing-projects) to properly organize team access to your infrastructure
- **Explore complete workflows**: Follow either the [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow) or [Two-Photon Imaging Workflow]({{site.baseurl}}/tutorials/two-photon-imaging-workflow) tutorials for end-to-end experimental documentation
- **Contribute to the platform**: Use [Submit Resources & Taxonomies]({{site.baseurl}}/tutorials/submit-resource-and-taxonomies) to add any missing equipment or consumable types to the BrainSTEM database
