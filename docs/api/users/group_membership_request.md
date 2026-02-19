---
layout: default
title: Group Membership Request
parent: Users
grand_parent: API
nav_order: 4
---

# Group Membership Request API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `user_account_request` | requesting user ID formatted as an integer |
| `authgroup` | related group ID formatted as an integer |


## List view
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/groupmembershiprequest
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('groupmembershiprequest')
```

### Response example
{: .no_toc}

```
{'group_membership_requests': [
    {
        'id': 'fd335535-cf79-4ae8-86af-ed87e1108889',
        'user_account_request': 3,
        'authgroup': 9
    },
    {
        'id': '5a6378e9-be26-4f0f-8e12-2d11a05cd769',
        'user_account_request': 3,
        'authgroup': 1
    },
]}
```

List responses include a `meta` object (pagination/filter metadata).


## Detail
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/groupmembershiprequest/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('groupmembershiprequest', id='fd335535-cf79-4ae8-86af-ed87e1108889')
```

### Response example
{: .no_toc}

```
{'group_membership_request': {
    'id': 'fd335535-cf79-4ae8-86af-ed87e1108889',
    'user_account_request': 3,
    'authgroup': 9}
}
```


## Accept
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/groupmembershiprequest/<id\>/accept/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model("groupmembershiprequest", id="fd335535-cf79-4ae8-86af-ed87e1108889", options="accept")
```



## Reject
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/groupmembershiprequest/<id\>/reject/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model("groupmembershiprequest", id="5a6378e9-be26-4f0f-8e12-2d11a05cd769", options="reject")
```


## Cancel
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/users/groupmembershiprequest/<id\>/cancel/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model("groupmembershiprequest", id="263fa5ff-1dd0-4b20-a028-5679ac1b54cf", options="cancel")
```
