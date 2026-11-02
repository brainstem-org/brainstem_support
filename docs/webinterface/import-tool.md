---
layout: default
title: Import tool
parent: Import and export
grand_parent: Web interface
nav_order: 1
---
# Import tool
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Overview

The import tool (**Tools** → **Import tool**, page title **Lab notebook import tool**) creates many entries at once. It has two tabs at the top of the page:

- **Batch entry**: fill a grid in the browser, validate the rows and import the valid ones.
- **CSV import**: download a CSV template for one kind of entry, fill it in a spreadsheet program and upload it.

Both tabs create new entries only. An entry that already exists with the same name is found and left unchanged, never overwritten. Related entries (the project of a subject, the subject of a procedure, the session of a recording) must exist before the rows that refer to them, so import in the order **Projects → Subjects → Sessions → related data**. Rows are created with the same rules as the forms: unique names, species before strain, an experimental interface for every recording. You need to be a Contributor, Manager or Owner of the project the rows go into.

For colony data from SoftMouse use the [SoftMouse integration]({{"webinterface/softmouse/"|absolute_url}}). For scripted imports use the [API tools]({{"tools/"|absolute_url}}).

## Batch entry

Batch entry is a spreadsheet-like grid with dropdowns, date pickers and tag editors. Nothing is written until you validate the rows and confirm the import.

{% include slides.html slides="import-tool-batch-grid|Batch entry for subjects after Validate current tab: one new row, one that already exists, and one blocked because a required field is missing; the summary line counts them.;;import-tool-fields|Fields chooses which columns the grid shows for a record type." %}

### Choosing what to create
{: .no_toc}

Under **Choose a model**, pick a **Model family** and then a **Record type**:

| Model family | Record types |
|--------------|--------------|
| **Projects** | **Projects** |
| **Subjects** | **Subjects**, **Procedures**, **Subject Logs**, **Log Entries**, **Breedings**, **Cohorts** |
| **Sessions** | **Sessions**, **Behaviors**, **Data Acquisition**, **Manipulations**, **Collections** |

Each record type has its own panel. The question-mark button in the panel title opens the help dialog of that entry type. Click **Pin** to keep a panel open while you switch to another record type, for example to keep the Subjects grid next to the Procedures grid; **Pinned** panels stack below the active one.

The project scope sits in the top-right corner of the model card. **All permitted projects** offers every project you may change; switch to **Active only** to offer only your [active projects]({{"webinterface/list-view/#active-projects"|absolute_url}}). The switch is disabled until you have marked at least one project as active; **Manage active projects** opens the selection dialog.

### Filling the grid
{: .no_toc}

- **Add row** appends an empty row. Rows are numbered; each row has **Duplicate** and **Delete** actions.
- Required cells are marked and show **Choose…** until a value is picked.
- Dropdown cells search the entries you may use. Dependent cells are filtered by their parent and show "filtered by {parent}": strain by species, target regions by atlas, breeding by project, subjects of a behavior by the session's project, experimental interfaces by session, equipment by setup, consumable stock by inventory, catalog consumable by supplier, protocol by type.
- Tag cells open a tag editor (**Search or create a tag…**).
- Date cells take **YYYY-MM-DD**, date and time cells add **HH:MM:SS**.
- Cells with type-specific fields show an **Edit** button (with the number of filled values) that opens the fields of the chosen type: the **Schema** column for procedure, log, data acquisition and manipulation details, the **Coordinates** column for the chosen coordinate system, **Extra content** for custom key and value pairs, and **Repository links** on sessions. Choose the type first; otherwise the editor says "Select a procedure type first."
- **Fields** opens a dialog to show or hide columns (**Search fields…**, **Select all**, **Deselect all**, "N of M fields visible"). Hidden columns keep their values.
- On narrow screens each row is a card; **Edit row** opens the row's fields in a drawer.

Your rows are saved as a draft in this browser and are still there when you come back to the page. **Clear draft** empties the grid of the current record type after a confirmation (**Clear this draft?**). A grid holds at most 500 rows ("max 500 records").

### What each record type asks for
{: .no_toc}

Required cells are in bold.

