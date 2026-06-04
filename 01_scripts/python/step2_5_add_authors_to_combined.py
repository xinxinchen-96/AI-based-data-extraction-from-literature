# -*- coding: utf-8 -*-
"""
Step 2.5 — Append author information (Step 2.4) to the combined methods+tables files (Step 2.3).

Usage:
    1. Set the paths in the USER CONFIG section below.
    2. Run:  python step2_5_add_authors_to_combined.py

Input:
    - Folder of combined .md files   (from Step 2.3)
    - Folder of author *_results.md  (from Step 2.4)
Output:
    - Folder of enriched .md files with author block appended
"""

import os

# =============================================================================
# === USER CONFIG =============================================================
# =============================================================================
COMBINED_FOLDER = r"C:\your\path\to\combined_methods_tables"  # Step 2.3 output
AUTHORS_FOLDER  = r"C:\your\path\to\authors"                  # Step 2.4 output
OUTPUT_FOLDER   = r"C:\your\path\to\combined_with_authors"    # this step's output
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


def combine_with_authors(combined_folder, authors_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    combined_files = {
        os.path.splitext(f)[0]: os.path.join(combined_folder, f)
        for f in os.listdir(combined_folder)
        if f.endswith(".md")
    }
    author_files = {
        f.replace("_results.md", ""): os.path.join(authors_folder, f)
        for f in os.listdir(authors_folder)
        if f.endswith("_results.md")
    }

    common_keys = set(combined_files.keys()) & set(author_files.keys())
    print(f"Found {len(common_keys)} matching file pair(s)")

    for key in common_keys:
        content_combined = read_file(combined_files[key])
        content_authors  = read_file(author_files[key])

        enriched = ""
        if content_combined:
            enriched += content_combined.strip() + "\n\n"
        if content_authors:
            enriched += "## Authors\n\n" + content_authors.strip()

        out_path = os.path.join(output_folder, f"{key}.md")
        save_file(out_path, enriched)
        print(f"  Saved -> {out_path}")


if __name__ == "__main__":
    combine_with_authors(COMBINED_FOLDER, AUTHORS_FOLDER, OUTPUT_FOLDER)
    print("Done — Step 2.5")
