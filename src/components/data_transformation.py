import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
import neattext as nfx
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from src.exception import customException
from src.logger import logging 
import os
from src.utils import save_object
import spacy
from sklearn.base import BaseEstimator,TransformerMixin
import re
import pickle
from sklearn.preprocessing import LabelEncoder
@dataclass
class DataTransformationconfig:
    preprocessor_obj_file=os.path.join('artifacts',"preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationconfig()
        
        
   
    def clean_data(self, data):
        data['clean_Text'] = data['Text'].apply(nfx.remove_stopwords)
        data['clean_Text'] = data['clean_Text'].apply(nfx.remove_userhandles)
        data['clean_Text'] = data['clean_Text'].apply(nfx.remove_punctuations)
        return data[['clean_Text', 'Emotion']]
    
    
    
    def initiate_data_transformation(self, train_data_path, test_data_path):
        try:
            logging.info('Reading train and test data...')
            train_data= pd.read_csv(train_data_path)
            test_data = pd.read_csv(test_data_path)
            logging.info('Cleaning train data...')
            train_data = self.clean_data(train_data)
            logging.info('Cleaning test data...')
            test_data = self.clean_data(test_data)
            logging.info('Applying CountVectorizer on train data...')
            xfeatures=train_data['clean_Text']
            ylabels=train_data['Emotion']
            cv= CountVectorizer()
            X = cv.fit_transform(xfeatures)
            print(X)
            x_train_arr=X
            lc=LabelEncoder()
            train_arr=lc.fit_transform(ylabels)
            y_train_arr=train_arr   
            x_test_features=test_data['clean_Text']
            y_test_labels=test_data['Emotion']
            x = cv.transform(x_test_features)
            x_test_arr=x
            test_arr=lc.fit_transform(y_test_labels)
            y_test_arr= test_arr
            logging.info('data transformation is done')
            
            save_object(file_path=self.data_transformation_config.preprocessor_obj_file,
                        obj=cv
                         
                         )
            return (
                x_train_arr,
                y_train_arr,
                x_test_arr,
                y_test_arr
                 
            )                                          
            
        except Exception as e:
            raise customException(e,sys)

