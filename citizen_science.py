#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 14:57:04 2025

@author: heatherkay
"""

import pandas as pd
from os import path
import glob
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def sort_data(TFTin, TFTout):
    """
    A function which takes citizen science TFT survey or count data and 
    splits it into location
    
    Parameters
    ----------
             
    TFTin: string
            path to folder with input csv file with data  
             
            
    TFTout: string
            path to folder to save files sorted by postcode
    """
    
    df = pd.read_csv(TFTin)
    
    hd, tl = path.split(TFTin)
    file_name = path.splitext(tl)[0]
    name_comp = file_name.split('_')
    dt = name_comp[2]
    
    df['postcode'] = df['postcode'].str.strip().str.upper()
    
    postcodes = df['postcode'].unique()   # unique so you don’t repeat work

    for p in postcodes:
        new_df = df[df['postcode'] == p]
        new_df.to_csv(TFTout + p + '_' + dt + '.csv', index=False)
        
def count_transect_graphs(folderin, folderout):
    """
    A function which takes citizen science TFT count data seperated by postcode and 
    analyses transect data, producing bar charts of the transects
    
    Parameters
    ----------
             
    folderin: string
            path to folder with input csv files with postcode data  
             
            
    TFTout: string
            path to folder to save graph files
    """    
    
    filelist = glob.glob(folderin + '*.csv')
    
    for file in filelist:
        df = pd.read_csv(file)
        
        hd, tl = path.split(file)
        file_name = path.splitext(tl)[0]
        
        transect_cols = [c for c in df.columns if c.startswith("Transect") and df[c].notna().any()]
        
        # Sort df by date
        df["Date_Count"] = pd.to_datetime(df["Date_Count"], format="%d/%m/%Y")
        df = df.sort_values("Date_Count")

        # Make a new figure for this file
        plt.figure(figsize=(8,6))
        
    
        #Convert to numpy for plotting
        values = df[transect_cols].values
        n_rows, n_cols = values.shape
        x = np.arange(len(transect_cols))
        width = 0.8 / n_rows

        for i, (date, vals) in enumerate(zip(df["Date_Count"], values)):
            plt.bar(x + i*width, vals, width=width, 
                label=date.strftime("%d-%b-%Y")) 

        plt.xticks(x + width*(n_rows-1)/2, transect_cols, rotation=45)
        plt.xlim(-0.5, len(transect_cols) - 0.5)
        plt.ylabel("Number of items")
        plt.title(f"Transect Values - {file_name}")
        plt.legend(title="Date", bbox_to_anchor=(1.05, 1), loc='upper left')

        plt.savefig(folderout + file_name + "_plot.png", dpi=300, bbox_inches="tight") 
        plt.close
    

def count_transect_stats_plots(folderin, folderout):
    """
    Given a dataframe with a 'Date_Count' column and Transect columns, 
    this function:
      1. Plots a correlation heatmap between dates
      2. Performs PCA on transect values and plots the first two PCs
      
    Parameters
    ----------
             
    folderin: string
            path to folder with input csv files with postcode data  
             
            
    folderout: string
            path to folder to save graph files  
    """
    
    filelist = glob.glob(folderin + '*.csv')
    
    for file in filelist:
        df = pd.read_csv(file)
        
        hd, tl = path.split(file)
        file_name = path.splitext(tl)[0]
        
        # Convert Date_Count to datetime if not already
        df["Date_Count"] = pd.to_datetime(df["Date_Count"], format="%d/%m/%Y")
    
        # Keep only transect columns that have at least one non-NaN value
        transect_cols = [c for c in df.columns if c.startswith("Transect") and df[c].notna().any()]
    
        df[transect_cols] = df[transect_cols].fillna(0)
    
        # --- Correlation Heatmap ---
        corr_matrix = df[transect_cols].T.corr()  # correlation between rows (dates)
        
        plt.figure(figsize=(10,8))
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm",
                xticklabels=df["Date_Count"].dt.strftime("%d-%b-%Y"),
                yticklabels=df["Date_Count"].dt.strftime("%d-%b-%Y"))
        plt.title("Correlation of Transect Patterns Between Dates")
        plt.tight_layout()
        
        plt.savefig(folderout + file_name + "_correlation_matrix.png", dpi=300, bbox_inches="tight") 
        plt.close
    
        # --- PCA ---
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(df[transect_cols])
    
        pca = PCA(n_components=2)
        pc = pca.fit_transform(scaled_data)
    
        plt.figure(figsize=(8,6))
        plt.scatter(pc[:,0], pc[:,1], c='blue')
    
        for i, date in enumerate(df["Date_Count"]):
            plt.text(pc[i,0]+0.02, pc[i,1]+0.02, date.strftime("%d-%b"))
    
        plt.xlabel("PC1")
        plt.ylabel("PC2")
        plt.title("PCA of Transect Patterns")
        plt.grid(True)
        plt.tight_layout()
        
        plt.savefig(folderout + file_name + "_PCA.png") 
        plt.close


def survey_date_comparison(TFTin, folderout):
    """
    A function which takes clean CS survey data and produces a barchart of 
    Total Items through time per location
    
    Parameters
    ----------
    
    TFTin: string
             path to input csv file with CS data
            
    folderout: string
           path for folder to save figures in
    """    

    df = pd.read_csv(TFTin)
    
    df['postcode'] = df['postcode'].str.strip().str.upper()
    
    postcodes = df['postcode'].unique() 

    for p in postcodes:
        dfp = df[df['postcode'] == p]

        # Sort df by date
        dfp["Date_TrailClean"] = pd.to_datetime(dfp["Date_TrailClean"], format="%d/%m/%Y")
        dfp = dfp.sort_values("Date_TrailClean")

        # Make a new figure for this file
        plt.figure(figsize=(10,6))
        
        plt.bar(dfp['Date_TrailClean'].dt.strftime("%Y-%m-%d"), dfp['TotItems'], color='skyblue')

        plt.title("Litter Collected Over Time")
        plt.xlabel("Survey Date")
        plt.ylabel("Total Items Collected")
        plt.xticks(rotation=45)  # rotate labels for readability
        plt.tight_layout()

        plt.savefig(folderout + p + "_plot.png", dpi=300, bbox_inches="tight") 
        plt.show()
        plt.close() 
        
def survey_types_comparison_per_season(TFTin, folderout):
    """
    A function which takes clean and filtered CS survey data and something TBC
    
    Parameters
    ----------
    
    TFTin: string
             path to input csv file with CS data
            
    folderout: string
           path for folder to save figures in
    """    

    df = pd.read_csv(TFTin)
    
    #matrials categories
    plastic = ['Value Full Dog Poo Bags',
            'Value Unused Dog Poo Bags','Value Toys (eg., tennis balls)','Value Other Pet Related Stuff',
            'Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
            'Value Plastic bottle, top','Value Plastic energy drink bottles',
            'Value Plastic energy gel sachet','Value Plastic energy gel end', 'Value Plastic straws',
            'Value Hot drinks tops and stirrers','Value Drinks tops (eg., McDonalds drinks)',
            'Value Plastic carrier bags','Value Plastic bin bags',
            'Value Plastic fast food, takeaway and / or on the go food packaging, cups, cutlery etc',
            'Value Confectionary/sweet wrappers',
            'Value Wrapper "corners" / tear-offs','Value Other confectionary (eg., Lollipop Sticks)',
            'Value Crisps Packets','Value Disposable vapes','Value Salt/mineral lick buckets','Value Silage wrap',
            'Value Tree guards','Value Cable ties','Value Industrial plastic wrap','Value Rubber/nitrile gloves',
            'Value Normal balloons','Value Helium balloons','Value Plastic milk bottles',
            'Value Plastic food containers','Value Cleaning products containers']
            
            
    potentially_plastic = ['Value Hot drinks cups','Value Drinks cups (eg., McDonalds drinks)',
                           'Value Food on the go (eg.salad boxes)']        
            
    metal = ['Value Aluminium soft drink cans','Value Aluminium energy drink can',
             'Value Aluminium alcoholic drink cans','Value Glass bottle tops',
             'Value Disposable BBQs and / or BBQ related items','Value BBQs and / or BBQ related items',]   

    glass = ['Value Glass soft drink bottles','Value Glass alcoholic bottles']     
    
    cardboard_paper_wood = ['Value Cartons','Value Paper straws',
            'Value Other fast food, takeaway and / or on the go food packaging, cups, cutlery (eg., cardboard)',
            'Value Vaping / E-Cigarette Paraphernalia','Value Toilet tissue','Value Cardboard food containers',]
    
    other = ['Value Used Chewing Gum','Value Fruit peel & cores','Value Cigarette Butts','Value Smoking related',
             'Value Drugs related','Value Farming',
             'Value Forestry','Value Industrial','Value Homemade lunch (eg., aluminium foil, cling film)',
             'Value Face/ baby wipes',
             'Value Nappies','Value Single-Use Period products','Value Single-Use Covid Masks',
             'Value Outdoor event (eg Festival)','Value Camping','Value Halloween & Fireworks','Value Seasonal (Christmas and/or Easter)',
             'Value MTB related (e.g. inner tubes, water bottles etc)',
             'Value Running','Value Roaming and other outdoor related (e.g. climbing, kayaking)',
             'Value Outdoor sports event related (e.g.race)','Value Textiles','Value Clothes & Footwear',
             'Value Miscellaneous','Value Too small/dirty to ID','Value Weird/Retro']
    
    #Uses categories
    pet_stuff = ['Value Full Dog Poo Bags','Value Unused Dog Poo Bags',
    'Value Toys (eg., tennis balls)','Value Other Pet Related Stuff']
    
    drinks_containers = ['Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
    'Value Aluminium soft drink cans','Value Plastic bottle, top','Value Glass soft drink bottles',
    'Value Plastic energy drink bottles','Value Aluminium energy drink can',
    'Value Plastic energy gel sachet','Value Plastic energy gel end','Value Aluminium alcoholic drink cans',
    'Value Glass alcoholic bottles','Value Glass bottle tops','Value Hot drinks cups',
    'Value Hot drinks tops and stirrers','Value Drinks cups (eg., McDonalds drinks)',
    'Value Drinks tops (eg., McDonalds drinks)','Value Cartons','Value Plastic straws',
    'Value Paper straws']
    
    snack = ['Value Plastic carrier bags','Value Plastic bin bags',
    'Value Confectionary/sweet wrappers','Value Wrapper "corners" / tear-offs',
    'Value Other confectionary (eg., Lollipop Sticks)','Value Crisps Packets',
    'Value Used Chewing Gum','Value Plastic fast food, takeaway and / or on the go food packaging, cups, cutlery etc',
    'Value Other fast food, takeaway and / or on the go food packaging, cups, cutlery (eg., cardboard)',
    'Value Disposable BBQs and / or BBQ related items','Value BBQs and / or BBQ related items',
    'Value Food on the go (eg.salad boxes)','Value Homemade lunch (eg., aluminium foil, cling film)',
    'Value Fruit peel & cores']
    
    smoking = ['Value Cigarette Butts','Value Smoking related',
    'Value Disposable vapes','Value Vaping / E-Cigarette Paraphernalia','Value Drugs related']
    
    agro_ind = ['Value Farming','Value Salt/mineral lick buckets','Value Silage wrap',
    'Value Forestry','Value Tree guards','Value Industrial','Value Cable ties',
    'Value Industrial plastic wrap']
    
    hygiene = ['Value Toilet tissue','Value Face/ baby wipes',
    'Value Nappies','Value Single-Use Period products','Value Single-Use Covid Masks',
    'Value Rubber/nitrile gloves']
    
    recreation = ['Value Outdoor event (eg Festival)','Value Camping',
    'Value Halloween & Fireworks','Value Seasonal (Christmas and/or Easter)',
    'Value Normal balloons','Value Helium balloons']
    
    sports = ['Value MTB related (e.g. inner tubes, water bottles etc)',
    'Value Running','Value Roaming and other outdoor related (e.g. climbing, kayaking)',
    'Value Outdoor sports event related (e.g.race)']
    
    textiles = ['Value Textiles','Value Clothes & Footwear']
    
    house = ['Value Plastic milk bottles','Value Plastic food containers','Value Cardboard food containers',
    'Value Cleaning products containers']
    
    misc = ['Value Miscellaneous','Value Too small/dirty to ID',
    'Value Weird/Retro']
    
    material_groups = {"Glass": glass, "Plastic": plastic, "Metal": metal,
             "Cardboard": cardboard_paper_wood, "Other": other}     
    
    for material, cols in material_groups.items():
            df[f"Total_m_{material}"] = df[cols].sum(axis=1)
        
    use_groups = {'Pet': pet_stuff, 'DRS': drinks_containers, 'Snacks': snack, 
                      'Smoking': smoking, 'Agro-ing': agro_ind, 'Hygiene': hygiene, 
                      'Recreation': recreation, 'Sports': sports, 'Textiles': textiles, 
                      'Household': house, 'Miscellaneous': misc}
        
    for use, cols in use_groups.items():
            df[f"Total_u_{use}"] = df[cols].sum(axis=1)   
    
    #df['postcode'] = df['postcode'].str.strip().str.upper()
    
    season = df['Season'].unique() 

    for s in season:
        dfs = df[df['Season'] == s]

        # Make a new figure for this file
        plt.figure(figsize=(10,6))
        
        material_cols = [c for c in dfs.columns if c.startswith("Total_m_") and dfs[c].notna().any()]
        material_legend = []
        for m in material_cols:
            name_comp = m.split('_')
            mat = name_comp[2]
            material_legend.append(mat)
        
        # Make a new figure for this file
        plt.figure(figsize=(10,6))
    
        #Convert to numpy for plotting
        values = dfs[material_cols].values
        n_rows, n_cols = values.shape
        x = np.arange(len(material_cols))
        width = 0.8 / n_rows

        for i, (loc, vals) in enumerate(zip(dfs["Location"], values)):
            plt.bar(x + i*width, vals, width=width,label=loc) 

        plt.xticks(x + width*(n_rows-1)/2, material_legend, rotation=45)
        #plt.xlim(-0.5, len(material_cols) - 0.5)
        plt.ylabel("Number of items")
        plt.title(f"Values per location in {s}")
        plt.legend(title="Location", bbox_to_anchor=(1.05, 1), loc='upper left')

        plt.savefig(folderout + s + "_materials_plot.png", dpi=300, bbox_inches="tight") 
        plt.close
        
        use_cols = [c for c in dfs.columns if c.startswith("Total_u_") and dfs[c].notna().any()]
        use_legend = []
        for u in use_cols:
            name_comp = u.split('_')
            use = name_comp[2]
            use_legend.append(use)
        # Make a new figure for this file
        plt.figure(figsize=(8,6))
    
        #Convert to numpy for plotting
        values = dfs[use_cols].values
        n_rows, n_cols = values.shape
        x = np.arange(len(use_cols))
        width = 0.8 / n_rows

        for i, (loc, vals) in enumerate(zip(dfs["Location"], values)):
            plt.bar(x + i*width, vals, width=width,label=loc) 

        plt.xticks(x + width*(n_rows-1)/2, use_legend, rotation=45)
        #plt.xlim(-0.5, len(use_cols) - 0.5)
        plt.ylabel("Number of items")
        plt.title(f"Values per location in {s}")
        plt.legend(title="Location", bbox_to_anchor=(1.05, 1), loc='upper left')

        plt.savefig(folderout + s + "_use_plot.png", dpi=300, bbox_inches="tight") 
        plt.close
        
        
        
        #percentages
        # Make a new figure for this file
        plt.figure(figsize=(10,6))
    
        #Convert to numpy for plotting
        values = dfs[material_cols].div(dfs["TotItems"], axis=0).fillna(0).values * 100
        n_rows, n_cols = values.shape
        x = np.arange(len(material_cols))
        width = 0.8 / n_rows

        for i, (loc, vals) in enumerate(zip(dfs["Location"], values)):
            plt.bar(x + i*width, vals, width=width,label=loc) 

        plt.xticks(x + width*(n_rows-1)/2, material_legend, rotation=45)
        #plt.xlim(-0.5, len(material_cols) - 0.5)
        plt.ylabel("Number of items as % of Total Items")
        plt.title(f"Values per location in {s} as a %")
        plt.legend(title="Location", bbox_to_anchor=(1.05, 1), loc='upper left')

        plt.savefig(folderout + s + "_percentage_materials_plot.png", dpi=300, bbox_inches="tight") 
        plt.close
        
        use_cols = [c for c in dfs.columns if c.startswith("Total_u_") and dfs[c].notna().any()]
        use_legend = []
        for u in use_cols:
            name_comp = u.split('_')
            use = name_comp[2]
            use_legend.append(use)
        # Make a new figure for this file
        plt.figure(figsize=(8,6))
    
        #Convert to numpy for plotting
        values = dfs[use_cols].div(dfs["TotItems"], axis=0).fillna(0).values * 100
        n_rows, n_cols = values.shape
        x = np.arange(len(use_cols))
        width = 0.8 / n_rows

        for i, (loc, vals) in enumerate(zip(dfs["Location"], values)):
            plt.bar(x + i*width, vals, width=width,label=loc) 

        plt.xticks(x + width*(n_rows-1)/2, use_legend, rotation=45)
        #plt.xlim(-0.5, len(use_cols) - 0.5)
        plt.ylabel("Number of items as % of Total Items")
        plt.title(f"Values per location in {s} as a %")
        plt.legend(title="Location", bbox_to_anchor=(1.05, 1), loc='upper left')

        plt.savefig(folderout + s + "_percentage_use_plot.png", dpi=300, bbox_inches="tight") 
        plt.close






















def CS_standard_stats(folderin, folderout):
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
           
            
               