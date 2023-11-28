# Purpose:     Header filling, script creator
# How:         Input request, skips regular inputs
# Status:      it works cNOTE
# Elements:    if, scritpwrite, date
# Imports:     os, datetime
# Author:      ROC
# Date:        4/11/2023 
# Note:        psudocoded, plus manual update to take argument. most of old script now a defined function.
# cNOTE:       updated to take argument on command line.  e.g. python newscript.py 8 creates 8 new scripts.
#______________________________________________________________________"""

import os
import datetime
import sys

# Function to create a script with a header
def create_script(script_name, use_defaults=False):
    # Default header values
    default_date = datetime.datetime.now().strftime("%Y-%m-%d")
    default_status = "not started"
    default_author = "ROC"

    header = ""
    header += f"# Purpose: {get_input('Purpose: ') if not use_defaults else ''}\n"
    header += f"# How: {get_input('How: ') if not use_defaults else ''}\n"
    header += f"# Status: {get_input('Status: ', default_status) if not use_defaults else default_status}\n"
    header += f"# Elements: {get_input('Elements: ') if not use_defaults else ''}\n"
    header += f"# Imports: {get_input('Imports: ') if not use_defaults else ''}\n"
    header += f"# Author: {get_input('Author: ', default_author) if not use_defaults else default_author}\n"
    header += f"# Date: {get_input('Date: ', default_date) if not use_defaults else default_date}\n"
    header += f"# Note: {get_input('Note: ') if not use_defaults else ''}\n"
    header += "#_" + "_" * 67 + "__\n"

    # Create the Python script file
    script_content = header
    script_file_path = os.path.join(os.getcwd(), script_name)
    with open(script_file_path, "w") as script_file:
        script_file.write(script_content)

    print(f"Python script '{script_file_path}' has been created with the custom header.")

# Function to prompt the user for input
def get_input(prompt, default_value=""):
    user_input = input(prompt)
    return default_value if user_input == "" else user_input

# Check if an argument is provided
if len(sys.argv) == 1:
    # Create a single script when no argument is provided
    script_name = input("Enter the name of the Python script (without the .py extension): ")
    create_script(f"{script_name}.py")

elif len(sys.argv) == 2 and sys.argv[1].isdigit():
    # Create multiple scripts when a numeric argument is provided
    n_times = int(sys.argv[1])
    for i in range(1, n_times + 1):
        create_script(f"{i}.py", use_defaults=True)

else:
    print('Unexpected argument, check documentation')