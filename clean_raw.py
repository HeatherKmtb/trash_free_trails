#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 14:37:41 2024

@author: heatherkay
"""

import pandas as pd

def survey_clean_data(TFTin, newin, monthout, TFTout):
    """
    A function which takes raw TFT survey data and prepares it for joining with
    existing data
    
    Parameters
    ----------
    
    TFTin: string
            path to input csv file with original TFT data
             
    newin: string
            path to input csv file with new data  
             
    monthout: string
            path to save the clean data just for the month you are processing
            
    TFTout: string
            path to save new file
    """
    #read csv file and remove unneeded columns
    df = pd.read_csv(newin)
    df = df.drop('Respondent ID', axis=1)
    df = df.drop('Collector ID', axis=1)
    df = df.drop('Start Date', axis=1)
    df = df.drop('End Date', axis=1)
    df = df.drop('IP Address', axis=1)
    df = df.drop('Email Address', axis=1)
    df = df.drop('First Name', axis=1)
    df = df.drop('Last Name', axis=1)
    df = df.drop('Custom Data 1', axis=1)

    #provide correct column names - could read from existing once wierd columns are sorted
    cols = ['Date_TrailClean','People','postcode','TrailName','ActivityBike',
        'ActivityRun','ActivityWalk','ActivityCombo','ActivityOther',
        'ZonesTrails','ZonesFootpaths','ZonesUnofficial','ZonesPump','ZonesUrban',
        'ZonesOtherTrails','ZonesAccess','ZonesCar','ZonesOther','MostZonesTrails',
        'MostZonesFootpaths','MostZonesUnofficial','MostZonesPump','MostZonesUrban',
        'MostZonesOtherTrails','MostZonesAccess','MostZonesCar','MostZonesOther',
        'Time_min','Distance_km','TotItems',
        #'AdjTotItems',
        'BinBags','Full Dog Poo Bags',
        'Unused Dog Poo Bags','Toys (eg., tennis balls)','Other Pet Related Stuff',
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
        'Weird/Retro','DL?','DM?','DN?','Perc_SU','RecycleY','RecycleN','RecyclePerc','MoreInfoY',
        'MoreInfoN','Value Full Dog Poo Bags','Value Unused Dog Poo Bags',
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
        'Value Weird/Retro','GR?','GS?','GT?','B1_Lucozade','B1_Coke','B1_RedBull','B1_Monster','B1_Cadbury',
        'B1_McDonalds','B1_Walkers','B1_Mars','B1_StellaArtois','B1_Strongbow','B1_Costa',
        'B1_Budweiser','B1_Haribo','B1_SIS','B1_Carling','B1_Fosters','B1_Thatchers',
        'B1_Pepsi','B1_Nestle','B1_Subway','B1_Other','B2_Lucozade','B2_Coke','B2_RedBull',
        'B2_Monster','B2_Cadbury','B2_McDonalds','B2_Walkers','B2_Mars','B2_StellaArtois',
        'B2_Strongbow','B2_Costa','B2_Budweiser','B2_Haribo','B2_SIS','B2_Carling',
        'B2_Fosters','B2_Thatchers','B2_Pepsi','B2_Nestle','B2_Subway','B2_Other',
        'B3_Lucozade','B3_Coke','B3_RedBull','B3_Monster','B3_Cadbury','B3_McDonalds',
        'B3_Walkers','B3_Mars','B3_StellaArtois','B3_Strongbow','B3_Costa','B3_Budweiser',
        'B3_Haribo','B3_SIS','B3_Carling','B3_Fosters','B3_Thatchers','B3_Pepsi',
        'B3_Nestle','B3_Subway','B3_Other','AnimalsY','AnimalsN','AnimalsInfo',
        'Connection_LitterFeel','Connection_LitterAmount','Connection_Action',
        'Connection_ConnectionY','Connection_ConnectionN','Connection_ConnectionSame',
        'Connection_Unsure','Connection_NewPeopleY','Connection_NewPeopleN',
        'Connection_NewPeopleUnsure','Connection_ActivityAfterY','Connection_ActivityAfterN',
        'Connection_ActivityAfterUnsure','Connection_TakePartAgainY','Connection_TakePartAgainN',
        'Connection_TakePartAgainUnsure','First time ','Volunteer','A-Team ',
        'Community Hub ','Name ','Surname','Email ','Phone','Receive email','Receive SMS ']


    #rename columns
    df.columns=cols
    #remove row with extra column names that aren't now needed
    df_clean = df.drop(index=0)

    #calculate AdjTotItems
    #start by converting data to floats (numbers) and defining for calcs
    df_clean[['TotItems', 'People', 'Time_min', 'Distance_km']] = df_clean[['TotItems', 'People', 'Time_min', 'Distance_km']].apply(pd.to_numeric)
    TotItems = df_clean['TotItems']#.astype(float)
    people = df_clean['People']#.astype(float)
    time = df_clean['Time_min']#.astype(float)
    km = df_clean['Distance_km']#.astype(float)
    #calculate ATI
    denominator = people*time*km
    AdjTotItems = TotItems/denominator 
    #Add ATI column to df in correct location
    df_clean.insert(loc=30, column = 'AdjTotItems', value=AdjTotItems)

    #filtering data
    #remove any rows with TotItems = 0
    df2 = df_clean[df_clean['TotItems']>0]
    #need distance = 0 change to ? here
    df2.loc[df2['Distance_km'] == 0, 'Distance_km'] = 1
    
    #remove any rows with error in AdjTotItems
    df3 = df2[df2['AdjTotItems'].notna()]
    
    #change data in presence(composition) data to TRUE
    change_cols = ['BinBags','Full Dog Poo Bags',
            'Unused Dog Poo Bags','Toys (eg., tennis balls)','Other Pet Related Stuff',
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

    for col in change_cols:
        df3.loc[df3[col] == col, col] = 'TRUE'
        
    #exporting the monthly data 
    df3.to_csv(monthout)
    
    #removing unexplained columns
    df3 = df3.drop('DL?', axis=1)
    df3 = df3.drop('DM?', axis=1)
    df3 = df3.drop('DN?', axis=1)
    df3 = df3.drop('GR?', axis=1)
    df3 = df3.drop('GS?', axis=1)
    df_toconcat = df3.drop('GT?', axis=1)        
        
    

    #read in 'old' data and add this cleaned data to top of that df
    orig_data = pd.read_csv(TFTin)   
    #cols2 = list(orig_data) # only needed if using column names from 'old' data or to check columns

    #check column headers - not needed unless df_final has more columns than orig_data
    #c = []
    #for val in cols:
    #    if val not in cols2:
    #        c.append(val)
    #        
    #d = []
    #for val in cols2:
    #    if val not in cols:
    #        d.append(val)        
    
    dfs = (df_toconcat, orig_data)
    
    df_final = pd.concat(dfs, ignore_index = True)
    
    df_final.to_csv(TFTout)
    
def count_clean_data(TFTin, newin, monthout, TFTout):
    """
    A function which takes raw TFT survey data and prepares it for joining with
    existing data
    
    Parameters
    ----------
    
    TFTin: string
            path to input csv file with original TFT data
             
    newin: string
            path to input csv file with new data  
             
    monthout: string
            path to save the clean data just for the month you are processing
            
    TFTout: string
            path to save new file
    """
    
    #awaiting answers to questions to understand purpose and where we want to go with this.
    
    #same for citizen science stuff, should probably collate all first?
    
def lite_clean_data(TFTin, TFTout):
    """
    A function which takes raw TFT lite data and prepares it for analyses
    
    Parameters
    ----------
    
    TFTin: string
            path to input csv file with original TFT data
             
    TFTout: string
            path to save new file
    """
    
    df = pd.read_csv(TFTin)
    
    #change date to year and month data to be able to extract monthly data 
    m = []
    y = []
    dates = df['Created Date'].values
    for d in dates:
        split = d.split('-')
        month = split[1]
        year = split[0]
        m.append(month)
        y.append(year)
        
    df['month'] = m
    df['year'] = y
    
    df.to_csv(TFTout)


    
