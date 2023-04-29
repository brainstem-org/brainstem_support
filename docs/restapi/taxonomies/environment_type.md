---
layout: default
title: Environment type
parent: Taxonomies
grand_parent: REST API
nav_order: 7
---

# Environment type API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | string with UUID identificator |
| `name` | string **[required]** [max length: 200]|
| `description` | string |
| `comments` | string |


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/taxonomies/environmenttype
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'environmenttype')
```

### Response example
{: .no_toc}

```
{'environment_types': [
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
- **URL:** http://brainstem.org/rest/private/taxonomies/environmenttype
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: Environment Types submissions go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "environmenttype",  data={
        "name": "MyNewEnvironmentType",
        "description": "",
    }
)
```

### Response example
{: .no_toc}

```
{'environment_type_approval': {'
    id': '725ef635-09b7-4817-98f7-d58e598b445e',
    'name': 'MyNewEnvironmentType',
    'description': '',
    'comments': ''}
}
```


## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/taxonomies/environmenttype/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'environmenttype', id='a2510c9e-3ef2-40eb-b4b4-70b8a3fbd3c6')
```

### Response example
{: .no_toc}

```
{'environment_type': {
    'id': 'a2510c9e-3ef2-40eb-b4b4-70b8a3fbd3c6',
    'name': 'MyNewEnvironmentType',
    'description': ''}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/taxonomies/environmenttype/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: environmenttypes changes go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "environmenttype", id="a2510c9e-3ef2-40eb-b4b4-70b8a3fbd3c6", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'environment_type_approval': {
    'id': '511f5736-5c34-46c5-b4d2-d7bb0727b5fe',
    'name': 'MyNewEnvironmentType',
    'description': 'new text',
    'comments': ''}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** http://brainstem.org/rest/private/taxonomies/environmenttype/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

**Note**: only administrators can delete Environment Types.

### Use example (using Python API)
{: .no_toc}

```
resp = delete_model(settings, "environmenttype", id="a2510c9e-3ef2-40eb-b4b4-70b8a3fbd3c6")
``` 


## List approvals
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/taxonomies/environmenttype_approvals
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'environmenttypeapproval')
```

### Response example
{: .no_toc}

```
{'environment_type_approvals': [
    {
        'id': '725ef635-09b7-4817-98f7-d58e598b445e',
        'name': 'MyNewEnvironmentType',
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
- **URL:** http://brainstem.org/rest/private/taxonomies/environmenttype_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'environmenttypeapproval', id='725ef635-09b7-4817-98f7-d58e598b445e')
```

### Response example
{: .no_toc}

```
{'environment_type_approval': {
    'id': '725ef635-09b7-4817-98f7-d58e598b445e',
    'name': 'MyNewEnvironmentType',
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
- **URL:** http://brainstem.org/rest/private/taxonomies/environmenttype_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "environmenttypeapproval", id="725ef635-09b7-4817-98f7-d58e598b445e", options="accept")
```


## Reject approval
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/taxonomies/environmenttype_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "environmenttypeapproval", id="511f5736-5c34-46c5-b4d2-d7bb0727b5fe", options="reject")
```