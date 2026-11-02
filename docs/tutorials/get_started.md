---
layout: default
title: Get started!
parent: Tutorials
nav_order: 1
---

# Get Started with BrainSTEM
{: .no_toc}

This tutorial takes you from a new account to your first project, subject and session, following the **Getting started** checklist on the dashboard. At the end you have a group, a project and a session that your lab members can see.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Create an account
{: .no_toc}

First thing to do is [create an account](https://www.brainstem.org/register/). Provide your name, email, and a secure password, then confirm your email address. Once you have created an account you can visit your profile from the top menu to add a profile image, and link to your orcid account, your google scholar profile, and your website.

## Follow the "Getting started" checklist
{: .no_toc}

Your dashboard opens with a **Getting started** card that tracks the lab basics in three groups: **Collaborate** (join or create a group, invite your first teammate), **Prepare your environment** (add your first setup, behavioral assay, inventory and data storage) and **Structure your work** (create your first project, subject and session). The sections below follow the same order. The card can be removed with **Add widget** → **Manage widgets** once you are done.

![The Getting started card with eight of nine steps done: the open step, Invite your first teammate, is at the top, and the completed steps are listed below in their three groups]({{site.baseurl}}/assets/images/screenshots/dashboard-getting-started.png)
{: .screenshot }
*The Getting started card with eight of nine steps done: the open step, Invite your first teammate, is at the top, and the completed steps are listed below in their three groups*

## Create or Join a Group
{: .no_toc}

Next, you need to either create a new group for your lab or join an existing one. Groups in BrainSTEM help organize lab members and manage permissions for projects and resources.

### Accessing Groups
{: .no_toc}

1. From your dashboard, locate and click the **Users, groups & invitations** icon in the top right corner of the screen
2. Select *Groups* from the dropdown menu

### Managing Group Membership
{: .no_toc}

Once on the Groups page, you have two options:

<div class="code-example" markdown="1">

#### Option 1: Create a New Group
{: .no_toc}

If your lab doesn't have a group yet:
1. Click the *Add group* button in the top right corner
2. Fill in the required information for your new group

#### Option 2: Join an Existing Group
{: .no_toc}

If your lab already has a group:
1. Click on the group name from the list of available groups
2. On the group's detail page, click the *Request membership* button
3. Wait for a group manager to approve your request

</div>

### Managing Group Membership Requests
{: .no_toc}

For group managers:

1. Click the **Users, groups & invitations** icon in the top right corner
2. Select *Invitations & Requests*
3. Navigate to the *Group membership requests* section
4. Review and accept requests from your lab members

{: .important }
> Labs should coordinate among their members to ensure proper group management. It's recommended to have at least two group managers per lab.

## Create Your First Project

After joining or creating a group, you can start creating projects. Projects in BrainSTEM are containers that help organize your research data, including subjects, sessions, and collections.

1. Click on *Projects* in the left navigation menu
2. Click the *Add project* button in the top right corner
3. Fill in the required project information: the **Name** and the **Authenticated groups** that should have access. The groups you select get Contributor access; everything else can be filled in after **Create and continue**.

![The add project form filled in: the project name and the authenticated groups, then Create and continue.]({{site.baseurl}}/assets/images/screenshots/get-started-project-form.png)
{: .screenshot }
*The add project form filled in: the project name and the authenticated groups, then Create and continue.*

{% include walkthrough.html slug="get-started-create-project" caption="Creating a project: the name and the groups that get access; the video ends with the pointer on Create and continue." %}

{: .note }
> For detailed information about project fields and structure, see the [Project data model]({{site.baseurl}}/datamodel/stem/project/).

## Add your personal attributes

Before creating subjects and sessions, set up personal attributes that describe your setups, inventories and behavioral assays. These provide standardized options for your experiments.

### Define behavioral assays to describe the behavioral conditions of your subjects
{: .no_toc}

1. Navigate to *Personal Attributes* → *Behavioral Assays* in the left menu
2. Click *Add behavioral assay*
3. Fill in the paradigm details (e.g., "Open Field Test", "Novel Object Recognition")
4. Add a description of the experimental protocol

### Set up data storage locations to link to your data files
{: .no_toc}

1. Go to *Personal Attributes* → *Data storage*
2. Click *Add data storage*
3. Define storage locations where your raw data files are kept (e.g., "Lab Server", "External Drive A")
4. Include relevant path information and access details

### Create setups to define your physical experimental environments
{: .no_toc}

1. Navigate to *Personal Attributes* → *Setups*
2. Click *Add setup*
3. Describe your experimental setups (e.g., "Theta behavior maze", "Surgical table", "Head-fixed 2P Virtual environment", "Home cage")
4. **Configure the equipment in your setups:**
   - Go to *Personal Attributes* → *Equipment*
   - Add devices like "Intan RHD2000", "Behavior Camera", "LED Arrays", linked to a hardware device from the shared catalog
   - Associate equipment with appropriate setups
   
### Set up inventories to track your lab resources
{: .no_toc}

1. Go to *Personal Attributes* → *Inventories*
2. Click *Add inventory*
3. Create inventory categories (e.g., "Silicon Probes", "Virus stocks")
4. **Add consumable stocks to your inventories:**
   - Navigate to *Personal Attributes* → *Consumable stocks*
   - Add your lots of catalog consumables: probe models, virus batches, drug solutions
   - Link them to appropriate inventories; procedures later pick them as material sources

{: .note }
> These personal attributes will appear as selectable options when creating sessions, subjects, and experiments. Setting them up first streamlines your data entry process.

Now that all your personal attributes are in place, you can continue and add your first subject.

## Create Your First Subject

 Subjects in BrainSTEM represent the experimental animals in your studies. Subject can be created without creating personal attributes but if you want to describe procedures performed on the subject, it is recommended to add relevant setups with equipment, and inventories with consumable stocks.

1. Click on *Subjects* in the left navigation menu
2. Click the *Add subject* button in the top right corner
3. Fill in the required subject information: the **Subject name**, **Projects**, **Sex**, **Species** and **Status**

![The add subject form filled in: name, project, sex, species, strain and status, then Create and continue.]({{site.baseurl}}/assets/images/screenshots/get-started-subject-form.png)
{: .screenshot }
*The add subject form filled in: name, project, sex, species, strain and status, then Create and continue.*

{% include walkthrough.html slug="get-started-create-subject" caption="Creating a subject: name, project, sex, species, strain and status; the strain list follows the species. The video ends with the pointer on Create and continue." %}

{: .note }
> **Species** is required for every subject. **Strain** is optional; it becomes selectable once a species is chosen and only lists strains of that species. If your species or strain is missing, submit it via the *Taxonomies* menu (see [Submit Resources & Taxonomies]({{site.baseurl}}/tutorials/submit-resource-and-taxonomies)).

{: .note }
> Working with slices, sections or cultures instead of live animals? Create a **Specimen set** instead of a subject. Specimen sets are the ex vivo counterpart of subjects and can be derived from one. See the [Ex vivo workflow]({{site.baseurl}}/tutorials/specimen-workflow).

{: .note }
> For detailed information about subject fields and available options, see the [Subject data model]({{site.baseurl}}/datamodel/stem/subject/).

{: .important }
> Remember to associate your subject with the correct project(s) to ensure proper access and organization of your research data.

## Create Your First Session

After adding subjects, you can create sessions to record your experimental data. Sessions in BrainSTEM help organize your experiments chronologically.

1. Click on *Sessions* in the left navigation menu
2. Click the *Add session* button in the top right corner 
3. Fill in the required session information: the **Name**, **Session type** (*Subject* for live animals, *Specimen* for ex vivo material), **Projects**, the **Subjects** (or **Specimen sets**) involved, and the **Status**

![The add session form: name, session type Subject and project, with the Subjects list open to pick the subjects of the session.]({{site.baseurl}}/assets/images/screenshots/get-started-session-form.png)
{: .screenshot }
*The add session form: name, session type Subject and project, with the Subjects list open to pick the subjects of the session.*

{% include walkthrough.html slug="get-started-create-session" caption="Creating a session: name, session type, project, the subjects it was run on and status; the video ends with the pointer on Create and continue." %}

{: .note }
> For detailed information about session fields and options, see the [Session data model]({{site.baseurl}}/datamodel/stem/session/).

{: .important }
> Sessions inherit permissions from their associated projects. Make sure to select the correct project to enable proper access for your team members.

## Find your records with the AI assistant

Once you have a few records, the quickest way to find them is the **AI assistant**, available from the corner button on every private page or from the header menu. Ask in plain language, for example "Show sessions with silicon probe implants in the hippocampus" or "Show the subject with identifier "EAR-TAG"". The assistant only returns records you may read and never changes anything. See [Working with AI]({{site.baseurl}}/tutorials/working-with-ai).

## Already have data in spreadsheets?

The import tool creates subjects, sessions, procedures and other records from a filled-in template: download the template for the record kind, fill it in, upload it and review the result. See the [Import tool]({{site.baseurl}}/webinterface/import-tool/) page.

## Build Your Own Experiment

BrainSTEM uses Personal Attributes and Modules to document your experimental procedures. Below is a recommended order for setting up your experiment components.

### Available Components
{: .no_toc}

STEM models
- [Subjects]({{site.baseurl}}/datamodel/stem/subject/)
   - [Procedures]({{site.baseurl}}/datamodel/modules/procedure/), with their [material usages]({{site.baseurl}}/datamodel/modules/materialusage/)
   - [Experimental interfaces]({{site.baseurl}}/datamodel/modules/experimentalinterface/) (created by implant procedures)
   - [Procedure logs]({{site.baseurl}}/datamodel/modules/procedurelog/)
   - [Subject logs]({{site.baseurl}}/datamodel/modules/subjectlog/)

- [Specimen sets]({{site.baseurl}}/datamodel/stem/specimenset/) (ex vivo material)
   - [Specimen procedures]({{site.baseurl}}/datamodel/modules/specimenprocedure/)

- [Sessions]({{site.baseurl}}/datamodel/stem/session/)
   - [Behaviors]({{site.baseurl}}/datamodel/modules/behavior/)
   - [Data acquisition]({{site.baseurl}}/datamodel/modules/dataacquisition/)
   - [Manipulations]({{site.baseurl}}/datamodel/modules/manipulation/)

The [interactive data model]({{site.baseurl}}/datamodel/?view=interactive) shows all of these as cards with their fields and connections.

Personal Attributes:
- [Behavioral Assays]({{site.baseurl}}/datamodel/personal_attributes/behavioralassay/)
- [Data storages]({{site.baseurl}}/datamodel/personal_attributes/datastorage/)
- [Setups]({{site.baseurl}}/datamodel/personal_attributes/setup/)
   - [Equipment]({{site.baseurl}}/datamodel/modules/equipment/)
- [Inventories]({{site.baseurl}}/datamodel/personal_attributes/inventory/)
   - [Consumable stocks]({{site.baseurl}}/datamodel/modules/consumablestock/)

### Recommended workflow
{: .no_toc}

1. Create/Join a group
2. Create a project
3. Next, create personal attributes relevant to your experiments
   1. Define behavioral assays to describe the behavioral conditions of your subjects
   2. Set up data storage locations to link to your data files
   3. Create setups to define your physical experimental environments
   - Configure the equipment in your setups
   4. Set up inventories to track your lab resources
   - Add consumable stocks to your inventories
4. Create your first subject (or specimen set)
   - Add procedures to the subject (e.g., implants and injections) with the materials they used
   - Implant procedures create an experimental interface (the probe, fiber or window) automatically
   - Begin tracking with procedure logs and subject logs
5. Create your first session
   - Set up behaviors to describe subject tasks
   - Configure data acquisition parameters and link each acquisition to its experimental interface
   - Define manipulations for experimental interventions

{: .note }
> The exact order may vary based on your specific experimental needs. Some components can be set up in parallel or may not be needed for every experiment.

{: .important }
> This order ensures dependent components are created first. For example, behaviors need setups and behavioral assays to be defined first.
> Data acquisitions are linked to subjects through experimental interfaces, and to setups through equipment, which should be created first.

## Next Steps

Now that you've completed the basic setup, here are the recommended next steps:

- **Set up your lab infrastructure**: Follow the [Setting Up Lab Infrastructure tutorial]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure) to properly configure your lab's setups, equipment, inventories, and consumable stocks
- **Learn project management**: Read [Managing Projects]({{site.baseurl}}/tutorials/managing-projects) to understand how to effectively organize and collaborate on research projects
- **Configure team access**: Review [Managing Groups]({{site.baseurl}}/tutorials/managing-groups) to set up proper permissions and team collaboration
- **Plan your experiments**: Explore [Behavioral Assays]({{site.baseurl}}/tutorials/behavioral-assays) to define standardized experimental protocols for your studies
- **Set up data storage**: Follow [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage) to link your metadata to actual data files for seamless analysis workflows
- **Work with AI**: See [Working with AI]({{site.baseurl}}/tutorials/working-with-ai) for the in-app assistant, the MCP server and the agent skills
