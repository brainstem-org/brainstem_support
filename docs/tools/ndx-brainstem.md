---
layout: default
title: ndx-brainstem
parent: Tools
nav_order: 6
---
# ndx-brainstem: NWB extension
{: .no_toc}

`ndx-brainstem` is an NWB extension that stores BrainSTEM experimental metadata inside an NWB file: the BrainSTEM records the file was made from, with every field, and the links between them. Core NWB fields describe the experiment for every reader; the extension adds the structured detail so nothing is lost. Files are written by [brainstem-nwb](/tools/brainstem-nwb/) with `brainstem-nwb export --extension brainstem`.

> **Repository:** [brainstem-org/ndx-brainstem](https://github.com/brainstem-org/ndx-brainstem).

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Installation

```bash
pip install ndx-brainstem
```

Python 3.10 or newer; depends on `pynwb`, `hdmf` and `ndx-anatomical-localization`, whose namespace is included. NWB stores the extension's schema in every file, so `pynwb` and MatNWB can read these files **without** installing the package.

## Neurodata types

### BrainstemMetadata
{: .no_toc}

A `LabMetaData` group at `/general/brainstem`. Its attributes record the provenance of the file: `export_format_version`, `export_scope` (`project` or `session`), `exported_at`, `source_sha256`, `project_ids`, `session_id`, `subject_id`, `unit_id` (`<session id>__<subject id>`), `exporter`, `exporter_version`, `mapping_version` and `content_sha256`. It holds one `BrainstemTable` per record kind and an optional `BrainstemSchemaTable`.

### BrainstemTable
{: .no_toc}

A `DynamicTable` of BrainSTEM records of one kind (procedures, sessions, materials, ...). Required columns:

| Column | Content |
|---|---|
| `brainstem_id` | the record's BrainSTEM id |
| `brainstem_model` | the model label, for example `modules.procedure` |

Optional columns: `details_schema` (`<Family>/<Type>@<version>`, for example `Procedure/VirusInjection@3.0.0`), `coordinates_schema` (the coordinate system's schema) and `unresolved_links` (links to records that are not in the file). The writer adds one column per BrainSTEM field, with strings as stored and other values as JSON text, and ragged link columns (`DynamicTableRegion`) to the tables of the related records or to the epochs table.

### BrainstemSchemaTable
{: .no_toc}

The schemas cited by the tables:

| Column | Content |
|---|---|
| `schema_id` | `<Family>/<Type>@<version>` |
| `schema_url` | the permanent URL, for example `https://www.brainstem.org/schemas/Procedure/VirusInjection/3.0.0.json` (see [Public schemas](/api/public-schemas/)) |
| `schema_json` | the schema document itself, when embedded with `--embed-schemas`; otherwise empty |

## Reading a file

```python
from pynwb import NWBHDF5IO

with NWBHDF5IO("sub-X_ses-Y.nwb", "r") as io:
    nwbfile = io.read()
    brainstem = nwbfile.lab_meta_data["brainstem"]
    procedures = brainstem.brainstem_tables["procedures"].to_dataframe()
    schemas = brainstem.schemas.to_dataframe()
```

With the package installed the classes are available as `from ndx_brainstem import BrainstemMetadata, BrainstemTable, BrainstemSchemaTable`.

## Versions

| Version | Change |
|---|---|
| 0.2.0 | `BrainstemSchemaTable` gains the required `schema_url`; `schema_json` may be empty; `BrainstemTable` gains `coordinates_schema` |
| 0.1.0 | `BrainstemMetadata`, `BrainstemTable`, `BrainstemSchemaTable` |

brainstem-nwb requires namespace 0.2.0 or newer when writing the extension.
