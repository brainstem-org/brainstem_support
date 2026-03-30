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
| `id` | UUID identificator formatted as a string |
| `name` | string **[required]** [max length: 500] |
| `description` | string [max length: 2000] |
| `website` | string [max length: 200] |
| `comments` | string, used when proposing approval changes |

Optional fields such as `comments` can be omitted from list/detail responses when empty.


## List view

- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/dissemination/journal
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('journal')
```

### Response example
{: .no_toc}

```
{'journals': [
    {
        'id': '<id>',
        'name': 'bioRxiv',
        'description': '',
        'website': 'https://www.biorxiv.org'
    },
    {
        'id': '<id>',
        'name': 'eLife',
        'description': '',
        'website': ''
    },
    {
        'id': '<id>',
        'name': 'SomeJournal',
        'description': '',
        'website': ''
    }
]}
```

Public list responses also include a `meta` object (pagination/filter metadata).


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
resp = client.save("journal",  data={
    'name': 'MyNewJournal',
    'description': '',
    'website': 'newjournal.com'}
)
```

### Response example
{: .no_toc}

```
{'journal_approval': {
        'id': '<id>',
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
resp = client.load('journal', id='<id>')
```

### Response example
{: .no_toc}

```
{'journal': {
    'id': '<id>',
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
resp = client.save("journal", id="<id>", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'journal_approval': {
    'id': '<id>',
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
resp = client.delete("journal", id="<id>")
```

## List approvals

- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/dissemination/journalapproval
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('journalapproval')
```

### Response example
{: .no_toc}

```
{'journal_approvals': [
    {
        'id': '<id>',
        'name': 'SomeJournal',
        'description': 'new text',
        'website': '',
        'instance_id': '<instance_id-id>',
        'action': 'Change',
        'reviewer': None,
        'status': 'Pending'
    },
    {
        'id': '<id>',
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
- **URL:** https://www.brainstem.org/api/private/dissemination/journalapproval/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('journalapproval', id='<id>')
```

### Response example
{: .no_toc}

```
{'journal_approval': {
    'id': '<id>',
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
- **URL:** https://www.brainstem.org/api/private/dissemination/journalapproval/<id\>/accept/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("journalapproval", id="<id>", options="accept")
```


## Reject approval

- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/dissemination/journalapproval/<id\>/reject/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("journalapproval", id="<id>", options="reject")
```
