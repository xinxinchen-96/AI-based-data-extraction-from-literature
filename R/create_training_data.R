## ------------------------------------------------------------------------------------------------------------------
## Script name: assemble_training_set.R
## Purpose of script: assemble jsonl training file for LLM-supported extraction of context metadata from tokenized
## scientific articles (pdf files) based on the ICASA crop modeling controlled vocabulary
##
## Author: Benjamin Leroy
## Date Created: 2025-08-06
## Email: benjamin.leroy@inrae.fr
##
## Usage:
##   Rscript create_training_data.R \
##     --markdown_folder DIR \
##     --json_folder DIR \
##     --output_directory DIR

# This one half of /R/assemble_training_set.R
if (!require("optparse")) install.packages("optparse")
library(optparse)

if (!require("optparse")) install.packages("optparse")
library(optparse)

option_list <- list(
  make_option(c("-m", "--markdown_folder"), type = "character", default = NULL,
              help = "Folder containing tokenized article markdown (.md) files", metavar = "DIR"),
  make_option(c("-j", "--json_folder"), type = "character", default = NULL,
              help = "Folder where/under which manually structured json files are read from and written to", metavar = "DIR"),
  make_option(c("-o", "--output_directory"), type = "character", default = NULL,
              help = "Output directory for the generated jsonl training files", metavar = "DIR")
)
 
opt_parser <- OptionParser(
  option_list = option_list,
  description = paste(
    "Assemble jsonl training files for LLM-supported extraction of context metadata from",
    "tokenized scientific articles (markdown) based on the ICASA crop modeling controlled vocabulary."
  )
)

opt <- parse_args(opt_parser)

markdown_folder   <- opt$markdown_folder
json_folder       <- opt$json_folder
output_directory  <- opt$output_directory

if (is.null(markdown_folder) || is.null(json_folder) || is.null(output_directory)) {
  stop("--markdown_folder, --json_folder, and --output_directory are all required. Use --help for usage.")
}


# ---- Create training files -----------------------------------------------------------------------------------------
source("R/icasa_attributes_config.R")

if (!dir.exists(output_directory)) {
  dir.create(output_directory, recursive = TRUE)
}
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
user_prompts <- lapply(names(target_attributes), function(section) {
  attrs <- paste(target_attributes[[section]], collapse = ", ")
  paste("Extract the ICASA", attrs, "variables from this content:")
}) |> setNames(names(target_attributes))

# Generate jsonl training sets
lapply(names(target_attributes), function(sec) {
  subdir <- tolower(sec)
  out_basename <- paste0(subdir, ".jsonl")
  generate_training_file(
    sec = sec,
    md_dir = markdown_folder,
    str_dir = json_folder,
    sys_msg = sys_msg,
    user_prompt = user_prompts[[sec]],
    output_file = file.path(output_directory, out_basename)  # training data name
  )
})
