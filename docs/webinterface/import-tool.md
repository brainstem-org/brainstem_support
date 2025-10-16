---
layout: default
title: Import tool
parent: Web interface
nav_order: 6
---
# Import tool
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Overview

The BrainSTEM import tool helps you add data to BrainSTEM by uploading CSV files. Instead of creating CSV files from scratch, you download pre-built templates for each data type, edit them with your data, and upload them.

**How it works**: Download template → Edit with your data → Upload → Review results

## Interface Overview

The import tool interface is organized into three main tabs: **Projects**, **Subjects**, and **Sessions**. Each tab provides templates and import functionality for related data types.

![Import tool web interface](/assets/images/webinterface/import_tool.png)

### Main Navigation Tabs
{: .no_toc}

- **Projects** - Import projects and project-related data
- **Subjects** - Import subjects, procedures, cohorts, and subject logs
- **Sessions** - Import sessions, behaviors, data acquisition, manipulations, epochs, and collections

### Template Downloads
{: .no_toc}

Each tab displays relevant template download buttons:

- **Blue template buttons** - Download pre-configured CSV templates for each data type
- Templates include example data and proper column formatting
- Multiple templates available per tab (e.g., Subjects tab has Subjects, Procedures, Subject Logs, and Cohorts templates; Sessions tab has Sessions, Behaviors, Data Acquisition, Manipulations, Epochs, and Collections templates)

### Import Process
{: .no_toc}

1. **Choose CSV File** - Drag and drop or click to select your completed CSV file
2. **Select Import Type** - Click the appropriate purple import button for your data type
3. **Review Results** - Check the import results for any errors or warnings


## Getting Started

### Quick Start
{: .no_toc}

