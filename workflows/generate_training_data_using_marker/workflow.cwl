#!/usr/bin/env cwl-runner

class: Workflow

inputs:
- id: pdf_directory
  type: Directory
- id: icasa_template
  type: File
- id: training_data_dirname
  type: string

outputs:
- id: training_data
  outputSource: workflow/training_data
  type: Directory

requirements:
- class: SubworkflowFeatureRequirement

steps:
- id: marker
  in:
  - id: pdf_directory
    source: pdf_directory
  out:
  - output_directory
  run: marker.cwl
- id: workflow
  in:
  - id: markdown_papers
    source: marker/output_directory
  - id: icasa_template
    source: icasa_template
  - id: training_data_dirname
    source: training_data_dirname
  out:
  - training_data
  run: ../generate_training_data/workflow.cwl
