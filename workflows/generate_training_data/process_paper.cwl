#!/usr/bin/env cwl-runner

cwlVersion: v1.2
class: CommandLineTool

requirements:
- class: InitialWorkDirRequirement
  listing:
  - entryname: py/step2_process_paper.py
    entry:
      $include: ../../py/step2_process_paper.py

inputs:
- id: input_folder
  type: Directory
  default:
    class: Directory
    location: ../../data/01_paper_to_md
  inputBinding:
    prefix: --input_folder
- id: output_folder
  type: string
  default: data/02_final_processed_md
  inputBinding:
    prefix: --output_folder

outputs:
- id: output_directory
  type: Directory
  outputBinding:
    glob: $(inputs.output_folder)

baseCommand:
- python3
- py/step2_process_paper.py
