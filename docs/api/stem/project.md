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
| `sessions` | list of related sessions IDs formatted as strings **[read-only]** |
| `subjects` | list of related subjects IDs formatted as strings **[read-only]** |
| `publications` | list of related publications IDs formatted as strings **[read-only]** |
| `extra_fields` | list of JSON dictionaries. *See structure below* |
| `is_public` | boolean |
| `name_used_in_storage` | string [max length: 200]|
| `tags` | list of strings |
| `users` | JSON dictionary. *See structure below* |
| `groups` | JSON dictionary. *See structure below* |


`extra_fields` is a list of JSON dictionaries with two elements, `name` and `value` like the example below. The name must start with a letter and can only consist of letters, numbers and underscore. The value can be a string or a numeric value. 

```
{
    "extra_property": "setting1", 
    "another_property: 22
}
```

Each entry of in the `users` dictionary must follow the following structure:

```
"<user_email>": {
                "can_change": <boolean>,
                "is_manager": <boolean>,
                "is_owner": <boolean>
            }
```
Each entry of in the `groups` dictionary must follow the following structure:

```
"<group_name>": {
                "can_change": <boolean>,
                "is_manager": <boolean>,
                "is_owner": <boolean>
            }
```  


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/project
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('project')
```

### Response example
{: .no_toc}

```
{"projects": [
    {
        "id": "c4b8a90b-2963-4d13-aa07-b6f497252dde",
        "name": "project2",
        "description": "",
        "sessions": [
            "1a827c68-19b4-4cec-8ae5-e13c8f1de900",
            "d8e72f9d-eb25-4280-a241-3317d5914055",
            "3865d613-a9a4-419b-80de-ae07cc754a2a"
        ],
        "subjects": [
            "0cdaf69d-63cf-429f-b549-fc0cc163d046"
        ],
        "publications": [],
        "extra_fields": [],
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
        "links": {
            "sessions": "sessions/",
            "subjects": "subjects/"
        }
    },
    {
        "id": "e7475834-7733-48cf-9e3b-f4f2d2d0305a",
        "name": "Test project1",
        "description": "<p>My first project1</p>",
        "sessions": [
            "eba7ed4b-44a9-4626-ae6f-09bccfa553fb",
            "1f7f103b-e949-405a-9b01-ddda3b2f10cf",
            "ef9ef292-4757-44c1-b8f7-9dc8cb36e8f1",
            "ef7ae22f-143a-4a5e-adf6-1c623531dd63"
        ],
        "subjects": [
            "0f87c229-6769-4854-83a5-c71e154246b8"
        ],
        "publications": [],
        "extra_fields": [],
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
        "links": {
            "sessions": "sessions/",
            "subjects": "subjects/"
        }
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/stem/project
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Additional notes:** when a user creates a project they become its owner and only member. Any other user or group will not be added at this point. Perform a change request to add more users or groups.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("project",  data={"name": "NewRestProject", "description": "some text"})
```

### Response example
{: .no_toc}

```
{'project': {'id': 'd7de95c0-eb63-40e8-ac90-7573b58f6033',
    'name': 'NewRestProject',
    'description': 'some text',
    'sessions': [],
    'subjects': [],
    'publications': [],
    'extra_fields': [],
    'is_public': False,
    'tags': [],
    'users': {
        'user@mail.com': {
            'can_change': True,
            'is_manager': True,
            'is_owner': True
        }
    },
    'groups': {}}
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/project/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('project', id='d7de95c0-eb63-40e8-ac90-7573b58f6033')
```

### Response example
{: .no_toc}

```
{'project': {'id': 'd7de95c0-eb63-40e8-ac90-7573b58f6033',
    'name': 'NewRestProject',
    'description': 'some text',
    'sessions': ["eba7ed4b-44a9-4626-ae6f-09bccfa553fb"],
    'subjects': [],
    'publications': [],
    'extra_fields': {
        "extra_property": "setting1", 
        "another_property: 22
    },
    'is_public': False,
    'tags': ["tag1", "tag2"],
    ''users': {
        'user@mail.com': {
            'can_change': True,
            'is_manager': True,
            'is_owner': True
        }
    },
    'groups': {}}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/stem/project/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("project", id="d7de95c0-eb63-40e8-ac90-7573b58f6033", data={"description": "new text"})
```

To add new users and/or groups to the project, or modify the permissions of the existing ones, provide their corresponding dictionaries. Missing permissions will default to *False*.
```
resp = client.save_model("project",
    id="d7de95c0-eb63-40e8-ac90-7573b58f6033",
    data={"description": "new text", 
    "users": {'user2@mail.com': {"can_change": True, "is_manager": True}}, 
    "groups": {"Group1": {"is_manager": True}}})
```

To remove users and/or groups, provide the key-value pair `"remove": True` in the corresponding dictionary.
```
resp = client.save_model("project",
    id="d7de95c0-eb63-40e8-ac90-7573b58f6033",
    data={"description": "new text", 
    "users": {'user2@mail.com': {"remove": True}}, 
    "groups": {"Group1": {"remove": True}}})
```

### Response example
{: .no_toc}

```
{'project': {'id': 'd7de95c0-eb63-40e8-ac90-7573b58f6033',
  'name': 'NewRestProject',
  'description': 'new text',
  'sessions': [],
  'subjects': [],
  'publications': [],
  'extra_fields': [],
  'is_public': False,
  'tags': [],
  'users': {'user1@mail.com': {'can_change': True,
    'is_manager': True,
    'is_owner': True},
   'user2@mail.com': {'can_change': True,
    'is_manager': True,
    'is_owner': False}},
  'groups': {'Group1': {'can_change': True,
    'is_manager': True,
    'is_owner': False}}}}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/stem/project/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("project", id="d7de95c0-eb63-40e8-ac90-7573b58f6033")
```
