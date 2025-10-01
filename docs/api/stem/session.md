---
layout: default
title: Session
parent: STEM
grand_parent: API
nav_order: 3
---

# Session API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `name` | string **[required]** [max length: 100; must be unique]|
| `description` | string |
| `projects` | list of related project IDs formatted as strings **[required; at least one]** |
| `date_time` | ISO 8601 date-time string (e.g. `"2023-03-22T15:30:00Z"`) |
| `epochs` | list of related epoch IDs formatted as strings **[read-only]** |
| `datastorage` | list of related data storage IDs formatted as strings *(create/update accepts a list; use the Session → Data Storage endpoint to manage ordering)* |
| `extra_fields` | JSON object of additional key/value metadata. *See structure below* |
| `download_links` | list of JSON objects with `repository` and `url` keys. *See structure below* |
| `dataacquisition` | list of related data acquisition IDs formatted as strings **[read-only]** |
| `behaviors` | list of related behaviors IDs formatted as strings **[read-only]** |
| `manipulations` | list of related manipulations IDs formatted as strings **[read-only]** |
| `name_used_in_storage` | string **[read-only]** [max length: 200]|
| `tags` | list of strings |


Use the Session → Data Storage endpoint (`/api/private/stem/sessiondatastorage/`) to add, remove, or reorder data storage associations. Session responses return `datastorage` IDs in the through-table order saved via this endpoint. You can include a `datastorage` list in Session POST/PATCH payloads (with the required permissions); use the dedicated endpoint when you need to control ordering explicitly.

`name_used_in_storage` is returned for display purposes but is not writable through the Session API.


`extra_fields` is a JSON object where each key/value pair captures additional metadata. Keys must start with a letter and can only contain letters, numbers, and underscores. Values can be strings or numeric values.

```json
{
    "extra_property": "setting1",
    "another_property": 22
}
```

`download_links` is a list of JSON objects with two elements, `repository` and `url`, like the following example:

```json
[
    {"repository": "DANDI", "url": "https://dandiarchive.org/dandiset/123456?pos=1"},
    {"repository": "GitHub", "url": "https://github.com/my_user/my_code"}
]
```

- Allowed repository values: `CRCNS`, `DANDI`, `Figshare`, `GitHub`, `Globus`, `Mendeley`, `Zenodo`, `Webshare`, or `Other`.
- Each `url` must already include a supported scheme (`http://`, `https://`, or `ftp://`). Requests missing a scheme are rejected.



## List view

- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** <https://www.brainstem.org/api/private/stem/session>
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Example request (list, Python API)

```python
resp = client.load_model("session")
```

### Example response (list)

```json
{
    "sessions": [
        {
            "id": "1a827c68-19b4-4cec-8ae5-e13c8f1de900",
            "name": "session1",
            "description": "",
            "epochs": [],
            "projects": ["c4b8a90b-2963-4d13-aa07-b6f497252dde"],
            "date_time": null,
            "datastorage": [],
            "extra_fields": {},
            "download_links": [],
            "dataacquisition": [],
            "behaviors": [],
            "manipulations": ["20387176-5f3c-433a-8bf9-34a0f2c431f7"],
            "tags": [],
        },
        {
            "id": "d8e72f9d-eb25-4280-a241-3317d5914055",
            "name": "session2",
            "description": "",
            "epochs": [],
            "projects": ["c4b8a90b-2963-4d13-aa07-b6f497252dde"],
            "date_time": null,
            "datastorage": [],
            "extra_fields": {},
            "download_links": [],
            "dataacquisition": ["1c77ae53-6f83-4398-bfe5-6eb95ff00610"],
            "behaviors": [],
            "manipulations": [],
            "tags": [],
        }
    ]
}
```

## Add

- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** <https://www.brainstem.org/api/private/stem/session>
- **Data:** JSON dictionary containing at least the required fields. Callers must have `change_project` permission for each project and `change_datastorage` for each data storage referenced.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Example request (create, Python API)

```python
resp = client.save_model(
    "session",
    data={
        "name": "NewSession",
        "description": "some text",
        "projects": ["c4b8a90b-2963-4d13-aa07-b6f497252dde"],
    },
)
```

### Example response (create)

```json
{
    "session": {
        "id": "13bdd793-86d4-428e-9708-167bbc26f6d2",
        "name": "NewSession",
        "description": "some text",
        "epochs": [],
        "projects": ["c4b8a90b-2963-4d13-aa07-b6f497252dde"],
        "date_time": null,
        "datastorage": [],
        "extra_fields": {},
        "download_links": [],
        "dataacquisition": [],
        "behaviors": [],
        "manipulations": [],
        "tags": [],
    }
}
```

## Detail

- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** `https://www.brainstem.org/api/private/stem/session/<id>/`
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Example request (detail, Python API)

```python
resp = client.load_model("session", id="13bdd793-86d4-428e-9708-167bbc26f6d2")
```

### Example response (detail)

```json
{
    "session": {
        "id": "13bdd793-86d4-428e-9708-167bbc26f6d2",
        "name": "NewSession",
        "description": "some text",
        "epochs": [],
        "projects": ["c4b8a90b-2963-4d13-aa07-b6f497252dde"],
        "date_time": null,
        "datastorage": [],
        "extra_fields": {
            "extra_property": "setting1",
            "another_property": 22
        },
        "download_links": [
            {"repository": "DANDI", "url": "https://dandiarchive.org/dandiset/123456?pos=1"},
            {"repository": "GitHub", "url": "https://github.com/my_user/my_code"}
        ],
        "dataacquisition": [],
        "behaviors": [],
        "manipulations": [],
        "tags": [],
    }
}
```

## Change

- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** `https://www.brainstem.org/api/private/stem/session/<id>/`
- **Data:** dictionary containing the fields to be updated. Callers must have `change_project` permission for each project and `change_datastorage` for each data storage referenced.
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Example request (update, Python API)

```python
resp = client.save_model(
    "session",
    id="13bdd793-86d4-428e-9708-167bbc26f6d2",
    data={"description": "new text"},
)
```

### Example response (update)

```json
{
    "session": {
        "id": "13bdd793-86d4-428e-9708-167bbc26f6d2",
        "name": "NewSession",
        "description": "new text",
        "epochs": [],
        "projects": ["c4b8a90b-2963-4d13-aa07-b6f497252dde"],
        "date_time": null,
        "datastorage": [],
        "extra_fields": {},
        "download_links": [],
        "dataacquisition": [],
        "behaviors": [],
        "manipulations": [],
        "tags": [],
    }
}
```

## Delete

- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** `https://www.brainstem.org/api/private/stem/session/<id>/`
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

### Example request (delete, Python API)

```python
resp = client.delete_model("session", id="13bdd793-86d4-428e-9708-167bbc26f6d2")
```
