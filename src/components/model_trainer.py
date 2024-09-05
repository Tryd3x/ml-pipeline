import sys, os
import pandas as pd
import numpy as np

from src.logger import logging 
from src.exception import CustomException
from src.utils import fetch_project_root, evaluate_model, save_object

from dataclasses import dataclass

from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import GridSearchCV

@dataclass
class ModelTrainerConfig:
    project_path = fetch_project_root(os.path.dirname(__file__))
    train_model_file_path = os.path.join(project_path,"artifacts", "model_trainer", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_data, test_data):
        logging.info("Model Trainer initiated..")
        try:
            X_train, y_train, X_test, y_test = (
                train_data[:, :-1],
                train_data[:, -1],
                test_data[:, :-1],
                test_data[:, -1],
            )

            models = {
                "random_forest" : RandomForestClassifier(),
                "decision_tree" : DecisionTreeClassifier(),
                "logistic_regression" : LogisticRegression()
            }

            params = {
                "random_forest" : {
                    "class_weight" : ["balanced"],
                    "n_estimators" : [20, 30, 50],
                    "max_depth" : [5, 8, 10],
                    "min_samples_split" : [2,5,10],
                },
                "decision_tree" : {
                    "class_weight" : ["balanced"],
                    "criterion" : ['gini', "entropy", "log_loss"],
                    "splitter" : ['best', 'random'],
                    "max_depth" : [3,4,5,6],
                    "min_samples_split" : [2,3,4,5],
                    "min_samples_leaf" : [1,2,3],
                    "max_features" : ['auto', 'sqrt', 'log2']
                },
                "logistic_regression" : {
                    "class_weight" : ["balanced"],
                    "penalty" : ["l1",'l2'],
                    'C' : [0.001,0.01,0.1,1,10],
                    'solver' : ['liblinear', 'saga']
                }
            }

            logging.info("Evaluating models...")

            report = evaluate_model(X_train, y_train, X_test, y_test, models, params)

            model_accuracy_list = {k:v['accuracy'] for k,v in report.items()}
            best_model_score = max(model_accuracy_list.values())
            index_of_max_val = list(model_accuracy_list.values()).index(best_model_score)
            best_model_name = list(model_accuracy_list.keys())[index_of_max_val]

            best_model = models[best_model_name]

            logging.info(f"Best model found, Model name: {best_model_name}, Accuracy: {best_model_score}")

            save_object(file_path=self.model_trainer_config.train_model_file_path, obj=best_model)

            logging.info("Model trainer completed successfully")
        except Exception as e:
            logging.error("Error in model trainer")
            raise CustomException(e,sys)



