---
layout: default
title: Managing Data Storage
parent: Tutorials
nav_order: 7
---

# Managing Data Storage in BrainSTEM
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

Data storage in BrainSTEM provides a flexible way to link your metadata to actual data files stored on various platforms. This tutorial covers how to set up data storage locations, associate them with sessions, and configure dynamic data linking for seamless access to your raw data.

## Understanding Data Storage Concepts

BrainSTEM's data storage system consists of three key components:

1. **Data Storage Locations**: Define where your data is physically stored (servers, cloud, local drives)
2. **Data Organization**: How your files are structured within the storage location
3. **Data Protocols**: How to access the data (paths, URLs, access methods)

## Creating a Data Storage Location

### Step 1: Navigate to Data Storage

1. From your BrainSTEM dashboard, go to *Personal Attributes* → *Data storage* in the left navigation menu
2. Click the *Add data storage* button in the top right corner

### Step 2: Configure Basic Information

**Fill in the basic details:**

| Field | Value/Instructions |
|-------|-------------------|
| **Name** | Give your data storage a descriptive name (e.g., "Lab Server 01", "Cloud Storage Main") |
| **Authenticated groups** | Select the groups that should have access to this data storage (**required**) |
| **Description** | Add details about what type of data is stored here and any access requirements |
| **Public access** | Set whether this data storage should be publicly accessible |

{: .important }
> Permissions are directly set on data storages. Data storage has four permission levels: membership (read access), contributors, managers, and owners.

{: .note }
> Choose names that clearly identify the storage location and its purpose. Other lab members will see these names when creating sessions.

### Step 3: Define Data Organization

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
Subjects → Sessions → Data files
```

```
Projects → Subjects → Sessions → Data files
```

Add organization elements that match your lab's file structure conventions using the available element types.

### Step 4: Configure Data Storage Protocols

Set up access methods for your data storage. Each protocol defines how to access the same data storage location:

**Protocol Configuration Options:**

| Storage Type | Protocol | Path Example | Public Status |
|--------------|----------|--------------|---------------|
| **Network/Server Storage** | Local harddrive | `/mnt/labserver/data/` or local mount path | false (internal lab access) |
| **Cloud Storage** | Dropbox (Cloud solution) | `data/myproject` or cloud folder path | Choose based on data sensitivity |
| **Local Storage** | Local harddrive | `/Users/researcher/data/` or `D:\Lab_Data\` | false |
| **Public Repositories** | Web | `https://dandiarchive.org/dandiset/123456/` or repository URL | true |

{: .important }
> You can configure multiple protocols for the same data storage. This allows flexibility in how different users or systems access the same data.

## Assigning Data Storage to Sessions

### During Session Creation

1. When creating a new session, locate the **Data storage** field
2. Select from your configured data storage locations in the dropdown
3. Optionally, specify a **Name used in storage** - this is the folder/file name used in your actual storage system

### For Existing Sessions

1. Navigate to the session you want to update
2. Click the *Edit* button
3. Select or change the **Data storage** field
4. Update the **Name used in storage** if needed
5. Save your changes

{: .note }
> The "Name used in storage" field helps maintain consistent naming between BrainSTEM and your actual file system, making it easier to locate files programmatically. This is a session-level field, not a data storage field.

## Dynamic Data Linking

BrainSTEM's data storage system enables dynamic construction of file paths based on your metadata and organization structure.

### How Dynamic Linking Works

When you associate a data storage with a session, BrainSTEM can automatically construct file paths based on:

1. **Data storage base path**: The root location defined in your data storage protocols
2. **Organization structure**: How you've defined data should be organized
3. **Session metadata**: Project names, subject names, session names, dates
4. **Custom storage name**: The specific name you've assigned for storage

### Example Dynamic Path Construction

**Data Storage Configuration:**
| Field | Value |
|-------|-------|
| **Name** | Lab Server Main |
| **Base path** | `/mnt/labserver/data/` |
| **Organization** | Projects → Subjects → Sessions → Data files |

{: .note }
> Data files are implied be stored in the session folder.

**Session Information:**
| Field | Value |
|-------|-------|
| **Project** | Memory_Study_2024 |
| **Subject** | Mouse_001 |
| **Session** | Baseline_Recording |
| **Name used in storage** | ses01_baseline |

**Resulting Dynamic Path:**
```
/mnt/labserver/data/Memory_Study_2024/Mouse_001/ses01_baseline/
```

### API Access to Dynamic Paths

Use the Python or MATLAB API to programmatically access your data paths:

```python
from brainstem_api_client import BrainstemClient

client = BrainstemClient()

# Load session with data storage information
session_response = client.load_model('session', 
                                   id='your-session-id', 
                                   include=['datastorage'])

session_data = session_response.json()['sessions'][0]
storage_info = session_data['datastorage']

# Access configured protocols and paths
for protocol in storage_info['data_protocols_json']:
    print(f"Protocol: {protocol['protocol']}")
    print(f"Base path: {protocol['path']}")
    print(f"Public access: {protocol['is_public']}")
```

### Constructing Full Paths in Your Analysis Code

```python
def construct_data_path(session_data):
    """
    Construct full path to session data based on BrainSTEM metadata
    """
    storage = session_data['datastorage']
    base_path = storage['data_protocols_json'][0]['path']  # First protocol
    
    # Extract organization elements
    organization = storage['data_organization_json']
    
    # Build path based on organization structure
    path_components = [base_path]
    
    for element in organization:
        if element['elements'] == 'Projects':
            path_components.append(session_data['projects'][0]['name'])
        elif element['elements'] == 'Subjects':
            path_components.append(session_data['subject']['name'])
        elif element['elements'] == 'Sessions':
            storage_name = session_data.get('name_used_in_storage', 
                                          session_data['name'])
            path_components.append(storage_name)
    
    return '/'.join(path_components)

# Usage
full_path = construct_data_path(session_data)
print(f"Data location: {full_path}")
```

