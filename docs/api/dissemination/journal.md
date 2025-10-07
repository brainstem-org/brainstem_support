---
layout: default
title: Journal
parent: Dissemination
grand_parent: API
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
| `id` | UUID identificator formatted as a string|
| `name` | string **[required]** [max length: 500] |
| `description` | string [max length: 500] |
| `website` | string [max length: 200]|


## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/dissemination/journal
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('journal')
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
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/dissemination/journal
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: journals submissions go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("journal",  data={
    'name': 'MyNewJournal',
    'description': '',
    'website': 'newjournal.com'}
)
```

### Response example
{: .no_toc}

```
{'journal_approval': {
        'id': '549b9e4f-5253-44f8-93ee-f18f08a39a36',
        'name': 'MyNewJournal',
        'description': '',
        'website': 'http://newjournal.com'
    }
}
```



## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/dissemination/journal/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('journal', id='da3359b7-e380-4dc6-ba9d-04831d3082d9')
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
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/dissemination/journal/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: journals changes go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("journal", id="da3359b7-e380-4dc6-ba9d-04831d3082d9", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'journal_approval': {
    'id': '640ea107-cf9e-413a-b0b8-562082654481',
    'name': 'SomeJournal',
    'description': 'new text',
    'website': ''}
}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/dissemination/journal/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("journal", id="d37c9255-d5ae-47d9-b6e1-4ec760c200fb")
``` 


## List approvals
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/dissemination/journal_approvals
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('journalapproval')
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
        'instance_id': 'da3359b7-e380-4dc6-ba9d-04831d3082d9',
        'action': 'Change',
        'reviewer': None,
        'status': 'Pending'
    },
    {
        'id': '549b9e4f-5253-44f8-93ee-f18f08a39a36',
        'name': 'MyNewJournal',
        'description': '',
        'website': 'http://newjournal.com',
        'instance_id': None,
        'action': 'Add',
        'reviewer': None,
        'status': 'Accepted'
    }
]}
```


## Detail approval
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/dissemination/journal_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('journalapproval', id='549b9e4f-5253-44f8-93ee-f18f08a39a36')
```

### Response example
{: .no_toc}

```
{'journal_approval': {
    'id': '549b9e4f-5253-44f8-93ee-f18f08a39a36',
    'name': 'MyNewJournal',
    'description': '',
    'website': 'http://newjournal.com',
    'instance_id': None,
    'action': 'Add',
    'reviewer': None,
    'status': 'Pending'}
}
```


## Accept approval
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/dissemination/journal_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("journalapproval", id="549b9e4f-5253-44f8-93ee-f18f08a39a36", options="accept")
```


## Reject approval
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/dissemination/journal_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("journalapproval", id="549b9e4f-5253-44f8-93ee-f18f08a39a36", options="reject")
```