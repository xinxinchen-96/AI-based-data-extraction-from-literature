# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 16:23:20 2025

@author: xinxin
"""

import os

def read_markdown_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return ""

def save_combined_file(file_path, content):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        print(f"Error writing combined file {file_path}: {e}")

def combine_markdown_files(folder1, folder2, output_folder):

    os.makedirs(output_folder, exist_ok=True)

    # create mapping for results files
    results_files = {
        f.replace("_results.md", ""): os.path.join(folder1, f)
        for f in os.listdir(folder1)
        if f.endswith("_results.md")
    }

    # create mapping for tables files
    tables_files = {
        f.replace("_tables.md", ""): os.path.join(folder2, f)
        for f in os.listdir(folder2)
        if f.endswith("_tables.md")
    }

    # find matching base names
    common_keys = set(results_files.keys()) & set(tables_files.keys())
    print("Found matches:", common_keys)

    for key in common_keys:
        file1_path = results_files[key]
        file2_path = tables_files[key]

        content1 = read_markdown_file(file1_path)
        content2 = read_markdown_file(file2_path)

        combined_content = ""
        if content1:
            combined_content += content1.strip() + "\n\n"
        if content2:
            combined_content += content2.strip()

        output_file_path = os.path.join(output_folder, f"{key}.md")
        save_combined_file(output_file_path, combined_content)

        print(f"✔ Combined: {output_file_path}")

def main():
    folder_script1 = r"..." #markdown method sections
    folder_script2 = r"..."# table before method
    output_combined = r"..."#combine output

    combine_markdown_files(folder_script1, folder_script2, output_combined)

if __name__ == "__main__":
    main()
