import os,sys

from src.logger import logging
from src.exception import CustomException
from src.utils import *

import pandas as pd
import numpy as np

class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        project_root = fetch_project_root(os.path.abspath(__file__))
        preprocessed_path_obj = os.path.join(project_root,'artifacts', 'data_transformation','preprocessed.pkl')
        model_path = os.path.join(project_root,"artifacts", "model_trainer", "model.pkl")
        
        processor = load_object(preprocessed_path_obj)
        model = load_object(model_path)

        scaled = processor.transform(features)
        logging.info(f"Input features: {scaled.shape}")
        pred = model.predict(scaled)

        return pred
    
class CustomClass:
    def __init__(self, age: int, workclass: int, education_num: int, marital_status: int, occupation: int, relationship: int, race: int, sex: int, capital_gain: int, capital_loss:int , hours_per_week: int):
        
        self.age = age
        self.workclass = workclass
        self.education_num = education_num
        self.marital_status = marital_status
        self.occupation = occupation
        self.relationship = relationship
        self.race = race
        self.sex = sex
        self.capital_gain = capital_gain
        self.capital_loss = capital_loss
        self.hours_per_week = hours_per_week

    def get_data_DataFrame(self):
        try:
            custom_input = {
                'age': [self.age],
                'workclass': [self.workclass],
                'education_num': [self.education_num],
                'marital_status': [self.marital_status],
                'occupation': [self.occupation],
                'relationship': [self.relationship],
                'race': [self.race],
                'sex': [self.sex],
                'capital_gain': [self.capital_gain],
                'capital_loss': [self.capital_loss],
                'hours_per_week': [self.hours_per_week]
            }

            df = pd.DataFrame(custom_input)
            return df
        except Exception as e:
            logging.error("Error creating data frame")
            raise CustomException(e,sys)