| Record type | Cells |
|-------------|-------|
| Projects | **Project name**, Description, Authenticated groups, Public (Yes or No), Tags, Can change (users), Managers, Owners |
| Subjects | **Project**, **Subject name**, **Sex**, **Species**, **Status** (default Active), Strain, Description, Genetic line, Genotype, Subject identifier, Supplier, Breeding, Licenses, Birth date, Death date, Tags, Extra content, Name used in storage |
| Procedures | **Subject**, **Procedure type**, Date/time, Notes, Protocol, Licenses, Atlas, Target regions, Stock source (inventory, catalog or manual) with Inventory and Consumable stock or Supplier and Catalog consumable, Setup, Equipment, Schema, Coordinate system, Coordinates |
| Subject Logs | **Subject**, **Log type**, Description, Protocol |
| Log Entries | **Subject**, **Subject log**, Entry date/time (single-point logs) or Entry start and Entry end (ranged logs such as Housing, Food deprivation, Water deprivation, Habituation, Handling, Training session), Entry notes, Schema |
| Breedings | **Project**, **Breeding name**, **Maternal subject**, **Paternal subject**, Description, Tags, Start date, End date, Birth date, Weaning date, Litter size, Expected genotype |
| Sessions | **Project**, **Session name**, Description, Date/time, Tags, Data storage, Name in storage, Extra content, Repository links |
| Behaviors | **Session**, **Subjects**, **Setup**, **Behavioral assay** (an assay with the same setup type as the setup), Notes |
| Data Acquisition | **Session**, **Data acquisition type**, **Experimental interfaces** (on the session's subjects or specimen sets, of a type the acquisition type allows), Setup, Equipment, Notes, Schema |
| Manipulations | **Session**, **Manipulation type**, **Experimental interfaces**, Setup, Equipment, Notes, Schema |
| Cohorts | **Project**, **Cohort name**, **Subjects**, Description, Tags |
| Collections | **Project**, **Collection name**, **Sessions**, Description, Tags |

Procedure types that place something in the brain require a coordinate system; only the systems the procedure form itself offers for that type are listed.

### Validating
{: .no_toc}

Click **Validate current tab**. Every row gets a status pill and the panel shows a summary line "Create: N · Existing skipped: N · Entries: N · Warnings: N · Blocked: N".

| Status | Meaning |
|--------|---------|
| **new** | "A new record will be created." |
| **existing** | "A matching record already exists and will be skipped." |
| **entry** | "A new entry will be added to the existing record." (log entries) |
| **blocked** | "This row has errors that prevent import." The message is shown under the cell, for example "This field is required.", "The value is too long." or "This name is unavailable or you do not have permission to use it." |
| **draft** | "Not validated yet." |

"All rows are ready to import." means every row is new, existing or entry. "Resolve the blocking row errors before importing." means at least one row is blocked. Validate again after changing rows; the import checks every row once more before writing.

### Importing
{: .no_toc}

**Import valid rows** is enabled once the current panel has been validated without blocked rows. A dialog asks **Import the validated rows now?** ("The validated rows are imported into BrainSTEM."); click **Import**. The panel reports "Import completed successfully. The draft was cleared." and the new entries are offered in the dropdowns of the other panels right away, for example a new project in a pinned Subjects grid. If the import fails, the row results show the reason and the draft is kept.

## CSV import

The **CSV import** tab has three sections: **Projects**, **Subjects** and **Sessions**. Each section offers templates, a field reference and an upload area.

![The CSV import tab: the three steps (download a template, prepare your data, upload and review), the recommended order (projects, subjects, sessions, then related data), and the Projects section with its template, field reference and upload area.]({{site.baseurl}}/assets/images/screenshots/import-tool-csv.png)
{: .screenshot }
*The CSV import tab: the three steps (download a template, prepare your data, upload and review), the recommended order (projects, subjects, sessions, then related data), and the Projects section with its template, field reference and upload area.*

### Steps
{: .no_toc}

1. Under **Download a CSV template**, click the template for the kind of entry you want to create. The file is named `brainstem_template_<kind>.csv` and holds the column headers and one or more example rows (one per type for procedures, subject logs, data acquisition and manipulations).
2. Open the file in a spreadsheet program, replace the example rows with your data and keep the headers unchanged. Save as CSV (UTF-8).
3. Drag the file onto **Click or drag file here** in the matching section, or click to select it. Only `.csv` files up to 10 MB are accepted. The area shows "CSV file ready" with the file name.
4. Click the import button that matches the template: **Import Projects**, **Import Subjects**, **Import Procedures**, **Import Subject Logs**, **Import Cohorts**, **Import Sessions**, **Import Behaviors**, **Import Data Acquisition**, **Import Manipulations**, **Import Epochs** or **Import Collections**.
5. Read **Import Results**: **Import Successful!** or **Import Completed with Warnings!** with counters such as "3 Subjects Created" and "1 Projects Found", followed by the **Warnings** and **Errors** lists with row numbers. If a row fails, the later rows are still processed.

{: .important }
> CSV import has no preview: valid rows are created as soon as you click the import button. Try a file with two or three rows first, then upload the rest.

### Templates
{: .no_toc}

| Section | Templates | Import in this order |
|---------|-----------|----------------------|
| **Projects** | **Projects Template** | First |
| **Subjects** | **Subjects Template**, **Procedures Template**, **Subject Logs Template**, **Cohorts Template** | Subjects, then procedures and subject logs, then cohorts |
| **Sessions** | **Sessions Template**, **Behaviors Template**, **Data Acquisition Template**, **Manipulations Template**, **Epochs Template**, **Collections Template** | Sessions, then behaviors, data acquisition and manipulations, then epochs and collections |

Breedings and log entries for existing logs are created through batch entry; the CSV tab has no template for them.

### Columns
{: .no_toc}

Headers follow the pattern `<kind>__<field>`, for example `project__name` or `subject__birth_date`. Unknown columns are ignored. The **field reference** under each section (click the heading to expand it) describes every column of the section's templates. The columns a row cannot do without:

| Template | Columns that must be filled |
|----------|-----------------------------|
| Projects | `project__name` |
| Subjects | `project__name`, `subject__name`, `subject__species` |
| Procedures | `subject__name`, `procedure__type` |
| Subject Logs | `subject__name`, `subject_log__type`, and `subject_log__entry_datetime` (or `subject_log__entry_start_datetime` for ranged log types) when the row adds an entry |
| Cohorts | `project__name`, `cohort__name`, `cohort__subjects` |
| Sessions | `project__name`, `session__name` |
| Behaviors | `session__name`, `subject__name`, `behavior__setup_id`, `behavior__behavioralassay_id` |
| Data Acquisition | `session__name`, `data_acquisition__type`, `data_acquisition__interfaces` |
| Manipulations | `session__name`, `manipulation__type`, `manipulation__interfaces` |
| Epochs | `session__id` (or `project__name` and `session__name`), `epoch__name` |
| Collections | `project__name`, `collection__name`, `collection__sessions` |

A subject without `subject__sex` is imported as Unknown and without `subject__status` as Active. A procedure row creates one procedure; a subject log row adds an entry to the subject's log of that type and creates the log when there is none; a cohort or collection row adds the listed subjects or sessions to an existing cohort or collection of that name in the project.

### How to write values
{: .no_toc}

| Kind of value | Write it as |
|---------------|-------------|
| Related entry | Its exact name (`Mouse_001`, `Session_20230601`). Names are matched exactly, including case. Setups, behavioral assays, data storages, experimental interfaces, equipment, breedings, licenses, consumable stock and the epoch links are given by ID instead, see below. |
| Several related entries | Comma-separated in one cell: `Mouse_001, Mouse_002`. Several data acquisitions or manipulations on one epoch are separated by `;`. |
| Tags | Comma-separated: `training, cohortA` |
| Yes or no | `true` or `false` (also `yes`/`no`, `1`/`0`) |
| Date | `2024-05-01` |
| Date and time | `2024-05-01 14:30` or `2024-05-01 14:30:00` |
| Epoch start and end | Time since the start of the session: `00:05:00` or `PT5M` |
| Type code | The type as shown in the API, for example `VirusInjection`, `Weighing`, `ExtracellularEphys`, `OptogeneticStimulation`. The template examples list one row per type. |
| Coordinate system | `Stereotaxic_BregmaBrainSurface`, `Stereotaxic_BregmaAbsolute` or another code from the [Coordinate systems]({{"datamodel/schemas/coordinates/"|absolute_url}}) page |
| Type-specific details, coordinates, log entry data | A JSON object in one cell, as in the template example for that type. A cell that is not valid JSON is skipped with a warning. |
| Materials of a procedure | `procedure__materials`: a JSON list as in the template example, one object per material with its type and a consumable stock, catalog consumable or manual name |
| Description | Plain text; simple formatting (paragraphs, bold, italics, links) is kept |

#### Finding an ID
{: .no_toc}

Some columns end in `_id` and take the identifier of an existing entry (`behavior__setup_id`, `session__data_storage__id`, `subject__breeding_id`, `epoch__dataacquisition_id`, …). Open the entry and copy the long identifier from the address bar of the browser, or from the **API** button on its details page. In batch entry these entries are chosen from dropdowns, so IDs are only needed for CSV files.

### Warnings and errors
{: .no_toc}

- A missing required column stops that row with an error; the other rows are still imported.
- A related entry that cannot be found stops the row when it is required (the project, subject or session) and is dropped with a warning when it is optional (a strain, supplier, target region or equipment item).
- An invalid date, time or JSON value is dropped with a warning and the rest of the row is imported.
- Rows that match an existing entry are counted as found, not created. A log entry at a date and time that already exists is reported as a warning.

## Limits

| Limit | Value |
|-------|-------|
| Rows per batch grid | 500 |
| CSV file size | 10 MB, `.csv` only |
| Name length | 100 characters for subjects, sessions, breedings, cohorts and collections; 200 for projects |
| Notes | 500 characters on procedures, data acquisition and manipulations |

## Related

- [Subjects]({{"datamodel/stem/subject/"|absolute_url}}), [Sessions]({{"datamodel/stem/session/"|absolute_url}}) and [Procedures]({{"datamodel/modules/procedure/"|absolute_url}}): the fields the templates and grids fill
- [Experimental interfaces]({{"datamodel/modules/experimentalinterface/"|absolute_url}}): what a data acquisition or manipulation row must point to
- [SoftMouse integration]({{"webinterface/softmouse/"|absolute_url}}): importing colony records instead of typing them
- [Python API tool]({{"tools/python-api-tool/"|absolute_url}}) and [MATLAB API tool]({{"tools/matlab-api-tool/"|absolute_url}}): scripted imports beyond the supported record types
- [Active projects]({{"webinterface/list-view/#active-projects"|absolute_url}}): the project scope switch
