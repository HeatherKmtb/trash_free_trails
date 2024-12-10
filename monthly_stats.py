#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 11:35:25 2024

@author: heatherkay
"""
import pandas as pd
import glob
from os import path

def survey_monthly_stats(TFTin, dataout):
    """
    A function which takes clean monthly TFT survey data and produces monthly stats
    
    Parameters
    ----------
    
    TFTin: string
             path to input csv file with monthly TFT data
            
    dataout: string
           path to save results
    """
    
    df = pd.read_csv(TFTin)
    #create df for results - or could read in and append to existing with each row as a new month...
    results = pd.DataFrame(columns = ['total_submisssions', 'bike', 'run', 'walk',
            'combo', 'other','no_people', 'duration_mins', 'duration_hm', 'distance_km', 'items_removed',
            'no_bags', '%_SUP', 'no_animal_int', '%_animal_int',
            'no_1st_time', 'no_volunteers', ' no_A_TEAM', 'no_CHs', '%_more_connected',
            '%_met_new_people', '%_did_activity_after'])
    
    #obtain count of total submissions and per activity
    count_bike = df['ActivityBike'].value_counts().get('Bike', 0)
    count_run = df['ActivityRun'].value_counts().get('Run', 0)
    count_walk = df['ActivityWalk'].value_counts().get('Walk', 0)
    count_combo = df['ActivityCombo'].value_counts().get('Combination of the above', 0)
    count_other = df['ActivityOther'].value_counts().get('Other', 0)   
    count_total = len(df.index)
    
    #obtain total people, minutes, kilometres, items removed, no bags,
    tot_people = df['People'].sum()
    tot_mins = df['Time_min'].sum()
    tot_km = df['Distance_km'].sum()
    tot_items = df['TotItems'].sum()
    binbags = df['BinBags'].notna()
    tot_bags = binbags.sum()
    #ridiculous calcs to get minutes to hours and minutes
    hours = tot_mins/60
    h, m = divmod(hours, 1)
    mins = m * 60
    int_mins = mins.astype(int)
    int_hours = hours.astype(int)
    duration = int_hours.astype(str) + ' hours ' + int_mins.astype(str) + ' mins'
    
    #obtain total % SUP
    #calcualte no items that are SUP
    SUP=[]
    df2 = df[df['Perc_SU'].notna()]
    for index,i in df2.iterrows():
        perSUP = i['Perc_SU']
        percSUP = float(perSUP)
        totitems = i['TotItems']
        result = percSUP/100 * totitems
        SUP.append(result) 
    tot_SUP = sum(SUP) 
    #calcualte percentage
    tot_percSUP = tot_SUP/tot_items *100
    
    #obtain total and % DRS
    #depends how you want to calculate it
    
    #calculate brands
    #depends how you want to calculate it
    
    #item of the month
    #probs need to make new df for this, subset columns and calculate totals
    #then new df with col and total    
    
    #animal interaction
    count_AI = df['AnimalsY'].value_counts().get('Yes', 0)
    perc_AI = count_AI/count_total *100
    type_AI = df['AnimalsInfo'].value_counts(dropna=True)
    print(type_AI)
    
    #nature connection
    more_connected = df['Connection_ConnectionY'].value_counts().get('Yes', 0) / count_total * 100
    new_people = df['Connection_NewPeopleY'].value_counts().get('Yes', 0) / count_total * 100
    activity_after = df['Connection_ActivityAfterY'].value_counts().get('Yes', 0) / count_total * 100
    
    #participant data
    count_1sttime = df['First time '].value_counts().get('This is my first time!', 0)
    count_vol = df['Volunteer'].value_counts().get('I am a volunteer', 0)
    count_AT = df['A-Team '].value_counts().get('I am an A-TEAMer', 0)
    #Community Hubs
    CHs = df['Community Hub '].value_counts(dropna=True)
    count_CH = len(CHs)
    print(CHs) #not sure what to do with this
    name = df['Name '] + ' ' + df['Surname']
    print(name) #not sure what to do with this
    
    results = results.append({'total_submisssions':count_total, 'bike':count_bike,
            'run':count_run, 'walk':count_walk, 'combo':count_combo, 'other':count_other,
            'no_people':tot_people, 'duration_mins':tot_mins, 'duration_hm':duration, 'distance_km':tot_km,
            'items_removed':tot_items, 'no_bags':tot_bags, '%_SUP':tot_percSUP,
            'no_animal_int':count_AI, '%_animal_int':perc_AI, 'no_1st_time':count_1sttime,
            'no_volunteers':count_vol, ' no_A_TEAM':count_AT, 'no_CHs':count_CH,
            '%_more_connected':more_connected, '%_met_new_people':new_people,
            '%_did_activity_after':activity_after}, ignore_index=True)   
    
    results.to_csv(dataout)
    
def historic_survey_monthly_stats(folderin, dataout):
    """
    A function which takes clean monthly TFT survey data and produces monthly stats
    
    Parameters
    ----------
    
    TFTin: string
             path to input csv file with monthly TFT data
            
    dataout: string
           path to save results
    """
    
    fileList = glob.glob(folderin + '/*.csv')
    
    #create df for results - or could read in and append to existing with each row as a new month...
    results = pd.DataFrame(columns = ['month', 'year', 'total_submisssions', 'bike', 'run', 'walk',
                'combo', 'other','no_people', 'duration_mins', 'duration_hm', 'distance_km', 'items_removed',
                'no_bags', '%_SUP', 'no_animal_int', '%_animal_int',
                'no_1st_time', 'no_volunteers', ' no_A_TEAM', 'no_CHs', '%_more_connected',
                '%_met_new_people', '%_did_activity_after'])
    for file in fileList:
        df = pd.read_csv(file)
        hd, tl = path.split(file)
        date, csv = tl.split('.')
        date_comp = date.split('_')
        year = date_comp[0]
        month = date_comp[1]
        

        
        #obtain count of total submissions and per activity
        count_bike = df['ActivityBike'].value_counts().get('Bike', 0)
        count_run = df['ActivityRun'].value_counts().get('Run', 0)
        count_walk = df['ActivityWalk'].value_counts().get('Walk', 0)
        count_combo = df['ActivityCombo'].value_counts().get('Combination of the above', 0)
        count_other = df['ActivityOther'].value_counts().get('Other', 0)   
        count_total = len(df.index)
        
        #obtain total people, minutes, kilometres, items removed, no bags,
        tot_people = df['People'].sum()
        tot_mins = df['Time_min'].sum()
        tot_km = df['Distance_km'].sum()
        tot_items = df['TotItems'].sum()
        binbags = df['BinBags'].notna()
        tot_bags = binbags.sum()
        #ridiculous calcs to get minutes to hours and minutes
        hours = tot_mins/60
        h, m = divmod(hours, 1)
        mins = m * 60
        int_mins = mins.astype(int)
        int_hours = hours.astype(int)
        duration = int_hours.astype(str) + ' hours ' + int_mins.astype(str) + ' mins'
        
        #obtain total % SUP
        #calcualte no items that are SUP
        SUP=[]
        df2 = df[df['Perc_SU'].notna()]
        for index,i in df2.iterrows():
            percSUP = i['Perc_SU']
            totitems = i['TotItems']
            result = percSUP/100 * totitems
            SUP.append(result) 
        tot_SUP = sum(SUP) 
        #calcualte percentage
        tot_percSUP = tot_SUP/tot_items *100
        
        #obtain total and % DRS
        #depends how you want to calculate it
        
        #calculate brands
        #depends how you want to calculate it
        
        #item of the month
        #probs need to make new df for this, subset columns and calculate totals
        #then new df with col and total    
        
        #animal interaction
        count_AI = df['AnimalsY'].value_counts().get('Yes', 0)
        perc_AI = count_AI/count_total *100
        type_AI = df['AnimalsInfo'].value_counts(dropna=True)
        print(type_AI)
        
        #nature connection
        more_connected = df['Connection_ConnectionY'].value_counts().get('Yes', 0) / count_total * 100
        new_people = df['Connection_NewPeopleY'].value_counts().get('Yes', 0) / count_total * 100
        activity_after = df['Connection_ActivityAfterY'].value_counts().get('Yes', 0) / count_total * 100
        
        #participant data
        count_1sttime = df['First time '].value_counts().get('This is my first time!', 0)
        count_vol = df['Volunteer'].value_counts().get('I am a volunteer', 0)
        count_AT = df['A-Team '].value_counts().get('I am an A-TEAMer', 0)
        #Community Hubs
        CHs = df['Community Hub '].value_counts(dropna=True)
        count_CH = len(CHs)
        print(CHs) #not sure what to do with this
        name = df['Name '] + ' ' + df['Surname']
        print(name) #not sure what to do with this
        
        results = results.append({'month':month, 'year':year,'total_submisssions':count_total, 'bike':count_bike,
                'run':count_run, 'walk':count_walk, 'combo':count_combo, 'other':count_other,
                'no_people':tot_people, 'duration_mins':tot_mins, 'duration_hm':duration, 'distance_km':tot_km,
                'items_removed':tot_items, 'no_bags':tot_bags, '%_SUP':tot_percSUP,
                'no_animal_int':count_AI, '%_animal_int':perc_AI, 'no_1st_time':count_1sttime,
                'no_volunteers':count_vol, ' no_A_TEAM':count_AT, 'no_CHs':count_CH,
                '%_more_connected':more_connected, '%_met_new_people':new_people,
                '%_did_activity_after':activity_after}, ignore_index=True)   
        
    results.to_csv(dataout) 
    
def lite_monthly_stats(TFTin, year, month, folderout):     
    """
    A function which takes TFT lite data, extracts monthly data and produces stats
    
    Parameters
    ----------
    
    TFTin: string
             path to input csv file with monthly TFT data
             
    year: string
             year of data to be used
             
    month: string
             month of data to be used             
            
    folderout: string
           path to folder to save results
           
    """
    
    df=pd.read_csv(TFTin)
    
    #get data for month and year in question
    new=df.loc[df['year']==year]
    data=new.loc[new['month']==month]
    
    #remove rows with no data in the postcode
    clean = data[data['Trail Postcode'].notna()]
    
    #now extract TRUE data for each bafg size and calcualte total items per bag type
    results = pd.DataFrame(columns = ['bag', 'items', 'no. of bags'])

    #handful * ?            
    df2 = clean[clean['Quantity - Pocketful'] == True]
    bag_total = []
    nobags = []
    bag = 'pocketful'
    for index, i in df2.iterrows():
        bags = i['How many bags?']
        items = bags * 2
        bag_total.append(items) 
        nobags.append(bags)
        
    tot_items = sum(bag_total)
    tot_bags = sum(nobags)
    results = results.append({'bag': bag, 'items': tot_items, 'no. of bags': tot_bags}, ignore_index=True)  
  
    #pocketful * ?
    df2 = clean[clean['Quantity - Handful'] == True]
    bag = 'handful'
    nobags = []
    bag_total = []
    for index, i in df2.iterrows():
        bags = i['How many bags?']
        items = bags * 5
        bag_total.append(items) 
        nobags.append(bags)
 
    tot_items = sum(bag_total)
    tot_bags = sum(nobags)
    results = results.append({'bag': bag, 'items': tot_items, 'no. of bags': tot_bags}, ignore_index=True)  
     
    #bread bag * 25
    df2 = clean[clean['Quantity - Bread Bag'] == True]
    bag = 'breadbag'
    nobags = []
    bag_total = []
    for index, i in df2.iterrows():
        bags = i['How many bags?']
        items = bags * 25
        bag_total.append(items) 
        nobags.append(bags)
        
    tot_items = sum(bag_total)
    tot_bags = sum(nobags)
    results = results.append({'bag': bag, 'items': tot_items, 'no. of bags': tot_bags}, ignore_index=True)  
     
    #carrier bag * 35
    df2 = clean[clean['Quantity - Carrier Bag'] == True]
    bag = 'carrierbag'
    nobags = []
    bag_total = []
    for index, i in df2.iterrows():
        bags = i['How many bags?']
        items = bags * 35
        bag_total.append(items) 
        nobags.append(bags)
        
    tot_items = sum(bag_total)
    tot_bags = sum(nobags)
    results = results.append({'bag': bag, 'items': tot_items, 'no. of bags': tot_bags}, ignore_index=True)  

    #standard bin bag * 143
    df2 = clean[clean['Quantity - Generic Bin Bag'] == True]
    bag = 'binbag'
    nobags = []
    bag_total = []
    for index, i in df2.iterrows():
        bags = i['How many bags?']
        items = bags * 143
        bag_total.append(items) 
        nobags.append(bags)
        
    tot_items = sum(bag_total)
    tot_bags = sum(nobags)
    results = results.append({'bag': bag, 'items': tot_items, 'no. of bags': tot_bags}, ignore_index=True)  
    results.to_csv(folderout + 'bag_res_lite.csv')
    del results


    #Now do the same for each litter category
    results = pd.DataFrame(columns = ['category', 'occurences'])
    df2 = clean[clean['Categories - Pet Stuff'] == True]   
    count = len(df2.index)
    category = 'Pet Stuff'
    results = results.append({'category':category, 'occurences':count}, ignore_index=True)
    
    df2 = clean[clean['Categories - Drinks Containers'] == True]   
    count = len(df2.index)
    category = 'Drinks Containers'
    results = results.append({'category':category, 'occurences':count}, ignore_index=True)
       
    df2 = clean[clean['Categories - Sweets / Snacks / Food'] == True]   
    count = len(df2.index)
    category = 'Sweets / Snacks / Food'
    results = results.append({'category':category, 'occurences':count}, ignore_index=True)
       
    df2 = clean[clean['Categories - Smoking / Vaping / Drugs'] == True]   
    count = len(df2.index)
    category = 'Smoking / Vaping / Drugs'
    results = results.append({'category':category, 'occurences':count}, ignore_index=True)
      
    df2 = clean[clean['Categories - Farming / Foresty / Industry'] == True]   
    count = len(df2.index)
    category = 'Farming / Foresty / Industry'
    results = results.append({'category':category, 'occurences':count}, ignore_index=True)
      
    df2 = clean[clean['Categories - Hygiene / Sanitary'] == True]   
    count = len(df2.index)
    category = 'Hygiene / Sanitary'
    results = results.append({'category':category, 'occurences':count}, ignore_index=True)
      
    df2 = clean[clean['Categories - Outdoor Sports & Recreation'] == True]   
    count = len(df2.index)
    category = 'Outdoor Sports & Recreation'
    results = results.append({'category':category, 'occurences':count}, ignore_index=True)
            
    df2 = clean[clean['Categories - Textiles'] == True]   
    count = len(df2.index)
    category = 'Textiles'
    results = results.append({'category':category, 'occurences':count}, ignore_index=True)
      
    df2 = clean[clean['Categories - Household / Domestic'] == True]   
    count = len(df2.index)
    category = 'Household / Domestic'
    results = results.append({'category':category, 'occurences':count}, ignore_index=True)
      
    df2 = clean[clean['Categories - Other'] == True]   
    count = len(df2.index)
    category = 'Other'
    results = results.append({'category':category, 'occurences':count}, ignore_index=True)
          
    results.to_csv(folderout + 'litter_res_lite.csv')
    del results


    #Now do the same for animal interactions
    results = pd.DataFrame(columns = ['category', 'occurences'])
    df2 = clean[clean["Animal Interaction - Didn't Check"] == True]   
    count = len(df2.index)
    category = 'Not checked'
    results = results.append({'category':category, 'occurences':count}, ignore_index=True)
        
    df2 = clean[clean['Animal Interaction - No'] == True]   
    count = len(df2.index)
    category = 'No'
    results = results.append({'category':category, 'occurences':count}, ignore_index=True)
        
    df2 = clean[clean['Animal Interaction - Chew Marks'] == True]   
    count = len(df2.index)
    category = 'Chew Marks'
    results = results.append({'category':category, 'occurences':count}, ignore_index=True)
        
    df2 = clean[clean['Animal Interaction - Death'] == True]   
    count = len(df2.index)
    category = 'Death'
    results = results.append({'category':category, 'occurences':count}, ignore_index=True)
            
    results.to_csv(folderout + 'animal_res_lite.csv')
    del results


    #and again for nature connection
    results = pd.DataFrame(columns = ['category', 'occurences'])
    df2 = clean[clean['Increased Nature Connection - No'] == True]   
    count = len(df2.index)
    category = 'No'
    results = results.append({'category':category, 'occurences':count}, ignore_index=True)
        
    df2 = clean[clean['Increased Nature Connection - No Change'] == True]   
    count = len(df2.index)
    category = 'No Change'
    results = results.append({'category':category, 'occurences':count}, ignore_index=True)
        
    df2 = clean[clean['Increased Nature Connection - Yes'] == True]   
    count = len(df2.index)
    category = 'Yes'
    results = results.append({'category':category, 'occurences':count}, ignore_index=True)
        
    df2 = clean[clean['Increased Nature Connection - Not Sure'] == True]   
    count = len(df2.index)
    category = 'Not Sure'
    results = results.append({'category':category, 'occurences':count}, ignore_index=True)
            
    results.to_csv(folderout + 'nat_con_res_lite.csv')
    del results











     

    