---
layout: default
title: Get started!
parent: Tutorials
nav_order: 1
---

# Get Started with BrainSTEM
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Create an account
First thing to do is [create an account](https://www.brainstem.org/register/). Provide your name, email, and a secure password. Once you have created an account you can visit your profile from the top menu to add a profile image, and link to your orcid account, your google scholar profile, and your website.

## Create or Join a Group

Next, you need to either create a new group for your lab or join an existing one. Groups in BrainSTEM help organize lab members and manage permissions for projects and resources.

### Accessing Groups
1. From your dashboard, locate and click the Users icon in the top right corner of the screen
2. Select *Groups* from the dropdown menu
![Groups menu]({{site.baseurl}}/assets/images/tutorials/user_group.png)

### Managing Group Membership
Once on the Groups page, you have two options:

<div class="code-example" markdown="1">

#### Option 1: Create a New Group
If your lab doesn't have a group yet:
1. Click the *Add group* button in the top right corner
2. Fill in the required information for your new group
![Add group button]({{site.baseurl}}/assets/images/tutorials/add_group.png)

#### Option 2: Join an Existing Group
If your lab already has a group:
1. Click on the group name from the list of available groups
2. On the group's detail page, click the *Request membership of group* button
3. Wait for a group manager to approve your request
![Request group membership]({{site.baseurl}}/assets/images/tutorials/request_member_lab.png)

</div>

### Managing Group Membership Requests

For group managers:

1. Click the Users icon in the top right corner
2. Select *Requests & Invitations*
3. Navigate to the *Group membership requests* section
4. Review and accept requests from your lab members

{: .important }
> Labs should coordinate among their members to ensure proper group management. It's recommended to have at least two group managers per lab.

## Create Your First Project

After joining or creating a group, you can start creating projects. Projects in BrainSTEM are containers that help organize your research data, including subjects, sessions, and collections.

1. Click on *Projects* in the left navigation menu
2. Click the *Add project* button in the top right corner
3. Fill in the required project information

![First project]({{site.baseurl}}/assets/images/tutorials/first_project.gif)

{: .note }
> For detailed information about project fields and structure, see the [Project data model]({{site.baseurl}}/datamodel/stem/project/).

## Add your personal attributes

Next, create personal attributes relevant to your experiments. 

### Define behavioral paradigms to describe the behavioral conditions of your subjects
### Set up data storage locations to link to your data files
### Create setups to define your physical experimental environments
   - Configure the equipment in your setups
### Set up inventories to track your lab resources
   - Add consumable stocks to your inventories

Now that all your personal attributes are in place, you can continue and add your first subject.

## Create Your First Subject

 Subjects in BrainSTEM represent the experimental animals in your studies. Subject can be created without creating personal attributes but if you want to describe procedures performed on the subject, it is recommended to add relevant setups with equipment, and inventories with consumable stocks.

1. Click on *Subjects* in the left navigation menu
2. Click the *Add subject* button in the top right corner
3. Fill in the required subject information

![First subject]({{site.baseurl}}/assets/images/tutorials/first_subject.gif)

{: .note }
> For detailed information about subject fields and available options, see the [Subject data model]({{site.baseurl}}/datamodel/stem/subject/).

{: .important }
> Remember to associate your subject with the correct project(s) to ensure proper access and organization of your research data.

## Create Your First Session

After adding subjects, you can create sessions to record your experimental data. Sessions in BrainSTEM help organize your experiments chronologically.

1. Click on *Sessions* in the left navigation menu
2. Click the *Add session* button in the top right corner 
3. Fill in the required session information

![First session]({{site.baseurl}}/assets/images/tutorials/first_session.gif)

{: .note }
> For detailed information about session fields and options, see the [Session data model]({{site.baseurl}}/datamodel/stem/session/).

{: .important }
> Sessions inherit permissions from their associated projects. Make sure to select the correct project to enable proper access for your team members.

## Build Your Own Experiment

BrainSTEM uses Personal Attributes and Modules to document your experimental procedures. Below is a recommended order for setting up your experiment components.

![Describe experiment]({{site.baseurl}}/assets/images/tutorials/describe_experiment.gif)

### Available Components

STEM models
- [Subjects]({{site.baseurl}}/datamodel/stem/subject/)
   - [Procedures]({{site.baseurl}}/datamodel/modules/procedure/)
   - [Procedure logs]({{site.baseurl}}/datamodel/modules/procedurelog/)
   - [Subject logs]({{site.baseurl}}/datamodel/modules/subjectlog/)

- [Sessions]({{site.baseurl}}/datamodel/stem/session/)
   - [Behaviors]({{site.baseurl}}/datamodel/modules/behavior/)
   - [Data acquisitions]({{site.baseurl}}/datamodel/modules/dataacquisition/)
   - [Manipulations]({{site.baseurl}}/datamodel/modules/manipulation/)

Personal Attributes:
- [Behavioral paradigms]({{site.baseurl}}/datamodel/personal_attributes/behavioralparadigm/)
- [Data storages]({{site.baseurl}}/datamodel/personal_attributes/datastorage/)
- [Setups]({{site.baseurl}}/datamodel/personal_attributes/setup/)
   - [Equipment]({{site.baseurl}}/datamodel/modules/equipment/)
- [Inventories]({{site.baseurl}}/datamodel/personal_attributes/inventory/)
   - [Consumable stocks]({{site.baseurl}}/datamodel/modules/consumablestock/)

### Recommended workflow

1. Create/Join a group
2. Create a project
3. Next, create personal attributes relevant to your experiments
   1. Define behavioral paradigms to describe the behavioral conditions of your subjects
   2. Set up data storage locations to link to your data files
   3. Create setups to define your physical experimental environments
   - Configure the equipment in your setups
   4. Set up inventories to track your lab resources
   - Add consumable stocks to your inventories
4. Create your first subject
   - Add procedures to the subject (e.g., implants and injections)
   - Begin tracking with procedure logs and subject logs
5. Create your first session
   - Set up behaviors to describe subject tasks
   - Configure data acquisition parameters
   - Define manipulations for experimental interventions

{: .note }
> The exact order may vary based on your specific experimental needs. Some components can be set up in parallel or may not be needed for every experiment.

{: .important }
> This order ensures dependent components are created first. For example, behaviors need setups and behavioral paradigms to be defined first.
> Data acquisition are linked to subjects through procedures, and to setups through equipment, which should be created first.
