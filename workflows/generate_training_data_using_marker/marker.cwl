#!/usr/bin/env cwl-runner


cwlVersion: v1.2
class: CommandLineTool

requirements:
- class: DockerRequirement
  dockerFile:
    $include: ../../Dockerfile.marker
  dockerImageId: sciwin-container
- class: NetworkAccess
  networkAccess: true

inputs:
- id: pdf_directory
  type: Directory
  default:
    class: Directory
    location: ../../data/00_paper_list
  inputBinding:
    position: 0
- id: output_dir_name
  type: string
  default: paper_to_md
  inputBinding:
    prefix: --output_dir

outputs:
- id: output_directory
  type: Directory
  outputBinding:
    glob: $(inputs.output_dir_name)

baseCommand: marker
