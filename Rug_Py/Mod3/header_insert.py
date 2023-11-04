# Purpose:     Insert standard header for readme_create to read
# How:         checks for existing header, if true skips
# Status:      it works
# Elements:    os.path and join
# Imports:     os
# Author:      ROC
# Date:        4/11/2023
# Note:        psudocoded
#______________________________________________________________________

import os

# Function to check if a file has a header based on the first few characters
def has_header(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
    return first_line.startswith("# Purpose:")

# Function to insert the header into a file if it's missing
def insert_header(file_path, header):
    with open(file_path, 'r') as file:
        content = file.read()

    if not has_header(file_path):
        with open(file_path, 'w') as file:
            file.write(header + '\n\n' + content)

# Define the header to insert
header = """\
# Purpose:     
# How:             
# Status:         
# Elements:   
# Imports:      
# Author:       ROC
# Date:           
# Note:   
#______________________________________________________________________"""

# Specify the folder to scan (use the current working directory)
folder_path = os.getcwd()

# Start the scanning process
for file in os.listdir(folder_path):
    if file.endswith('.py'):
        file_path = os.path.join(folder_path, file)
        insert_header(file_path, header)
