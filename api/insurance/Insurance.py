#cleaning, transformation and enconding

import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler,StandardScaler
 

class Insurance(object):
    def _init_( self ):
        self.home_path = '/home/guilherme/Documentos/repos/pa_health_cross_sell/projeto/'
        self.annual_premium_scaler = pickle.load(open ( self.home_path + 'parameter/annual_premium_scaler.pkl','rb' ) )
        self.age_scaler = pickle.load(open (self.home_path + 'parameter/age_scaler.pkl','rb') )
        self.vintage_scaler = pickle.load(open (self.home_path + 'parameter/vintage_scaler.pkl','rb') )

        
    def cleaning_data(self,df1):
        df1['region_code']    = df1['region_code'].astype(int)

        df1['annual_premium'] = df1['annual_premium'].astype(int)

        df1['policy_sales_channel'] = df1['policy_sales_channel'].astype(int)
        
        return df1
    
    def feature_engineering(self,df2):
        #rename the rows of colum vehicle age
        df2['vehicle_age'] = df2['vehicle_age'].apply(lambda x: 0 if x== '< 1 Year' 
                                              else 2 if x== '1-2 Year'
                                              else 3 
                                              if x== '> 2 Years' else x)

        #rename the rows of colum vehicle damage
        df2['vehicle_damage'] = df2['vehicle_damage'].apply(lambda x: 0 if x=='No' else 1)

        #convent the days in month
        df2['vintage'] = df2['vintage'].apply(lambda x: x/30)

        #convent the colum to type int
        df2['vintage'] = df2['vintage'].astype('int')

    def data_preparation(self,df3):
        
        #Normalizing the data

        df3['annual_premium'] = self.annual_premium_scaler.transform(df3[['annual_premium']].values)
        
        # =================================== Target Enconding ===================================== #

        #making the mean by region code in dataframe
        target_enconding_region_code = df3.groupby('region_code')['response'].mean()

        #add new scale in dataframe 
        df3.loc[:, 'region_code'] = df3['region_code'].map(target_enconding_region_code)

        # =============================== Frequency ===============================================#

        #policy_sales_channel / frenquecy between dataset

        #new variable with the frequency in dataset
        fre_policy_sales_channel = df3.groupby('policy_sales_channel').size()/ len(df3)

        # add in dataset the new rescaling
        df3.loc[:,'policy_sales_channel'] = df3['policy_sales_channel'].map(fre_policy_sales_channel)

        #====== vehicle_age =========

        fre_vehicle_age = df3.groupby('vehicle_age').size()/ len(df3)

        df3.loc[:,'vehicle_age'] = df3['vehicle_age'].map(fre_vehicle_age)

        # ======================================== MinMax Scaler ================================================= #

        #Pack to make rescaling


        #
        df3['vintage'] = self_vintage_scaler.transform( df3[['vintage']].values )


        df3['age'] = self_age_scaler.transform( df3[['age']].values )
        
        ## ===================================== Target Enconder ======================================================= ##

        target_gender = df3.groupby('gender')['response'].mean()

        df3.loc[:,'gender'] = df3['gender'].map(target_gender)
        
        # Features selected with more of 5 percent of importance
        cols_selected = ['annual_premium','age','region_code','vintage','vehicle_damage','policy_sales_channel','previously_insured']
        
        return df3[cols_selected]
        
        def get_prediction(self,model, original_data,test_data):
            
            #prediction
            pred = model.predict_proba(test_data)
            
            #create new feature of score probabilty
            original_data['proba'] = pred[:,1].tolist()

            #ordened the values
            original_data = original_data.sort_values(by='proba',ascending=False)
            
            return original_data.to_json(orient = 'records',date_format = 'iso')
            
            

