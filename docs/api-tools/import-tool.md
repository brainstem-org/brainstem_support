---
layout: default
title: Import tool
parent: API tools
nav_order: 4
---
# Import tool
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Overview

The BrainSTEM import tool helps you add data to BrainSTEM by uploading CSV files. Instead of creating CSV files from scratch, you download pre-built templates for each data type, edit them with your data, and upload them.

**🎯 How it works**: Download template → Edit with your data → Upload → Review results

## Getting Started

### Quick Start

1. Go to the import tool page
2. Select your data type (e.g., "subjects", "procedures")
3. Click "Download CSV Template"
4. Open the downloaded file and replace the example data with your data
5. Upload the modified CSV file
6. Check the results for any errors

### Why Use Templates?

✅ **No mistakes** - Templates have correct column names and formatting

✅ **Faster** - All required fields are already included

✅ **Better examples** - Shows you exactly how to format your data

### Finding Your UUIDs

Some templates need IDs from your existing BrainSTEM data. These are marked as `YOUR_*_ID` in the templates:

| Template ID | Where to find it |
| --- | --- |
| `YOUR_PROCEDURE_ID` | Admin → Procedures → Click edit → Copy ID from URL |
| `YOUR_EQUIPMENT_ID` | Admin → Equipment → Click edit → Copy ID from URL |
| `YOUR_CONSUMABLESTOCK_ID` | Admin → Consumable Stock → Click edit → Copy ID from URL |
| `YOUR_SETUP_ID` | Admin → Setup → Click edit → Copy ID from URL |
| `YOUR_BEHAVIORAL_PARADIGM_ID` | Admin → Behavioral Paradigm → Click edit → Copy ID from URL |

**💡 Tip**: The ID is the long string of letters and numbers in the URL when you're editing a record.

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

## Projects CSV

| Field | Required | Accepted Input | Multiple? | Notes |
| --- | --- | --- | --- | --- |
| `project__name` | Yes | Text (e.g. `Auditory Cortex Project`) | No | Must be unique across BrainSTEM; importer creates the project when it does not exist. |
| `project__description` | No | Plain text or limited HTML (e.g. `<p>Two-photon recordings.</p>`) | No | Stored in the rich-text description field; avoid interactive markup. |
| `project__is_public` | No | Boolean keywords (e.g. `true`, `no`, `0`) | No | Parsed via `parse_boolean`; blank values become `false`. |
| `project__tags` | No | Comma-separated tags (e.g. `vision, cortex`) | Yes | Converted into an array of individual tag names. |

## Subjects CSV

| Field | Required | Accepted Input | Multiple? | Notes |
| --- | --- | --- | --- | --- |
| `project__name` | Yes | Existing project name (e.g. `Auditory Cortex Project`) | No | Projects must exist before importing subjects. |
| `subject__name` | Yes | Text (e.g. `Mouse_001`) | No | Subject names are globally unique. |
| `subject__sex` | No | `M`, `F`, `U` | No | Defaults to `U` (Unknown) when omitted. |
| `subject__description` | No | Plain text or limited HTML (e.g. `<p>WT male.</p>`) | No | Stored in the subject's rich-text description; avoid interactive markup. |
| `subject__strain` | No | Strain name (e.g. `C57BL/6J`) | No | Looks up the strain taxonomy; missing strains trigger warnings. |
| `subject__genetic_line` | No | Text (e.g. `Thy1-GCaMP6s`) | No | Free-form genetic line entry. |
| `subject__subject_identifier` | No | Text (e.g. `EarTag-123`) | No | External identifier. |
| `subject__supplier` | No | Supplier name (e.g. `Charles River Laboratories`) | No | Looks up existing suppliers; missing suppliers trigger warnings. |
| `subject__birth_date` | No | Date (e.g. `2023-02-14`) | No | Parsed and serialised to ISO date. |
| `subject__death_date` | No | Date (e.g. `2024/03/01`) | No | Parsed and serialised to ISO date. |
| `subject__tags` | No | Comma-separated tags (e.g. `training, cohortA`) | Yes | Split into a tag list. |
| `subject__name_used_in_storage` | No | Text (e.g. `mouse_001_data`) | No | Optional alternate storage label. |


## Procedures CSV

