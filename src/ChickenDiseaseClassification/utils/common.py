# Importing necessary libraries
import os
from pathlib import Path
import yaml
from box import ConfigBox, BoxValueError
from ChickenDiseaseClassification import logger  
import joblib
from ensure import ensure_annotations

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents in a ConfigBox object

    Args:
        path_to_yaml (Path): Path to the YAML file

    Raises:
        ValueError: If the YAML file is empty

    Returns:
        ConfigBox: Contents of the YAML file as a ConfigBox object
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if not content:
                raise ValueError("YAML file is empty")
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error loading YAML file: {e}")
        raise ValueError("YAML file is empty") from e
    except Exception as e:
        logger.error(f"Error loading YAML file: {e}")
        raise

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates a list of directories

    Args:
        path_to_directories (list): List of directory paths to create
        verbose (bool, optional): If True, logs the creation of each directory
    """
    for path in path_to_directories:
        try:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Created directory at: {path}")
        except Exception as e:
            logger.error(f"Error creating directory {path}: {e}")
            raise

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Gets the size of a file in kilobytes.

    Args:
        path (Path): Path of the file.

    Returns:
        str: Size of the file rounded to the nearest kilobyte, represented as a string.
    """
    try:
        size_in_kb = round(os.path.getsize(path) / 1024)
        return f"~ {size_in_kb} KB"
    except Exception as e:
        logger.error(f"Error getting size for {path}: {e}")
        raise


