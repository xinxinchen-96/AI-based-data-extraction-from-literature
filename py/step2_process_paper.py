# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 11:28:17 2026

@author: xinxin
"""

# -*- coding: utf-8 -*-
"""
Step 2 — Unified Sequential Pipeline
 
Pipeline:
    2.1  Extract "Materials and Methods" section
    2.2  Extract tables before Methods
    2.3  Combine 2.1 + 2.2                        → results_1_0
    2.4  Extract author block
    2.5  Combine 2.4 + results_1_0                → results_2_0
    2.6  Extract publication date
    2.7  Combine 2.6 + results_2_0                → results_3_0/  ← FINAL OUTPUT
    
Usage: python3 step2_process_paper.py -i INPUT_FOLDER -o OUTPUT_FOLDER

Arguments:
  -i, --input_folder    Step 1 output
  -o, --output_folder   Folder for all intermediate + final output

Example:
  python3 step2_process_paper.py -i ./step1_output -o ./results
"""


import os
import re
import argparse

parser = argparse.ArgumentParser("process_paper")
parser.add_argument("-i", "--input_folder", help="Step 1 output", required=True)
parser.add_argument(
    "-o",
    "--output_folder",
    help="Folder for all intermediate + final output",
    required=True,
)

args = parser.parse_args()

# =============================================================================
# === USER CONFIG =============================================================
# =============================================================================
INPUT_MD_FOLDER: str = args.input_folder  # Step 1 output
OUTPUT_FOLDER: str = args.output_folder  # All intermediate + final output
# =============================================================================


# =============================================================================
# === SHARED CONSTANTS ========================================================
# =============================================================================

SECTION_NAMES = [
    "Materials and Methods",
    "Material and Methods",
    "Materials and methods",
    "2. Materials and Methods",
    "2 | Materials and Methods",
    "2 Materials and Methods",
    "2. Methods",
    "2 | Methods",
    "2. Materials and methods",
    "## 2. Materials and methods",
    '<span id="page-2-0"></span>**2. Materials and methods**',
    "###2. Methods",
    "2. MATERIALS AND METHODS",
    "2. Methodology",
    "2 | MATERIALS AND METHODS",
    "3. Layout of the experiment, treatments and management",
    "2. Data and methods",
    "MATERIALS AND METHODS",
    "2. Methods and data",
    "2 METHODS",
    "II. Materials and Methods",
    "LOCATIONS",
    "Methods",
    "2. Material and methods",
    "**2. Methodology**",
    "*2 . MATERIALS AND METHODS 2.1 Validation of model predictability with experimental data",
    "**2. Materials and methods**",
    "**2. Material and methods**",
    "*2. Materials and method*",
    "**2. Materials and method**",
    "2. Material & methods",
    "**MATERIALS AND METHODS Study Region**",
    "**2 . MATERIALS AND METHODS",
    "**2** | **MATERIALS AND METHODS**",
    "*Materials and Methods*",
    "Materials and methods",
    "## **2 Site and measurements**",
    "## **2. Data and methods**",
    "2. Field experiments",
    "#### 2. Field experiments",
    "**Materials and Methods**",
    "**2 METHODS**",
    "*2. Materials and methods**",
    "24.2 Engineering vs. Biological Databases",
    "2 Site and measurements",
]

STOPPING_SECTIONS = [
    "# 3. Results",
    " 3. Development of the Hybrid-Maize model",
    "# 3. Development of the Hybrid-Maize model",
    "## 3. Results",
    "3. Results and Discussion",
    "3 | Results and Discussion",
    "3 Results and Discussion",
    "Results and Discussion",
    "Results and discussion",
    "2. Historical background",
    "#### 4. Results",
    "3. Results",
    "3 | Results",
    "Results",
    "2 Site and measurements",
    "### 3. Results",
    "Methods",
    "Results",
    "3. RESULTS",
    "3. Results and discussion",
    "3 | RESULTS AND DISCUSSION",
    "RESULTS AND DISCUSSION",
    "III. Results and Discussion",
    "4. Results",
    "**RESULTS AND DISCUSSION Planting Dates and Growing Season Temperature**",
    "RESULTS",
    "**3. Results**",
    "**3 . RESULTS",
    "**3. Results and discussion**",
    "**3** | **RESULTS AND DISCUSSION**",
    "**Results**",
    "References",
    "### **4 Methodology**",
    "## **RESULTS AND DISCUSSION**",
    "**3. RESULTS**",
    "## 3. Results",
    "## 4. Discussion",
    "## **3. Results**",
    "# *3.1. Yield*",
    " *3.1. Yield*",
    "# **RESULTS AND DISCUSSION Planting Dates and Growing Season Temperature**",
]

KEYWORD_NAMES = [
    "Keywords",
    "KEYWORDS",
    "Key words",
    "KEY WORDS",
    "**Keywords**",
    "**KEYWORDS**",
    "*Keywords*",
    "*KEYWORDS*",
    "Index terms",
    "INDEX TERMS",
    "### **1 Introduction**",
    "**1. INTRODUCTION**",
    "1. Introduction",
    "## 1. Introduction",
    "**MATERIALS AND METHODS Study Region**",
]


# -------------------------------------------------
def extract_date(markdown_content):
    """
    Extract content starting with 'https://doi.org/'
    and ending with 'All rights reserved'
    """

    pattern = r"""
        (https:\/\/doi\.org\/.*?          # start at DOI
        (?:All\s+rights\s+reserved|©))    # end at either phrase or ©
    """

    match = re.search(
        pattern, markdown_content, flags=re.DOTALL | re.IGNORECASE | re.VERBOSE
    )

    return match.group(1).strip() if match else ""


# =============================================================================
# === HELPERS =================================================================
# =============================================================================


def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"  Error reading {path}: {e}")
        return ""


def save_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        print(f"  Error saving {path}: {e}")


# =============================================================================
# === EXTRACTION FUNCTIONS ====================================================
# =============================================================================


def extract_methods_section(content):
    """2.1 — Pull the Methods section out of the full document."""
    section_pattern = "|".join(re.escape(n) for n in SECTION_NAMES)
    stopping_pattern = "|".join(re.escape(n) for n in STOPPING_SECTIONS)
    pattern = rf"\s*({section_pattern}).*?(?=#\s*({stopping_pattern})|$)"
    match = re.search(pattern, content, flags=re.DOTALL)
    return match.group(0).strip() if match else ""


def extract_tables_before_methods(content):
    """2.2 — Pull all pipe-tables that appear before the Methods heading."""
    section_pattern = "|".join(re.escape(n) for n in SECTION_NAMES)
    match = re.search(rf"({section_pattern})", content, flags=re.IGNORECASE)
    content_before = content[: match.start()].strip() if match else content.strip()

    tables = []
    lines = content_before.split("\n")
    current_table, table_name, in_table = [], "", False
    previous_non_empty = ""

    for line in lines:
        if "|" in line:
            if not in_table:
                table_name = previous_non_empty
                in_table = True
            current_table.append(line)
        else:
            if in_table and current_table:
                body = "\n".join(current_table)
                tables.append(f"{table_name}\n\n{body}" if table_name else body)
                current_table, table_name, in_table = [], "", False
            if line.strip():
                previous_non_empty = line.strip()

    if current_table:
        body = "\n".join(current_table)
        tables.append(f"{table_name}\n\n{body}" if table_name else body)

    return tables


def extract_author_block(content):
    """2.4 — Pull everything before the Keywords / Introduction heading."""
    keyword_pattern = "|".join(re.escape(n) for n in KEYWORD_NAMES)
    pattern = rf"^(.*?)(?=#?\s*({keyword_pattern})[\s:]*|$)"
    match = re.search(pattern, content, flags=re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else content.strip()


# =============================================================================
# === MAIN PIPELINE ===========================================================
# =============================================================================


def process_file(md_path, input_folder):
    """Run the full sequential Step 2 pipeline for one Markdown file.
    Only the final results_3_0 file is written to disk.
    """
    rel = os.path.relpath(os.path.dirname(md_path), input_folder)
    base = os.path.splitext(os.path.basename(md_path))[0]
    content = read_file(md_path)

    if not content:
        print(f"  Skipping (empty): {md_path}")
        return

    # 2.1  Extract Methods section
    methods = extract_methods_section(content)
    print(f"  2.1 -> Methods extracted ({len(methods)} chars)")

    # 2.2  Extract tables before Methods
    tables = extract_tables_before_methods(content)
    tables_text = (
        "\n\n---\n\n".join(tables)
        if tables
        else "No tables found before Methods section."
    )
    print(f"  2.2 -> {len(tables)} table(s) extracted")

    # 2.3  results_1_0 = Methods + Tables
    results_1_0 = methods.strip() + "\n\n" + tables_text.strip()
    print(f"  2.3 -> results_1_0 ready (in memory)")

    # 2.4  Extract author block
    authors = extract_author_block(content)
    print(f"  2.4 -> Authors extracted ({len(authors)} chars)")

    # 2.5  results_2_0 = Authors + results_1_0
    results_2_0 = authors.strip() + "\n\n" + results_1_0.strip()
    print(f"  2.5 -> results_2_0 ready (in memory)")

    # 2.6  Extract publication date
    date_text = extract_date(content)
    print(f"  2.6 -> Date: {date_text[:60]}")

    # 2.7  results_3_0 = Date + results_2_0  <- FINAL, written to disk
    results_3_0 = date_text.strip() + results_2_0.strip()
    final_path = os.path.join(OUTPUT_FOLDER, rel, f"{base}.md")
    save_file(final_path, results_3_0)
    print(f"  2.7 -> Saved: {final_path}  OK")


def run_pipeline(input_folder):
    md_files = [
        os.path.join(root, f)
        for root, _, files in os.walk(input_folder)
        for f in files
        if f.lower().endswith(".md")
    ]

    if not md_files:
        print(f"No Markdown files found in: {input_folder}")
        return

    print(f"Found {len(md_files)} Markdown file(s). Starting pipeline...\n")
    for md_path in md_files:
        print(f"Processing: {md_path}")
        process_file(md_path, input_folder)
        print()

    print("=" * 60)
    print("Done — Step 2 pipeline complete.")
    print(f"Final files -> {OUTPUT_FOLDER}")


if __name__ == "__main__":
    run_pipeline(INPUT_MD_FOLDER)
