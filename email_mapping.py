#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 16:28:09 2026

@author: heatherkay
"""

import pandas as pd
            
def email_mapping_get_all_emails(folderin, folderout):
    """
    A function which takes clean all years combined TFT survey data and maps
    all the emails to create an initial reference .csv for email mapping and GDPR
    
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
        df.drop(columns=['Email'], inplace=True)
        
    survey.to_csv(folderout + 'survey/all_survey.csv', index=False)
    lite.to_csv(folderout + 'lite/all_lite.csv', index=False)
    count.to_csv(folderout + 'count/all_count.csv', index=False)
    
   
 
    
def email_mapping_annual(folderin, folderout):
    """
    A function which takes annual TFT data, does email mapping and deletes emails
    
    Parameters
    ----------
    
    folderin: string
             path to input folder with csv files with monthly TFT data
            
    folderout: string
           path for folder to save results in
    """
    years = ['2019','2020','2021','2022','2023','2024','2025','2026']
    
    for year in years:
        survey = pd.read_csv(folderin + 'survey/survey_' + year + '.csv')
        lite = pd.read_csv(folderin + 'lite/lite_' + year + '.csv')
        count = pd.read_csv(folderin + 'count/count_' + year + '.csv')
    
        dfs = [survey, lite, count]
    
        email_ref_df = pd.read_csv(folderout + 'email_reference.csv')
    
        email_map = dict(zip(email_ref_df['email'], email_ref_df['email_id']))
    
        for df in dfs:
            df['email_id'] = df['Email'].map(email_map)
            df.drop(columns=['Email'], inplace=True)
        
        survey.to_csv(folderout + 'survey/survey_' + year + '.csv', index=False)
        lite.to_csv(folderout + 'lite/lite_' + year + '.csv', index=False)
        count.to_csv(folderout + 'count/count_' + year + '.csv', index=False)   
        
def email_mapping_monthly(folderin, folderout, year_folder):
    """
    A function which takes monthly TFT data, does email mapping and deletes emails
    
    Parameters
    ----------
    
    folderin: string
             path to input folder with csv files with monthly TFT data
            
    folderout: string
           path for folder to save results in
    """
    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    
    for month in months:
        survey = pd.read_csv(folderin + '2025_' + month + '/input/survey.csv')
        lite = pd.read_csv(folderin + '2025_' + month + '/input/lite.csv')
        count = pd.read_csv(folderin + '2025_' + month + '/input/count.csv')
    
        dfs = [survey, lite, count]
  
    
        email_ref_df = pd.read_csv(year_folder + 'email_reference.csv')
    
        email_map = dict(zip(email_ref_df['email'], email_ref_df['email_id']))
    
        for df in dfs:
            df['email_id'] = df['Email'].map(email_map)
            df.drop(columns=['Email'], inplace=True)
        
        survey.to_csv(folderout + '2025_' + month + '/input/survey.csv', index=False)
        lite.to_csv(folderout + '2025_' + month + '/input/lite.csv', index=False)
        count.to_csv(folderout + '2025_' + month + '/input/count.csv', index=False)  
        
def email_mapping_rando_folder(folderin, year_folder):
    """
    A function which takes and TFT data folder, does email mapping and deletes emails
    
    Parameters
    ----------
    
    folderin: string
             path to input folder with csv files with monthly TFT data
            
    folderout: string
           path for folder to save results in
    """
    
    survey = pd.read_csv(folderin + 'survey.csv')
    lite = pd.read_csv(folderin + 'lite.csv')
    count = pd.read_csv(folderin + 'count.csv')
    
    dfs = [survey, lite, count]

    email_ref_df = pd.read_csv(year_folder + 'email_reference.csv')

    email_map = dict(zip(email_ref_df['email'], email_ref_df['email_id']))

    for df in dfs:
        df['email_id'] = df['Email'].map(email_map)
        df.drop(columns=['Email'], inplace=True)
        
    survey.to_csv(folderin + 'survey.csv', index=False)
    lite.to_csv(folderin + 'lite.csv', index=False)
    count.to_csv(folderin + 'count.csv', index=False)
