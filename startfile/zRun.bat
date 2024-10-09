:: Dedicated to God the Father
:: All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
:: https://github.com/ChristopherTopalian
:: https://github.com/ChristopherAndrewTopalian
:: This .bat File runs a .pyfile found in the folder.
:: To activate this .bat file, we double click the .bat file, while it is located in our folder.
:: zRun.bat

@echo off

set "pyFile="

for %%f in (*.py) do set "pyFile=%%f" & goto :run_js

:run_js
if defined pyFile (
    echo Running the file: %pyFile%
    python "%~dp0%pyFile%"
) else (
    echo No such files found in the directory.
)

pause
