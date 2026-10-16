#!/usr/bin/env cwl-runner

cwlVersion: v1.2
class: CommandLineTool

requirements:
- class: InitialWorkDirRequirement
  listing:
  - entryname: R/generate_icasa_json.R
    entry:
      $include: ../../R/generate_icasa_json.R
  - entryname: R/icasa_attributes_config.R
    entry: $(inputs.icasa_attributes)
- class: DockerRequirement
  dockerFile:
    $include: ../../Dockerfile.renv
  dockerImageId: renv-container

inputs:
- id: template_path
  type: File
  default:
    class: File
    location: ../../data/03_icasa_template/icasa_template_allColumns.xlsm
  inputBinding:
    prefix: --template_path
- id: json_folder_name
  type: string
  default: manual_json
  inputBinding:
    prefix: --json_folder
- id: icasa_attributes
  doc: "constant ICASA attribute names" 
  type: File
  default:
    class: File
    location: ../../R/icasa_attributes_config.R

outputs:
- id: icasa_json_outputs
  type: Directory
  outputBinding:
    glob: $(inputs.json_folder_name)

baseCommand:
- Rscript
- R/generate_icasa_json.R
