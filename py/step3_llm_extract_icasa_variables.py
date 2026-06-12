# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 16:23:20 2025

@author: xinxin

Step 3 — Use a fine-tuned OpenAI GPT model to extract ICASA-structured variables
          from enriched Markdown files.
 
Usage:
    1. Set your OpenAI API key as an environment variable:
           Windows:  setx OPENAI_API_KEY "sk-..."
    2. Set all paths and fine-tuned model IDs in the USER CONFIG section below.
    3. Run:  python step3_llm_extract_icasa_variables.py
 
Input:
    - Folder of enriched Markdown files (from Step 2.7)
Output:
    - One .txt file per paper per ICASA category
      saved under OUTPUT_FOLDER/<same subfolder structure as input>/
 
ICASA categories processed:
    fields, genotypes, plantings, irrigations, fertilizers,
    harvests, plot_details, 
"""
 
import os
import openai
 

# =============================================================================
# === USER CONFIG =============================================================
# =============================================================================

# OpenAI API key — prefer environment variable over hard-coding
openai.api_key = os.getenv("OPENAI_API_KEY")  # set env var OPENAI_API_KEY

# Fine-tuned model IDs — replace with your own fine-tuned model names
FINE_TUNED_MODELS = {
    "context_metadata" : "ft:gpt-4.1-mini-2025-04-14:personal:context-YOUR_ID",  # example
    "fields"       : "ft:gpt-4.1-mini-2025-04-14:personal:fields-YOUR_ID",
    "genotypes"    : "ft:gpt-4.1-mini-2025-04-14:personal:genotypes-YOUR_ID",
    "plantings"    : "ft:gpt-4.1-mini-2025-04-14:personal:plantings-YOUR_ID",
    "irrigations"   : "ft:gpt-4.1-mini-2025-04-14:personal:irrigations-YOUR_ID",
    "fertilizers"  : "ft:gpt-4.1-mini-2025-04-14:personal:fertilizers-YOUR_ID",
    "harvests"     : "ft:gpt-4.1-mini-2025-04-14:personal:harvests-YOUR_ID",
    "plot_details" : "ft:gpt-4.1-mini-2025-04-14:personal:plot-details-YOUR_ID",
}

# Paths
MARKDOWN_FOLDER = r"C:\your\path\to\02_final_processed_md"
OUTPUT_FOLDER   = r"C:\your\path\to\07_llm_output_json"


# =============================================================================

client = openai.OpenAI()

# ICASA categories and the prompt instruction for each
CATEGORY_PROMPTS = {
    "context_metadata" : (
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
    "irrigations" : (
        "Extract ICASA irrigations applied events variables from this content:"
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


def save_file(path, content_str):
    """Save raw LLM response string to a .json file."""
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content_str)
    except Exception as e:
        print(f"  Error saving {path}: {e}")



def call_llm(model_id: str, content: str, prompt_prefix: str) -> str:
    """Send content to the fine-tuned model and return the response text."""
    try:
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are an expert in agriculture."},
                {"role": "user",   "content": f"{prompt_prefix} {content}"},
                ],
            temperature=0,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"  LLM call failed: {e}")
        return ""
    
CATEGORIES = [
    "fields",
    "genotypes",
    "plantings",
    "irrigations",
    "fertilizers",
    "harvests",
    "plot_details"
]
 

def process_file(md_path: str, output_base: str, paper_stem: str) -> None:
    """Run all active category extractions for a single Markdown file."""
    content = read_file(md_path)
    if not content:
        return
 
    for category in CATEGORIES:
        model_id = FINE_TUNED_MODELS.get(category)
        if not model_id:
            print(f"  Skipping '{category}' — no model ID configured.")
            continue
 
        prompt_prefix = CATEGORY_PROMPTS.get(category)
        if not prompt_prefix:
            print(f"  Skipping '{category}' — no prompt configured.")
            continue
 
        print(f"  [{category}] calling model {model_id.split(':')[-1]} ...")
        result = call_llm(model_id, content, prompt_prefix)
 
        if result:
            out_path = os.path.join(output_base, f"{paper_stem}_{category}.txt")
            save_file(out_path, result)
            print(f"    Saved -> {out_path}")
        else:
            print(f"    No result for [{category}].")
 
 
def main() -> None:
    if not openai.api_key:
        raise EnvironmentError(
            "OpenAI API key not set. "
            "Please set the OPENAI_API_KEY environment variable."
        )
 
    total = 0
    for root, _, files in os.walk(MARKDOWN_FOLDER):
        for file_name in files:
            if not file_name.lower().endswith(".md"):
                continue
 
            md_path = os.path.join(root, file_name)
            paper_stem = os.path.splitext(file_name)[0]
 
            # Mirror the subfolder structure in the output directory
            rel_path = os.path.relpath(root, MARKDOWN_FOLDER)
            out_dir = os.path.join(OUTPUT_FOLDER, rel_path)
 
            print(f"\nProcessing: {md_path}")
            process_file(md_path, out_dir, paper_stem)
            total += 1
 
    print(f"\nDone — processed {total} file(s). Outputs saved to: {OUTPUT_FOLDER}")
 
 
if __name__ == "__main__":
    main()