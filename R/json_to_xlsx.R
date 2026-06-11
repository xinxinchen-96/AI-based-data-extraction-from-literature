## ------------------------------------------------------------------------------------------------------------------
## Script name: json_to_xlsx.R
## Purpose of script: write structured Excel workbook to compare manually extracted metadata (training set) to the
## output of the fine-tuned LLM
##
## Author: Benjamin Leroy
## Date Created: 2025-06-10
## Email: benjamin.leroy@inrae.fr
## ------------------------------------------------------------------------------------------------------------------

# ---- Install/load libraries ---------------------------------------------------------------------------------------

library(jsonlite)
library(openxlsx2)


# ---- Extract from template ----------------------------------------------------------------------------------------

# Read json files as data frames
json_dir <- "./data/03_manual_json"
json_files <- list.files(json_dir, pattern = "\\.json$", full.names = TRUE, ignore.case = TRUE, recursive = TRUE)
file_names <- basename(json_files)

json_data <- lapply(json_files, function(path) {
  jsonlite::fromJSON(path)  # parses to R list, not raw string
})
names(json_data) <- file_names

# Merge ICASA sections by study
study_tables <- split(json_data, names(json_data)) |>
  lapply(function(sections) {
    do.call(c, unname(sections))
  })

# Write a xlsx workbook per study with set formatting
output_dir <- "./data/04_manual_tabular"

for (study in names(study_tables)) {
  wb <- openxlsx2::wb_workbook()
  
  for (section in names(study_tables[[study]])) {
    df <- study_tables[[study]][[section]]
    
    # NAs as blank cells
    df[is.na(df)] <- ""
    
    header_dims <- openxlsx2::wb_dims(rows = 1, cols = 1:ncol(df))
    
    wb <- wb %>%
      openxlsx2::wb_add_worksheet(sheet = section) %>%
      openxlsx2::wb_add_data(sheet = section, x = df) %>%
      # Apply header style
      openxlsx2::wb_add_font(
        sheet = section,
        dims = header_dims,
        bold = TRUE,
        color = wb_color("white")
      ) %>%
      openxlsx2::wb_add_fill(
        sheet = section,
        dims = header_dims,
        color = wb_color("#2E75B6")
      ) %>%
      # Auto-fill col width
      openxlsx2::wb_set_col_widths(
        sheet = section,
        cols = 1:ncol(df),
        widths = "auto"
      )
  }
  
  wb_save(wb, file = file.path(output_dir, paste0(tools::file_path_sans_ext(study), ".xlsx")))
}
