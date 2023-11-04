Each directory will have:

ReadMe_Create.py    Which auto creates a readme file as described below
                    It overwrites old readme with new versions when run
                    Thus if you update the status of the script and run this
                    script, it auto updates the readme file

ReadMe.txt          which lists all files in that folder and its subfolder
                    It also give key details, like what it does and if it works

newscript.py        creats a new python script with a header used to create the readme
                    # Purpose:     what the code tries to do
                    # How:         how it does it - can be left blank  
                    # Status:      "not started" default
                    # Elements:    Any key elements of the program can be added for ref
                    # Imports:     Any import
                    # Author:      "ROC" default
                    # Date:        "today's date" default
                    # Note:        e.g. codewhisperer or psudocoded etc.

header_insert.py    Inserts headers compatable with the ReadMe_Create.py script to all 
                    scripts in a folder. This is useful where you want to use auto gen
                    Readme.txt on leggacy folder.   The particulars still need to be 
                    added manually. 

