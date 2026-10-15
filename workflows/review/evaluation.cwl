#!/usr/bin/env cwl-runner

cwlVersion: v1.2
class: CommandLineTool

requirements:
- class: InitialWorkDirRequirement
  listing:
  - entryname: py/step4_evaluation.py
    entry:
      $include: ../../py/step4_evaluation.py
- class: DockerRequirement
  dockerFile:
    $include: ../../Dockerfile.python
  dockerImageId: python-container

inputs:
- id: reference_data
  type: Directory
  default:
    class: Directory
    location: ../../data/05_manual_tabular
  inputBinding:
    prefix: --reference_data
- id: output_folder
  type: string
  default: evaluation
  inputBinding:
    prefix: --output_folder
- id: context_metadata_dir
  type: Directory
  default:
    class: Directory
    location: ../../data/08_llm_output_tabular/context_metadata
  inputBinding:
    prefix: --context_metadata_dir
- id: genotypes_dir
  type: Directory
  default:
    class: Directory
    location: ../../data/08_llm_output_tabular/genotypes
  inputBinding:
    prefix: --genotypes_dir
- id: fields_dir
  type: Directory
  default:
    class: Directory
    location: ../../data/08_llm_output_tabular/fields
  inputBinding:
    prefix: --fields_dir
- id: plantings_dir
  type: Directory
  default:
    class: Directory
    location: ../../data/08_llm_output_tabular/plantings
  inputBinding:
    prefix: --plantings_dir
- id: irrigations_dir
  type: Directory
  default:
    class: Directory
    location: ../../data/08_llm_output_tabular/irrigations
  inputBinding:
    prefix: --irrigations_dir
- id: fertilizers_dir
  type: Directory
  default:
    class: Directory
    location: ../../data/08_llm_output_tabular/fertilizers
  inputBinding:
    prefix: --fertilizers_dir
- id: plot_details_dir
  type: Directory
  default:
    class: Directory
    location: ../../data/08_llm_output_tabular/plot_details
  inputBinding:
    prefix: --plot_details_dir
- id: harvests_dir
  type: Directory
  default:
    class: Directory
    location: ../../data/08_llm_output_tabular/harvests
  inputBinding:
    prefix: --harvests_dir

outputs:
- id: output_directory
  type: Directory
  outputBinding:
    glob: $(inputs.output_folder)

baseCommand:
- python3
- py/step4_evaluation.py
