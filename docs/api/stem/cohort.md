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
| `name` | string **[required]** [max length: 200]|
| `description` | string |
| `project` | related project ID formatted as a string **[required]** |
| `subjects` | list of related subjects IDs formatted as strings **[required]** |
| `tags` | list of strings |

## List view
- **Allowed portals:** public, private, super
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
            'id': '8df1fb4e-5fb7-41f1-9494-06c813c5d9f7',
            'name': 'newcohort1',
            'project': 'e7475834-7733-48cf-9e3b-f4f2d2d0305a',
            'subjects': [
                            '1a827c68-19b4-4cec-8ae5-e13c8f1de900',
                            'ef7ae22f-143a-4a5e-adf6-1c623531dd63'
                        ]
        },
        {
            'id': 'd00de634-3078-442a-bb24-5f4dbbd62983',
            'name': 'cohort2',
            'project': 'c4b8a90b-2963-4d13-aa07-b6f497252dde',
            'subjects': [
                            'd8e72f9d-eb25-4280-a241-3317d5914055',
                            '3865d613-a9a4-419b-80de-ae07cc754a2a'
                        ]
        }
    ]
}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/stem/cohort
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Additional notes:** when a user creates a project they become its owner and only member. Any other user or group will not be added at this point. Perform a change request to add more users or groups.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("cohort", data={"name": "NewRestCohort", "project": "e7475834-7733-48cf-9e3b-f4f2d2d0305a", "subjects": ["1a827c68-19b4-4cec-8ae5-e13c8f1de900"]})
```

### Response example
{: .no_toc}

```
{'cohort': {
    'id': '54d5bab2-e520-4f1a-b518-6f66d28ee7ee',
    'name': 'NewRestCohort',
    'project': 'e7475834-7733-48cf-9e3b-f4f2d2d0305a',
    'subjects': ['1a827c68-19b4-4cec-8ae5-e13c8f1de900'],
    'links': {'subjects': 'subjects/'}
    }
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/cohort/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('cohort', id='54d5bab2-e520-4f1a-b518-6f66d28ee7ee')
```

### Response example
{: .no_toc}

```
{'cohort': {
    'id': '54d5bab2-e520-4f1a-b518-6f66d28ee7ee',
    'name': 'NewRestCohort',
    'project': 'e7475834-7733-48cf-9e3b-f4f2d2d0305a',
    'subjects': ['1a827c68-19b4-4cec-8ae5-e13c8f1de900'],
    'links': {'subjects': 'subjects/'}
    }
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/stem/cohort/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("cohort", id="54d5bab2-e520-4f1a-b518-6f66d28ee7ee", data={"name": "new name"})
```

### Response example
{: .no_toc}

```
{'cohort': {
    'id': '54d5bab2-e520-4f1a-b518-6f66d28ee7ee',
    'name': 'new name',
    'project': 'e7475834-7733-48cf-9e3b-f4f2d2d0305a',
    'subjects': ['1a827c68-19b4-4cec-8ae5-e13c8f1de900'],
    'links': {'subjects': 'subjects/'}
    }
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/stem/cohort/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("cohort", id="54d5bab2-e520-4f1a-b518-6f66d28ee7ee")
```
