# -*- coding: utf-8 -*-
"""
Step 2.2 — Extract tables that appear BEFORE the Methods section in each Markdown file.

Usage:
    1. Set the paths in the USER CONFIG section below.
    2. Run:  python step2_2_extract_tables_before_methods.py

Input:  Folder of Markdown files produced by Step 1
Output: Folder of Markdown files containing only the tables found before Methods
        (each output file is named  <original_name>_tables.md)
"""

import os
import re

# =============================================================================
# === USER CONFIG =============================================================
# =============================================================================
INPUT_MD_FOLDER  = r"C:\your\path\to\output_markdown"       # Step 1 output
OUTPUT_MD_FOLDER = r"C:\your\path\to\tables_before_methods" # this step's output
# =============================================================================

SECTION_NAMES = [
    "Materials and Methods", "Material and Methods", "Materials and methods",
    "2. Materials and Methods", "2 | Materials and Methods", "2 Materials and Methods",
    "2. Methods", "2 | Methods", "2. Materials and methods", "## 2. Materials and methods",
    "<span id=\"page-2-0\"></span>**2. Materials and methods**", "###2. Methods",
    "2. MATERIALS AND METHODS", "2. Methodology", "2 | MATERIALS AND METHODS",
    "3. Layout of the experiment, treatments and management",
    "2. Data and methods", "MATERIALS AND METHODS", "2. Methods and data",
    "2 METHODS", "II. Materials and Methods", "LOCATIONS", "Methods",
    "2. Material and methods", "**2. Methodology**",
    "*2 . MATERIALS AND METHODS 2.1 Validation of model predictability with experimental data",
    "**2. Materials and methods**", "**2. Material and methods**",
    "*2. Materials and method*", "**2. Materials and method**",
    "2. Material & methods", "**MATERIALS AND METHODS Study Region**",
    "**2 . MATERIALS AND METHODS", "**2** | **MATERIALS AND METHODS**",
    "*Materials and Methods*", "Materials and methods",
    "## **2 Site and measurements**", "## **2. Data and methods**",
    "2. Field experiments", "#### 2. Field experiments",
    "**Materials and Methods**", "**2 METHODS**", "*2. Materials and methods**",
    "24.2 Engineering vs. Biological Databases", "2 Site and measurements",
]


def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"  Error reading {path}: {e}")
        return ""


def save_file(path, content):
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        print(f"  Error saving {path}: {e}")


def extract_tables_with_names(content):
    """Parse markdown pipe tables, capturing the preceding heading as table name."""
    tables = []
    lines = content.split("\n")
    current_table = []
    table_name = ""
    in_table = False
    previous_non_empty_line = ""

    for line in lines:
        if "|" in line:
            if not in_table:
                table_name = previous_non_empty_line
                in_table = True
            current_table.append(line)
        else:
            if in_table and current_table:
                table_content = "\n".join(current_table)
                tables.append(f"{table_name}\n\n{table_content}" if table_name else table_content)
                current_table = []
                table_name = ""
                in_table = False
            if line.strip():
                previous_non_empty_line = line.strip()

    if current_table:
        table_content = "\n".join(current_table)
        tables.append(f"{table_name}\n\n{table_content}" if table_name else table_content)

    return tables


def extract_tables_before_methods(markdown_content):
    section_pattern = "|".join(re.escape(n) for n in SECTION_NAMES)
    match = re.search(rf"({section_pattern})", markdown_content, flags=re.IGNORECASE)

    if match:
        content_before = markdown_content[:match.start()].strip()
        print(f"  Methods section found at position {match.start()}")
    else:
        content_before = markdown_content.strip()
        print("  No Methods section found — processing entire document")

    return extract_tables_with_names(content_before)


def process_folder(input_folder, output_folder):
    for root, dirs, files in os.walk(input_folder):
        for file_name in files:
            if not file_name.lower().endswith(".md"):
                continue
            md_path = os.path.join(root, file_name)
            rel_path = os.path.relpath(root, input_folder)
            target_dir = os.path.join(output_folder, rel_path)
            os.makedirs(target_dir, exist_ok=True)
            out_path = os.path.join(target_dir, f"{os.path.splitext(file_name)[0]}_tables.md")

            print(f"Processing: {md_path}")
            content = read_file(md_path)
            if not content:
                continue

            tables = extract_tables_before_methods(content)
            if tables:
                save_file(out_path, "\n\n---\n\n".join(tables))
                print(f"  Found {len(tables)} table(s)")
            else:
                save_file(out_path, "No tables found before Methods section.")
                print("  No tables found")


if __name__ == "__main__":
    process_folder(INPUT_MD_FOLDER, OUTPUT_MD_FOLDER)
    print("Done — Step 2.2")
