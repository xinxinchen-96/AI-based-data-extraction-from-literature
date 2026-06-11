# -*- coding: utf-8 -*-
"""
Step 2.1 — Extract the "Materials and Methods" section from each Markdown file.

Usage:
    1. Set the paths in the USER CONFIG section below.
    2. Run:  python step2_1_extract_method_sections.py

Input:  Folder of Markdown files produced by Step 1
Output: Folder of Markdown files containing only the Methods section
        (each output file is named  <original_name>_results.md)
"""

import os
import re

# =============================================================================
# === USER CONFIG =============================================================
# =============================================================================
INPUT_MD_FOLDER  = r"C:\your\path\to\output_markdown"          # Step 1 output
OUTPUT_MD_FOLDER = r"C:\your\path\to\method_sections"          # this step's output
# =============================================================================

# All known headings that mark the start of a Methods section
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

# All known headings that mark the end of the Methods section (start of Results)
STOPPING_SECTIONS = [
    "# 3. Results", " 3. Development of the Hybrid-Maize model",
    "# 3. Development of the Hybrid-Maize model", "## 3. Results",
    "3. Results and Discussion", "3 | Results and Discussion",
    "3 Results and Discussion", "Results and Discussion", "Results and discussion",
    "2. Historical background", "#### 4. Results",
    "3. Results", "3 | Results", "Results", "2 Site and measurements",
    "### 3. Results", "Methods", "Results", "3. RESULTS",
    "3. Results and discussion", "3 | RESULTS AND DISCUSSION",
    "RESULTS AND DISCUSSION", "III. Results and Discussion", "4. Results",
    "**RESULTS AND DISCUSSION Planting Dates and Growing Season Temperature**",
    "RESULTS", "**3. Results**", "**3 . RESULTS",
    "**3. Results and discussion**", "**3** | **RESULTS AND DISCUSSION**",
    "**Results**", "References", "### **4 Methodology**",
    "## **RESULTS AND DISCUSSION**", "**3. RESULTS**", "## 3. Results",
    "## 4. Discussion", "## **3. Results**", "# *3.1. Yield*",
    " *3.1. Yield*",
    "# **RESULTS AND DISCUSSION Planting Dates and Growing Season Temperature**",
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


def extract_methods_section(markdown_content):
    section_pattern  = "|".join(re.escape(n) for n in SECTION_NAMES)
    stopping_pattern = "|".join(re.escape(n) for n in STOPPING_SECTIONS)
    pattern = rf"\s*({section_pattern}).*?(?=#\s*({stopping_pattern})|$)"
    match = re.search(pattern, markdown_content, flags=re.DOTALL)
    return match.group(0).strip() if match else ""


def process_folder(input_folder, output_folder):
    for root, dirs, files in os.walk(input_folder):
        for file_name in files:
            if not file_name.lower().endswith(".md"):
                continue
            md_path = os.path.join(root, file_name)
            rel_path = os.path.relpath(root, input_folder)
            target_dir = os.path.join(output_folder, rel_path)
            os.makedirs(target_dir, exist_ok=True)
            out_path = os.path.join(target_dir, f"{os.path.splitext(file_name)[0]}_results.md")
            print(f"Processing: {md_path}")
            content = read_file(md_path)
            if content:
                save_file(out_path, extract_methods_section(content))


if __name__ == "__main__":
    process_folder(INPUT_MD_FOLDER, OUTPUT_MD_FOLDER)
    print("Done — Step 2.1")
