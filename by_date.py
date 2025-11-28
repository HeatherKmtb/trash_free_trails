#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 09:48:08 2025

@author: heatherkay
"""
import pandas as pd

def date_range_stats(folderin, start_date, end_date):
    """
    A function which takes clean monthly TFT survey data and produces monthly stats
    
    Parameters
    ----------
    
    folderin: string
             path to input folder with csv files with monthly TFT data
            
    start_date: string
           date - format d/m/y
           
    end_date: string
           date - format d/m/y
    """

    survey = pd.read_csv(folderin + 'survey/survey_2025.csv')
    lite = pd.read_csv(folderin + 'lite/lite_2025.csv')
    count = pd.read_csv(folderin + 'count/count_2025.csv')
    CSsurvey = pd.read_csv(folderin + 'CS_survey/CS_survey_2025.csv')
    CScount = pd.read_csv(folderin + 'CS_count/CS_count_2025.csv')
    #bag_res_lite = pd.read_csv(folderin + 'bag_res_lite.csv')
    tfr = pd.read_csv(folderin + 'TFR/TFR_2025.csv')
    
    #prepping the date columns
    dfs_TrailClean = [survey, CSsurvey]
    
    dfs_Count = [count, CScount]
    
    tfr['date_dt'] = pd.to_datetime(tfr['Start_Date'], format='%d/%m/%Y')
    tfr.insert(1, 'date_dt', tfr.pop('date_dt'))
    

    lite['date_dt'] = pd.to_datetime(lite['Created Date'])
    lite['date_dmy'] = lite['date_dt'].dt.strftime('%d/%m/%Y')
    lite.insert(1, 'date_dmy', lite.pop('date_dmy'))
    
    for df in dfs_TrailClean:
        df['date_dt'] = pd.to_datetime(df['Date_TrailClean'], format='%d/%m/%Y')
        df.insert(1, 'date_dt', df.pop('date_dt'))
        
    for df in dfs_Count:
        df['date_dt'] = pd.to_datetime(df['Date_Count'], format='%d/%m/%Y')
        df.insert(1, 'date_dt', df.pop('date_dt'))
    
    #getting total items
    dfs = {"survey": survey,"CSsurvey": CSsurvey,"count": count,
    "CScount": CScount,"tfr": tfr,"lite": lite}

    start = pd.to_datetime(start_date, dayfirst=True)
    end   = pd.to_datetime(end_date, dayfirst=True)
    
    items = []

    for name, df in dfs.items():
        df['date_dt'] = df['date_dt'].dt.tz_localize(None)
        dfs[name] = df[(df['date_dt'] >= start) & (df['date_dt'] <= end)]  
        itms = dfs[name]['TotItems']
        clean_items = []
        for x in itms:
            if x == x:
                clean_items.append(x)
            
        total = sum(clean_items)
        items.append(total)
        
        
    tot_items = sum(items)
    
    print(tot_items)
    
def date_and_location_stats(folderin, start_date, end_date, postcode):
    """
    A function which takes clean monthly TFT survey data and produces monthly stats
    
    Parameters
    ----------
    
    folderin: string
             path to input folder with csv files with monthly TFT data
            
    start_date: string
           date - format d/m/y
           
    end_date: string
           date - format d/m/y
           
    postcode: string
           postcode - start of postcode in uppercase
    """

    survey = pd.read_csv(folderin + 'survey/all_survey.csv')
    lite = pd.read_csv(folderin + 'lite/all_lite.csv')
    count = pd.read_csv(folderin + 'count/all_count.csv')
    CSsurvey = pd.read_csv(folderin + 'CS_survey/all_CS_survey.csv')
    CScount = pd.read_csv(folderin + 'CS_count/all_CS_count.csv')
    #bag_res_lite = pd.read_csv(folderin + 'bag_res_lite.csv')
    tfr = pd.read_csv(folderin + 'TFR/all_TFR.csv')
    
    #prepping the date columns
    dfs_TrailClean = [survey, CSsurvey]
    
    dfs_Count = [count, CScount]
    
    tfr['date_dt'] = pd.to_datetime(tfr['Start_Date'], format='%d/%m/%Y')
    tfr.insert(1, 'date_dt', tfr.pop('date_dt'))
    

    lite['date_dt'] = pd.to_datetime(lite['Created Date'])
    lite['date_dmy'] = lite['date_dt'].dt.strftime('%d/%m/%Y')
    lite.insert(1, 'date_dmy', lite.pop('date_dmy'))
    lite = lite.rename({'Trail Postcode':'postcode'}, axis=1)
    
    for df in dfs_TrailClean:
        df['date_dt'] = pd.to_datetime(df['Date_TrailClean'], format='%d/%m/%Y')
        df.insert(1, 'date_dt', df.pop('date_dt'))
        
    for df in dfs_Count:
        df['date_dt'] = pd.to_datetime(df['Date_Count'], format='%d/%m/%Y')
        df.insert(1, 'date_dt', df.pop('date_dt'))
    
    #getting total items
    dfs = {"survey": survey,"CSsurvey": CSsurvey,"count": count,
    "CScount": CScount,"tfr": tfr,"lite": lite}

    start = pd.to_datetime(start_date, dayfirst=True)
    end   = pd.to_datetime(end_date, dayfirst=True)
    
    items = []

    for name, df in dfs.items():
        df['postcode'] = df['postcode'].str.upper()
        df['date_dt'] = df['date_dt'].dt.tz_localize(None)
        dfs[name] = df[(df['date_dt'] >= start) & 
                       (df['date_dt'] <= end) &
                       (df['postcode'].str.startswith(postcode, na=False))]  
        itms = dfs[name]['TotItems']
        clean_items = []
        for x in itms:
            if x == x:
                clean_items.append(x)
            
        total = sum(clean_items)
        items.append(total)
        
        
    tot_items = sum(items)
    
    print(tot_items)
    
    
    
    