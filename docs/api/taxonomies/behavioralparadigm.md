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
| `rrid_url` | URL to RRID lookup page **[read-only]** |
| `external_identifiers` | JSON object containing external identifier information |


## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralparadigm
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('behavioralparadigm')
```

### Response example
{: .no_toc}

```
{'behavioralparadigms': [
    {
        'id': 'e5f6a7b8-9012-34ef-0123-5678901234ef',
        'name': 'Morris Water Navigation Task',
        'description': 'A spatial learning task using a water maze to assess hippocampal-dependent spatial memory',
        'category': 'b2c3d4e5-6789-01bc-def0-2345678901bc',
        'species': [],
        'original_publication': 'Morris 1984',
        'reference_url': '',
        'rrid': None,
        'external_identifiers': None
    },
    {
        'id': 'f6a7b8c9-0123-45f0-1234-6789012345f0',
        'name': 'Elevated Plus Exploration',
        'description': 'Assessment of anxiety-like behavior via open arm avoidance on an elevated plus-shaped maze',
        'category': 'c3d4e5f6-7890-12cd-ef01-3456789012cd',
        'species': [],
        'original_publication': '',
        'reference_url': '',
        'rrid': None,
        'external_identifiers': None
    }
]}
```


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
resp = client.save_model("behavioralparadigm", data={
        "name": "Rotarod",
        "description": "Assessment of balance, coordination, and motor learning on a rotating rod",
        "category": "c3d4e5f6-7890-12cd-ef01-3456789012cd",
        "original_publication": "Dunham & Miya 1957",
    }
)
```

### Response example
{: .no_toc}

```
{'behavioralparadigm_approval': {
    'id': 'a7b8c9d0-1234-56a1-2345-7890123456a1',
    'name': 'Rotarod',
    'description': 'Assessment of balance, coordination, and motor learning on a rotating rod',
    'category': 'c3d4e5f6-7890-12cd-ef01-3456789012cd',
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
resp = client.load_model('behavioralparadigm', id='e5f6a7b8-9012-34ef-0123-5678901234ef')
```

### Response example
{: .no_toc}

```
{'behavioralparadigm': {
    'id': 'e5f6a7b8-9012-34ef-0123-5678901234ef',
    'name': 'Morris Water Navigation Task',
    'description': 'A spatial learning task using a water maze to assess hippocampal-dependent spatial memory',
    'category': 'b2c3d4e5-6789-01bc-def0-2345678901bc',
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
resp = client.save_model("behavioralparadigm", id="e5f6a7b8-9012-34ef-0123-5678901234ef", data={"description": "updated description"})
```

### Response example
{: .no_toc}

```
{'behavioralparadigm_approval': {
    'id': 'b8c9d0e1-2345-67b2-3456-8901234567b2',
    'name': 'Morris Water Navigation Task',
    'description': 'updated description',
    'category': 'b2c3d4e5-6789-01bc-def0-2345678901bc',
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
resp = client.delete_model("behavioralparadigm", id="e5f6a7b8-9012-34ef-0123-5678901234ef")
``` 


## List approvals
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralparadigm_approvals
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('behavioralparadigmapproval')
```

### Response example
{: .no_toc}

```
{'behavioralparadigm_approvals': [
    {
        'id': 'a7b8c9d0-1234-56a1-2345-7890123456a1',
        'name': 'Rotarod',
        'description': 'Assessment of balance, coordination, and motor learning on a rotating rod',
        'category': 'c3d4e5f6-7890-12cd-ef01-3456789012cd',
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
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralparadigm_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('behavioralparadigmapproval', id='a7b8c9d0-1234-56a1-2345-7890123456a1')
```

### Response example
{: .no_toc}

```
{'behavioralparadigm_approval': {
    'id': 'a7b8c9d0-1234-56a1-2345-7890123456a1',
    'name': 'Rotarod',
    'description': 'Assessment of balance, coordination, and motor learning on a rotating rod',
    'category': 'c3d4e5f6-7890-12cd-ef01-3456789012cd',
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
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralparadigm_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("behavioralparadigmapproval", id="a7b8c9d0-1234-56a1-2345-7890123456a1", options="accept")
```


## Reject approval
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralparadigm_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("behavioralparadigmapproval", id="b8c9d0e1-2345-67b2-3456-8901234567b2", options="reject")
```
