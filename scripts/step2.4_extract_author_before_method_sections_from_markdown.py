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

# Function to remove unwanted sections from markdown
def extract_before_keywords(markdown_content):
    # Common keyword section names
    keyword_names = [
        "Keywords", "KEYWORDS", "Key words", "KEY WORDS",
        "**Keywords**", "**KEYWORDS**", "*Keywords*", "*KEYWORDS*",
        "Index terms", "INDEX TERMS","### **1 Introduction**","**1. INTRODUCTION**",
        "1. Introduction","## 1. Introduction","**MATERIALS AND METHODS Study Region**"
    ]

    # Build a pattern to detect any keyword heading
    keyword_pattern = "|".join(re.escape(name) for name in keyword_names)

    # Regex: capture everything from the start up to the first keyword occurrence
    pattern = rf"^(.*?)(?=#?\s*({keyword_pattern})[\s:]*|$)"

    match = re.search(pattern, markdown_content, flags=re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else markdown_content.strip()

# Function to save extracted content to a file
def save_to_file(file_path, content):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print(f"Error saving content to {file_path}: {e}")

# Function to process markdown and extract methods section
def process_markdown_extract_methods(md_file_path, output_path):
    markdown_content = read_markdown_file(md_file_path)
    if not markdown_content:
        return

    content = extract_before_keywords(markdown_content)
    save_to_file(output_path, content)

# Function to process all markdown files in a folder
def process_all_markdown_files(input_folder, output_folder):
    for root, dirs, files in os.walk(input_folder):
        for file_name in files:
            if file_name.lower().endswith(".md"):
                md_file_path = os.path.join(root, file_name)

                # keep subfolder structure inside the output folder
                rel_path = os.path.relpath(root, input_folder)
                target_dir = os.path.join(output_folder, rel_path)
                os.makedirs(target_dir, exist_ok=True)

                output_path = os.path.join(
                    target_dir, f"{os.path.splitext(file_name)[0]}_results.md"
                )

                print(f"Processing file: {md_file_path}")
                process_markdown_extract_methods(md_file_path, output_path)


# Main function
def main():
    markdown_folder = '...' #markdown
    base_output_folder = '...' #authors

    process_all_markdown_files(markdown_folder, base_output_folder)

if __name__ == "__main__":
    main()






