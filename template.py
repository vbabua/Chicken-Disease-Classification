"""
This script is used to initialise the file structure for the ChickenDiseaseClassification project
It creates a predefined set of directories and files necessary for the project's organisation and workflow

Usage:
    python template.py

The script iterates through a list of required files and directories, creating them if they don't already exist
"""

import os
from pathlib import Path
import logging

# Basic Logging Configuration
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# List of necessary files and directories for the project
project_name = "ChickenDiseaseClassification"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    try:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)

        # Creating directory if they don't exist
        if filedir !="":
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating {filedir} for the file: {filename}")
        
        # Creating a file if they don't exist or are empty
        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, "w") as f:
                pass
            logging.info(f"Creating empty file: {filepath}")


        else:
            logging.info(f"{filename} is already exists")
    except Exception as e:
        # Logging erros encountered during file or directory creation
        logging.error(f"Error occured while creating file or directory {filepath}: as {e}")