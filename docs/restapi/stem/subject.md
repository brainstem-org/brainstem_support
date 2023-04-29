---
layout: default
title: Subject
parent: STEM
grand_parent: REST API
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
| `id` | string with UUID identificator |
| `name` | string **[required]** |
| `description` | string |
| `strain` | string with UUID **[required]** |
| `sex` | string with "M" (male),"F" (female) or "U" (unknown) **[required]** |
| `genetic_line` | string |
| `projects` | list of strings representing the related projects IDs **[required]** |
| `birth_date` | string containing date (e.g. "2023-03-22") |
| `death_date` | string containing date (e.g. "2023-03-22") |
| `extra_content_json` | JSON dictionary |
| `actions` | list of strings representing the related actions IDs **[read-only]** |
| `subjectstatechanges` | list of strings representing the related subject state changes IDs **[read-only]** |
| `tags` | list of strings |



## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/stem/subject
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'subject')
```

### Response example
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
		'extra_content_json': [],
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
		'extra_content_json': [],
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
- **URL:** http://brainstem.org/rest/private/stem/subject
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = save_model(settings, "subject",  data={
	"name": "NewSubject", 
	"description": "some text", 
	"strain": "deec9da3-ee26-4348-954e-484f62c463c8", 
	"sex": "U", 
	"projects": ["c4b8a90b-2963-4d13-aa07-b6f497252dde"]
})
```

### Response example
```
{'subject': {'id': 'c20b2025-2e98-4eb9-bc89-0bad9f271c7f',
	'name': 'NewSubject',
	'description': 'some text',
	'strain': 'deec9da3-ee26-4348-954e-484f62c463c8',
	'sex': 'U',
	'genetic_line': '',
	'projects': ['c4b8a90b-2963-4d13-aa07-b6f497252dde'],
	'birth_date': None,
	'death_date': None,
	'extra_content_json': None,
	'actions': [],
	'subjectstatechanges': [],
	'tags': [],
	'links': {'projects': 'projects/'}}
}
```


## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** http://brainstem.org/rest/private/stem/subject/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
```
resp = load_model(settings, 'subject', id='c20b2025-2e98-4eb9-bc89-0bad9f271c7f')
```

### Response example
```
{'subject': {'id': 'c20b2025-2e98-4eb9-bc89-0bad9f271c7f',
	'name': 'NewSubject',
	'description': 'some text',
	'strain': 'deec9da3-ee26-4348-954e-484f62c463c8',
	'sex': 'U',
	'genetic_line': '',
	'projects': ['c4b8a90b-2963-4d13-aa07-b6f497252dde'],
	'birth_date': None,
	'death_date': None,
	'extra_content_json': None,
	'actions': [],
	'subjectstatechanges': [],
	'tags': [],
	'links': {'projects': 'projects/'}}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** http://brainstem.org/rest/private/stem/subject/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = save_model(settings, "subject", id="c20b2025-2e98-4eb9-bc89-0bad9f271c7f", data={"description": "new text"})
```

### Response example
```
{'subject': {'id': 'c20b2025-2e98-4eb9-bc89-0bad9f271c7f',
    'name': 'NewSubject',
    'description': 'new text',
    'strain': 'deec9da3-ee26-4348-954e-484f62c463c8',
    'sex': 'U',
    'genetic_line': '',
    'projects': ['c4b8a90b-2963-4d13-aa07-b6f497252dde'],
    'birth_date': None,
    'death_date': None,
    'extra_content_json': None,
    'actions': [],
    'subjectstatechanges': [],
    'tags': [],
    'links': {'projects': 'projects/'}}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** http://brainstem.org/rest/private/stem/subject/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
```
resp = delete_model(settings, "subject", id="c20b2025-2e98-4eb9-bc89-0bad9f271c7f")
```