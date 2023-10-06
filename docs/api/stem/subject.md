---
layout: default
title: Subject
parent: STEM
grand_parent: API
nav_order: 2
---

# Subject API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `name` | string **[required]** [max length: 100]|
| `description` | string |
| `strain` | strain ID formatted as a string **[required]** |
| `sex` | string with "M" (male),"F" (female) or "U" (unknown) **[required]** [max length: 1]|
| `genetic_line` | string [max length: 100]|
| `subject_identifier` | string [max length: 100]|
| `source` | string [max length: 100]|
| `projects` | list of related projects IDs formatted as strings **[required]** |
| `birth_date` | string containing date (e.g. "2023-03-22") |
| `death_date` | string containing date (e.g. "2023-03-22") |
| `extra_fields` | list of JSON dictionaries. *See structure below* |
| `actions` | list of related actions IDs formatted as strings **[read-only]** |
| `subjectstatechanges` | list of related subject state changes IDs formatted as strings **[read-only]** |
| `name_used_in_repository` | string [max length: 200]|
| `tags` | list of strings |


`extra_fields` is a list of JSON dictionaries with two elements, `name` and `value` like the example below. The name must start with a letter and can only consist of letters, numbers and underscore. The value can be a string or a numeric value. 

```
{
    "extra_property": "setting1", 
    "another_property: 22
}
```


## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/subject
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('subject')
```

### Response example
{: .no_toc}

```
{'subjects': [{'id': '0cdaf69d-63cf-429f-b549-fc0cc163d046',
		'name': 'subject1',
		'description': '',
		'strain': 'deec9da3-ee26-4348-954e-484f62c463c8',
		'sex': 'M',
		'genetic_line': '',
		'projects': ['c4b8a90b-2963-4d13-aa07-b6f497252dde'],
		'birth_date': '2023-03-22',
		'death_date': None,
		'extra_fields': [],
		'actions': ['9542eb95-90b3-40c6-9e35-9eef01b3334a'],
		'subjectstatechanges': ['7791fcff-fcee-4c74-bfff-e2b3e4e38481'],
		'tags': [],
		'links': {'projects': 'projects/',
		'actions': 'actions/',
		'subjectstatechanges': 'subjectstatechanges/'}},
	{'id': '0f87c229-6769-4854-83a5-c71e154246b8',
		'name': 'subject2',
		'description': '',
		'strain': '7d056b05-ff2c-4dda-96f5-e34fe4dc3ac4',
		'sex': 'M',
		'genetic_line': '',
		'projects': ['e7475834-7733-48cf-9e3b-f4f2d2d0305a'],
		'birth_date': None,
		'death_date': None,
		'extra_fields': [],
		'actions': ['f79d84c8-6bec-40e3-b18a-5b25e57f4a09',
		'a18dd2b1-6393-468c-9424-1bc77b9e4976',
		'087b71c4-6785-437c-b8ef-e35a82a8463e',
		'794fbe3b-3b11-4593-9a6a-96bad2ecf518',
		'655ed49b-c86f-42f8-aac0-1a2d56046fcf',
		'2ef9b54f-080e-46a9-a172-612cffe3a24a',
		'dedef2d7-00ae-4967-8e93-a9d65a20dfce',
		'9bb4f750-07fb-44f5-9f68-cc0e1bfbcc74'],
		'subjectstatechanges': ['3d8ba812-2237-4811-875d-96cfdca66e18'],
		'tags': ['cooling'],
		'links': {'projects': 'projects/',
		'actions': 'actions/',
		'subjectstatechanges': 'subjectstatechanges/'}
	}
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/stem/subject
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("subject",  data={
	"name": "NewSubject", 
	"description": "some text", 
	"strain": "deec9da3-ee26-4348-954e-484f62c463c8", 
	"sex": "U", 
	"projects": ["c4b8a90b-2963-4d13-aa07-b6f497252dde"]
})
```

### Response example
{: .no_toc}

```
{'subject': {'id': 'b4ae1f92-5260-4605-8d21-25ac5c3fce91',
	'name': 'NewSubject',
	'description': 'some text',
	'strain': 'deec9da3-ee26-4348-954e-484f62c463c8',
	'sex': 'U',
	'genetic_line': '',
	'projects': ['c4b8a90b-2963-4d13-aa07-b6f497252dde'],
	'birth_date': None,
	'death_date': None,
	'extra_fields': None,
	'actions': [],
	'subjectstatechanges': [],
	'tags': [],
	'links': {'projects': 'projects/'}}
}
```


## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/stem/subject/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('subject', id='b4ae1f92-5260-4605-8d21-25ac5c3fce91')
```

### Response example
{: .no_toc}

```
{'subject': {'id': 'b4ae1f92-5260-4605-8d21-25ac5c3fce91',
	'name': 'NewSubject',
	'description': 'some text',
	'strain': 'deec9da3-ee26-4348-954e-484f62c463c8',
	'sex': 'U',
	'genetic_line': '',
	'projects': ['c4b8a90b-2963-4d13-aa07-b6f497252dde'],
	'birth_date': None,
	'death_date': None,
	'extra_fields': {
	    "extra_property": "setting1", 
	    "another_property: 22
	},
	'actions': [],
	'subjectstatechanges': [],
	'tags': [],
	'links': {'projects': 'projects/'}}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/stem/subject/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("subject", id="b4ae1f92-5260-4605-8d21-25ac5c3fce91", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'subject': {'id': 'b4ae1f92-5260-4605-8d21-25ac5c3fce91',
    'name': 'NewSubject',
    'description': 'new text',
    'strain': 'deec9da3-ee26-4348-954e-484f62c463c8',
    'sex': 'U',
    'genetic_line': '',
    'projects': ['c4b8a90b-2963-4d13-aa07-b6f497252dde'],
    'birth_date': None,
    'death_date': None,
    'extra_fields': None,
    'actions': [],
    'subjectstatechanges': [],
    'tags': [],
    'links': {'projects': 'projects/'}}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/stem/subject/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("subject", id="b4ae1f92-5260-4605-8d21-25ac5c3fce91")
```