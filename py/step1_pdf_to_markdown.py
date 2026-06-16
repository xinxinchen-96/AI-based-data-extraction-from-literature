# -*- coding: utf-8 -*-
"""
Step 1 — Convert PDF papers to Markdown using the `marker` tool.

Usage:
    1. Install marker:  pip install marker-pdf
    2. Set the paths in the USER CONFIG section below.
    3. Run:  python step1_pdf_to_markdown.py

Input:  A folder containing PDF files (one per paper)
Output: A folder of Markdown files (one subfolder per PDF)
"""
# step1: https://pypi.org/project/marker-pdf/
# pip install marker-pdf 

import subprocess

# =============================================================================
# === USER CONFIG — edit these two paths before running =======================
# =============================================================================
INPUT_PDF_FOLDER  = r"C:\your\path\to\00_paper_list"       # folder with .pdf files
OUTPUT_MD_FOLDER  = r"C:\your\path\to\01_paper_to_md"  # where .md files will be saved
# =============================================================================

command = [
    "marker",
    INPUT_PDF_FOLDER,
    "--output_dir",
    OUTPUT_MD_FOLDER,
]

try:
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    if result.returncode != 0:
        print(f"Command failed with return code {result.returncode}.")
except FileNotFoundError as e:
    print("Error: 'marker' command not found. Install it with:  pip install marker-pdf")
    print(e)
except Exception as e:
    print("Unexpected error:", e)
