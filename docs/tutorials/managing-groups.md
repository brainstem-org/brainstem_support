---
layout: default
title: Manage Groups
parent: Tutorials
nav_order: 2
---

# Managing Groups
{: .no_toc}

A group is your lab in BrainSTEM: projects, setups, inventories and data storage are shared with a group, and every member inherits that access. This tutorial creates a group for your lab (or joins an existing one), invites your lab members, and shows how to manage their roles. At the end, your lab members are in one group that you can select in **Authenticated groups** when you create entries.

**Prerequisites**: a BrainSTEM account (see [Get started!]({{site.baseurl}}/tutorials/get_started)).

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Find the groups

Click the **Users, groups & invitations** icon in the top bar and select **Groups**, or go to [www.brainstem.org/private/auth/group/](https://www.brainstem.org/private/auth/group/). The list shows every group with its laboratory and number of users. Search it before creating a group: your lab may already have one.

## Option A: Create a group

1. On the Groups page, click **Add group**.
2. Enter the **Group name (must be unique)**. Add your institution to the name, for example "Sample Lab - NYU".
3. Click **Save**. The group's page opens. You are its first member, with the Manager and Owner roles.

## Option B: Request to join a group

1. On the Groups page, open the group of your lab.
2. Click **Request membership**. The message "Membership requested!" confirms it, and the group's managers are emailed.
3. Wait for a manager to accept. You are emailed when the request is accepted or denied, and you can withdraw it with **Cancel request** on the group's page.

## Invite a member

You need Manager on the group.

1. Open your group's page and click **Invite users**.
2. In **Invite user**, enter the email address of the person. People who already have an account are suggested as you type. People without an account receive a signup link.
3. As an Owner, you can tick **Manager** or **Owner** under **Extra permissions** to invite the person with that role.
4. Click **Send invitation**.

{: .note }
> The invited person must accept the invitation from the email or from **Invitations & Requests** before joining. Invitations to people without an account expire after 14 days. Pending invitations and requests are listed on the group's page, where managers can **Accept** or **Deny** requests and **Cancel invitation**. Answering invitations is described on [Sharing and memberships]({{site.baseurl}}/webinterface/sharing-and-memberships/#answering-an-invitation).

## Manage members and roles

1. Open your group's page and click **Manage**.
2. The member table has the columns **User**, **Manager**, **Owner** and **Remove**. Tick **Manager** or **Owner** to give a role, or **Remove** to take someone out of the group. Changing Managers and Owners needs the Owner role.
3. Click **Save**.

{: .important }
> Removing a member immediately revokes everything they could access through the group. A group always keeps at least one owner.

To leave a group yourself, click **Leave group** on the **Manage** page.

## Add laboratory details

You need Owner on the group.

1. Open your group's page and click **Add laboratory details**.
2. Select the **Principal investigators** from the group's members and enter the **Institution**. The other fields are described on the [Users]({{site.baseurl}}/datamodel/users/) page.
3. Click **Save**.

The laboratory details help other users recognize your group when they invite it to a project. To rename the group, click **Edit group** on its page.

## End state

Your lab group exists, you are its owner, and your lab members have joined or been invited. Select it in **Authenticated groups** whenever you create a setup, inventory, data storage or project, and every member gets Contributor access. What each role can do is listed on the [Permissions]({{site.baseurl}}/datamodel/permissions/#group-permissions) page.

## Next steps

- **Next:** [Setting Up Lab Infrastructure]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure): create the setups, equipment and inventories your group shares.
- [Manage Projects]({{site.baseurl}}/tutorials/managing-projects): give your group a level on a project.
- [Sharing and memberships]({{site.baseurl}}/webinterface/sharing-and-memberships/): invitations, requests and the Manage permissions page in detail.
- Data model: [Users, groups and laboratories]({{site.baseurl}}/datamodel/users/) and [Permissions]({{site.baseurl}}/datamodel/permissions/).
