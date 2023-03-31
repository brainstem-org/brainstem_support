---
layout: default
title: Modules - Behavior
parent: API endpoints
grand_parent: REST API
nav_order: 2
---

## Table of contents
- [Fields](/brainstem_support/restapi/modules/behavior/#fields)
- Endpoints
  - [List view](/brainstem_support/restapi/modules/behavior/#list-view)
  - [Add](/brainstem_support/restapi/modules/behavior/#add)
  - [Detail](/brainstem_support/restapi/modules/behavior/#detail)
  - [Change](/brainstem_support/restapi/modules/behavior/#change)
  - [Delete](/brainstem_support/restapi/modules/behavior/#delete)

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | string with UUID identificator |
| `dataset` | string with the related dataset ID **[required]** |
| `subjects` | list of strings representing the related subjects IDs **[required]** |
| `physical_environment` | string with the related physical environment ID **[required]** |
| `behavioral_paradigm` | string with the related behavioral paradigm ID **[required]** |


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/modules/behavior
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'behavior')
```

### Response example
```
{'behaviors': [
	{
		'id': '4ee63327-cb5e-4dc1-99f0-e4bd3c1e0598',
		'dataset': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
		'subjects': ['0f87c229-6769-4854-83a5-c71e154246b8'],
		'physical_environment': '3e9ec0e0-d685-42ec-8386-0fa24602a73e',
		'behavioral_paradigm': 'febe36f7-4769-496d-bb91-6a8443214b94'
	},
	{
		'id': 'f99631ef-f7bd-4f79-90b8-e2d790f26e0a',
		'dataset': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
		'subjects': ['35c41e86-dde1-4eb2-a0e2-94dfb1dccd92', '0f87c229-6769-4854-83a5-c71e154246b8'],
		'physical_environment': 'df63fe54-17e9-4bc2-8409-1c7546a9c19f',
		'behavioral_paradigm': '1a81b58f-f11d-4beb-81f4-1a7c9ed0b064'
	},
	{
		'id': '42fa77fe-c899-422d-815e-d7de230f0faa',
		'dataset': 'ef7ae22f-143a-4a5e-adf6-1c623531dd63',
		'subjects': ['35c41e86-dde1-4eb2-a0e2-94dfb1dccd92'],
		'physical_environment': 'df63fe54-17e9-4bc2-8409-1c7546a9c19f',
		'behavioral_paradigm': '1a81b58f-f11d-4beb-81f4-1a7c9ed0b064'
	}
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** http://brainstem.org/rest/private/modules/behavior
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = save_model(settings, "behavior",  data={
	"dataset": "1f7f103b-e949-405a-9b01-ddda3b2f10cf", 
	"subjects": ["0f87c229-6769-4854-83a5-c71e154246b8"],
	"physical_environment": "3e9ec0e0-d685-42ec-8386-0fa24602a73e",
	"behavioral_paradigm": "febe36f7-4769-496d-bb91-6a8443214b94"
})
```

### Response example
```
{'behavior': 
	{
		'id': 'f9733b12-e2d5-4886-9e00-09ba26b01a16',
		'dataset': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
		'subjects': ['0f87c229-6769-4854-83a5-c71e154246b8'],
		'physical_environment': '3e9ec0e0-d685-42ec-8386-0fa24602a73e',
		'behavioral_paradigm': 'febe36f7-4769-496d-bb91-6a8443214b94'
	}
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/modules/behavior/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'behavior', id='f9733b12-e2d5-4886-9e00-09ba26b01a16')
```

### Response example
```
{'behavior': 
	{
		'id': 'f9733b12-e2d5-4886-9e00-09ba26b01a16',
		'dataset': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
		'subjects': ['0f87c229-6769-4854-83a5-c71e154246b8'],
		'physical_environment': '3e9ec0e0-d685-42ec-8386-0fa24602a73e',
		'behavioral_paradigm': 'febe36f7-4769-496d-bb91-6a8443214b94'
	}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/modules/behavior/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = save_model(settings, "behavior", id="f9733b12-e2d5-4886-9e00-09ba26b01a16", data={'subjects': ['0f87c229-6769-4854-83a5-c71e154246b8', '35c41e86-dde1-4eb2-a0e2-94dfb1dccd92']})
```

### Response example
```
{'behavior': 
	{
		'id': 'f9733b12-e2d5-4886-9e00-09ba26b01a16',
		'dataset': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
		'subjects': ['0f87c229-6769-4854-83a5-c71e154246b8', '35c41e86-dde1-4eb2-a0e2-94dfb1dccd92'],
		'physical_environment': '3e9ec0e0-d685-42ec-8386-0fa24602a73e',
		'behavioral_paradigm': 'febe36f7-4769-496d-bb91-6a8443214b94'
	}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** http://brainstem.org/rest/private/modules/behavior/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = delete_model(settings, "behavior", id="f9733b12-e2d5-4886-9e00-09ba26b01a16")
```