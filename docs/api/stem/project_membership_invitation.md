---
layout: default
title: Project Membership Invitation
parent: STEM
grand_parent: API
nav_order: 6
---

# Project Membership Invitation API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `invitee` | invited user ID formatted as an integer |
| `project` | related project ID formatted as a string |
| `can_change` | boolean |
| `manage_project` | boolean |
| `own_project` | boolean |



## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/projectmembershipinvitation
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('projectmembershipinvitation')
```

### Response example
{: .no_toc}

```
{'project_membership_invitations': [
    {
        'id': '5c386192-1dc6-42d1-84a0-6561fa61845d',
        'invitee': 27,
        'project': 'a31e6de1-bd46-4f48-9afe-620ae6435a09',
        'can_change': False,
        'manage_project': False,
        'own_project': False
    },
    {
        'id': '4acd89b5-7d85-4ecb-94b1-094ee6473dbb',
        'invitee': 1,
        'project': 'c4b8a90b-2963-4d13-aa07-b6f497252dde',

        'can_change': False,
        'manage_project': False,
        'own_project': False
    }
]}
```


## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/projectmembershipinvitation/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('projectmembershipinvitation', id='5c386192-1dc6-42d1-84a0-6561fa61845d')
```

### Response example
{: .no_toc}

```
{'project_membership_invitation': {
    'id': '5c386192-1dc6-42d1-84a0-6561fa61845d',
    'invitee': 27,
    'project': 'a31e6de1-bd46-4f48-9afe-620ae6435a09',
    'can_change': False,
    'manage_project': False,
    'own_project': False}
}
```


## Accept
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/projectmembershipinvitation/<id\>/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model("projectmembershipinvitation", id="5c386192-1dc6-42d1-84a0-6561fa61845d", options="accept")
```



## Reject
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/projectmembershipinvitation/<id\>/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model("projectmembershipinvitation", id="0f1e0097-0f41-4c52-82f2-d643be507120", options="reject")
```


## Cancel
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/projectmembershipinvitation/<id\>/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model("projectmembershipinvitation", id="5c386192-1dc6-42d1-84a0-6561fa61845d", options="cancel")
```