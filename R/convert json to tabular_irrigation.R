# Install required packages if not already installed
if (!require("jsonlite")) install.packages("jsonlite")
if (!require("openxlsx")) install.packages("openxlsx")
if (!require("dplyr"))    install.packages("dplyr")

library(jsonlite)
library(openxlsx)
library(dplyr)

# ── 1. Configuration ──────────────────────────────────────────────────────────
input_folder  <- "C:\\Users\\xinxin\\OneDrive - Leibniz-Zentrum für Agrarlandschaftsforschung (ZALF) e.V\\Desktop\\FAIRagro_fine_tunning\\data\\0_training_set_version2\\genotype_gpt-4.1-mini_finetuning_output_v050526_irrigation_v119"          # folder containing your JSON/txt files
output_folder <- "C:\\Users\\xinxin\\OneDrive - Leibniz-Zentrum für Agrarlandschaftsforschung (ZALF) e.V\\Desktop\\FAIRagro_fine_tunning\\data\\0_training_set_version2\\genotype_gpt-4.1-mini_finetuning_output_v050526_irrigation_v119_excel"  # folder where Excel files will be saved
file_pattern  <- "\\.(json|txt)$"  # match .json or .txt files
# ── 1. Setup & Configuration ──────────────────────────────────────────────────
library(jsonlite)
library(openxlsx)
library(dplyr)
library(purrr)

if (!dir.exists(output_folder)) dir.create(output_folder, recursive = TRUE)

# ── 2. The Conversion Function ────────────────────────────────────────────────
convert_json_to_excel <- function(json_path, out_path) {
  
  # Load JSON
  data <- fromJSON(json_path, flatten = TRUE)
  
  # Handle nested cropYear -> GENOTYPES structure
  # Based on str() output: cropYear is a dataframe, GENOTYPES is a list column
  if (!is.null(data$cropYear$IRRIGATIONS)) {
    # Combine the list of observations into one flat dataframe
    df <- bind_rows(data$cropYear$IRRIGATIONS)
  } else if (!is.null(data$IRRIGATIONS)) {
    df <- as.data.frame(data$IRRIGATIONS)
  } else {
    # Fallback for other structures
    df <- as.data.frame(data)
  }
  
  # Safety Check: If df is empty, stop here
  if (nrow(df) == 0) {
    stop("No data rows found in the expected JSON structure.")
  }
  all_cols <- c(
    "experiment_ID",
    "irrigation_operation_name",
    "irrigation_date",
    "irrig_amount_depth",
    "irrigation_operation_notes"
  )
  # ── Data Cleaning (Essential for Excel) ─────────────────────────────────────
  # Convert any remaining list-columns into comma-separated strings
  df <- bind_rows(lapply(data$cropYear$IRRIGATIONS, function(rec) {
    
    # Add missing fields
    rec[setdiff(all_cols, names(rec))] <- ""
    
    # Convert {} or NULL → ""
    rec <- lapply(rec, function(x) {
      if (is.null(x) || (is.list(x) && length(x) == 0)) return("")
      x
    })
    
    as.data.frame(rec, stringsAsFactors = FALSE)
  }))
  df <- df[, all_cols]
  # ── Excel Workbook Creation ─────────────────────────────────────────────────
  wb <- createWorkbook()
  sheet_name <- substr(tools::file_path_sans_ext(basename(json_path)), 1, 31)
  addWorksheet(wb, sheet_name)
  
  # Styles
  header_style <- createStyle(
    fontName = "Arial", fontSize = 11, fontColour = "#FFFFFF", 
    fgFill = "#2E75B6", halign = "CENTER", valign = "CENTER",
    textDecoration = "bold", border = "TopBottomLeftRight"
  )
  
  data_style <- createStyle(
    fontName = "Arial", fontSize = 10, halign = "CENTER",
    border = "TopBottomLeftRight", borderColour = "#CCCCCC"
  )
  
  alt_style <- createStyle(
    fontName = "Arial", fontSize = 10, fgFill = "#DCE6F1",
    halign = "CENTER", border = "TopBottomLeftRight", borderColour = "#CCCCCC"
  )
  
  # Write Data
  writeData(wb, sheet_name, df, startRow = 1, startCol = 1, headerStyle = header_style)
  
  # Apply Alternating Row Colors
  for (i in seq_len(nrow(df))) {
    style <- if (i %% 2 == 0) alt_style else data_style
    addStyle(wb, sheet_name, style = style, rows = i + 1, 
             cols = seq_len(ncol(df)), gridExpand = TRUE)
  }
  
  setColWidths(wb, sheet_name, cols = seq_len(ncol(df)), widths = "auto")
  freezePane(wb, sheet_name, firstRow = TRUE)
  
  saveWorkbook(wb, out_path, overwrite = TRUE)
}

# ── 3. Batch process all matching files ───────────────────────────────────────
json_files <- list.files(input_folder, pattern = file_pattern,
                         full.names = TRUE, recursive = FALSE)

if (length(json_files) == 0) {
  cat("No JSON/txt files found in:", input_folder, "\n")
} else {
  cat(sprintf("Found %d file(s). Processing...\n\n", length(json_files)))
  
  results <- data.frame(file = character(), status = character(), stringsAsFactors = FALSE)
  
  for (json_path in json_files) {
    base_name <- tools::file_path_sans_ext(basename(json_path))
    out_path  <- file.path(output_folder, paste0(base_name, ".xlsx"))
    
    cat(sprintf("Converting: %s ... ", basename(json_path)))
    
    tryCatch({
      convert_json_to_excel(json_path, out_path)
      cat("DONE ✓\n")
      results <- rbind(results, data.frame(file = basename(json_path), status = "Success"))
    }, error = function(e) {
      cat(sprintf("FAILED ✗ (%s)\n", conditionMessage(e)))
      results <<- rbind(results, data.frame(file = basename(json_path), status = paste("Error:", conditionMessage(e))))
    })
  }
  
  # ── 4. Summary ──────────────────────────────────────────────────────────────
  cat("\n── Conversion Summary ───────────────────────────────\n")
  cat(sprintf("  Total files : %d\n", nrow(results)))
  cat(sprintf("  Succeeded   : %d\n", sum(results$status == "Success")))
  cat(sprintf("  Failed      : %d\n", sum(results$status != "Success")))
  cat("─────────────────────────────────────────────────────\n")
}