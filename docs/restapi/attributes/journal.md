---
layout: default
title: General attributes - Journal
parent: API endpoints
grand_parent: REST API
nav_order: 4
---

## Table of contents
- [Fields](/brainstem_support/restapi/attributes/journal/#fields)
- Endpoints
  - [List view](/brainstem_support/restapi/attributes/journal/#list-view)
  - [Add](/brainstem_support/restapi/attributes/journal/#add)
  - [Detail](/brainstem_support/restapi/attributes/journal/#detail)
  - [Change](/brainstem_support/restapi/attributes/journal/#change)
  - [Delete](/brainstem_support/restapi/attributes/journal/#delete)
  - [List approvals](/brainstem_support/restapi/attributes/journal/#list-approvals)
  - [Detail approval](/brainstem_support/restapi/attributes/journal/#detail-approval)
  - [Accept approval](/brainstem_support/restapi/attributes/journal/#accept-approval)
  - [Reject approval](/brainstem_support/restapi/attributes/journal/#reject-approval)

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | string with UUID identificator |
| `name` | string **[required]** |
| `description` | string |
| `website` | string |
| `comments` | string |


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/attributes/journal
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'journal')
```

### Response example
```
{'journals': [
    {
        'id': 'fb66207b-bc2d-4e93-9047-7ad38a8883ef',
        'name': 'bioRxiv',
        'description': '',
        'website': 'https://www.biorxiv.org'
    },
    {
        'id': 'd061bcf6-ac0c-4aa1-8ead-09aadbde7bf9',
        'name': 'eLife',
        'description': '',
        'website': ''
    },
    {
        'id': 'da3359b7-e380-4dc6-ba9d-04831d3082d9',
        'name': 'SomeJournal',
        'description': '',
        'website': ''
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** http://brainstem.org/rest/private/attributes/journal
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: journals submissions go through an approval process.

### Use example (using Python API)
```
resp = save_model(settings, "journal",  data={
    'name': 'MyNewJournal',
    'description': '',
    'website': 'newjournal.com'}
)
```

### Response example
```
{'journal_approval': {
        'id': 'dfb879c9-0e31-420b-8918-64dc30dbec6d',
        'name': 'MyNewJournal',
        'description': '',
        'website': 'http://newjournal.com',
        'comments': ''
    }
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/attributes/journal/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'journal', id='da3359b7-e380-4dc6-ba9d-04831d3082d9')
```

### Response example
```
{'journal': {
    'id': 'da3359b7-e380-4dc6-ba9d-04831d3082d9',
    'name': 'SomeJournal',
    'description': '',
    'website': ''}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/attributes/journal/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: journals changes go through an approval process.

### Use example (using Python API)
```
resp = save_model(settings, "journal", id="da3359b7-e380-4dc6-ba9d-04831d3082d9", data={"description": "new text"})
```

### Response example
```
{'journal_approval': {
    'id': '640ea107-cf9e-413a-b0b8-562082654481',
    'name': 'SomeJournal',
    'description': 'new text',
    'website': '',
    'comments': ''}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** http://brainstem.org/rest/private/attributes/journal/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = delete_model(settings, "journal", id="d37c9255-d5ae-47d9-b6e1-4ec760c200fb")
``` 


## List approvals
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/attributes/journal_approvals
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'journalapproval')
```

### Response example
```
{'journal_approvals': [
    {
        'id': '640ea107-cf9e-413a-b0b8-562082654481',
        'name': 'SomeJournal',
        'description': 'new text',
        'website': '',
        'comments': '',
        'instance_id': 'da3359b7-e380-4dc6-ba9d-04831d3082d9',
        'action': 'Change',
        'reviewer': None,
        'status': 'Pending'
    },
    {
        'id': '41f99539-e54e-4224-8e53-88a692f9a185',
        'name': 'MyNewJournal',
        'description': '',
        'website': 'http://newjournal.com',
        'comments': '',
        'instance_id': None,
        'action': 'Add',
        'reviewer': None,
        'status': 'Accepted'
    }
]}
```


## Detail approval
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/attributes/journal_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'journalapproval', id='41f99539-e54e-4224-8e53-88a692f9a185')
```

### Response example
```
{'journal_approval': {
    'id': '41f99539-e54e-4224-8e53-88a692f9a185',
    'name': 'MyNewJournal',
    'description': '',
    'website': 'http://newjournal.com',
    'comments': '',
    'instance_id': None,
    'action': 'Add',
    'reviewer': None,
    'status': 'Pending'}
}
```


## Accept approval
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/attributes/journal_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = save_model(settings, "journalapproval", id="41f99539-e54e-4224-8e53-88a692f9a185", options="accept")
```


## Reject approval
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/attributes/journal_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = save_model(settings, "journalapproval", id="41f99539-e54e-4224-8e53-88a692f9a185", options="reject")
```