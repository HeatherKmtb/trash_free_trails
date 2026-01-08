#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:21:47 2024

@author: heatherkay
"""
import pandas as pd
import numpy as np
import statistics
import glob
from os import path
from rapidfuzz import process
import re
import matplotlib.pyplot as plt

def get_data_quantity_per_month(datain, dataout):
    """
    A function which takes full survey data and gets overall and yearly mean submissions per month
    
    Parameters
    ----------
    
    datain: string
             path to input csv file with all TFT survey data
            
    dataout: string
           path to save results
    """


    df2 = pd.read_csv(datain)
    #get list of years and months
    years = list(np.unique(df2['year']))
    months = list(np.unique(df2['month']))
    
    count = []
    
    for year in years:
        #extract data for one year
        new=df2.loc[df2['year']==year]
        #extract data for each month
        for month in months:
            data=new.loc[new['month']==month]
            if data.empty:
                continue
            submissions = len(data.index)
            count.append(submissions)
            
    monthly_mean = statistics.mean(count)
    
    results = pd.DataFrame(columns = ['year', 'submissions'])

    for year in years:
        count = []
        #extract data for one year
        new=df2.loc[df2['year']==year]
        #extract data for each month
        for month in months:
            data=new.loc[new['month']==month]
            if data.empty:
                continue
            submissions = len(data.index)
            count.append(submissions)
        monthly_mean = statistics.mean(count)    
        
        results = results.append({'year':year, 'mean':monthly_mean}, ignore_index = True)
        
        results.to_csv(dataout)
        
def average_hours_per_person(datain):
    """
    A function which takes full survey data and gets average volunteer hours per person
    
    Parameters
    ----------
    
    datain: string
             path to input csv file with all TFT survey data

    """
    df2 = pd.read_csv(datain)
    
    total = []
    for index, i in df2.iterrows():
        mins = i['Time_min']
        people = i['People']
        hours = mins/60
        tot = people * hours
        total.append(tot)
        
    total_hours = sum(total)
    people = df2['People']
    total_people = sum(people)
    average = total_hours / total_people
    
def get_schools(TFTin, TFTout):
    
    df = pd.read_csv(TFTin)
    
    cols = ['TrailName']

    mask = df[cols].astype(str).agg(
        lambda row: row.str.contains("mob", case=False).any(),
        axis=1)

    result = df[mask]
    
    result.to_csv(TFTout)
            


def ateam_weekender(TFT24in, TFT25in, fileout):
    """
    A function which takes TFT dats since A-TEAMers were seperated and calcuates
    some stats.
    
    Parameters
    ----------
    
    TFT24in: string
             path to input folder with 2024.csv file with TFT data
             
    TFT25in: string
             path to input folder with 2024.csv file with TFT data             
            
    fileout: string
           path for file to save results in
    """         
    
    df1 = pd.read_csv(TFT24in)
    df2 = pd.read_csv(TFT25in)
    
    dfs = [df1, df2]
    df = pd.concat(dfs, ignore_index=True)
    
    results = pd.DataFrame(columns = ['kms_cleaned', 'total_items','top 3 items',
                                      'top 3 brands', 'top 3 a-teamers (most cleans)',
                                      '%DRS'])
                           
    dfA = df[df['A-Team '].notna()]
    km = dfA['Distance_km'].sum()
    tot_items = dfA['TotItems'].sum() 
    
    items = ['Full Dog Poo Bags','Unused Dog Poo Bags','Toys (eg., tennis balls)','Other Pet Related Stuff',
          'Plastic Water Bottles','Plastic Soft Drink Bottles','Aluminium soft drink cans',
          'Plastic bottle, top','Glass soft drink bottles','Plastic energy drink bottles',
          'Aluminium energy drink can','Plastic energy gel sachet','Plastic energy gel end',
          'Aluminium alcoholic drink cans','Glass alcoholic bottles','Glass bottle tops',
          'Hot drinks cups','Hot drinks tops and stirrers','Drinks cups (eg., McDonalds drinks)',
          'Drinks tops (eg., McDonalds drinks)','Cartons','Plastic straws','Paper straws',
          'Plastic carrier bags','Plastic bin bags','Confectionary/sweet wrappers',
          'Wrapper "corners" / tear-offs','Other confectionary (eg., Lollipop Sticks)',
          'Crisps Packets','Used Chewing Gum',
          'Plastic fast food, takeaway and / or on the go food packaging, cups, cutlery etc',
          'Other fast food, takeaway and / or on the go food packaging, cups, cutlery (eg., cardboard)',
          'Disposable BBQs and / or BBQ related items','BBQs and / or BBQ related items',
          'Food on the go (eg.salad boxes)','Homemade lunch (eg., aluminium foil, cling film)',
          'Fruit peel & cores','Cigarette Butts','Smoking related','Disposable vapes',
          'Vaping / E-Cigarette Paraphernalia','Drugs related','Farming',
          'Salt/mineral lick buckets','Silage wrap','Forestry','Tree guards','Industrial',
          'Cable ties','Industrial plastic wrap','Toilet tissue','Face/ baby wipes',
          'Nappies','Single-Use Period products','Single-Use Covid Masks','Rubber/nitrile gloves',
          'Outdoor event (eg Festival)','Camping','Halloween & Fireworks','Seasonal (Christmas and/or Easter)',
          'Normal balloons','Helium balloons','MTB related (e.g. inner tubes, water bottles etc)',
          'Running','Roaming and other outdoor related (e.g. climbing, kayaking)',
          'Outdoor sports event related (e.g.race)','Textiles','Clothes & Footwear',
          'Plastic milk bottles','Plastic food containers','Cardboard food containers',
          'Cleaning products containers','Miscellaneous','Too small/dirty to ID',
          'Weird/Retro']   
    
    
    # Filter your DataFrame to just the columns that match your items
    matching_cols = [col for col in df.columns if col in items]

    # Sum the values in each item column
    item_totals = dfA[matching_cols].sum().sort_values(ascending=False)

    # Get the top 3 items
    top_3_items = item_totals.head(3)

            
    #calculate brands
    brands = ['Lucozade','Coke','RedBull','Monster','Cadbury','McDonalds','Walkers','Mars','StellaArtois','Strongbow',
              'Costa','Budweiser','Haribo','SIS','Carling','Fosters','Thatchers','Pepsi','Nestle','Subway','Other']
    
    brand_res = pd.DataFrame(columns = ['brand','count'])
                             
    for b in brands:
        b1 = df[df['B1_' + b].notna()]
        b2 = df[df['B2_' + b].notna()]
        b3 = df[df['B3_' + b].notna()]
        dfs = (b1, b2, b3)
        brand = pd.concat(dfs, ignore_index = True)
          
    # Sum the values in each brand column
    brand_totals = dfA[brand].sum().sort_values(ascending=False)

    # Get the top 3 items
    top_3_brands = brand_totals.head(3)        


    
    
    dfA['Name'] = dfA['Name'].astype(str)
    dfA['Surname'] = dfA['Surname'].astype(str)
    dfA['full_name'] = dfA['Name'].fillna('') + ' ' + dfA['Surname'].fillna('')
    dfA['full_name'] = dfA['full_name'].str.strip().str.lower()
    
    mask_fullname_in_name = dfA.apply(lambda row: row['Surname'].lower() in row['Name'].lower(), axis=1)
    dfA.loc[mask_fullname_in_name, 'full_name'] = dfA.loc[mask_fullname_in_name, 'Name'].str.lower().str.strip()

    # Get unique names
    unique_names = dfA['full_name'].unique()

    # Map similar names to a canonical name
    name_map = {}
    canonical_names = []
    for name in unique_names:
        result = process.extractOne(name, canonical_names, score_cutoff=90)
    
        if result:  # result is a tuple like (match, score, index)
           match = result[0]
           name_map[name] = match
        else:
            name_map[name] = name
            canonical_names.append(name)

    # Apply mapping
    dfA['cleaned_name'] = dfA['full_name'].map(name_map)      
    top_contributors = dfA['cleaned_name'].value_counts().head(3)
    
    DRS = ['Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
    'Value Aluminium soft drink cans', 'Value Glass soft drink bottles',
    'Value Plastic energy drink bottles','Value Aluminium energy drink can',
    'Value Aluminium alcoholic drink cans','Value Glass alcoholic bottles']
                                      
    DRSs = dfA.sum(axis=0)[DRS].to_list() 
    DRS_items = sum(DRSs)
    perc_DRS = (DRS_items/tot_items)*100


def ateam_weekender_alt(folderin,  folderout):
    """
    A function which takes TFT dats since A-TEAMers were seperated and calcuates
    some stats.
    
    Parameters
    ----------
    
    folderin: string
             path to input folder with yearly TFT data
             
    fileout: string
           path for file to save results in
    """   
    
    Names = ['alistair hair', 'andy lund', 'chloe parker', 'dan jarvis', 
             'dom barry', 'ed roberts', 'emma johnson', 'gill houlsby', 
             'hannah lowther', 'hari milburn', 'harry wood', 'ian white', 
             'ian lean', 'jake rainford', 'james mackeddie', 'jane chisholm', 
             'jay schreiber', 'jo shwe', 'john bellis', 'kyle harvey', 
             'lauren munro-bennet', 'leon rosser', 'mario presi', 'mark wilson', 
             'marv davies', 'matt kennelly', 'monet adams', 'neil hudson', 
             'nush lee', 'pete scullion', 'ram gurung', 'rosie holdsworth', 
             'ross lambie', 'sam piper', 'tom laws', 'will atkinson', 
             'victoria herbert', 'ollie cain', 'laurance ward', 'tim bowden', 
             'kristina vackova', 'helen wilson', 'lauren cattell']
    
    
    df1 = pd.read_csv(folderin + 'survey/survey_2024.csv')
    df2 = pd.read_csv(folderin + 'survey/survey_2025.csv')
    
    dfs = [df1, df2]
    dfA = pd.concat(dfs, ignore_index=True)
    
  #sort out names
    # Normalize names function
    def normalize_name(name):
        name = name.lower().strip()
        name = re.sub(r'\b(\w+)( \1\b)+', r'\1', name)  # Remove repeated words
        name = re.sub(r'\s+', ' ', name)               # Normalize whitespace
        return name
    
    dfA['Name'] = dfA['Name'].astype(str).fillna('')
    dfA['Surname'] = dfA['Surname'].astype(str).fillna('')
    dfA['full_name'] = dfA['Name'].fillna('') + ' ' + dfA['Surname'].fillna('')
    dfA['full_name'] = dfA['full_name'].apply(normalize_name)
    
    # Fuzzy match to canonical list
    dfA['matched_name'] = dfA['full_name'].apply(
        lambda x: process.extractOne(x, Names, score_cutoff=80)[0]
              if process.extractOne(x, Names, score_cutoff=80)
              else x)
    
    survey = dfA
    
    df1 = pd.read_csv(folderin + 'lite/lite_2024.csv')
    df2 = pd.read_csv(folderin + 'lite/lite_2025.csv')
    
    dfs = [df1, df2]
    dfA = pd.concat(dfs, ignore_index=True)    
    
    dfA['Title'] = dfA['Title'].astype(str)
    dfA['full_name'] = dfA['Title'].apply(normalize_name)
        
    # Fuzzy match to canonical list
    dfA['matched_name'] = dfA['full_name'].apply(
        lambda x: process.extractOne(x, Names, score_cutoff=80)[0]
              if process.extractOne(x, Names, score_cutoff=80)
              else x)
    
    lite = dfA        
    
    df1 = pd.read_csv(folderin + 'count/count_2024.csv')
    df2 = pd.read_csv(folderin + 'count/count_2025.csv')
    
    dfs = [df1, df2]
    dfA = pd.concat(dfs, ignore_index=True)    
        
    dfA['FirstName'] = dfA['FirstName'].astype(str).fillna('')
    dfA['LastName'] = dfA['LastName'].astype(str).fillna('')
    dfA['full_name'] = dfA['FirstName'].fillna('') + ' ' + dfA['LastName'].fillna('')
    dfA['full_name'] = dfA['full_name'].apply(normalize_name)
    
    # Fuzzy match to canonical list
    dfA['matched_name'] = dfA['full_name'].apply(
        lambda x: process.extractOne(x, Names, score_cutoff=80)[0]
              if process.extractOne(x, Names, score_cutoff=80)
              else x)
    
    count = dfA    
    
  #get number of times each A-TEAMer has submitted
    all_matched_names = pd.concat([
    survey['matched_name'],
    lite['matched_name'],
    count['matched_name']])

    # Count occurrences of each name
    name_counts = all_matched_names.value_counts().reset_index()
    name_counts.columns = ['name', 'count']

    # Ensure all names are represented, even those with zero counts
    canonical_df = pd.DataFrame({'name': Names})
    final_counts = canonical_df.merge(name_counts, on='name', how='left').fillna(0)
    
    final_counts.to_csv(folderout + 'subs_per_person.csv')

  #get distance, items removed and surveyed per person 
    results_rows = []
    for name in Names:
        s_name = survey[survey['matched_name']==name]
        l_name = lite[lite['matched_name']==name]
        
        s_dist = s_name['Distance_km'].sum()
        count_lite = len(l_name.index)
        l_dist = count_lite * 6.77
        dists = [s_dist, l_dist]
        dist = sum(dists)
        
        s_items = s_name['TotItems'].sum() 
        cols = ['Handful', 'Pocketful', 'Bread Bag', 'Carrier Bag',
                      'Generic Bin Bag']
        multipliers = {'Handful': 6,'Pocketful': 10,'Bread Bag': 25,
              'Carrier Bag': 35,'Generic Bin Bag': 184.6}
        
        sum_items = []
        for c in cols:
            col_name = 'Quantity - ' + c
            cat = l_name[col_name].astype(str).str.strip().str.upper().eq('TRUE').sum()
            items = cat * multipliers[c]
            sum_items.append(items)
            
        multipledf = l_name[l_name['Quantity - Multiple Bin Bags'] == True]
        multipledf['How many bags?'].fillna(1, inplace = True)
        for index, i in multipledf.iterrows():
            bags = i['How many bags?']
            items = bags * 184.6
            sum_items.append(items)

        
        l_items = sum(sum_items)
        tot_items = l_items + s_items
  
        results_rows.append({
            'name': name,
            'distance_km': dist,
            'total_items': tot_items,
            'surveyed': s_items})
        
    results = pd.DataFrame(results_rows)
    results.to_csv(folderout + 'per_person.csv', index=False) 
    
  #get kms cleaned. removed and surveyed items, top 3 items, top 3 brands, %DRS
    dfA_s = survey[survey['matched_name'].isin(Names)]
    dfA_l = lite[lite['matched_name'].isin(Names)] 
    
    s_dist = dfA_s['Distance_km'].sum()
    count_lite = len(dfA_l.index)
    l_dist = count_lite * 6.77
    dists = [s_dist, l_dist]
    dist = sum(dists)

    s_items = dfA_s['TotItems'].sum()     
    
    items = ['Full Dog Poo Bags','Unused Dog Poo Bags','Toys (eg., tennis balls)','Other Pet Related Stuff',
          'Plastic Water Bottles','Plastic Soft Drink Bottles','Aluminium soft drink cans',
          'Plastic bottle, top','Glass soft drink bottles','Plastic energy drink bottles',
          'Aluminium energy drink can','Plastic energy gel sachet','Plastic energy gel end',
          'Aluminium alcoholic drink cans','Glass alcoholic bottles','Glass bottle tops',
          'Hot drinks cups','Hot drinks tops and stirrers','Drinks cups (eg., McDonalds drinks)',
          'Drinks tops (eg., McDonalds drinks)','Cartons','Plastic straws','Paper straws',
          'Plastic carrier bags','Plastic bin bags','Confectionary/sweet wrappers',
          'Wrapper "corners" / tear-offs','Other confectionary (eg., Lollipop Sticks)',
          'Crisps Packets','Used Chewing Gum',
          'Plastic fast food, takeaway and / or on the go food packaging, cups, cutlery etc',
          'Other fast food, takeaway and / or on the go food packaging, cups, cutlery (eg., cardboard)',
          'Disposable BBQs and / or BBQ related items','BBQs and / or BBQ related items',
          'Food on the go (eg.salad boxes)','Homemade lunch (eg., aluminium foil, cling film)',
          'Fruit peel & cores','Cigarette Butts','Smoking related','Disposable vapes',
          'Vaping / E-Cigarette Paraphernalia','Drugs related','Farming',
          'Salt/mineral lick buckets','Silage wrap','Forestry','Tree guards','Industrial',
          'Cable ties','Industrial plastic wrap','Toilet tissue','Face/ baby wipes',
          'Nappies','Single-Use Period products','Single-Use Covid Masks','Rubber/nitrile gloves',
          'Outdoor event (eg Festival)','Camping','Halloween & Fireworks','Seasonal (Christmas and/or Easter)',
          'Normal balloons','Helium balloons','MTB related (e.g. inner tubes, water bottles etc)',
          'Running','Roaming and other outdoor related (e.g. climbing, kayaking)',
          'Outdoor sports event related (e.g.race)','Textiles','Clothes & Footwear',
          'Plastic milk bottles','Plastic food containers','Cardboard food containers',
          'Cleaning products containers','Miscellaneous','Too small/dirty to ID',
          'Weird/Retro']

    results = []
    for i in items:
        col = 'Value ' + i
        if col in dfA_s.columns:
            total = dfA_s[col].dropna().astype(int).sum()
            if total > 0:
                results.append({'item': i, 'count': total})

    item_res = pd.DataFrame(results) 
    item_res.to_csv(folderout + 'items.csv') 

        
    brands = ['Lucozade','Coke','RedBull','Monster','Cadbury','McDonalds','Walkers','Mars','StellaArtois','Strongbow',
              'Costa','Budweiser','Haribo','SIS','Carling','Fosters','Thatchers','Pepsi','Nestle','Subway']
            
    results = []
    for b in brands:
        cols = [f'B1_{b}', f'B2_{b}', f'B3_{b}']
        count = 0

        for col in cols:
            if col in survey.columns:
                count += survey[col].notna().sum()

        results.append({'brand': b, 'count': count})

    brand_res = pd.DataFrame(results)

    brand_res.to_csv(folderout + 'brands.csv')
    
    DRS = ['Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
    'Value Aluminium soft drink cans', 'Value Glass soft drink bottles',
    'Value Plastic energy drink bottles','Value Aluminium energy drink can',
    'Value Aluminium alcoholic drink cans','Value Glass alcoholic bottles']

    results = []
    for col in DRS:
        if col in dfA_s.columns:
            total = dfA_s[col].dropna().sum()
            if total > 0:
                results.append(total)

    DRS_tot = sum(results)
    perc_DRS = (DRS_tot/s_items) * 100
    





def HQ_comparison(folderin,  fileout):
    """
    A function which takes TFT dats since A-TEAMers were seperated and calcuates
    some stats.
    
    Parameters
    ----------
    
    folderin: string
             path to input folder with yearly TFT data
             
    fileout: string
           path for file to save results in
    """   
    
    Names = ['heather friendship', 'dominic ferris', 'leigh rose', 'sarah-jane brown', 
             'rach coleman', 'rich breedon']
    
    
    df1 = pd.read_csv(folderin + 'survey/survey_2024.csv')
    df2 = pd.read_csv(folderin + 'survey/survey_2025.csv')
    
    dfs = [df1, df2]
    dfA = pd.concat(dfs, ignore_index=True)
    
    # Normalize names function
    def normalize_name(name):
        name = name.lower().strip()
        name = re.sub(r'\b(\w+)( \1\b)+', r'\1', name)  # Remove repeated words
        name = re.sub(r'\s+', ' ', name)               # Normalize whitespace
        return name
    
    dfA['Name'] = dfA['Name'].astype(str).fillna('')
    dfA['Surname'] = dfA['Surname'].astype(str).fillna('')
    dfA['full_name'] = dfA['Name'].fillna('') + ' ' + dfA['Surname'].fillna('')
    dfA['full_name'] = dfA['full_name'].apply(normalize_name)
    
    # Fuzzy match to canonical list
    dfA['matched_name'] = dfA['full_name'].apply(
        lambda x: process.extractOne(x, Names, score_cutoff=80)[0]
              if process.extractOne(x, Names, score_cutoff=80)
              else x)
    
    survey = dfA
    
    df1 = pd.read_csv(folderin + 'lite/lite_2024.csv')
    df2 = pd.read_csv(folderin + 'lite/lite_2025.csv')
    
    dfs = [df1, df2]
    dfA = pd.concat(dfs, ignore_index=True)    
    
    dfA['Title'] = dfA['Title'].astype(str)
    dfA['full_name'] = dfA['Title'].apply(normalize_name)
        
    # Fuzzy match to canonical list
    dfA['matched_name'] = dfA['full_name'].apply(
        lambda x: process.extractOne(x, Names, score_cutoff=80)[0]
              if process.extractOne(x, Names, score_cutoff=80)
              else x)
    
    lite = dfA        
    
    df1 = pd.read_csv(folderin + 'count/count_2024.csv')
    df2 = pd.read_csv(folderin + 'count/count_2025.csv')
    
    dfs = [df1, df2]
    dfA = pd.concat(dfs, ignore_index=True)    
        
    dfA['FirstName'] = dfA['FirstName'].astype(str).fillna('')
    dfA['LastName'] = dfA['LastName'].astype(str).fillna('')
    dfA['full_name'] = dfA['FirstName'].fillna('') + ' ' + dfA['LastName'].fillna('')
    dfA['full_name'] = dfA['full_name'].apply(normalize_name)
    
    # Fuzzy match to canonical list
    dfA['matched_name'] = dfA['full_name'].apply(
        lambda x: process.extractOne(x, Names, score_cutoff=80)[0]
              if process.extractOne(x, Names, score_cutoff=80)
              else x)
    
    count = dfA    
    
    all_matched_names = pd.concat([
    survey['matched_name'],
    lite['matched_name'],
    count['matched_name']])

    # Count occurrences of each name
    name_counts = all_matched_names.value_counts().reset_index()
    name_counts.columns = ['name', 'count']

    # Ensure all canonical names are represented, even those with zero counts
    canonical_df = pd.DataFrame({'name': Names})
    final_counts = canonical_df.merge(name_counts, on='name', how='left').fillna(0)    
    
def weekender_per_month(datain, dataout):
    """
    A function which takes full survey data and gets overall and yearly mean submissions per month
    
    Parameters
    ----------
    
    datain: string
             path to input csv file with all TFT survey data
            
    dataout: string
           path to save results
    """


    df = pd.read_csv(datain)
    
    Names = ['alistair hair', 'andy lund', 'chloe parker', 'dan jarvis', 
             'dom barry', 'ed roberts', 'emma johnson', 'gill houlsby', 
             'hannah lowther', 'hari milburn', 'harry wood', 'ian white', 
             'ian lean', 'jake rainford', 'james mackeddie', 'jane chisholm', 
             'jay schreiber', 'jo shwe', 'john bellis', 'kyle harvey', 
             'lauren munro-bennet', 'leon rosser', 'mario presi',
             'marv davies', 'matt kennelly', 'monet adams', 'neil hudson', 
             'nush lee', 'pete scullion', 'ram gurung', 'rosie holdsworth', 
             'ross lambie', 'sam piper', 'tom laws', 'will atkinson', 
             'victoria herbert', 'ollie cain', 'laurance ward', 'tim bowden', 
             'kristina vackova', 'helen wilson', 'lauren cattell']
   
    df2 = df.loc[df['matched_name']=='mark wilson']
    
    for name in Names:
        df2 = pd.concat([df2, df.loc[df['matched_name']== name]],ignore_index=True)
       
    
    #get list of years and months
    years = list(np.unique(df2['year']))
    months = list(np.unique(df2['month']))
    
    results = pd.DataFrame(columns = ['year','month','items','distance','time'])
    
    for year in years:
        #extract data for one year
        new=df2.loc[df2['year']==year]
        #extract data for each month
        for month in months:
            data=new.loc[new['month']==month]
            if data.empty:
                continue
            submissions = len(data.index)
            sup = data['TotItems'].sum()
            distance = data['Distance_km'].sum()
            time = data['Time_min'].sum()
        
            results = results.append({'year': year,'month': month,'items':sup,
                        'distance': distance,'time': time}, ignore_index=True)
            
            
    lite = pd.read_csv('/Users/heatherkay/Documents/TrashFreeTrails/Data/Misc_data_requests/A-TEAM_weekender/all_lite.csv')
    
   
    df3 = lite.loc[lite['matched_name']=='mark wilson']
    
    for name in Names:
        df3 = pd.concat([df3, lite.loc[lite['matched_name']== name]],ignore_index=True)
       
    
    results = pd.DataFrame(columns = ['year','month', 'TotItems', 'lite_distance', 'lite_time'])
    
    for year in years:
        #extract data for one year
        new=df3.loc[df3['year']==year]
        #extract data for each month
        for month in months:
            clean=new.loc[new['month']==month]
            if clean.empty:
                continue
            
            #handful * 6.2            
            df2 = clean[clean['Quantity - Handful'] == True]
            bag_total = []
  
            for index, i in df2.iterrows():
                bags = 1
                items = bags * 6
                bag_total.append(items) 

            #pocketful * 10
            df2 = clean[clean['Quantity - Pocketful'] == True]

            for index, i in df2.iterrows():
                bags = 1
                items = bags * 10
                bag_total.append(items) 
     
            #bread bag * 25
            df2 = clean[clean['Quantity - Bread Bag'] == True]

            for index, i in df2.iterrows():
                bags = 1
                items = bags * 25
                bag_total.append(items) 

            #carrier bag * 35
            df2 = clean[clean['Quantity - Carrier Bag'] == True]
            for index, i in df2.iterrows():
                bags = 1
                items = bags * 35
                bag_total.append(items) 
 
            #standard bin bag * 184.6
            df2 = clean[clean['Quantity - Generic Bin Bag'] == True]

 
            for index, i in df2.iterrows():
                bags = 1
                items = bags * 184.6
                bag_total.append(items) 

                
            #multiple standard bin bags * 184.6
            df2 = clean[clean['Quantity - Multiple Bin Bags'] == True]
            df2['How many bags?'].fillna(1, inplace = True)

            for index, i in df2.iterrows():
                bags = i['How many bags?']
                items = bags * 184.6
                bag_total.append(items) 
        
            tot_items = sum(bag_total)
            
            count_lite = len(clean.index)
            lite_km = count_lite * 6.77
            lite_time = count_lite * 1.64
            
            results = results.append({'year':year,'month':month, 
                            'TotItems': tot_items, 'lite_distance':lite_km,
                            'lite_time':lite_time}, ignore_index=True)  
            
    results.to_csv(folderout + 'res_lite.csv')  

    #plotting
    df = pd.read_csv('/Users/heatherkay/Documents/TrashFreeTrails/Data/Misc_data_requests/A-TEAM_weekender/res_survey.csv')

# 1. Create a new 'date' column using year and month
    df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))

# 2. Sort by date (optional but helpful)
    df = df.sort_values('date')

# 3. Plot_items
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['items'], marker='o')
    plt.plot(df['date'], df['lite_items'], marker='o', color = 'red')
    plt.plot(df['date'], df['tot_items'], marker='o', color = 'green')
    plt.xlabel('Date')
    plt.ylabel('Items')
    plt.title('Items over Time')
    plt.grid(True)
    plt.tight_layout()
    plt.show()   

# 3. Plot time
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['time'], marker='o')
    plt.plot(df['date'], df['lite_mins'], marker='o', color = 'red')
    plt.plot(df['date'], df['tot_time'], marker='o', color = 'green')
    plt.xlabel('Date')
    plt.ylabel('Time (minutes)')
    plt.title('Time spent trail cleaning')
    plt.grid(True)
    plt.tight_layout()
    plt.show()  

# 3. Plot distance
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['distance'], marker='o')
    plt.plot(df['date'], df['lite_distance'], marker='o', color = 'red')
    plt.plot(df['date'], df['tot_distance'], marker='o', color = 'green')
    plt.xlabel('Date')
    plt.ylabel('Distance')
    plt.title('Distance over Time')
    plt.grid(True)
    plt.tight_layout()
    plt.show()             
        


 