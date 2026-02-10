#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 16:28:09 2026

@author: heatherkay
"""

import pandas as pd
            
def email_mapping(folderin):
    """
    A function which takes clean all years combined TFT survey data and produces monthly stats
    
    Parameters
    ----------
    
    folderin: string
             path to input folder with csv files with monthly TFT data
            
    folderout: string
           path for folder to save results in
    """
      
    survey = pd.read_csv(folderin + 'survey/all_survey.csv')
    lite = pd.read_csv(folderin + 'lite/all_lite.csv')
    count = pd.read_csv(folderin + 'count/all_count.csv')
    
    dfs = [survey, lite, count]
    
    for df in dfs:
        df['Email'] = (df['Email'].str.strip().str.lower())
    
    all_emails = pd.concat([df['Email'] for df in dfs])

    # Drop duplicates and reset index
    unique_emails = pd.Series(all_emails.dropna().unique(), name='email')
    
    email_reference_df = pd.DataFrame({
    'email': unique_emails,
    'email_id': range(1, len(unique_emails) + 1)})
    
    email_map = dict(zip(email_reference_df['email'], email_reference_df['email_id']))
    
    for df in dfs:
        df['email_id'] = df['Email'].map(email_map)
    
    email_reference_df.to_csv(folderin + 'email_reference.csv', index=False)
    
    for df in dfs:
        df.drop(columns=['email'], inplace=True)
    
   
    #now develop this so name of df is read in and then they can all be written out
