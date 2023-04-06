import sys
import pandas as pd
from src.exception import customException
from src.utils import load_object

class predictpipeline:
    def __init__(self):
     pass
    def predict(self,features):
     try:
        model_path='artifacts\model.pkl'
        preprocessor_path='artifacts\preprocessor.pkl'
        model=load_object(file_path=model_path)
        preprocessor=load_object(file_path=preprocessor_path)
        data_scaled=preprocessor.transform(features)
        pred=model.predict(data_scaled)
        
        
        return pred
     except Exception as e:
        raise customException(e,sys)    
class customData:
    def __init__(self,message):
                
      self.message=message
   
    def get_data_as_frame(self):
        try:
            custom_data_input_dict=[self.message]
            
            return custom_data_input_dict
        except Exception as e:
            raise customException(e,sys)