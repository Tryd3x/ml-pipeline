import os, sys

from src.logger import logging
from src.exception import CustomException

import pickle

def fetch_project_root(current_path):
    marker = ".project_root"
    # D print(f"Initial_path: {current_path}")
    while current_path != os.path.dirname(current_path):
        # D print(current_path)
        if marker in os.listdir(os.path.dirname(current_path)):
            # D print(os.listdir(os.path.dirname(current_path)))
            # D print(f"path returned: {os.path.dirname(current_path)}")
            return os.path.dirname(current_path)
        current_path = os.path.dirname(current_path)
    raise FileNotFoundError(f"Project root marker file '{marker}' not found.")

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path, 'wb') as f:
            pickle.dump(obj, f)
        logging.info(f"Saved object to {dir_path}")
    except Exception as e:
        logging.error(f"Failed to save {obj} to {dir_path}")
        raise CustomException(e,sys)

