# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 10:54:37 2025

@author: xinxin
"""

############################################# 
#############################################
import subprocess

# Define input and output directories
input_pdf = r"..."
output_markdown = r"..."

# Define command arguments
command_batch = [
    "marker", 
    input_pdf, 
    "--output_dir", 
    output_markdown
]

# Try to run the command
try:
    # Run the command and capture output
    result = subprocess.run(command_batch, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Print the standard output and error
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

    # Check for errors in execution
    if result.returncode != 0:
        print(f"Command failed with return code {result.returncode}. Please check the STDERR output for more details.")
except FileNotFoundError as e:
    print("Error: The 'marker_single' command was not found. Make sure it is installed and available in your system PATH.")
    print(e)
except Exception as e:
    print("An unexpected error occurred while running the command.")
    print(e)
############################################# 
############################################# 