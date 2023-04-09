from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import time
from sklearn.preprocessing  import StandardScaler 
from src.pipeline.predict_pipeline import customData,predictpipeline
application=Flask(__name__)

app=application
#route for homepage
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
     return render_template('home.html')
    else:
        data=customData(
            message=request.form.get('message')
        )
        pred_df=data.get_data_as_frame( )
        print(pred_df)                         
        
        predict_pipeline=predictpipeline()
        start_time = time.time()
        results=predict_pipeline.predict(pred_df)
        latency = time.time() - start_time
        print('Latency: {} seconds'.format(latency))
        print(results)
        return render_template('result.html',results=results)
       
        
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)        