---
layout: default
title: Get started!
parent: Tutorials
nav_order: 1
---

# Getting Started with BrainSTEM
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Create or Join a Group

Before you can start using BrainSTEM, you need to either create a new group for your lab or join an existing one. Groups in BrainSTEM help organize lab members and manage permissions for projects and resources.

### Accessing Groups

1. From your dashboard, locate and click the Users icon in the top right corner of the screen
2. Select *Groups* from the dropdown menu

![Groups menu]({{site.baseurl}}/assets/images/tutorials/user_group.png)

### Creating a New Group

If your lab doesn't have a group yet, you can create one:

1. Click the *Add group* button in the top right corner of the Groups page
2. Fill in the required information for your new group

![Add group button]({{site.baseurl}}/assets/images/tutorials/add_group.png)

### Joining an Existing Group

To join your lab's existing group:

1. Click on the group name from the list of available groups
2. On the group's detail page, click the *Request membership of group* button
3. Wait for a group manager to approve your request

![Request group membership]({{site.baseurl}}/assets/images/tutorials/request_member_lab.png)

### Managing Group Membership Requests

For group managers:

1. Click the Users icon in the top right corner
2. Select *Requests & Invitations*
3. Navigate to the *Group membership requests* section
4. Review and accept requests from your lab members

{: .important }
> Labs should coordinate among their members to ensure proper group management. It's recommended to have at least two group managers per lab.

## Create Your First Project

After joining or creating a group, you can start creating projects. Projects in BrainSTEM are containers that help organize your research data, including subjects, datasets, and collections.

1. Click on *Projects* in the left navigation menu
2. Click the *Add project* button in the top right corner
3. Fill in the required project information

![First project]({{site.baseurl}}/assets/images/tutorials/first_project.png)

{: .note }
> For detailed information about project fields and structure, see the [Project data model]({{site.baseurl}}/datamodel/stem/project/).

## Create Your First Subject

Once you have created a project, you can start adding research subjects. Subjects in BrainSTEM represent the experimental animals in your studies.

1. Click on *Subjects* in the left navigation menu
2. Click the *Add subject* button in the top right corner
3. Fill in the required subject information

![First subject]({{site.baseurl}}/assets/images/tutorials/first_subject.png)

{: .note }
> For detailed information about subject fields and available options, see the [Subject data model]({{site.baseurl}}/datamodel/stem/subject/).

{: .important }
> Remember to associate your subject with the correct project(s) to ensure proper access and organization of your research data.

## Create Your First Session

After adding subjects, you can create sessions to record your experimental data. Sessions in BrainSTEM help organize your experiments chronologically.

1. Click on *Sessions* in the left navigation menu
2. Click the *Add session* button in the top right corner 
3. Fill in the required session information

![First session]({{site.baseurl}}/assets/images/tutorials/first_session.png)

{: .note }
> For detailed information about session fields and options, see the [Session data model]({{site.baseurl}}/datamodel/stem/dataset/).

{: .important }
> Sessions inherit permissions from their associated projects. Make sure to select the correct project to enable proper access for your team members.

## Build Your Own Experiment

BrainSTEM uses Personal Attributes and Modules to document your experimental procedures. Below is a recommended order for setting up your experiment components.

![Describe experiment]({{site.baseurl}}/assets/images/tutorials/describe_experiment.png)

### Available Components

Personal Attributes:
- [Behavioral paradigms]({{site.baseurl}}/datamodel/personal_attributes/behavioral_paradigm/)
- [Data storage]({{site.baseurl}}/datamodel/personal_attributes/data_storage/)
- [Experimental setups]({{site.baseurl}}/datamodel/personal_attributes/experiment_setups/)
- [Inventories]({{site.baseurl}}/datamodel/personal_attributes/inventories/)

Modules:
- [Behavior]({{site.baseurl}}/datamodel/modules/behavior/)
- [Data acquisition]({{site.baseurl}}/datamodel/modules/experiment_data/)
- [Equipments]({{site.baseurl}}/datamodel/modules/installation/)
- [Consumable stocks]({{site.baseurl}}/datamodel/modules/consumable_stock/)
- [Manipulation]({{site.baseurl}}/datamodel/modules/manipulation/)
- [Procedure]({{site.baseurl}}/datamodel/modules/procedure/)
- [Action logs]({{site.baseurl}}/datamodel/modules/actionlog/)
- [Subject logs]({{site.baseurl}}/datamodel/modules/subjectlog/)

### Recommended Setup Order

1. Set up data storage locations to organize your data files
2. Create experimental setups to define your physical experiment environment
3. Define behavioral paradigms for your experimental tasks
4. Set up inventories to track your lab resources
5. Add procedures (e.g., surgeries, implants, injections)
6. Configure equipment installations in your setups
7. Set up behaviors to describe subject tasks
8. Define manipulations for experimental interventions
9. Configure data acquisition parameters
10. Begin tracking with action logs and subject logs

{: .important }
> This order ensures dependent components are created first. For example, behaviors need experimental setups and behavioral paradigms to be defined first.

{: .note }
> The exact order may vary based on your specific experimental needs. Some components can be set up in parallel or may not be needed for every experiment.