## Best Practices

### Naming Conventions

- **Data Storage Names**: Use descriptive names that indicate location and purpose
- **Storage Names**: Keep file/folder names consistent with your lab's conventions
- **Avoid Special Characters**: Use underscores or hyphens instead of spaces

### Organization Strategies

- **Standardize Early**: Establish organization patterns before accumulating lots of data
- **Document Conventions**: Create lab protocols for file naming and organization
- **Plan for Growth**: Design structures that scale with increasing data volumes

### Security and Access

- **Authenticated Groups**: Data storage requires authenticated groups (required field)
- **Public/Private Settings**: Use the `is_public` field appropriately for your data sensitivity
- **Project Permissions**: Data storage is shared through project groups - you can only add data storage associated with the same groups as the selected projects

### Backup and Redundancy

- **Multiple Protocols**: Configure both local and cloud access for important data
- **Document Locations**: Maintain clear records of where different data types are stored
- **Test Access**: Regularly verify that configured paths are accessible

## Troubleshooting Common Issues

### Cannot Access Data Storage in Sessions

**Problem**: Data storage doesn't appear in session dropdown

**Solutions**:
- Verify your user is a member of one of the authenticated groups for the data storage
- Check that the data storage is properly saved and configured

### Path Construction Errors

**Problem**: Generated paths don't match actual file locations

**Solutions**:
- Review your data organization structure configuration
- Verify the base paths in your protocols are correct
- Check that "Name used in storage" matches your actual file/folder names

### API Access Issues

**Problem**: Cannot access data storage information via API

**Solutions**:
- Ensure you're including 'datastorage' in your API include parameters
- Verify your API authentication is working
- Check that you have proper permissions to access the data storage
- Confirm you're using the correct session ID

## Integration with Analysis Workflows

### Loading Data in Python

```python
import os
from brainstem_api_client import BrainstemClient

def load_session_data(session_id):
    """
    Load session metadata and construct data paths
    """
    client = BrainstemClient()
    
    # Get session with data storage info
    response = client.load_model('session', 
                               id=session_id, 
                               include=['datastorage', 'dataacquisition'])
    
    session = response.json()['sessions'][0]
    
    # Construct data path
    data_path = construct_data_path(session)
    
    # Load actual data files
    data_files = []
    if os.path.exists(data_path):
        data_files = [f for f in os.listdir(data_path) 
                     if f.endswith(('.dat', '.bin', '.h5'))]
    
    return {
        'session_metadata': session,
        'data_path': data_path,
        'data_files': data_files
    }
```

### MATLAB Integration

```matlab
function data_info = load_session_data(session_id)
    % Load session metadata and construct data paths
    
    % Get session with data storage info
    session_data = load_model('model', 'session', ...
                             'id', session_id, ...
                             'include', {'datastorage', 'dataacquisition'});
    
    % Extract data storage information
    storage = session_data.datastorage;
    base_path = storage.data_protocols_json{1}.path;
    
    % Construct full path (simplified example)
    project_name = session_data.projects{1}.name;
    subject_name = session_data.subject.name;
    storage_name = session_data.name_used_in_storage;
    
    full_path = fullfile(base_path, project_name, subject_name, storage_name);
    
    data_info.session_metadata = session_data;
    data_info.data_path = full_path;
    data_info.exists = exist(full_path, 'dir') == 7;
end
```

## Advanced Configuration

### Multiple Protocol Setup

For labs with complex data access needs:

```json
{
  "data_protocols_json": [
    {
      "protocol": "Local harddrive",
      "path": "/mnt/labserver/data",
      "is_public": false
    },
    {
      "protocol": "Dropbox (Cloud solution)",
      "path": "lab_backup",
      "is_public": false
    },
    {
      "protocol": "Web",
      "path": "https://dandiarchive.org/dandiset/123456",
      "is_public": true
    }
  ]
}
```

### Custom Organization Patterns

For specialized data organization:

```json
{
  "data_organization_json": [
    {"elements": "Projects"},
    {"elements": "Subjects"},
    {"elements": "Sessions"}
  ]
}
```

This configuration would create paths like:
```
/base_path/Memory_Study/Mouse_001/Baseline_Recording/
```

By following this tutorial, you'll be able to effectively manage your data storage in BrainSTEM, creating seamless links between your metadata and actual data files for more efficient analysis workflows.

## Next Steps

With data storage configured, you can now effectively manage and analyze your research data:

- **Start experimental workflows**: Follow complete experimental documentation with [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow) or [Two-Photon Imaging Workflow]({{site.baseurl}}/tutorials/two-photon-imaging-workflow) tutorials that demonstrate data storage integration
- **Use API tools**: Access your data programmatically with [Python API tool]({{site.baseurl}}/tutorials/python-api-tool) or [MATLAB API tool]({{site.baseurl}}/tutorials/matlab-api-tool) for seamless integration with analysis workflows
- **Organize experiments**: Create structured [Behavioral Paradigms]({{site.baseurl}}/tutorials/behavioral-paradigms) that integrate with your data storage system for organized behavioral data
- **Enable collaboration**: Set up proper [Managing Projects]({{site.baseurl}}/tutorials/managing-projects) to share your organized data storage with lab members and collaborators
- **Enable open data**: Make your data publicly accessible through [Sharing Project Publicly]({{site.baseurl}}/tutorials/sharing-project-publicly) to promote open science and collaboration
