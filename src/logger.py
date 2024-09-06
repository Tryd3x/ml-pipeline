import os
import logging
from src.utils import fetch_project_root
from datetime import datetime


'''
Configuration for log directory and log file
'''

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