:: Run this script to set up your virtual enviroment for the project
:: Works on Windows
@echo off
if not EXIST %0\..\..\project_venv\ (
    echo Creating Python VENV
    cd %0\..\..
    py -3 -m venv project_venv
    call %0\..\..\project_venv\Scripts\activate.bat
    pip install pytrends fastapi[all] progressbar2 django
    echo Created VENV
)
if not defined VIRTUAL_ENV  (
    call %0\..\..\project_venv\Scripts\activate.bat)
