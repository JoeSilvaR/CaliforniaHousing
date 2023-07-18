# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 16:41:21 2023

@author: Joe Silva
"""

"""
Viewing the Data
"""
# Libraries


# Loading Data


import pandas as pd
import numpy as np
df_zillow = pd.read_csv('C:/Users/josep/OneDrive/Documents/Projects/Cali Housing/data_raw/County_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv')

# Viewing Data, Zillow;
df_zillow.head(5)
df_zillow.dtypes


# Filtering for data with regards to California
ca_data = df_zillow[df_zillow['State'] == 'CA']

# Observring first few rows of new data frame
ca_data.head()

##Transforming the data to 'long' format for ease of use in Tableau

# Transforming to long using 'melt'
ca_data_long = ca_data.melt(id_vars=['RegionName'],var_name='Date', value_name='HomePrice' )

# Filtering out non-date related columns; region type and size rank
ca_data_long = ca_data_long[ca_data_long['Date'].str.contains('-')]

# Converting Date to datetime
ca_data_long['Date']= pd.to_datetime(ca_data_long['Date'])

#Viewing transformed dataframe
ca_data_long.head()

##saving prepared data to CSV
ca_data_long.to_csv('C:/Users/josep/OneDrive/Documents/Projects/Cali Housing/data_processed/ CA_HomePrices_Long.csv', index= False)
