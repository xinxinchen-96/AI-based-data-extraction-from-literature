# -*- coding: utf-8 -*-
"""
Step 3 — Use a fine-tuned OpenAI GPT model to extract ICASA-structured variables
          from the enriched Markdown files produced by Step 2.7.

Usage:
    1. Set your OpenAI API key as an environment variable:
           Windows:  setx OPENAI_API_KEY "sk-..."
           or set it directly in the USER CONFIG section (not recommended for shared code).
    2. Set all paths and the fine-tuned model IDs in the USER CONFIG section below.
    3. Run:  python step3_llm_extract_icasa_variables.py

Input:
    - Folder of enriched Markdown files  (from Step 2.7)
    - ICASA Excel template (.xlsm)       (defines variable codes, descriptions, units)
Output:
    - One JSON file per paper per ICASA category  (saved in OUTPUT_JSON_FOLDER/<category>/)

ICASA categories processed:
    exp_metadata, fields, genotypes, plantings, irrigation,
    fertilizers, harvests, plot_details
"""

import os
import json
import re
import pandas as pd
import openai

# =============================================================================
# === USER CONFIG =============================================================
# =============================================================================

# OpenAI API key — prefer environment variable over hard-coding
openai.api_key = os.getenv("OPENAI_API_KEY")  # set env var OPENAI_API_KEY

# Fine-tuned model IDs — replace with your own fine-tuned model names
FINE_TUNED_MODELS = {
    "exp_metadata" : "ft:gpt-4.1-mini-2025-04-14:personal:exp-v040526:DbkEyIz7",  # example
    "fields"       : "ft:gpt-4.1-mini-2025-04-14:personal:fields-YOUR_ID",
    "genotypes"    : "ft:gpt-4.1-mini-2025-04-14:personal:genotypes-YOUR_ID",
    "plantings"    : "ft:gpt-4.1-mini-2025-04-14:personal:plantings-YOUR_ID",
    "irrigation"   : "ft:gpt-4.1-mini-2025-04-14:personal:irrigation-YOUR_ID",
    "fertilizers"  : "ft:gpt-4.1-mini-2025-04-14:personal:fertilizers-YOUR_ID",
    "harvests"     : "ft:gpt-4.1-mini-2025-04-14:personal:harvests-YOUR_ID",
    "plot_details" : "ft:gpt-4.1-mini-2025-04-14:personal:plot-details-YOUR_ID",
}

# Paths
ENRICHED_MD_FOLDER  = r"C:\your\path\to\final_enriched_markdown"  # Step 2.7 output
ICASA_EXCEL_PATH    = r"C:\your\path\to\data\2.0 template_icasa_vba_trainingSet_allColumns.xlsm"
OUTPUT_JSON_FOLDER  = r"C:\your\path\to\llm_output_json"           # JSON results go here

# Sheet name in the ICASA Excel template that contains variable definitions
ICASA_SHEET_NAME = "ICASA_variables"   # adjust if your sheet has a different name

# =============================================================================

client = openai.OpenAI()

# ICASA categories and the prompt instruction for each
CATEGORY_PROMPTS = {
    "exp_metadata" : (
        "Extract the ICASA experiment metadata variables (location, dates, objectives, "
        "experiment ID, etc.) from this content:"
    ),
    "fields" : (
        "Extract the ICASA field/soil characteristics variables (soil type, texture, "
        "organic matter, pH, etc.) from this content:"
    ),
    "genotypes" : (
        "Understanding and extract the ICASA experiment_ID, crop_ident_ICASA, "
        "cultivar_name, crop_intended_use, cultivar_notes et al variables from this content:"
    ),
    "plantings" : (
        "Understanding and extract the ICASA planting_level_name, planting_date, "
        "transplant_date, emergence_date, plant_pop_at_planting, plant_pop_at_emergence, "
        "planting_material, planting_distribution, plant_spacing, row_spacing, "
        "planting_depth, planting_material_weight, planting_method, planting_notes "
        "et al variables from this content:"
    ),
    "irrigation" : (
        "Extract ICASA irrigation applied events variables from this content:"
    ),
    "fertilizers" : (
        "Understanding and extract the ICASA fertiliz_app_name, fertilization_date, "
        "fertilizer_material, application_depth_fert, fertilizer_total_amount, "
        "N_in_applied_fertilizer, phosphorus_applied_fert, fertilizer_K_applied, "
        "fertilizer_applic_notes et al variables from this content:"
    ),
    "harvests" : (
        "Extract the ICASA harvest events variables from this content:"
    ),
    "plot_details" : (
        "Extract all values for each ICASA plot-level experimental design variable "
        "from this content, do not use table format or fake example data:"
    ),
}


