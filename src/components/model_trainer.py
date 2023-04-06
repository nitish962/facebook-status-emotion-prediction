import os
import sys
from dataclasses  import dataclass
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.ensemble import (
    AdaBoostClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier,
    
)
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from src.exception import customException
from src.logger import logging
from src.utils import save_object,evaluate_models
from src.utils import load_object


@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
        
    def initiate_model_trainer(self,x_train_arr,y_train_arr,x_test_arr,y_test_arr):
        try:
            logging.info('split training and test imput data')
            x_train=x_train_arr
            y_train=y_train_arr
            x_test=x_test_arr
            y_test=y_test_arr
          
    
            models={
                'decision tree':RandomForestClassifier(),
                'Logistic Regression': LogisticRegression(max_iter=1000),
                'naive bayes':MultinomialNB(),
                'AdaBoostClassifier':AdaBoostClassifier(),
            }
            
            model_report=evaluate_models(x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test,models=models)
            # to get best model score from dict
            best_model_score=max(sorted(model_report.values()))
            #to get best model name from dict
            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model=models[best_model_name]
            
            
            logging.info(f"best found model on both training and testing dataset")
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            predicted=best_model.score(x_test,y_test)
            return predicted
        except Exception as e:
            raise customException(e,sys)