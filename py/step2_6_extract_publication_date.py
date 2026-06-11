# -*- coding: utf-8 -*-
"""
Step 2.6 — Extract the publication / corresponding date from each Markdown file.

Usage:
    1. Set the paths in the USER CONFIG section below.
    2. Run:  python step2_6_extract_publication_date.py

Input:  Folder of Markdown files produced by Step 1
Output: Folder of small Markdown files containing only the detected date line
        (each output file is named  <original_name>_results.md)

Note:
    The script searches for common date patterns such as:
      "Received", "Accepted", "Published", "Corresponding", year patterns, etc.
    If no date is found the output file will contain "Date not found."
"""

import os
import re

# =============================================================================
# === USER CONFIG =============================================================
# =============================================================================
INPUT_MD_FOLDER  = r"C:\your\path\to\output_markdown"       # Step 1 output
OUTPUT_MD_FOLDER = r"C:\your\path\to\publication_dates"     # this step's output
# =============================================================================

# Regex patterns to detect date-related lines in the paper header
DATE_PATTERNS = [
    r"Received[:\s]+.{0,60}",
    r"Accepted[:\s]+.{0,60}",
    r"Published[:\s]+.{0,60}",
    r"Available online[:\s]+.{0,60}",
    r"Corresponding author[:\s]+.{0,80}",
    r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}",
    r"\b\d{1,2}\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}",
    r"\b(19|20)\d{2}\b",
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


def extract_date(markdown_content):
    """Return the first matching date-related line found in the document."""
    for pattern in DATE_PATTERNS:
        match = re.search(pattern, markdown_content, flags=re.IGNORECASE)
        if match:
            return match.group(0).strip()
    return "Date not found."


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
                date_text = extract_date(content)
                save_file(out_path, date_text)
                print(f"  Date found: {date_text[:60]}")


if __name__ == "__main__":
    process_folder(INPUT_MD_FOLDER, OUTPUT_MD_FOLDER)
    print("Done — Step 2.6")
