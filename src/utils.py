import os, sys

from src.logger import logging
from src.exception import CustomException

import pickle

from sklearn.model_selection import GridSearchCV

from sklearn.metrics import \
    accuracy_score as acs,\
          confusion_matrix as cm,\
              precision_score as ps,\
                  recall_score as rs,\
                      f1_score as f1s,\
                          classification_report as clr,\
                            ConfusionMatrixDisplay as cmd

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

def evaluate_model(X_train, y_train, X_test, y_test, models, params):
    try:
        results = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            param = params[list(models.keys())[i]]

            grid_search = GridSearchCV(model,param,cv=5)
            grid_search.fit(X_train, y_train)

            model.set_params(**grid_search.best_params_)
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)
            test_model_accuracy = acs(y_test, y_pred)

            results[list(models.keys())[i]] = {
                "best_params": grid_search.best_params_,
                "accuracy": test_model_accuracy
            }

        return results

    except Exception as e:
        logging.error(f"Failed to evaluate model")
        raise CustomException(e,sys)
