#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 11:59:31 2025

@author: heatherkay
"""

import os
import pandas as pd



folderin = '/Users/heatherkay/Documents/TrashFreeTrails/Data/Monthly_stats/'
folderout = '/Users/heatherkay/Documents/TrashFreeTrails/Data/Misc_data_requests/SoOT_2025/'

def grouping_all_brand_data(folderin, folderout):
    '''

    Parameters
    ----------
    folderin : TYPE
        DESCRIPTION.
    folderout : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    years = ['2019','2020','2021','2022','2023','2024', '2025']

    months = ['01','02','03','04','05','06','07','08','09','10','11','12']


    all_dfs = []

    for year in years:
        for month in months:
        # try version with "2020_" prefix first
            filepath = f"{folderin}{year}/output_10_25/2020_{month}_brands_all.csv"
        
            if not os.path.exists(filepath):
            # fall back to version without prefix
                filepath = f"{folderin}{year}/output_10_25/{month}_brands_all.csv"
        
            if os.path.exists(filepath):
                df = pd.read_csv(filepath)
                print(f"Loaded: {filepath}")
            
            # --- Clean brand names ---
                df['brand'] = (
                    df['brand']
                    .astype(str)           # make sure it’s string
                    .str.lower()           # lowercase
                    .str.replace(r'[\s\-]+', '', regex=True)  # remove spaces and dashes
                )
        
                all_dfs.append(df)
            else:
                print(f"Skipped missing: {filepath}")
                continue

    # --- Combine and aggregate ---
    if all_dfs:
        combined_df = pd.concat(all_dfs, ignore_index=True)
    
        # Group by brand, summing count and score
        summary_df = combined_df.groupby('brand', as_index=False)[['count', 'score']].sum()

    else:
        print("No files found.")
        
    summary_df.to_csv(folderout + 'brands.csv')    
    
    

def EPR_materials(TFTin, dataout):
    """
    A function which takes full survey data and gets overall and yearly mean submissions per month
    
    Parameters
    ----------
    
    TFTin: string
             path to folder with yearly TFT survey data
            
    dataout: string
           path to save results
    """
    survey = pd.read_csv(TFTin + 'survey/all_survey.csv')
    CSsurvey = pd.read_csv(TFTin + 'CS_survey/all_CS_survey.csv')


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
    
    
    # Apply conversion to both DataFrames individually
    for df in [survey, CSsurvey]:
        df[all_items] = df[all_items].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

    # Now they both have clean numeric columns
    combined = pd.concat([survey, CSsurvey], ignore_index=True)
    
    reported_items = combined[all_items].sum(axis=0).to_list()
    
    total_reported_items = sum(reported_items)

    plastic = [
            'Value Plastic bottle, top',
            'Value Plastic energy gel sachet','Value Plastic energy gel end', 
            'Value Plastic straws',
            'Value Plastic carrier bags','Value Plastic bin bags',
            'Value Plastic fast food, takeaway and / or on the go food packaging, cups, cutlery etc',
            'Value Confectionary/sweet wrappers',
            'Value Wrapper "corners" / tear-offs',
            'Value Crisps Packets','Value Plastic milk bottles',
            'Value Plastic food containers','Value Cleaning products containers']
    
    fibre_composite = ['Value Hot drinks cups', 'Value Hot drinks tops and stirrers',
                       'Value Drinks tops (eg., McDonalds drinks)',
                           'Value Food on the go (eg.salad boxes)']        
            
    aluminium = ['Value Glass bottle tops',
             'Value Disposable BBQs and / or BBQ related items','Value BBQs and / or BBQ related items']   

    glass = ['Value Glass soft drink bottles','Value Glass alcoholic bottles',]     
    
    cardboard = ['Value Cartons','Value Paper straws', 'Value Drinks cups (eg., McDonalds drinks)',
            'Value Other fast food, takeaway and / or on the go food packaging, cups, cutlery (eg., cardboard)',
            'Value Vaping / E-Cigarette Paraphernalia','Value Toilet tissue',
            'Value Cardboard food containers']
    
    wood = ['Value Other confectionary (eg., Lollipop Sticks)']
    
    other = ['Value Disposable vapes',
    'Value Salt/mineral lick buckets','Value Silage wrap',
    'Value Tree guards','Value Cable ties','Value Industrial plastic wrap',
    'Value Rubber/nitrile gloves','Value Face/ baby wipes',
    'Value Normal balloons','Value Helium balloons','Value Full Dog Poo Bags',
            'Value Unused Dog Poo Bags','Value Toys (eg., tennis balls)','Value Other Pet Related Stuff','Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
    'Value Aluminium soft drink cans', 'Value Plastic energy drink bottles',
    'Value Aluminium energy drink can',
    'Value Used Chewing Gum','Value Fruit peel & cores','Value Cigarette Butts','Value Smoking related',
    'Value Aluminium alcoholic drink cans','Value Drugs related','Value Farming',
             'Value Forestry','Value Industrial','Value Homemade lunch (eg., aluminium foil, cling film)',
             
             'Value Nappies','Value Single-Use Period products','Value Single-Use Covid Masks',
             'Value Outdoor event (eg Festival)','Value Camping','Value Halloween & Fireworks',
             'Value Seasonal (Christmas and/or Easter)',
             'Value MTB related (e.g. inner tubes, water bottles etc)',
             'Value Running','Value Roaming and other outdoor related (e.g. climbing, kayaking)',
             'Value Outdoor sports event related (e.g.race)','Value Textiles',
             'Value Clothes & Footwear',
             'Value Miscellaneous','Value Too small/dirty to ID','Value Weird/Retro']
    
    
    plastics = combined[plastic].sum(axis=0).to_list()
    fibres = combined[fibre_composite].sum(axis=0).to_list()
    ally = combined[aluminium].sum(axis=0).to_list() 
    glasses = combined[glass].sum(axis=0).to_list()
    card = combined[cardboard].sum(axis=0).to_list()       
    woods = combined[wood].sum(axis=0).to_list()
    others = combined[other].sum(axis=0).to_list()
        
    
    totpl = sum(plastics)
    totfi = sum(fibres)
    totgl = sum(glasses)
    total = sum(ally)    
    totca = sum(card)
    totwo = sum(woods)
    tototh = sum(others)

    df = pd.DataFrame({'type': ['all items', 'plastic','fibre_composite','glass','aluminium','card','wood','other'],
                           'quantity':[total_reported_items, totpl, totfi, totgl, total, totca, totwo, tototh]})
    
    df.to_csv(dataout, index=False)


    import matplotlib.pyplot as plt

  
    # Group by material and sum quantities
    grouped = df.groupby('type')['quantity'].sum().reset_index()

    # Exclude 'other'
    filtered = grouped[grouped['type'] != 'other']

    # Make pie chart
    plt.pie(
        filtered['quantity'],
        labels=filtered['type'],
        autopct='%1.1f%%',
        startangle=90)
    
    plt.title("EPR Material Distribution")
    plt.show()

def branded_EPR_materials(TFTin, dataout):
    """
    A function which takes full survey data and gets overall and yearly mean submissions per month
    
    Parameters
    ----------
    
    TFTin: string
             path to folder with yearly TFT survey data
            
    dataout: string
           path to save results
    """
    survey = pd.read_csv(TFTin + 'survey/all_survey.csv')
    CSsurvey = pd.read_csv(TFTin + 'CS_survey/all_CS_survey.csv')


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
    
    
    # Apply conversion to both DataFrames individually
    for df in [survey, CSsurvey]:
        df[all_items] = df[all_items].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

    # Now they both have clean numeric columns
    #combined = pd.concat([survey, CSsurvey], ignore_index=True)
    combined = pd.concat([survey, CSsurvey], ignore_index=True)
    
    # Summation works the same
    reported_items = combined[all_items].sum(axis=0).to_list()
    
    total_reported_items = sum(reported_items)
    

    plastic = ['Value Plastic energy gel sachet','Value Plastic energy gel end', 
               'Value Plastic carrier bags',
            'Value Plastic fast food, takeaway and / or on the go food packaging, cups, cutlery etc',
            'Value Confectionary/sweet wrappers',
            'Value Wrapper "corners" / tear-offs',
            'Value Crisps Packets','Value Plastic milk bottles',
            'Value Plastic food containers','Value Cleaning products containers']
    
    fibre_composite = ['Value Hot drinks cups','Value Food on the go (eg.salad boxes)']        
            
    aluminium = ['Value Glass bottle tops']   

    cardboard = ['Value Cartons', 'Value Drinks cups (eg., McDonalds drinks)',
            'Value Other fast food, takeaway and / or on the go food packaging, cups, cutlery (eg., cardboard)',
            'Value Cardboard food containers','Value Vaping / E-Cigarette Paraphernalia',
            'Value Smoking related', 'Value Cardboard food containers']
    
    #wood = ['Value Other confectionary (eg., Lollipop Sticks)']
    #for EPR items that aren't usually branded
    other = ['Value Plastic bottle, top', 'Value Plastic straws', 
             'Value Hot drinks tops and stirrers', 'Value Drinks tops (eg., McDonalds drinks)',
             'Value Glass bottle tops', 'Value Disposable BBQs and / or BBQ related items',
             'Value BBQs and / or BBQ related items', 'Value Paper straws','Value Other confectionary (eg., Lollipop Sticks)']
    
    
    plasticDRS = ['Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
            'Value Plastic bottle, top','Value Plastic energy drink bottles']
         
            
    aluminiumDRS = ['Value Aluminium soft drink cans','Value Aluminium energy drink can']   

    glassDRS = ['Value Glass soft drink bottles','Value Glass alcoholic bottles']     

    
    #wood = ['Value Other confectionary (eg., Lollipop Sticks)']
    
    #other = []
    

    
    plastics = combined[plastic].sum(axis=0).to_list()
    fibres = combined[fibre_composite].sum(axis=0).to_list()
    ally = combined[aluminium].sum(axis=0).to_list() 
    #glasses = combined[glass].sum(axis=0).to_list()
    card = combined[cardboard].sum(axis=0).to_list()       
    #woods = combined[wood].sum(axis=0).to_list()
    others = combined[other].sum(axis=0).to_list()
    plasticsDRS = combined[plasticDRS].sum(axis=0).to_list()
    allyDRS = combined[aluminiumDRS].sum(axis=0).to_list() 
    glassesDRS = combined[glassDRS].sum(axis=0).to_list()

        
    
    totpl = sum(plastics)
    totfi = sum(fibres)
    #totgl = sum(glasses)
    total = sum(ally)    
    totca = sum(card)
    #totwo = sum(woods)
    tototh = sum(others)
    totplDRS = sum(plasticsDRS)
 
    totglDRS = sum(glassesDRS)
    totalDRS = sum(allyDRS)    
   

    df = pd.DataFrame({'type': ['all items','plastic','fibre_composite','aluminium','card', 'other','plastic DRS','glass DRS', 'aluminium DRS'],
                           'quantity':[total_reported_items, totpl, totfi, total, totca, tototh, totplDRS, totglDRS, totalDRS]})   


    df.to_csv(dataout)
    
            