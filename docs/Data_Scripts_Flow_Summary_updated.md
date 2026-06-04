# Data Flow Summary (Updated)

> **Changes from original:** Incorporates colleague feedback — added R script role in
> generating `04_manual_json` and `03_training_data`, added OpenAI fine-tuning upload step,
> clarified the `05_manual_tabular` generation path, and corrected comparison direction.

---

## Full Pipeline Diagram

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
                                          |                                                │
                  ┌───────────────────────┘                                                │
                  │                                                                        │
                  v                                                                        │
  +-----------------------------+                                                          │
  |  02_icasa_template/         |  ← Created by colleague, based on ICASA dictionary       │
  |  ICASA variable schema      |    (Excel workbook with variable definitions             │
  |  (Excel .xlsm)              |     and tick-boxes for inclusion/exclusion)              │
  +-----------------------------+                                                          │
                  |                                                                        │
                  v                                                                        │
  +---------------------------------------------------------+                             │
  |  R SCRIPTS  (01_scripts/R_scripts/)                     |  ←──────────────────────────┘
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
                  |             +----------------------------+
                  |             |  STEP 3                    |
                  |             |  step3_llm_extract_        |
                  |             |  icasa_variables.py        |
                  |             |                            |
                  |             |  Input: FINAL enriched .md |
                  |             |       + ICASA Excel schema  |
                  |             |       + fine-tuned model ID |
                  |             |  Calls OpenAI API          |
                  |             +----------------------------+
                  |                         |
                  |         +---------------+---------------+
                  |         v                               v
                  |  [OUT] 06_llm_output_json/    [OUT] 07_llm_output_tabular/
                  |  <cat>/<paper>_<cat>.json          <category>.xlsx
                  |                                         |
                  +──────────────────► compare ◄───────────+
                                           |
                             (07_llm_output_tabular  vs  05_manual_tabular)
```

---

## Folder / File Reference

| Folder / File | Description |
|---|---|
| `00_paper_list/` | List of 55 publications used in the study (45 training + 10 evaluation) |
| `01_scripts/python/` | Python scripts implementing the full pipeline (Steps 1–3) |
| `01_scripts/R/` | **8 R scripts** (one per ICASA category) — read ICASA Excel template and enriched Markdown files; produce `04_manual_json` JSON files and `03_training_data` JSONL files |
| `02_icasa_template/icasa_template_allColumns.xlsm` | ICASA variable schema as Excel workbook. Created by colleague based on the ICASA dictionary (available at [DSSAT/ICASA-Dictionary](https://github.com/DSSAT/ICASA-Dictionary)). Read at runtime by both R scripts and Python Step 3. |
| `03_training_data/` | JSONL fine-tuning datasets — one `.jsonl` per category, each with 55 conversation pairs (messages: user = enriched Markdown, assistant = structured JSON). Uploaded to OpenAI platform to fine-tune the GPT model. |
| `04_manual_json/` | Ground-truth JSON extractions — one JSON file per paper per category, produced by the R scripts from the filled-in Excel template. Used as the target (assistant) output in the JSONL training files. |
| `05_manual_tabular/` | Manual extraction results in tabular form — one `.xlsx` per paper with all categories combined. Derived from `04_manual_json`. Serves as human-baseline for evaluation. |
| `06_llm_output_json/` | LLM-generated structured JSON outputs — one file per paper per category, organized in per-category subfolders. |
| `07_llm_output_tabular/` | LLM outputs in tabular form — one `.xlsx` per category. Compared against `05_manual_tabular` for quality evaluation. |

---

## R Script Role (New — clarified by colleague)

The 8 R scripts in `01_scripts/R_scripts/` serve a **dual purpose** — they are not simple converters but the core data-preparation tools:

### Inputs
- `02_icasa_template/` — the Excel workbook (filled in manually for each paper/year)
- `FINAL enriched .md` files — the tokenized PDFs from Step 2.7

### Output A — Individual JSON files (`04_manual_json/`)
Each R script exports one JSON file per paper (and per experimental year where applicable), capturing the manually extracted ICASA variables for that paper. These JSON files are the **ground truth**.

### Output B — JSONL training files (`03_training_data/`)
The same R script pairs each enriched Markdown (user prompt) with the corresponding JSON (assistant response) to produce a JSONL file ready for OpenAI fine-tuning. Two pairing strategies are available:
- **one-to-one** (recommended): each experimental year gets its own training pair — smaller individual pairs, more focused learning.
- **one-to-many**: all years from one paper are bundled into a single training pair.

---

## Fine-Tuning Step (New — clarified by colleague)

Before Python Step 3 can run, the JSONL training data must be uploaded manually to the **OpenAI platform**:

1. Upload each category's `.jsonl` file to [platform.openai.com → Fine-tuning](https://platform.openai.com/finetune).
2. Start a fine-tuning job for each category.
3. Once training completes, copy the resulting **fine-tuned model ID** (e.g., `ft:gpt-4.1-mini-2025-04-14:personal:exp-v040526:DbkEyIz7`).
4. Paste the model IDs into the `FINE_TUNED_MODELS` dictionary in `step3_llm_extract_icasa_variables.py`.

---

## Evaluation / Comparison

After Step 3 runs:

- `06_llm_output_json/` → converted to `07_llm_output_tabular/` (one `.xlsx` per category)
- `07_llm_output_tabular/` is compared against `05_manual_tabular/` (human baseline)

This comparison measures how well the fine-tuned LLM reproduces the manual extraction results.

---

## Naming — Standardised (applied)

All category names are now consistent across folders and files:

| Category | `03_training_data/` | `04_manual_json/` subfolder | `06_llm_output_json/` subfolder | `07_llm_output_tabular/` subfolder |
|---|---|---|---|---|
| `exp_metadata` | `exp_metadata.jsonl` | `exp_metadata` | `exp_metadata` | `exp_metadata` |
| `fields` | `fields.jsonl` | `fields` | `fields` | `fields` |
| `genotypes` | `genotypes.jsonl` | `genotypes` | `genotypes` | `genotypes` |
| `planting` | `planting.jsonl` | `planting` | `planting` | `planting` |
| `irrigation` | `irrigation.jsonl` | `irrigation` | `irrigation` | `irrigation` |
| `fertilization` | `fertilization.jsonl` | `fertilization` | `fertilization` | `fertilization` |
| `harvest` | `harvest.jsonl` | `harvest` | `harvest` | `harvest` |
| `plot_details` | `plot_details.jsonl` | `plot_details` | `plot_details` | `plot_details` |
