---
layout: default
title: Protocol
parent: Personal attributes
grand_parent: API
nav_order: 6
---

# Protocol API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Overview

The Protocol API manages reusable methods for procedures and subject logs. See the [Protocol model]({{"datamodel/personal_attributes/protocol/"|absolute_url}}) for the web workflow, relationships, and permissions.

| Operation | Method | URL |
|:----------|:-------|:----|
| List | GET | `https://www.brainstem.org/api/private/personal_attributes/protocol/` |
| Create | POST | `https://www.brainstem.org/api/private/personal_attributes/protocol/` |
| Detail | GET | `https://www.brainstem.org/api/private/personal_attributes/protocol/<id>/` |
| Partial update | PATCH | `https://www.brainstem.org/api/private/personal_attributes/protocol/<id>/` |
| Full update | PUT | `https://www.brainstem.org/api/private/personal_attributes/protocol/<id>/` |
| Delete | DELETE | `https://www.brainstem.org/api/private/personal_attributes/protocol/<id>/` |

Replace `private` with `public` for unauthenticated, read-only access to protocols with `is_public: true`. Private requests require [API authentication]({{"api/"|absolute_url}}). Reading private protocols requires read permission; editing protocol details and deleting protocols require ownership. The creator receives owner permissions, and the groups selected on creation receive contributor permissions.

Successful reads and updates return `200`, creation returns `201`, and deletion returns `204`. Invalid fields return `400`; access failures can return `403` or `404`.

## Fields

| Field | Description |
|:------|:------------|
| `id` | Protocol UUID, formatted as a string (read-only). |
| `name` | String **[required]**, maximum length 255. |
| `protocol_type` | String **[required]**: `procedure` or `subject_log`. |
| `subtypes` | Optional list of subtype codes. An empty list allows all subtypes within the selected protocol type. |
| `subtype_display` | List of human-readable subtype labels (read-only). |
| `description` | Optional rich text string. |
| `url` | Optional URL, maximum length 200. |
| `licenses` | List of related [license]({{"api/personal_attributes/license/"|absolute_url}}) UUIDs. Adding a license requires `change_license` permission on it. |
| `attachment` | Optional file upload; responses contain a signed download URL, or `null` when absent. |
| `authgroups` | List of group IDs for initial contributor access. Select groups you belong to; manage subsequent access through the protocol's Manage tab. |
| `is_public` | Boolean, default `false`. Owners can change public access. |
| `procedures` | Related procedure UUIDs. Link records using the procedure endpoint's `protocol` field. |
| `subjectlogs` | Related subject-log UUIDs. Link records using the subject-log endpoint's `protocol` field. |

Public responses omit `authgroups`, `procedures`, and `subjectlogs`. List responses use the `protocols` key; detail, create, and update responses use `protocol`.

### Subtype validation

Subtype codes are case-sensitive and must belong to the selected protocol type:

- For `procedure`, use [procedure type codes]({{"api/schemas/procedure/"|absolute_url}}), such as `Anesthesia` or `Craniotomy`.
- For `subject_log`, use [subject-log type codes]({{"api/schemas/subjectlog/"|absolute_url}}), such as `Handling` or `Weighing`.

For example, `{"protocol_type": "subject_log", "subtypes": ["Handling"]}` is valid; `Craniotomy` is not a valid subject-log subtype. When changing `protocol_type`, also supply compatible `subtypes` or an empty list.

## Examples using Python requests

These examples use the REST API directly. Replace the token and record IDs with your own values.

### Create

```python
import requests

base_url = "https://www.brainstem.org/api/private/personal_attributes/protocol/"
headers = {"Authorization": "Bearer YOUR_PERSONAL_TOKEN"}

response = requests.post(
    base_url,
    headers=headers,
    json={
        "name": "Handling SOP v2",
        "protocol_type": "subject_log",
        "subtypes": ["Handling"],
        "description": "Standard handling and acclimatization method.",
        "authgroups": [],
        "is_public": False,
    },
)
response.raise_for_status()
protocol_id = response.json()["protocol"]["id"]
detail_url = f"{base_url}{protocol_id}/"
```

An empty `authgroups` list creates a protocol owned by the creator without granting group access. To share on creation, supply IDs of groups you belong to.

### List and detail

```python
response = requests.get(base_url, headers=headers)
response.raise_for_status()
protocols = response.json()["protocols"]

response = requests.get(detail_url, headers=headers)
response.raise_for_status()
protocol = response.json()["protocol"]
```

### Update

```python
response = requests.patch(
    detail_url,
    headers=headers,
    json={"description": "Revised handling method.", "subtypes": []},
)
response.raise_for_status()
```

Omitted fields are preserved by `PATCH`. An explicit `subtypes: []` removes subtype restrictions; `licenses: []` removes license links. Use `PATCH` when changing only selected fields.

### Upload or remove an attachment

Use multipart form data for file uploads. Accepted formats are PDF, DOCX, XLSX, PPTX, ODT, CSV, Markdown (`.md`), and plain text (`.txt`), up to 15 MB. Supply the file itself rather than a local path or URL in JSON.

```python
with open("handling-sop.pdf", "rb") as attachment:
    response = requests.patch(
        detail_url,
        headers=headers,
        files={"attachment": ("handling-sop.pdf", attachment, "application/pdf")},
    )
response.raise_for_status()
```

Let `requests` set the multipart content type. To remove an attachment, send `{"attachment": null}` in a JSON `PATCH` request (`None` in Python). Signed download URLs can expire; fetch the protocol again to obtain a current URL.

### Link a subject log to the protocol

```python
response = requests.post(
    "https://www.brainstem.org/api/private/modules/subjectlog/",
    headers=headers,
    json={
        "type": "Handling",
        "subject": "<subject-id>",
        "protocol": protocol_id,
        "description": "Daily handling sessions",
    },
)
response.raise_for_status()
```

The protocol must be readable by you or public, have the correct protocol type, and allow the record's subtype. Creating or editing the linked record also requires the appropriate project permissions. [Procedures]({{"api/modules/procedure/"|absolute_url}}) similarly accept an optional `protocol` UUID for a `procedure` protocol. The subject-log link belongs to the log as a whole, not an individual log entry.

### Delete

Send `DELETE` to the detail URL as an owner. A protocol cannot be deleted while a procedure, subject log, procedure episode, or their templates reference it. Remove or reassign those references first.

```python
response = requests.delete(detail_url, headers=headers)
response.raise_for_status()
```
