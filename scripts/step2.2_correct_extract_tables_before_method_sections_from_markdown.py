# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 15:00:41 2025

@author: xinxin
"""
import os
import re
import pandas as pd


# Function to read markdown files
def read_markdown_file(md_file_path):
    try:
        with open(md_file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Error reading markdown file {md_file_path}: {e}")
        return ""


# Extract tables with names
def extract_tables_with_names(content):
    tables = []
    lines = content.split('\n')

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
                if table_name:
                    tables.append(f"{table_name}\n\n{table_content}")
                else:
                    tables.append(table_content)
                current_table = []
                table_name = ""
                in_table = False

            if line.strip():
                previous_non_empty_line = line.strip()

    if current_table:
        table_content = "\n".join(current_table)
        if table_name:
            tables.append(f"{table_name}\n\n{table_content}")
        else:
            tables.append(table_content)

    return tables


# Extract tables before Methods section
def extract_tables_before_methods(markdown_content):
    section_names = ["Materials and Methods", "Material and Methods", "Materials and methods","2. Materials and Methods", "2 | Materials and Methods", "2 Materials and Methods",
                       "2. Methods", "2 | Methods","2. Materials and methods","## 2. Materials and methods",
                    "<span id=\"page-2-0\"></span>**2. Materials and methods**","###2. Methods",
                      "2. MATERIALS AND METHODS","2. Methodology","2 | MATERIALS AND METHODS","3. Layout of the experiment, treatments and management",
                      "2. Data and methods","MATERIALS AND METHODS","2. Methods and data","2 METHODS","II. Materials and Methods","LOCATIONS","Methods",
                      "2. Material and methods","**2. Methodology**","2. Data and methods","*2 . MATERIALS AND METHODS 2.1 Validation of model predictability with experimental data",
                      "**2. Materials and methods**","**2. Material and methods**","*2. Materials and method*","**2. Materials and method**","2. Material & methods","**MATERIALS AND METHODS Study Region**",
                      "**2 . MATERIALS AND METHODS","**2** | **MATERIALS AND METHODS**","*Materials and Methods*",
                      "Materials and methods","## **2 Site and measurements**","## **2. Data and methods**","2. Field experiments","#### 2. Field experiments",
                      "**Materials and Methods**","**2 METHODS**","*2. Materials and methods**","24.2 Engineering vs. Biological Databases","2 Site and measurements"
                      ]

    section_pattern = "|".join(re.escape(name) for name in section_names)

    # FIXED: remove incorrect #\s*
    pattern = rf"({section_pattern})"
    match = re.search(pattern, markdown_content, flags=re.IGNORECASE)

    if match:
        content_before_methods = markdown_content[:match.start()].strip()
        print(f"  Found Methods section at position {match.start()}")
    else:
        content_before_methods = markdown_content.strip()
        print(f"  No Methods section found, processing entire document")

    tables = extract_tables_with_names(content_before_methods)
    return tables


# Save to file
def save_to_file(file_path, content):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print(f"Error saving content to {file_path}: {e}")


# Process one markdown file
def process_markdown_extract_tables(md_file_path, output_path):
    markdown_content = read_markdown_file(md_file_path)
    if not markdown_content:
        return

    tables = extract_tables_before_methods(markdown_content)

    if tables:
        combined_tables = "\n\n---\n\n".join(tables)
        save_to_file(output_path, combined_tables)
        print(f"  Found {len(tables)} table(s)")
    else:
        save_to_file(output_path, "No tables found before Methods section.")
        print(f"  No tables found")


# Recursively process all markdown files
def process_all_markdown_files(input_folder, output_folder):
    for root, dirs, files in os.walk(input_folder):
        for file_name in files:
            if file_name.lower().endswith(".md"):
                md_file_path = os.path.join(root, file_name)

                rel_path = os.path.relpath(root, input_folder)
                target_dir = os.path.join(output_folder, rel_path)
                os.makedirs(target_dir, exist_ok=True)

                output_path = os.path.join(
                    target_dir, f"{os.path.splitext(file_name)[0]}_tables.md"
                )

                print(f"Processing file: {md_file_path}")
                process_markdown_extract_tables(md_file_path, output_path)


# Main
def main():
    markdown_folder = '...'
    base_output_folder = '...'

    os.makedirs(base_output_folder, exist_ok=True)

    # Process root-level markdown files
    print("Processing root-level markdown files...")
    process_all_markdown_files(markdown_folder, base_output_folder)


if __name__ == "__main__":
    main()
