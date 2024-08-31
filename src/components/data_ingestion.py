import os, sys

from src.logger import logging, fetch_project_root
from src.exception import CustomException

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split


"""The configuration creates a new folder with the data sorted into raw, train and test files"""
class DataIngestionConfig:
    project_root = fetch_project_root(os.path.abspath(__file__))
    folder_path = 'artifacts'
    train_data_file = os.path.join(project_root,folder_path,"train.csv")
    test_data_file = os.path.join(project_root,folder_path,"test.csv")
    raw_data_file = os.path.join(project_root,folder_path,"raw.csv")


class DataIngestion:
    def __init__(self,):
        self.ingestion_config = DataIngestionConfig()

    def initiateDataIngestion(self):
        logging.info("Initializing data ingestion")
        try:
            # Can possibly make this code dynamic to handle multiple sources of data
            data = pd.read_csv("../../datasets/people-2000000.csv")
            logging.info("Data loaded successfully")
            
            os.makedirs(os.path.join(self.ingestion_config.project_root, self.ingestion_config.folder_path),exist_ok=True)
            logging.info("Artifacts folder created")
            
            data.to_csv(self.ingestion_config.raw_data_file, index=False)
            logging.info("Raw data saved successfully")

            train, test = train_test_split(data, test_size=.3, random_state=12)
            logging.info("Data successfully split into train and test data")

            train.to_csv(self.ingestion_config.train_data_file, index=False, header = True)
            test.to_csv(self.ingestion_config.test_data_file, index=False, header = True)
            logging.info("Train and test data saved successfully")

            logging.info("Data ingestion completed")
            return (
                self.ingestion_config.train_data_file,
                self.ingestion_config.test_data_file,
                )

        except Exception as e:
            logging.error(f"Error occured in data ingestion stage")
            raise CustomException(e,sys)


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiateDataIngestion()