---
layout: default
title: Breeding
parent: STEM
grand_parent: API
nav_order: 7
---

# Breeding API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field | Description |
|:------|:------------|
| `id` | UUID identificator formatted as a string |
| `name` | string **[required]** [max length: 100] |
| `project` | related project ID formatted as a string **[required]** |
| `mother` | related maternal subject ID formatted as a string **[required]** |
| `father` | related paternal subject ID formatted as a string **[required]** |
| `description` | string |
| `tags` | list of strings |
| `birth_date` | date (YYYY-MM-DD) |
| `start_date` | date (YYYY-MM-DD) |
| `end_date` | date (YYYY-MM-DD) |
| `weaning_date` | date (YYYY-MM-DD) |
| `litter_size` | positive integer |
| `expected_genotype` | string [max length: 100] |

## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/breeding
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('breeding')
```

### Response example
{: .no_toc}

```
{'breedings': [
        {
            'id': '<id>',
            'name': 'B6J x PV-Cre Spring 2026',
            'project': '<project-id>',
            'mother': '<mother-id>',
            'father': '<father-id>'
        }
    ]
}
```

Public list responses also include a `meta` object (pagination/filter metadata).


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/stem/breeding
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Additional notes:** both `mother` and `father` must already belong to the same `project` as the breeding.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("breeding", data={
    "name": "NewBreeding",
    "project": "<project-id>",
    "mother": "<mother-id>",
    "father": "<father-id>"
})
```

### Response example
{: .no_toc}

```
{'breeding': {
    'id': '<id>',
    'name': 'NewBreeding',
    'project': '<project-id>',
    'mother': '<mother-id>',
    'father': '<father-id>'
    }
}
```


## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/breeding/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('breeding', id='<id>')
```

### Response example
{: .no_toc}

```
{'breeding': {
    'id': '<id>',
    'name': 'NewBreeding',
    'project': '<project-id>',
    'mother': '<mother-id>',
    'father': '<father-id>',
    'description': '',
    'tags': [],
    'birth_date': null,
    'start_date': null,
    'end_date': null,
    'weaning_date': null,
    'litter_size': null,
    'expected_genotype': ''
    }
}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/stem/breeding/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("breeding", id="<id>", data={"name": "new name"})
```

### Response example
{: .no_toc}

```
{'breeding': {
    'id': '<id>',
    'name': 'new name',
    'project': '<project-id>',
    'mother': '<mother-id>',
    'father': '<father-id>'
    }
}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/stem/breeding/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.delete("breeding", id="<id>")
```
