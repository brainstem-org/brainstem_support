---
layout: default
title: Journal
parent: General attributes
grand_parent: REST API
nav_order: 4
---

# Journal API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | string with UUID identificator|
| `name` | string **[required]** [max length: 500] |
| `description` | string [max length: 500] |
| `website` | string [max length: 200]|
| `comments` | string |


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/attributes/journal
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'journal')
```

### Response example
{: .no_toc}

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
- **URL:** https://www.brainstem.org/api/private/attributes/journal
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: journals submissions go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "journal",  data={
    'name': 'MyNewJournal',
    'description': '',
    'website': 'newjournal.com'}
)
```

### Response example
{: .no_toc}

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
- **URL:** https://www.brainstem.org/api/private/attributes/journal/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'journal', id='da3359b7-e380-4dc6-ba9d-04831d3082d9')
```

### Response example
{: .no_toc}

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
- **URL:** https://www.brainstem.org/api/private/attributes/journal/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: journals changes go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "journal", id="da3359b7-e380-4dc6-ba9d-04831d3082d9", data={"description": "new text"})
```

### Response example
{: .no_toc}

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
- **URL:** https://www.brainstem.org/api/private/attributes/journal/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = delete_model(settings, "journal", id="d37c9255-d5ae-47d9-b6e1-4ec760c200fb")
``` 


## List approvals
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/attributes/journal_approvals
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'journalapproval')
```

### Response example
{: .no_toc}

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
- **URL:** https://www.brainstem.org/api/private/attributes/journal_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'journalapproval', id='41f99539-e54e-4224-8e53-88a692f9a185')
```

### Response example
{: .no_toc}

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
- **URL:** https://www.brainstem.org/api/private/attributes/journal_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "journalapproval", id="41f99539-e54e-4224-8e53-88a692f9a185", options="accept")
```


## Reject approval
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/attributes/journal_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "journalapproval", id="41f99539-e54e-4224-8e53-88a692f9a185", options="reject")
```