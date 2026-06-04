# Data Scripts Flow Summary — v3.0

> **Purpose of this document:** Refinement log for folder names, script names, and
> ICASA category naming applied before the repository was made public. The workflow order and blocks
> are unchanged from v2.0 (`Data_Scripts_Flow_Summary_updated.md`). All suggestions below have been applied.

---

## 1 — Suggested `01_scripts/` Restructure

### Current layout

```
01_scripts/
  step1_pdf_to_markdown.py
  step2_1_extract_method_sections.py
  step2_2_extract_tables_before_methods.py
  step2_3_combine_methods_and_tables.py
  step2_4_extract_authors.py
  step2_5_add_authors_to_combined.py
  step2_6_extract_publication_date.py
  step2_7_add_date_to_combined.py
  step3_llm_extract_icasa_variables.py
  R_scripts/
    create_text2icasa_training_set_xx_variables_renajson_expmetadata_...R
    create_text2icasa_training_set_xx_variables_renajson_fields_...R
    ... (8 files, long version-stamped names)
```

### Issues

- Python scripts and R scripts sit at different levels with no visual separation.
- R script names are very long, embed internal version stamps (`v050526`, `v125`), and
  contain a typo (`renajson` → unclear abbreviation) and a category misspelling
  (`fertilizeration`). These details are valuable internally but confuse external readers.
- `R_scripts/` is functional but inconsistent with Python naming style.

### Suggested layout

```
01_scripts/
  python/
    step1_pdf_to_markdown.py
    step2_1_extract_method_sections.py
    step2_2_extract_tables_before_methods.py
    step2_3_combine_methods_and_tables.py
    step2_4_extract_authors.py
    step2_5_add_authors_to_combined.py
    step2_6_extract_publication_date.py
    step2_7_add_date_to_combined.py
    step3_llm_extract_icasa_variables.py
  R/
    r_create_training_data_exp_metadata.R
    r_create_training_data_fields.R
    r_create_training_data_genotypes.R
    r_create_training_data_planting.R
    r_create_training_data_irrigation.R
    r_create_training_data_fertilization.R
    r_create_training_data_harvest.R
    r_create_training_data_plot_details.R
```

**Rationale:**

| Change | Reason |
|---|---|
| Add `python/` subfolder | Makes language separation immediately visible |
| Rename `R_scripts/` → `R/` | Shorter, consistent with `python/` |
| R scripts: prefix `r_create_training_data_` | Clear verb + language prefix; mirrors Python `step` convention |
| R scripts: use canonical category name | Consistent with the data folders (see Section 2) |
| Remove version stamps from filenames | Version control (git) tracks history; stamps clutter public names |

---

## 2 — Standardise ICASA Category Names Across All Folders

### Problem

The same 8 data categories are named differently across folders and files:

| Canonical name | `03_training_data/` | `04_manual_json/` subfolder | `06_llm_output_json/` subfolder | `07_llm_output_tabular/` subfolder |
|---|---|---|---|---|
| `exp_metadata` | `exp_metadata.jsonl` ✅ | `exp_metadata_json` ⚠️ | `exp_metadata` ✅ | `exp_metadata` ✅ |
| `fields` | `fields.jsonl` ✅ | `fields_json` ⚠️ | `fields` ✅ | `fields` ✅ |
| `genotypes` | `genotypes.jsonl` ✅ | `genotypes_json` ⚠️ | `genotype` ⚠️ | `genotype` ⚠️ |
| `planting` | `planting.jsonl` ✅ | `planting_json` ⚠️ | `planting` ✅ | `planting` ✅ |
| `irrigation` | `irrigation.jsonl` ✅ | `irrigation_json` ⚠️ | `irrigation` ✅ | `irrigation` ✅ |
| `fertilization` | `fertilizeration.jsonl` ❌ | `fertilizeration_json` ❌ | `fertilizer` ⚠️ | `fertilizer` ⚠️ |
| `harvest` | `harvest.jsonl` ✅ | `harvest_json` ⚠️ | `harvest` ✅ | `harvest` ✅ |
| `plot_details` | `plotdetils.jsonl` ❌ | `plotdetails_json` ⚠️ | `plot` ⚠️ | `plot` ⚠️ |

