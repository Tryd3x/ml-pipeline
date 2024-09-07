import os,sys 

from src.logger import logging
from src.exception import CustomException

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == '__main__':
    try:
        obj = DataIngestion(path_to_data="../../datasets/income_cleandata.csv")
        train_data_path, test_data_path = obj.initiateDataIngestion()

        data_transformation_obj = DataTransformation()
        train_arr, test_arr, _ = data_transformation_obj.initiate_data_transformation(train_data_path,test_data_path)

        model_trainer_obj = ModelTrainer()
        model_trainer_obj.initiate_model_trainer(train_arr, test_arr)
        pass
    except CustomException as e:
        raise CustomException(e,sys)

