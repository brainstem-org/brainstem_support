---
layout: default
title: Manage Groups
parent: Tutorials
nav_order: 3
---

# Managing Groups in BrainSTEM
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Groups in BrainSTEM are essential for organizing lab members and managing permissions. This tutorial will guide you through the process of managing groups effectively, including understanding different permission levels and performing common management tasks.

## Group Permission Levels

BrainSTEM groups have three levels of membership:

1. **Members (Basic)**
   - Can view group resources
   - Inherit project permissions assigned to the group
   - Can leave the group voluntarily
   - Cannot modify group settings or membership

2. **Managers**
   - All Member permissions
   - Can add new members
   - Can remove existing members
   - Can create member invitations
   - Cannot modify group settings

3. **Owners**
   - All Manager permissions
   - Can associate group with laboratory
   - Can rename the group
   - Can add/remove managers
   - Can modify group settings
   - Can grant manager/owner privileges to members

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## Accessing Group Management

1. Navigate to the Groups page:
   - Visit [https://www.brainstem.org/private/auth/group/](https://www.brainstem.org/private/auth/group/)
   - Or click the Users icon in the top navigation bar and select "Groups"

2. Find your group in the list and click on it to access management options

## Manager Capabilities

### Adding New Members

1. Go to your group's management page
2. Click the **Invite user** button
3. Fill in the required information for the invitation
4. Submit the invitation

### Checking Invitation Status

1. Navigate to [https://www.brainstem.org/private/users/groupmembershipinvitation/](https://www.brainstem.org/private/users/groupmembershipinvitation/)
2. View the status of all pending invitations
3. Monitor which invitations have been accepted or are still pending

### Removing Members

1. Access your group's member list
2. Locate the user(s) you want to remove
3. Check the checkbox next to their name(s)
4. Click the Save button to confirm the removal

## Owner Capabilities

### Managing Privileges

1. Access your group's member list
2. Locate the member(s) you want to modify
3. Check/uncheck the appropriate boxes:
   - "Managers" checkbox for manager privileges
   - "Owners" checkbox for owner privileges
4. Click Save to apply the changes

### Associating with Laboratory

Group owners can link their group to a laboratory:

1. Access your group's settings page
2. Click the "Add Laboratory" button
3. Fill in details about the lab, including the PI, Institution, Website, City and Country
4. Click Save to apply the association

### Renaming the Group

Group owners can change the group name:

1. Go to your group's main page
2. Click the "Edit" button 
3. Locate the "Name" field at the top of the form
4. Enter the new group name
5. Click Save to confirm the changes

{: .important }
> Choose group names carefully as they should clearly identify your lab or research team. Other users will see this name when collaborating on projects.

## Next Steps

After setting up your research groups, you're ready to organize your research:

- **Create collaborative projects**: Use [Managing Projects]({{site.baseurl}}/tutorials/managing-projects) to organize your research and enable team collaboration
- **Set up your lab infrastructure**: Follow [Setting Up Lab Infrastructure]({{site.baseurl}}/tutorials/setting-up-lab-infrastructure) to configure equipment, setups, and inventories that your group can access
- **Configure data storage**: Set up [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage) locations that your team can use for data management
- **Start documenting experiments**: Begin with [Get Started]({{site.baseurl}}/tutorials/get_started) to create your first subjects and sessions with proper group permissions
- **Plan for data sharing**: Learn about [Share Data Publicly]({{site.baseurl}}/tutorials/sharing-project-publicly) when you're ready to make research openly accessible
