---
layout: default
title: Inventory
parent: Personal attributes
grand_parent: API
nav_order: 5
---

# Inventory API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}


## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `name` | string **[required]** [max length: 50] |
| `description` | string [max length: 500]|
| `is_public` | boolean |


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/personal_attributes/inventory
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('inventory')
```

### Response example
{: .no_toc}

```
{'inventories': [
    {
        'id': '58e0003d-16c2-4264-913d-288463c0356d',
        'name': 'My probe inventory',
        'description': '',
        'is_public': False
    },
    {
        'id': '3e9ec0e0-d685-42ec-8386-0fa24602a73e',
        'name': "My virus inventory",
        'description': '',
        'is_public': True
    }
]}

```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/personal_attributes/inventory
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("inventory",  data=
    {
        'name': 'My new probe inventory',
        'description': '',
        'is_public': False
    }
)
```

### Response example
{: .no_toc}

```
{'inventory': {
    'id': 'd0ada97d-8607-48da-817b-bdd54bc9077b',
    'name': 'My new probe inventory',
    'description': '',
    'is_public': False}
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/personal_attributes/inventory/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('inventory', id='d0ada97d-8607-48da-817b-bdd54bc9077b')
```

### Response example
{: .no_toc}

```
{'inventory': {
    'id': 'd0ada97d-8607-48da-817b-bdd54bc9077b',
    'name': 'My new probe inventory',
    'description': '',
    'is_public': False}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/personal_attributes/inventory/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("inventory", id="d0ada97d-8607-48da-817b-bdd54bc9077b", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'inventory': {
    'id': 'd0ada97d-8607-48da-817b-bdd54bc9077b',
    'name': 'My new probe inventory',
    'description': 'new text',
    'is_public': False}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/personal_attributes/inventory/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("inventory", id="d0ada97d-8607-48da-817b-bdd54bc9077b")
``` 