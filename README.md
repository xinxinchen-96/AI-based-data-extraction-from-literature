# AI-based data extraction from literature
AI-based data extraction from literature

# Summary of the codebase and data

## Overview

This project is a **scientific data extraction pipeline** that uses **Large Language Models (LLMs)**, specifically fine-tuned OpenAI GPT models to automatically extract structured crop experiment metadata from scientific PDF papers. The extracted data is mapped to the **ICASA (International Consortium for Agricultural Systems Applications)** standard, making it **FAIR** (Findable, Accessible, Interoperable, Reusable) for use in crop modeling and agronomy research. The project is part of the **FAIRagro** initiative at **ZALF (Leibniz Centre for Agricultural Landscape Research)**.

---

## Dataset

- **55 crop modeling papers** are used in total (see `00_paper_list/paper_list.csv`):
  - **45 papers** are used for **training** (fine-tuning the LLM)
  - **10 papers** are used for **validation**
- Papers cover a wide range of crops (wheat, maize, soybean, sorghum, barley, etc.) and topics (yield simulation, CO₂ enrichment, irrigation, nitrogen management, soil carbon, etc.)

---

## Folder structure

| Folder | Description |
|--------|-------------|
| `R/` | R scripts (one per ICASA category) that generate training data and ground-truth JSON files |
| `python/` | Python scripts implementing the full pipeline (Steps 1–4) |
| `R_env/` | R environment dependencies and package configurations |
| `data/00_paper_list/` | List of 55 publications used in the study (45 training + 10 validation), see `paper_list.csv` |
| `data/01_paper_to_md/` | 55 publications of PDF covert to markdown format|
| `data/02_final_processed_md/` | Final processed Markdown versions of the publications |
| `data/03_icasa_template/` | Excel template with ICASA variable definitions used for manual extraction and as LLM prompt reference |
| `data/04_manual_json/` | Manually extracted ground-truth JSON files; one file per paper per ICASA category |
| `data/05_manual_tabular/` | Manual extraction results in tabular Excel format; one `.xlsx` per paper |
| `data/06_training_data/` | JSONL fine-tuning datasets, one `.jsonl` per category (45 training + 10 validation pairs) |
| `data/07_llm_output_json/` | LLM-generated structured JSON outputs; one file per paper per category |
| `data/08_llm_output_tabular/` | LLM outputs in tabular form; one `.xlsx` per category, compared against `05_manual_tabular/` |
---

## Pipeline workflow

### Full pipeline diagram

