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
- **Personal Attributes** (behavioral paradigms, setups, data storage, inventories) have independent public settings
- Making a project public does NOT automatically make its personal attributes public

The diagram below illustrates how public permissions flow through the BrainSTEM data model:
 
![permissions]({{site.baseurl}}/assets/images/permission_public.png)

{: .important }
> Making a project public does NOT automatically share its associated personal attributes. Behavioral paradigms, setups, data storage, and inventories must be made public separately to ensure complete data accessibility.

## Understanding Public Project Sharing

When you make a project public, the following components become publicly accessible:

| Component | What Becomes Public |
|-----------|-------------------|
| **Subjects** | All subject details and associated procedures |
| **Sessions** | All session metadata, epoch information and related behavior, data acquisition, and manipulation modules |
| **Collections** | Session collections and groupings |
| **Cohorts** | Subject cohorts and group assignments |

{: .note }
> Project-level data becomes public, but the **personal attributes** referenced in sessions (behavioral paradigms, setups, data storage) remain private unless separately shared.

## Making a Project Public

{: .important }
> **Permission Required:** Only project **Owners** can change the public sharing status of a project.

**To make a project public:**

1. Navigate to **Stem** → **Projects**
2. Select your project from the list
3. Click the **Edit** button to access the project settings
4. Scroll to the bottom of the form and locate the **Public** checkbox
5. Check the **Public** checkbox
6. A confirmation dialog will appear:
   ```
   Are you sure you want to make this project public? This will make all related 
   content visible to the public (subjects, sessions, and modules associated with 
   the project).
   ```
7. Click **Confirm** to proceed, or **Cancel** to keep it private
8. Click **Save** to apply your changes

**What happens after making a project public:**
- The project appears in the public dashboard at [www.brainstem.org/public](https://www.brainstem.org/public)
- Anyone can browse subjects, sessions, and modules
- Users can access the project via the API without authentication
- All project metadata becomes searchable

## Sharing Related Personal Attributes

Personal attributes referenced in your sessions must be shared separately to provide complete experimental context. Without this, users can see that modules exist but cannot access the methodological details.

### Which Personal Attributes to Share

| Personal Attribute | When to Share Publicly | Why It's Needed |
|-------------------|----------------------|----------------|
| **Behavioral Paradigms** | If your sessions include behavior modules | Users need to understand experimental protocols and task parameters |
| **Setups** | If your sessions reference specific experimental environments | Users need to know equipment configuration and environmental conditions |
| **Data Storage** | If you want users to access raw data files | Users need file paths and access protocols to retrieve actual data |
| **Inventories** | If procedures reference specific consumables | Users need to know exact materials used (probes, drugs, etc.) |

## Making Personal Attributes Public

{: .important }
> **Permission Required:** Only **Owners** of personal attributes can change their public status.

**To make any personal attribute public:**

1. Navigate to the appropriate section:
   - **Personal Attributes** → **Behavioral Paradigms**
   - **Personal Attributes** → **Setups**
   - **Personal Attributes** → **Data storage**
   - **Personal Attributes** → **Inventories**
2. Select the item used in your public sessions
3. Click **Edit**
4. Scroll to the bottom and check the **Public access** checkbox
5. Click **Save**

{: .note }
> Repeat this process for each personal attribute referenced in your public project's sessions.

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
3. **Uncheck** the **Public** or **Public access** checkbox
4. Click **Save**

{: .warning }
> Making a project private will immediately remove it from the public dashboard. However, users who have already downloaded or accessed the data will retain their copies.

## Next Steps

After making your data publicly available, consider these enhancements:

- **Improve discoverability**: Use [Submit Resources & Taxonomies]({{site.baseurl}}/tutorials/submit-resource-and-taxonomies) to contribute standardized resources that make your data more findable
- **Document protocols thoroughly**: Ensure your [Behavioral Paradigms]({{site.baseurl}}/tutorials/behavioral-paradigms) are well-documented for protocol reproducibility
- **Optimize data access**: Review [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage) to ensure public data has appropriate file access protocols
- **Enable programmatic access**: Share example API scripts in the [Python API tool]({{site.baseurl}}/api-tools/python-api-tool) or [MATLAB API tool]({{site.baseurl}}/api-tools/matlab-api-tool) tutorials
