---
layout: default
title: Behavior
parent: Modules
grand_parent: API
nav_order: 1
---

# Behavior API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `session` | related session ID formatted as a string **[required]** |
| `subjects` | list of related subjects IDs formatted as strings **[required]** |
| `setup` | related experimental setup ID formatted as a string **[required]** |
| `behavioralparadigm` | related behavioral paradigm ID formatted as a string **[required]** |
| `notes` | optional string (max 500 characters) for additional information |
| `order` | optional positive integer controlling display order within a session |


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/behavior
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('behavior')
```

### Response example
{: .no_toc}

```
{'behaviors': [
	{
		'id': '4ee63327-cb5e-4dc1-99f0-e4bd3c1e0598',
		'session': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
		'subjects': ['0f87c229-6769-4854-83a5-c71e154246b8'],
		'setup': '3e9ec0e0-d685-42ec-8386-0fa24602a73e',
		'behavioralparadigm': 'febe36f7-4769-496d-bb91-6a8443214b94'
	},
	{
		'id': 'f99631ef-f7bd-4f79-90b8-e2d790f26e0a',
		'session': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
		'subjects': ['35c41e86-dde1-4eb2-a0e2-94dfb1dccd92', '0f87c229-6769-4854-83a5-c71e154246b8'],
		'setup': 'df63fe54-17e9-4bc2-8409-1c7546a9c19f',
		'behavioralparadigm': '1a81b58f-f11d-4beb-81f4-1a7c9ed0b064'
	},
	{
		'id': '42fa77fe-c899-422d-815e-d7de230f0faa',
		'session': 'ef7ae22f-143a-4a5e-adf6-1c623531dd63',
		'subjects': ['35c41e86-dde1-4eb2-a0e2-94dfb1dccd92'],
		'setup': 'df63fe54-17e9-4bc2-8409-1c7546a9c19f',
		'behavioralparadigm': '1a81b58f-f11d-4beb-81f4-1a7c9ed0b064'
	}
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/modules/behavior
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("behavior",  data={
	"session": "1f7f103b-e949-405a-9b01-ddda3b2f10cf", 
	"subjects": ["0f87c229-6769-4854-83a5-c71e154246b8"],
	"setup": "3e9ec0e0-d685-42ec-8386-0fa24602a73e",
	"behavioralparadigm": "febe36f7-4769-496d-bb91-6a8443214b94",
	"notes": "Optional notes about this behavior"
})
```

### Response example
{: .no_toc}

```
{'behavior': 
	{
		'id': 'f9733b12-e2d5-4886-9e00-09ba26b01a16',
		'session': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
		'subjects': ['0f87c229-6769-4854-83a5-c71e154246b8'],
		'setup': '3e9ec0e0-d685-42ec-8386-0fa24602a73e',
		'behavioralparadigm': 'febe36f7-4769-496d-bb91-6a8443214b94',
		'notes': 'Optional notes about this behavior'
	}
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/behavior/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('behavior', id='f9733b12-e2d5-4886-9e00-09ba26b01a16')
```

### Response example
{: .no_toc}

```
{'behavior': 
	{
		'id': 'f9733b12-e2d5-4886-9e00-09ba26b01a16',
		'session': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
		'subjects': ['0f87c229-6769-4854-83a5-c71e154246b8'],
		'setup': '3e9ec0e0-d685-42ec-8386-0fa24602a73e',
		'behavioralparadigm': 'febe36f7-4769-496d-bb91-6a8443214b94',
		'notes': 'Optional notes about this behavior'
	}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/behavior/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("behavior", id="f9733b12-e2d5-4886-9e00-09ba26b01a16", data={'subjects': ['0f87c229-6769-4854-83a5-c71e154246b8', '35c41e86-dde1-4eb2-a0e2-94dfb1dccd92']})
```

### Response example
{: .no_toc}

```
{'behavior': 
	{
		'id': 'f9733b12-e2d5-4886-9e00-09ba26b01a16',
		'session': '1f7f103b-e949-405a-9b01-ddda3b2f10cf',
		'subjects': ['0f87c229-6769-4854-83a5-c71e154246b8', '35c41e86-dde1-4eb2-a0e2-94dfb1dccd92'],
		'setup': '3e9ec0e0-d685-42ec-8386-0fa24602a73e',
		'behavioralparadigm': 'febe36f7-4769-496d-bb91-6a8443214b94',
		'notes': 'Optional notes about this behavior'
	}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/modules/behavior/<id\>/
- **Data:** None
- **Responses:** `204` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("behavior", id="f9733b12-e2d5-4886-9e00-09ba26b01a16")
```
