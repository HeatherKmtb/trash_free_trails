#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 08:59:54 2025

@author: heatherkay
"""

import pandas as pd

def CS_stats(folderin, folderout):
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
    results = pd.DataFrame(columns = ['total_submisssions', 'total_count', 
                                      'total_survey', 'total_lite', 'trash_watch',
                                      'no_people','area_km2','distance_km','duration_hours', 
                                      'items_removed','items_surveyed', 'total_items',
                                      'total_kg','total_cokecans','Adjusted Total Items'])
    
    CSsurvey = pd.read_csv(folderin + 'CS_survey/CS_survey_all.csv')
    CScount = pd.read_csv(folderin + 'CS_count/CS_count_all.csv')

    
    dfs = [CSsurvey, CScount]
    
    #total submmissions before any filtering
    count_CSsurvey = len(CSsurvey.index)
    count_CScount = len(CScount.index)
    
    #Overview Stats - submitted data

    CS = [count_CSsurvey, count_CScount]
#Total combined data sets submitted
    total_CS = sum(CS)

#Total Count Datasets
    total_count = count_CScount

#Total survey dasets
    total_survey = count_CSsurvey
#Total lite datasets calculated as count_lite
    
    
    #Overview - volunteers, distance, hours, items
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
    
 
#volunteers
    total_people = sum(tot_people)
    
    CScount_m = CScount['Total_distance(m)'].sum()
    CScount_km = CScount_m / 1000
    
#area cleaned / surveyed - excludes Lite
    area = CSsurvey['Area_km2'].sum()  
    
    CSsurvey_km = area / 0.006
    kms = [CSsurvey_km, CScount_km]
#distance cleaned / surveyed 
    km = sum(kms)
        
#time 
    total_time = sum(tot_time) 

    all_items = ['Value Full Dog Poo Bags','Value Unused Dog Poo Bags',
    'Value Toys (eg., tennis balls)','Value Other Pet Related Stuff',
    'Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
    'Value Aluminium soft drink cans','Value Plastic bottle, top','Value Glass soft drink bottles',
    'Value Plastic energy drink bottles','Value Aluminium energy drink can',
    'Value Plastic energy gel sachet','Value Plastic energy gel end','Value Aluminium alcoholic drink cans',
    'Value Glass alcoholic bottles','Value Glass bottle tops','Value Hot drinks cups',
    'Value Hot drinks tops and stirrers','Value Drinks cups (eg., McDonalds drinks)',
    'Value Drinks tops (eg., McDonalds drinks)','Value Cartons','Value Plastic straws',
    'Value Paper straws','Value Plastic carrier bags','Value Plastic bin bags',
    'Value Confectionary/sweet wrappers','Value Wrapper "corners" / tear-offs',
    'Value Other confectionary (eg., Lollipop Sticks)','Value Crisps Packets',
    'Value Used Chewing Gum','Value Plastic fast food, takeaway and / or on the go food packaging, cups, cutlery etc',
    'Value Other fast food, takeaway and / or on the go food packaging, cups, cutlery (eg., cardboard)',
    'Value Disposable BBQs and / or BBQ related items','Value BBQs and / or BBQ related items',
    'Value Food on the go (eg.salad boxes)','Value Homemade lunch (eg., aluminium foil, cling film)',
    'Value Fruit peel & cores','Value Cigarette Butts','Value Smoking related',
    'Value Disposable vapes','Value Vaping / E-Cigarette Paraphernalia','Value Drugs related',
    'Value Farming','Value Salt/mineral lick buckets','Value Silage wrap',
    'Value Forestry','Value Tree guards','Value Industrial','Value Cable ties',
    'Value Industrial plastic wrap','Value Toilet tissue','Value Face/ baby wipes',
    'Value Nappies','Value Single-Use Period products','Value Single-Use Covid Masks',
    'Value Rubber/nitrile gloves','Value Outdoor event (eg Festival)','Value Camping',
    'Value Halloween & Fireworks','Value Seasonal (Christmas and/or Easter)',
    'Value Normal balloons','Value Helium balloons','Value MTB related (e.g. inner tubes, water bottles etc)',
    'Value Running','Value Roaming and other outdoor related (e.g. climbing, kayaking)',
    'Value Outdoor sports event related (e.g.race)','Value Textiles','Value Clothes & Footwear',
    'Value Plastic milk bottles','Value Plastic food containers','Value Cardboard food containers',
    'Value Cleaning products containers','Value Miscellaneous','Value Too small/dirty to ID',
    'Value Weird/Retro']
    
    reported_items = CSsurvey.sum(axis=0)[all_items].to_list()
    
    total_reported_items = sum(reported_items)
    
    srvy_items = []
    rmv_items = []       
            
    CSsurvey_items = CSsurvey['TotItems'].sum()   
    srvy_items.append(CSsurvey_items)
    rmv_items.append(CSsurvey_items)
        
    CScount_items = CScount['TotItems'].sum() 
    srvy_items.append(CScount_items)
    
    removed_items = sum(rmv_items)
    surveyed_items = sum(srvy_items)   
#total removed items (reported)
    total_items = surveyed_items

#weight removed items
    total_kg = removed_items / 57  
#volume of removed items as number of coke cans
    total_cokecans = removed_items / 1.04
    
    
    ATIs = []
    for index, i in CSsurvey.iterrows():
        TotItems = i['TotItems']#.astype(float)
        people = i['People']#.astype(float)
        hours = i['Time_hours']#.astype(float)
        time = hours*60
        area = i['Area_km2']#.astype(float)
        dist = area / 0.006
        #calculate ATI
        denominator = (people*time)*dist
        if denominator == 0:
            continue
        AdjTotItems = TotItems/denominator 
        if AdjTotItems > 0:
            ATIs.append(AdjTotItems)
        
    for index, i in CScount.iterrows():
        TotItems = i['TotItems']#.astype(float)
        people = i['People']#.astype(float)
        hours = i['Time_hours']#.astype(float)
        time = hours*60
        m = i['Total_distance(m)']#.astype(float)
        kmcs = m / 1000
        #calculate ATI
        denominator = (people*time)*kmcs
        if denominator == 0:
            continue
        AdjTotItems = TotItems/denominator     
        if AdjTotItems > 0:
            ATIs.append(AdjTotItems) 
              
    
    ATI = sum(ATIs)
#Adjusted total items    

    
    results = results.append({'total_submisssions':total_CS, 'total_count':total_count,
                              'total_survey':total_survey,'no_people':total_people, 
                              'area_km2':area, 'distance_km':km,
                              'duration_hours':total_time, 'items_removed':removed_items,
                              'items_surveyed':surveyed_items, 'total_items':total_items,
                              'total_kg':total_kg,'total_cokecans':total_cokecans,
                              'Adjusted Total Items':ATI}, ignore_index=True)                                         
    
    results.to_csv(folderout + '/overview.csv',index=False)    

    
    impacts_results = pd.DataFrame(columns = ['Fauna Interaction', 'Fauna Death',
                    'First Time', 'Repeat volunteers','Felt proud',
                    'Felt more connected','met someone inspiring', 'went out after',
                    'Would do again','provided contact info'])
    
    #animal interaction - how many (%) answered the question and checked
    CSsurv_AIcols = ['AnimalsY','AnimalsN','AnimalsInfo']
    CScount_AIcols = ['AIY','AIN','AINotSure']


    AI_CSsurvey = CSsurvey[CSsurv_AIcols].notna().any(axis=1).sum()
    AI_CScount = CScount[CScount_AIcols].notna().any(axis=1).sum()

    
    AI_subs = [AI_CSsurvey, AI_CScount]
    subs_tot = sum(AI_subs)
    CSsurvey_AI = CSsurvey['AnimalsY'].value_counts().get('Yes', 0)
    CScount_AI = CScount['AIY'].value_counts().get('Yes', 0)
    AI_yes = [CSsurvey_AI, CScount_AI]
    AI_tot = sum(AI_yes)
    
#percent submissions reporting AI observed
    perc_AI = (AI_tot/subs_tot)*100
    
    dfs = [CSsurvey]
    deaths = []
    for df in dfs:
        death = df['AnimalsInfo'].str.contains(r'\b(death|dead)\b', case=False, na=False).sum()
        deaths.append(death)
    
    tot_deaths = sum(deaths)
    subs_for_death = [AI_CSsurvey]
    death_subs_tot = sum(subs_for_death)
#percent submissions reporting death of those reporting they checked for AI  
    perc_death = (tot_deaths/death_subs_tot)*100
    
 
    p_CSsurvey4 = CSsurvey['Connection_Action'].value_counts().get(4, 0)
    p_CScount4 = CScount['Connect_Feel'].value_counts().get(4, 0)
    p_CSsurvey5 = CSsurvey['Connection_Action'].value_counts().get(5, 0)
    p_CScount5 = CScount['Connect_Feel'].value_counts().get(5, 0)
    proud = [p_CSsurvey4, p_CScount4, p_CSsurvey5, p_CScount5]     
    prouds = sum(proud)

    na_CSsurvey = CSsurvey['Connection_Action'].notna().sum()
    na_CScount = CScount['Connect_Feel'].notna().sum()
    nas = [na_CSsurvey, na_CScount]
    count_nas = sum(nas)
#percent feeling proud after taking action 
    perc_proud = (prouds/count_nas) * 100

    dfs = [CSsurvey]
    connection = []
    counts_connect = []
    for df in dfs:
        more_connected = df['Connection_ConnectionY'].value_counts().get('Yes', 0) 
        connection.append(more_connected)
        columns_of_interest = ['Connection_ConnectionY', 'Connection_ConnectionN', 
                               'Connection_ConnectionSame', 'Connection_Unsure'] #won't work for count until redo columns
        count_connect = df[columns_of_interest].notnull().any(axis=1).sum()
        counts_connect.append(count_connect)
       
    total_answer_connect = sum(counts_connect)
    connects = sum(connection)
#percent feeling more connected    
    perc_more_connected = (connects/total_answer_connect) *100
    
    dfs = [CSsurvey] 
    people = []
    answered_p = []
    activity = []
    answered_a = []
    people_cols = ['Connection_NewPeopleY', 'Connection_NewPeopleN']
    activity_cols = ['Connection_ActivityAfterY', 'Connection_ActivityAfterN']
    for df in dfs:
        new_people = df['Connection_NewPeopleY'].value_counts().get('Yes', 0)
        answered_people = df[people_cols].notnull().any(axis=1).sum()
        activity_after = df['Connection_ActivityAfterY'].value_counts().get('Yes', 0)
        answered_activity = df[activity_cols].notnull().any(axis=1).sum()
        people.append(new_people)
        answered_p.append(answered_people)
        activity.append(activity_after)
        answered_a.append(answered_activity)
    
    new_people = sum(people)
    ans_people = sum(answered_p)
#percentage meeting inspiring/new people    
    perc_new_peeps = (new_people/ans_people) *100
    
    active_after = sum(activity)
    ans_act = sum(answered_a)
#percentage doing an activity after
    perc_active = (active_after/ans_act) * 100
    

    impacts_results = impacts_results.append({'Fauna Interaction':perc_AI, 
                    'Fauna Death':perc_death,'Felt proud':perc_proud,
                       'Felt more connected':perc_more_connected,
                       'met someone inspiring':perc_new_peeps, 
                       'went out after':perc_active}, ignore_index=True)     
    
    impacts_results.to_csv(folderout + '/impacts.csv', index=False) 
           
            
            
          