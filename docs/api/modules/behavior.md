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
| `behavioralassay` | related behavioral assay ID formatted as a string **[required]** |
| `notes` | optional string (max 500 characters) for additional information |
| `order` | optional positive integer controlling display order within a session |


## List view
- **Allowed portals:** public, private
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
		'id': '00000000-0000-0000-0000-000000000000',
		'session': '00000000-0000-0000-0000-000000000000',
		'subjects': ['00000000-0000-0000-0000-000000000000'],
		'setup': '00000000-0000-0000-0000-000000000000',
		'behavioralassay': '00000000-0000-0000-0000-000000000000'
	},
	{
		'id': '00000000-0000-0000-0000-000000000000',
		'session': '00000000-0000-0000-0000-000000000000',
		'subjects': ['00000000-0000-0000-0000-000000000000', '00000000-0000-0000-0000-000000000000'],
		'setup': '00000000-0000-0000-0000-000000000000',
		'behavioralassay': '00000000-0000-0000-0000-000000000000'
	},
	{
		'id': '00000000-0000-0000-0000-000000000000',
		'session': '00000000-0000-0000-0000-000000000000',
		'subjects': ['00000000-0000-0000-0000-000000000000'],
		'setup': '00000000-0000-0000-0000-000000000000',
		'behavioralassay': '00000000-0000-0000-0000-000000000000'
	}
]}
```


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/modules/behavior
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("behavior",  data={
	"session": "00000000-0000-0000-0000-000000000000", 
	"subjects": ["00000000-0000-0000-0000-000000000000"],
	"setup": "00000000-0000-0000-0000-000000000000",
	"behavioralassay": "00000000-0000-0000-0000-000000000000",
	"notes": "Optional notes about this behavior"
})
```

### Response example
{: .no_toc}

```
{'behavior': 
	{
		'id': '00000000-0000-0000-0000-000000000000',
		'session': '00000000-0000-0000-0000-000000000000',
		'subjects': ['00000000-0000-0000-0000-000000000000'],
		'setup': '00000000-0000-0000-0000-000000000000',
		'behavioralassay': '00000000-0000-0000-0000-000000000000',
		'notes': 'Optional notes about this behavior'
	}
}
```



## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/modules/behavior/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('behavior', id='00000000-0000-0000-0000-000000000000')
```

### Response example
{: .no_toc}

```
{'behavior': 
	{
		'id': '00000000-0000-0000-0000-000000000000',
		'session': '00000000-0000-0000-0000-000000000000',
		'subjects': ['00000000-0000-0000-0000-000000000000'],
		'setup': '00000000-0000-0000-0000-000000000000',
		'behavioralassay': '00000000-0000-0000-0000-000000000000',
		'notes': 'Optional notes about this behavior'
	}
}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/modules/behavior/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("behavior", id="00000000-0000-0000-0000-000000000000", data={'subjects': ['00000000-0000-0000-0000-000000000000', '00000000-0000-0000-0000-000000000000']})
```

### Response example
{: .no_toc}

```
{'behavior': 
	{
		'id': '00000000-0000-0000-0000-000000000000',
		'session': '00000000-0000-0000-0000-000000000000',
		'subjects': ['00000000-0000-0000-0000-000000000000', '00000000-0000-0000-0000-000000000000'],
		'setup': '00000000-0000-0000-0000-000000000000',
		'behavioralassay': '00000000-0000-0000-0000-000000000000',
		'notes': 'Optional notes about this behavior'
	}
}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/modules/behavior/<id\>/
- **Data:** None
- **Responses:** `204` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("behavior", id="00000000-0000-0000-0000-000000000000")
```
