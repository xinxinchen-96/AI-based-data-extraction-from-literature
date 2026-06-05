# Bridging-literature-and-model
Bridging literature and models: a workflow for harmonizing agricultural datasets for simulation model using AI

# Summary of the codebase and data

## Overview

This project is a **scientific data extraction pipeline** that uses **Large Language Models (LLMs)** — specifically fine-tuned OpenAI GPT models — to automatically extract structured crop experiment metadata from scientific PDF papers. The extracted data is mapped to the **ICASA (International Consortium for Agricultural Systems Applications)** standard, making it **FAIR** (Findable, Accessible, Interoperable, Reusable) for use in crop modeling and agronomy research. The project is part of the **FAIRagro** initiative at **ZALF (Leibniz Centre for Agricultural Landscape Research)**.

---

## Dataset

- **55 crop modeling papers** are used in total (see `00_paper_list/paper_list.csv`):
  - **45 papers** → used for **training** (fine-tuning the LLM)
  - **10 papers** → used for **evaluation**
- Papers cover a wide range of crops (wheat, maize, soybean, sorghum, barley, etc.) and topics (yield simulation, CO₂ enrichment, irrigation, nitrogen management, soil carbon, etc.)

---

## Folder Structure

| Folder / File | Description |
|---|---|
| `00_paper_list/` | List of 55 publications used in the study (45 training + 10 evaluation) — see `paper_list.csv` |
| `01_scripts/python/` | Python scripts implementing the full pipeline (Steps 1–3) |
| `01_scripts/R/` | R scripts (one per ICASA category) that generate training data and ground-truth JSON files |
| `02_icasa_template/icasa_template_allColumns.xlsm` | Excel template with ICASA variable definitions used for manual extraction and as LLM prompt reference |
| `03_training_data/` | JSONL fine-tuning datasets — one `.jsonl` per category (45 training + 10 evaluation pairs) |
| `04_manual_json/` | Manually extracted ground-truth JSON files — one file per paper per ICASA category |
| `05_manual_tabular/` | Manual extraction results in tabular Excel format — one `.xlsx` per paper |
| `06_llm_output_json/` | LLM-generated structured JSON outputs — one file per paper per category |
| `07_llm_output_tabular/` | LLM outputs in tabular form — one `.xlsx` per category, compared against `05_manual_tabular/` |

---

## Pipeline Workflow

### Full Pipeline Diagram

