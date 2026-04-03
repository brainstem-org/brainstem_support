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
resp = client.load('publication')
```

### Response example
{: .no_toc}

```
{'publications': [
    {
        "id": "<id>",
        "title": "RTHybrid: A Standardized and Open-Source Real-Time Software Model Library for Experimental Neuroscience",
        "authors": "Amaducci R, Reyes-Sanchez M, Elices I, Rodriguez FB and Varona P",
        "journal": "<journal-id>",
        "abstract": "Short explanation of the paper",
        "doi": "",
        "publication_url": "",
        "pdf_url": "",
        "publication_date": "2020-03-12"
    },
    {
        "id": "<id>",
        "title": "Cooling of Medial Septum Reveals Theta Phase Lag Coordination of Hippocampal Cell Assemblies",
        "authors": "Peter Christian Petersen, György Buzsáki",
        "journal": "<journal-id>",
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
resp = client.save("publication",  data=
    {
        "title": "MyNewPaper",
        "authors": "Me et al.",
        "journal": "<journal-id>",
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
{'publication': {'id': '<id>',
  'title': 'MyNewPaper',
  'authors': 'Me et al.',
  'journal': '<journal-id>',
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
resp = client.load('publication', id='<id>')
```

### Response example
{: .no_toc}

```
{'publication': {'id': '<id>',
  'title': 'MyNewPaper',
  'authors': 'Me et al.',
  'journal': '<journal-id>',
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
resp = client.save("publication", id="<id>", data={"abstract": "new text"})
```

### Response example
{: .no_toc}

```
{'publication': {'id': '<id>',
  'title': 'MyNewPaper',
  'authors': 'Me et al.2',
  'journal': '<journal-id>',
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
resp = client.delete("publication", id="<id>")
```
