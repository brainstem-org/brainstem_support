---
layout: default
title: Taxonomies - Species
parent: API endpoints
grand_parent: REST API
nav_order: 6
---

## Table of contents
- [Fields](/brainstem_support/restapi/taxonomies/species/#fields)
- Endpoints
  - [List view](/brainstem_support/restapi/taxonomies/species/#list-view)
  - [Add](/brainstem_support/restapi/taxonomies/species/#add)
  - [Detail](/brainstem_support/restapi/taxonomies/species/#detail)
  - [Change](/brainstem_support/restapi/taxonomies/species/#change)
  - [Delete](/brainstem_support/restapi/taxonomies/species/#delete)
  - [List approvals](/brainstem_support/restapi/taxonomies/species/#list-approvals)
  - [Detail approval](/brainstem_support/restapi/taxonomies/species/#detail-approval)
  - [Accept approval](/brainstem_support/restapi/taxonomies/species/#accept-approval)
  - [Reject approval](/brainstem_support/restapi/taxonomies/species/#reject-approval)

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | string with UUID identificator |
| `name` | string **[required]** |
| `description` | string |
| `comments` | string |


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/taxonomies/species
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'species')
```

### Response example
```
{'species': [
    {
        'id': '089b00eb-94e3-464b-b7e8-62d04ddf2b11',
        'name': 'Rat',
        'description': 'Rattus rattus'
        },
    {
        'id': '93dd9502-305a-4e7b-b66b-42cf8c79368f',
        'name': 'Red-eared Turtles',
        'description': 'Trachemys scripta elegans'
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** http://brainstem.org/rest/private/taxonomies/species
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: Species submissions go through an approval process.

### Use example (using Python API)
```
resp = save_model(settings, "species",  data={
        "name": "MyNewSpecies",
        "description": "",
    }
)
```

### Response example
```
{'species_approval': {
    'id': '529efb3b-99f9-4e42-90e3-f5990988f037',
    'name': 'MyNewSpecies',
    'description': '',
    'comments': ''}
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/taxonomies/species/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'species', id='855d4962-52d9-49f2-a9ab-36073bd34c3f')
```

### Response example
```
{'species': {
    'id': '855d4962-52d9-49f2-a9ab-36073bd34c3f',
    'name': 'MyNewSpecies',
    'description': ''}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/taxonomies/species/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: Species changes go through an approval process.

### Use example (using Python API)
```
resp = save_model(settings, "species", id="855d4962-52d9-49f2-a9ab-36073bd34c3f", data={"description": "new text"})
```

### Response example
```
{'species_approval': {
    'id': '5ccb907c-520a-4c67-baf1-ac23a71ab710',
    'name': 'MyNewSpecies',
    'description': 'new text',
    'comments': ''}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** http://brainstem.org/rest/private/taxonomies/species/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

**Note**: only administrators can delete Species.

### Use example (using Python API)
```
resp = delete_model(settings, "species", id="855d4962-52d9-49f2-a9ab-36073bd34c3f")
``` 


## List approvals
- **Allowed portals:** private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/taxonomies/species_approvals
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'speciesapproval')
```

### Response example
```
{'species_approvals': [
    {
        'id': '529efb3b-99f9-4e42-90e3-f5990988f037',
        'name': 'MyNewSpecies',
        'description': '',
        'comments': '',
        'instance_id': None,
        'action': 'Add',
        'reviewer': None,
        'status': 'Pending'
    },
    {
        'id': '0e03a0f2-3b11-47bf-acc1-8b4b6d005692',
        'name': 'Digimon',
        'description': 'aaa',
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
- **URL:** http://brainstem.org/rest/private/taxonomies/species_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'speciesapproval', id='529efb3b-99f9-4e42-90e3-f5990988f037')
```

### Response example
```
{'species_approval': {
    'id': '529efb3b-99f9-4e42-90e3-f5990988f037',
    'name': 'MyNewSpecies',
    'description': '',
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
- **URL:** http://brainstem.org/rest/private/taxonomies/species_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = save_model(settings, "speciesapproval", id="529efb3b-99f9-4e42-90e3-f5990988f037", options="accept")
```


## Reject approval
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/taxonomies/species_approvals/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = save_model(settings, "speciesapproval", id="5ccb907c-520a-4c67-baf1-ac23a71ab710", options="reject")
```