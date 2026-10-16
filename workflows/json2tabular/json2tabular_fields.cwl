#!/usr/bin/env cwl-runner

cwlVersion: v1.2
class: CommandLineTool

requirements:
- class: InitialWorkDirRequirement
  listing:
  - entryname: R/json2tabular_fields.R
    entry:
      $include: ../../R/json2tabular_fields.R
- class: DockerRequirement
  dockerFile:
    $include: ../../Dockerfile.renv
  dockerImageId: renv-container

inputs:
- id: input_folder
  type: Directory
  default:
    class: Directory
    location: ../../data/07_llm_output_json
  inputBinding:
    prefix: --input_folder
- id: output_folder
  type: string
  default: llm_output_tabular/fields
  inputBinding:
    prefix: --output_folder

outputs:
- id: output_directory
  type: Directory
  outputBinding:
    glob: $(inputs.output_folder)

baseCommand:
- Rscript
- R/json2tabular_fields.R
