#!/usr/bin/env cwl-runner

class: Workflow

inputs:
- id: pdf_files
  type: Directory
- id: icasa_template
  type: File
- id: openai_api_key
  type: string
- id: evaluation_folder_name
  type: string

outputs:
- id: evaluation_directory
  outputSource: evaluation/output_directory
  type: Directory

requirements:
- class: SubworkflowFeatureRequirement

steps:
- id: marker
  in:
  - id: pdf_directory
    source: pdf_files
  out:
  - output_directory
  run: generate_training_data_using_marker/marker.cwl
- id: process_paper
  in:
  - id: input_folder
    source: marker/output_directory
  out:
  - output_directory
  run: generate_training_data/process_paper.cwl
- id: generate_icasa_json
  in:
  - id: template_path
    source: icasa_template
  out:
  - icasa_json_outputs
  run: generate_icasa_json/generate_icasa_json.cwl
- id: json_to_xlsx
  in:
  - id: input_folder
    source: generate_icasa_json/icasa_json_outputs
  out:
  - output_directory
  run: generate_manual_data/json_to_xlsx.cwl
- id: create_training_data
  in:
  - id: json_folder
    source: generate_icasa_json/icasa_json_outputs
  - id: markdown_folder
    source: process_paper/output_directory
  out:
  - output_folder
  run: generate_training_data/create_training_data.cwl
- id: llm_extract_icasa
  in:
  - id: fields_model
    source: fine_tune_model/fields_model_id
  - id: context_metadata_model
    source: fine_tune_model/context_metadata_model_id
  - id: genotypes_model
    source: fine_tune_model/genotypes_model_id
  - id: plantings_model
    source: fine_tune_model/plantings_model_id
  - id: irrigations_model
    source: fine_tune_model/irrigations_model_id
  - id: fertilizers_model
    source: fine_tune_model/fertilizers_model_id
  - id: harvests_model
    source: fine_tune_model/harvests_model_id
  - id: plot_details_model
    source: fine_tune_model/plot_details_model_id
  - id: input_folder
    source: process_paper/output_directory
  - id: openai_api_key
    source: openai_api_key
  out:
  - llm_output_json
  run: tune_and_use_llm_model/llm_extract_icasa.cwl
- id: fine_tune_model
  in:
  - id: training_data
    source: create_training_data/output_folder
  out:
  - context_metadata_model_id
  - fields_model_id
  - genotypes_model_id
  - plantings_model_id
  - irrigations_model_id
  - fertilizers_model_id
  - harvests_model_id
  - plot_details_model_id
  run: tune_and_use_llm_model/fine_tune_model.cwl
- id: json2tabular_exp_metadata
  in:
  - id: input_folder
    source: llm_extract_icasa/llm_output_json
  out:
  - output_directory
  run: json2tabular/json2tabular_exp_metadata.cwl
- id: json2tabular_fertilizeration_improved
  in:
  - id: input_folder
    source: llm_extract_icasa/llm_output_json
  out:
  - output_directory
  run: json2tabular/json2tabular_fertilizeration_improved.cwl
- id: json2tabular_fields
  in:
  - id: input_folder
    source: llm_extract_icasa/llm_output_json
  out:
  - output_directory
  run: json2tabular/json2tabular_fields.cwl
- id: json2tabular_genotype
  in:
  - id: input_folder
    source: llm_extract_icasa/llm_output_json
  out:
  - output_directory
  run: json2tabular/json2tabular_genotype.cwl
- id: json2tabular_harvest
  in:
  - id: input_folder
    source: llm_extract_icasa/llm_output_json
  out:
  - output_directory
  run: json2tabular/json2tabular_harvest.cwl
- id: json2tabular_irrigation
  in:
  - id: input_folder
    source: llm_extract_icasa/llm_output_json
  out:
  - output_directory
  run: json2tabular/json2tabular_irrigation.cwl
- id: json2tabular_planting
  in:
  - id: input_folder
    source: llm_extract_icasa/llm_output_json
  out:
  - output_directory
  run: json2tabular/json2tabular_planting.cwl
- id: json2tabular_plotdetails
  in:
  - id: input_folder
    source: llm_extract_icasa/llm_output_json
  out:
  - output_directory
  run: json2tabular/json2tabular_plotdetails.cwl
- id: evaluation
  in:
  - id: plot_details_dir
    source: json2tabular_plotdetails/output_directory
  - id: plantings_dir
    source: json2tabular_planting/output_directory
  - id: irrigations_dir
    source: json2tabular_irrigation/output_directory
  - id: harvests_dir
    source: json2tabular_harvest/output_directory
  - id: genotypes_dir
    source: json2tabular_genotype/output_directory
  - id: fields_dir
    source: json2tabular_fields/output_directory
  - id: fertilizers_dir
    source: json2tabular_fertilizeration_improved/output_directory
  - id: context_metadata_dir
    source: json2tabular_exp_metadata/output_directory
  - id: reference_data
    source: json_to_xlsx/output_directory
  - id: output_folder
    source: evaluation_folder_name
  out:
  - output_directory
  run: review/evaluation.cwl
