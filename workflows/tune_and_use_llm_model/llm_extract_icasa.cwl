#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: CommandLineTool
$namespaces:
  cwltool: http://commonwl.org/cwltool

requirements:
- class: InitialWorkDirRequirement
  listing:
  - entryname: py/step3_llm_extract_icasa_variables.py
    entry:
      $include: ../../py/step3_llm_extract_icasa_variables.py
- class: DockerRequirement
  dockerFile:
    $include: ../../Dockerfile.python
  dockerImageId: python-container
- class: EnvVarRequirement
  envDef:
    OPENAI_API_KEY: $(inputs.openai_api_key)

inputs:
- id: openai_api_key
  type: string
- id: input_folder
  type: Directory
  inputBinding:
    prefix: --input_folder
- id: output_folder
  type: string
  inputBinding:
    prefix: --output_folder
- id: context_metadata_model
  type: string?
  inputBinding:
    prefix: --context_metadata_model
- id: fields_model
  type: string?
  inputBinding:
    prefix: --fields_model
- id: genotypes_model
  type: string?
  inputBinding:
    prefix: --genotypes_model
- id: plantings_model
  type: string?
  inputBinding:
    prefix: --plantings_model
- id: irrigations_model
  type: string?
  inputBinding:
    prefix: --irrigations_model
- id: fertilizers_model
  type: string?
  inputBinding:
    prefix: --fertilizers_model
- id: harvests_model
  type: string?
  inputBinding:
    prefix: --harvests_model
- id: plot_details_model
  type: string?
  inputBinding:
    prefix: --plot_details_model

outputs:
- id: llm_output_json
  type: Directory
  outputBinding:
    glob: $(inputs.output_folder)

baseCommand:
- python3
- py/step3_llm_extract_icasa_variables.py

hints:
  cwltool:Secrets:
    secrets:
    - token
