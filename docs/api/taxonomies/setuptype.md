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
| `description` | string [max length: 2000] |
| `category` | single-character code categorizing the setup type **[required for POST; optional for PATCH]** |
| `comments` | string, used when proposing approval changes |

Optional fields such as `comments` can be omitted from list/detail responses when empty.


These are the available `category` options for Setup Type:
- `I`: In Vitro
- `E`: Ex Vivo
- `A`: Anesthetized In Vivo
- `H`: Head-Fixed Awake
- `V`: Voluntarily Stationary Awake
- `F`: Freely Moving Awake
- `U`: Unknown


## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/setuptype
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('setuptype')
```

### Response example
{: .no_toc}

```
{'setup_types': [
    {
        'id': '<id>',
        'name': 'Barnes maze',
        'description': 'The Barnes maze is a paradigm to study spatial learning and memory. It consists of a circular table with holes around the circumference.',
        'category': 'F'
    },
    {
        'id': '<id>',
        'name': 'Theta maze',
        'description': 'A circular maze with a central arm going across the center of the circle.',
        'category': 'U'
    },
    {
        'id': '<id>',
        'name': 'Y-maze',
        'description': 'The Y-maze is, similar to the T-maze, a test to investigate spatial learning and memory. Specifically designed for testing rats or mice.',
        'category': 'U'
    }
]}
```

Public list responses also include a `meta` object (pagination/filter metadata).


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/taxonomies/setuptype
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: Setup Types submissions go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("setuptype",  data={
        "name": "MyNewSetupType",
        "description": "",
        "category": "F",
    }
)
```

### Response example
{: .no_toc}

```
{'setup_type_approval': {
    'id': '<id>',
    'name': 'MyNewSetupType',
    'description': '',
    'category': 'F'}
}
```


## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/setuptype/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('setuptype', id='<id>')
```

### Response example
{: .no_toc}

```
{'setup_type': {
    'id': '<id>',
    'name': 'MyNewSetupType',
    'description': '',
    'category': 'F'}
}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/setuptype/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: setuptypes changes go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("setuptype", id="<id>", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'setup_type_approval': {
    'id': '<id>',
    'name': 'MyNewSetupType',
    'description': 'new text',
    'category': 'F'}
}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/taxonomies/setuptype/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

**Note**: only administrators can delete Setup Types.

### Use example (using Python API)
{: .no_toc}

```
resp = client.delete("setuptype", id="<id>")
``` 


## List approvals
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/setuptypeapproval
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('setuptypeapproval')
```

### Response example
{: .no_toc}

```
{'setup_type_approvals': [
    {
        'id': '<id>',
        'name': 'MyNewSetupType',
        'description': '',
        'category': 'F',
        'instance_id': None,
        'action': 'Add',
        'reviewer': None,
        'status': 'Pending'
    },
    {
        'id': '<id>',
        'name': 'MyNewMaze',
        'description': '',
        'category': 'U',
        'instance_id': '<instance_id-id>',
        'action': 'Add',
        'reviewer': 3,
        'status': 'Rejected'
    }
]}
```


## Detail approval
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/setuptypeapproval/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('setuptypeapproval', id='<id>')
```

### Response example
{: .no_toc}

```
{'setup_type_approval': {
    'id': '<id>',
    'name': 'MyNewSetupType',
    'description': '',
    'category': 'F',
    'instance_id': None,
    'action': 'Add',
    'reviewer': None,
    'status': 'Pending'}
}
```


## Accept approval
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/setuptypeapproval/<id\>/accept/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("setuptypeapproval", id="<id>", options="accept")
```


## Reject approval
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/setuptypeapproval/<id\>/reject/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("setuptypeapproval", id="<id>", options="reject")
```
