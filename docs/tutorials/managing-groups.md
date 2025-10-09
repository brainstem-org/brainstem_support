---
layout: default
title: Manage Groups
parent: Tutorials
nav_order: 2
---

# Managing Groups
{: .no_toc}

## Introduction

Groups in BrainSTEM are essential for organizing lab members and managing permissions. This tutorial will guide you through the process of managing groups effectively, including understanding different permission levels and performing common management tasks.

## Group Permission Levels

BrainSTEM groups have three levels of membership, each with increasing levels of control:

| Permission Level | Capabilities |
|-----------------|-------------|
| **Members** | View group resources<br>Inherit project permissions assigned to the group<br>Leave the group voluntarily<br>**Cannot** modify group settings or membership |
| **Managers** | All Member permissions<br>Add new members to the group<br>Remove existing members from the group<br>Create and manage member invitations<br>**Cannot** modify group settings or grant privileges |
| **Owners** | All Manager permissions<br>Associate group with laboratory information<br>Rename the group<br>Promote members to Manager or Owner roles<br>Modify all group settings<br>Full administrative control |

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more about the BrainSTEM permission system. 

## Accessing Group Management

**To access your group's management page:**

1. Navigate to the Groups page:
   - Visit [https://www.brainstem.org/private/auth/group/](https://www.brainstem.org/private/auth/group/)
   - Or click the **Users** icon in the top navigation bar and select **Groups**

2. Find your group in the list and click on it to access management options

## Manager Capabilities

As a group manager, you can add and remove members, as well as manage invitations.

### Adding New Members

**To invite a new member to your group:**

1. Go to your group's management page
2. Click the **Invite user** button
3. Select the user from the dropdown list. 
4. Click **Submit** to send the invitation

{: .note }
> The invited user will receive an email notification and must accept the invitation to join the group.

### Checking Invitation Status

**To monitor pending invitations:**

1. Navigate to [https://www.brainstem.org/private/users/groupmembershipinvitation/](https://www.brainstem.org/private/users/groupmembershipinvitation/)
2. View the status of all pending invitations
3. Monitor which invitations have been accepted or are still pending

### Removing Members

**To remove members from your group:**

1. Access your group's member list
2. Locate the user(s) you want to remove
3. Check the checkbox next to their name(s)
4. Click the **Save** button to confirm the removal

{: .important }
> Removing a member will revoke their access to all group resources.

## Owner Capabilities

As a group owner, you have full administrative control including the ability to promote members, and modify group settings.

### Managing Member Privileges

**To promote members to Manager or Owner roles:**

1. Access your group's member list
2. Locate the member(s) you want to modify
3. Check/uncheck the appropriate boxes:
   - **Managers** checkbox: Grants manager privileges (can add/remove members)
   - **Owners** checkbox: Grants owner privileges (full administrative control)
4. Click **Save** to apply the changes

{: .important }
> Owner privileges should be granted carefully as they provide complete control over the group, including the ability to modify all settings and member roles.

### Associating with Laboratory

**To link your group to laboratory information:**

Group owners can associate their group with institutional and Principal investigators for better organization and identification.

1. Access your group's settings page
2. Click the **Add Laboratory** button
3. Fill in the laboratory details:

| Field | Description |
|-------|-------------|
| **Principal investigators** | Select from group members |
| **Website** | Lab website URL (optional) |
| **Department** | Department name |
| **Institution** | University or research institution name |
| **City** | Laboratory location city |
| **Country** | Laboratory location country |

4. Click **Save** to apply the association

{: .note }
> Laboratory associations help other users identify your research group and can be useful for collaboration and data sharing.

### Renaming the Group

**To change your group's name:**

1. Go to your group's main page
2. Click the **Edit** button 
3. Locate the **Name** field at the top of the form
4. Enter the new group name
5. Click **Save** to confirm the changes

{: .important }
> Choose group names carefully as they should clearly identify your lab or research team. Other users will see this name when collaborating on projects.

## Next Steps

After setting up your research groups, you're ready to organize your research:

- **Create collaborative projects**: Use [Managing Projects]({{site.baseurl}}/tutorials/managing-projects) to organize your research and enable team collaboration
- **Set up your lab infrastructure**: Follow [Setting Up Lab Infrastructure]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure) to configure equipment, setups, and inventories that your group can access
- **Configure data storage**: Set up [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage) locations that your team can use for data management
- **Start documenting experiments**: Begin with [Get Started]({{site.baseurl}}/tutorials/get_started) to create your first subjects and sessions with proper group permissions
- **Plan for data sharing**: Learn about [Share Data Publicly]({{site.baseurl}}/tutorials/sharing-project-publicly) when you're ready to make research openly accessible
