---
layout: default
title: Share data publicly
parent: Tutorials
nav_order: 10
---

# Share Data Publicly
{: .no_toc}

## Introduction

BrainSTEM allows you to make your research data publicly accessible to promote open science and collaboration. Public sharing is managed at the project level, with personal attributes requiring individual public sharing settings.

The diagram below illustrates how public permissions are inherited through the BrainSTEM data model:
 
![permissions]({{site.baseurl}}/assets/images/permission_public.png)

## Project Public Sharing

{: .warning }
> Important: Making a project public does NOT automatically make its associated personal attributes public. Personal attributes (behavioral paradigms, data storage, setups) must be made public separately.

When a project is made public, all associated components become publicly accessible, including:
- Subjects and their procedures
- Sessions and associated modules
- Collections and cohorts
- Related modules (behaviors, data acquisition, manipulations)

### Making a Project Public
{: .no_toc}

{: .important }
> Only project owners can change the public sharing status of a project.

To make a project public:

1. Navigate to the project you want to make public
2. Click the "Edit" button to access the project profile
3. Locate the "Public" checkbox at the bottom of the form
4. When you check the box, a confirmation dialog will appear:
```
Are you sure you want to make this project public? This will make all related content visible to
the public (subjects, sessions, and modules associated with the project).
```
5. Click "Confirm" to proceed with making the project public, or "Cancel" to keep it private
6. Click "Save" to apply the changes to your project

{: .warning }
> Once a project is made public, anyone can access:
> - All subjects in the project
> - All sessions in the project
> - All modules (behaviors, data acquisition, manipulations) associated with these sessions
> - All collections and cohorts within the project

## Public Sharing of related Personal Attributes

When using personal attributes in public projects, certain components must also be individually shared:
- Behavioral paradigms
- Data storage
- Setups
- Inventories

### Example Scenario
{: .no_toc}

Let's say you have:
1. A project called "Mouse Behavior Study"
2. Sessions in this project involving behavioral experiments
3. A behavioral paradigm called "Open Field Test" used in the behavior module of these sessions
4. A setup called "Behavior Room A" also used in the behavior module of these sessions

If you make the project public but don't make the behavioral paradigm and setup public:
- Users can see your project and its components (subjects, sessions, collections)
- When they open a session and try to view its behavior module:
  - They can see that there is a behavior module
  - But they'll get access errors when trying to view the behavioral paradigm details
  - They'll also get access errors when trying to view the setup details
- This creates an incomplete view of your experimental methods, as users can't access the critical details about how the behavior was conducted

{: .important }
> This is why it's essential to make both your project AND its associated personal attributes public. Remember:
> - Behaviors in sessions require both behavioral paradigms and setups to be public
> - Data acquisition in sessions require data storage to be public
> - The relationships between sessions and personal attributes determine which attributes need to be made public


### Making Personal Attributes Public
{: .no_toc}

{: .important }
> Only owners of personal attributes can change their public status.

To make a personal attribute public:

1. Navigate to the personal attribute you want to make public
2. Click the "Edit" button
3. Find the "Public access" checkbox at the bottom of the form
4. Check the box to make the attribute public
5. Click "Save" to apply the changes

## Verifying Public Access

After making items public, verify their accessibility:

1. Visit the public dashboard at [www.brainstem.org/public](https://www.brainstem.org/public)
2. Search for your shared project or attributes
3. Verify that all components are accessible as expected

## Next Steps

After making your data publicly available, consider these additional steps:

- **Enhance discoverability**: Use [Submit Resources & Taxonomies]({{site.baseurl}}/tutorials/submit-resource-and-taxonomies) to contribute standardized resources that make your data more findable and usable by the research community
- **Document methodologies**: Ensure your [Behavioral Paradigms]({{site.baseurl}}/tutorials/behavioral-paradigms) are well-documented and publicly accessible for protocol reproducibility
- **Optimize data accessibility**: Review your [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage) configuration to ensure public data has appropriate access protocols