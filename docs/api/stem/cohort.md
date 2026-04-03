---
layout: default
title: Cohort
parent: STEM
grand_parent: API
nav_order: 4
---

# Cohort API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `name` | string **[required]** [max length: 100]|
| `description` | string |
| `project` | related project ID formatted as a string **[required]** |
| `subjects` | list of related subjects IDs formatted as strings |
| `tags` | list of strings |

## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/cohort
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('cohort')
```

### Response example
{: .no_toc}

```
{'cohorts': [
        {
            'id': '<id>',
            'name': 'newcohort1',
            'project': '<project-id>',
            'subjects': [
                            '<id>',
                            '<id>'
                        ]
        },
        {
            'id': '<id>',
            'name': 'cohort2',
            'project': '<project-id>',
            'subjects': [
                            '<id>',
                            '<id>'
                        ]
        }
    ]
}
```

Public list responses also include a `meta` object (pagination/filter metadata).


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/stem/cohort
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Additional notes:** every subject in `subjects` must already belong to the same `project` as the cohort.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("cohort", data={"name": "NewRestCohort", "project": "<project-id>", "subjects": ["<id>"]})
```

### Response example
{: .no_toc}

```
{'cohort': {
    'id': '<id>',
    'name': 'NewRestCohort',
    'project': '<project-id>',
    'subjects': ['<id>']
    }
}
```



## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/cohort/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('cohort', id='<id>')
```

### Response example
{: .no_toc}

```
{'cohort': {
    'id': '<id>',
    'name': 'NewRestCohort',
    'project': '<project-id>',
    'subjects': ['<id>']
    }
}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/stem/cohort/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save("cohort", id="<id>", data={"name": "new name"})
```

### Response example
{: .no_toc}

```
{'cohort': {
    'id': '<id>',
    'name': 'new name',
    'project': '<project-id>',
    'subjects': ['<id>']
    }
}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/stem/cohort/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete("cohort", id="<id>")
```
