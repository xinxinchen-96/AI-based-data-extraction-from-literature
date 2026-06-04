# -*- coding: utf-8 -*-
"""
Step 2.7 — Append publication date (Step 2.6) to the author-enriched combined files (Step 2.5).
           This produces the FINAL enriched Markdown files ready for LLM processing (Step 3).

Usage:
    1. Set the paths in the USER CONFIG section below.
    2. Run:  python step2_7_add_date_to_combined.py

Input:
    - Folder of combined+author .md files  (from Step 2.5)
    - Folder of date *_results.md files    (from Step 2.6)
Output:
    - Folder of fully enriched .md files   (methods + tables + authors + year)
      → These are the final inputs for Step 3 (LLM extraction)
"""

import os

# =============================================================================
# === USER CONFIG =============================================================
# =============================================================================
COMBINED_FOLDER = r"C:\your\path\to\combined_with_authors"   # Step 2.5 output
DATES_FOLDER    = r"C:\your\path\to\publication_dates"       # Step 2.6 output
OUTPUT_FOLDER   = r"C:\your\path\to\final_enriched_markdown" # this step's output (→ Step 3 input)
# =============================================================================


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


def combine_with_dates(combined_folder, dates_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    combined_files = {
        os.path.splitext(f)[0]: os.path.join(combined_folder, f)
        for f in os.listdir(combined_folder)
        if f.endswith(".md")
    }
    date_files = {
        f.replace("_results.md", ""): os.path.join(dates_folder, f)
        for f in os.listdir(dates_folder)
        if f.endswith("_results.md")
    }

    common_keys = set(combined_files.keys()) & set(date_files.keys())
    print(f"Found {len(common_keys)} matching file pair(s)")

    for key in common_keys:
        content_combined = read_file(combined_files[key])
        content_date     = read_file(date_files[key])

        enriched = ""
        if content_combined:
            enriched += content_combined.strip() + "\n\n"
        if content_date:
            enriched += "## Publication Date\n\n" + content_date.strip()

        out_path = os.path.join(output_folder, f"{key}.md")
        save_file(out_path, enriched)
        print(f"  Saved -> {out_path}")


if __name__ == "__main__":
    combine_with_dates(COMBINED_FOLDER, DATES_FOLDER, OUTPUT_FOLDER)
    print("Done — Step 2.7  |  Final enriched Markdown files are ready for Step 3.")
