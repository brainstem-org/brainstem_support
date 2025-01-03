---
layout: default
title: Data storage
parent: Personal attributes
grand_parent: API
nav_order: 5
---

# Data storage API endpoint
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
| `description` | string [max length: 500] |
| `is_public` | boolean |
| `data_organization_json` | JSON dictionary |
| `data_protocols_json` | JSON dictionary |

## List view
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/personal_attributes/datastorage
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('datastorage')
```

### Response example
{: .no_toc}

```
{'datastorage': [
    {
        'id': '2ba92d91-349d-4e8c-9785-fc941ddd8868',
        'name': 'Peters testdata',
        'description': '',
        'is_public': False,
        'data_organization_json': [],
        'data_protocols_json': []
    },
    {
        'id': 'c2197dea-eab6-4bbc-8257-3f05537ffdb6',
        'name': "Rodrigo's data",
        'description': '',
        'is_public': False,
        'data_organization_json': [
                {
                    "elements": "Sessions"
                },
                {
                    "elements": "Subjects"
                }
            ],
        'data_protocols_json': [
                {
                    "protocol": "Dropbox (Cloud solution)",
                    "path": "data/myproject",
                    "is_public": true
                },
                {
                    "protocol": "Local harddrive",
                    "path": "/home/myuser/data/myproject",
                    "is_public": false
                }
            ]
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/personal_attributes/datastorage
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("datastorage",  data=
    {
        'name': "MyNewRepo",
        'data_organization_json': [
                {
                    "elements": "Sessions"
                },
                {
                    "elements": "Subjects"
                }
            ],
        'data_protocols_json': [
                {
                    "protocol": "Dropbox (Cloud solution)",
                    "path": "data/myproject",
                    "is_public": True
                },
                {
                    "protocol": "Local harddrive",
                    "path": "/home/myuser/data/myproject",
                    "is_public": False
                }
            ]
    }
)
```

### Response example
{: .no_toc}

```
{'datastorage': {
    'id': '9f322057-cf48-4ec7-ab19-d0d7175cffe2',
    'name': 'MyNewRepo',
    'description': '',
    'is_public': False,
    'data_organization_json': [
                {
                    "elements": "Sessions"
                },
                {
                    "elements": "Subjects"
                }
            ],
    'data_protocols_json': [
                {
                    "protocol": "Dropbox (Cloud solution)",
                    "path": "data/myproject",
                    "is_public": true
                },
                {
                    "protocol": "Local harddrive",
                    "path": "/home/myuser/data/myproject",
                    "is_public": false
                }
            ]}
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/personal_attributes/datastorage/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('datastorage', id='9f322057-cf48-4ec7-ab19-d0d7175cffe2')
```

### Response example
{: .no_toc}

```
{'datastorage': {
    'id': '9f322057-cf48-4ec7-ab19-d0d7175cffe2',
    'name': 'MyNewRepo',
    'description': '',
    'is_public': False,
    'data_organization_json': [
                {
                    "elements": "Sessions"
                },
                {
                    "elements": "Subjects"
                }
            ],
    'data_protocols_json': [
                {
                    "protocol": "Dropbox (Cloud solution)",
                    "path": "data/myproject",
                    "is_public": true
                },
                {
                    "protocol": "Local harddrive",
                    "path": "/home/myuser/data/myproject",
                    "is_public": false
                }
            ]}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/personal_attributes/datastorage/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("datastorage", id="9f322057-cf48-4ec7-ab19-d0d7175cffe2", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'datastorage': {
    'id': '9f322057-cf48-4ec7-ab19-d0d7175cffe2',
    'name': 'MyNewRepo',
    'description': 'new text',
    'is_public': False,
    'data_organization_json': [
                {
                    "elements": "Sessions"
                },
                {
                    "elements": "Subjects"
                }
            ],
    'data_protocols_json': [
                {
                    "protocol": "Dropbox (Cloud solution)",
                    "path": "data/myproject",
                    "is_public": true
                },
                {
                    "protocol": "Local harddrive",
                    "path": "/home/myuser/data/myproject",
                    "is_public": false
                }
            ]}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/personal_attributes/datastorage/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("datastorage", id="9f322057-cf48-4ec7-ab19-d0d7175cffe2")
``` 