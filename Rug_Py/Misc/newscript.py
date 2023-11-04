# Purpose:     Header filling, script creator
# How:         Input request, skips regular inputs
# Status:      it works
# Elements:    if, scritpwrite, date
# Imports:     os, datetime
# Author:      ROC
# Date:        4/11/2023 
# Note:        psudocoded
#______________________________________________________________________"""


import os
import datetime

# Function to prompt the user for input, skipping if it's the same as the previous time
def get_input(prompt, previous_value=""):
    user_input = input(prompt)
    return previous_value if user_input == "" else user_input

# Default header values
default_date = datetime.datetime.now().strftime("%Y-%m-%d")
default_status = "not started"
default_author = "ROC"

# Prompt the user for input
script_name = get_input("Enter the name of the Python script (without the .py extension): ")
header = ""
header += f"# Purpose: {get_input('Purpose: ')}\n"
header += f"# How: {get_input('How: ')}\n"
header += f"# Status: {get_input('Status: ', default_status)}\n"
header += f"# Elements: {get_input('Elements: ')}\n"
header += f"# Imports: {get_input('Imports: ')}\n"
header += f"# Author: {get_input('Author: ', default_author)}\n"
header += f"# Date: {get_input('Date: ', default_date)}\n"
header += f"# Note: {get_input('Note: ')}\n"
header += "#_" + "_" * 67 + "__\n"

# Create the Python script file
script_content = header
script_file_path = f"{script_name}.py"
with open(script_file_path, "w") as script_file:
    script_file.write(script_content)

print(f"Python script '{script_file_path}' has been created with the custom header.")
