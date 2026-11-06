---
layout: default
title: Managing Data Storage
parent: Tutorials
nav_order: 5
---

# Managing Data Storage
{: .no_toc}

This tutorial creates the data storage **Lab Server**, which describes where your recordings live and how their folders are nested, links it to a session, and builds the path to that session's files in your analysis code. At the end, every session can point at its folder on your server, cloud storage or public repository.

**Prerequisites**: a lab group (see [Manage Groups]({{site.baseurl}}/tutorials/managing-groups)) and a project with at least one session (see [Get started!]({{site.baseurl}}/tutorials/get_started)).

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## What a data storage describes

A data storage does not hold files. It records three things:

1. **Where** the data is: the storage's name, location and description.
2. **How the folders are nested**: its **Data organization**, for example Projects → Subjects → Sessions.
3. **How to reach it**: its **Data protocols**, one per access route (a network share, a cloud folder, a public repository), each with its own path.

A session names its data storage, and the project, subject and session each carry the folder name used in storage. Together these give the path to a session's files.

## Step 1: Create the data storage

![A data storage's form: name, location, description, the data organization rows and the data protocols with their public access value.]({{site.baseurl}}/assets/images/screenshots/data-storage-form.png)
{: .screenshot }
*A data storage's form: name, location, description, the data organization rows and the data protocols with their public access value.*

1. Go to **Personal attributes** → **Data storage** and click **Add data storage**.
2. Enter the **Data storage name (must be unique)** "Lab Server". The name is unique across BrainSTEM; if it is taken, add your lab's name, for example "Sample Lab Server".
3. In **Authenticated groups**, select your lab group. The groups you select get Contributor access, which lets their members select the storage on a session.
4. Click **Save**. The data storage's edit page opens.

## Step 2: Describe the folders and the access routes

1. Fill in the **Location**, for example "Network storage, Room 301", and a **Description** of what is stored there.
2. Under **Data organization**, add one row per folder level, from the top level down: "Projects", "Subjects", "Sessions". The elements are Projects, Cohorts, Collections, Subjects, Sessions, Users and Years.
3. Under **Data protocols**, add one row per access route, with its **Protocol Type**, its **Access Path/URL** and whether it has **Public Access**. For example:

   | Protocol Type | Access Path/URL | Public Access |
   |---------------|-----------------|---------------|
   | SMB/CIFS | `smb://uni.domain/group/data` | No |
   | Local Storage | `/Volumes/LabServer/Data` | No |
   | HTTPS/Web | `https://dandiarchive.org/dandiset/123456` | Yes |

4. Click **Save**.

A data storage has no visibility switch of its own. Each data protocol has its own **Public Access** value.

{: .warning }
> Setting **Public Access** on one data protocol makes the whole data storage public when you save it: its name, location, description and the public protocols' paths appear on the public portal. The files themselves are not made reachable.

All fields are described on the [Data storage]({{site.baseurl}}/datamodel/personal_attributes/datastorage/) page.

## Step 3: Assign the data storage to sessions

A session's **Data storage** list offers only the data storages on which you are at least Contributor.

1. Open the session and click **Edit**.
2. In **Data storage**, select "Lab Server". A session can have several data storages; their order is kept.
3. If the session's folder has another name than the session, enter it in **Session name in data storage**, for example "ses01_baseline".
4. Click **Save**.

Projects and subjects have the same kind of field: **Project name in storage** (under **Online repositories** on the project's form) and **Subject name used in data storage**. To assign many sessions at once, select them in the **Sessions** list and run **Assign selected sessions to a data storage**.

## Step 4: Build a session's path in your analysis code

BrainSTEM stores the parts of the path; your code joins them. Take the **Access Path/URL** of a data protocol and add one folder per **Data organization** element, using each entry's name in storage, or its name when that is empty:

| Part | Value |
|------|-------|
| **Access Path/URL** (Local Storage) | `/Volumes/LabServer/Data` |
| Projects | Memory_Study_2024 |
| Subjects | Mouse_001 |
| Sessions (its **Session name in data storage**) | ses01_baseline |
| **Path** | `/Volumes/LabServer/Data/Memory_Study_2024/Mouse_001/ses01_baseline` |

The function below does this with the [Python API tool]({{site.baseurl}}/tools/python-api-tool/), which explains installation and sign-in. It handles Projects, Subjects and Sessions, and stops with an error on any other element, so a storage organized by Years or Cohorts tells you what to add instead of returning a wrong path.

```python
from brainstem_api_tools import BrainstemClient

client = BrainstemClient()


def load(kind, entry_id):
    return client.load(kind, id=entry_id).json()[kind]


def folder(entry):
    """An entry's folder: its name used in storage, else its name."""
    return entry.get("name_used_in_storage") or entry["name"]


def session_path(session_id, protocol="Local Storage"):
    session = load("session", session_id)
    storage = load("datastorage", session["datastorage"][0])
    paths = {p["protocol"]: p["path"] for p in storage["data_protocols"] or []}
    parts = [paths[protocol].rstrip("/")]
    for element in storage["data_organization"] or []:
        if element == "Projects":
            parts.append(folder(load("project", session["projects"][0])))
        elif element == "Subjects":
            parts.append(folder(load("subject", session["subjects"][0])))
        elif element == "Sessions":
            parts.append(folder(session))
        else:
            raise ValueError(f"No rule for the data organization element {element!r}")
    return "/".join(parts)


print(session_path("<session-id>"))
```

{: .note }
> The **Project name in storage** is not available through the API, so the function uses the project's name for the Projects folder. If your project folder has another name, put it in the function. The [MATLAB API tool]({{site.baseurl}}/tools/matlab-api-tool/) loads entries the same way, with `client.load('session', 'id', session_id)`.

## End state

The data storage "Lab Server" describes your folder structure and access routes, your session points at it, and your analysis code can turn a session into the folder that holds its files.

## Troubleshooting

**Data storage missing in a session's list**: you need at least Contributor on the data storage. Ask its owner or a manager to give you or your group a role from the storage's **Manage** page (see [Permissions]({{site.baseurl}}/datamodel/permissions/#personal-attribute-permissions)).

**Session not added by the list action**: a group with a role on one of the session's projects must be at least Contributor on the data storage, and you must be Contributor on one of the session's projects.

**Path does not match the files**: check the order of the **Data organization** rows, the **Access Path/URL** of the protocol you use, and the names in storage of the project, subject and session.

## Next steps

- **Next:** [Manage Projects]({{site.baseurl}}/tutorials/managing-projects): give your collaborators a role on the project.
- [Electrophysiology Workflow]({{site.baseurl}}/tutorials/electrophysiology-workflow): links each session to "Lab Server".
- [Share data publicly]({{site.baseurl}}/tutorials/sharing-project-publicly): mark the protocol that points at a public repository as public.
- Data model: [Data storage]({{site.baseurl}}/datamodel/personal_attributes/datastorage/) and [Sessions]({{site.baseurl}}/datamodel/stem/session/).
