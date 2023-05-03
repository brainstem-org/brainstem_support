---
layout: default
title: Group Membership Invitation
parent: Users
grand_parent: REST API
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
| `id` | string with UUID identificator |
| `user_account_invitation` | string with the invited user ID |
| `authgroup` | string with the related group ID |
| `new_manager` | boolean |
| `new_owner` | boolean |


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/groupmembershipinvitation
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'groupmembershipinvitation')
```

### Response example
{: .no_toc}

```
{'group_membership_invitations': [
    {
        'id': 'bdbc1823-7bcf-402d-bcaf-c16ce8da4632',
        'user_account_invitation': 11,
        'authgroup': 12,
        'new_manager': False,
        'new_owner': False
    },
    {
        'id': '4820aea8-151c-422e-9427-d7985a949518',
        'user_account_invitation': 7,
        'authgroup': 48,
        'new_manager': False,
        'new_owner': False
    }
]}
```


## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/groupmembershipinvitation/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'groupmembershipinvitation', id='bdbc1823-7bcf-402d-bcaf-c16ce8da4632')
```

### Response example
{: .no_toc}

```
{'group_membership_invitation': {
    'id': 'bdbc1823-7bcf-402d-bcaf-c16ce8da4632',
    'user_account_invitation': 11,
    'authgroup': 12,
    'new_manager': False,
    'new_owner': False}
}
```


## Accept
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/groupmembershipinvitation/<id\>/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, "groupmembershipinvitation", id="caf8093f-def3-43a4-9c46-543e3f7d63b0", options="accept")
```



## Reject
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/groupmembershipinvitation/<id\>/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, "groupmembershipinvitation", id="fa2d3f83-f5e8-4c3f-9006-fc2d92d0c0a0", options="reject")
```


## Cancel
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/groupmembershipinvitation/<id\>/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, "groupmembershipinvitation", id="77c92a03-79ce-4cd6-9379-fd3d4f459012", options="cancel")
```