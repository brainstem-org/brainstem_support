---
layout: default
title: Setup type
parent: Taxonomies
grand_parent: API
nav_order: 7
---

# Setup type API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `name` | string **[required]** [max length: 200]|
| `description` | string [max length: 500] |
| `comments` | string |


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/setuptype
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('setuptype')
```

### Response example
{: .no_toc}

```
{'setup_types': [
    {
        'id': '531b2a21-ab1f-4aa8-8eaf-905421168d6b',
        'name': 'Barnes maze',
        'description': 'The Barnes maze is a paradigm to study spatial learning and memory. It consists of a circular table with holes around the circumference.'
    },
    {
        'id': '414a49b2-61b5-4ef5-8b64-6528d5f1ed8d',
        'name': 'Theta maze',
        'description': 'A circular maze with a central arm going across the center of the circle.'
    },
    {
        'id': '70b1d2eb-a721-4fef-8e86-0c2b1469283a',
        'name': 'Y-maze',
        'description': 'The Y-maze is, similar to the T-maze, a test to investigate spatial learning and memory. Specifically designed for testing rats or mice.'
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/taxonomies/setuptype
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: Setup Types submissions go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("setuptype",  data={
        "name": "MyNewSetupType",
        "description": "",
    }
)
```

### Response example
{: .no_toc}

```
{'setup_type_approval': {'
    id': '725ef635-09b7-4817-98f7-d58e598b445e',
    'name': 'MyNewSetupType',
    'description': '',
    'comments': ''}
}
```


## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/setuptype/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('setuptype', id='a2510c9e-3ef2-40eb-b4b4-70b8a3fbd3c6')
```

### Response example
{: .no_toc}

```
{'setup_type': {
    'id': 'a2510c9e-3ef2-40eb-b4b4-70b8a3fbd3c6',
    'name': 'MyNewSetupType',
    'description': ''}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/setuptype/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: setuptypes changes go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("setuptype", id="a2510c9e-3ef2-40eb-b4b4-70b8a3fbd3c6", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'setup_type_approval': {
    'id': '511f5736-5c34-46c5-b4d2-d7bb0727b5fe',
    'name': 'MyNewSetupType',
    'description': 'new text',
    'comments': ''}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/taxonomies/setuptype/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

**Note**: only administrators can delete Setup Types.

### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("setuptype", id="a2510c9e-3ef2-40eb-b4b4-70b8a3fbd3c6")
``` 


## List approvals
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/setuptype_approvals
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('setuptypeapproval')
```

### Response example
{: .no_toc}

```
{'setup_type_approvals': [
    {
        'id': '725ef635-09b7-4817-98f7-d58e598b445e',
        'name': 'MyNewSetupType',
        'description': '',
        'comments': '',
        'instance_id': None,
        'action': 'Add',
        'reviewer': None,
        'status': 'Pending'
    },
    {
        'id': '97b70a5e-52f9-4358-8b27-0a886248e749',
        'name': 'MyNewMaze',
        'description': '',
        'comments': '',
        'instance_id': 'e10ea8ab-9afa-4060-8382-dc9d9e1763f8',
        'action': 'Add',
        'reviewer': 3,
        'status': 'Rejected'
    }
]}
```


## Detail approval
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/setuptype_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('setuptypeapproval', id='725ef635-09b7-4817-98f7-d58e598b445e')
```

### Response example
{: .no_toc}

```
{'setup_type_approval': {
    'id': '725ef635-09b7-4817-98f7-d58e598b445e',
    'name': 'MyNewSetupType',
    'description': '',
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
- **URL:** https://www.brainstem.org/api/private/taxonomies/setuptype_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("setuptypeapproval", id="725ef635-09b7-4817-98f7-d58e598b445e", options="accept")
```


## Reject approval
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/setuptype_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("setuptypeapproval", id="511f5736-5c34-46c5-b4d2-d7bb0727b5fe", options="reject")
```