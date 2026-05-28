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


def remove_unwanted_sections_method(markdown_content):
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
   
    
    stopping_sections = ["# 3. Results"," 3. Development of the Hybrid-Maize model","# 3. Development of the Hybrid-Maize model","## 3. Results","3. Results and Discussion", "3 | Results and Discussion", "3 Results and Discussion", "Results and Discussion","Results and discussion","2. Historical background","#### 4. Results"
                          "3. Results", "3 | Results", "Results","2 Site and measurements","### 3. Results","Methods","Results",
                          "3. RESULTS","3. Results and discussion","3 | RESULTS AND DISCUSSION","RESULTS AND DISCUSSION","III. Results and Discussion","4. Results","**RESULTS AND DISCUSSION Planting Dates and Growing Season Temperature**",
                          "RESULTS","**3. Results**","**3 . RESULTS","**3. Results and discussion**","**3** | **RESULTS AND DISCUSSION**","**Results**","References","### **4 Methodology**","## **RESULTS AND DISCUSSION**","**3. RESULTS**","## 3. Results",
                          "## 4. Discussion","## **3. Results**","# *3.1. Yield*"," *3.1. Yield*","# **RESULTS AND DISCUSSION Planting Dates and Growing Season Temperature**"]

    section_pattern = "|".join(re.escape(name) for name in section_names)
    stopping_pattern = "|".join(re.escape(name) for name in stopping_sections)

    #pattern = rf"#\s*({section_pattern}).*?(?=#\s*({stopping_pattern})|$)"
    #pattern = r"(^|\n)\s*(\d+\..*?)(.*?)(?=\n\s*\d+\.|\Z)"
    
    # pattern = rf"\s*({section_pattern}).*?(?=#\s*({stopping_pattern})|$)"
    # match = re.search(pattern, markdown_content, flags=re.DOTALL | re.IGNORECASE)
    # return match.group(0).strip() if match else ""
    
    pattern = rf"\s*({section_pattern}).*?(?=#\s*({stopping_pattern})|$)"
    match = re.search(pattern, markdown_content, flags=re.DOTALL)
    return match.group(0).strip() if match else ""


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

    content = remove_unwanted_sections_method(markdown_content)
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
    markdown_folder = '...'#put own input markdown folder
    base_output_folder = '...' ####put output method section

    process_all_markdown_files(markdown_folder, base_output_folder)

if __name__ == "__main__":
    main()


