# -*- coding: utf-8 -*-
"""
Extract content from 'https://doi.org/' to 'All rights reserved'
"""

import os
import re


# -------------------------------------------------
# Read markdown file
# -------------------------------------------------
def read_markdown_file(md_file_path):
    try:
        with open(md_file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Error reading markdown file {md_file_path}: {e}")
        return ""


# -------------------------------------------------
# Extract DOI → All rights reserved block
# -------------------------------------------------
def extract_doi_to_all_rights_reserved(markdown_content):
    """
    Extract content starting with 'https://doi.org/'
    and ending with 'All rights reserved'
    """
  
    pattern = r"""
        (https:\/\/doi\.org\/.*?          # start at DOI
        (?:All\s+rights\s+reserved|©))    # end at either phrase or ©
    """

    match = re.search(
        pattern,
        markdown_content,
        flags=re.DOTALL | re.IGNORECASE | re.VERBOSE
    )

    return match.group(1).strip() if match else ""


# -------------------------------------------------
# Save extracted content
# -------------------------------------------------
def save_to_file(file_path, content):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        print(f"Error saving file {file_path}: {e}")


# -------------------------------------------------
# Process a single markdown file
# -------------------------------------------------
def process_markdown_file(md_file_path, output_path):
    markdown_content = read_markdown_file(md_file_path)
    if not markdown_content:
        return

    extracted = extract_doi_to_all_rights_reserved(markdown_content)

    if extracted:
        save_to_file(output_path, extracted)
    else:
        # Create empty file to keep one-to-one mapping
        save_to_file(output_path, "")
        print(f"No DOI / All-rights-reserved block found in: {md_file_path}")


# -------------------------------------------------
# Process all markdown files
# -------------------------------------------------
def process_all_markdown_files(input_folder, output_folder):
    for root, _, files in os.walk(input_folder):
        for file_name in files:
            if file_name.lower().endswith(".md"):
                md_file_path = os.path.join(root, file_name)

                # Preserve folder structure safely
                if root == input_folder:
                    target_dir = output_folder
                else:
                    rel_path = os.path.relpath(root, input_folder)
                    target_dir = os.path.join(output_folder, rel_path)

                os.makedirs(target_dir, exist_ok=True)

                output_path = os.path.join(
                    target_dir,
                    f"{os.path.splitext(file_name)[0]}_results.md"
                )

                print(f"Processing: {md_file_path}")
                process_markdown_file(md_file_path, output_path)


# -------------------------------------------------
# Main
# -------------------------------------------------
def main():
    markdown_folder = (
      "..."#markdown folder
    )

    output_folder = (
        "..."#publish year
    )

    process_all_markdown_files(markdown_folder, output_folder)


if __name__ == "__main__":
    main()
