#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 08:55:07 2025

@author: heatherkay
"""

import pandas as pd

months = ['5','6','8','9','10','11','12']
folder = '/Users/heatherkay/Documents/TrashFreeTrails/Data/Monthly stats/2024/input/'

for month in months:
    df = pd.read_csv(folder + 'CS_count_' + month + '.csv' )
    df = df.rename(columns={'Time(hours)':'Time_hours'})
    df.to_csv(folder + 'CS_count_' + month + '.csv' , index=False)
    
def join_survey_clean_data(oldin, newin, cleanout):
    """
    A function which takes new cleaned monthly TFT survey data and joins it with
    existing data
    
    Parameters
    ----------
    
    TFTin: string
            path to input csv file with original TFT data
             
    newin: string
            path to input csv file with new data  
             
    monthout: string
            path to save the clean data just for the month you are processing
            
    rawout:  string        
            path to save file with raw data
            
    TFTout: string
            path to save file with clean data
    """    

    #read in 'old' data and 'new' data
    orig_data = pd.read_csv(oldin)   
    new_data = pd.read_csv(newin)
    cols2 = list(orig_data) # only needed if using column names from 'old' data or to check columns

    #check column headers - not needed unless df_final has more columns than orig_data
    c = []
    for val in cols:
        if val not in cols2:
            c.append(val)
            
    d = []
    for val in cols2:
        if val not in cols:
            d.append(val)  

      
    #add new cleaned data to top of original data
    dfs = (new_data, orig_data)
    
    #stage above may be changed so data is added to the appropriate yearly/monhtly dataset
    
    df_final = pd.concat(dfs, ignore_index = True) 
    
    df_final.to_csv(cleanout)    
    