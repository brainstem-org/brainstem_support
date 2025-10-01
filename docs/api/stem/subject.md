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
| `strain` | strain ID formatted as a string **[required]** |
| `sex` | string with `"F"`, `"M"`, or `"U"` **[required for POST; optional for PATCH]** [max length: 1]|
| `genetic_line` | string [max length: 100]|
| `subject_identifier` | string [max length: 100]|
| `supplier` | supplier ID formatted as a string |
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
- **Allowed portals:** public, private, super
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
            "id": "0cdaf69d-63cf-429f-b549-fc0cc163d046",
            "name": "subject1",
            "description": "",
            "projects": ["c4b8a90b-2963-4d13-aa07-b6f497252dde"],
            "strain": "deec9da3-ee26-4348-954e-484f62c463c8",
            "sex": "M",
            "genetic_line": "",
            "subject_identifier": "",
            "supplier": null,
            "birth_date": "2023-03-22",
            "death_date": null,
            "extra_fields": {},
            "procedures": ["9542eb95-90b3-40c6-9e35-9eef01b3334a"],
            "subjectlogs": [],
            "tags": [],
            "name_used_in_storage": null,
        },
        {
            "id": "0f87c229-6769-4854-83a5-c71e154246b8",
            "name": "subject2",
            "description": "",
            "projects": ["e7475834-7733-48cf-9e3b-f4f2d2d0305a"],
            "strain": "7d056b05-ff2c-4dda-96f5-e34fe4dc3ac4",
            "sex": "M",
            "genetic_line": "",
            "subject_identifier": "",
            "supplier": null,
            "birth_date": null,
            "death_date": null,
            "extra_fields": {},
            "procedures": [
                "f79d84c8-6bec-40e3-b18a-5b25e57f4a09",
                "a18dd2b1-6393-468c-9424-1bc77b9e4976",
                "087b71c4-6785-437c-b8ef-e35a82a8463e",
                "794fbe3b-3b11-4593-9a6a-96bad2ecf518",
                "655ed49b-c86f-42f8-aac0-1a2d56046fcf",
                "2ef9b54f-080e-46a9-a172-612cffe3a24a",
                "dedef2d7-00ae-4967-8e93-a9d65a20dfce",
                "9bb4f750-07fb-44f5-9f68-cc0e1bfbcc74"
            ],
            "subjectlogs": ["6612752a-76a9-429c-82d7-5f4cc0a13d1e"],
            "tags": ["cooling"],
            "name_used_in_storage": "subject2_local",
        }
    ]
}
```


## Add
- **Allowed portals:** private, super
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
        "strain": "deec9da3-ee26-4348-954e-484f62c463c8",
        "sex": "U",
        "projects": ["c4b8a90b-2963-4d13-aa07-b6f497252dde"],
        "subject_identifier": "WF-123",
        "supplier": "8a04d79a-0a90-41da-83dd-2c0e0be6b827",
    },
)
```

### Response example
{: .no_toc}

```json
{
    "subject": {
        "id": "b4ae1f92-5260-4605-8d21-25ac5c3fce91",
        "name": "NewSubject",
        "description": "some text",
        "projects": ["c4b8a90b-2963-4d13-aa07-b6f497252dde"],
        "strain": "deec9da3-ee26-4348-954e-484f62c463c8",
        "sex": "U",
        "genetic_line": "",
        "subject_identifier": "WF-123",
        "supplier": "8a04d79a-0a90-41da-83dd-2c0e0be6b827",
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
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/subject/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('subject', id='b4ae1f92-5260-4605-8d21-25ac5c3fce91')
```

### Response example
{: .no_toc}

```json
{
    "subject": {
        "id": "b4ae1f92-5260-4605-8d21-25ac5c3fce91",
        "name": "NewSubject",
        "description": "some text",
        "projects": ["c4b8a90b-2963-4d13-aa07-b6f497252dde"],
        "strain": "deec9da3-ee26-4348-954e-484f62c463c8",
        "sex": "U",
        "genetic_line": "",
        "subject_identifier": "WF-123",
        "supplier": "8a04d79a-0a90-41da-83dd-2c0e0be6b827",
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
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/stem/subject/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model(
    "subject",
    id="b4ae1f92-5260-4605-8d21-25ac5c3fce91",
    data={"description": "new text"}
)
```

### Response example
{: .no_toc}

```json
{
    "subject": {
        "id": "b4ae1f92-5260-4605-8d21-25ac5c3fce91",
        "name": "NewSubject",
        "description": "new text",
        "projects": ["c4b8a90b-2963-4d13-aa07-b6f497252dde"],
        "strain": "deec9da3-ee26-4348-954e-484f62c463c8",
        "sex": "U",
        "genetic_line": "",
        "subject_identifier": "WF-123",
        "supplier": "8a04d79a-0a90-41da-83dd-2c0e0be6b827",
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
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/stem/subject/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("subject", id="b4ae1f92-5260-4605-8d21-25ac5c3fce91")
```
