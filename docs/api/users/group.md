---
layout: default
title: Group
parent: Users
grand_parent: API
nav_order: 2
---

# Group API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `name` | string **[required]** |
| `users` | dictionary with one entry per member of the group. *See structure below.* |

Each entry in the `users` dictionary has the user `email` as key and the following dictionary as value:
```
{'is_manager': <boolean>, 'is_owner': <boolean>}
```

## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/group
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('group')
```

### Response example
{: .no_toc}

```
{'groups': [
    {
        'id': 1,
        'name': 'Buzsaki lab',
        'users': {
            'user1@mail.com': {'is_manager': True, 'is_owner': True}
            'petersen.peter@gmail.com': {'is_manager': True, 'is_owner': False},
            'user2@mail.com': {'is_manager': False, 'is_owner': False}
        }
    },
    {
        'id': 41,
        'name': 'Peters lab',
        'users': {
            'petersen.peter@gmail.com': {'is_manager': True, 'is_owner': True},
            'user3@mail.com': {'is_manager': False, 'is_owner': False}
        }
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/users/group
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Additional notes:** when a user creates a group they become its owner and only member. Any other user will not be added at this point. Perform a change request to add more users.


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("group",  data={
    "name": "NewGroup", 
})
```

### Response example
{: .no_toc}

```
{'group': {
        'id': 48,
        'name': 'NewGroup',
        'users': {
            'user3@mail.com': {'is_manager': True, 'is_owner': True}
        }
    }
}
```


## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/group/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('group', id='48')
```

### Response example
{: .no_toc}

```
{'group': {
        'id': 48,
        'name': 'NewGroup',
        'users': {
            'user3@mail.com': {'is_manager': True, 'is_owner': True}
        }
    }
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/users/group/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("group", id="48", data={"name": "NewGroupName"})
```

To add new users to the group, or modify the permissions of the existing ones, provide their corresponding dictionaries. Missing permissions will default to *False*.

```
resp = client.save_model("group", id="48", data={
    "users": {'user4@mail.com': {'is_manager': False, 'is_owner': False}}
    }
)
```

To remove users, provide the key-value pair `"remove": True` in the corresponding dictionary.

```
resp = client.save_model("group", id="48", data={
    "users": {'user4@mail.com': {'remove': True}}
    }
)
```

### Response example
{: .no_toc}


**Note:** `'user4@mail.com'` has been invited to join the group.
```
{'group': {
        'id': 48,
        'name': 'NewGroup',
        'users': {
            'user3@mail.com': {'is_manager': True, 'is_owner': True}
        }
    }
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/users/group/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("group", id="3654964e-1bf7-40c7-a376-9dcec4c125cd")
``` 



## Join
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/group/<id\>/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model("group", id="9", options="join")
```

**Note:** a request to join the group is created.



## Leave
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/group/<id\>/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model("group", id="9", options="leave")
```