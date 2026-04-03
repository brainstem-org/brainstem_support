---
layout: default
title: Behavioral paradigm
parent: Taxonomies
grand_parent: API
nav_order: 2
---

# Behavioral paradigm API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `name` | string **[required]** [must be unique] |
| `description` | string |
| `category` | related behavioral category ID |
| `species` | related species ID(s) |
| `original_publication` | string |
| `reference_url` | URL string |
| `rrid` | Research Resource Identifier (RRID) |
| `external_identifiers` | JSON object containing external identifier information |
| `comments` | string, used when proposing approval changes |

Optional fields such as `comments` can be omitted from list/detail responses when empty.



## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralparadigm
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('behavioralparadigm')
```

### Response example
{: .no_toc}

```
{'behavioral_paradigms': [
    {
        'id': '<id>',
        'name': 'Morris Water Navigation Task',
        'description': 'A spatial learning task using a water maze to assess hippocampal-dependent spatial memory',
        'category': '<category-id>',
        'species': [],
        'original_publication': 'Morris 1984',
        'reference_url': '',
        'rrid': None,
        'external_identifiers': None
    },
    {
        'id': '<id>',
        'name': 'Elevated Plus Exploration',
        'description': 'Assessment of anxiety-like behavior via open arm avoidance on an elevated plus-shaped maze',
        'category': '<category-id>',
        'species': [],
        'original_publication': '',
        'reference_url': '',
        'rrid': None,
        'external_identifiers': None
    }
]}
```

Public list responses also include a `meta` object (pagination/filter metadata).


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralparadigm
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: Behavioral paradigm submissions go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("behavioralparadigm", data={
        "name": "Rotarod",
        "description": "Assessment of balance, coordination, and motor learning on a rotating rod",
        "category": "<category-id>",
        "original_publication": "Dunham & Miya 1957",
    }
)
```

### Response example
{: .no_toc}

```
{'behavioral_paradigm_approval': {
    'id': '<id>',
    'name': 'Rotarod',
    'description': 'Assessment of balance, coordination, and motor learning on a rotating rod',
    'category': '<category-id>',
    'species': [],
    'original_publication': 'Dunham & Miya 1957',
    'reference_url': '',
    'rrid': None,
    'external_identifiers': None}
}
```

## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralparadigm/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('behavioralparadigm', id='<id>')
```

### Response example
{: .no_toc}

```
{'behavioral_paradigm': {
    'id': '<id>',
    'name': 'Morris Water Navigation Task',
    'description': 'A spatial learning task using a water maze to assess hippocampal-dependent spatial memory',
    'category': '<category-id>',
    'species': [],
    'original_publication': 'Morris 1984',
    'reference_url': '',
    'rrid': None,
    'external_identifiers': None}
}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralparadigm/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: Behavioral paradigm changes go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("behavioralparadigm", id="<id>", data={"description": "updated description"})
```

### Response example
{: .no_toc}

```
{'behavioral_paradigm_approval': {
    'id': '<id>',
    'name': 'Morris Water Navigation Task',
    'description': 'updated description',
    'category': '<category-id>',
    'species': [],
    'original_publication': 'Morris 1984',
    'reference_url': '',
    'rrid': None,
    'external_identifiers': None}
}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralparadigm/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

**Note**: only administrators can delete Behavioral paradigms.

### Use example (using Python API)
{: .no_toc}

```
resp = client.delete("behavioralparadigm", id="<id>")
``` 


## List approvals
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralparadigmapproval
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('behavioralparadigmapproval')
```

### Response example
{: .no_toc}

```
{'behavioral_paradigm_approvals': [
    {
        'id': '<id>',
        'name': 'Rotarod',
        'description': 'Assessment of balance, coordination, and motor learning on a rotating rod',
        'category': '<category-id>',
        'species': [],
        'original_publication': 'Dunham & Miya 1957',
        'reference_url': '',
        'rrid': None,
        'external_identifiers': None,
        'instance_id': None,
        'action': 'Add',
        'reviewer': None,
        'status': 'Pending'
    }
]}
```


## Detail approval
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralparadigmapproval/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('behavioralparadigmapproval', id='<id>')
```

### Response example
{: .no_toc}

```
{'behavioral_paradigm_approval': {
    'id': '<id>',
    'name': 'Rotarod',
    'description': 'Assessment of balance, coordination, and motor learning on a rotating rod',
    'category': '<category-id>',
    'species': [],
    'original_publication': 'Dunham & Miya 1957',
    'reference_url': '',
    'rrid': None,
    'external_identifiers': None,
    'instance_id': None,
    'action': 'Add',
    'reviewer': None,
    'status': 'Pending'}
}
```


## Accept approval
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralparadigmapproval/<id\>/accept/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("behavioralparadigmapproval", id="<id>", options="accept")
```


## Reject approval
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralparadigmapproval/<id\>/reject/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("behavioralparadigmapproval", id="<id>", options="reject")
```
