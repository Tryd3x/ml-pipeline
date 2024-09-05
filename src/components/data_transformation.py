import os, sys
from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object, fetch_project_root

import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

""" Todo
- Handle missing values
- Handle outliers
- Handle imbalanced dataset
- Convert categorical values into numerical values
"""
@dataclass
class DataTransformationConfig:

    def __post_init__(self):
        self.project_root = fetch_project_root(os.path.abspath(__file__))
        self.preprocessed_path_obj = os.path.join(self.project_root,'artifacts', 'data_transformation','preprocessed.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transformation_obj(self):
        try:
            logging.info("Initializing data transformation...")

            num_col = ['age', 'workclass', 'education_num', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week']

            num_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy="median")),
                ('scaler', StandardScaler()),
            ])

            preprocessor = ColumnTransformer([
                ('num_pipeline', num_pipeline, num_col)
            ])

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def remove_outliers_IQR(self, col, df):
        
        try:

            # inter quartile approach to eliminate outliers
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3-q1

            lower_limit = q1-1.5*iqr
            upper_limit = q3+1.5*iqr

            # Rows that execeed the upper limit will be replaced with the upper limit val
            df.loc[(df[col] > upper_limit), col] = upper_limit
            # Rows that are below the lower limit will be replaced with the lower limit val
            df.loc[(df[col] < lower_limit), col] = lower_limit

            return df        

        except Exception as e:
            logging.error("Outlier detection error")
            raise CustomException(e,sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            num_col = ['age', 'workclass', 'education_num', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week']

            logging.info("Detecting and eliminating outliers...")
            for col in num_col:
                self.remove_outliers_IQR(col=col, df=train_data)
            
            logging.info("Outliers handled successfully")

            preprocessor_obj = self.get_data_transformation_obj()
            
            target_column = 'income'

            drop_columns = [target_column]

            logging.info("Splitting train data into dependent and independent columns")
            input_feature_train_data = train_data.drop(columns=drop_columns, axis = 1)
            target_feature_train_data = train_data[target_column]

            logging.info("Splitting test data into dependent and independent columns")
            input_feature_test_data = test_data.drop(columns=drop_columns, axis = 1)
            target_feature_test_data = test_data[target_column]

            # Apply transformation on train and test data
            input_train_arr = preprocessor_obj.fit_transform(X=input_feature_train_data)
            input_test_arr = preprocessor_obj.transform(X=input_feature_test_data)

            train_array = np.c_[input_train_arr, np.array(target_feature_train_data)]
            test_array = np.c_[input_test_arr, np.array(target_feature_test_data)]

            save_object(self.data_transformation_config.preprocessed_path_obj,preprocessor_obj)

            logging.info("Data transformation completed successfully")
            
            return (train_array, test_array, self.data_transformation_config.preprocessed_path_obj)

        except Exception as e:
            logging.info("Error in data_transformation")
            raise CustomException(e,sys)
        
if __name__ == '__main__':
    pass