# This one half of /R/assemble_training_set.R
## Usage:
##   Rscript generate_icasa_json.R \
##     --template_path FILE \
##     --json_folder DIR
##
## Example:
##   Rscript generate_icasa_json.R \
##     -t ICASA_template.xlsm \
##     -j ./json

if (!require("optparse")) install.packages("optparse")
library(optparse)

option_list <- list(
  make_option(c("-t", "--template_path"), type = "character", default = NULL,
              help = "Path to the ICASA template (.xlsm) file", metavar = "FILE"),
  make_option(c("-j", "--json_folder"), type = "character", default = NULL,
              help = "Folder where/under which manually structured json files are read from and written to", metavar = "DIR")
)
 
opt_parser <- OptionParser(
  option_list = option_list,
  description = paste(
    "Assemble jsonl training files for LLM-supported extraction of context metadata from",
    "tokenized scientific articles (markdown) based on the ICASA crop modeling controlled vocabulary."
  )
)

opt <- parse_args(opt_parser)

template_path     <- opt$template_path
json_folder       <- opt$json_folder

str_datasets <- csmTools::get_field_data0(
  path = template_path,
  headers = "long",  # <-- set whether to use long or short ICASA headers
  keep_empty = TRUE,
  keep_null_events = TRUE,
  keep_na_cols = TRUE
)

# ---- Extract from template ----------------------------------------------------------------------------------------
source("R/icasa_attributes_config.R")

# Subset data and order sections/attributes
data_subset <- lapply(str_datasets, function(ls) {
  ls <- ls[names(target_attributes)[names(target_attributes) %in% names(ls)]]
  lapply(names(ls), function(sec) {
    df <- ls[[sec]]
    attrs <- target_attributes[[sec]]
    df <- df[attrs[attrs %in% colnames(df)]]
    df[!duplicated(df), ]
  }) |> setNames(names(ls))
})

# Transpose list (nest studies into standard ICASA sections)
data_by_exp <- lapply(names(target_attributes), function(sec) {
  lapply(data_subset, function(ls) ls[[sec]])
})
names(data_by_exp) <- names(target_attributes)

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
  dir.create(file.path(json_folder, subdir), recursive = TRUE, showWarnings = FALSE)
  
  lapply(names(data_by_study[[sec]]), function(study) {
    df <- fix_empty_df(data_by_study[[sec]][[study]])
    wrapped <- setNames(list(df), sec)
    json <- jsonlite::toJSON(wrapped, pretty = TRUE, na = "null", Date = "ISO8601", POSIXt = "ISO8601")
    writeLines(json, con = file.path(json_folder, subdir, paste0(study, ".json")))
  })
})
