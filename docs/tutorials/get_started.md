---
layout: default
title: Get started!
parent: Tutorials
nav_order: 1
---

# Get Started with BrainSTEM
{: .no_toc}

This tutorial takes you from a new account to your first project, subject and session, following the **Getting started** checklist on the dashboard. At the end you have a group, a project, a subject and a session that your lab members can see, and the checklist shows those steps as done.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Create an account

1. [Create an account](https://www.brainstem.org/register/) with your name, email and a password.
2. Confirm your email address from the message BrainSTEM sends you.
3. Optional: open your profile from the top menu to add a profile image and links to your ORCID, Google Scholar profile and website (see [User profile]({{site.baseurl}}/webinterface/user-profile/)).

## Follow the "Getting started" checklist

Your dashboard opens with a **Getting started** card that tracks the lab basics in three groups: **Collaborate** (join or create a group, invite your first teammate), **Prepare your environment** (add your first setup, behavioral assay, inventory and data storage) and **Structure your work** (create your first project, subject and session). The sections below follow the same three groups. Once you are done, remove the card with **Add widget** → **Manage widgets**.

![The Getting started card with eight of nine steps done: the open step, Invite your first teammate, is at the top, and the completed steps are listed below in their three groups]({{site.baseurl}}/assets/images/screenshots/dashboard-getting-started.png)
{: .screenshot }
*The Getting started card with eight of nine steps done: the open step, Invite your first teammate, is at the top, and the completed steps are listed below in their three groups*

## Collaborate: create or join a group

A group is your lab in BrainSTEM. Projects and personal attributes are shared with groups, so every member gets access at once.

1. Click the **Users, groups & invitations** icon in the top right corner and select *Groups*.
2. If your lab already has a group, open it and click *Request membership*. A group manager approves the request.
3. If it does not, click *Add group* and fill in the group's name. You become its owner.

Group managers find pending requests under **Users, groups & invitations** → *Invitations & Requests* → *Group membership requests*. To invite your first teammate and to give members manager or owner roles, follow [Managing groups]({{site.baseurl}}/tutorials/managing-groups).

Give at least two people in the lab the manager role, so requests and invitations are never blocked by one person's absence.

## Prepare your environment

Setups, behavioral assays, inventories and data storage are your lab's **personal attributes**: the rigs, tasks, stocks and storage locations your records point to. You can create projects, subjects and sessions without them, and add them later. Procedures, behaviors and data acquisitions do need them, so set them up before you record a full experiment:

| Checklist step | What it describes | How to set it up |
|---|---|---|
| **Add your first setup** | A physical rig or room and its equipment | [Setting up lab infrastructure]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure) |
| **Add your first behavioral assay** | A task or behavioral condition sessions refer to | [Behavioral assays]({{site.baseurl}}/tutorials/behavioral-assays) |
| **Add your first inventory** | Your lab's stocks of probes, viruses and drugs | [Setting up lab infrastructure]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure) |
| **Add your first data storage** | Where the data files of your sessions live | [Managing data storage]({{site.baseurl}}/tutorials/managing-data-storage) |

## Structure your work: create your first project

A project holds your subjects and sessions and decides who can see them.

1. Click *Projects* in the left navigation menu.
2. Click *Add project* in the top right corner.
3. Enter the **Project name** and choose the **Authenticated groups** that should have access. The groups you select get Contributor access.
4. Click **Create and continue**. Everything else can be filled in on the form that opens.

![The add project form filled in: the project name and the authenticated groups, then Create and continue.]({{site.baseurl}}/assets/images/screenshots/get-started-project-form.png)
{: .screenshot }
*The add project form filled in: the project name and the authenticated groups, then Create and continue.*

The project's fields are described on the [Project]({{site.baseurl}}/datamodel/stem/project/) page.

## Create your first subject

A subject is one experimental animal.

1. Click *Subjects* in the left navigation menu.
2. Click *Add subject* in the top right corner.
3. Enter the **Subject name**, choose your project under **Projects**, and set **Sex**, **Species** and **Status**. **Strain** is optional; its list shows only strains of the chosen species.
4. Click **Create and continue**.

![The add subject form filled in: name, project, sex, species, strain and status, then Create and continue.]({{site.baseurl}}/assets/images/screenshots/get-started-subject-form.png)
{: .screenshot }
*The add subject form filled in: name, project, sex, species, strain and status, then Create and continue.*

{% include walkthrough.html slug="get-started-create-subject" caption="Creating a subject: name, project, sex, species, strain and status; the strain list follows the species. The video ends with the pointer on Create and continue." %}

{: .important }
> A subject is visible to the people of its projects only. If you leave out a project, its members cannot see the subject.

If your species or strain is missing, submit it from the *Taxonomies* menu (see [Submitting resources and taxonomies]({{site.baseurl}}/tutorials/submit-resource-and-taxonomies)). Working with slices, sections or cultures instead of live animals? Create a **specimen set** instead; see the [Ex vivo workflow]({{site.baseurl}}/tutorials/specimen-workflow). All subject fields are described on the [Subject]({{site.baseurl}}/datamodel/stem/subject/) page.

## Create your first session

A session records one occasion with a subject: a recording, an imaging run, a training day.

1. Click *Sessions* in the left navigation menu.
2. Click *Add session* in the top right corner.
3. Enter the **Session name**, set **Session type** to *Subject* (*Specimen* is for ex vivo material), choose your project under **Projects**, pick your subject under **Subjects** and set the **Status**.
4. Click **Create and continue**. The session's behaviors, data acquisitions, manipulations and epochs are added on the tabs of the form that opens; the workflow tutorials show how.

![The add session form: name, session type Subject and project, with the Subjects list open to pick the subjects of the session.]({{site.baseurl}}/assets/images/screenshots/get-started-session-form.png)
{: .screenshot }
*The add session form: name, session type Subject and project, with the Subjects list open to pick the subjects of the session.*

{% include walkthrough.html slug="get-started-create-session" caption="Creating a session: name, session type, project, the subjects it was run on and status; the video ends with the pointer on Create and continue." %}

All session fields are described on the [Session]({{site.baseurl}}/datamodel/stem/session/) page.

## Check your result

- The **Getting started** card on your dashboard shows the project, subject and session steps as done.
- *Sessions* lists your new session, and its details page names your subject and project.
- Members of the groups you chose for the project see the same entries.

## Two shortcuts

- **Find entries by asking.** The **AI assistant**, from the corner button on every private page, answers plain-language questions such as "Show sessions with silicon probe implants in the hippocampus". It only returns entries you may read and never changes anything. See [AI assistant]({{site.baseurl}}/webinterface/ai-assistant/).
- **Already have data in spreadsheets?** The [import tool]({{site.baseurl}}/webinterface/import-tool/) creates subjects, sessions, procedures and other entries from a filled-in template.

## Next steps

**Next:** [Managing groups]({{site.baseurl}}/tutorials/managing-groups): invite your lab and give members the right roles.

Then, in order:

1. [Setting up lab infrastructure]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure): setups, equipment, inventories and consumable stocks.
2. [Behavioral assays]({{site.baseurl}}/tutorials/behavioral-assays) and [Managing data storage]({{site.baseurl}}/tutorials/managing-data-storage).
3. A complete experiment: the [Electrophysiology]({{site.baseurl}}/tutorials/electrophysiology-workflow), [Two-photon imaging]({{site.baseurl}}/tutorials/two-photon-imaging-workflow) or [Ex vivo]({{site.baseurl}}/tutorials/specimen-workflow) workflow.

To see how all kinds of entries connect, read [How BrainSTEM structures an experiment]({{site.baseurl}}/datamodel/).
