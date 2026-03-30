---
layout: default
title: Brain Region
parent: Taxonomies
grand_parent: API
nav_order: 7
---

# Brain Region API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `name` | string **[required]** [max length: 200]|
| `description` | string [max length: 2000] |
| `acronym` | string **[required]** [max length: 15]|
| `atlas` | string **[required]**. *See options below* [max length: 7]|

unique_together: [`atlas`, `acronym`] and [`atlas`, `name`]. 

These are the available `atlas` options for Brain Region:
- `AIA`: Allen Mouse Brain Atlas
- `AIA_dM`: Allen Developing Mouse Brain Atlas
- `AIA_HB`: Allen Human Brain Atlas
- `AIA_dHB`: Allen Developing Human Brain Atlas
- `AIA_P`: Allen Non-Human Primate Brain Atlas
- `AIA_S`: Allen Spinal Column Atlas
- `BM4`: Brain Maps 4.0 - Rat brain Atlas
- `PF2001`: Paxinos & Franklin 2001 Mouse Brain Atlas
- `PW1997`: Paxinos & Watson 1997 Rat Brain Atlas
- `S2004`: Swanson 2004 Rat Brain Atlas


## List view
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/brainregion
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('brainregion')
```

### Response example
{: .no_toc}

```
{"brain_regions": [
    {
        'id': '<id>',
        'name': 'Perifornical nucleus',
        'description': '',
        'acronym': 'PeF',
        'atlas': 'AIA'
    },
    {
        'id': '<id>',
        'name': 'Retrochiasmatic area',
        'description': '',
        'acronym': 'RCH',
        'atlas': 'AIA'
    },
    {
        'id': '<id>',
        'name': 'Subthalamic nucleus',
        'description': '',
        'acronym': 'STN',
        'atlas': 'AIA'
    }
]}
```

Public list responses also include a `meta` object (pagination/filter metadata).


## Add
- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/taxonomies/brainregion
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: only administrators can add Brain Regions.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("brainregion",  data={
        "name": "MyNewBrainRegion",
        "description": "",
        "acronym": "MNBR",
        "atlas": "AIA"
    }
)
```

### Response example
{: .no_toc}

```
{'brain_region': {
    'id': '<id>',
    'name': 'MyNewBrainRegion',
    'description': '',
    'acronym': 'MNBR',
    'atlas': 'AIA'}
}
```



## Detail
- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/brainregion/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load('brainregion', id='<id>')
```

### Response example
{: .no_toc}

```
{'brain_region': {
    'id': '<id>',
    'name': 'MyNewBrainRegion',
    'description': '',
    'acronym': 'MNBR',
    'atlas': 'AIA'}
}
```


## Change
- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/brainregion/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: only administrators can change Brain Regions.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save("brainregion", id="<id>", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'brain_region': {
    'id': '<id>',
    'name': 'MyNewBrainRegion',
    'description': 'new text',
    'acronym': 'MNBR',
    'atlas': 'AIA'}
}
```


## Delete
- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/taxonomies/brainregion/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

**Note**: only administrators can delete Brain Regions.

### Use example (using Python API)
{: .no_toc}

```
resp = client.delete("brainregion", id="<id>")
``` 