```
                                    [INPUT] PDF papers
                                           |
                                           v
                             +----------------------------+
                             |  STEP 1: pdf → markdown    |
                             |  step1_pdf_to_markdown.py  |
                             +----------------------------+
                                          |
                              [OUTPUT] Markdown files (.md)
                                          |
         +-----------------+--------------+--------------+------------------+
         v                 v              v              v                  v
  +--------------+  +--------------+      |      +-------------+  +-------------+
  |  STEP 2.1    |  |  STEP 2.2    |      |      |  STEP 2.4   |  |  STEP 2.6   |
  | extract      |  | extract      |      |      | extract     |  | extract     |
  | method       |  | tables       |      |      | authors     |  | pub. date   |
  | sections     |  | bef. method  |      |      |             |  |             |
  +--------------+  +--------------+      |      +-------------+  +-------------+
         |                  |             |              |                  |
  [OUT] *_results.md [OUT] *_tables.md    |      [OUT] *_authors.md [OUT] *_dates.md
         |                  |             |              |                  |
         +--------+---------+             |              |                  |
                  v                       |              |                  |
         +--------------+                 |              |                  |
         |  STEP 2.3    |                 |              |                  |
         | combine      |                 |              |                  |
         | methods +    |                 |              |                  |
         | tables       |                 |              |                  |
         +--------------+                 |              |                  |
                  |                       |              |                  |
         [OUT] combined.md                |              |                  |
                  |                       |              |                  |
                  +-----------------------+--------------+                  |
                                          |                                 |
                                          v                                 |
                              +----------------------------+                |
                              |  STEP 2.5                  |                |
                              |  add authors to combined   |                |
                              +----------------------------+                |
                                          |                                 |
                              [OUT] combined + authors .md                  |
                                          |                                 |
                                          +---------------------------------+
                                          |
                                          v
                              +----------------------------+
                              |  STEP 2.7                  |
                              |  add date to combined      |
                              +----------------------------+
                                          |
                              [OUT] FINAL enriched .md  ◄─────────────────────────────────┐
                                          |                                               │
                  ┌───────────────────────┘                                               │
                  │                                                                       │
                  v                                                                       │
  +-----------------------------+                                                         │
  |  02_icasa_template/         |  ← Created by colleague, based on ICASA dictionary      │
  |  ICASA variable schema      |    (Excel workbook with variable definitions            │
  |  (Excel .xlsm)              |     and tick-boxes for inclusion/exclusion)             │
  +-----------------------------+                                                         │
                  |                                                                       │
                  v                                                                       │
  +---------------------------------------------------------+                             │
  |  R SCRIPTS  (01_scripts/R/)                             |  ←──────────────────────────┘
  |  8 scripts, one per ICASA category:                     |     (also reads enriched .md)
  |                                                         |
  |  Input:  02_icasa_template  +  FINAL enriched .md       |
  |  Output A → 04_manual_json/   (one JSON per paper)      |
  |  Output B → 03_training_data/ (one JSONL per category)  |
  |                                                         |
  |  Categories:                                            |
  |    exp_metadata · fields · genotypes · planting         |
  |    irrigation · fertilization · harvest · plot_details  |
  +---------------------------------------------------------+
                  |                         |
                  v                         v
  +---------------------------+   +-------------------------------+
  |  04_manual_json/          |   |  03_training_data/            |
  |  Ground-truth JSON files  |   |  JSONL fine-tuning datasets   |
  |  (one JSON per paper,     |   |  (one .jsonl per category,    |
  |   per category)           |   |   55 items each:              |
  |                           |   |   45 training + 10 evaluation)|
  +---------------------------+   +-------------------------------+
                  |                         |
                  v                         v
  +---------------------------+   +-------------------------------+
  |  05_manual_tabular/       |   |  [OpenAI Platform]            |
  |  Manual extractions in    |   |  Upload JSONL → fine-tune     |
  |  tabular Excel format     |   |  GPT model (one per category) |
  |  (one .xlsx per paper,    |   |  → returns fine-tuned         |
  |   all categories combined)|   |    model ID                   |
  +---------------------------+   +-------------------------------+
                  |                         |
                  |                         v
                  |             +-----------------------------+
                  |             |  STEP 3                     |
                  |             |  step3_llm_extract_         |
                  |             |  icasa_variables.py         |
                  |             |                             |
                  |             |  Input: FINAL enriched .md  |
                  |             |       + ICASA Excel schema  |
                  |             |       + fine-tuned model ID |
                  |             |  Calls OpenAI API           |
                  |             +-----------------------------+
                  |                         |
                  |         +---------------+---------------+
                  |         v                               v
                  |  [OUT] 06_llm_output_json/    [OUT] 07_llm_output_tabular/
                  |  <cat>/<paper>_<cat>.json          <category>.xlsx
                  |                                         |
                  +──────────────────► compare ◄────────────+
                                           |
                             (07_llm_output_tabular  vs  05_manual_tabular)
```

---

### Step-by-Step Description

#### Step 1 — PDF to Markdown (`01_scripts/python/step1_pdf_to_markdown.py`)
- Uses the **`marker`** tool (a PDF-to-Markdown converter) to convert scientific PDF papers into Markdown text files.
- Input: folder of PDF papers
- Output: folder of Markdown files

#### Step 2 — Markdown Preprocessing (steps 2.1–2.7, in `01_scripts/python/`)
A series of scripts that clean and enrich the Markdown files:

| Script | Purpose |
|---|---|
| `step2_1_extract_method_sections.py` | Extract **Methods sections** from Markdown |
| `step2_2_extract_tables_before_methods.py` | Extract **tables appearing before** the Methods section |
| `step2_3_combine_methods_and_tables.py` | Combine tables-before-methods + methods sections |
| `step2_4_extract_authors.py` | Extract **author names** from Markdown |
| `step2_5_add_authors_to_combined.py` | Add author info to the combined content |
| `step2_6_extract_publication_date.py` | Extract **publication/corresponding date** from Markdown |
| `step2_7_add_date_to_combined.py` | Add year/date info to the combined content |

