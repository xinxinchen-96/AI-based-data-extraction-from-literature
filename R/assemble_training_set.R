## ------------------------------------------------------------------------------------------------------------------
## Script name: generate_training_corpus.R
## Purpose of script: generate jsonl training file for LLM-supported metadata extraction from tokenized pdf files to
## the ICASA data format
##
## Author: Benjamin Leroy
## Date Created: 2025-08-06
## Email: benjamin.leroy@inrae.fr
## ------------------------------------------------------------------------------------------------------------------

# ---- Install/load libraries ---------------------------------------------------------------------------------------

library(pak)
# pak::pak("leroy-bml/csmTools")  # run to install or update the package (install all dependencies when prompted)
library(csmTools)  # load ICASA template from Excel file
library(jsonlite)  # json file handling
library(dplyr)  # bind_rows
library(tools)  # file name utilities


# ---- Extract from template ----------------------------------------------------------------------------------------

template_path <- "./02_icasa_template/icasa_template_allColumns.xlsm" 

str_datasets <- csmTools::get_field_data0(
  path = template_path,
  headers = "long",  # <-- set whether to use long or short ICASA headers
  keep_empty = TRUE,
  keep_null_events = TRUE,
  keep_na_cols = TRUE
)


# ---- Select training subset ----------------------------------------------------------------------------------------

# Set list of attributes to extract for the training job (long headers here)
training_attributes <- list(
  EXP_METADATA = c(
    "experiment_ID", "name_of_experiment", "experiment_type", "management_type", "number_of_replicates",
    "number_of_treatments", "experimental_design", "main_experiment_factor", "experimental_factor_comb",
    "experiment_duration"
  ),
  FIELDS = c(
    "experiment_ID", "field_name", "field_country", "field_sub_country", "field_sub_sub_country",
    "field_latitude", "field_longitude", "field_elevation"
  ),
  GENOTYPES = c(
    "experiment_ID", "crop_ident_ICASA", "cultivar_name", "crop_intended_use", "cultivar_notes"
  ),
  PLOT_DETAILS = c(
    "experiment_ID", "plot_length", "plot_width", "plot_area", "plot_layout"
  ),
  IRRIGATIONS = c(
    "experiment_ID", "irrigation_operation_name", "irrigation_date", "irrig_amount_depth", "irrigation_operation_notes"
  ),
  PLANTINGS = c(
    "experiment_ID", "plantng_level_name", "planting_date", "emergence_date", "plant_pop_at_planting",
    "plant_pop_at_emergence", "planting_material", "planting_distribution", "plant_spacing", "row_spacing",
    "planting_depth", "planting_notes"
  ),
  HARVESTS = c(
    "experiment_ID", "harvest_ops_level_name", "harvest_operations_date", "harvest_method", "harvest_operations_notes"
  ),
  FERTILIZERS = c(
    "experiment_ID", "fertilizer_level_name", "fertilization_date", "fertilizer_material", "fertilizer_total_amount",
    "N_in_applied_fertilizer", "phosphorus_applied_fert", "fertilizer_K_applied", "fertilizer_applic_notes"
  )
)

# Subset data and order sections/attributes
data_subset <- lapply(str_datasets, function(ls) {
  ls <- ls[names(training_attributes)[names(training_attributes) %in% names(ls)]]
  lapply(names(ls), function(section) {
    df <- ls[[section]]
    attrs <- training_attributes[[section]]
    df <- df[attrs[attrs %in% colnames(df)]]
    df[!duplicated(df), ]
  }) |> setNames(names(ls))
})

# Transpose list (nest studies into standard ICASA sections)
data_by_exp <- lapply(names(training_attributes), function(sec) {
  lapply(data_subset, function(ls) ls[[sec]])
})
names(data_by_exp) <- names(training_attributes)

