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
    
#rest TBD




    #Survey stats
    
#first ones currently covered in overvies
    
    kms_survey = [survey_km, CSsurvey_km] 
#distance covered - doesn't include Lite    
    km_survey = kms_survey.sum()
    
    areas_survey = [survey_area,  CSsurvey_area]
#area directly protected - excludes Lite
    area_survey = areas_survey.sum()   
    
    plastic = ['BinBags','Full Dog Poo Bags',
            'Unused Dog Poo Bags','Toys (eg., tennis balls)','Other Pet Related Stuff',
            'Plastic Water Bottles','Plastic Soft Drink Bottles',
            'Plastic bottle, top','Plastic energy drink bottles',
            'Plastic energy gel sachet','Plastic energy gel end', 'Plastic straws',
            'Hot drinks tops and stirrers','Drinks cups (eg., McDonalds drinks)',
            'Plastic carrier bags','Plastic bin bags',
            'Plastic fast food, takeaway and / or on the go food packaging, cups, cutlery etc',
            'Confectionary/sweet wrappers',
            'Wrapper "corners" / tear-offs','Other confectionary (eg., Lollipop Sticks)',
            'Crisps Packets','Disposable vapes','Salt/mineral lick buckets','Silage wrap',
            'Tree guards','Cable ties','Industrial plastic wrap','Rubber/nitrile gloves',
            'Normal balloons','Helium balloons','Plastic milk bottles',
            'Plastic food containers','Cleaning products containers']
            
            
    potentially_plastic = ['Hot drinks cups','Drinks tops (eg., McDonalds drinks)',
                           'Food on the go (eg.salad boxes)']        
            
    metal = ['Aluminium soft drink cans','Aluminium energy drink can',
             'Aluminium alcoholic drink cans','Glass bottle tops',
             'Disposable BBQs and / or BBQ related items','BBQs and / or BBQ related items',]   

    glass = ['Glass soft drink bottles','Glass alcoholic bottles',]     
    
    cardboard_paper_wood = ['Cartons','Paper straws',
            'Other fast food, takeaway and / or on the go food packaging, cups, cutlery (eg., cardboard)',
            'Vaping / E-Cigarette Paraphernalia','Toilet tissue','Cardboard food containers',]
    
    other = ['Used Chewing Gum','Fruit peel & cores','Cigarette Butts','Smoking related',
             'Drugs related','Farming',
             'Forestry','Industrial','Homemade lunch (eg., aluminium foil, cling film)',
             'Face/ baby wipes',
             'Nappies','Single-Use Period products','Single-Use Covid Masks',
             'Outdoor event (eg Festival)','Camping','Halloween & Fireworks','Seasonal (Christmas and/or Easter)',
             'MTB related (e.g. inner tubes, water bottles etc)',
             'Running','Roaming and other outdoor related (e.g. climbing, kayaking)',
             'Outdoor sports event related (e.g.race)','Textiles','Clothes & Footwear',
             'Miscellaneous','Too small/dirty to ID','Weird/Retro']
    
    
    plastics = []
    metals = []
    glasses = []
    papers = []
    for p in plastic:
        item = survey[p].sum()
        CSitem = CSsurvey[p].sum()
        total = item + CSitem
        plastics.append(total)
        
    for p in metal:
        item = survey[p].sum()
        CSitem = CSsurvey[p].sum()
        total = item + CSitem
        metals.append(total)

    for p in glass:
        item = survey[p].sum()
        CSitem = CSsurvey[p].sum()
        total = item + CSitem
        glasses.append(total)

    for p in papers:
        item = survey[p].sum()
        CSitem = CSsurvey[p].sum()
        total = item + CSitem
        papers.append(total)             
           
            
           
            
            
            
            
            
            
    
    
                                      

    
    
#COMPARE ORIG & CS DATA

    
    
    
        
        
        
    
    
    
    
    
    