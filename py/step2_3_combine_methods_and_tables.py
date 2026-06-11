# -*- coding: utf-8 -*-
"""
Step 2.3 — Combine the Methods section (Step 2.1) with the tables before Methods (Step 2.2).

Usage:
    1. Set the paths in the USER CONFIG section below.
    2. Run:  python step2_3_combine_methods_and_tables.py

Input:
    - Folder of *_results.md files  (from Step 2.1 — methods sections)
    - Folder of *_tables.md files   (from Step 2.2 — tables before methods)
Output:
    - Folder of combined .md files  (methods + tables, matched by base filename)
"""

import os

# =============================================================================
# === USER CONFIG =============================================================
# =============================================================================
METHODS_FOLDER  = r"C:\your\path\to\method_sections"        # Step 2.1 output
TABLES_FOLDER   = r"C:\your\path\to\tables_before_methods"  # Step 2.2 output
OUTPUT_FOLDER   = r"C:\your\path\to\combined_methods_tables" # this step's output
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


def combine_folders(methods_folder, tables_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    # Build lookup: base_name -> full path
    results_files = {
        f.replace("_results.md", ""): os.path.join(methods_folder, f)
        for f in os.listdir(methods_folder)
        if f.endswith("_results.md")
    }
    tables_files = {
        f.replace("_tables.md", ""): os.path.join(tables_folder, f)
        for f in os.listdir(tables_folder)
        if f.endswith("_tables.md")
    }

    common_keys = set(results_files.keys()) & set(tables_files.keys())
    print(f"Found {len(common_keys)} matching file pair(s): {common_keys}")

    for key in common_keys:
        content_methods = read_file(results_files[key])
        content_tables  = read_file(tables_files[key])

        combined = ""
        if content_methods:
            combined += content_methods.strip() + "\n\n"
        if content_tables:
            combined += content_tables.strip()

        out_path = os.path.join(output_folder, f"{key}.md")
        save_file(out_path, combined)
        print(f"  Combined -> {out_path}")


if __name__ == "__main__":
    combine_folders(METHODS_FOLDER, TABLES_FOLDER, OUTPUT_FOLDER)
    print("Done — Step 2.3")
