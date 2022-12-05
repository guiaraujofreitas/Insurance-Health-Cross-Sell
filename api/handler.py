import pickle
import pandas as pd
import requests
from flask import Flask, request, Response

#collecting the past archive and imnport class
from insurance.Insurance import Insurance

model = pickle.load(open('/home/guilherme/Documentos/repos/pa_health_cross_sell/projeto/model/model_insurance.pkl','rb' ) )


#start api
app = Flask(__name__)

#creating url (endpoint) to send data
@app.route('/predict', methods=['POST'] )

def insurance_predict():
    test_json = request.get_json()
    
    if test_json: #In there is data
        
        if isintance(test_json, dict): #unique example
            #in case there is only row
            test_row = pd.DataFrame(test_json, index=[0] )
            
        else:
            #colletcting all json of all all rows
            test_row= pd.DataFrame(test_json, columns=test_json[0].keys() )#multiples examples
        
        #Instance the class (Making the copy)
        
        pipeline = Insurance()
        
        df1 = pipeline.cleaniing_data(test_row)
        
        df2 = pipeline.feature_engineering(df1)
        
        df3 = pipeline.data_preparation(df2)
        
        #predict of probability
        df_response= pipeline.get_prediction(model, df3)
    
        return df_response
    
    else: #If case empty
        return Response( '{}', status=200, mimetype='application/json')

if __name__ == '_main_':
    app.run('0.0.0.0')
