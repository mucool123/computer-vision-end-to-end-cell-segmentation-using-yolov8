import os
from pathlib import Path
import logging

# Initialize logging with time and custom message format
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')  

# Project name definition
project_name = "cellSegmentation"  

# List of files and directories to be created for a structured and modular project setup
list_of_files = [
    ".github/workflows/.gitkeep",  # Placeholder file for GitHub Actions workflows
    "data/.gitkeep",  # Placeholder file in data directory for dataset storage
    f"{project_name}/__init__.py",  # Initialize the project as a Python package
    f"{project_name}/components/__init__.py",  # Initialize the components package
    f"{project_name}/components/data_ingestion.py",  # Script for data ingestion process
    f"{project_name}/components/data_validation.py",  # Script for data validation process
    f"{project_name}/components/model_trainer.py",  # Script for model training process
    f"{project_name}/constant/__init__.py",  # Initialize the constants package
    f"{project_name}/constant/training_pipeline/__init__.py",  # Initialize training pipeline constants
    f"{project_name}/constant/application.py",  # Script for application-wide constants
    f"{project_name}/entity/config_entity.py",  # Script for configuration entities
    f"{project_name}/entity/artifacts_entity.py",  # Script for artifacts entities
    f"{project_name}/exception/__init__.py",  # Initialize the exceptions package
    f"{project_name}/logger/__init__.py",  # Initialize the logger package
    f"{project_name}/pipeline/__init__.py",  # Initialize the pipeline package
    f"{project_name}/pipeline/training_pipeline.py",  # Script for the training pipeline
    f"{project_name}/utils/__init__.py",  # Initialize the utilities package
    f"{project_name}/utils/main_utils.py",  # Script for main utilities
    "research/trials.ipynb",  # Jupyter notebook for research and trials
    "templates/index.html",  # HTML template for web interface
    "app.py",  # Main application script
    "Dockerfile",  # Dockerfile for container setup
    "requirements.txt",  # Dependencies file
    "setup.py",  # Setup script for project installation
]

# Loop through each file path in the list to ensure creation of directories and files
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert to Path object for OS compatibility

    # Extract directory and filename from the path
    filedir, filename = os.path.split(filepath)

    # Create the directory if it does not exist
    if filedir!="":
        os.makedirs(filedir, exist_ok=True)  # Avoid error if directory exists
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # Check if the file exists and is not empty, then create or skip
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        with open(filepath, "w") as f:  # Create an empty file
            pass  # Placeholder for future code, does nothing
            logging.info(f"Creating empty file: {filename}")  # Log file creation

    else:
        # Log if the file already exists and is not empty
        logging.info(f"{filename} is already created")
