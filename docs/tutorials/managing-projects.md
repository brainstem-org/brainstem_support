---
layout: default
title: Manage Projects
parent: Tutorials
nav_order: 6
---

# Managing Projects
{: .no_toc}

A project holds a study's subjects, sessions and procedures, and decides who can read and change them. This tutorial gives your lab group and individual collaborators a level on a project, changes the levels, edits the project's details and links its publication. At the end, everyone who works on the study has the access they need.

**Prerequisites**: a project you own (see [Get started!]({{site.baseurl}}/tutorials/get_started)) and a lab group (see [Manage Groups]({{site.baseurl}}/tutorials/managing-groups)).

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Step 1: Open the project's Manage permissions page

1. Click **Projects** in the left menu, or go to [www.brainstem.org/private/stem/project/](https://www.brainstem.org/private/stem/project/).
2. Open the project.
3. Click **Manage**. The **Manage permissions** page opens. Everyone with access can open it; only Managers and Owners can change it.

![The project's Manage permissions page: a member (Alex Sample, Contributor) and a group (SAMPLE Lab, Contributor, Manager and Owner) with their Contributor, Manager, Owner and Remove boxes, and the Invite user and Invite group buttons.]({{site.baseurl}}/assets/images/screenshots/project-manage-members.png)
{: .screenshot }
*The project's Manage permissions page: a member (Alex Sample, Contributor) and a group (SAMPLE Lab, Contributor, Manager and Owner) with their Contributor, Manager, Owner and Remove boxes, and the Invite user and Invite group buttons.*

## Step 2: Invite your lab group

1. Click **Invite group**.
2. Type your group's name and pick it from the suggestions.
3. As an Owner, tick **Contributor** under **Extra permissions**, so that your lab members can add subjects and sessions.
4. Click **Send invitation**.

{: .important }
> Leaving all boxes unticked invites the group as Members, who can only read the project. Managers who are not Owners do not see **Extra permissions**, so their invitations always grant Member; an Owner must raise the level afterwards.

The group's managers receive an email, and any member of the group can accept the invitation under **Invitations & Requests**. Every current and future member of the group then holds the group's level. Invite an individual collaborator the same way with **Invite user** and their email address; people without an account receive a sign-up link that is valid for 14 days.

## Step 3: Change or remove levels

1. On the **Manage permissions** page, tick or untick **Contributor**, **Manager** or **Owner** in a user's or group's row, or tick **Remove**.
2. Click **Save**. "Permissions updated successfully!" confirms the change.

{: .important }
> Removing a user or group immediately revokes their access. Only Owners can grant or take away Manager and Owner, and a project always keeps at least one Owner. An Owner can change the project's details, make it public and delete it, so give the Owner level sparingly.

The invitation flow, the messages and leaving a project are described on [Sharing and memberships]({{site.baseurl}}/webinterface/sharing-and-memberships/); what each level allows is on the [Permissions]({{site.baseurl}}/datamodel/permissions/#project-permissions) page.

## Step 4: Edit the project's details

You need Owner on the project.

1. Open the project and click **Edit**.
2. Change the **Description** or **Tags**, or the **Project name in storage** under **Online repositories** if your data folders use another name.
3. Click **Save**.

All fields are described on the [Projects]({{site.baseurl}}/datamodel/stem/project/) page. **Project visibility** makes the project public; see [Share data publicly]({{site.baseurl}}/tutorials/sharing-project-publicly) before switching it.

## Step 5: Link the publication

1. On the project's edit page, click the **+** next to **Publications**.
2. Enter the DOI and click **Lookup DOI**, as described in [Resources & Taxonomies]({{site.baseurl}}/tutorials/submit-resource-and-taxonomies#step-2-submit-a-new-entry), and save the publication.
3. Select it in **Publications** and click **Save**.

The DOI then appears in the project's STAR Methods report and NWB files. The **Publication coverage** dashboard widget shows which of your projects have a publication.

## End state

Your lab group and collaborators hold the roles they need on the project, and the project carries its description and publication. Contributors can now add subjects and sessions to it.

To download the project or draft a methods section, use **Export** on the project's page; see [Exports and reports]({{site.baseurl}}/webinterface/exports-and-reports/). **Graph** on the project's page shows its entries counted by kind; the [Interactive data model]({{site.baseurl}}/datamodel/?view=interactive) shows how permissions flow from the project.

## Next steps

- **Next:** [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow): document a complete experiment in the project.
- [Two-Photon Imaging Workflow]({{site.baseurl}}/tutorials/two-photon-imaging-workflow) and [Ex vivo workflow]({{site.baseurl}}/tutorials/specimen-workflow): other complete workflows.
- [Share data publicly]({{site.baseurl}}/tutorials/sharing-project-publicly): publish the project when the study is out.
- Data model: [Projects]({{site.baseurl}}/datamodel/stem/project/) and [Permissions]({{site.baseurl}}/datamodel/permissions/).
- [Exporting to NWB]({{site.baseurl}}/tutorials/exporting-to-nwb): turn the project's export into NWB files.
