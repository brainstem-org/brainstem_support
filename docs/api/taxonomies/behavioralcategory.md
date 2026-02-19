---
layout: default
title: Behavioral category
parent: Taxonomies
grand_parent: API
nav_order: 1
---

# Behavioral category API endpoint
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
| `parent` | related behavioral category ID |
| `comments` | string, used when proposing approval changes |


## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralcategory
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('behavioralcategory')
```

### Response example
{: .no_toc}

```
{'behavioral_categories': [
    {
        'id': 'a1b2c3d4-5678-90ab-cdef-1234567890ab',
        'name': 'Learning & Memory',
        'description': 'Behavioral tasks assessing learning and memory processes',
        'parent': None
    },
    {
        'id': 'b2c3d4e5-6789-01bc-def0-2345678901bc',
        'name': 'Spatial Learning',
        'description': 'Tasks assessing spatial navigation and spatial memory',
        'parent': 'a1b2c3d4-5678-90ab-cdef-1234567890ab'
    }
]}
```

Public list responses also include a `meta` object (pagination/filter metadata).


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralcategory
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: Behavioral category submissions go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("behavioralcategory", data={
        "name": "Motor Function",
        "description": "Tasks assessing motor abilities and coordination",
    }
)
```

### Response example
{: .no_toc}

```
{'behavioral_category_approval': {
    'id': 'c3d4e5f6-7890-12cd-ef01-3456789012cd',
    'name': 'Motor Function',
    'description': 'Tasks assessing motor abilities and coordination',
    'parent': None}
}
```

## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralcategory/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('behavioralcategory', id='a1b2c3d4-5678-90ab-cdef-1234567890ab')
```

### Response example
{: .no_toc}

```
{'behavioral_category': {
    'id': 'a1b2c3d4-5678-90ab-cdef-1234567890ab',
    'name': 'Learning & Memory',
    'description': 'Behavioral tasks assessing learning and memory processes',
    'parent': None}
}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralcategory/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: Behavioral category changes go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("behavioralcategory", id="a1b2c3d4-5678-90ab-cdef-1234567890ab", data={"description": "updated description"})
```

### Response example
{: .no_toc}

```
{'behavioral_category_approval': {
    'id': 'd4e5f6a7-8901-23de-f012-4567890123de',
    'name': 'Learning & Memory',
    'description': 'updated description',
    'parent': None}
}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralcategory/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

**Note**: only administrators can delete Behavioral categories.

### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("behavioralcategory", id="a1b2c3d4-5678-90ab-cdef-1234567890ab")
``` 


## List approvals
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralcategoryapproval
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('behavioralcategoryapproval')
```

### Response example
{: .no_toc}

```
{'behavioral_category_approvals': [
    {
        'id': 'c3d4e5f6-7890-12cd-ef01-3456789012cd',
        'name': 'Motor Function',
        'description': 'Tasks assessing motor abilities and coordination',
        'parent': None,
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
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralcategoryapproval/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('behavioralcategoryapproval', id='c3d4e5f6-7890-12cd-ef01-3456789012cd')
```

### Response example
{: .no_toc}

```
{'behavioral_category_approval': {
    'id': 'c3d4e5f6-7890-12cd-ef01-3456789012cd',
    'name': 'Motor Function',
    'description': 'Tasks assessing motor abilities and coordination',
    'parent': None,
    'instance_id': None,
    'action': 'Add',
    'reviewer': None,
    'status': 'Pending'}
}
```


## Accept approval
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralcategoryapproval/<id\>/accept/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("behavioralcategoryapproval", id="c3d4e5f6-7890-12cd-ef01-3456789012cd", options="accept")
```


## Reject approval
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/behavioralcategoryapproval/<id\>/reject/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("behavioralcategoryapproval", id="d4e5f6a7-8901-23de-f012-4567890123de", options="reject")
```
