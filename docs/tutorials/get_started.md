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
{: .no_toc}

First thing to do is [create an account](https://www.brainstem.org/register/). Provide your name, email, and a secure password. Once you have created an account you can visit your profile from the top menu to add a profile image, and link to your orcid account, your google scholar profile, and your website.

## Create or Join a Group
{: .no_toc}

Next, you need to either create a new group for your lab or join an existing one. Groups in BrainSTEM help organize lab members and manage permissions for projects and resources.

### Accessing Groups
{: .no_toc}

1. From your dashboard, locate and click the Users icon in the top right corner of the screen
2. Select *Groups* from the dropdown menu
![Groups menu]({{site.baseurl}}/assets/images/tutorials/user_group.png)

### Managing Group Membership
{: .no_toc}

Once on the Groups page, you have two options:

<div class="code-example" markdown="1">

#### Option 1: Create a New Group
{: .no_toc}

If your lab doesn't have a group yet:
1. Click the *Add group* button in the top right corner
2. Fill in the required information for your new group
![Add group button]({{site.baseurl}}/assets/images/tutorials/add_group.png)

#### Option 2: Join an Existing Group
{: .no_toc}

If your lab already has a group:
1. Click on the group name from the list of available groups
2. On the group's detail page, click the *Request membership of group* button
3. Wait for a group manager to approve your request
![Request group membership]({{site.baseurl}}/assets/images/tutorials/request_member_lab.png)

</div>

### Managing Group Membership Requests
{: .no_toc}

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

Before creating subjects and sessions, set up personal attributes that describe your setups, inventories and behavioral paradigms. These provide standardized options for your experiments.

### Define behavioral paradigms to describe the behavioral conditions of your subjects
{: .no_toc}

1. Navigate to *Personal Attributes* → *Behavioral paradigms* in the left menu
2. Click *Add behavioral paradigm*
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
   - Go to *Modules* → *Equipment*
   - Add devices like "Intan RHD2000", "Behavior Camera", "LED Arrays"
   - Associate equipment with appropriate setups
   
### Set up inventories to track your lab resources
{: .no_toc}

1. Go to *Personal Attributes* → *Inventories*
2. Click *Add inventory*
3. Create inventory categories (e.g., "Silicon Probes", "Virus stocks")
4. **Add consumable stocks to your inventories:**
   - Navigate to *Modules* → *Consumable stocks*
   - Add specific items like probe models, virus batches, drug concentrations
   - Link them to appropriate inventories

{: .note }
> These personal attributes will appear as selectable options when creating sessions, subjects, and experiments. Setting them up first streamlines your data entry process.

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

## Already Have Data? Import It Quickly!

**Don't want to enter everything manually?** If you already have your research data in spreadsheets, our powerful import tool can save you hours of manual data entry!

**Why use the import tool?**

- **Save time** - Import dozens or hundreds of records at once
- **Easy to use** - Download a template, fill in your data, and upload
- **Comprehensive** - Supports all major data types (subjects, sessions, procedures, and more!)

**Get started in 3 simple steps:**

1. **Download a template** for your data type
2. **Fill in your data** following the provided examples
3. **Upload and review** - we'll check for errors and show you the results

**Ready to import?** Check out our complete [Import Tool Guide]({{site.baseurl}}/webinterface/import-tool/) for detailed instructions and templates!

## Build Your Own Experiment

BrainSTEM uses Personal Attributes and Modules to document your experimental procedures. Below is a recommended order for setting up your experiment components.

![Describe experiment]({{site.baseurl}}/assets/images/tutorials/describe_experiment.gif)

### Available Components
{: .no_toc}

STEM models
- [Subjects]({{site.baseurl}}/datamodel/stem/subject/)
   - [Procedures]({{site.baseurl}}/datamodel/modules/procedure/)
   - [Procedure logs]({{site.baseurl}}/datamodel/modules/procedurelog/)
   - [Subject logs]({{site.baseurl}}/datamodel/modules/subjectlog/)

- [Sessions]({{site.baseurl}}/datamodel/stem/session/)
   - [Behaviors]({{site.baseurl}}/datamodel/modules/behavior/)
   - [Data acquisition]({{site.baseurl}}/datamodel/modules/dataacquisition/)
   - [Manipulations]({{site.baseurl}}/datamodel/modules/manipulation/)

Personal Attributes:
- [Behavioral paradigms]({{site.baseurl}}/datamodel/personal_attributes/behavioralparadigm/)
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

## Next Steps

Now that you've completed the basic setup, here are the recommended next steps:

- **Set up your lab infrastructure**: Follow the [Setting Up Lab Infrastructure tutorial]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure) to properly configure your lab's setups, equipment, inventories, and consumable stocks
- **Learn project management**: Read [Managing Projects]({{site.baseurl}}/tutorials/managing-projects) to understand how to effectively organize and collaborate on research projects
- **Configure team access**: Review [Managing Groups]({{site.baseurl}}/tutorials/managing-groups) to set up proper permissions and team collaboration
- **Plan your experiments**: Explore [Behavioral Paradigms]({{site.baseurl}}/tutorials/behavioral-paradigms) to define standardized experimental protocols for your studies
- **Set up data storage**: Follow [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage) to link your metadata to actual data files for seamless analysis workflows
