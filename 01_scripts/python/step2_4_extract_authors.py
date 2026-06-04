# -*- coding: utf-8 -*-
"""
Step 2.4 — Extract author names from the beginning of each Markdown file
           (text before the Keywords / Introduction section).

Usage:
    1. Set the paths in the USER CONFIG section below.
    2. Run:  python step2_4_extract_authors.py

Input:  Folder of Markdown files produced by Step 1
Output: Folder of Markdown files containing only the author block
        (each output file is named  <original_name>_results.md)
"""

import os
import re

# =============================================================================
# === USER CONFIG =============================================================
# =============================================================================
INPUT_MD_FOLDER  = r"C:\your\path\to\output_markdown"  # Step 1 output
OUTPUT_MD_FOLDER = r"C:\your\path\to\authors"          # this step's output
# =============================================================================

# Headings that signal the end of the author/abstract block
KEYWORD_NAMES = [
    "Keywords", "KEYWORDS", "Key words", "KEY WORDS",
    "**Keywords**", "**KEYWORDS**", "*Keywords*", "*KEYWORDS*",
    "Index terms", "INDEX TERMS",
    "### **1 Introduction**", "**1. INTRODUCTION**",
    "1. Introduction", "## 1. Introduction",
    "**MATERIALS AND METHODS Study Region**",
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


def extract_author_block(markdown_content):
    """Return everything before the first Keywords / Introduction heading."""
    keyword_pattern = "|".join(re.escape(n) for n in KEYWORD_NAMES)
    pattern = rf"^(.*?)(?=#?\s*({keyword_pattern})[\s:]*|$)"
    match = re.search(pattern, markdown_content, flags=re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else markdown_content.strip()


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
                save_file(out_path, extract_author_block(content))


if __name__ == "__main__":
    process_folder(INPUT_MD_FOLDER, OUTPUT_MD_FOLDER)
    print("Done — Step 2.4")
