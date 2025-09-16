---
layout: default
title: Manage Projects
parent: Tutorials
nav_order: 4
---

# Managing Projects in BrainSTEM
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Project Permission Levels

BrainSTEM projects implement four distinct permission levels that can be assigned to both individual users and groups:

1. **Members (Basic)**
   - Read access to project-related subjects, sessions, and modules
   - Can view but not modify project content
   - Can leave the project voluntarily

2. **Contributors**
   - All Member permissions
   - Can create new project-related content
   - Can edit existing project content
   - Can delete project-related models

3. **Managers**
   - All Contributor permissions
   - Can add new project members
   - Can remove project members
   - Can add and remove project groups

4. **Owners**
   - All Manager permissions
   - Can modify project details
   - Can add/remove managers
   - Full control over project settings

Visit the [permissions page]({{"datamodel/permissions/"|absolute_url}}) to learn more. 

## Accessing Project Management

1. Navigate to the Projects page:
   - Visit [https://www.brainstem.org/private/stem/project/](https://www.brainstem.org/private/stem/project/)
   - Select the project you want to manage
   - Click the "Manage" button in the top right corner

## Manager Capabilities

### Adding New Members

1. Go to your project's management page
2. Click the **Invite user** or **Invite group** button
3. Complete the invitation form
4. Submit the invitation

### Tracking Invitations

1. Visit [https://www.brainstem.org/private/users/projectmembershipinvitation/](https://www.brainstem.org/private/users/projectmembershipinvitation/)
2. Monitor pending and accepted invitations

### Managing Membership

1. Access the project's user/group list
2. To remove members or groups:
   - Select the checkbox next to their name
   - Click Save to confirm removal

## Owner Capabilities

### Setting Permission Levels

1. Access the project member list
2. For each member, you can assign:
   - Contributor permissions (Change permissions checkbox)
   - Manager permissions (Managers checkbox)
   - Owner permissions (Owners checkbox)
3. Click Save to apply changes

### Project Settings Management

1. Edit project details
2. Modify project configuration
3. Update project metadata

## Next Steps

With your projects properly configured, you can start documenting your research:

- **Set up experimental protocols**: Define [Behavioral Paradigms]({{site.baseurl}}/tutorials/behavioral-paradigms) for standardized experimental procedures within your projects
- **Configure data management**: Set up [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage) to link project data to actual files for analysis workflows  
- **Start documenting experiments**: Follow complete experimental workflows like [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow) or [Two-Photon Imaging Workflow]({{site.baseurl}}/tutorials/two-photon-imaging-workflow)
- **Enable programmatic access**: Master the [Python API tool]({{site.baseurl}}/tutorials/python-api-tool) or [MATLAB API tool]({{site.baseurl}}/tutorials/matlab-api-tool) to programmatically access your project data
- **Enable open science**: Use [Sharing Project Publicly]({{site.baseurl}}/tutorials/sharing-project-publicly) to make your project data accessible to the research community