1. Go to the import tool page ([www.brainstem.org/private/import-tool/](https://www.brainstem.org/private/import-tool/))
2. Select your data type (e.g., "subjects", "procedures")
3. Click "Download CSV Template"
4. Open the downloaded file and replace the example data with your data
5. Upload the modified CSV file
6. Check the results for any errors

### Why Use Templates?
{: .no_toc}

**No mistakes** - Templates have correct column names and formatting

**Faster** - All required fields are already included

**Better examples** - Shows you exactly how to format your data

### Finding Your UUIDs
{: .no_toc}

Templates use `YOUR_*_ID` placeholders for existing BrainSTEM data. To find these IDs:

1. Navigate to the relevant admin section (Procedures, Equipment, etc.)
2. Click edit/view on your record
3. Copy the UUID from the URL (long string of letters and numbers)

## Input conventions
- Column headers must follow the pattern `<entity>__<field>` and match exactly; unrecognised columns are ignored.
- CSVs are read with `pandas.read_csv`, so values may be wrapped in double quotes or left bare—both are accepted.
- Trimming happens automatically, but lookups remain case-sensitive. Keep names ≤200 characters to stay within model limits.
- Boolean fields accept `true/false`, `yes/no`, `1/0`, `on/off`, or `enabled/disabled` in any casing (for example `TRUE`, `0`). Blank values resolve to `false`.
- Datetimes accept ISO-8601 (`2024-05-01T14:30`), spaced formats (`2024-05-01 14:30[:45]`), and regional variants (`05/01/2024`, `01/05/2024 14:30`). Dates accept the same patterns without a time component.
- List-style columns must use comma-separated values with no brackets (for example `behavior, imaging, ephys`). The importer splits on commas and trims whitespace.
- JSON columns must contain valid JSON objects; malformed JSON raises a warning and the field is skipped. Example: `{"laserPower": 5, "units": "mW"}`.
- Rich-text fields (project, subject, session, cohort, collection descriptions) are backed by CKEditor and therefore accept HTML. Because inline scripts and event handlers will render, keep inputs to simple formatting (paragraphs, bold, italics, links) to avoid introducing interactive content.

## Data Type Details

### Projects
{: .no_toc}

| Field | Accepted Input | Notes |
| --- | --- | --- |
| `project__name` **\*** | Text (e.g. `Auditory Cortex Project`) | Must be unique across BrainSTEM; importer creates the project when it does not exist. |
| `project__description` | Plain text or limited HTML (e.g. `<p>Two-photon recordings.</p>`) | Stored in the rich-text description field; avoid interactive markup. |
| `project__is_public` | Boolean keywords (e.g. `true`, `no`, `0`) | Parsed via `parse_boolean`; blank values become `false`. |
| `project__tags` | Comma-separated tags (e.g. `vision, cortex`) | Converted into an array of individual tag names. |

### Subjects
{: .no_toc}

| Field | Accepted Input | Notes |
| --- | --- | --- |
| `project__name` **\*** | Existing project name (e.g. `Auditory Cortex Project`) | Projects must exist before importing subjects. |
| `subject__name` **\*** | Text (e.g. `Mouse_001`) | Subject names are globally unique. |
| `subject__sex` | `M`, `F`, `U` | Defaults to `U` (Unknown) when omitted. |
| `subject__description` | Plain text or limited HTML (e.g. `<p>WT male.</p>`) | Stored in the subject's rich-text description; avoid interactive markup. |
| `subject__strain` | Strain name (e.g. `C57BL/6J`) | Looks up the strain taxonomy; missing strains trigger warnings. |
| `subject__genetic_line` | Text (e.g. `Thy1-GCaMP6s`) | Free-form genetic line entry. |
| `subject__subject_identifier` | Text (e.g. `EarTag-123`) | External identifier. |
| `subject__supplier` | Supplier name (e.g. `Charles River Laboratories`) | Looks up existing suppliers; missing suppliers trigger warnings. |
| `subject__birth_date` | Date (e.g. `2023-02-14`) | Parsed and serialised to ISO date. |
| `subject__death_date` | Date (e.g. `2024/03/01`) | Parsed and serialised to ISO date. |
| `subject__tags` | Comma-separated tags (e.g. `training, cohortA`) | Split into a tag list. |
| `subject__name_used_in_storage` | Text (e.g. `mouse_001_data`) | Optional alternate storage label. |


### Procedures
{: .no_toc}

| Field | Accepted Input | Notes |
| --- | --- | --- |
| `subject__name` **\*** | Existing subject name (e.g. `Mouse_001`) | Subjects must exist before importing procedures. |
| `procedure__type` **\*** | Procedure type code (e.g. `VirusInjection`) | Must match an API choice. |
| `procedure__notes` | Plain text (e.g. `Injected 200 nL AAV.`) | Stored as free-form notes (500 characters). |
| `procedure__date_time` | Datetime (e.g. `2024-04-12 09:30`) | Parsed and stored as ISO-8601. |
| `procedure__atlas` | Atlas identifier (e.g. `AllenCCFv3`) | Used to scope brain-region lookups. |
| `procedure__brain_region` | Brain-region UUID or name (e.g. `VISp`) | Resolves within the supplied atlas first; warns and drops the field if unresolved. |
| `procedure__brain_region_acronym` | Atlas acronym (e.g. `VISp`) | Fallback lookup when the name is absent or ambiguous. |
| `procedure__coordinates` | Coordinate system key (e.g. `Stereotaxic_BregmaBrainSurface`) | Defaults when omitted. |
| `procedure__coordinates_data` | JSON object (e.g. `{"apCoordinate": -3.2}`) | Parsed into `coordinates_json`. |
| `procedure__consumablestock` | Consumable stock UUID (e.g. `6ac4...`) | Must reference an existing consumable stock record. |
| `procedure__equipment` | Comma-separated equipment UUIDs (e.g. `7f1b...,d2c9...`) | Each UUID is validated individually; invalid IDs raise warnings. |
| `procedure__details` | JSON object (e.g. `{"virus": "AAV9"}`) | Parsed into `type_json`; schema defaults are loaded if omitted. |

### Subject Logs
{: .no_toc}

| Field | Accepted Input | Notes |
| --- | --- | --- |
| `subject__name` **\*** | Existing subject name (e.g. `Mouse_001`) | Subjects must exist before logging entries. |
| `subject_log__type` **\*** | Subject-log type code (e.g. `TrainingSession`) | Example values: `Housing`, `WaterDeprivation`, `Handling`. |
| `subject_log__description` | Plain text (e.g. `Habituation to head-fix.`) | Stored on the log record (500 characters). |
| `subject_log__entry_datetime` | Datetime (e.g. `2024-05-02 10:00`) | Required for single-point logs (anything not in the start/end list below). |
| `subject_log__entry_start_datetime` | Datetime (e.g. `2024-05-02 10:00`) | Required for `Housing`, `FoodDeprivation`, `WaterDeprivation`, `Habituation`, `Handling`, `TrainingSession`. |
| `subject_log__entry_end_datetime` | Datetime (e.g. `2024-05-02 11:00`) | Optional for the start/end list; defaults to one hour after the start when omitted. |
| `subject_log__entry_notes` | Plain text (e.g. `Handled by J.D.`) | Saved with the log entry. |
| `subject_log__entry_data` | JSON object (e.g. `{"task": "Go/No-Go"}`) | Parsed into the entry `details` field. |

The importer finds or creates a `SubjectLog` for the subject/type pair, then adds a log entry when any entry timestamps are present. Duplicate entries for the same timestamp receive warnings and are counted as existing records.

### Sessions
{: .no_toc}

| Field | Accepted Input | Notes |
| --- | --- | --- |
| `project__name` **\*** | Existing project name (e.g. `Auditory Cortex Project`) | Projects must exist before importing sessions. |
| `session__name` **\*** | Text (e.g. `Session_001`) | Session names are globally unique. |
| `session__description` | Plain text or limited HTML (e.g. `<p>Baseline recording.</p>`) | Stored in the session's rich-text description; avoid interactive markup. |
| `session__date_time` | Datetime (e.g. `2024-05-10T13:45`) | Parsed and stored as ISO-8601. |
| `session__tags` | Comma-separated tags (e.g. `baseline, imaging`) | Converted into a tag list. |
| `session__data_storage` | Data storage UUID (e.g. `a1b2c3d4-...`) | Must reference an existing data storage record; warnings are emitted when not found. |
| `session_name_in_data_storage` | Text (e.g. `2024-05-10_baseline`) | Optional alias for storage systems. |

### Behaviors
{: .no_toc}

| Field | Accepted Input | Notes |
| --- | --- | --- |
| `session__name` **\*** | Existing session name (e.g. `Session_001`) | Sessions must exist before importing behaviors. |
| `subject__name` **\*** | Existing subject name (e.g. `Mouse_001`) | Subjects must exist before importing behaviors. |
| `behavior__setup` **\*** | Setup UUID (e.g. `d3d0...`) | Validated via the Setup endpoint. |
| `behavior__behavioral_paradigm` **\*** | Behavioral paradigm UUID (e.g. `f6d4...`) | Validated via the Behavioral Paradigm endpoint. |

### Data Acquisition
{: .no_toc}

| Field | Accepted Input | Notes |
| --- | --- | --- |
| `session__name` **\*** | Existing session name (e.g. `Session_001`) | Sessions must exist before importing data acquisition records. |
| `data_acquisition__type` **\*** | Data-acquisition type code (e.g. `FiberPhotometry`) | Must match an API choice. |
| `data_acquisition__procedures` **\*** | Comma-separated procedure UUIDs (e.g. `9f50...,aa21...`) | At least one procedure is required; each UUID is validated before linking. |
| `data_acquisition__equipment` | Comma-separated equipment UUIDs (e.g. `7f1b...,d2c9...`) | Each UUID is validated and attached when found. |
| `data_acquisition__notes` | Plain text (e.g. `Laser at 10 mW.`) | Stored as free-form notes (500 characters). |
| `data_acquisition__details` | JSON object (e.g. `{"samplingRate": 30000}`) | Parsed into the `details` field; defaults are pulled from the schema when omitted. |

### Manipulations
{: .no_toc}

| Field | Accepted Input | Notes |
| --- | --- | --- |
| `session__name` **\*** | Existing session name (e.g. `Session_001`) | Sessions must exist before importing manipulations. |
| `manipulation__type` **\*** | Manipulation type code (e.g. `OptogeneticStimulation`) | Must match an API choice. |
| `manipulation__procedures` **\*** | Comma-separated procedure UUIDs (e.g. `9f50...,aa21...`) | At least one procedure is required; each UUID is validated. |
| `manipulation__equipment` | Comma-separated equipment UUIDs (e.g. `7f1b...,d2c9...`) | Each UUID is validated before linking. |
| `manipulation__notes` | Plain text (e.g. `Blue light, 20 Hz.`) | Stored as free-form notes (500 characters). |
| `manipulation__details` | JSON object (e.g. `{"pulseWidthMs": 10}`) | Parsed into `type_json`; schema defaults apply when omitted. |

### Epochs
{: .no_toc}

| Field | Accepted Input | Notes |
| --- | --- | --- |
| `project__name` **\*** | Existing project name (e.g. `Auditory Cortex Project`) | Projects must exist before importing epochs. |
| `session__name` **\*** | Existing session name (e.g. `Session_001`) | Sessions must exist before importing epochs. |
| `epoch__name` **\*** | Text (e.g. `Baseline_Recording`) | Epoch names are unique within each session. |
| `epoch__start` | Time duration or timestamp (e.g. `00:00:00`, `PT0S`) | Start time relative to session beginning. Accepts HH:MM:SS format or ISO 8601 duration (PT#S/M/H). |
| `epoch__end` | Time duration or timestamp (e.g. `00:05:00`, `PT5M`) | End time relative to session beginning. Accepts HH:MM:SS format or ISO 8601 duration (PT#S/M/H). |
| `epoch__behavior` | Behavior UUID (e.g. `a8f2...`) | Optional link to behavior record during this epoch. |
| `epoch__dataacquisition` | Data acquisition UUID (e.g. `b3c7...`) | Optional link to data acquisition record during this epoch. |
| `epoch__manipulation` | Manipulation UUID (e.g. `c4d8...`) | Optional link to manipulation record during this epoch. |

### Cohorts
{: .no_toc}

| Field | Accepted Input | Notes |
| --- | --- | --- |
| `project__name` **\*** | Existing project name (e.g. `Auditory Cortex Project`) | Projects must exist before importing cohorts. |
| `cohort__name` **\*** | Text (e.g. `Training Cohort A`) | Names are enforced per project by the API. |
| `cohort__subjects` **\*** | Comma-separated subject names (e.g. `Mouse_001, Mouse_002`) | Each subject must already exist; missing subjects trigger warnings. |
| `cohort__description` | Plain text or limited HTML (e.g. `<p>For pilot sessions.</p>`) | Stored in the cohort's rich-text description; avoid interactive markup. |
| `cohort__tags` | Comma-separated tags (e.g. `pilot, cohortA`) | Split into a tag list. |

### Collections
{: .no_toc}

| Field | Accepted Input | Notes |
| --- | --- | --- |
| `project__name` **\*** | Existing project name (e.g. `Auditory Cortex Project`) | Projects must exist before importing collections. |
| `collection__name` **\*** | Text (e.g. `Baseline Series`) | Names are enforced per project by the API. |
| `collection__sessions` **\*** | Comma-separated session names (e.g. `Session_001, Session_002`) | Each session must already exist; missing sessions trigger warnings. |
| `collection__description` | Plain text or limited HTML (e.g. `<p>Includes pilot days.</p>`) | Stored in the collection's rich-text description; avoid interactive markup. |
| `collection__tags` | Comma-separated tags (e.g. `baseline, imaging`) | Split into a tag list. |

## Error handling

- Missing required fields stop the current row and records an error; later rows are still evaluated.
- Lookup failures on required relationships raise errors; missing optional lookups generate warnings and skip only the unresolved relationship.
- Invalid JSON, date, or datetime values raise warnings and the affected field is removed before the API call.
- Duplicate Subject Log entries and other unique-constraint hits are reported as warnings and counted as existing records.

## Tips for Success

### Before You Import
{: .no_toc}

1. **Download the right template** for your data type
2. **Check existing data** to avoid duplicates (especially for projects, subjects, sessions)
3. **Find your UUIDs** if the template needs them (see guide above)
4. **Back up your data** before bulk imports

### Common Issues
{: .no_toc}

- **Missing required fields** - The template will show you which fields are required
- **Wrong date format** - Use `YYYY-MM-DD` format
- **Invalid JSON** - Copy the exact format from template examples
- **UUID not found** - Double-check that the ID exists in your system and that you have permissions to use it.

### After Import
{: .no_toc}

- Review the results for any errors or warnings
- Fix any issues in your CSV and re-upload
- Check that your data appears correctly in BrainSTEM
