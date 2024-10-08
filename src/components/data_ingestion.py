import os, sys

from src.logger import logging
from src.utils import fetch_project_root
from src.exception import CustomException
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from dataclasses import dataclass

"""The configuration creates a new folder with the data sorted into raw, train and test files"""
@dataclass
class DataIngestionConfig:
    
    path_to_file: str

    def __post_init__(self):
        self.project_root = fetch_project_root(os.path.abspath(__file__))
        self.folder_path = os.path.basename(self.path_to_file).split('.')[0]
        print(f"folder path: {self.folder_path}")
        self.train_data_file = os.path.join(self.project_root,'artifacts/data_ingestion',self.folder_path,"train.csv")
        self.test_data_file = os.path.join(self.project_root,'artifacts/data_ingestion',self.folder_path,"test.csv")
        self.raw_data_file = os.path.join(self.project_root,'artifacts/data_ingestion',self.folder_path,"raw.csv")


class DataIngestion:
    def __init__(self,path_to_data):
        self.path_to_data = path_to_data
        self.ingestion_config = DataIngestionConfig(path_to_file=self.path_to_data)

    def initiateDataIngestion(self):
        print("Initiated Data Ingestion...")

        print(self.ingestion_config)
        logging.info("Initializing data ingestion")
        print("Initializing data ingestion")
        try:
            # Can possibly make this code dynamic to handle multiple sources of data
            data = pd.read_csv(self.path_to_data)
            logging.info("Data loaded successfully")
            
            os.makedirs(os.path.join(self.ingestion_config.project_root, 'artifacts','data_ingestion', self.ingestion_config.folder_path),exist_ok=True)
            logging.info("Artifacts folder created")
            
            data.to_csv(self.ingestion_config.raw_data_file, index=False)
            logging.info("Raw data saved successfully")

            train, test = train_test_split(data, test_size=.3, random_state=12)
            logging.info("Data successfully split into train and test data")

            train.to_csv(self.ingestion_config.train_data_file, index=False, header = True)
            test.to_csv(self.ingestion_config.test_data_file, index=False, header = True)
            logging.info("Train and test data saved successfully")

            logging.info("Data ingestion completed")

            print("Data Ingestion completed successfully")
            return (
                self.ingestion_config.train_data_file,
                self.ingestion_config.test_data_file,
                )

        except Exception as e:
            logging.error(f"Error occured in data ingestion stage")
            raise CustomException(e,sys)


if __name__ == "__main__":
    # obj = DataIngestion(path_to_data="../../datasets/people-2000000.csv")
    obj = DataIngestion(path_to_data="../../datasets/income_cleandata.csv")
    train_data_path, test_data_path = obj.initiateDataIngestion()

    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)

    model_trainer = ModelTrainer()
    model_trainer.initiate_model_trainer(train_arr, test_arr)