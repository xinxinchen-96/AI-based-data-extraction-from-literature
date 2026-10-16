#!/usr/bin/env cwl-runner

class: Workflow
cwlVersion: v1.2

inputs:
- id: icasa_template
  type: File
- id: evaluation_folder_name
  type: string
- id: processed_folder_name
  type: string
- id: json_folder_name
  type: string
- id: tabular_folder_name
  type: string
- id: llm_output_json
  type: Directory
- id: llm_tabular_folder_name
  type: string
- id: training_data_folder_name
  type: string
- id: md_folder
  type: Directory

outputs:
- id: evaluation_directory
  outputSource: evaluation/output_directory
  type: Directory
- id: training_data
  outputSource: create_training_data/output_folder
  type: Directory
- id: processed_papers
  outputSource: process_paper/output_directory
  type: Directory
- id: icasa_json
  outputSource: generate_icasa_json/icasa_json_outputs
  type: Directory
- id: manual_tabular
  outputSource: json_to_xlsx/output_directory
  type: Directory
- id: tabular_llm
  outputSource: merge/merged_data
  type: Directory

requirements:
- class: SubworkflowFeatureRequirement

steps:
- id: process_paper
  in:
  - id: output_folder
    source: processed_folder_name
  - id: input_folder
    source: md_folder
  out:
  - output_directory
  run: ../generate_training_data/process_paper.cwl
- id: generate_icasa_json
  in:
  - id: template_path
    source: icasa_template
  - id: json_folder_name
    source: json_folder_name
  out:
  - icasa_json_outputs
  run: ../generate_icasa_json/generate_icasa_json.cwl
- id: json_to_xlsx
  in:
  - id: input_folder
    source: generate_icasa_json/icasa_json_outputs
  - id: output_folder
    source: tabular_folder_name
  out:
  - output_directory
  run: ../generate_manual_data/json_to_xlsx.cwl
- id: create_training_data
  in:
  - id: json_folder
    source: generate_icasa_json/icasa_json_outputs
  - id: markdown_folder
    source: process_paper/output_directory
  - id: output_directory_name
    source: training_data_folder_name
  out:
  - output_folder
  run: ../generate_training_data/create_training_data.cwl
- id: json2tabular_exp_metadata
  in:
  - id: input_folder
    source: split/context_metadata_dir
  out:
  - output_directory
  run: ../json2tabular/json2tabular_exp_metadata.cwl
- id: json2tabular_fertilizeration_improved
  in:
  - id: input_folder
    source: split/fertilizers_dir
  out:
  - output_directory
  run: ../json2tabular/json2tabular_fertilizeration_improved.cwl
- id: json2tabular_fields
  in:
  - id: input_folder
    source: split/fields_dir
  out:
  - output_directory
  run: ../json2tabular/json2tabular_fields.cwl
- id: json2tabular_genotype
  in:
  - id: input_folder
    source: split/genotypes_dir
  out:
  - output_directory
  run: ../json2tabular/json2tabular_genotype.cwl
- id: json2tabular_harvest
  in:
  - id: input_folder
    source: split/harvests_dir
  out:
  - output_directory
  run: ../json2tabular/json2tabular_harvest.cwl
- id: json2tabular_irrigation
  in:
  - id: input_folder
    source: split/irrigations_dir
  out:
  - output_directory
  run: ../json2tabular/json2tabular_irrigation.cwl
- id: json2tabular_planting
  in:
  - id: input_folder
    source: split/plantings_dir
  out:
  - output_directory
  run: ../json2tabular/json2tabular_planting.cwl
- id: json2tabular_plotdetails
  in:
  - id: input_folder
    source: split/plot_details_dir
  out:
  - output_directory
  run: ../json2tabular/json2tabular_plotdetails.cwl
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
  run: evaluation.cwl
- id: split
  in:
  - id: llm_output_json
    source: llm_output_json
  out:
  - context_metadata_dir
  - fertilizers_dir
  - fields_dir
  - genotypes_dir
  - harvests_dir
  - irrigations_dir
  - plantings_dir
  - plot_details_dir
  run: ../util/split.cwl
- id: merge
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
  - id: output_folder_name
    source: llm_tabular_folder_name
  out:
  - merged_data
  run: ../util/merge.cwl
