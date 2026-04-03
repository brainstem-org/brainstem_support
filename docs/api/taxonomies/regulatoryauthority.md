---
layout: default
title: Regulatory authorities
parent: Taxonomies
grand_parent: API
nav_order: 8
---

# Regulatory authority API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}


## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `name` | string **[required]** [max length: 255; must be unique] |
| `abbreviation` | string [max length: 32] |
| `country` | ISO 3166-1 alpha-2 country code string |
| `authority_type` | string [max length: 64]. Choices: `national`, `institutional`, `regional`, `international` |
| `website` | URL string [max length: 200] |
| `description` | string |
| `is_active` | boolean [default: True]; indicates whether the authority is currently operational |

Optional fields such as `abbreviation` and `comments` can be omitted from list/detail responses when empty.


## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/regulatoryauthority
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('regulatoryauthority')
```

### Response example
{: .no_toc}

```
{'regulatoryauthorities': [
    {
        'id': '<id>',
        'name': 'Institutional Animal Care and Use Committee',
        'abbreviation': 'IACUC',
        'country': 'US',
        'authority_type': 'institutional',
        'website': 'https://www.example.edu/iacuc',
        'description': 'Institutional committee overseeing animal research compliance.',
        'is_active': True
    },
    {
        'id': '<id>',
        'name': 'Home Office',
        'abbreviation': 'HO',
        'country': 'GB',
        'authority_type': 'national',
        'website': 'https://www.gov.uk/government/organisations/home-office',
        'description': 'UK national authority issuing project and personal licences for animal research.',
        'is_active': True
    }
]}
```

Public list responses also include a `meta` object (pagination/filter metadata).


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/taxonomies/regulatoryauthority
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: Regulatory authority submissions go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("regulatoryauthority", data={
    "name": "Animal Ethics Committee",
    "abbreviation": "AEC",
    "country": "AU",
    "authority_type": "institutional",
    "description": "Institutional committee approving animal research protocols."
})
```

### Response example
{: .no_toc}

```
{'regulatoryauthority_approval': {
    'id': '<id>',
    'name': 'Animal Ethics Committee',
    'abbreviation': 'AEC',
    'country': 'AU',
    'authority_type': 'institutional',
    'website': '',
    'description': 'Institutional committee approving animal research protocols.',
    'is_active': True,
    'instance_id': None,
    'action': 'Add',
    'reviewer': None,
    'status': 'Pending'}
}
```


## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/regulatoryauthority/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('regulatoryauthority', id='<id>')
```

### Response example
{: .no_toc}

```
{'regulatoryauthority': {
    'id': '<id>',
    'name': 'Institutional Animal Care and Use Committee',
    'abbreviation': 'IACUC',
    'country': 'US',
    'authority_type': 'institutional',
    'website': 'https://www.example.edu/iacuc',
    'description': '',
    'is_active': True}
}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/regulatoryauthority/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: Regulatory authority changes go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("regulatoryauthority", id="<id>", data={"description": "Updated description."})
```

### Response example
{: .no_toc}

```
{'regulatoryauthority_approval': {
    'id': '<id>',
    'name': 'Institutional Animal Care and Use Committee',
    'abbreviation': 'IACUC',
    'country': 'US',
    'authority_type': 'institutional',
    'website': '',
    'description': 'Updated description.',
    'is_active': True,
    'instance_id': '<instance_id-id>',
    'action': 'Change',
    'reviewer': None,
    'status': 'Pending'}
}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/taxonomies/regulatoryauthority/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

**Note**: Only administrators can delete regulatory authorities.

### Use example (using Python API)
{: .no_toc}

```
resp = client.delete("regulatoryauthority", id="<id>")
```


## List approvals
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/regulatoryauthorityapproval
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('regulatoryauthorityapproval')
```

### Response example
{: .no_toc}

```
{'regulatoryauthority_approvals': [
    {
        'id': '<id>',
        'name': 'Animal Ethics Committee',
        'abbreviation': 'AEC',
        'country': 'AU',
        'authority_type': 'institutional',
        'website': '',
        'description': '',
        'is_active': True,
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
- **URL:** https://www.brainstem.org/api/private/taxonomies/regulatoryauthorityapproval/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('regulatoryauthorityapproval', id='<id>')
```

### Response example
{: .no_toc}

```
{'regulatoryauthority_approval': {
    'id': '<id>',
    'name': 'Animal Ethics Committee',
    'abbreviation': 'AEC',
    'country': 'AU',
    'authority_type': 'institutional',
    'website': '',
    'description': '',
    'is_active': True,
    'instance_id': None,
    'action': 'Add',
    'reviewer': None,
    'status': 'Pending'}
}
```


## Accept approval
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/regulatoryauthorityapproval/<id\>/accept/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("regulatoryauthorityapproval", id="<id>", options="accept")
```


## Reject approval
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/regulatoryauthorityapproval/<id\>/reject/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("regulatoryauthorityapproval", id="<id>", options="reject")
```
