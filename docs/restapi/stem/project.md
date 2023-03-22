---
layout: default
title: Project
parent: API endpoints
grand_parent: REST API
nav_order: 2
---

## Contents
- [Fields](/brainstem_support/restapi/stem/project/#fields)
- Endpoints
  - [List view](/brainstem_support/restapi/stem/project/#list-view)
  - [Add](/brainstem_support/restapi/stem/project/#add)
  - [Detail](/brainstem_support/restapi/stem/project/#detail)
  - [Change](/brainstem_support/restapi/stem/project/#change)
  - [Delete](/brainstem_support/restapi/stem/project/#delete)


## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | string with UUID identificator |
| `name` | string **[required]** |
| `description` | string |
| `datasets` | list of strings representing the related datasets IDs **[read-only]** |
| `subjects` | list of strings representing the related subjects IDs **[read-only]** |
| `publications` | list of strings representing the related publications IDs **[read-only]** |
| `extra_content_json` | JSON dictionary |
| `is_public` | boolean |
| `tags` | list of strings |
| `users` | JSON dictionary |
| `groups` | JSON dictionary |

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


## Endpoints
- List view
- Add
- Detail
- Change
- Delete

## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/stem/project
- **Data:** None

### Use example (using Python API):
```
resp = load_model(settings, 'project')
```

### Response example:
```
{"projects": [
    {
        "id": "c4b8a90b-2963-4d13-aa07-b6f497252dde",
        "name": "project2",
        "description": "",
        "datasets": [
            "1a827c68-19b4-4cec-8ae5-e13c8f1de900",
            "d8e72f9d-eb25-4280-a241-3317d5914055",
            "3865d613-a9a4-419b-80de-ae07cc754a2a"
        ],
        "subjects": [
            "0cdaf69d-63cf-429f-b549-fc0cc163d046"
        ],
        "publications": [],
        "extra_content_json": [],
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
            "datasets": "datasets/",
            "subjects": "subjects/"
        }
    },
    {
        "id": "e7475834-7733-48cf-9e3b-f4f2d2d0305a",
        "name": "Test project1",
        "description": "<p>My first project1</p>",
        "datasets": [
            "eba7ed4b-44a9-4626-ae6f-09bccfa553fb",
            "1f7f103b-e949-405a-9b01-ddda3b2f10cf",
            "ef9ef292-4757-44c1-b8f7-9dc8cb36e8f1",
            "ef7ae22f-143a-4a5e-adf6-1c623531dd63"
        ],
        "subjects": [
            "0f87c229-6769-4854-83a5-c71e154246b8"
        ],
        "publications": [],
        "extra_content_json": [],
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
            "datasets": "datasets/",
            "subjects": "subjects/"
        }
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** http://brainstem.org/rest/private/stem/project
- **Data:** JSON dictionary containing at least the required fields.

**Additional notes:** when a user creates a project they become its owner and only member. Any other user or group will not be added at this point. Perform a change request to add more users or groups.

### Use example (using Python API):
```
resp = save_model(settings, "project",  data={"name": "NewRestProject", "description": "some text"})
```

### Response example:
```
{'project': {'id': 'a5f29099-2758-4163-a8e4-e5e2898e57b2',
    'name': 'NewRestProject',
    'description': 'some text',
    'datasets': [],
    'subjects': [],
    'publications': [],
    'extra_content_json': [],
    'is_public': False,
    'tags': [],
    'users': {'user@mail.com': {'can_change': True,
    'is_manager': True,
    'is_owner': True}},
    'groups': {}}
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/stem/project/<id\>/
- **Data:** None

### Use example (using Python API):
```
resp = load_model(settings, 'project', filters={'id': 'a5f29099-2758-4163-a8e4-e5e2898e57b2'})
```

### Response example:
```
{'project': {'id': 'a5f29099-2758-4163-a8e4-e5e2898e57b2',
    'name': 'NewRestProject',
    'description': 'some text',
    'datasets': [],
    'subjects': [],
    'publications': [],
    'extra_content_json': [],
    'is_public': False,
    'tags': [],
    'users': {'user@mail.com': {'can_change': True,
    'is_manager': True,
    'is_owner': True}},
    'groups': {}}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/stem/project/<id\>/
- **Data:** JSON dictionary containing the fields to be updated **and the project's ID**.


### Use example (using Python API):
```
resp = save_model(settings, "project",  
    data={"id": "a5f29099-2758-4163-a8e4-e5e2898e57b2", 
    "description": "new text"})
```

To add new users and/or groups to the project, or modify the permissions of the existing ones, provide their corresponding dictionaries. Missing permissions will default to *False*.
```
resp = save_model(settings, "project",  
    data={"id": "a5f29099-2758-4163-a8e4-e5e2898e57b2", 
    "description": "new text", 
    "users": {'user2@mail.com': {"can_change": True, "is_manager": True}}, 
    "groups": {"Group1": {"is_manager": True}}})
```

To remove users and/or groups, provide the key-value pair `"remove": True` in the corresponding dictionary.
```
resp = save_model(settings, "project",  
    data={"id": "a5f29099-2758-4163-a8e4-e5e2898e57b2", 
    "description": "new text", 
    "users": {'user2@mail.com': {"remove": True}}, 
    "groups": {"Group1": {"remove": True}}})
```

### Response example:
```
{'project': {'id': 'a5f29099-2758-4163-a8e4-e5e2898e57b2',
  'name': 'NewRestProject',
  'description': 'new text',
  'datasets': [],
  'subjects': [],
  'publications': [],
  'extra_content_json': [],
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
- **URL:** http://brainstem.org/rest/private/stem/project/<id\>/
- **Data:** JSON dictionary containing the **project's ID**.


### Use example (using Python API):
```
resp = delete_model(settings, "project", data={"id": "a5f29099-2758-4163-a8e4-e5e2898e57b2"})
```