| Field | Required | Accepted Input | Multiple? | Notes |
| --- | --- | --- | --- | --- |
| `subject__name` | Yes | Existing subject name (e.g. `Mouse_001`) | No | Subjects must exist before importing procedures. |
| `procedure__type` | Yes | Procedure type code (e.g. `VirusInjection`) | No | Must match an API choice. |
| `procedure__notes` | No | Plain text (e.g. `Injected 200 nL AAV.`) | No | Stored as free-form notes (500 characters). |
| `procedure__date_time` | No | Datetime (e.g. `2024-04-12 09:30`) | No | Parsed and stored as ISO-8601. |
| `procedure__atlas` | No | Atlas identifier (e.g. `AllenCCFv3`) | No | Used to scope brain-region lookups. |
| `procedure__brain_region` | No | Brain-region UUID or name (e.g. `VISp`) | No | Resolves within the supplied atlas first; warns and drops the field if unresolved. |
| `procedure__brain_region_acronym` | No | Atlas acronym (e.g. `VISp`) | No | Fallback lookup when the name is absent or ambiguous. |
| `procedure__coordinates` | No | Coordinate system key (e.g. `Stereotaxic_BregmaBrainSurface`) | No | Defaults when omitted. |
| `procedure__coordinates_data` | No | JSON object (e.g. `{"apCoordinate": -3.2}`) | No | Parsed into `coordinates_json`. |
| `procedure__consumablestock` | No | Consumable stock UUID (e.g. `6ac4...`) | No | Must reference an existing consumable stock record. |
| `procedure__equipment` | No | Comma-separated equipment UUIDs (e.g. `7f1b...,d2c9...`) | Yes | Each UUID is validated individually; invalid IDs raise warnings. |
| `procedure__details` | No | JSON object (e.g. `{"virus": "AAV9"}`) | No | Parsed into `type_json`; schema defaults are loaded if omitted. |

## Subject Logs CSV

| Field | Required | Accepted Input | Multiple? | Notes |
| --- | --- | --- | --- | --- |
| `subject__name` | Yes | Existing subject name (e.g. `Mouse_001`) | No | Subjects must exist before logging entries. |
| `subject_log__type` | Yes | Subject-log type code (e.g. `TrainingSession`) | No | Example values: `Housing`, `WaterDeprivation`, `Handling`. |
| `subject_log__description` | No | Plain text (e.g. `Habituation to head-fix.`) | No | Stored on the log record (500 characters). |
| `subject_log__entry_datetime` | Conditional | Datetime (e.g. `2024-05-02 10:00`) | No | Required for single-point logs (anything not in the start/end list below). |
| `subject_log__entry_start_datetime` | Conditional | Datetime (e.g. `2024-05-02 10:00`) | No | Required for `Housing`, `FoodDeprivation`, `WaterDeprivation`, `Habituation`, `Handling`, `TrainingSession`. |
| `subject_log__entry_end_datetime` | No | Datetime (e.g. `2024-05-02 11:00`) | No | Optional for the start/end list; defaults to one hour after the start when omitted. |
| `subject_log__entry_notes` | No | Plain text (e.g. `Handled by J.D.`) | No | Saved with the log entry. |
| `subject_log__entry_data` | No | JSON object (e.g. `{"task": "Go/No-Go"}`) | No | Parsed into the entry `details` field. |

The importer finds or creates a `SubjectLog` for the subject/type pair, then adds a log entry when any entry timestamps are present. Duplicate entries for the same timestamp receive warnings and are counted as existing records.

## Sessions CSV

| Field | Required | Accepted Input | Multiple? | Notes |
| --- | --- | --- | --- | --- |
| `project__name` | Yes | Existing project name (e.g. `Auditory Cortex Project`) | No | Projects must exist before importing sessions. |
| `session__name` | Yes | Text (e.g. `Session_001`) | No | Session names are globally unique. |
| `session__description` | No | Plain text or limited HTML (e.g. `<p>Baseline recording.</p>`) | No | Stored in the session's rich-text description; avoid interactive markup. |
| `session__date_time` | No | Datetime (e.g. `2024-05-10T13:45`) | No | Parsed and stored as ISO-8601. |
| `session__tags` | No | Comma-separated tags (e.g. `baseline, imaging`) | Yes | Converted into a tag list. |
| `session__data_storage` | No | Data-storage name (e.g. `NAS Array 01`) | No | Looks up a matching Personal Attribute › Data Storage record; warnings are emitted when not found. |
| `session_name_in_data_storage` | No | Text (e.g. `2024-05-10_baseline`) | No | Optional alias for storage systems. |


## Behaviors CSV

| Field | Required | Accepted Input | Multiple? | Notes |
| --- | --- | --- | --- | --- |
| `session__name` | Yes | Existing session name (e.g. `Session_001`) | No | Sessions must exist before importing behaviors. |
| `subject__name` | Yes | Existing subject name (e.g. `Mouse_001`) | No | Subjects must exist before importing behaviors. |
| `behavior__setup` | Yes | Setup UUID (e.g. `d3d0...`) | No | Validated via the Setup endpoint. |
| `behavior__behavioral_paradigm` | Yes | Behavioral paradigm UUID (e.g. `f6d4...`) | No | Validated via the Behavioral Paradigm endpoint. |


## Data Acquisition CSV