def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"  Error reading {path}: {e}")
        return ""


def save_json(path, content_str):
    """Save raw LLM response string to a .json file."""
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content_str)
    except Exception as e:
        print(f"  Error saving {path}: {e}")


def load_icasa_variables(excel_path, sheet_name, category):
    """Load ICASA variable definitions for a given category from the Excel template."""
    try:
        df = pd.read_excel(excel_path, sheet_name=sheet_name, engine="openpyxl")
        # Filter rows belonging to this category (adjust column name if needed)
        if "Category" in df.columns:
            df = df[df["Category"].str.lower() == category.lower()]
        return df
    except Exception as e:
        print(f"  Warning: could not load ICASA variables for '{category}': {e}")
        return pd.DataFrame()


def call_llm(model_id, system_msg, user_msg):
    """Send a prompt to the fine-tuned model and return the response text."""
    try:
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user",   "content": user_msg},
            ],
            temperature=0,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"  LLM call failed: {e}")
        return ""


def process_paper(md_path, paper_name, output_base):
    """Run all ICASA category extractions for a single paper."""
    content = read_file(md_path)
    if not content:
        return

    for category, prompt_prefix in CATEGORY_PROMPTS.items():
        model_id = FINE_TUNED_MODELS.get(category)
        if not model_id:
            print(f"  Skipping '{category}' — no model ID configured.")
            continue

        print(f"  Extracting [{category}] ...")
        # Load ICASA variable definitions from the Excel template to guide the LLM
        icasa_vars_df = load_icasa_variables(ICASA_EXCEL_PATH, ICASA_SHEET_NAME, category)
        if not icasa_vars_df.empty:
            var_names = icasa_vars_df.iloc[:, 0].dropna().tolist()
            var_hint = "Relevant ICASA variables: " + ", ".join(str(v) for v in var_names) + "."
        else:
            var_hint = ""
        system_msg = "You are an expert in agriculture and crop modeling."
        if var_hint:
            system_msg += " " + var_hint
        user_message = f"{prompt_prefix} {content}"
        result = call_llm(
            model_id=model_id,
            system_msg=system_msg,
            user_msg=user_message,
        )

        if result:
            out_path = os.path.join(output_base, category, f"{paper_name}_{category}.json")
            save_json(out_path, result)
            print(f"    Saved -> {out_path}")
        else:
            print(f"    No result returned for [{category}].")


def main():
    if not openai.api_key:
        raise EnvironmentError(
            "OpenAI API key not set. "
            "Please set the OPENAI_API_KEY environment variable or add it to the USER CONFIG."
        )

    md_files = [f for f in os.listdir(ENRICHED_MD_FOLDER) if f.lower().endswith(".md")]
    print(f"Found {len(md_files)} enriched Markdown file(s) to process.\n")

    for md_file in md_files:
        paper_name = os.path.splitext(md_file)[0]
        md_path    = os.path.join(ENRICHED_MD_FOLDER, md_file)
        print(f"Processing paper: {paper_name}")
        process_paper(md_path, paper_name, OUTPUT_JSON_FOLDER)
        print()

    print("Done — Step 3  |  JSON outputs saved to:", OUTPUT_JSON_FOLDER)


if __name__ == "__main__":
    main()
