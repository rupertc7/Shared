# Purpose:     Creates readme with file script details
# How:         It reads this header for each script in a folder
# Status:      it works
# Elements:    extract data, splits it, goes through subdirectorys and over writes old files
# Imports:     os
# Author:      ROC
# Date:        4/11/2023   
# Note:        psudocoded and interativly refined
#______________________________________________________________________
import os

# Define the header markers
header_markers = {
    "Purpose": "# Purpose:",
    "How": "# How:",
    "Status": "# Status:",
    "Elements": "# Elements:"
}

# Function to process a directory and generate a ReadMe file
def process_directory(directory):
    # Get a list of all .py files in the directory
    py_files = [file for file in os.listdir(directory) if file.endswith('.py')]

    # Initialize the table header
    table_header = "Filename\tFunction\tStatus\tHow\tElements\n"

    # Initialize the table data
    table_data = ""

    # Loop through the .py files in the directory and extract data from their headers
    for py_file in py_files:
        with open(os.path.join(directory, py_file), 'r', encoding='utf-8') as file:
            file_lines = file.readlines()

        header_data = {key: '' for key in header_markers.keys()}

        # Extract header data
        for line in file_lines:
            for key, marker in header_markers.items():
                if line.strip().startswith(marker):
                    header_data[key] = line.replace(marker, '').strip()

        # Format the output
        formatted_data = f"{os.path.splitext(py_file)[0]}\tFunction:\t{header_data['Purpose']}\n"
        formatted_data += f"    STATUS: {header_data['Status']}\n"
        if header_data['How']:
            formatted_data += f"    HOW: {header_data['How']}\n"
        formatted_data += f"    ELEMENTS: {header_data['Elements']}\n"

        # Append formatted data to the table
        table_data += formatted_data

    # Write the table data to the ReadMe file in the current directory
    with open(os.path.join(directory, "ReadMe.txt"), "w") as readme_file:
        readme_file.write(table_data)

# Start processing the root directory
root_directory = os.getcwd()
process_directory(root_directory)

# Recursively process subdirectories
for root, _, _ in os.walk(root_directory):
    if root != root_directory:  # Skip the root directory itself
        process_directory(root)

print("ReadMe files generated or updated.")