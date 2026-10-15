#!/usr/bin/env cwl-runner

cwlVersion: v1.2
class: Workflow
label: create_manual_xlsx

requirements:
- class: SubworkflowFeatureRequirement

inputs:
- id: icasa_template
  type: File
- id: xlsx_dirname
  type: string

outputs:
- id: manual_json
  type: Directory
  outputSource: json_to_xlsx/output_directory

steps:
- id: json_to_xlsx
  in:
  - id: input_folder
    source: generate_icasa_json/icasa_json_outputs
  - id: output_folder
    source: xlsx_dirname
  run: json_to_xlsx.cwl
  out:
  - output_directory
- id: generate_icasa_json
  in:
  - id: template_path
    source: icasa_template
  run: ../generate_icasa_json/generate_icasa_json.cwl
  out:
  - icasa_json_outputs
