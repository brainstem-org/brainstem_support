---
layout: default
title: Managing Data Storage
parent: Tutorials
nav_order: 6
---

# Managing Data Storage
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

This tutorial creates a data storage entry that describes where your data files live, links it to a session, and shows how to build the path to a session's files from the API in Python and MATLAB. At the end, every session can point at its folder on your server, cloud storage or public repository.

**Prerequisites**: an account in a group, and a project with at least one session (see [Get started!]({{site.baseurl}}/tutorials/get_started)). Field definitions are on the [Data storage data model page]({{site.baseurl}}/datamodel/personal_attributes/datastorage/).

## Understanding Data Storage Concepts

BrainSTEM's data storage system consists of three key components:

1. **Data Storage Locations**: Define where your data is physically stored (servers, cloud, local drives)
2. **Data Organization**: How your files are structured within the storage location
3. **Data Protocols**: How to access the data (paths, URLs, access methods)

## Creating a Data Storage Location

### Step 1: Navigate to Data Storage
{: .no_toc}

1. From the dashboard, go to *Personal Attributes* → *Data storage* in the left navigation menu
2. Click the *Add data storage* button in the top right corner

![A data storage's form: name, location, description, the data organization rows and the data protocols with their public access value.]({{site.baseurl}}/assets/images/screenshots/data-storage-form.png)
{: .screenshot }
*A data storage's form: name, location, description, the data organization rows and the data protocols with their public access value.*

### Step 2: Configure Basic Information
{: .no_toc}

Fill in the basic details:

| Field | Description |
|-------|-------------|
| **Name** | Descriptive name for your data storage (e.g., "Lab Server 01", "Cloud Storage Main"); unique across BrainSTEM |
| **Authenticated groups** | Groups that can access this data storage **(required)** |
| **Location** | Where the storage is, for example `nas://sample-lab/working` |
| **Description** | Details about stored data types and access requirements |

A data storage has no visibility switch of its own. Each data protocol (step 4) has its own **Public access** value, and the storage is public when one of its protocols is.

{: .important }
> Permissions are directly set on data storages. Data storage has four permission levels: membership (read access), contributors, managers, and owners.

{: .note }
> Choose names that clearly identify the storage location and its purpose. Other lab members will see these names when creating sessions.

### Step 3: Define Data Organization
{: .no_toc}

Configure how your data is organized within the storage location. This defines the hierarchy of folders/directories:

**Available organization elements:**
- Projects
- Collections
- Cohorts
- Subjects  
- Sessions
- Years

**Example organization structures:**

```
Subjects → Sessions
```

```
Projects → Subjects → Sessions
```

Add organization elements that match your lab's file structure conventions using the available element types.

### Step 4: Configure Data Storage Protocols
{: .no_toc}

Set up how to access your data storage. You can configure multiple protocols for the same storage location, e.g.:

| Storage Type | Protocol | Path Example | Public |
|--------------|----------|--------------|--------|
| **Local Drive** | Local Storage | `/Users/researcher/data/` | No |
| **Network/Server** | SMB/CIFS | `smb://uni.domain/group/data/` | No |
| **Cloud Storage** | Dropbox | `data/myproject` | No |
| **Public Repository** | HTTPS/Web | `https://dandiarchive.org/dandiset/123456/` | Yes |

{: .important }
> You can configure multiple protocols for the same data storage. This allows flexibility in how different users or systems access the same data.

## Assigning Data Storage to Sessions

### During Session Creation
{: .no_toc}

1. When creating a new session, locate the **Data storage** field
2. Select one or more of your configured data storage locations
3. Optionally, specify a **Name used in storage** - this is the folder/file name used in your actual storage system

### For Existing Sessions
{: .no_toc}

1. Navigate to the session you want to update
2. Click the *Edit* button
3. Select or change the **Data storage** field
4. Update the **Name used in storage** if needed
5. Save your changes

{: .note }
> The "Name used in storage" field helps maintain consistent naming between BrainSTEM and your actual file system, making it easier to locate files programmatically. Projects and subjects have the same field, so every level of the folder hierarchy can carry its storage name. Several sessions can be assigned to a data storage at once with the list action **Assign selected sessions to a data storage**.

## Dynamic Data Linking

BrainSTEM's data storage system enables dynamic construction of file paths based on your metadata and organization structure.

### How Dynamic Linking Works
{: .no_toc}

When you associate a data storage with a session, BrainSTEM can automatically construct file paths based on:

1. **Data storage base path**: The root location defined in your data storage protocols
2. **Organization structure**: How you've defined data should be organized
3. **Session metadata**: Project names, subject names, session names, dates

### Example Dynamic Path Construction
{: .no_toc}

**Data Storage Configuration:**

| Field | Value |
|-------|-------|
| **Name** | Lab Server Main |
| **Base path** | `/Volumes/StorageName/Data/` |
| **Organization** | Projects → Subjects → Sessions |

**Dynamic Path:**
```
/Volumes/StorageName/Data/{projects}/{subjects}/{sessions}/
```

{: .note }
> Data files should be stored in the session folder based on this organization structure.

**Session Information:**

| Field | Value |
|-------|-------|
| **Project** | Memory_Study_2024 |
| **Subject** | Mouse_001 |
| **Session** | Baseline_Recording |
| **Name used in storage** | ses01_baseline |

**Resulting Path:**
```
/Volumes/StorageName/Data/Memory_Study_2024/Mouse_001/ses01_baseline/
```

### API Access to Dynamic Paths
{: .no_toc}

Use the Python or MATLAB API to programmatically access your data paths:

```python
from brainstem_api_tools import BrainstemClient

client = BrainstemClient()

# Load one session by its id. Its datastorage field lists the ids of its data storages.
session = client.load('session', id='your-session-id').json()['session']

# Load each data storage by its id to read its access protocols
for storage_id in session['datastorage']:
    storage = client.load('datastorage', id=storage_id).json()['datastorage']
    for protocol in storage['data_protocols'] or []:
        print(f"Protocol: {protocol['protocol']}")
        print(f"Base path: {protocol['path']}")
        print(f"Public access: {protocol.get('is_public', False)}")
```

A session lists its data storages and projects by id. The Python and MATLAB clients send `include` only with list requests, so load a single linked record by its id, as here.

### Constructing Full Paths in Your Analysis Code
{: .no_toc}

```python
def storage_name(record):
    """The folder name of a record: its name used in storage, else its name."""
    return record.get('name_used_in_storage') or record['name']


def construct_data_path(session, storage, project, subject_name=None):
    """
    Construct the full path to a session's data from BrainSTEM metadata.

    session, storage and project are the records themselves (loaded by id).
    Pass subject_name when the storage's organization includes Subjects.
    """
    # Use the first configured protocol by default.
    # Update this selection if your storage relies on a specific protocol.
    base_path = storage['data_protocols'][0]['path']

    # data_organization is a list of folder levels, e.g. ['Projects', 'Subjects', 'Sessions']
    path_components = [base_path]
    for element in storage['data_organization'] or []:
        if element == 'Projects':
            path_components.append(storage_name(project))
        elif element == 'Subjects' and subject_name:
            path_components.append(subject_name)
        elif element == 'Sessions':
            path_components.append(storage_name(session))

    return '/'.join(path_components)


def load_path_records(client, session_id):
    """The session, its first data storage, its first project and its first subject's folder name."""
    session = client.load('session', id=session_id).json()['session']
    if not session['datastorage']:
        return session, None, None, None
    storage = client.load('datastorage', id=session['datastorage'][0]).json()['datastorage']
    project = client.load('project', id=session['projects'][0]).json()['project']
    subject_name = None
    if session.get('subjects'):
        subject = client.load('subject', id=session['subjects'][0]).json()['subject']
        subject_name = storage_name(subject)
    return session, storage, project, subject_name


session, storage, project, subject_name = load_path_records(client, 'your-session-id')
if storage:
    full_path = construct_data_path(session, storage, project, subject_name=subject_name)
    print(f"Data location: {full_path}")
```

## Best Practices

### Naming Conventions
{: .no_toc}

- **Data Storage Names**: Use descriptive names that indicate location and purpose
- **Storage Names**: Keep file/folder names consistent with your lab's conventions
- **Avoid Special Characters**: Use underscores or hyphens instead of spaces

### Organization Strategies
{: .no_toc}

- **Standardize Early**: Establish organization patterns before accumulating lots of data
- **Document Conventions**: Create lab protocols for file naming and organization
- **Plan for Growth**: Design structures that scale with increasing data volumes

### Security and Access
{: .no_toc}

- **Authenticated groups**: Required - only users in these groups can access the data storage
- **Public/Private Settings**: Set the public flag per data protocol; a public project's data storage stays private until one of its protocols is public (see [Sharing Project Publicly]({{site.baseurl}}/tutorials/sharing-project-publicly))
- **Group Matching**: Data storage can only be added to sessions in projects that share at least one authenticated group

## Troubleshooting Common Issues

### Cannot Access Data Storage in Sessions
{: .no_toc}

**Problem**: Data storage doesn't appear in the session dropdown

**Solutions**:
- Verify you're a member of at least one authenticated group for the data storage

### Path Construction Errors
{: .no_toc}

**Problem**: Generated paths don't match actual file locations

**Solutions**:
- Review your data organization structure configuration
- Verify the base paths in your protocols are correct
- Check that "Name used in storage" matches your actual file/folder names

### API Access Issues
{: .no_toc}

**Problem**: Cannot access data storage information via API

**Solutions**:
- Load the data storage by its id: the session's `datastorage` field holds ids, and the clients send `include` only with list requests
- Verify your API authentication is working
- Check that you have proper permissions to access the data storage
- Confirm you're using the correct session ID

## Integration with Analysis Workflows

### Loading Data in Python
{: .no_toc}

```python
import os
from brainstem_api_tools import BrainstemClient

def load_session_data(session_id):
    """
    Load session metadata and construct its data path, using
    load_path_records and construct_data_path from the example above.
    """
    client = BrainstemClient()
    session, storage, project, subject_name = load_path_records(client, session_id)

    data_path = None
    if storage:
        data_path = construct_data_path(session, storage, project, subject_name=subject_name)

    # Load actual data files
    data_files = []
    if data_path and os.path.exists(data_path):
        data_files = [f for f in os.listdir(data_path)
                      if f.endswith(('.dat', '.bin', '.h5'))]

    return {
        'session_metadata': session,
        'data_path': data_path,
        'data_files': data_files
    }
```

### MATLAB Integration
{: .no_toc}

```matlab
function data_info = load_session_data(session_id)
    % Load session metadata and construct data paths. The session lists its
    % data storages and projects by id; load each record by its id.
    client = BrainstemClient();

    % One record by id is returned under the singular key: out.session
    out = client.load('session', 'id', session_id);
    session_data = out.session;

    % jsondecode returns a struct array or a cell array for lists; take the first item
    out = client.load('datastorage', 'id', first_item(session_data.datastorage));
    storage = out.datastorage;
    out = client.load('project', 'id', first_item(session_data.projects));
    project = out.project;
    protocol = first_item(storage.data_protocols);
    base_path = protocol.path;

    % Sessions name their subjects directly; take the first one when the
    % organization includes Subjects.
    subject_name = '';
    if ~isempty(session_data.subjects)
        sub = client.load('subject', 'id', first_item(session_data.subjects));   % returns sub.subject
        subject_name = storage_label(sub.subject);
    end

    % Follow the storage's data_organization, e.g. {'Projects','Subjects','Sessions'}
    full_path = base_path;
    organization = cellstr(storage.data_organization);
    for k = 1:numel(organization)
        switch organization{k}
            case 'Projects'
                full_path = fullfile(full_path, storage_label(project));
            case 'Subjects'
                if ~isempty(subject_name), full_path = fullfile(full_path, subject_name); end
            case 'Sessions'
                full_path = fullfile(full_path, storage_label(session_data));
        end
    end

    data_info.session_metadata = session_data;
    data_info.data_path = full_path;
    data_info.exists = exist(full_path, 'dir') == 7;
end

function item = first_item(list)
    if iscell(list), item = list{1}; else, item = list(1); end
end

function name = storage_label(record)
    % Prefer the name used in storage, fall back to the record name
    name = record.name;
    if isfield(record, 'name_used_in_storage') && ~isempty(record.name_used_in_storage)
        name = record.name_used_in_storage;
    end
end
```

Both samples read the storage's **Data organization** list, so a storage organized as Subjects → Sessions produces a shorter path without changes to the code.

## Next Steps

With data storage configured, you can now effectively manage and analyze your research data:

- **Start experimental workflows**: Follow complete experimental documentation with the [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow) or [Two-Photon Imaging Workflow]({{site.baseurl}}/tutorials/two-photon-imaging-workflow) tutorial, which link sessions to a data storage
- **Use API tools**: Access your data programmatically with [Python API tool]({{site.baseurl}}/tools/python-api-tool) or [MATLAB API tool]({{site.baseurl}}/tools/matlab-api-tool) for seamless integration with analysis workflows
- **Organize experiments**: Create structured [Behavioral Assays]({{site.baseurl}}/tutorials/behavioral-assays) that integrate with your data storage system for organized behavioral data
- **Enable collaboration**: Set up proper [Managing Projects]({{site.baseurl}}/tutorials/managing-projects) to share your organized data storage with lab members and collaborators
- **Enable open data**: Make your data publicly accessible through [Sharing Project Publicly]({{site.baseurl}}/tutorials/sharing-project-publicly) to promote open science and collaboration