```
                                    [INPUT] PDF papers
                                           |
                                           v
                             +----------------------------+
                             |  STEP 1: pdf → markdown    |
                             |  step1_pdf_to_markdown.py  |
                             +----------------------------+
                                          |
                                  [OUT] 01_paper_to_md/
                                          |
                                          v
                             +------------------------------+
                             |  STEP 2: process paper       |
                             |  step2_process_paper.py      |
                             |                              |
                             |  · extract specificsection   |
                             +------------------------------+
                                          |
                         [OUT] 02_final_processed_md/  ◄─────────────────────────────────┐
                                          |                                              │
                  ┌───────────────────────┘                                              │
                  │                                                                      │
                  v                                                                      │
  +-----------------------------+                                                        │
  |  03_icasa_template/         |  ← Created by colleague, based on ICASA dictionary     │
  |  ICASA variable schema      |    (Excel workbook with variable definitions           │
  |  (Excel .xlsm)              |     and tick-boxes for inclusion/exclusion)            │
  +-----------------------------+                                                        │
                  |                                                                      │
                  v                                                                      │
  +---------------------------------------------------------+                            │
  |  R SCRIPTS  (R/)                                        |  ←─────────────────────────┘
  |  assemble_training_set.R                                |     (also reads enriched .md)
  |                                                         |
  |  Input:  03_icasa_template  +  02_final_processed_md/   |
  |  Output A → 04_manual_json/   (one JSON per paper)      |
  |  Output B → 06_training_data/ (one JSONL per category)  |
  |                                                         |
  |  Categories:                                            |
  |    context_metadata · fields · genotypes · plantings    |
  |    irrigations · fertilizers · harvests · plot_details  |
  +---------------------------------------------------------+
                  |                         |
                  v                         v
  +---------------------------+   +-------------------------------+
  |  04_manual_json/          |   |  06_training_data/            |
  |  Ground-truth JSON files  |   |  JSONL fine-tuning datasets   |
  |  (one JSON per paper,     |   |  (one .jsonl per category,    |
  |   per category)           |   |   55 items each:              |
  |                           |   |   45 training + 10 validation)|
  +---------------------------+   +-------------------------------+
                  |                         |
                  v                         v
  +---------------------------+   +-------------------------------+
  |  R SCRIPTS  (R/)          |   |  [OpenAI Platform]            |
  |  json_to_xlsx.R           |   |  Upload JSONL → fine-tune     |
  +---------------------------+   |  GPT model (one per category) |
                  |               |  → returns fine-tuned         |
                  v               |    model ID                   |
  +---------------------------+   +-------------------------------+
  |  05_manual_tabular/       |               |
  |  Manual extractions in    |               v
  |  tabular Excel format     |   +-----------------------------+
  |  (one .xlsx per paper,    |   |  STEP 3                     |
  |   all categories combined)|   |  step3_llm_extract_         |
  +---------------------------+   |  icasa_variables.py         |
                  |               |                             |
                  |               |  Input: 02_final_processed_ |
                  |               |    md/ + ICASA Excel schema |
                  |               |       + fine-tuned model ID |
                  |               |  Calls OpenAI API           |
                  |               +-----------------------------+
                  |                         |
                  |                         v
                  |             +-----------------------------+
                  |             |  07_llm_output_json/        |
                  |             |  LLM-generated JSON files   |
                  |             |  (one file per paper,       |
                  |             |   per category)             |
                  |             +-----------------------------+
                  |                         |
                  |                         v
                  |             +-----------------------------+
                  |             |  R SCRIPTS  (R/)            |
                  |             |  convert json to tabular_*  |
                  |             +-----------------------------+
                  |                         |
                  |                         v
                  |             +-----------------------------+
                  |             |  08_llm_output_tabular/     |
                  |             |  LLM outputs in tabular     |
                  |             |  Excel format               |
                  |             |  (one .xlsx per category)   |
                  |             +-----------------------------+
                  |                         |
                  +──────────────► compare ◄+
                                       |
                   +-----------------------------+
                   |  STEP 4                     |
                   |  step4_evaluation.py        |
                   |                             |
                   |  05_manual_tabular  vs      |
                   |  08_llm_output_tabular      |
                   +-----------------------------+
```

---

### Step-by-Step description

#### Step 1. PDF to Markdown (`py/step1_pdf_to_markdown.py`)
- Uses the **`marker`** tool (a PDF-to-Markdown converter) to convert scientific PDF papers into Markdown text files.
- Input: folder of PDF papers
- Output: 01_paper_to_md

#### Step 2. Markdown preprocessing (step2_process_paper.py, in `py/`)
A script that clean and proces the Markdown files:
Output: 02_final_processed_md (enriched markdown files containing methods text, relevant tables, author names, and publication year which are ready for LLM processing).

#### R Scripts: Training data generation (`R/assemble_training_set.R`)

**Inputs:**
- `03_icasa_template/icasa_template_allColumns.xlsm` is the Excel workbook (filled in manually for each paper)
- the process markdown file in folder 02_final_processed_md

**Output A: Ground-truth JSON files (data/`04_manual_json/`):**
R script exports one JSON file per paper, capturing the manually extracted ICASA variables. These JSON files are the **ground truth**.The json files are convert to tabular files and output in the folders 05_manual_tabular

**Output B:JSONL training files (`data/06_training_data/`):**
The same R script pairs each enriched Markdown (user prompt) with the corresponding JSON (assistant response) to produce a JSONL file ready for OpenAI fine-tuning:
- **one-to-one** (recommended): each experimental year gets its own training pair that is smaller and more focused pairs.

#### Step 3. LLM structured extraction (`py/step3_llm_extract_icasa_variables.py`)
- Constructs structured prompts for each **ICASA data category**.
- Calls the **fine-tuned OpenAI GPT model**  via API.
- Saves the LLM responses as structured **JSON files** per paper per category.
- output:LLM extracted JSON files (data/`08_llm_output_tabular/`)

#### Step 4. manual and LLM extraction comparision (`py/step4_evaluation.py`)
-input:05_manual_tabular and 08_llm_output_tabular

## ICASA data categories extracted

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

The model is fine-tuned **separately for each of the 8 ICASA categories**, using 45 papers for training and 10 papers held out for validation.

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
