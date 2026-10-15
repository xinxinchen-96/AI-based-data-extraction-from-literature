#!/usr/bin/env cwl-runner

cwlVersion: v1.2
class: Workflow

requirements:
- class: SubworkflowFeatureRequirement

inputs:
- id: markdown_papers
  type: Directory
- id: icasa_template
  type: File
- id: training_data_dirname
  type: string

outputs:
- id: training_data
  type: Directory
  outputSource: create_training_data/output_folder

steps:
- id: create_training_data
  in:
  - id: markdown_folder
    source: process_paper/output_directory
  - id: json_folder
    source: generate_icasa_json/icasa_json_outputs
  - id: output_directory_name
    source: training_data_dirname
  run: create_training_data.cwl
  out:
  - output_folder
- id: process_paper
  in:
  - id: input_folder
    source: markdown_papers
  run: process_paper.cwl
  out:
  - output_directory
- id: generate_icasa_json
  in:
  - id: template_path
    source: icasa_template
  run: ../generate_icasa_json/generate_icasa_json.cwl
  out:
  - icasa_json_outputs
