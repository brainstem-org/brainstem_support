---
layout: default
title: Project
parent: STEM
grand_parent: API
nav_order: 1
---

# Project API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `name` | string **[required]** [max length: 200; must be unique]|
| `description` | string |
| `sessions` | list of related session IDs formatted as strings **[read-only]** |
| `subjects` | list of related subject IDs formatted as strings **[read-only]** |
| `publications` | list of related publication IDs formatted as strings |
| `collections` | list of related collection IDs formatted as strings **[read-only]** |
| `cohorts` | list of related cohort IDs formatted as strings **[read-only]** |
| `extra_fields` | JSON object of additional key/value metadata. *See structure below* |
| `is_public` | boolean |
| `tags` | list of strings |
| `users` | JSON object keyed by user email. *See structure below* |
| `groups` | JSON object keyed by group name. *See structure below* |


`extra_fields` is a JSON object where each key/value pair captures additional metadata. Keys must start with a letter and can only contain letters, numbers, and underscores. Values can be strings or numeric values.

```json
{
    "extra_property": "setting1",
    "another_property": 22
}
```

Each entry in the `users` object follows the structure:

```json
"<user_email>": {
                "can_change": <boolean>,
                "is_manager": <boolean>,
                "is_owner": <boolean>
            }
```

Each entry in the `groups` object follows the structure:

```json
"<group_name>": {
                "can_change": <boolean>,
                "is_manager": <boolean>,
                "is_owner": <boolean>
            }
```  


## List view

- **Allowed portals:** public, private
- **Request method:** GET
- **URL (private portal):** <https://www.brainstem.org/api/private/stem/project/>
- **URL (public portal):** <https://www.brainstem.org/api/public/stem/project/>
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

**Example request (Python API tool)**
{: .no_toc}

```python
resp = client.load_model("project")
```

**Example response**
{: .no_toc}

```json
{
    "projects": [
        {
            "id": "00000000-0000-0000-0000-000000000000",
            "name": "project2",
            "description": "",
            "sessions": [
                "00000000-0000-0000-0000-000000000000",
                "00000000-0000-0000-0000-000000000000",
                "00000000-0000-0000-0000-000000000000"
            ],
            "subjects": [
                "00000000-0000-0000-0000-000000000000"
            ],
            "publications": [],
            "collections": [
                "00000000-0000-0000-0000-000000000000"
            ],
            "cohorts": [],
            "extra_fields": {
                "temperature": "ambient"
            },
            "is_public": true,
            "tags": [],
            "users": {
                "user1@mail.com": {
                    "can_change": true,
                    "is_manager": true,
                    "is_owner": true
                },
                "user2@mail.com": {
                    "can_change": true,
                    "is_manager": false,
                    "is_owner": false
                }
            },
            "groups": {
                "Group1": {
                    "can_change": true,
                    "is_manager": true,
                    "is_owner": false
                }
            },
        },
        {
            "id": "00000000-0000-0000-0000-000000000000",
            "name": "Test project1",
            "description": "<p>My first project1</p>",
            "sessions": [
                "00000000-0000-0000-0000-000000000000",
                "00000000-0000-0000-0000-000000000000",
                "00000000-0000-0000-0000-000000000000",
                "00000000-0000-0000-0000-000000000000"
            ],
            "subjects": [
                "00000000-0000-0000-0000-000000000000"
            ],
            "publications": [],
            "collections": [],
            "cohorts": [],
            "extra_fields": {},
            "is_public": true,
            "tags": [
                "cooling",
                "medial septum",
                "extracellular"
            ],
            "users": {
                "user3@mail.com": {
                    "can_change": true,
                    "is_manager": true,
                    "is_owner": true
                },
                "user1@mail.com": {
                    "can_change": true,
                    "is_manager": true,
                    "is_owner": true
                }
            },
            "groups": {},
        }
    ]
}
```


## Add

