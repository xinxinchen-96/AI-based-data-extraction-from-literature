#!/usr/bin/env cwl-runner

cwlVersion: v1.2
class: CommandLineTool

requirements:
- class: ShellCommandRequirement
- class: DockerRequirement
  dockerPull: docker.io/bash:4.4
- class: InitialWorkDirRequirement
  listing:
  - $(inputs.context_metadata_dir)
  - $(inputs.fertilizers_dir)
  - $(inputs.fields_dir)
  - $(inputs.genotypes_dir)
  - $(inputs.harvests_dir)
  - $(inputs.irrigations_dir)
  - $(inputs.plantings_dir)
  - $(inputs.plot_details_dir)

inputs:
- id: context_metadata_dir
  type: Directory
- id: fertilizers_dir
  type: Directory
- id: fields_dir
  type: Directory
- id: genotypes_dir
  type: Directory
- id: harvests_dir
  type: Directory
- id: irrigations_dir
  type: Directory
- id: plantings_dir
  type: Directory
- id: plot_details_dir
  type: Directory
- id: output_folder_name
  type: string

outputs:
  merged_data:
    type: Directory
    outputBinding:
      glob: $(inputs.output_folder_name)

baseCommand:
- bash
- -c

arguments:
- |
  shopt -s extglob
  mkdir $(inputs.output_folder_name)
  cp -RL !($(inputs.output_folder_name)) $(inputs.output_folder_name)
