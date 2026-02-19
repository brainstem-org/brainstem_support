---
layout: default
title: Publication
parent: Dissemination
grand_parent: API
nav_order: 4
---

# Publication API endpoint
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Fields

| Field        | Description  |
|:-------------|:-------------|
| `id` | UUID identificator formatted as a string |
| `title` | string **[required]** [max length: 200] |
| `authors` | string **[required]** [max length: 500] |
| `journal` | related journal ID formatted as a string **[required]** |
| `abstract` | string **[required]** |
| `doi` | string [max length: 200] |
| `publication_url` | string [max length: 300] |
| `pdf_url` | string [max length: 300] |
| `publication_date` | string containing date (e.g. "2023-03-22") **[required]** |

## List view

- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/dissemination/publication
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('publication')
```

### Response example
{: .no_toc}

```
{'publications': [
    {
        "id": "9cb4b5ba-b5d9-4bad-9b1e-65b5bdce0746",
        "title": "RTHybrid: A Standardized and Open-Source Real-Time Software Model Library for Experimental Neuroscience",
        "authors": "Amaducci R, Reyes-Sanchez M, Elices I, Rodriguez FB and Varona P",
        "journal": "0a71caa7-c984-47a4-921c-8b18405ee202",
        "abstract": "Short explanation of the paper",
        "doi": "",
        "publication_url": "",
        "pdf_url": "",
        "publication_date": "2020-03-12"
    },
    {
        "id": "8d0e93c1-ffa8-4d7d-a42a-65e1a0d938f6",
        "title": "Cooling of Medial Septum Reveals Theta Phase Lag Coordination of Hippocampal Cell Assemblies",
        "authors": "Peter Christian Petersen, György Buzsáki",
        "journal": "330b41c4-b4a4-4761-8d59-300695fdaf2a",
        "abstract": "Short explanation of the paper",
        "doi": "",
        "publication_url": "https://www.cell.com/neuron/fulltext/S0896-6273(20)30392-5",
        "pdf_url": "",
        "publication_date": "2020-06-10"
    }
]}
```

Public list responses also include a `meta` object (pagination/filter metadata).


## Add

- **Allowed portals:** private
- **Request method:** POST
- **URL:** https://www.brainstem.org/api/private/dissemination/publication
- **Data:** JSON dictionary containing at least the required fields.
- **Responses:** `201` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("publication",  data=
    {
        "title": "MyNewPaper",
        "authors": "Me et al.",
        "journal": "0a71caa7-c984-47a4-921c-8b18405ee202",
        "abstract": "Short explanation of the paper",
        "doi": "",
        "publication_url": "",
        "pdf_url": "",
        "publication_date": "1970-01-01"
    }
)
```

### Response example
{: .no_toc}

```
{'publication': {'id': 'e308cb04-428b-4b2c-b86b-15e02c664560',
  'title': 'MyNewPaper',
  'authors': 'Me et al.',
  'journal': '0a71caa7-c984-47a4-921c-8b18405ee202',
  'abstract': 'Short explanation of the paper',
  'doi': '',
  'publication_url': '',
  'pdf_url': '',
  'publication_date': '1970-01-01'}
}
```

## Detail

- **Allowed portals:** public, private
- **Request method:** GET
- **URL:** https://www.brainstem.org/api/private/dissemination/publication/<id\>/
- **Data:** None
- **Responses:** `200` OK; `403` Not allowed; `404` Not found

### Use example (using Python API)
{: .no_toc}

```
resp = client.load_model('publication', id='da3359b7-e380-4dc6-ba9d-04831d3082d9')
```

### Response example
{: .no_toc}

```
{'publication': {'id': 'e308cb04-428b-4b2c-b86b-15e02c664560',
  'title': 'MyNewPaper',
  'authors': 'Me et al.',
  'journal': '0a71caa7-c984-47a4-921c-8b18405ee202',
  'abstract': 'Short explanation of the paper',
  'doi': '',
  'publication_url': '',
  'pdf_url': '',
  'publication_date': '1970-01-01'}
}
```


## Change

- **Allowed portals:** private
- **Request method:** PATCH
- **URL:** https://www.brainstem.org/api/private/dissemination/publication/<id\>/
- **Data:** dictionary containing the fields to be updated
- **Responses:** `200` OK; `400` Bad request; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.save_model("publication", id="e308cb04-428b-4b2c-b86b-15e02c664560", data={"abstract": "new text"})
```

### Response example
{: .no_toc}

```
{'publication': {'id': 'e308cb04-428b-4b2c-b86b-15e02c664560',
  'title': 'MyNewPaper',
  'authors': 'Me et al.2',
  'journal': '0a71caa7-c984-47a4-921c-8b18405ee202',
  'abstract': 'new text',
  'doi': '',
  'publication_url': '',
  'pdf_url': '',
  'publication_date': '1970-01-01'}
}
```

## Delete

- **Allowed portals:** private
- **Request method:** DELETE
- **URL:** https://www.brainstem.org/api/private/dissemination/publication/<id\>/
- **Data:** None
- **Responses:** `204` OK; `403` Not allowed; `404` Not found


### Use example (using Python API)
{: .no_toc}

```
resp = client.delete_model("publication", id="e308cb04-428b-4b2c-b86b-15e02c664560")
```
