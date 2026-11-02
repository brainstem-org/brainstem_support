---
layout: default
title: Manage Projects
parent: Tutorials
nav_order: 3
---

# Managing Projects
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

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
   - Or click **Projects** in the left navigation menu
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

1. Click the **Users, groups & invitations** icon in the header and select **Invitations & Requests**
2. Review the **Projects** section; it lists invitations sent but not yet accepted. Invitations to people without an account expire after 14 days.

### Managing Membership

**To remove members or groups from your project:**

1. Access the project's user/group list in the management page
2. To remove members or groups:
   - Tick the **Remove** box in their row
   - Click **Save** to confirm removal

{: .important }
> Removing a member or group will immediately revoke their access to the project.

## Owner Capabilities

As a project owner, you have full administrative control including the ability to promote members, modify project settings, and manage all aspects of the project.

### Setting Permission Levels

**To modify member permission levels:**

![The project's Manage permissions page: a member (Alex Sample, Contributor) and a group (SAMPLE Lab, Contributor, Manager and Owner) with their Contributor, Manager, Owner and Remove boxes, and the Invite user and Invite group buttons.]({{site.baseurl}}/assets/images/screenshots/project-manage-members.png)
{: .screenshot }
*The project's Manage permissions page: a member (Alex Sample, Contributor) and a group (SAMPLE Lab, Contributor, Manager and Owner) with their Contributor, Manager, Owner and Remove boxes, and the Invite user and Invite group buttons.*

1. Access the project member list in the management page
2. For each member or group, you can assign elevated permissions by checking the appropriate boxes:

| Checkbox | Permission Granted | Capabilities |
|----------|-------------------|-------------|
| **Contributor** | Contributor | Create, edit, and delete project content |
| **Manager** | Manager | All Contributor permissions plus member management |
| **Owner** | Owner | Full administrative control |

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
| **Tags** | Free labels for filtering |
| **Publications** | Papers that came out of the project (see below) |
| **Name used in storage** | Folder name of the project in your data storage |
| **Project visibility** | Switch between **Private** and **Public** |

4. Click **Save** to apply changes

{: .note }
> Changes to public access settings will affect project visibility across BrainSTEM. See [Sharing Project Publicly]({{site.baseurl}}/tutorials/sharing-project-publicly) for more details on making projects public.

### Linking Publications by DOI

1. On the project form, open the **Publications** field and click the **+** to add a publication.
2. Enter the DOI and click **Lookup DOI**. Title, authors, abstract, volume, URL and date are filled in from Crossref; the journal is selected when it exists.
3. Save the publication and select it on the project.

Publications are shared catalog entries: a new one is reviewed by the BrainSTEM team but can be used by you right away. The DOI appears in the STAR Methods report and in NWB files as `related_publications`. The **Publication coverage** dashboard widget shows which of your projects have one.

## Exporting a Project

Any project member can download the project from its details page with **Export**.

### Download project data
{: .no_toc}

1. Open the project's details page and click **Export** → **Download project data**.
2. Choose the **File format**:
   - **JSON**: every record of the project you can read, in the versioned export format (2.1). This is the input for the [NWB converter]({{site.baseurl}}/tools/brainstem-nwb/) and for scripts.
   - **XLS**: a workbook with one sheet per record kind (Project, Subjects, Sessions, Collections, Cohorts, Data acquisition, Epochs, Manipulations, Experimental interfaces, Procedures, Specimen procedures, Behavioral assays, Data storage, Setups, Equipment). Always the whole project.
3. Choose the **Contents**: **Whole project**, or one session with everything it touches (JSON only).
4. For large projects tick **Compress JSON output (gzip)** and **Prepare in the background and email me when it is ready**. The file is built by a worker, you receive an email, and the download is listed under **Your background exports** for 7 days.
5. Click **Download**.

Lab resources (setups, stocks, protocols) are included only when the project uses them and you can read them; the export lists the ones you cannot read. Uploaded files are referenced by name only. See [Exports]({{site.baseurl}}/api/export/) for the format and the API equivalents.

### STAR Methods report
{: .no_toc}

**Export** → **STAR Methods (preview)** opens a draft methods section in the browser; **STAR Methods (.docx)** downloads it as Word. The draft contains a **Key Resources Table** (organisms and strains, antibodies, chemicals and viruses, deposited data, with suppliers and RRIDs), **Experimental Model and Study Participant Details**, **Method Details** built from procedures, interfaces, sessions and templates, and a **Missing Information Report** listing what BrainSTEM could not fill. Statistics, randomization and blinding statements are placeholders marked "[Author review required]".

### Other exports
{: .no_toc}

**Print / Save as PDF** and **Download Word** on any details page produce a readable report of that record. **Export selected entries** in a list does the same for several records at once.

## Seeing the Project as a Graph

- **Graph** on the project's details page opens the **Data graph**: your entries counted in boxes by kind, narrowed to what belongs to this project. Open a box to list its entries and pick one to narrow further. The same view is under **Tools** → **Data graph**.
- The **Interactive data model** (Help menu, or the Graph tab of every help modal) shows the models, their fields and how permissions flow from the project. A copy is on this site: [Interactive data model]({{site.baseurl}}/datamodel/?view=interactive).

## Next Steps

With your projects properly configured, you can start documenting your research:

- **Set up experimental protocols**: Define [Behavioral Assays]({{site.baseurl}}/tutorials/behavioral-assays) for standardized experimental procedures within your projects
- **Configure data management**: Set up [Managing Data Storage]({{site.baseurl}}/tutorials/managing-data-storage) to link project data to actual files for analysis workflows  
- **Start documenting experiments**: Follow complete experimental workflows like [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow) or [Two-Photon Imaging Workflow]({{site.baseurl}}/tutorials/two-photon-imaging-workflow)
- **Enable programmatic access**: Master the [Python API tool]({{site.baseurl}}/tools/python-api-tool) or [MATLAB API tool]({{site.baseurl}}/tools/matlab-api-tool) to programmatically access your project data
- **Enable open science**: Use [Sharing Project Publicly]({{site.baseurl}}/tutorials/sharing-project-publicly) to make your project data accessible to the research community
- **Convert to NWB**: Follow [Exporting to NWB]({{site.baseurl}}/tutorials/exporting-to-nwb) to turn the JSON export into NWB files