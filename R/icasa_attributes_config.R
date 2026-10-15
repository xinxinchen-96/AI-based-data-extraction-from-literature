# This extracted from /R/assemble_training_set.R and used by /R/create_training_data.R and /R/generate_icasa_json.R

target_attributes <- list(
  EXP_METADATA = c(
    "experiment_ID", "name_of_experiment", "experiment_type", "objectives_of_study", "management_type",
    "number_of_replicates", "number_of_treatments", "experimental_design", "main_experiment_factor",
    "experimental_factor_comb", "experiment_duration"
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
    "experiment_ID", "planting_level_name", "planting_date", "emergence_date", "plant_pop_at_planting",
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