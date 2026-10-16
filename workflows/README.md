# Workflows
This folder contains multiple CWL (Common Workflow Language) Descriptions of the given R- and Python-Scripts. CWL is used to wrap Steps into `CommandLineTool`s which are combined to multiple Workflows. However one step `fine_tune_model` requires manual work. This is representated by an abstract description of type `Operation` making all workflows that contain this step non-executable.

Some of the Workflows contained herein and described herafter are for the validation of data to circumvent the problem of the manual `fine_tune_model` step and also the `llm_extract_icasa` step which needs an API key to use the fine-tuned models on OpenAI Platform. The Results of the combination of those steps in `tune_and_use_llm_model` are stored in this repository at `/data/07_llm_output_json`.
The `marker` step which converts PDFs to markdown is also not used in most of the executable steps as the PDFs are not part of this repository due to copyright limitations. Its output is located at `data/01_paper_to_md`.

Example commands on how to execute are shown in `.github/workflows/check_executable.yaml` which is a GitHub Action that confirms those workflows are runnable.

To run workflows a runner such as [`cwltool`](https://github.com/common-workflow-language/cwltool) is needed: `pip install cwltool`. Furthermore `docker` (or a similiar technology) needs to be installed on the executing system.

## Main Workflow
The main workflow file is located in this folder called `workflow.cwl` which represents a **non-executable** representation of the full pipeline including the beforementioned non-executable description of the `fine-tune_model` step. 
```mermaid
---
config:
  theme: base
  look: neo
  themeVariables:
    primaryColor: '#C5E0B4'
    primaryTextColor: '#231f20'
    secondaryColor: '#EEEEEE'
    lineColor: '#385723'    
    fontSize: 12px
    tertiaryTextColor: '#231f20'
    fontFamily: 'Fira Sans, trebuchet ms, verdana, arial'
---
flowchart TB
  linkStyle default stroke:#385723,stroke-width: 2px;
  subgraph inputs[Workflow Inputs]
    direction TB
    pdf_files(pdf_files)
    icasa_template(icasa_template)
    openai_api_key(openai_api_key)
    evaluation_folder_name(evaluation_folder_name)
  end
  subgraph outputs[Workflow Outputs]
    direction TB
    evaluation_directory(evaluation_directory)
  end
    marker(marker)
  pdf_files --> |pdf_directory|marker
    marker_output_dir_name(paper_to_md)
  marker_output_dir_name --> |output_dir_name|marker
    process_paper(process_paper)
  marker --> |input_folder|process_paper
    process_paper_output_folder(data/02_final_processed_md)
  process_paper_output_folder --> |output_folder|process_paper
    generate_icasa_json(generate_icasa_json)
  icasa_template --> |template_path|generate_icasa_json
    generate_icasa_json_json_folder_name(manual_json)
  generate_icasa_json_json_folder_name --> |json_folder_name|generate_icasa_json
    generate_icasa_json_icasa_attributes(../../R/icasa_attributes_config.R)
  generate_icasa_json_icasa_attributes --> |icasa_attributes|generate_icasa_json
    json_to_xlsx(json_to_xlsx)
  generate_icasa_json --> |input_folder|json_to_xlsx
    json_to_xlsx_output_folder(output_folder)
  json_to_xlsx_output_folder --> |output_folder|json_to_xlsx
    create_training_data(create_training_data)
  generate_icasa_json --> |json_folder|create_training_data
  process_paper --> |markdown_folder|create_training_data
    create_training_data_output_directory_name(training_data)
  create_training_data_output_directory_name --> |output_directory_name|create_training_data
    create_training_data_icasa_attributes(../../R/icasa_attributes_config.R)
  create_training_data_icasa_attributes --> |icasa_attributes|create_training_data
    llm_extract_icasa(llm_extract_icasa)
  fine_tune_model --> |fields_model|llm_extract_icasa
  fine_tune_model --> |context_metadata_model|llm_extract_icasa
  fine_tune_model --> |genotypes_model|llm_extract_icasa
  fine_tune_model --> |plantings_model|llm_extract_icasa
  fine_tune_model --> |irrigations_model|llm_extract_icasa
  fine_tune_model --> |fertilizers_model|llm_extract_icasa
  fine_tune_model --> |harvests_model|llm_extract_icasa
  fine_tune_model --> |plot_details_model|llm_extract_icasa
  process_paper --> |input_folder|llm_extract_icasa
  openai_api_key --> |openai_api_key|llm_extract_icasa
    fine_tune_model(fine_tune_model)
  create_training_data --> |training_data|fine_tune_model
    json2tabular_exp_metadata(json2tabular_exp_metadata)
  llm_extract_icasa --> |input_folder|json2tabular_exp_metadata
    json2tabular_exp_metadata_output_folder(llm_output_tabular/exp_metadata)
  json2tabular_exp_metadata_output_folder --> |output_folder|json2tabular_exp_metadata
    json2tabular_fertilizeration_improved(json2tabular_fertilizeration_improved)
  llm_extract_icasa --> |input_folder|json2tabular_fertilizeration_improved
    json2tabular_fertilizeration_improved_output_folder(llm_output_tabular/fertilizers)
  json2tabular_fertilizeration_improved_output_folder --> |output_folder|json2tabular_fertilizeration_improved
    json2tabular_fields(json2tabular_fields)
  llm_extract_icasa --> |input_folder|json2tabular_fields
    json2tabular_fields_output_folder(llm_output_tabular/fields)
  json2tabular_fields_output_folder --> |output_folder|json2tabular_fields
    json2tabular_genotype(json2tabular_genotype)
  llm_extract_icasa --> |input_folder|json2tabular_genotype
    json2tabular_genotype_output_folder(llm_output_tabular/genotypes)
  json2tabular_genotype_output_folder --> |output_folder|json2tabular_genotype
    json2tabular_harvest(json2tabular_harvest)
  llm_extract_icasa --> |input_folder|json2tabular_harvest
    json2tabular_harvest_output_folder(llm_output_tabular/harvests)
  json2tabular_harvest_output_folder --> |output_folder|json2tabular_harvest
    json2tabular_irrigation(json2tabular_irrigation)
  llm_extract_icasa --> |input_folder|json2tabular_irrigation
    json2tabular_irrigation_output_folder(llm_output_tabular/irrigations)
  json2tabular_irrigation_output_folder --> |output_folder|json2tabular_irrigation
    json2tabular_planting(json2tabular_planting)
  llm_extract_icasa --> |input_folder|json2tabular_planting
    json2tabular_planting_output_folder(llm_output_tabular/plantings)
  json2tabular_planting_output_folder --> |output_folder|json2tabular_planting
    json2tabular_plotdetails(json2tabular_plotdetails)
  llm_extract_icasa --> |input_folder|json2tabular_plotdetails
    json2tabular_plotdetails_output_folder(llm_output_tabular/plot_details)
  json2tabular_plotdetails_output_folder --> |output_folder|json2tabular_plotdetails
    evaluation(evaluation)
  json2tabular_plotdetails --> |plot_details_dir|evaluation
  json2tabular_planting --> |plantings_dir|evaluation
  json2tabular_irrigation --> |irrigations_dir|evaluation
  json2tabular_harvest --> |harvests_dir|evaluation
  json2tabular_genotype --> |genotypes_dir|evaluation
  json2tabular_fields --> |fields_dir|evaluation
  json2tabular_fertilizeration_improved --> |fertilizers_dir|evaluation
  json2tabular_exp_metadata --> |context_metadata_dir|evaluation
  json_to_xlsx --> |reference_data|evaluation
  evaluation_folder_name --> |output_folder|evaluation
  evaluation --> |evaluation_directory|evaluation_directory
  style inputs fill:#EEEEEE,stroke-width:2px;
  style pdf_files stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style icasa_template stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style openai_api_key stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style evaluation_folder_name stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style outputs fill:#EEEEEE,stroke-width:2px;
  style evaluation_directory stroke:#823909,fill:#F8CBAD,stroke-width:2px;
  style marker stroke:#385723,stroke-width:2px;
  style marker_output_dir_name font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style process_paper stroke:#385723,stroke-width:2px;
  style process_paper_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style generate_icasa_json stroke:#385723,stroke-width:2px;
  style generate_icasa_json_json_folder_name font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style generate_icasa_json_icasa_attributes font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json_to_xlsx stroke:#385723,stroke-width:2px;
  style json_to_xlsx_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style create_training_data stroke:#385723,stroke-width:2px;
  style create_training_data_output_directory_name font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style create_training_data_icasa_attributes font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style llm_extract_icasa stroke:#385723,stroke-width:2px;
  style fine_tune_model stroke:#385723,stroke-width:2px;
  style json2tabular_exp_metadata stroke:#385723,stroke-width:2px;
  style json2tabular_exp_metadata_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json2tabular_fertilizeration_improved stroke:#385723,stroke-width:2px;
  style json2tabular_fertilizeration_improved_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json2tabular_fields stroke:#385723,stroke-width:2px;
  style json2tabular_fields_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json2tabular_genotype stroke:#385723,stroke-width:2px;
  style json2tabular_genotype_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json2tabular_harvest stroke:#385723,stroke-width:2px;
  style json2tabular_harvest_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json2tabular_irrigation stroke:#385723,stroke-width:2px;
  style json2tabular_irrigation_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json2tabular_planting stroke:#385723,stroke-width:2px;
  style json2tabular_planting_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json2tabular_plotdetails stroke:#385723,stroke-width:2px;
  style json2tabular_plotdetails_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style evaluation stroke:#385723,stroke-width:2px;
```
An alternative visualization without printing the default values:
```mermaid
---
config:
  theme: base
  look: neo
  themeVariables:
    primaryColor: '#C5E0B4'
    primaryTextColor: '#231f20'
    secondaryColor: '#EEEEEE'
    lineColor: '#385723'    
    fontSize: 12px
    tertiaryTextColor: '#231f20'
    fontFamily: 'Fira Sans, trebuchet ms, verdana, arial'
---
flowchart TB
  linkStyle default stroke:#385723,stroke-width: 2px;
  subgraph inputs[Workflow Inputs]
    direction TB
    pdf_files(pdf_files)
    icasa_template(icasa_template)
    openai_api_key(openai_api_key)
    evaluation_folder_name(evaluation_folder_name)
  end
  subgraph outputs[Workflow Outputs]
    direction TB
    evaluation_directory(evaluation_directory)
  end
    marker(marker)
  pdf_files --> |pdf_directory|marker
    process_paper(process_paper)
  marker --> |input_folder|process_paper
    generate_icasa_json(generate_icasa_json)
  icasa_template --> |template_path|generate_icasa_json
    json_to_xlsx(json_to_xlsx)
  generate_icasa_json --> |input_folder|json_to_xlsx
    create_training_data(create_training_data)
  generate_icasa_json --> |json_folder|create_training_data
  process_paper --> |markdown_folder|create_training_data
    llm_extract_icasa(llm_extract_icasa)
  fine_tune_model --> |fields_model|llm_extract_icasa
  fine_tune_model --> |context_metadata_model|llm_extract_icasa
  fine_tune_model --> |genotypes_model|llm_extract_icasa
  fine_tune_model --> |plantings_model|llm_extract_icasa
  fine_tune_model --> |irrigations_model|llm_extract_icasa
  fine_tune_model --> |fertilizers_model|llm_extract_icasa
  fine_tune_model --> |harvests_model|llm_extract_icasa
  fine_tune_model --> |plot_details_model|llm_extract_icasa
  process_paper --> |input_folder|llm_extract_icasa
  openai_api_key --> |openai_api_key|llm_extract_icasa
    fine_tune_model(fine_tune_model)
  create_training_data --> |training_data|fine_tune_model
    json2tabular_exp_metadata(json2tabular_exp_metadata)
  llm_extract_icasa --> |input_folder|json2tabular_exp_metadata
    json2tabular_fertilizeration_improved(json2tabular_fertilizeration_improved)
  llm_extract_icasa --> |input_folder|json2tabular_fertilizeration_improved
    json2tabular_fields(json2tabular_fields)
  llm_extract_icasa --> |input_folder|json2tabular_fields
    json2tabular_genotype(json2tabular_genotype)
  llm_extract_icasa --> |input_folder|json2tabular_genotype
    json2tabular_harvest(json2tabular_harvest)
  llm_extract_icasa --> |input_folder|json2tabular_harvest
    json2tabular_irrigation(json2tabular_irrigation)
  llm_extract_icasa --> |input_folder|json2tabular_irrigation
    json2tabular_planting(json2tabular_planting)
  llm_extract_icasa --> |input_folder|json2tabular_planting
    json2tabular_plotdetails(json2tabular_plotdetails)
  llm_extract_icasa --> |input_folder|json2tabular_plotdetails
    evaluation(evaluation)
  json2tabular_plotdetails --> |plot_details_dir|evaluation
  json2tabular_planting --> |plantings_dir|evaluation
  json2tabular_irrigation --> |irrigations_dir|evaluation
  json2tabular_harvest --> |harvests_dir|evaluation
  json2tabular_genotype --> |genotypes_dir|evaluation
  json2tabular_fields --> |fields_dir|evaluation
  json2tabular_fertilizeration_improved --> |fertilizers_dir|evaluation
  json2tabular_exp_metadata --> |context_metadata_dir|evaluation
  json_to_xlsx --> |reference_data|evaluation
  evaluation_folder_name --> |output_folder|evaluation
  evaluation --> |evaluation_directory|evaluation_directory
  style inputs fill:#EEEEEE,stroke-width:2px;
  style pdf_files stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style icasa_template stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style openai_api_key stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style evaluation_folder_name stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style outputs fill:#EEEEEE,stroke-width:2px;
  style evaluation_directory stroke:#823909,fill:#F8CBAD,stroke-width:2px;
  style marker stroke:#385723,stroke-width:2px;
  style process_paper stroke:#385723,stroke-width:2px;
  style generate_icasa_json stroke:#385723,stroke-width:2px;
  style json_to_xlsx stroke:#385723,stroke-width:2px;
  style create_training_data stroke:#385723,stroke-width:2px;
  style llm_extract_icasa stroke:#385723,stroke-width:2px;
  style fine_tune_model stroke:#385723,stroke-width:2px;
  style json2tabular_exp_metadata stroke:#385723,stroke-width:2px;
  style json2tabular_fertilizeration_improved stroke:#385723,stroke-width:2px;
  style json2tabular_fields stroke:#385723,stroke-width:2px;
  style json2tabular_genotype stroke:#385723,stroke-width:2px;
  style json2tabular_harvest stroke:#385723,stroke-width:2px;
  style json2tabular_irrigation stroke:#385723,stroke-width:2px;
  style json2tabular_planting stroke:#385723,stroke-width:2px;
  style json2tabular_plotdetails stroke:#385723,stroke-width:2px;
  style evaluation stroke:#385723,stroke-width:2px;
```

## Review Workflow
The most comprehensive subworkflow is the `review` workflow as it contains all steps which can be executed without the llm API key, the PDF files and the manual fine tuned models.

### Usage:
```
cwltool workflows/review/workflow.cwl inputs_review.yaml
```

```mermaid
---
config:
  theme: base
  look: neo
  themeVariables:
    primaryColor: '#C5E0B4'
    primaryTextColor: '#231f20'
    secondaryColor: '#EEEEEE'
    lineColor: '#385723'    
    fontSize: 12px
    tertiaryTextColor: '#231f20'
    fontFamily: 'Fira Sans, trebuchet ms, verdana, arial'
---
flowchart TB
  linkStyle default stroke:#385723,stroke-width: 2px;
  subgraph inputs[Workflow Inputs]
    direction TB
    icasa_template(icasa_template)
    evaluation_folder_name(evaluation_folder_name)
    processed_folder_name(processed_folder_name)
    json_folder_name(json_folder_name)
    tabular_folder_name(tabular_folder_name)
    llm_output_json(llm_output_json)
    llm_tabular_folder_name(llm_tabular_folder_name)
    training_data_folder_name(training_data_folder_name)
    md_folder(md_folder)
  end
  subgraph outputs[Workflow Outputs]
    direction TB
    evaluation_directory(evaluation_directory)
    training_data(training_data)
    processed_papers(processed_papers)
    icasa_json(icasa_json)
    manual_tabular(manual_tabular)
    tabular_llm(tabular_llm)
  end
    process_paper(process_paper)
  processed_folder_name --> |output_folder|process_paper
  md_folder --> |input_folder|process_paper
    generate_icasa_json(generate_icasa_json)
  icasa_template --> |template_path|generate_icasa_json
  json_folder_name --> |json_folder_name|generate_icasa_json
    generate_icasa_json_icasa_attributes(../../R/icasa_attributes_config.R)
  generate_icasa_json_icasa_attributes --> |icasa_attributes|generate_icasa_json
    json_to_xlsx(json_to_xlsx)
  generate_icasa_json --> |input_folder|json_to_xlsx
  tabular_folder_name --> |output_folder|json_to_xlsx
    create_training_data(create_training_data)
  generate_icasa_json --> |json_folder|create_training_data
  process_paper --> |markdown_folder|create_training_data
  training_data_folder_name --> |output_directory_name|create_training_data
    create_training_data_icasa_attributes(../../R/icasa_attributes_config.R)
  create_training_data_icasa_attributes --> |icasa_attributes|create_training_data
    json2tabular_exp_metadata(json2tabular_exp_metadata)
  split --> |input_folder|json2tabular_exp_metadata
    json2tabular_exp_metadata_output_folder(llm_output_tabular/exp_metadata)
  json2tabular_exp_metadata_output_folder --> |output_folder|json2tabular_exp_metadata
    json2tabular_fertilizeration_improved(json2tabular_fertilizeration_improved)
  split --> |input_folder|json2tabular_fertilizeration_improved
    json2tabular_fertilizeration_improved_output_folder(llm_output_tabular/fertilizers)
  json2tabular_fertilizeration_improved_output_folder --> |output_folder|json2tabular_fertilizeration_improved
    json2tabular_fields(json2tabular_fields)
  split --> |input_folder|json2tabular_fields
    json2tabular_fields_output_folder(llm_output_tabular/fields)
  json2tabular_fields_output_folder --> |output_folder|json2tabular_fields
    json2tabular_genotype(json2tabular_genotype)
  split --> |input_folder|json2tabular_genotype
    json2tabular_genotype_output_folder(llm_output_tabular/genotypes)
  json2tabular_genotype_output_folder --> |output_folder|json2tabular_genotype
    json2tabular_harvest(json2tabular_harvest)
  split --> |input_folder|json2tabular_harvest
    json2tabular_harvest_output_folder(llm_output_tabular/harvests)
  json2tabular_harvest_output_folder --> |output_folder|json2tabular_harvest
    json2tabular_irrigation(json2tabular_irrigation)
  split --> |input_folder|json2tabular_irrigation
    json2tabular_irrigation_output_folder(llm_output_tabular/irrigations)
  json2tabular_irrigation_output_folder --> |output_folder|json2tabular_irrigation
    json2tabular_planting(json2tabular_planting)
  split --> |input_folder|json2tabular_planting
    json2tabular_planting_output_folder(llm_output_tabular/plantings)
  json2tabular_planting_output_folder --> |output_folder|json2tabular_planting
    json2tabular_plotdetails(json2tabular_plotdetails)
  split --> |input_folder|json2tabular_plotdetails
    json2tabular_plotdetails_output_folder(llm_output_tabular/plot_details)
  json2tabular_plotdetails_output_folder --> |output_folder|json2tabular_plotdetails
    evaluation(evaluation)
  json2tabular_plotdetails --> |plot_details_dir|evaluation
  json2tabular_planting --> |plantings_dir|evaluation
  json2tabular_irrigation --> |irrigations_dir|evaluation
  json2tabular_harvest --> |harvests_dir|evaluation
  json2tabular_genotype --> |genotypes_dir|evaluation
  json2tabular_fields --> |fields_dir|evaluation
  json2tabular_fertilizeration_improved --> |fertilizers_dir|evaluation
  json2tabular_exp_metadata --> |context_metadata_dir|evaluation
  json_to_xlsx --> |reference_data|evaluation
  evaluation_folder_name --> |output_folder|evaluation
    split(split)
  llm_output_json --> |llm_output_json|split
    merge(merge)
  json2tabular_plotdetails --> |plot_details_dir|merge
  json2tabular_planting --> |plantings_dir|merge
  json2tabular_irrigation --> |irrigations_dir|merge
  json2tabular_harvest --> |harvests_dir|merge
  json2tabular_genotype --> |genotypes_dir|merge
  json2tabular_fields --> |fields_dir|merge
  json2tabular_fertilizeration_improved --> |fertilizers_dir|merge
  json2tabular_exp_metadata --> |context_metadata_dir|merge
  llm_tabular_folder_name --> |output_folder_name|merge
  evaluation --> |evaluation_directory|evaluation_directory
  create_training_data --> |training_data|training_data
  process_paper --> |processed_papers|processed_papers
  generate_icasa_json --> |icasa_json|icasa_json
  json_to_xlsx --> |manual_tabular|manual_tabular
  merge --> |tabular_llm|tabular_llm
  style inputs fill:#EEEEEE,stroke-width:2px;
  style icasa_template stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style evaluation_folder_name stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style processed_folder_name stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style json_folder_name stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style tabular_folder_name stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style llm_output_json stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style llm_tabular_folder_name stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style training_data_folder_name stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style md_folder stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style outputs fill:#EEEEEE,stroke-width:2px;
  style evaluation_directory stroke:#823909,fill:#F8CBAD,stroke-width:2px;
  style training_data stroke:#823909,fill:#F8CBAD,stroke-width:2px;
  style processed_papers stroke:#823909,fill:#F8CBAD,stroke-width:2px;
  style icasa_json stroke:#823909,fill:#F8CBAD,stroke-width:2px;
  style manual_tabular stroke:#823909,fill:#F8CBAD,stroke-width:2px;
  style tabular_llm stroke:#823909,fill:#F8CBAD,stroke-width:2px;
  style process_paper stroke:#385723,stroke-width:2px;
  style generate_icasa_json stroke:#385723,stroke-width:2px;
  style generate_icasa_json_icasa_attributes font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json_to_xlsx stroke:#385723,stroke-width:2px;
  style create_training_data stroke:#385723,stroke-width:2px;
  style create_training_data_icasa_attributes font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json2tabular_exp_metadata stroke:#385723,stroke-width:2px;
  style json2tabular_exp_metadata_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json2tabular_fertilizeration_improved stroke:#385723,stroke-width:2px;
  style json2tabular_fertilizeration_improved_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json2tabular_fields stroke:#385723,stroke-width:2px;
  style json2tabular_fields_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json2tabular_genotype stroke:#385723,stroke-width:2px;
  style json2tabular_genotype_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json2tabular_harvest stroke:#385723,stroke-width:2px;
  style json2tabular_harvest_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json2tabular_irrigation stroke:#385723,stroke-width:2px;
  style json2tabular_irrigation_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json2tabular_planting stroke:#385723,stroke-width:2px;
  style json2tabular_planting_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json2tabular_plotdetails stroke:#385723,stroke-width:2px;
  style json2tabular_plotdetails_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style evaluation stroke:#385723,stroke-width:2px;
  style split stroke:#385723,stroke-width:2px;
  style merge stroke:#385723,stroke-width:2px;
```

## Generate Manual Tabular Data
`generate_manual_data` contains a workflow which extracts the manual data from the ICASA Template into JSON which is than converted into a tabular format, more specifically XLSX. Its purpose is to generate the manual ground truth data which later is compared to the LLM generated data.

### Usage:
```
cwltool workflows/generate_manual_data/workflow.cwl inputs_generate_manual_data.yaml
```

```mermaid
---
config:
  theme: base
  look: neo
  themeVariables:
    primaryColor: '#C5E0B4'
    primaryTextColor: '#231f20'
    secondaryColor: '#EEEEEE'
    lineColor: '#385723'    
    fontSize: 12px
    tertiaryTextColor: '#231f20'
    fontFamily: 'Fira Sans, trebuchet ms, verdana, arial'
---
flowchart TB
  linkStyle default stroke:#385723,stroke-width: 2px;
  subgraph inputs[Workflow Inputs]
    direction TB
    icasa_template(icasa_template)
    xlsx_dirname(xlsx_dirname)
  end
  subgraph outputs[Workflow Outputs]
    direction TB
    manual_json(manual_json)
  end
    json_to_xlsx(json_to_xlsx)
  generate_icasa_json --> |input_folder|json_to_xlsx
  xlsx_dirname --> |output_folder|json_to_xlsx
    generate_icasa_json(generate_icasa_json)
  icasa_template --> |template_path|generate_icasa_json
    generate_icasa_json_json_folder_name(manual_json)
  generate_icasa_json_json_folder_name --> |json_folder_name|generate_icasa_json
    generate_icasa_json_icasa_attributes(../../R/icasa_attributes_config.R)
  generate_icasa_json_icasa_attributes --> |icasa_attributes|generate_icasa_json
  json_to_xlsx --> |manual_json|manual_json
  style inputs fill:#EEEEEE,stroke-width:2px;
  style icasa_template stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style xlsx_dirname stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style outputs fill:#EEEEEE,stroke-width:2px;
  style manual_json stroke:#823909,fill:#F8CBAD,stroke-width:2px;
  style json_to_xlsx stroke:#385723,stroke-width:2px;
  style generate_icasa_json stroke:#385723,stroke-width:2px;
  style generate_icasa_json_json_folder_name font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style generate_icasa_json_icasa_attributes font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
```

## Generate Training Data
`generate_training_data` contains a workflow which processes the extracted markdownfiles and generates training data in JSONL format by also using data from the ICASA template. This JSONL files need to be manually uploaded to OpenAIs Platform. That's why this workflow contains all needed steps up to this point and exits here. 
The `marker` step is left out on purpose on this workflow due to copyright limitations.

### Usage:
```
cwltool workflows/generate_training_data/workflow.cwl inputs_generate_training_data.yaml
```

```mermaid
---
config:
  theme: base
  look: neo
  themeVariables:
    primaryColor: '#C5E0B4'
    primaryTextColor: '#231f20'
    secondaryColor: '#EEEEEE'
    lineColor: '#385723'    
    fontSize: 12px
    tertiaryTextColor: '#231f20'
    fontFamily: 'Fira Sans, trebuchet ms, verdana, arial'
---
flowchart TB
  linkStyle default stroke:#385723,stroke-width: 2px;
  subgraph inputs[Workflow Inputs]
    direction TB
    markdown_papers(markdown_papers)
    icasa_template(icasa_template)
    training_data_dirname(training_data_dirname)
  end
  subgraph outputs[Workflow Outputs]
    direction TB
    training_data(training_data)
  end
    create_training_data(create_training_data)
  process_paper --> |markdown_folder|create_training_data
  generate_icasa_json --> |json_folder|create_training_data
  training_data_dirname --> |output_directory_name|create_training_data
    create_training_data_icasa_attributes(../../R/icasa_attributes_config.R)
  create_training_data_icasa_attributes --> |icasa_attributes|create_training_data
    process_paper(process_paper)
  markdown_papers --> |input_folder|process_paper
    process_paper_output_folder(data/02_final_processed_md)
  process_paper_output_folder --> |output_folder|process_paper
    generate_icasa_json(generate_icasa_json)
  icasa_template --> |template_path|generate_icasa_json
    generate_icasa_json_json_folder_name(manual_json)
  generate_icasa_json_json_folder_name --> |json_folder_name|generate_icasa_json
    generate_icasa_json_icasa_attributes(../../R/icasa_attributes_config.R)
  generate_icasa_json_icasa_attributes --> |icasa_attributes|generate_icasa_json
  create_training_data --> |training_data|training_data
  style inputs fill:#EEEEEE,stroke-width:2px;
  style markdown_papers stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style icasa_template stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style training_data_dirname stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style outputs fill:#EEEEEE,stroke-width:2px;
  style training_data stroke:#823909,fill:#F8CBAD,stroke-width:2px;
  style create_training_data stroke:#385723,stroke-width:2px;
  style create_training_data_icasa_attributes font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style process_paper stroke:#385723,stroke-width:2px;
  style process_paper_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style generate_icasa_json stroke:#385723,stroke-width:2px;
  style generate_icasa_json_json_folder_name font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style generate_icasa_json_icasa_attributes font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
```

The `marker` step can be used together with `generate_training_data` as subworkflow by using `workflows/generate_training_data_using_marker/workflow.cwl` which gives the opportunity to use this pipeline with different PDF files.
```mermaid
---
config:
  theme: base
  look: neo
  themeVariables:
    primaryColor: '#C5E0B4'
    primaryTextColor: '#231f20'
    secondaryColor: '#EEEEEE'
    lineColor: '#385723'    
    fontSize: 12px
    tertiaryTextColor: '#231f20'
    fontFamily: 'Fira Sans, trebuchet ms, verdana, arial'
---
flowchart TB
  linkStyle default stroke:#385723,stroke-width: 2px;
  subgraph inputs[Workflow Inputs]
    direction TB
    pdf_directory(pdf_directory)
    icasa_template(icasa_template)
    training_data_dirname(training_data_dirname)
  end
  subgraph outputs[Workflow Outputs]
    direction TB
    training_data(training_data)
  end
    marker(marker)
  pdf_directory --> |pdf_directory|marker
    marker_output_dir_name(paper_to_md)
  marker_output_dir_name --> |output_dir_name|marker
    workflow(workflow)
  marker --> |markdown_papers|workflow
  icasa_template --> |icasa_template|workflow
  training_data_dirname --> |training_data_dirname|workflow
  workflow --> |training_data|training_data
  style inputs fill:#EEEEEE,stroke-width:2px;
  style pdf_directory stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style icasa_template stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style training_data_dirname stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style outputs fill:#EEEEEE,stroke-width:2px;
  style training_data stroke:#823909,fill:#F8CBAD,stroke-width:2px;
  style marker stroke:#385723,stroke-width:2px;
  style marker_output_dir_name font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style workflow stroke:#385723,stroke-width:2px;
```

## Convert LLM JSON to Tabular files
The `json2tabular` workflow combines the conversion of all supported ICASA categories to prepare for a comparison to the manual created data. The tools are all combined in this folder to create a small but helpful workflow.

### Usage
```
cwltool workflows/json2tabular/workflow.cwl inputs_json2tabular.yaml
```

```mermaid
---
---
config:
  theme: base
  look: neo
  themeVariables:
    primaryColor: '#C5E0B4'
    primaryTextColor: '#231f20'
    secondaryColor: '#EEEEEE'
    lineColor: '#385723'    
    fontSize: 12px
    tertiaryTextColor: '#231f20'
    fontFamily: 'Fira Sans, trebuchet ms, verdana, arial'
---
flowchart TB
  linkStyle default stroke:#385723,stroke-width: 2px;
  subgraph inputs[Workflow Inputs]
    direction TB
    llm_output_json(llm_output_json)
  end
  subgraph outputs[Workflow Outputs]
    direction TB
    harvest(harvest)
    fertilizers(fertilizers)
    plantings(plantings)
    plot_details(plot_details)
    irrigations(irrigations)
    fields(fields)
    genotypes(genotypes)
    exp_metadata(exp_metadata)
  end
    json2tabular_exp_metadata(json2tabular_exp_metadata)
  split --> |input_folder|json2tabular_exp_metadata
    json2tabular_exp_metadata_output_folder(llm_output_tabular/exp_metadata)
  json2tabular_exp_metadata_output_folder --> |output_folder|json2tabular_exp_metadata
    json2tabular_genotype(json2tabular_genotype)
  split --> |input_folder|json2tabular_genotype
    json2tabular_genotype_output_folder(llm_output_tabular/genotypes)
  json2tabular_genotype_output_folder --> |output_folder|json2tabular_genotype
    json2tabular_fields(json2tabular_fields)
  split --> |input_folder|json2tabular_fields
    json2tabular_fields_output_folder(llm_output_tabular/fields)
  json2tabular_fields_output_folder --> |output_folder|json2tabular_fields
    json2tabular_irrigation(json2tabular_irrigation)
  split --> |input_folder|json2tabular_irrigation
    json2tabular_irrigation_output_folder(llm_output_tabular/irrigations)
  json2tabular_irrigation_output_folder --> |output_folder|json2tabular_irrigation
    json2tabular_plotdetails(json2tabular_plotdetails)
  split --> |input_folder|json2tabular_plotdetails
    json2tabular_plotdetails_output_folder(llm_output_tabular/plot_details)
  json2tabular_plotdetails_output_folder --> |output_folder|json2tabular_plotdetails
    json2tabular_planting(json2tabular_planting)
  split --> |input_folder|json2tabular_planting
    json2tabular_planting_output_folder(llm_output_tabular/plantings)
  json2tabular_planting_output_folder --> |output_folder|json2tabular_planting
    json2tabular_fertilizeration_improved(json2tabular_fertilizeration_improved)
  split --> |input_folder|json2tabular_fertilizeration_improved
    json2tabular_fertilizeration_improved_output_folder(llm_output_tabular/fertilizers)
  json2tabular_fertilizeration_improved_output_folder --> |output_folder|json2tabular_fertilizeration_improved
    json2tabular_harvest(json2tabular_harvest)
  split --> |input_folder|json2tabular_harvest
    json2tabular_harvest_output_folder(llm_output_tabular/harvests)
  json2tabular_harvest_output_folder --> |output_folder|json2tabular_harvest
    split(split)
  llm_output_json --> |llm_output_json|split
  json2tabular_harvest --> |harvest|harvest
  json2tabular_fertilizeration_improved --> |fertilizers|fertilizers
  json2tabular_planting --> |plantings|plantings
  json2tabular_plotdetails --> |plot_details|plot_details
  json2tabular_irrigation --> |irrigations|irrigations
  json2tabular_fields --> |fields|fields
  json2tabular_genotype --> |genotypes|genotypes
  json2tabular_exp_metadata --> |exp_metadata|exp_metadata
  style inputs fill:#EEEEEE,stroke-width:2px;
  style llm_output_json stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style outputs fill:#EEEEEE,stroke-width:2px;
  style harvest stroke:#823909,fill:#F8CBAD,stroke-width:2px;
  style fertilizers stroke:#823909,fill:#F8CBAD,stroke-width:2px;
  style plantings stroke:#823909,fill:#F8CBAD,stroke-width:2px;
  style plot_details stroke:#823909,fill:#F8CBAD,stroke-width:2px;
  style irrigations stroke:#823909,fill:#F8CBAD,stroke-width:2px;
  style fields stroke:#823909,fill:#F8CBAD,stroke-width:2px;
  style genotypes stroke:#823909,fill:#F8CBAD,stroke-width:2px;
  style exp_metadata stroke:#823909,fill:#F8CBAD,stroke-width:2px;
  style json2tabular_exp_metadata stroke:#385723,stroke-width:2px;
  style json2tabular_exp_metadata_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json2tabular_genotype stroke:#385723,stroke-width:2px;
  style json2tabular_genotype_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json2tabular_fields stroke:#385723,stroke-width:2px;
  style json2tabular_fields_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json2tabular_irrigation stroke:#385723,stroke-width:2px;
  style json2tabular_irrigation_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json2tabular_plotdetails stroke:#385723,stroke-width:2px;
  style json2tabular_plotdetails_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json2tabular_planting stroke:#385723,stroke-width:2px;
  style json2tabular_planting_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json2tabular_fertilizeration_improved stroke:#385723,stroke-width:2px;
  style json2tabular_fertilizeration_improved_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style json2tabular_harvest stroke:#385723,stroke-width:2px;
  style json2tabular_harvest_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style split stroke:#385723,stroke-width:2px;
```