#!/usr/bin/env cwl-runner

doc: |
  This CWL File is of type Operation which means it is an abstract description of a process.
  It describes the manual fine tuning of the GPT Models on the OpenAI Platform. 
class: Operation
cwlVersion: v1.2
inputs:
- id: training_data
  type: Directory
outputs:
- id: context_metadata_model_id
  type: string?
- id: fields_model_id
  type: string?
- id: genotypes_model_id
  type: string?
- id: plantings_model_id
  type: string?
- id: irrigations_model_id
  type: string?
- id: fertilizers_model_id
  type: string?
- id: harvests_model_id
  type: string?
- id: plot_details_model_id
  type: string?