Legend: ✅ already correct · ⚠️ minor inconsistency · ❌ typo or significant mismatch

### Recommended canonical names (8 categories)

```
exp_metadata   fields   genotypes   planting
irrigation     fertilization   harvest   plot_details
```

### Specific renames needed

**`03_training_data/` (files)**

| Current | Suggested |
|---|---|
| `fertilizeration.jsonl` | `fertilization.jsonl` |
| `plotdetils.jsonl` | `plot_details.jsonl` |

**`04_manual_json/` (subfolders)**

| Current | Suggested |
|---|---|
| `exp_metadata_json` | `exp_metadata` |
| `fields_json` | `fields` |
| `genotypes_json` | `genotypes` |
| `planting_json` | `planting` |
| `irrigation_json` | `irrigation` |
| `fertilizeration_json` | `fertilization` |
| `harvest_json` | `harvest` |
| `plotdetails_json` | `plot_details` |

> The `_json` suffix in `04_manual_json/` subfolders is redundant — the parent folder name
> already conveys the format. Removing it makes subfolder names consistent with `06_llm_output_json/`.

**`06_llm_output_json/` and `07_llm_output_tabular/` (subfolders)**

| Current | Suggested |
|---|---|
| `genotype` | `genotypes` |
| `fertilizer` | `fertilization` |
| `plot` | `plot_details` |

---

## 3 — Minor Filename Refinements

### `02_icasa_template/`

| Current | Suggested | Reason |
|---|---|---|
| `2.0 template_icasa_vba_trainingSet_allColumns.xlsm` | `icasa_template_allColumns.xlsm` | Spaces in filenames cause issues on some systems; the `2.0` version prefix is redundant inside a versioned git repo |

### `00_paper_list/`

| Current | Suggested | Reason |
|---|---|---|
| `paper_list.txt` | `paper_list.txt` ✅ | Already clear — no change needed |

---

## 4 — `data/` Folder Clarification

The `data/` folder currently holds two subfolders (`01/` and `02/`) that contain working
drafts of this documentation and PDF exports. This is not obvious to external readers.

**Suggestion:** Either

- Remove `data/` entirely and consolidate all documentation in `docs/`, or
- Rename `data/` to `docs_archive/` and keep it for historical reference only.

---

## 5 — Summary of All Suggested Changes

| # | Item | Current | Suggested |
|---|---|---|---|
| 1 | `01_scripts/` structure | Python + `R_scripts/` mixed at root | Split into `python/` and `R/` subfolders |
| 2 | R script names | Long version-stamped names | `r_create_training_data_<category>.R` |
| 3 | `03_training_data/` files | `fertilizeration.jsonl`, `plotdetils.jsonl` | `fertilization.jsonl`, `plot_details.jsonl` |
| 4 | `04_manual_json/` subfolders | `<category>_json` | `<category>` (drop `_json` suffix) |
| 5 | `04_manual_json/fertilizeration_json` | typo + `_json` suffix | `fertilization` |
| 6 | `06_llm_output_json/` subfolders | `genotype`, `fertilizer`, `plot` | `genotypes`, `fertilization`, `plot_details` |
| 7 | `07_llm_output_tabular/` subfolders | same as above | same fix as above |
| 8 | `02_icasa_template/` filename | `2.0 template_icasa_vba_trainingSet_allColumns.xlsm` | `icasa_template_allColumns.xlsm` |
| 9 | `data/` folder | unclear purpose | rename to `docs_archive/` or merge into `docs/` |

---

## 6 — What to Keep Unchanged

- Top-level folder numbering (`00_`, `01_`, …, `07_`) — already logical and sequential. ✅
- Python script naming (`step1_`, `step2_1_`, … `step3_`) — clear and readable. ✅
- Workflow order and block structure — confirmed correct by owner. ✅
- `docs/` folder — good location for pipeline documentation. ✅