# Merge by study (i.e., multi-year/multi-site experiments in the same study = unique training record)
data_by_study <- lapply(data_by_exp, function(sec) {
  # Get base name (before first "_")
  base_names <- sub("_.*", "", names(sec))
  
  # Split by base name and bind_rows within each group
  lapply(split(names(sec), base_names), function(study_names) {
    dplyr::bind_rows(sec[study_names])
  })
})


# ---- Generate json outputs for each study and section (separate extraction jobs) -----------------------------------

# Helper to keep empty dataframes in
fix_empty_df <- function(df) {
  if (is.data.frame(df) && nrow(df) == 0) {
    # Create a one-row data frame with NA for each column
    as.data.frame(lapply(df, function(x) NA), stringsAsFactors = FALSE)
  } else {
    df
  }
}

# Write output as separate json per study and section
lapply(names(data_by_study), function(sec) {
  subdir <- tolower(sec)
  dir.create(file.path("./04_manual_json", subdir), showWarnings = FALSE)
  
  lapply(names(data_by_study[[sec]]), function(study) {
    df <- fix_empty_df(data_by_study[[sec]][[study]])
    wrapped <- setNames(list(df), sec)
    json <- jsonlite::toJSON(wrapped, pretty = TRUE, na = "null", Date = "ISO8601", POSIXt = "ISO8601")
    writeLines(json, con = file.path("./04_manual_json", subdir, paste0(study, ".json")))
  })
})

# ---- Create training files -----------------------------------------------------------------------------------------

# Function to generate training json pair
generate_training_file <- function(sec = NULL, md_dir, str_dir, sys_msg, user_prompt, output_file) {

  # Overwrite existing file
  if (file.exists(output_file)) file.remove(output_file)

  # Find markdown files (unstructured input)
  md_files <- list.files(md_dir, pattern = "\\.md$", full.names = TRUE, ignore.case = TRUE)

  # Find json files (structured output)
  if (!is.null(sec)) {
    str_dir <- file.path(str_dir, tolower(sec))
  }
  str_files <- list.files(str_dir, pattern = "\\.json$", full.names = TRUE, ignore.case = TRUE)
  str_basenames <- tools::file_path_sans_ext(basename(str_files))

  # Match files and combine into jsonl pairs
  # md_path <- md_files[1]  #tmp
  for (md_path in md_files) {
    base_name <- tools::file_path_sans_ext(basename(md_path))
    json_path <- str_files[grep(base_name, str_basenames)]

    if (length(json_path) == 0) {
      warning(paste("No structured JSON found for:", basename(md_path)))
      next
    }

    # Load matching input (md) and output (json)
    unstructured_text <- paste(readLines(md_path, warn = FALSE), collapse = "\n")
    structured_attrs <- jsonlite::minify(paste(readLines(json_path, warn = FALSE), collapse = "\n"))

    # Assemble jsonl pair with prompts
    entry <- list(
      messages = list(
        list(role = "system", content = sys_msg),
        list(role = "user", content = paste(user_prompt, unstructured_text)),
        list(role = "assistant", content = structured_attrs)
      )
    )

    # Write jsonl pair
    write(jsonlite::toJSON(entry, auto_unbox = TRUE), file = output_file, append = TRUE)
  }

  invisible(output_file)
}

# Set system message
sys_msg <- "You are expert in agriculture"

# Set section-specific prompts
user_prompts <- lapply(names(training_attributes), function(section) {
  attrs <- paste(training_attributes[[section]], collapse = ", ")
  paste("Extract the ICASA", attrs, "variables from this content:")
}) |> setNames(names(training_attributes))

# Generate jsonl training sets
lapply(names(training_attributes), function(sec) {
  section <- tolower(sec)
  out_basename <- paste0(section, ".jsonl")
  generate_training_file(
    sec = section,
    md_dir = "./xx_text_markdown",  # markown folder
    str_dir = "./04_manual_json",  # json folder
    sys_msg = sys_msg,
    user_prompt = user_prompts[[sec]],
    output_file = file.path("./03_training_data", out_basename)  # training data name
  )
})
