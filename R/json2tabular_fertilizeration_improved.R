## Usage:
##   Rscript json2tabular_fertilizeration_improved.R \
##     --input_folder DIR \
##     --output_folder DIR
##

# Install required packages if not already installed
if (!require("jsonlite")) install.packages("jsonlite")
if (!require("openxlsx")) install.packages("openxlsx")
if (!require("dplyr"))    install.packages("dplyr")

library(jsonlite)
library(openxlsx)
library(dplyr)

if (!require("optparse")) install.packages("optparse")
library(optparse)

option_list <- list(
  make_option(c("-j", "--input_folder"), type = "character", default = NULL,
              help = "Folder where/under which manually structured json files are read from and written to", metavar = "DIR"),
  make_option(c("-o", "--output_folder"), type = "character", default = NULL,
              help = "Output directory for the generated jsonl training files", metavar = "DIR")
)

opt_parser <- OptionParser(
  option_list = option_list,
  description = paste(
    "Convert JSON to tabular exp metadata"
  )
)

opt <- parse_args(opt_parser)


input_folder <- opt$input_folder
output_folder <- opt$output_folder

if (!dir.exists(output_folder)) {
  dir.create(output_folder, recursive = TRUE)
}

# ── 1. Configuration ──────────────────────────────────────────────────────────
#input_folder  <- "C:\\Users\\xinxin\\OneDrive - Leibniz-Zentrum für Agrarlandschaftsforschung (ZALF) e.V\\Desktop\\FAIRagro_fine_tunning\\data\\0_training_set_version2\\gpt-4.1-mini_finetuning_output_v050526_fertilizer_v121"          # folder containing your JSON/txt files
#output_folder <- "C:\\Users\\xinxin\\OneDrive - Leibniz-Zentrum für Agrarlandschaftsforschung (ZALF) e.V\\Desktop\\FAIRagro_fine_tunning\\data\\0_training_set_version2\\gpt-4.1-mini_finetuning_output_v050526_fertilizer_v121_excel"  # folder where Excel files will be saved
file_pattern  <- "\\.(json|txt)$"  # match .json or .txt files
# ── 1. Setup & Configuration ──────────────────────────────────────────────────
library(jsonlite)
library(openxlsx)
library(dplyr)
library(purrr)



convert_json_to_excel <- function(json_path, out_path) {
  
  # 1. Check if file is empty to avoid "Premature EOF"
  if (file.info(json_path)$size == 0) {
    stop("File is empty.")
  }
  
  # 2. Load JSON
  raw_data <- fromJSON(json_path, simplifyVector = FALSE)
  
  # 3. Extract and Flatten the FERTILIZERS data
  if (!is.null(raw_data$cropYear)) {
    # Combine list of lists into a single data frame
    df_list <- lapply(raw_data$cropYear, function(year_entry) {
      if (is.null(year_entry$FERTILIZERS)) return(NULL)
      
      # Convert each fertilizer record into a clean data frame row
      lapply(year_entry$FERTILIZERS, function(rec) {
        # Convert empty lists {} to NA so they don't break the dataframe
        rec <- lapply(rec, function(val) {
          if (is.list(val) && length(val) == 0) return(NA)
          return(val)
        })
        return(as.data.frame(rec, stringsAsFactors = FALSE))
      }) %>% bind_rows()
    })
    
    df <- bind_rows(df_list)
    
  } else {
    stop("JSON does not contain the expected 'cropYear' key.")
  }
  
  if (is.null(df) || nrow(df) == 0) {
    stop("No fertilizer data found within cropYear.")
  }
  
  # 4. Column Alignment (Replacing all_of with base R for stability)
  all_cols <- c(
    "experiment_ID", "fertiliz_app_name", "fertilization_date",
    "fertilizer_material", "fertilizer_total_amount", "N_in_applied_fertilizer",
    "phosphorus_applied_fert", "fertilizer_K_applied", "fertilizer_applic_notes"
  )
  
  # Ensure every column exists (fill with NA if missing)
  for (col in all_cols) {
    if (!(col %in% names(df))) {
      df[[col]] <- NA
    }
  }
  
  # Reorder and subset using base R
  df <- df[, all_cols, drop = FALSE]
  
  # 5. Excel Workbook Creation
  wb <- createWorkbook()
  sheet_name <- substr(tools::file_path_sans_ext(basename(json_path)), 1, 31)
  addWorksheet(wb, sheet_name)
  
  header_style <- createStyle(
    fontName = "Arial", fontSize = 11, fontColour = "#FFFFFF", 
    fgFill = "#2E75B6", halign = "CENTER", valign = "CENTER",
    textDecoration = "bold", border = "TopBottomLeftRight"
  )
  
  alt_style <- createStyle(
    fontName = "Arial", fontSize = 10, fgFill = "#DCE6F1",
    halign = "CENTER", border = "TopBottomLeftRight", borderColour = "#CCCCCC"
  )
  
  writeData(wb, sheet_name, df, startRow = 1, startCol = 1, headerStyle = header_style)
  
  # Apply alternating colors
  if (nrow(df) > 0) {
    for (i in seq_len(nrow(df))) {
      if (i %% 2 == 0) {
        addStyle(wb, sheet_name, style = alt_style, rows = i + 1, 
                 cols = seq_len(ncol(df)), gridExpand = TRUE)
      }
    }
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