| Field | Required | Accepted Input | Multiple? | Notes |
| --- | --- | --- | --- | --- |
| `session__name` | Yes | Existing session name (e.g. `Session_001`) | No | Sessions must exist before importing data acquisition records. |
| `data_acquisition__type` | Yes | Data-acquisition type code (e.g. `FiberPhotometry`) | No | Must match an API choice. |
| `data_acquisition__procedures` | Yes | Comma-separated procedure UUIDs (e.g. `9f50...,aa21...`) | Yes | At least one procedure is required; each UUID is validated before linking. |
| `data_acquisition__equipment` | No | Comma-separated equipment UUIDs (e.g. `7f1b...,d2c9...`) | Yes | Each UUID is validated and attached when found. |
| `data_acquisition__notes` | No | Plain text (e.g. `Laser at 10 mW.`) | No | Stored as free-form notes (500 characters). |
| `data_acquisition__details` | No | JSON object (e.g. `{"samplingRate": 30000}`) | No | Parsed into the `details` field; defaults are pulled from the schema when omitted. |

## Manipulations CSV

| Field | Required | Accepted Input | Multiple? | Notes |
| --- | --- | --- | --- | --- |
| `session__name` | Yes | Existing session name (e.g. `Session_001`) | No | Sessions must exist before importing manipulations. |
| `manipulation__type` | Yes | Manipulation type code (e.g. `OptogeneticStimulation`) | No | Must match an API choice. |
| `manipulation__procedures` | Yes | Comma-separated procedure UUIDs (e.g. `9f50...,aa21...`) | Yes | At least one procedure is required; each UUID is validated. |
| `manipulation__equipment` | No | Comma-separated equipment UUIDs (e.g. `7f1b...,d2c9...`) | Yes | Each UUID is validated before linking. |
| `manipulation__notes` | No | Plain text (e.g. `Blue light, 20 Hz.`) | No | Stored as free-form notes (500 characters). |
| `manipulation__details` | No | JSON object (e.g. `{"pulseWidthMs": 10}`) | No | Parsed into `type_json`; schema defaults apply when omitted. |

## Cohorts CSV

| Field | Required | Accepted Input | Multiple? | Notes |
| --- | --- | --- | --- | --- |
| `project__name` | Yes | Existing project name (e.g. `Auditory Cortex Project`) | No | Projects must exist before importing cohorts. |
| `cohort__name` | Yes | Text (e.g. `Training Cohort A`) | No | Names are enforced per project by the API. |
| `cohort__subjects` | Yes | Comma-separated subject names (e.g. `Mouse_001, Mouse_002`) | Yes | Each subject must already exist; missing subjects trigger warnings. |
| `cohort__description` | No | Plain text or limited HTML (e.g. `<p>For pilot sessions.</p>`) | No | Stored in the cohort's rich-text description; avoid interactive markup. |
| `cohort__tags` | No | Comma-separated tags (e.g. `pilot, cohortA`) | Yes | Split into a tag list. |

## Collections CSV

| Field | Required | Accepted Input | Multiple? | Notes |
| --- | --- | --- | --- | --- |
| `project__name` | Yes | Existing project name (e.g. `Auditory Cortex Project`) | No | Projects must exist before importing collections. |
| `collection__name` | Yes | Text (e.g. `Baseline Series`) | No | Names are enforced per project by the API. |
| `collection__sessions` | Yes | Comma-separated session names (e.g. `Session_001, Session_002`) | Yes | Each session must already exist; missing sessions trigger warnings. |
| `collection__description` | No | Plain text or limited HTML (e.g. `<p>Includes pilot days.</p>`) | No | Stored in the collection's rich-text description; avoid interactive markup. |
| `collection__tags` | No | Comma-separated tags (e.g. `baseline, imaging`) | Yes | Split into a tag list. |

## Error handling
- Missing required fields stop the current row and record an error; later rows are still evaluated.
- Lookup failures on required relationships raise errors; missing optional lookups generate warnings and skip only the unresolved relationship.
- Invalid JSON, date, or datetime values raise warnings and the affected field is removed before the API call.
- Duplicate Subject Log entries and other unique-constraint hits are reported as warnings and counted as existing records.

## Tips for Success

### Before You Import

1. **Download the right template** for your data type
2. **Check existing data** to avoid duplicates (especially for projects, subjects, sessions)
3. **Find your UUIDs** if the template needs them (see guide above)
4. **Back up your data** before bulk imports

### Common Issues

- **Missing required fields** - The template will show you which fields are required
- **Wrong date format** - Use `YYYY-MM-DD` format
- **Invalid JSON** - Copy the exact format from template examples
- **UUID not found** - Double-check that the ID exists in your system

### After Import

- Review the results for any errors or warnings
- Fix any issues in your CSV and re-upload
- Check that your data appears correctly in BrainSTEM

**💡 Remember**: Templates are your best friend - they prevent most common import errors!