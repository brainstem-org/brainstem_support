---
layout: default
title: License
parent: Personal attributes
grand_parent: API
nav_order: 5
---

# License API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}


## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `name` | string **[required]** [max length: 255] |
| `type` | string **[required]** [max length: 64]. Choices: `animal_research_authorization`, `human_research_authorization`, `biosafety_gmo_authorization`, `wildlife_fieldwork_permit`, `controlled_substance_license`, `chemical_use_authorization`, `import_export_permit` |
| `status` | string **[required]** [max length: 16; default: `draft`]. Choices: `draft`, `pending`, `active`, `suspended`, `expired`, `revoked` |
| `description` | rich text string |
| `country` | ISO 3166-1 alpha-2 country code string |
| `regulatory_authority` | UUID of a related [regulatory authority]({{"api/taxonomies/regulatoryauthority/"|absolute_url}}) |
| `license_number` | string [max length: 128] |
| `license_document` | file upload (PDF recommended) |
| `valid_from` | date string (YYYY-MM-DD) |
| `valid_until` | date string (YYYY-MM-DD); must be on or after `valid_from` when both dates are provided |
| `license_holders` | list of user UUIDs |
| `behavioralassays` | list of related behavioral assay UUIDs |
| `subjects` | list of related subject UUIDs |
| `procedures` | list of related procedure UUIDs |
| `is_public` | boolean |


## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/personal_attributes/license
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('license')
```

### Response example
{: .no_toc}

```
{'licenses': [
    {
        'id': 'a1b2c3d4-e5f6-7890-abcd-ef1234567890',
        'name': 'PPL: Septo-hippocampal dynamics 2025-2028',
        'type': 'animal_research_authorization',
        'status': 'active',
        'description': '',
        'country': 'GB',
        'regulatory_authority': 'b2c3d4e5-f6a7-8901-bcde-f12345678901',
        'license_number': 'PP1234567',
        'license_document': None,
        'valid_from': '2025-01-01',
        'valid_until': '2028-12-31',
        'license_holders': [],
        'is_public': False
    }
]}
```

Public list responses also include a `meta` object (pagination/filter metadata).


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/personal_attributes/license
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("license", data={
    'name': 'IACUC Protocol 2026-001',
    'type': 'animal_research_authorization',
    'status': 'active',
    'license_number': 'IACUC-2026-001',
    'valid_from': '2026-01-01',
    'valid_until': '2028-12-31',
    'is_public': False
})
```

### Response example
{: .no_toc}

```
{'license': {
    'id': 'c3d4e5f6-a7b8-9012-cdef-123456789012',
    'name': 'IACUC Protocol 2026-001',
    'type': 'animal_research_authorization',
    'status': 'active',
    'description': '',
    'country': None,
    'regulatory_authority': None,
    'license_number': 'IACUC-2026-001',
    'license_document': None,
    'valid_from': '2026-01-01',
    'valid_until': '2028-12-31',
    'license_holders': [],
    'is_public': False}
}
```


## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/personal_attributes/license/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('license', id='c3d4e5f6-a7b8-9012-cdef-123456789012')
```

### Response example
{: .no_toc}

```
{'license': {
    'id': 'c3d4e5f6-a7b8-9012-cdef-123456789012',
    'name': 'IACUC Protocol 2026-001',
    'type': 'animal_research_authorization',
    'status': 'active',
    'description': '',
    'country': None,
    'regulatory_authority': None,
    'license_number': 'IACUC-2026-001',
    'license_document': None,
    'valid_from': '2026-01-01',
    'valid_until': '2028-12-31',
    'license_holders': [],
    'is_public': False}
}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/personal_attributes/license/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("license", id="c3d4e5f6-a7b8-9012-cdef-123456789012", data={"status": "expired"})
```

### Response example
{: .no_toc}

```
{'license': {
    'id': 'c3d4e5f6-a7b8-9012-cdef-123456789012',
    'name': 'IACUC Protocol 2026-001',
    'type': 'animal_research_authorization',
    'status': 'expired',
    'description': '',
    'country': None,
    'regulatory_authority': None,
    'license_number': 'IACUC-2026-001',
    'license_document': None,
    'valid_from': '2026-01-01',
    'valid_until': '2028-12-31',
    'license_holders': [],
    'is_public': False}
}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/personal_attributes/license/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("license", id="c3d4e5f6-a7b8-9012-cdef-123456789012")
```
