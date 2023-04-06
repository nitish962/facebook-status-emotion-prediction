import os 
import sys
import numpy as np 
import pandas as pd
from src.exception import customException
import dill


def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise customException(e,sys)
 
def evaluate_models(x_train, y_train, x_test, y_test, models):
    try:
        report = {}
        for name, model in models.items():
            model.fit(x_train, y_train)
            test_model_score = model.score(x_test, y_test)
            report[name] = test_model_score
            print(report)
        return report 
    except Exception as e:
        raise Exception(e)
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        raise customException(e,sys)    