---
layout: default
title: Subject
parent: STEM
grand_parent: API
nav_order: 2
---

# Subject API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `name` | string **[required for POST; optional for PATCH]** [max length: 100; must be unique]|
| `description` | string |
| `projects` | list of related project IDs formatted as strings **[required; at least one]** |
| `licenses` | list of related license IDs formatted as strings |
| `strain` | strain ID formatted as a string **[required]** |
| `sex` | string with `"F"`, `"M"`, or `"U"` **[required for POST; optional for PATCH]** [max length: 1]|
| `genetic_line` | string [max length: 100]|
| `genotype` | string [max length: 200] |
| `subject_identifier` | string [max length: 100]|
| `supplier` | supplier ID formatted as a string |
| `breeding` | breeding ID formatted as a string |
| `birth_date` | string containing date (e.g. `"2023-03-22"`) |
| `death_date` | string containing date (e.g. `"2023-03-22"`) |
| `extra_fields` | JSON object of additional key/value metadata. *See structure below* |
| `procedures` | list of related procedures IDs formatted as strings **[read-only]** |
| `subjectlogs` | list of related subject log IDs formatted as strings **[read-only]** |
| `name_used_in_storage` | string [max length: 200]|
| `tags` | list of strings |


`extra_fields` is a JSON object where each key/value pair captures additional metadata for the subject. Keys must start with a letter and can only contain letters, numbers, and underscores. Values can be strings or numeric values.

```json
{
    "extra_property": "setting1",
    "another_property": 22
}
```


## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/subject
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('subject')
```

### Response example
{: .no_toc}

```json
{
    "subjects": [
        {
            "id": "00000000-0000-0000-0000-000000000000",
            "name": "subject1",
            "description": "",
            "projects": ["00000000-0000-0000-0000-000000000000"],
            "strain": "00000000-0000-0000-0000-000000000000",
            "sex": "M",
            "genetic_line": "",
            "subject_identifier": "",
            "supplier": null,
            "birth_date": "2023-03-22",
            "death_date": null,
            "extra_fields": {},
            "procedures": ["00000000-0000-0000-0000-000000000000"],
            "subjectlogs": [],
            "tags": [],
            "name_used_in_storage": null,
        },
        {
            "id": "00000000-0000-0000-0000-000000000000",
            "name": "subject2",
            "description": "",
            "projects": ["00000000-0000-0000-0000-000000000000"],
            "strain": "00000000-0000-0000-0000-000000000000",
            "sex": "M",
            "genetic_line": "",
            "subject_identifier": "",
            "supplier": null,
            "birth_date": null,
            "death_date": null,
            "extra_fields": {},
            "procedures": [
                "00000000-0000-0000-0000-000000000000",
                "00000000-0000-0000-0000-000000000000",
                "00000000-0000-0000-0000-000000000000",
                "00000000-0000-0000-0000-000000000000",
                "00000000-0000-0000-0000-000000000000",
                "00000000-0000-0000-0000-000000000000",
                "00000000-0000-0000-0000-000000000000",
                "00000000-0000-0000-0000-000000000000"
            ],
            "subjectlogs": ["00000000-0000-0000-0000-000000000000"],
            "tags": ["cooling"],
            "name_used_in_storage": "subject2_local",
        }
    ]
}
```


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/stem/subject
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model(
    "subject",
    data={
        "name": "NewSubject",
        "description": "some text",
        "strain": "00000000-0000-0000-0000-000000000000",
        "sex": "U",
        "projects": ["00000000-0000-0000-0000-000000000000"],
        "subject_identifier": "WF-123",
        "supplier": "00000000-0000-0000-0000-000000000000",
    },
)
```

### Response example
{: .no_toc}

```json
{
    "subject": {
        "id": "00000000-0000-0000-0000-000000000000",
        "name": "NewSubject",
        "description": "some text",
        "projects": ["00000000-0000-0000-0000-000000000000"],
        "strain": "00000000-0000-0000-0000-000000000000",
        "sex": "U",
        "genetic_line": "",
        "subject_identifier": "WF-123",
        "supplier": "00000000-0000-0000-0000-000000000000",
        "birth_date": null,
        "death_date": null,
        "extra_fields": null,
        "procedures": [],
        "subjectlogs": [],
        "tags": [],
        "name_used_in_storage": null,
    }
}
```


## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/subject/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('subject', id='00000000-0000-0000-0000-000000000000')
```

### Response example
{: .no_toc}

```json
{
    "subject": {
        "id": "00000000-0000-0000-0000-000000000000",
        "name": "NewSubject",
        "description": "some text",
        "projects": ["00000000-0000-0000-0000-000000000000"],
        "strain": "00000000-0000-0000-0000-000000000000",
        "sex": "U",
        "genetic_line": "",
        "subject_identifier": "WF-123",
        "supplier": "00000000-0000-0000-0000-000000000000",
        "birth_date": null,
        "death_date": null,
        "extra_fields": {
            "extra_property": "setting1",
            "another_property": 22
        },
        "procedures": [],
        "subjectlogs": [],
        "tags": [],
        "name_used_in_storage": null,
    }
}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/stem/subject/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model(
    "subject",
    id="00000000-0000-0000-0000-000000000000",
    data={"description": "new text"}
)
```

### Response example
{: .no_toc}

```json
{
    "subject": {
        "id": "00000000-0000-0000-0000-000000000000",
        "name": "NewSubject",
        "description": "new text",
        "projects": ["00000000-0000-0000-0000-000000000000"],
        "strain": "00000000-0000-0000-0000-000000000000",
        "sex": "U",
        "genetic_line": "",
        "subject_identifier": "WF-123",
        "supplier": "00000000-0000-0000-0000-000000000000",
        "birth_date": null,
        "death_date": null,
        "extra_fields": null,
        "procedures": [],
        "subjectlogs": [],
        "tags": [],
        "name_used_in_storage": null,
    }
}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/stem/subject/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("subject", id="00000000-0000-0000-0000-000000000000")
```
