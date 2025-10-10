---
layout: default
title: Manage Projects
parent: Tutorials
nav_order: 3
---

# Managing Projects
{: .no_toc}

## Project Permission Levels

BrainSTEM projects implement four distinct permission levels that can be assigned to both individual users and groups. Each level builds on the previous one with additional capabilities:

| Permission Level | Capabilities |
|-----------------|-------------|
| **Members** | View project-related subjects, sessions, and modules<br>Read-only access to all project content<br>Leave the project voluntarily<br>**Cannot** create, edit, or delete content |
| **Contributors** | All Member permissions<br>Create new project-related content (subjects, sessions, etc.)<br>Edit existing project content<br>Delete project-related models<br>**Cannot** manage membership or project settings |
| **Managers** | All Contributor permissions<br>Add new individual members to the project<br>Remove individual members from the project<br>Add and remove project groups<br>Manage project invitations<br>**Cannot** modify core project settings or grant Owner privileges |
| **Owners** | All Manager permissions<br>Modify project details and metadata<br>Promote members to Manager or Owner roles<br>Change project visibility and access settings<br>Full administrative control over the project |

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more about the BrainSTEM permission system. 

## Accessing Project Management

**To access your project's management page:**

1. Navigate to the Projects page:
   - Visit [https://www.brainstem.org/private/stem/project/](https://www.brainstem.org/private/stem/project/)
   - Or go to **Stem** → **Projects** in the navigation menu
2. Select the project you want to manage from the list
3. Click the **Manage** button in the top right corner

{: .note }
> You must have Manager or Owner permissions to access the project management interface.

## Manager Capabilities

As a project manager, you can add and remove members and groups, as well as manage invitations.

### Adding New Members

**To invite users or groups to your project:**

1. Go to your project's management page
2. Click either:
   - **Invite user** button to invite an individual researcher
   - **Invite group** button to invite an entire research group
3. Complete the invitation form:
   - **Email** (for users): The recipient's email address
   - **Group** (for groups): Select the group from the dropdown
   - **Permission Level**: Select Member, Contributor, or Manager
   - **Message** (optional): Personal note explaining the invitation
4. Click **Submit** to send the invitation

{: .note }
> When inviting a group, all current and future members of that group will inherit the assigned permission level for this project.

### Tracking Invitations

**To monitor pending project invitations:**

1. Visit [https://www.brainstem.org/private/users/projectmembershipinvitation/](https://www.brainstem.org/private/users/projectmembershipinvitation/)
2. Review invitation status:
   - **Pending**: Invitation sent but not yet accepted

### Managing Membership

**To remove members or groups from your project:**

1. Access the project's user/group list in the management page
2. To remove members or groups:
   - Check the checkbox next to their name
   - Click **Save** to confirm removal

{: .important }
> Removing a member or group will immediately revoke their access to the project.

## Owner Capabilities

As a project owner, you have full administrative control including the ability to promote members, modify project settings, and manage all aspects of the project.

### Setting Permission Levels

**To modify member permission levels:**

1. Access the project member list in the management page
2. For each member or group, you can assign elevated permissions by checking the appropriate boxes:

| Checkbox | Permission Granted | Capabilities |
|----------|-------------------|-------------|
| **Change permissions** | Contributor | Create, edit, and delete project content |
| **Managers** | Manager | All Contributor permissions plus member management |
| **Owners** | Owner | Full administrative control |

3. Click **Save** to apply changes

{: .important }
> Owner permissions should be granted carefully as they provide complete control over the project, including the ability to modify settings and remove other owners.

### Managing Project Settings

**To modify core project details:**

Project owners can update fundamental project information and configuration:

1. Go to the project's main page
2. Click the **Edit** button
3. Modify project fields as needed:

| Field | Description |
|-------|-------------|
| **Name** | Project title visible to all members |
| **Description** | Detailed project overview and goals |
| **Keywords/Tags** | Search terms for project discovery |
| **Public Access** | Toggle project visibility (private/public) |
| **Authenticated Groups** | Default groups with project access |

4. Click **Save** to apply changes

{: .note }
> Changes to public access settings will affect project visibility across BrainSTEM. See [Sharing Project Publicly]({{site.baseurl}}/tutorials/sharing-project-publicly) for more details on making projects public.

## Next Steps

With your projects properly configured, you can start documenting your research:

- **Set up experimental protocols**: Define [Behavioral Paradigms]({{site.baseurl}}/tutorials/behavioral-paradigms) for standardized experimental procedures within your projects
- **Configure data management**: Set up [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage) to link project data to actual files for analysis workflows  
- **Start documenting experiments**: Follow complete experimental workflows like [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow)<!-- or [Two-Photon Imaging Workflow]({{site.baseurl}}/tutorials/two-photon-imaging-workflow)-->
- **Enable programmatic access**: Master the [Python API tool]({{site.baseurl}}/api-tools/python-api-tool) or [MATLAB API tool]({{site.baseurl}}/api-tools/matlab-api-tool) to programmatically access your project data
- **Enable open science**: Use [Sharing Project Publicly]({{site.baseurl}}/tutorials/sharing-project-publicly) to make your project data accessible to the research community