# list_all_files_paths_in_all_folders.py

import os

# get current working directory
currentFolder = os.getcwd()

# walk through all folders and subfolders
for dirpath, dirnames, filenames in os.walk(currentFolder):
    # check each file in current folder
    for file in filenames:
        # print full path by joining directory path and file name
        fullPath = os.path.join(dirpath, file)
        print(fullPath)

input('')

##

#D:\_1Code\_2PY\_0PY_Published\Python_Computer_Science\py\dir\image_gallery.html
#D:\_1Code\_2PY\_0PY_Published\Python_Computer_Science\py\dir\listdir.py
#D:\_1Code\_2PY\_0PY_Published\Python_Computer_Science\py\dir\listdir_endswith.py
#D:\_1Code\_2PY\_0PY_Published\Python_Computer_Science\py\dir\list_all_files_in_all_folders.py
#D:\_1Code\_2PY\_0PY_Published\Python_Computer_Science\py\dir\list_all_file_paths_in_all_folders.py
#D:\_1Code\_2PY\_0PY_Published\Python_Computer_Science\py\dir\list_image_file_names_all_folders_list.py
#D:\_1Code\_2PY\_0PY_Published\Python_Computer_Science\py\dir\list_py_file_names_all_folders.py
#D:\_1Code\_2PY\_0PY_Published\Python_Computer_Science\py\dir\list_py_file_names_all_folders_list.py
#D:\_1Code\_2PY\_0PY_Published\Python_Computer_Science\py\dir\list_py_file_paths_all_folders.py
#D:\_1Code\_2PY\_0PY_Published\Python_Computer_Science\py\dir\make_folder_if_not_already_made.py
#D:\_1Code\_2PY\_0PY_Published\Python_Computer_Science\py\dir\notes.txt
#D:\_1Code\_2PY\_0PY_Published\Python_Computer_Science\py\dir\New folder\001.jpg
#D:\_1Code\_2PY\_0PY_Published\Python_Computer_Science\py\dir\New folder\002.jpg
#D:\_1Code\_2PY\_0PY_Published\Python_Computer_Science\py\dir\New folder\008.jpg
#D:\_1Code\_2PY\_0PY_Published\Python_Computer_Science\py\dir\New folder\008.png

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

