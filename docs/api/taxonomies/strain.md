---
layout: default
title: Strain
parent: Taxonomies
grand_parent: API
nav_order: 7
---

# Strain API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `name` | string **[required]** [max length: 100; must be unique] |
| `description` | string [max length: 2000] |
| `species` | related species ID formatted as a string **[required]** |
| `rrid` | Research Resource Identifier (RRID) |
| `rrid_url` | URL to RRID lookup page **[read-only]** |
| `external_identifiers` | JSON object containing external identifier information |
| `comments` | string, used when proposing approval changes |

Optional fields such as `comments` can be omitted from list/detail responses when empty.



## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/strain
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('strain')
```

### Response example
{: .no_toc}

```
{'strains': [
    {
        'id': '<id>',
        'name': 'Brown Norway',
        'description': '',
        'species': '<species-id>',
        'rrid': None,
        'rrid_url': None,
        'external_identifiers': []
    },
    {
        'id': '<id>',
        'name': 'Red-eared slider',
        'description': '',
        'species': '<species-id>',
        'rrid': None,
        'rrid_url': None,
        'external_identifiers': []
    }
]}
```

Public list responses also include a `meta` object (pagination/filter metadata).


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/taxonomies/strain
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: Strains submissions go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("strain", data={
        "name": "MyNewStrain",
        "description": "",
        "species": "<species-id>",
    }
)
```

### Response example
{: .no_toc}

```
{'strain_approval': {
    'id': '<id>',
    'name': 'MyNewStrain',
    'description': '',
    'species': '<species-id>',
    'rrid': None,
    'external_identifiers': []}
}
```

## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/strain/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('strain', id='<id>')
```

### Response example
{: .no_toc}

```
{'strain': {
    'id': '<id>',
    'name': 'MyNewStrain',
    'description': '',
    'species': '<species-id>',
    'rrid': None,
    'rrid_url': None,
    'external_identifiers': []}
}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/strain/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: Strains changes go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("strain", id="<id>", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'strain_approval': {
    'id': '<id>',
    'name': 'MyNewStrain',
    'description': 'new text',
    'species': '<species-id>',
    'rrid': None,
    'external_identifiers': []}
}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/taxonomies/strain/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

**Note**: only administrators can delete Strains.

### Use example (using Python API)
{: .no_toc}

```
resp = client.delete("strain", id="<id>")
``` 


## List approvals
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/strainapproval
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('strainapproval')
```

### Response example
{: .no_toc}

```
{'strain_approvals': [
    {
        'id': '<id>',
        'name': 'MyNewStrain',
        'description': '',
        'species': '<species-id>',
        'rrid': None,
        'external_identifiers': [],
        'instance_id': None,
        'action': 'Add',
        'reviewer': None,
        'status': 'Pending'
    },
    {
        'id': '<id>',
        'name': 'Agumon',
        'description': '',
        'species': '<species-id>',
        'rrid': None,
        'external_identifiers': [],
        'instance_id': None,
        'action': 'Add',
        'reviewer': 3,
        'status': 'Rejected'
    }
]}
```


## Detail approval
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/strainapproval/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('strainapproval', id='<id>')
```

### Response example
{: .no_toc}

```
{'strain_approval': {
    'id': '<id>',
    'name': 'MyNewStrain',
    'description': '',
    'species': '<species-id>',
    'rrid': None,
    'external_identifiers': [],
    'instance_id': None,
    'action': 'Add',
    'reviewer': None,
    'status': 'Pending'}
}
```


## Accept approval
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/strainapproval/<id\>/accept/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("strainapproval", id="<id>", options="accept")
```


## Reject approval
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/strainapproval/<id\>/reject/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("strainapproval", id="<id>", options="reject")
```
