#!/usr/bin/env cwl-runner

class: Workflow
cwlVersion: v1.2

inputs:
- id: llm_output_json
  type: Directory

outputs:
- id: harvest
  outputSource: json2tabular_harvest/output_directory
  type: Directory
- id: fertilizers
  outputSource: json2tabular_fertilizeration_improved/output_directory
  type: Directory
- id: plantings
  outputSource: json2tabular_planting/output_directory
  type: Directory
- id: plot_details
  outputSource: json2tabular_plotdetails/output_directory
  type: Directory
- id: irrigations
  outputSource: json2tabular_irrigation/output_directory
  type: Directory
- id: fields
  outputSource: json2tabular_fields/output_directory
  type: Directory
- id: genotypes
  outputSource: json2tabular_genotype/output_directory
  type: Directory
- id: exp_metadata
  outputSource: json2tabular_exp_metadata/output_directory
  type: Directory

requirements:
- class: SubworkflowFeatureRequirement

steps:
- id: json2tabular_exp_metadata
  in:
  - id: input_folder
    source: split/context_metadata_dir
  out:
  - output_directory
  run: ../json2tabular/json2tabular_exp_metadata.cwl
- id: json2tabular_genotype
  in:
  - id: input_folder
    source: split/genotypes_dir
  out:
  - output_directory
  run: ../json2tabular/json2tabular_genotype.cwl
- id: json2tabular_fields
  in:
  - id: input_folder
    source: split/fields_dir
  out:
  - output_directory
  run: ../json2tabular/json2tabular_fields.cwl
- id: json2tabular_irrigation
  in:
  - id: input_folder
    source: split/irrigations_dir
  out:
  - output_directory
  run: ../json2tabular/json2tabular_irrigation.cwl
- id: json2tabular_plotdetails
  in:
  - id: input_folder
    source: split/plot_details_dir
  out:
  - output_directory
  run: ../json2tabular/json2tabular_plotdetails.cwl
- id: json2tabular_planting
  in:
  - id: input_folder
    source: split/plantings_dir
  out:
  - output_directory
  run: ../json2tabular/json2tabular_planting.cwl
- id: json2tabular_fertilizeration_improved
  in:
  - id: input_folder
    source: split/fertilizers_dir
  out:
  - output_directory
  run: ../json2tabular/json2tabular_fertilizeration_improved.cwl
- id: json2tabular_harvest
  in:
  - id: input_folder
    source: split/harvests_dir
  out:
  - output_directory
  run: ../json2tabular/json2tabular_harvest.cwl
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
