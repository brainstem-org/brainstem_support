---
layout: default
title: Group Membership Invitation
parent: Users
grand_parent: API
nav_order: 3
---

# Group Membership Invitation API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}


## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `user_account_invitation` | invited user ID formatted as an integer |
| `authgroup` | related group ID formatted as an integer |
| `new_manager` | boolean |
| `new_owner` | boolean |


## List view
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/groupmembershipinvitation
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('groupmembershipinvitation')
```

### Response example
{: .no_toc}

```
{'group_membership_invitations': [
    {
        'id': '<id>',
        'user_account_invitation': 11,
        'authgroup': 12,
        'new_manager': False,
        'new_owner': False
    },
    {
        'id': '<id>',
        'user_account_invitation': 7,
        'authgroup': 48,
        'new_manager': False,
        'new_owner': False
    }
]}
```

List responses include a `meta` object (pagination/filter metadata).


## Detail
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/groupmembershipinvitation/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('groupmembershipinvitation', id='<id>')
```

### Response example
{: .no_toc}

```
{'group_membership_invitation': {
    'id': '<id>',
    'user_account_invitation': 11,
    'authgroup': 12,
    'new_manager': False,
    'new_owner': False}
}
```


## Accept
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/groupmembershipinvitation/<id\>/accept/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load("groupmembershipinvitation", id="<id>", options="accept")
```



## Reject
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/groupmembershipinvitation/<id\>/reject/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load("groupmembershipinvitation", id="<id>", options="reject")
```


## Cancel
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/groupmembershipinvitation/<id\>/cancel/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load("groupmembershipinvitation", id="<id>", options="cancel")
```
