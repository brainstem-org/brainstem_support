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
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/projectmembershipinvitation/
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
        'id': '00000000-0000-0000-0000-000000000000',
        'invitee': 27,
        'project': '00000000-0000-0000-0000-000000000000',
        'can_change': False,
        'manage_project': False,
        'own_project': False
    },
    {
        'id': '00000000-0000-0000-0000-000000000000',
        'invitee': 1,
        'project': '00000000-0000-0000-0000-000000000000',

        'can_change': False,
        'manage_project': False,
        'own_project': False
    }
]}
```


## Detail
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/projectmembershipinvitation/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('projectmembershipinvitation', id='00000000-0000-0000-0000-000000000000')
```

### Response example
{: .no_toc}

```
{'project_membership_invitation': {
    'id': '00000000-0000-0000-0000-000000000000',
    'invitee': 27,
    'project': '00000000-0000-0000-0000-000000000000',
    'can_change': False,
    'manage_project': False,
    'own_project': False}
}
```


## Accept
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/projectmembershipinvitation/<id\>/accept/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model("projectmembershipinvitation", id="00000000-0000-0000-0000-000000000000", options="accept")
```



## Reject
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/projectmembershipinvitation/<id\>/reject/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model("projectmembershipinvitation", id="00000000-0000-0000-0000-000000000000", options="reject")
```


## Cancel
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/projectmembershipinvitation/<id\>/cancel/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model("projectmembershipinvitation", id="00000000-0000-0000-0000-000000000000", options="cancel")
```
