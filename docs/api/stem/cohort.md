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
resp = client.load_model('cohort')
```

### Response example
{: .no_toc}

```
{'cohorts': [
        {
            'id': '00000000-0000-0000-0000-000000000000',
            'name': 'newcohort1',
            'project': '00000000-0000-0000-0000-000000000000',
            'subjects': [
                            '00000000-0000-0000-0000-000000000000',
                            '00000000-0000-0000-0000-000000000000'
                        ]
        },
        {
            'id': '00000000-0000-0000-0000-000000000000',
            'name': 'cohort2',
            'project': '00000000-0000-0000-0000-000000000000',
            'subjects': [
                            '00000000-0000-0000-0000-000000000000',
                            '00000000-0000-0000-0000-000000000000'
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
resp = client.save_model("cohort", data={"name": "NewRestCohort", "project": "00000000-0000-0000-0000-000000000000", "subjects": ["00000000-0000-0000-0000-000000000000"]})
```

### Response example
{: .no_toc}

```
{'cohort': {
    'id': '00000000-0000-0000-0000-000000000000',
    'name': 'NewRestCohort',
    'project': '00000000-0000-0000-0000-000000000000',
    'subjects': ['00000000-0000-0000-0000-000000000000']
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
resp = client.load_model('cohort', id='00000000-0000-0000-0000-000000000000')
```

### Response example
{: .no_toc}

```
{'cohort': {
    'id': '00000000-0000-0000-0000-000000000000',
    'name': 'NewRestCohort',
    'project': '00000000-0000-0000-0000-000000000000',
    'subjects': ['00000000-0000-0000-0000-000000000000']
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
resp = client.save_model("cohort", id="00000000-0000-0000-0000-000000000000", data={"name": "new name"})
```

### Response example
{: .no_toc}

```
{'cohort': {
    'id': '00000000-0000-0000-0000-000000000000',
    'name': 'new name',
    'project': '00000000-0000-0000-0000-000000000000',
    'subjects': ['00000000-0000-0000-0000-000000000000']
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
resp = client.delete_model("cohort", id="00000000-0000-0000-0000-000000000000")
```
