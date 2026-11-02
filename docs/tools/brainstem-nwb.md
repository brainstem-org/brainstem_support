---
layout: default
title: brainstem-nwb
parent: Tools
nav_order: 5
---
# brainstem-nwb: NWB export
{: .no_toc}

`brainstem-nwb` exports experimental metadata from BrainSTEM to [Neurodata Without Borders](https://www.nwb.org) (NWB) files. It reads a BrainSTEM [project or session export](/api/export/) and writes one NWB file per session and subject, following NWB and DANDI conventions, together with a conversion manifest and a validation report.

Each file holds the session and its subject; the surgeries, viruses and drugs the subject received; the devices, electrode groups and optogenetic sites; and the acquisitions, behaviors, manipulations and epochs of the session. The converter is **metadata only**: measured data (time series, images, video) is not converted.

> **Repository:** [brainstem-org/brainstem-nwb](https://github.com/brainstem-org/brainstem-nwb), with full documentation of the mapping, the manifest, the warnings and the validation.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Principles

- **Nothing invented.** Experimenter, lab and institution come from your configuration file, never from guesses. A missing session start time leaves that session without a file and reports why.
- **Nothing silently dropped.** Every value that could not be mapped is listed in the manifest with a reason.
- **Traceable.** Each file carries a provenance block with the export it came from, its checksum, the converter and mapping versions, and a content-derived NWB identifier.
- **Core NWB by default.** Plain NWB files that any reader understands; with `--extension brainstem` the complete BrainSTEM records are added through [ndx-brainstem](/tools/ndx-brainstem/) so nothing is lost.

## Installation

```bash
pip install brainstem-nwb
```

Python 3.10 or newer. The package depends on `pynwb`, `nwbinspector` and the [Python API tool](/tools/python-api-tool/) (2.1 or newer, used to fetch exports). For the extension output also install `ndx-brainstem`.

## Quick start

From a downloaded export (Project → Download → JSON in the web interface):

```bash
brainstem-nwb export --export-file brainstem-export.json.gz --output ./nwb/
```

Directly from the server:

```bash
brainstem login                                                 # once, from the Python API tool
brainstem-nwb export --project PROJECT_UUID --output ./nwb/
brainstem-nwb export --session SESSION_UUID --output ./nwb/     # one session
```

Authentication follows the API tools: `--token` or `BRAINSTEM_API_TOKEN`, then the cached token from `brainstem login`, then the browser sign-in on an interactive terminal. In scripts and CI, `--no-device-flow` makes the exporter stop with exit code 3 instead of waiting for a browser. Export needs read access to the project.

## Configuration

Values NWB requires but BrainSTEM does not store per session come from a TOML file passed with `--config`:

```toml
[nwbfile]
experimenter = ["Last, First", "Other, Person"]
experimenter_source = "config"    # or "session_creator"
lab = "My Lab"
institution = "My University"

[subject]
label_field = "name"              # or "name_used_in_storage": used for subject_id and file names
species_format = "binomial"       # or "ncbitaxon": NCBI Taxonomy IRI, preferred by DANDI
```

## Output

```
nwb/
├── sub-<subject>/sub-<subject>_ses-<session>.nwb
├── brainstem-nwb-manifest.json      # what was written, from which records, with every warning
├── validation-report.json / .txt    # pynwb validation, NWB Inspector (DANDI configuration), BrainSTEM checks
└── source/brainstem-export-….json.gz  # the export, when fetched from the server
```

Specimen (ex vivo) sessions are supported; the subject is reached through the specimen set.

## What goes where

| NWB | BrainSTEM |
|---|---|
| `session_id`, `session_start_time`, `session_description` | session name, date and time, description |
| `experiment_description`, `keywords`, `related_publications`, `protocol` | project name and description, tags, publications (DOI), protocols of the procedures |
| `surgery` | one line per surgical, implant, tissue, sample collection and endpoint procedure before the session: type, date, target regions with atlas, coordinates, materials with supplier and RRID, performer, protocol, notes |
| `virus`, `pharmacology`, `stimulus_notes` | virus injections with construct, batch and titer; anesthesia, analgesics, drug and fluid administrations and pharmacological manipulations; other manipulations |
| `data_collection` | one line per data acquisition: type, file name, format, sampling rate, channels, interfaces, equipment |
| `slices` | specimen sets, specimens and specimen procedures |
| `Subject` | subject id, species (binomial or NCBI Taxonomy IRI), strain, sex, date of birth, age, genotype, latest weight before the session, description |
| `Device`, `ElectrodeGroup`, `OptogeneticStimulusSite` | equipment and experimental interfaces, hardware devices and probe designs; one electrode group per probe with the region acronyms as location; an optic fiber with one recorded wavelength |
| epochs table | session epochs with their linked records |

Not yet written: electrode rows, `ElectricalSeries`, `OptogeneticSeries`, imaging planes, intracellular recordings, position or video data, trials. The repository's `docs/modalities.md` lists the coverage per modality.

## Extension output

`--extension brainstem` adds a `/general/brainstem` group written with [ndx-brainstem](/tools/ndx-brainstem/): one table per record kind (projects, subjects, sessions, specimen sets, procedures, interfaces, materials, acquisitions, manipulations, behaviors, epochs, logs and their entries, catalog entries, people, atlases, regions, publications, suppliers, and more), with every field as stored and links between tables. Each typed row names its schema as `<Family>/<Type>@<version>` and a schema table lists the permanent URL of every cited schema version (see [Public schemas](/api/public-schemas/)); `--embed-schemas` stores the schema documents themselves in the file.

Coordinates recorded in the bregma- and lambda-based absolute systems and in Allen CCFv3 are also written as `ndx-anatomical-localization` tables. `--herd` writes the ontology terms (NCBI Taxonomy, RRIDs, atlas regions) as a sidecar.

## Command line

```bash
brainstem-nwb export (--project UUID | --export-file FILE | --session UUID) --output DIR [options]
brainstem-nwb manifest --export-file export.json -o manifest.json    # dry run, no files written
brainstem-nwb validate ./nwb/ [--manifest FILE] [--inspector-config dandi|none] [--fail-on error|warning]
brainstem-nwb fetch --project UUID -o export.json.gz                  # download the export only
brainstem-nwb mapping [--format md|json]                              # the mapping specification
brainstem-nwb schema manifest|report                                  # JSON schemas of the manifest and report
```

Useful `export` options: `--session ID|NAME` (repeatable, to select sessions of a project), `--config FILE.toml`, `--dry-run`, `--extension brainstem`, `--embed-schemas`, `--herd`, `--overwrite`, `--reproducible`, `--no-validate`, `--json`.

Exit codes: `0` success, `1` some sessions failed, `2` usage or configuration error, `3` authentication or download failure, `4` validation errors.

## Python API

```python
from brainstem_nwb import export_project

result = export_project(project_id="PROJECT_UUID", output_dir="./nwb")
# or: export_project(export_file="brainstem-export.json.gz", output_dir="./nwb")
print(result.exit_code, result.manifest.summary)
```

`export_session`, `build_manifest`, `validate_output`, `load_export` and `fetch_export` are also available.

## Limitations

- Metadata only; no time series, electrode positions, imaging planes or trials. Raw-data conversion is planned.
- Needs export format 2.x; format 2.1 is required for regions, publications, suppliers, user names and log entries.
- Experimenter, lab and institution must be given in the configuration.
- Brain-surface coordinate systems and approach angles are not written as localization points.

## Related

- [Exports](/api/export/): the input format.
- [ndx-brainstem](/tools/ndx-brainstem/): the extension that stores the complete records.
- [Agent skills](/tools/agent-skills/): the `brainstem-export` skill drives this converter.
