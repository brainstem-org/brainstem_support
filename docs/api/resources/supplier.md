---
layout: default
title: Supplier
parent: Resources
grand_parent: API
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
| `id` | UUID identificator formatted as a string |
| `name` | string **[required]** [max length: 100; must be unique] |
| `description` | string |
| `website` | string [max length: 200] |
| `comments` | string, used when proposing approval changes |

Optional fields such as `comments` can be omitted from list/detail responses when empty.



## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/resources/supplier
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('supplier')
```

### Response example
{: .no_toc}

```
{'suppliers': [
    {
        'id': '<id>',
        'name': 'Thorlabs',
        'description': '',
        'website': 'https://www.thorlabs.com/'
    },
    {
        'id': '<id>',
        'name': 'UNC Vector Core',
        'description': 'UNC Vector Core',
        'website': 'https://www.med.unc.edu/genetherapy/vectorcore/'
    }
]}
```

Public list responses also include a `meta` object (pagination/filter metadata).


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/resources/supplier
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: suppliers submissions go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("supplier",  data={
    'name': 'MyNewSupplier',
    'description': '',
    'website': 'newsupplier.com'}
)
```

### Response example
{: .no_toc}

```
{'supplier_approval': {
    'id': '<id>',
    'name': 'MyNewSupplier',
    'description': '',
    'website': 'http://newsupplier.com'}
}
```



## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/resources/supplier/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('supplier', id='<id>')
```

### Response example
{: .no_toc}

```
{'supplier': {
    'id': '<id>',
  'name': 'MyNewSupplier',
  'description': '',
  'website': 'http://newsupplier.com'}
}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/resources/supplier/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: suppliers changes go through an approval process.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("supplier", id="<id>", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'supplier_approval': {
    'id': '<id>',
    'name': 'MyNewSupplier',
    'description': 'new text',
    'website': 'http://newsupplier.com'}
}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/resources/supplier/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

**Note**: only administrators can delete Suppliers.


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete("supplier", id="<id>")
``` 


## List approvals
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/resources/supplierapproval
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('supplierapproval')
```

### Response example
{: .no_toc}

```
{'supplier_approvals': [
    {
        'id': '<id>',
        'name': 'MyNewSupplier',
        'description': '',
        'website': 'http://newsupplier.com',
        'instance_id': None,
        'action': 'Add',
        'reviewer': None,
        'status': 'Pending'
    },
    {
        'id': '<id>',
        'name': 'NeuroNexus',
        'description': 'bbb',
        'website': '',
        'instance_id': '<instance_id-id>',
        'action': 'Change',
        'reviewer': 3,
        'status': 'Accepted'
    }
]}
```

Approval list responses also include a `meta` object (pagination/filter metadata).


## Detail approval
- **Allowed portals:** private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/resources/supplierapproval/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('supplierapproval', id='<id>')
```

### Response example
{: .no_toc}

```
{'supplier_approval': {
    'id': '<id>',
    'name': 'MyNewSupplier',
    'description': '',
    'website': 'http://newsupplier.com',
    'instance_id': None,
    'action': 'Add',
    'reviewer': None,
    'status': 'Pending'}
}
```


## Accept approval
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/resources/supplierapproval/<id\>/accept/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("supplierapproval", id="<id>", options="accept")
```


## Reject approval
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/resources/supplierapproval/<id\>/reject/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("supplierapproval", id="<id>", options="reject")
```
