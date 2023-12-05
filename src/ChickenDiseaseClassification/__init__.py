import os
import sys
import logging

# Logging format string
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Directory and file path for logging
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)  

# Basic configuration for logging
logging.basicConfig(
    level=logging.INFO, 

    # Use the defined logging format                
    format=logging_str,                 
    handlers=[
        
        # File handler to write logs to a file
        logging.FileHandler(log_filepath), 

        # Stream handler to output logs to the console 
        logging.StreamHandler(sys.stdout)   
    ]
)

# Creating a logger instance
logger = logging.getLogger("cnnClassifierLogger")
