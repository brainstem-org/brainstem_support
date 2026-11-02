---
layout: default
title: Share data publicly
parent: Tutorials
nav_order: 10
---

# Sharing Data Publicly in BrainSTEM
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

BrainSTEM enables open science by allowing you to make your research data publicly accessible to the scientific community. This tutorial explains how to configure public sharing for projects and their associated personal attributes.

**Key Concepts:**
- **Projects** are the primary container for public data sharing
- **Personal Attributes** (behavioral assays, setups, data storage, inventories, protocols) have independent public settings
- Making a project public does NOT automatically make its personal attributes public

Public access flows from the project to everything that belongs to it (subjects, sessions, procedures and their modules), while personal attributes keep their own switch. The [permissions page]({{site.baseurl}}/datamodel/permissions/#public-sharing) shows this inheritance in the interactive data model.

{: .important }
> Making a project public does NOT automatically share its associated personal attributes. Behavioral Assays, setups, data storage, inventories, and protocols must be made public separately to ensure complete data accessibility.

## Understanding Public Project Sharing

When you make a project public, the following components become publicly accessible:

| Component | What Becomes Public |
|-----------|-------------------|
| **Subjects** | Subject details, performed procedures and episodes, experimental interfaces, subject and procedure logs |
| **Specimen sets** | Specimen sets and specimens, their specimen procedures and logs |
| **Sessions** | Performed sessions with their epochs, behaviors, data acquisitions and manipulations |
| **Collections** | Session collections and groupings |
| **Cohorts** and **breedings** | Subject cohorts and performed breedings |
| **Templates** | Templates shared with the project |

{: .important }
> **Planned records are never public.** Planned subjects, specimen sets and specimens, and planned or cancelled procedures, sessions and breedings stay hidden on the public portal and in the public API until they are marked performed, enrolled or collected.

{: .note }
> Project-level data becomes public, but the **personal attributes** referenced in sessions (behavioral assays, setups, data storage) remain private unless separately shared. Membership and permission lists are never public. Shared catalogs (species, strains, consumables, hardware devices, publications) are always public.

## Making a Project Public

{: .important }
> **Permission Required:** Only project **Owners** can change the public sharing status of a project.

**To make a project public:**

1. Click **Projects** in the left navigation menu
2. Select your project from the list
3. Click the **Edit** button to access the project settings
4. In **Project visibility**, switch from **Private** to **Public**

![The project Edit form: switching Project visibility to Public opens the "Make this project public?" dialog]({{site.baseurl}}/assets/images/screenshots/project-public-access-dialog.png)
{: .screenshot }
*The project Edit form: switching **Project visibility** to **Public** opens the "Make this project public?" confirmation dialog*

5. A confirmation dialog **Make this project public?** appears:
   ```
   Are you sure you want to make this project public? This will make all related 
   content visible to the public (subjects, sessions, and modules associated with 
   the project).
   ```
6. Click **Make public** to proceed, or cancel to keep it private
7. Click **Save** to apply your changes

**What happens after making a project public:**
- The project appears on the **public portal** at [www.brainstem.org/public](https://www.brainstem.org/public/), which needs no account. Visitors get read-only lists and details pages; filters, column settings, exports and bulk actions are reserved for signed-in users.
- Anyone can read the project through the **public API** at `https://www.brainstem.org/api/public/...` without a token, and MCP clients without a token see it too (see [MCP server]({{site.baseurl}}/api/mcp/)).
- The **Interactive data model** on the public portal (`/public/datamodel/`) still requires signing in; the copy on this site at [Interactive data model]({{site.baseurl}}/datamodel/?view=interactive) does not.
- Anonymous visitors do not see planned records (see above).

Use the **Public project** filter in the Projects list, or the **Public status** filter on shared catalogs, to check what is public.

## Sharing Related Personal Attributes

Personal attributes referenced in your sessions, procedures, and subject logs must be shared separately to provide complete experimental context. Without this, users can see that modules exist but cannot access the methodological details.

### Which Personal Attributes to Share

| Personal Attribute | When to Share Publicly | Why It's Needed |
|-------------------|----------------------|----------------|
| **Behavioral Assays** | If your sessions include behavior modules | Users need to understand experimental protocols and task parameters |
| **Setups** | If your sessions reference specific experimental environments | Users need to know equipment configuration and environmental conditions |
| **Data Storage** | If you want users to access raw data files | Users need file paths and access protocols to retrieve actual data |
| **Inventories** | If procedures reference specific consumables | Users need to know exact materials used (probes, drugs, etc.) |
| **[Protocols]({{"datamodel/personal_attributes/protocol/"|absolute_url}})** | If procedures, subject logs, or procedure episodes reference reusable methods | Users need the method description, URL, and any attached protocol document |

## Making Personal Attributes Public

{: .important }
> **Permission Required:** Only **Owners** of personal attributes can change their public status.

**To make any personal attribute public:**

1. Navigate to the appropriate section:
   - **Personal attributes** → **Behavioral assays**
   - **Personal attributes** → **Setups** (equipment follows its setup)
   - **Personal attributes** → **Inventories** (consumable stocks follow their inventory)
   - **Personal attributes** → **Protocols**
   - **Personal attributes** → **Licenses**
2. Select the item referenced by your public project
3. Click **Edit**
4. Switch its visibility (for example **Setup visibility**) to **Public** and confirm the **Make public** dialog
5. Click **Save**

**Data storage** has no visibility switch of its own. Its visibility follows its data protocols: mark the protocol that points at a public location (for example a DANDI or web URL) as public, and keep the lab-internal paths private.

{: .note }
> Repeat this process for each personal attribute referenced in your public project. Making a protocol public also exposes its attachment download link; linked licenses retain their own public access settings.

## Best Practices for Public Data Sharing

### Before Making Data Public

1. **Review sensitive information**: Ensure no personally identifiable information or proprietary data is included
2. **Complete documentation**: Fill in descriptions for projects, sessions, and personal attributes
3. **Verify data quality**: Check that all metadata is accurate and complete
4. **Test internally**: Have lab members verify access to ensure nothing is missing

## Revoking Public Access

If you need to make data private again:

1. Navigate to the public project or personal attribute
2. Click **Edit**
3. Switch the visibility back to **Private** and confirm **Make private** in the **Stop sharing publicly?** dialog
4. Click **Save**

{: .warning }
> Making a project private will immediately remove it from the public dashboard. However, users who have already downloaded or accessed the data will retain their copies.

## Next Steps

After making your data publicly available, consider these enhancements:

- **Improve discoverability**: Use [Submit Resources & Taxonomies]({{site.baseurl}}/tutorials/submit-resource-and-taxonomies) to contribute standardized resources that make your data more findable
- **Document protocols thoroughly**: Ensure your [Behavioral Assays]({{site.baseurl}}/tutorials/behavioral-assays) are well-documented for protocol reproducibility
- **Optimize data access**: Review [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage) to ensure public data has appropriate file access protocols
- **Enable programmatic access**: Readers can load your public project without a token with `BrainstemClient(anonymous=True)` in the [Python API tool]({{site.baseurl}}/tools/python-api-tool) or `BrainstemClient('anonymous', true)` in the [MATLAB API tool]({{site.baseurl}}/tools/matlab-api-tool)
- **Deposit the metadata**: Convert the project to NWB files with [Exporting to NWB]({{site.baseurl}}/tutorials/exporting-to-nwb)
