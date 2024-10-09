# list_py_file_paths_all_folders.py

import os

currentFolder = os.getcwd()

for dirpath, dirnames, filenames in os.walk(currentFolder):
    for file in filenames:
        if file.endswith('.py'):
            print(os.path.join(dirpath, file))

input('')

##

# D:\_1Code\_2PY\_0PY_Published\Python_Computer_Science\Python_Computer_Science\Python_Computer_Science\py\dir\listdir.py

#D:\_1Code\_2PY\_0PY_Published\Python_Computer_Science\Python_Computer_Science\Python_Computer_Science\py\dir\list_py_file_paths_all_folders.py

#D:\_1Code\_2PY\_0PY_Published\Python_Computer_Science\Python_Computer_Science\Python_Computer_Science\py\dir\listdir_endswith.py

#D:\_1Code\_2PY\_0PY_Published\Python_Computer_Science\Python_Computer_Science\Python_Computer_Science\py\dir\New folder\test.py

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

