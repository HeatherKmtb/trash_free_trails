#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:29:33 2025

@author: heatherkay
"""

import pandas as pd

def monthly_stats(folderin, folderout):
    """
    A function which takes clean monthly TFT survey data and produces monthly stats
    
    Parameters
    ----------
    
    folderin: string
             path to input folder with csv files with monthly TFT data
            
    folderout: string
           path to save results
    """
    
    #create df for results - or could read in and append to overall stats sheet
    results = pd.DataFrame(columns = ['total_submisssions', 'total_count', 'total_survey',
                                      'no_people', 'duration_hours', 'items_removed',
                                      'items_surveyed', 'total_kg','total_cokecans'])
    
      
    survey = pd.read_csv(folderin + 'survey.csv')
    lite = pd.read_csv(folderin + 'lite.csv')
    count = pd.read_csv(folderin + 'count.csv')
    CSsurvey = pd.read_csv(folderin + 'CS_survey.csv')
    CScount = pd.read_csv(folderin + 'CS_count.csv')
    bag_res_lite = pd.read_csv(folderin + 'bag_res_lite.csv')
    
    dfs = [survey, CSsurvey, CScount]
    
    #total submmissions before any filtering
    count_survey = len(survey.index)    
    count_lite = len(lite.index)
    count_count = len(count.index)
    count_CSsurvey = len(CSsurvey.index)
    count_CScount = len(CScount.index)
    
    #Overview Stats
#check if Lite is included for ALL following
    CS = [count_survey, count_lite, count_count, count_CSsurvey,
                            count_CScount]
    total_CS = sum(CS)
    cnt = [count_count, count_CScount]
    total_count = sum(cnt)
    srvy = [count_survey, count_CSsurvey]
    total_survey = sum(srvy)
    
    mins = survey['Time_min']
    hours = []
    for m in mins:
        hour = m/60
        hours.append(hour)
        
    survey['Time_hours'] = hours    
    
    tot_people = []
    tot_time = []
    #tot_km = []
    tot_items = []
    for df in dfs:
        people = df['People'].sum()
        mins = df['Time_hours'].sum()
        #km = df['Distance_km'].sum()
        #items = df['TotItems'].sum()
        tot_people.append(people)
        tot_time.append(mins)
        #tot_km.append(km)
        #tot_items.append(items)
        
    srvy_items = []
    rmv_items = []    
        
    survey_items = survey['TotItems'].sum()   
    srvy_items.append(survey_items)
    rmv_items.append(survey_items)
    
    CSsurvey_items = CSsurvey['TotItems'].sum()   
    srvy_items.append(CSsurvey_items)
    rmv_items.append(CSsurvey_items)
    
    lite_items = bag_res_lite['TotItems'].sum() 
    rmv_items.append(lite_items)
    
    count_items = count['TotItems'].sum() 
    srvy_items.append(count_items)
    
    CScount_items = CScount['TotItems'].sum() 
    srvy_items.append(CScount_items)
    
    removed_items = sum(rmv_items)
    surveyed_items = sum(srvy_items)
    
    tot_people.append(count_lite)
    
    total_people = sum(tot_people)
    total_time = sum(tot_time)
    #total_km = sum(tot_km)
    #total_items = sum(tot_items)

    total_kg = removed_items / 57  
    total_cokecans = removed_items / 1.04
    
    #Count stats
    dfs = (count, CScount)        
    df = pd.concat(dfs, ignore_index = True) 
    km = df['Distance_km'].sum()
    items = df['TotItems'].sum()  
    prevalence = items/km
    
                                      
    results = results.append({'total_submisssions':total_CS, 'total_count':total_count,
                              'total_survey':total_survey,'no_people':total_people, 
                              'duration_hours':total_time, 'items_removed':removed_items,
                              'items_surveyed':surveyed_items, 'total_kg':total_kg,
                              'total_cokecans':total_cokecans}, ignore_index=True)                                         
    
    results.to_csv('/Users/heatherkay/Documents/TrashFreeTrails/Data/Monthly stats/Output/Feb_25/new.csv')
    
    
#COMPARE ORIG & CS DATA

    
    
    
        
        
        
    
    
    
    
    
    