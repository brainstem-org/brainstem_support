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
| `description` | string [max length: 500] |
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
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/brainregion
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('brainregion')
```

### Response example
{: .no_toc}

```
{"brain_regions": [
    {
        'id': '620a4416-54fb-4386-b8a7-dda66ac0a7e5',
        'name': 'Perifornical nucleus',
        'description': '',
        'acronym': 'PeF',
        'atlas': 'AIA'
    },
    {
        'id': 'b4782d29-c96c-4bf9-9394-8be2f2ed269a',
        'name': 'Retrochiasmatic area',
        'description': '',
        'acronym': 'RCH',
        'atlas': 'AIA'
    },
    {
        'id': '927a4e7a-4c75-4ecc-8670-bef7e8f4e944',
        'name': 'Subthalamic nucleus',
        'description': '',
        'acronym': 'STN',
        'atlas': 'AIA'
    }
]}
```


## Add
- **Allowed portals:** private, super
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/taxonomies/brainregion
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: only administrators can add Brain Regions.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("brainregion",  data={
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
    'id': '2cdd3db4-1dc4-4568-9ee3-de2356ee31a9',
    'name': 'MyNewBrainRegion',
    'description': '',
    'acronym': 'MNBR',
    'atlas': 'AIA'}
}
```



## Detail
- **Allowed portals:** public, private, super
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/taxonomies/brainregion/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('brainregion', id='2cdd3db4-1dc4-4568-9ee3-de2356ee31a9')
```

### Response example
{: .no_toc}

```
{'brain_region': {
    'id': '2cdd3db4-1dc4-4568-9ee3-de2356ee31a9',
    'name': 'MyNewBrainRegion',
    'description': '',
    'acronym': 'MNBR',
    'atlas': 'AIA'}
}
```


## Change
- **Allowed portals:** private, super
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/taxonomies/brainregion/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found

**Note**: only administrators can change Brain Regions.

### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("brainregion", id="2cdd3db4-1dc4-4568-9ee3-de2356ee31a9", data={"description": "new text"})
```

### Response example
{: .no_toc}

```
{'brain_region': {
    'id': '2cdd3db4-1dc4-4568-9ee3-de2356ee31a9',
    'name': 'MyNewBrainRegion',
    'description': 'new text',
    'acronym': 'MNBR',
    'atlas': 'AIA'}
}
```


## Delete
- **Allowed portals:** private, super
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/taxonomies/brainregion/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found

**Note**: only administrators can delete Brain Regions.

### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("brainregion", id="2cdd3db4-1dc4-4568-9ee3-de2356ee31a9")
``` 
