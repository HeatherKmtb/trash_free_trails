#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:29:33 2025

@author: heatherkay
"""

import pandas as pd

def overview_stats(folderin, folderout):
    """
    A function which takes clean monthly TFT survey data and produces monthly stats
    
    Parameters
    ----------
    
    folderin: string
             path to input folder with csv files with monthly TFT data
            
    folderout: string
           path for folder to save results in
    """
    
    #create df for results - or could read in and append to overall stats sheet
    results = pd.DataFrame(columns = ['total_submisssions', 'total_count', 'total_survey',
                                      'no_people', 'area_km2', 'distance_km','duration_hours', 
                                      'items_removed','items_surveyed', 'total_items',
                                      'total_kg','total_cokecans'])
    
      
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
    
    #Overview Stats - submitted data

    CS = [count_survey, count_lite, count_count, count_CSsurvey,
                            count_CScount]
#Total combined data sets submitted
    total_CS = sum(CS)
    cnt = [count_count, count_CScount]
#Total Count Datasets
    total_count = sum(cnt)
    srvy = [count_survey, count_CSsurvey]
#Total survey dasets
    total_survey = sum(srvy)
    
    #Overview - volunteers, distance, hours, items
    mins = survey['Time_min']
    hours = []
    for m in mins:
        hour = m/60
        hours.append(hour)
        
    survey['Time_hours'] = hours    
    
    tot_people = []
    tot_time = []

    for df in dfs: #survey, CSsurvey & CS count
        people = df['People'].sum()
        hours = df['Time_hours'].sum()
        #km = df['Distance_km'].sum()
        #items = df['TotItems'].sum()
        tot_people.append(people)
        tot_time.append(hours)
        #tot_km.append(km)
        #tot_items.append(items)
    
    #add to total people the number of lite and count submissions
    tot_people.append(count_lite)
    tot_people.append(count_count)
 
#volunteers
    total_people = sum(tot_people)
    
    survey_km = survey['Distance_km'].sum()
    count_m = count['Total_distance_m'].sum()
    count_km = count_m / 1000
    CScount_m = CScount['Total_distance_m'].sum()
    CScount_km = CScount_m / 1000
    
    survey_area = survey_km * 0.006
    count_area = count_km * 0.006
    CScount_area = CScount_km * 0.006
    CSsurvey_area = CSsurvey['Area_km2'].sum()
    
    areas = [survey_area, count_area, CScount_area, CSsurvey_area]
#area cleaned / surveyed - excludes Lite
    area = areas.sum()
    
    CSsurvey_km = CSsurvey_area / 0.006
    kms = [survey_km, count_km, CSsurvey_km, CScount_km]
#distance cleaned / surveyed - excludes Lite
    km = kms.sum()
        
    #method to estimate time spent on count
    count_time = count_count * 1.52
    tot_time.apppend(count_time)
#time - excludes Lite
    total_time = sum(tot_time) #doesn't include lite - no data

    
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
    tot_items = surveyed_items
    tot_items.append(lite_items)
#total items
    total_items = sum(tot_items)
#weight removed items
    total_kg = removed_items / 57  
#volume of removed items as number of coke cans
    total_cokecans = removed_items / 1.04
    
    results = results.append({'total_submisssions':total_CS, 'total_count':total_count,
                              'total_survey':total_survey,'no_people':total_people, 
                              'area_km2':area, 'distance_km':km,
                              'duration_hours':total_time, 'items_removed':removed_items,
                              'items_surveyed':surveyed_items, 'total_items':total_items,
                              'total_kg':total_kg,'total_cokecans':total_cokecans}, ignore_index=True)                                         
    
    results.to_csv(folderout + '/overview.csv')    
    
    

    count_results = pd.DataFrame(columns = ['count_submisssions', 'prevalence', 'total_survey',
                                      'no_people', 'area_km2', 'distance_km','duration_hours', 
                                      'items_removed','items_surveyed', 'total_items',
                                      'total_kg','total_cokecans'])
    
    
    #Count stats
     
    
    #this will only work once dfs are the same 
    #dfs = (count, CScount) 
    #df = pd.concat(dfs, ignore_index = True) 
    #km = df['Distance_km'].sum()
    #items = df['TotItems'].sum()  
    #prevalence = items/km
    
    distance = CScount_km + count_km
    items = CScount_items + count_items
#how much is out there per km
    prevalence = items/distance
    
    
    
    
    
                                      

    
    
#COMPARE ORIG & CS DATA

    
    
    
        
        
        
    
    
    
    
    
    