Output: enriched Markdown files containing methods text, relevant tables, author names, and publication year — ready for LLM processing.

#### R Scripts — Training Data Generation (`01_scripts/R/`)

The 8 R scripts (one per ICASA category) serve a **dual purpose** — they are the core data-preparation tools, not simple converters.

**Inputs:**
- `02_icasa_template/icasa_template_allColumns.xlsm` — the Excel workbook (filled in manually for each paper/year)
- FINAL enriched `.md` files — the tokenised PDFs from Step 2.7

**Output A — Ground-truth JSON files (`04_manual_json/`):**
Each R script exports one JSON file per paper (and per experimental year where applicable), capturing the manually extracted ICASA variables. These JSON files are the **ground truth**.

**Output B — JSONL training files (`03_training_data/`):**
The same R script pairs each enriched Markdown (user prompt) with the corresponding JSON (assistant response) to produce a JSONL file ready for OpenAI fine-tuning. Two pairing strategies are available:
- **one-to-one** (recommended): each experimental year gets its own training pair — smaller, more focused pairs.
- **one-to-many**: all years from one paper are bundled into a single training pair.

#### Step 3 — LLM Structured Extraction (`01_scripts/python/step3_llm_extract_icasa_variables.py`)
- Reads the enriched Markdown files and the ICASA Excel template.
- Constructs structured prompts for each **ICASA data category**.
- Calls the **fine-tuned OpenAI GPT model** (e.g., `gpt-4.1-mini`) via API.
- Saves the LLM responses as structured **JSON files** per paper per category.

---

## ICASA Data Categories Extracted

The pipeline extracts data across **8 ICASA-standard categories**:

| Category | Description |
|---|---|
| `exp_metadata` | Experiment metadata (location, dates, objectives) |
| `fields` | Soil and field characteristics |
| `genotypes` | Crop cultivar/genotype information |
| `planting` | Sowing/planting details |
| `irrigation` | Irrigation management |
| `fertilization` | Fertilizer application details |
| `harvest` | Harvest data and yield observations |
| `plot_details` | Plot-level experimental design details |

---

## Fine-Tuning

Before Python Step 3 can run, the JSONL training data must be uploaded manually to the **OpenAI platform**:

1. Upload each category's `.jsonl` file to [platform.openai.com → Fine-tuning](https://platform.openai.com/finetune).
2. Start a fine-tuning job for each category.
3. Once training completes, copy the resulting **fine-tuned model ID** (e.g., `ft:gpt-4.1-mini-2025-04-14:personal:exp-v040526:DbkEyIz7`).
4. Paste the model IDs into the `FINE_TUNED_MODELS` dictionary in `step3_llm_extract_icasa_variables.py`.

The model is fine-tuned **separately for each of the 8 ICASA categories**, using 45 papers for training and 10 papers held out for evaluation.

---

## Evaluation

After Step 3 runs, the LLM outputs are converted to tabular form and compared against the manual baseline:

- `06_llm_output_json/` → converted to `07_llm_output_tabular/` (one `.xlsx` per category)
- `07_llm_output_tabular/` is compared against `05_manual_tabular/` (human baseline)

This comparison measures how well the fine-tuned LLM reproduces the manual extraction results.

---

## Technology Stack

| Component | Tool / Library |
|---|---|
| PDF → Markdown | `marker` (Python CLI tool) |
| LLM API | OpenAI GPT (fine-tuned, e.g., `gpt-4.1-mini`) |
| Data standard | ICASA (International Consortium for Agricultural Systems Applications) |
| Scripting | Python, R |
| Data storage | JSON, JSONL, Excel (`.xlsx`, `.xlsm`) |
| Initiative | FAIRagro / ZALF |

---

## Key Goal

> Automate the extraction of structured, ICASA-compliant crop experiment data from scientific literature using fine-tuned LLMs, reducing manual curation effort while maintaining data quality for use in crop modeling and agricultural research.
