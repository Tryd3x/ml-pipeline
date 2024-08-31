import os
import logging
from datetime import datetime


'''
Configuration for log directory and log file
'''

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

# D print(f"abspath = {os.path.abspath(__file__)}")
log_dir = os.path.join(fetch_project_root(os.path.abspath(__file__)), 'logs') # Define creation of logs directory
log_file = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log" # Define name-format of log file
log_path = os.path.join(log_dir, log_file)

# Create a log directory
os.makedirs(log_dir,exist_ok=True)

'''
Configuration for logging details
'''
logging.basicConfig(
    filename=log_path,
    format='[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

if __name__ == '__main__':
    logging.info('Initiated Logger')