# Bridging-literature-and-model
Bridging literature and models: a workflow for harmonizing agricultural datasets for simulation model using AI

# Summary of the Codebase and Data

## Overview

This project is a **scientific data extraction pipeline** that uses **Large Language Models (LLMs)** — specifically fine-tuned OpenAI GPT models — to automatically extract structured crop experiment metadata from scientific PDF papers. The extracted data is mapped to the **ICASA (International Consortium for Agricultural Systems Applications)** standard, making it **FAIR** (Findable, Accessible, Interoperable, Reusable) for use in crop modeling and agronomy research. The project is part of the **FAIRagro** initiative at **ZALF (Leibniz Centre for Agricultural Landscape Research)**.

---

## Dataset

- **55 crop modeling papers** are used in total (see `00_paper_list/paper_list.txt`):
  - **45 papers** → used for **training** (fine-tuning the LLM)
  - **10 papers** → used for **evaluation**
- Papers cover a wide range of crops (wheat, maize, soybean, sorghum, barley, etc.) and topics (yield simulation, CO₂ enrichment, irrigation, nitrogen management, soil carbon, etc.)

---

## Folder Structure

| Folder / File | Description |
|---|---|
| `00_paper_list/` | List of 55 publications used in the study (45 training + 10 evaluation) |
| `01_scripts/python/` | Python scripts implementing the full pipeline (Steps 1–3) |
| `01_scripts/R/` | R scripts (one per ICASA category) that generate training data and ground-truth JSON files |
| `02_icasa_template/icasa_template_allColumns.xlsm` | Excel template with ICASA variable definitions used for manual extraction and as LLM prompt reference |
| `03_training_data/` | JSONL fine-tuning datasets — one `.jsonl` per category (45 training + 10 evaluation pairs) |
| `04_manual_json/` | Manually extracted ground-truth JSON files — one file per paper per ICASA category |
| `05_manual_tabular/` | Manual extraction results in tabular Excel format — one `.xlsx` per paper |
| `06_llm_output_json/` | LLM-generated structured JSON outputs — one file per paper per category |
| `07_llm_output_tabular/` | LLM outputs in tabular form — one `.xlsx` per category, compared against `05_manual_tabular/` |
| `docs/` | Pipeline documentation and data flow diagrams |

---

## Pipeline Workflow (Step by Step)

### Step 1 — PDF to Markdown (`01_scripts/python/step1_pdf_to_markdown.py`)
- Uses the **`marker`** tool (a PDF-to-Markdown converter) to convert scientific PDF papers into Markdown text files.
- Input: folder of PDF papers
- Output: folder of Markdown files

### Step 2 — Markdown Preprocessing (steps 2.1–2.7, in `01_scripts/python/`)
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

### R Scripts — Training Data Generation (`01_scripts/R/`)
Eight R scripts (one per ICASA category) read the enriched Markdown files and the ICASA Excel template, then produce:
- `04_manual_json/` — ground-truth JSON files (one per paper per category)
- `03_training_data/` — JSONL fine-tuning datasets (one per category)

### Step 3 — LLM Structured Extraction (`01_scripts/python/step3_llm_extract_icasa_variables.py`)
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

## Fine-Tuning Approach

- **Training data** (folder `03_training_data/`): JSONL files where each record contains a paper's extracted Markdown text as input and the manually curated ICASA-structured JSON as the expected output.
- The model is fine-tuned separately for each ICASA category.
- After fine-tuning, the model is applied to all 55 papers to generate automatic extractions (folders `06_llm_output_json/` and `07_llm_output_tabular/`).
- Results are compared against the manual extractions (folders `04_manual_json/` and `05_manual_tabular/`) for evaluation.

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
