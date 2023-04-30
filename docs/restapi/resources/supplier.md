---
layout: default
title: Supplier
parent: Resources
grand_parent: REST API
nav_order: 6
---

# Supplier API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | string with UUID identificator |
| `name` | string **[required]** [max length: 100; must be unique] |
| `description` | string |
| `website` | string [max length: 200] |
| `comments` | string |


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/rest/private/resources/supplier
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'supplier')
```

### Response example
{: .no_toc}

```
{'suppliers': [
    {
        'id': 'a8fd144e-0207-4d47-917e-b89fd505ff06',
        'name': 'Thorlabs',
        'description': '',
        'website': 'https://www.thorlabs.com/'
    },
    {
        'id': '4fa1c3b4-f955-47f5-8524-3f1afa3fc657',
        'name': 'UNC Vector Core',
        'description': 'UNC Vector Core',
        'website': 'https://www.med.unc.edu/genetherapy/vectorcore/'
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** https://www.brainstem.org/rest/private/resources/supplier
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: suppliers submissions go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "supplier",  data={
    'name': 'MyNewSupplier',
    'description': '',
    'website': 'newsupplier.com'}
)
```

### Response example
{: .no_toc}

```
{'supplier_approval': {
    'id': '1af72008-d203-4bea-9766-f692b8a89df6',
    'name': 'MyNewSupplier',
    'description': '',
    'website': 'http://newsupplier.com',
    'comments': ''}
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/rest/private/resources/supplier/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'supplier', id='1338d838-5b69-4e89-8db9-b35224dcb01e')
```

### Response example
{: .no_toc}

```
{'supplier': {
    'id': '1338d838-5b69-4e89-8db9-b35224dcb01e',
  'name': 'MyNewSupplier',
  'description': '',
  'website': 'http://newsupplier.com'}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/rest/private/resources/supplier/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: suppliers changes go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "supplier", id="1338d838-5b69-4e89-8db9-b35224dcb01e", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'supplier_approval': {
    'id': 'e52eb599-a42f-4c37-9298-9bc4c9b42ff0',
    'name': 'MyNewSupplier',
    'description': 'new text',
    'website': 'http://newsupplier.com',
    'comments': ''}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/rest/private/resources/supplier/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

**Note**: only administrators can delete Suppliers.


### Use example (using Python API)
{: .no_toc}

```
resp = delete_model(settings, "supplier", id="1338d838-5b69-4e89-8db9-b35224dcb01e")
``` 


## List approvals
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/rest/private/resources/supplier_approvals
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'supplierapproval')
```

### Response example
{: .no_toc}

```
{'supplier_approvals': [
    {
        'id': '1af72008-d203-4bea-9766-f692b8a89df6',
        'name': 'MyNewSupplier',
        'description': '',
        'website': 'http://newsupplier.com',
        'comments': '',
        'instance_id': None,
        'action': 'Add',
        'reviewer': None,
        'status': 'Pending'
    },
    {
        'id': '5c73ffd2-6d37-4336-be1b-9c39815497e9',
        'name': 'NeuroNexus',
        'description': 'bbb',
        'website': '',
        'comments': 'Update description',
        'instance_id': 'f314f4b0-a51d-45f8-8cda-d9dade2bff66',
        'action': 'Change',
        'reviewer': 3,
        'status': 'Accepted'
    }
]}
```


## Detail approval
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/rest/private/resources/supplier_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = load_model(settings, 'supplierapproval', id='1af72008-d203-4bea-9766-f692b8a89df6')
```

### Response example
{: .no_toc}

```
{'supplier_approval': {
    'id': '1af72008-d203-4bea-9766-f692b8a89df6',
    'name': 'MyNewSupplier',
    'description': '',
    'website': 'http://newsupplier.com',
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
- **URL:** https://www.brainstem.org/rest/private/resources/supplier_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "supplierapproval", id="1af72008-d203-4bea-9766-f692b8a89df6", options="accept")
```


## Reject approval
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/rest/private/resources/supplier_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = save_model(settings, "supplierapproval", id="f314f4b0-a51d-45f8-8cda-d9dade2bff66", options="reject")
```