- **Allowed portals:** private
- **Request method:** POST
- **URL:** <https://www.brainstem.org/api/private/stem/project/>
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Additional notes:** when a user creates a project they become its owner and only member. Any other user or group will not be added at this point. Perform a change request to add more users or groups.

**Example request (Python API tool)**
{: .no_toc}

```python
resp = client.save_model("project",  data={"name": "NewRestProject", "description": "some text"})
```

**Example response**
{: .no_toc}

```json
{
    "project": {
        "id": "00000000-0000-0000-0000-000000000000",
        "name": "NewRestProject",
        "description": "some text",
        "sessions": [],
        "subjects": [],
        "publications": [],
        "collections": [],
        "cohorts": [],
        "extra_fields": {},
        "is_public": false,
        "tags": [],
        "users": {
            "user@mail.com": {
                "can_change": true,
                "is_manager": true,
                "is_owner": true
            }
        },
        "groups": {}
    }
}
```



## Detail

- **Allowed portals:** public, private
- **Request method:** GET
- **URL (private portal):** `https://www.brainstem.org/api/private/stem/project/<id>/`
- **URL (public portal):** `https://www.brainstem.org/api/public/stem/project/<id>/`
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

**Example request (Python API tool)**
{: .no_toc}

```python
resp = client.load_model("project", id="00000000-0000-0000-0000-000000000000")
```

**Example response**
{: .no_toc}

```json
{
    "project": {
        "id": "00000000-0000-0000-0000-000000000000",
        "name": "NewRestProject",
        "description": "some text",
        "sessions": [
            "00000000-0000-0000-0000-000000000000"
        ],
        "subjects": [],
        "publications": [],
        "collections": [],
        "cohorts": [],
        "extra_fields": {
            "extra_property": "setting1",
            "another_property": 22
        },
        "is_public": false,
        "tags": [
            "tag1",
            "tag2"
        ],
        "users": {
            "user@mail.com": {
                "can_change": true,
                "is_manager": true,
                "is_owner": true
            }
        },
        "groups": {}
    }
}
```


## Change

- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** `https://www.brainstem.org/api/private/stem/project/<id>/`
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


**Example request (Python API tool)**
{: .no_toc}

```python
resp = client.save_model("project", id="00000000-0000-0000-0000-000000000000", data={"description": "new text"})
```

To add new users and/or groups to the project, or modify the permissions of the existing ones, provide their corresponding dictionaries. Missing permissions will default to *False*.

```python
resp = client.save_model(
    "project",
    id="00000000-0000-0000-0000-000000000000",
    data={
        "description": "new text",
        "users": {"user2@mail.com": {"can_change": True, "is_manager": True}},
        "groups": {"Group1": {"is_manager": True}}
    }
)
```

To remove users and/or groups, provide the key-value pair `"remove": True` in the corresponding dictionary.

```python
resp = client.save_model(
    "project",
    id="00000000-0000-0000-0000-000000000000",
    data={
        "description": "new text",
        "users": {"user2@mail.com": {"remove": True}},
        "groups": {"Group1": {"remove": True}}
    }
)
```

**Example response**
{: .no_toc}

```json
{
    "project": {
        "id": "00000000-0000-0000-0000-000000000000",
        "name": "NewRestProject",
        "description": "new text",
        "sessions": [],
        "subjects": [],
        "publications": [],
        "collections": [],
        "cohorts": [],
        "extra_fields": {},
        "is_public": false,
        "tags": [],
        "users": {
            "user1@mail.com": {
                "can_change": true,
                "is_manager": true,
                "is_owner": true
            },
            "user2@mail.com": {
                "can_change": true,
                "is_manager": true,
                "is_owner": false
            }
        },
        "groups": {
            "Group1": {
                "can_change": true,
                "is_manager": true,
                "is_owner": false
            }
        }
    }
}
```


## Delete

- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** `https://www.brainstem.org/api/private/stem/project/<id>/`
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


**Example request (Python API tool)**
{: .no_toc}

```python
resp = client.delete_model("project", id="00000000-0000-0000-0000-000000000000")
```
