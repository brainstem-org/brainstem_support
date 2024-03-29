---
layout: default
title: Strain
parent: Taxonomies
grand_parent: API
nav_order: 7
---

# Strain API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `name` | string **[required]** [max length: 100; must be unique] |
| `description` | string [max length: 500] |
| `species` | related species ID formatted as a string **[required]** |
| `comments` | string |


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/strain
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('strain')
```

### Response example
{: .no_toc}

```
{'strains': [
    {
        'id': 'd7e490ec-66ef-447e-ae9f-3f74c858258e',
        'name': 'Brown Norway',
        'description': '',
        'species': '089b00eb-94e3-464b-b7e8-62d04ddf2b11'
    },
    {
        'id': '378bc660-f35a-48a7-b06d-89ece1e4ba40',
        'name': 'Red-eared slider',
        'description': '',
        'species': '93dd9502-305a-4e7b-b66b-42cf8c79368f'
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/taxonomies/strain
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: Strains submissions go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("strain", data={
        "name": "MyNewStrain",
        "description": "",
        "species": "93dd9502-305a-4e7b-b66b-42cf8c79368f",
    }
)
```

### Response example
{: .no_toc}

```
{'strain_approval': {
    'id': 'b460dfbc-79bb-499e-87ed-57df02832d88',
    'name': 'MyNewStrain',
    'description': '',
    'species': '93dd9502-305a-4e7b-b66b-42cf8c79368f',
    'comments': ''}
}
```

## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/strain/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('strain', id='7963dc0b-e4e7-459c-9a05-cf5a54200e02')
```

### Response example
{: .no_toc}

```
{'strain': {
    'id': '7963dc0b-e4e7-459c-9a05-cf5a54200e02',
    'name': 'MyNewStrain',
    'description': '',
    'species': '93dd9502-305a-4e7b-b66b-42cf8c79368f'}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/strain/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: Strains changes go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("strain", id="7963dc0b-e4e7-459c-9a05-cf5a54200e02", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'strain_approval': {
    'id': '6403fdaf-7896-4ef7-9b30-ee12d69aa408',
    'name': 'MyNewStrain',
    'description': 'new text',
    'species': '93dd9502-305a-4e7b-b66b-42cf8c79368f',
    'comments': ''}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/taxonomies/strain/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

**Note**: only administrators can delete Strains.

### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("strain", id="7963dc0b-e4e7-459c-9a05-cf5a54200e02")
``` 


## List approvals
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/strain_approvals
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('strainapproval')
```

### Response example
{: .no_toc}

```
{'strain_approvals': [
    {
        'id': 'b460dfbc-79bb-499e-87ed-57df02832d88',
        'name': 'MyNewStrain',
        'description': '',
        'species': '93dd9502-305a-4e7b-b66b-42cf8c79368f',
        'comments': '',
        'instance_id': None,
        'action': 'Add',
        'reviewer': None,
        'status': 'Pending'
    },
    {
        'id': '535e2f20-5571-4acd-83ef-edc4c076bbb4',
        'name': 'Agumon',
        'description': '',
        'species': '7a224fef-df3f-4b4e-aa52-7ae743b7bf58',
        'comments': '',
        'instance_id': None,
        'action': 'Add',
        'reviewer': 3,
        'status': 'Rejected'
    }
]}
```


## Detail approval
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/strain_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('strainapproval', id='b460dfbc-79bb-499e-87ed-57df02832d88')
```

### Response example
{: .no_toc}

```
{'strain_approval': {
    'id': 'b460dfbc-79bb-499e-87ed-57df02832d88',
    'name': 'MyNewStrain',
    'description': '',
    'species': '93dd9502-305a-4e7b-b66b-42cf8c79368f',
    'comments': '',
    'instance_id': None,
    'action': 'Add',
    'reviewer': None,
    'status': 'Pending'}
}
```


## Accept approval
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/strain_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("strainapproval", id="b460dfbc-79bb-499e-87ed-57df02832d88", options="accept")
```


## Reject approval
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/strain_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("strainapproval", id="6403fdaf-7896-4ef7-9b30-ee12d69aa408", options="reject")
```