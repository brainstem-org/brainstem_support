---
layout: default
title: Users - Group Membership Request
parent: API endpoints
grand_parent: REST API
nav_order: 8
---

## Table of contents
- [Fields](/brainstem_support/restapi/users/group_membership_request/#fields)
- Endpoints
  - [List view](/brainstem_support/restapi/users/group_membership_request/#list-view)
  - [Detail](/brainstem_support/restapi/users/group_membership_request/#detail)
  - [Accept](/brainstem_support/restapi/users/group_membership_request/#accept)
  - [Reject](/brainstem_support/restapi/users/group_membership_request/#reject)
  - [Cancel](/brainstem_support/restapi/users/group_membership_request/#cancel)

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | string with UUID identificator |
| `user_account_request` | string with the requesting user ID |
| `authgroup` | string with the related group ID |



## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/users/groupmembershiprequest
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'groupmembershiprequest')
```

### Response example
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


## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/users/groupmembershiprequest/<id>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'groupmembershiprequest', id='fd335535-cf79-4ae8-86af-ed87e1108889')
```

### Response example
```
{'group_membership_request': {
    'id': 'fd335535-cf79-4ae8-86af-ed87e1108889',
    'user_account_request': 3,
    'authgroup': 9}
}
```


## Accept
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/users/groupmembershiprequest/<id>/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, "groupmembershiprequest", id="fd335535-cf79-4ae8-86af-ed87e1108889", options="accept")
```



## Reject
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/users/groupmembershiprequest/<id>/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, "groupmembershiprequest", id="5a6378e9-be26-4f0f-8e12-2d11a05cd769", options="reject")
```


## Cancel
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/users/groupmembershiprequest/<id>/
- **Data:** None
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, "groupmembershiprequest", id="263fa5ff-1dd0-4b20-a028-5679ac1b54cf", options="cancel")
```