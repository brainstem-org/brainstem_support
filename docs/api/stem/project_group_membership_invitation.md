---
layout: default
title: Project Group Membership Invitation
parent: STEM
grand_parent: API
nav_order: 5
---

# Project Group Membership Invitation API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}


## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `invitee` | invited group ID |
| `project` | related project ID formatted as a string |
| `can_change` | boolean |
| `manage_project` | boolean |
| `own_project` | boolean |



## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/projectgroupmembershipinvitation
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('projectgroupmembershipinvitation')
```

### Response example
{: .no_toc}

```
{'project_group_membership_invitations': [
    {
        'id': 'b6529885-e670-4052-98c5-ea10d447e134',
        'invitee': 8,
        'project': 'a31e6de1-bd46-4f48-9afe-620ae6435a09',
        'can_change': False,
        'manage_project': True,
        'own_project': False
        },
    {
        'id': '540a69bd-7a6b-4968-b4ab-ccb64299320d',
        'invitee': 11,
        'project': 'c4b8a90b-2963-4d13-aa07-b6f497252dde',
        'can_change': False,
        'manage_project': True,
        'own_project': True
    }
]}
```


## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/projectgroupmembershipinvitation/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('projectgroupmembershipinvitation', id='b6529885-e670-4052-98c5-ea10d447e134')
```

### Response example
{: .no_toc}

```
{'project_group_membership_invitation': {
    'id': 'b6529885-e670-4052-98c5-ea10d447e134',
    'invitee': 8,
    'project': 'a31e6de1-bd46-4f48-9afe-620ae6435a09',
    'can_change': False,
    'manage_project': True,
    'own_project': False
}}
```


## Accept
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/projectgroupmembershipinvitation/<id\>/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model("projectgroupmembershipinvitation", id="b6529885-e670-4052-98c5-ea10d447e134", options="accept")
```



## Reject
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/projectgroupmembershipinvitation/<id\>/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model("projectgroupmembershipinvitation", id="540a69bd-7a6b-4968-b4ab-ccb64299320d", options="reject")
```


## Cancel
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/projectgroupmembershipinvitation/<id\>/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model("projectgroupmembershipinvitation", id="50be407d-0e20-43cd-8795-b88bbd0dab22", options="cancel")
```