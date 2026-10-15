#!/usr/bin/env cwl-runner

cwlVersion: v1.2
class: CommandLineTool

requirements:
- class: InitialWorkDirRequirement
  listing:
  - $(inputs.llm_output_json)

inputs:
- id: llm_output_json
  type: Directory
  default:
    class: Directory
    location: ../../data/07_llm_output_json

outputs:
- id: context_metadata_dir
  type: Directory
  outputBinding:
    glob: $(inputs.llm_output_json.basename)/context_metadata
- id: fertilizers_dir
  type: Directory
  outputBinding:
    glob: $(inputs.llm_output_json.basename)/fertilizers
- id: fields_dir
  type: Directory
  outputBinding:
    glob: $(inputs.llm_output_json.basename)/fields
- id: genotypes_dir
  type: Directory
  outputBinding:
    glob: $(inputs.llm_output_json.basename)/genotypes
- id: harvests_dir
  type: Directory
  outputBinding:
    glob: $(inputs.llm_output_json.basename)/harvests
- id: irrigations_dir
  type: Directory
  outputBinding:
    glob: $(inputs.llm_output_json.basename)/irrigations
- id: plantings_dir
  type: Directory
  outputBinding:
    glob: $(inputs.llm_output_json.basename)/plantings
- id: plot_details_dir
  type: Directory
  outputBinding:
    glob: $(inputs.llm_output_json.basename)/plot_details

baseCommand: "true"