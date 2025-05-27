t#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 14:37:41 2024

@author: heatherkay
"""

import pandas as pd
import glob


def survey_clean_data(TFTin, TFTout):
    """
    A function which takes new raw TFT survey data and prepares it for analyses
    
    Parameters
    ----------
             
    TFTin: string
            path to folder with input csv file with new data  
             
            
    TFTout: string
            path to folder to save file with clean data
    """
    #read csv file
    df = pd.read_csv(TFTin + 'survey.csv' )
    
    #remove unneeded columns
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
        'TypeMrkdTrails','TypeRoW','TypeUnofficial','TypePump','TypeUrban',
        'TypeOtherTrails','TypeAccess','TypeCar','TypeOther','MostTypeTrails',
        'MostTypeFootpaths','MostTypeUnofficial','MostTypePump','MostTypeUrban',
        'MostTypeOtherTrails','MostTypeAccess','MostTypeCar','MostTypeOther',
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
        'Connection_TakePartAgainUnsure','First time','Volunteer','A-Team',
        'Community Hub','Name','Surname','Email','Phone','Receive email','Receive SMS']


    #rename columns
    df.columns=cols
    #remove row with extra column names that aren't now needed
    df_clean = df.drop(index=0)
    
    #remove other uneeded columns
    df_clean = df_clean.drop('DL?', axis=1)
    df_clean = df_clean.drop('DM?', axis=1)
    df_clean = df_clean.drop('DN?', axis=1)
    df_clean = df_clean.drop('GR?', axis=1)
    df_clean = df_clean.drop('GS?', axis=1)
    df_clean = df_clean.drop('GT?', axis=1)
    
    df_clean = df_clean[~df_clean['TrailName'].str.contains(r'\btest\b', case=False, na=False)]
    
    #Save file to add to raw dataset
    #df_clean.to_csv(rawout)
    
    #need distance = 0 changed to ? here - use an average here!!!!
    df_clean.loc[df_clean['Distance_km'] == 0, 'Distance_km'] = 4.83

    #calculate AdjTotItems
    #start by converting data to floats (numbers) and defining for calcs
    df_clean[['TotItems', 'People', 'Time_min', 'Distance_km']] = df_clean[['TotItems', 'People', 'Time_min', 'Distance_km']].apply(pd.to_numeric)
    TotItems = df_clean['TotItems']#.astype(float)
    people = df_clean['People']#.astype(float)
    time = df_clean['Time_min']#.astype(float)
    km = df_clean['Distance_km']#.astype(float)
    #calculate ATI
    denominator = (people*time)*km
    AdjTotItems = TotItems/denominator 
    #Add ATI column to df in correct location
    df_clean.insert(loc=30, column = 'AdjTotItems', value=AdjTotItems)
   

    #filtering data
    #remove any rows with TotItems = 0
    #df2 = df_clean[df_clean['TotItems']>0]
    
    #remove any rows with error in AdjTotItems
    #df3 = df2[df2['AdjTotItems'].notna()]
    
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

    df3 = df_clean
    
    for col in change_cols:
        df3.loc[df3[col] == col, col] = 'TRUE'
        
    
    #prepare columns with year and month data to be able to extract monthly or yearly data 
    m = []
    y = []
    dates = df3['Date_TrailClean'].values
    for d in dates:
        split = d.split('/')
        month = split[1]
        year = split[2]
        if len(month) == 1:
            new = '0' + month
            m.append(new)
            y.append(year)
        else:
            m.append(month)
            y.append(year)
        
    df3['month'] = m
    df3['year'] = y
                  
    #exporting the cleaned monthly data 
    df3.to_csv(TFTout + 'survey.csv', index=False)
    
    
def count_clean_data(TFTin, TFTout):
    """
    A function which takes raw TFT count data and prepares it for analyses
    
    Parameters
    ----------
             
    TFTin: string
            path to folder with input csv file with new data  
             
            
    TFTout: string
            path to folder to save file with clean data
    """        
    
    #awaiting answers to questions to understand purpose and where we want to go with this.
    
    #same for citizen science stuff, should probably collate all first?
    
    df = pd.read_csv(TFTin + 'count.csv')
    
    #remove unneeded columns
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
    cols = ['Date_Count','People','postcode', 'Komoot_link','TrailName','ActivityBike',
        'ActivityRun','ActivityWalk','ActivityCombo','ActivityOther','TFTmethods_Y',
        'TFTmethods_N','TFTmethods_NotSure','Total_distance(m)','100m_transect',
        '1km_transect','other_transect','TypeMrkdTrails','TypeRoW','TypeUnofficial',
        'TypePump','TypeUrban','TypeOtherTrails','TypeAccess','TypeCar','TypeBeach',
        'TypeRiverbank','TypeOther','ZonesCarpark','ZonesVisitorInfrastructure',
        'ZonesTrailMaps','ZonesTrailhead','ZonesDogPoo','ZonesShakedown',
        'ZonesTopClimb','ZonesView','ZonesPicnic','ZonesRoadCrossing',
        'ZonesSwimspot','ZonesBottomDescent','ZonesJumps','ZonesPause',
        'ZonesAlmostHome','ZonesLake','ZonesRiver','ZonesBeach','ZonesSanddunes',
        'MostZonesCarpark','MostZonesVisitorInfrastructure','MostZonesTrailMaps',
        'MostZonesTrailhead','MostZonesDogPoo','MostZonesShakedown','MostZonesTopClimb',
        'MostZonesView','MostZonesPicnic','MostZonesRoadCrossing','MostZonesSwimspot',
        'MostZonesBottomDescent','MostZonesJumps','MostZonesPause','MostZonesAlmostHome',
        'MostZonesLake','MostZonesRiver','MostZonesBeach','MostZonesSanddunes','TotItems',
        'Transect1','Transect2','Transect3','Transect4','Transect5','Transect6',
        'Transect7','Transect8','Transect9','Transect10','Connection_SUP_amount',
        'Connection_Feel','Connection_ConnectionY','Connection_ConnectionN',
        'Connection_ConnectionSame','Connection_Unsure',
        'Count_UnnaturalY','Count_UnnaturalN',
        'Count_UnnaturalNotSure','Participate_CleanY','Participate_CleanN',
        'Participate_CleanNotSure','First_time','Volunteer','A-Team','Community Hub',
        'FirstName','LastName','Email','phone','email','SMS']
    
    #rename columns
    df.columns=cols
    #remove row with extra column names that aren't now needed
    df3 = df.drop(index=0)
    
    df3 = df3[~df3['TrailName'].str.contains(r'\btest\b', case=False, na=False)]
  
    #prepare columns with year and month data to be able to extract monthly or yearly data 
    m = []
    y = []
    dates = df3['Date_Count'].values
    for d in dates:
        split = d.split('/')
        month = split[1]
        year = split[2]
        if len(month) == 1:
            new = '0' + month
            m.append(new)
            y.append(year)
        else:
            m.append(month)
            y.append(year)
        
    df3['month'] = m
    df3['year'] = y
            
    df3.to_csv(TFTout + 'count.csv', index=False)
    
    
    
def lite_clean_data(TFTin, TFTout):
    """
    A function which takes raw TFT lite data and prepares it for analyses,
    producing 2 .csvs one with clean TFT lite data and one with number of
    items and number of bags reported from our averages data
    
    Parameters
    ----------
    
    TFTin: string
            path to folder with input csv file with new data  
             
            
    TFTout: string
            path to folder to save files with clean data
    """
    
    df = pd.read_csv(TFTin + 'lite.csv')
    
    #change date to year and month data to be able to extract monthly data 
    m = []
    y = []
    dates = df['Created Date'].values
    for d in dates:
        split = d.split('-')
        mth = split[1]
        yr = split[0]
        m.append(mth)
        y.append(yr)
        
    df['month'] = m
    df['year'] = y
        
    #remove rows with too many TRUES...
    trash_cols = ['Quantity - Handful', 'Quantity - Pocketful', 'Quantity - Bread Bag',
                  'Quantity - Carrier Bag', 'Quantity - Generic Bin Bag',
                  'Quantity - Multiple Bin Bags']
    
    rows_to_drop = []

    for index, row in df.iterrows():
        true_counts = row[trash_cols].sum()
        if true_counts != 1:
            rows_to_drop.append(index)

    df.drop(index=rows_to_drop, inplace=True)
    
    df.to_csv(TFTout + 'lite.csv', index=False)
    #now extract TRUE data for each bafg size and calcualte total items per bag type
    results = pd.DataFrame(columns = ['bag', 'TotItems', 'no. of bags'])
    
    clean = df
    #handful * 6.2            
    df2 = clean[clean['Quantity - Handful'] == True]
    bag_total = []
    nobags = []
    bag = 'handful'
    for index, i in df2.iterrows():
        bags = 1
        items = bags * 6
        bag_total.append(items) 
        nobags.append(bags)
        
    tot_items = sum(bag_total)
    tot_bags = sum(nobags)
    results = results.append({'bag': bag, 'TotItems': tot_items, 'no. of bags': tot_bags}, ignore_index=True)  
  
    #pocketful * 10
    df2 = clean[clean['Quantity - Pocketful'] == True]
    bag = 'pocketful'
    nobags = []
    bag_total = []
    for index, i in df2.iterrows():
        bags = 1
        items = bags * 10
        bag_total.append(items) 
        nobags.append(bags)
 
    tot_items = sum(bag_total)
    tot_bags = sum(nobags)
    results = results.append({'bag': bag, 'TotItems': tot_items, 'no. of bags': tot_bags}, ignore_index=True)  
     
    #bread bag * 25
    df2 = clean[clean['Quantity - Bread Bag'] == True]
    bag = 'breadbag'
    nobags = []
    bag_total = []
    for index, i in df2.iterrows():
        bags = 1
        items = bags * 25
        bag_total.append(items) 
        nobags.append(bags)
        
    tot_items = sum(bag_total)
    tot_bags = sum(nobags)
    results = results.append({'bag': bag, 'TotItems': tot_items, 'no. of bags': tot_bags}, ignore_index=True)  
     
    #carrier bag * 35
    df2 = clean[clean['Quantity - Carrier Bag'] == True]
    bag = 'carrierbag'
    nobags = []
    bag_total = []
    for index, i in df2.iterrows():
        bags = 1
        items = bags * 35
        bag_total.append(items) 
        nobags.append(bags)
        
    tot_items = sum(bag_total)
    tot_bags = sum(nobags)
    results = results.append({'bag': bag, 'TotItems': tot_items, 'no. of bags': tot_bags}, ignore_index=True)  

    #standard bin bag * 184.6
    df2 = clean[clean['Quantity - Generic Bin Bag'] == True]
    bag = 'binbag'
    nobags = []
    bag_total = []
    for index, i in df2.iterrows():
        bags = 1
        items = bags * 184.6
        bag_total.append(items) 
        nobags.append(bags)
        
    tot_items = sum(bag_total)
    tot_bags = sum(nobags)
    results = results.append({'bag': bag, 'TotItems': tot_items, 'no. of bags': tot_bags}, ignore_index=True)  
        
        
    #multiple standard bin bags * 184.6
    df2 = clean[clean['Quantity - Multiple Bin Bags'] == True]
    df2['How many bags?'].fillna(1)
    bag = 'multiplebinbags'
    nobags = []
    bag_total = []
    for index, i in df2.iterrows():
        bags = i['How many bags?']
        items = bags * 184.6
        bag_total.append(items) 
        nobags.append(bags)        
        
    tot_items = sum(bag_total)
    tot_bags = sum(nobags)
    results = results.append({'bag': bag, 'TotItems': tot_items, 'no. of bags': tot_bags}, ignore_index=True)  
    results.to_csv(TFTout + 'bag_res_lite.csv', index=False)
    
    
def citizen_science_survey_clean_data(TFTin, TFTout):
    """
    A function which takes raw TFT Citizen Science raw survey data and prepares it for analyses
    
    Parameters
    ----------
             
    TFTin: string
            path to folder with input csv file with new data  
             
            
    TFTout: string
            path to folder to save file with clean data
    """

    #read csv file
    df = pd.read_csv(TFTin + 'CSsurvey.csv')
    
    #remove unneeded columns
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
        'ActivityRun','ActivityWalk','ActivityCombo','ActivityOther', 'FollowMethodologyY',
        'FollowMethodologyN','FollowMethodologyNotSure','NavDevY','NavDevN','NavDevLink',
        'Time_hours','TotItems','Area_km2', 'TypeMrkdTrails', 'TypeRoW', 'TypeMtnSummitTrail',
        'TypeUpliftAccessed','TypeUnofficial','TypePump','TypeUrban',
        'TypeOtherTrails','TypeAccess','TypeCar',
        'TypeAquatic','TypeOther','MostTr_Marked', 'MostTr_PublicRoW', 'MostTr_MtnSummit',
        'MostTr_UplistAccessed','MostTr_Unofficial','MostTr_PumpTracks','MostTr_UrbanGreen',
        'MostTr_OtherTrailsandGreenSpaces','MostTr_AccessRoute','MostTr_Carpark',
        'MostTr_Aquatic','MostTr_Other','Zone_Carpark','Zone_VisitorInfrastructure','Zone_TrailMaps','Zone_Trailhead',
        'Zone_DogPoo','Zone_Rattly','Zone_TrailBottom','Zone_ClimbTop','Zone_Viewpoint',
        'Zone_Jumps','Zone_Uplift(Un)Load','Zone_ViewPause','Zone_Picnic','Zone_Puncture',
        'Zone_FinalFuelUp','Zone_Summit','Zone_RoadCrossing','Zone_Swim','Zone_Camp',
        'Zone_Toilet','Zone_Skilift','Zone_Other', 'MostZonesCarpark','MostZonesVisitor','MostZonesMap',
        'MostZonesTrailhead','MostZonesDogPoo','MostZonesRattly','MostZonesTrailBottom',
        'MostZonesClimbTop','MostZonesViewpoint','MostZonesJumps','MostZonesUplift',
        'MostZonesViewPausePoint','MostZonesPicnic','MostZonesPuncture',
        'MostZonesFinalFuelUp','MostZonesToilet','MostZonesSummit','MostZonesRoadCrossing','MostZonesSwim',
        'MostZonesCamp','MostZonesSkilift','MostZonesOtherText','MostZonesOther',
        'Perc_SU','RecycleY','RecycleN','RecyclePerc',
        'Value Full Dog Poo Bags','Value Unused Dog Poo Bags',
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
        'Value Nappies','Value Single-Use Period products','Value Rubber/nitrile gloves',
        'Value Single-Use Covid Masks','Value Outdoor event (eg Festival)','Value Camping',
        'Value Halloween & Fireworks','Value Seasonal (Christmas and/or Easter)',
        'Value Normal balloons','Value Helium balloons','Value MTB related (e.g. inner tubes, water bottles etc)',
        'Value Running','Value Roaming and other outdoor related (e.g. climbing, kayaking)',
        'Value Outdoor sports event related (e.g.race)','Value Textiles','Value Clothes & Footwear',
        'Value Plastic milk bottles','Value Glass milk bottles','Value Plastic food containers',
        'Value Cardboard food containers',
        'Value Cleaning products containers','Value Miscellaneous','Value Too small/dirty to ID',
        'Value Weird/Retro','Other_Specify','B1_Lucozade','B1_Coke','B1_RedBull','B1_Monster','B1_Cadbury',
        'B1_McDonalds','B1_Walkers','B1_Mars','B1_StellaArtois','B1_Strongbow','B1_Costa',
        'B1_Budweiser','B1_Haribo','B1_SIS','B1_Carling','B1_Fosters','B1_Thatchers',
        'B1_Pepsi','B1_Nestle','B1_Subway','B1_Other','B2_Lucozade','B2_Coke','B2_RedBull',
        'B2_Monster','B2_Cadbury','B2_McDonalds','B2_Walkers','B2_Mars','B2_StellaArtois',
        'B2_Strongbow','B2_Costa','B2_Budweiser','B2_Haribo','B2_SIS','B2_Carling',
        'B2_Fosters','B2_Thatchers','B2_Pepsi','B2_Nestle','B2_Subway','B2_Other',
        'B3_Lucozade','B3_Coke','B3_RedBull','B3_Monster','B3_Cadbury','B3_McDonalds',
        'B3_Walkers','B3_Mars','B3_StellaArtois','B3_Strongbow','B3_Costa','B3_Budweiser',
        'B3_Haribo','B3_SIS','B3_Carling','B3_Fosters','B3_Thatchers','B3_Pepsi',
        'B3_Nestle','B3_Subway','B3_Other','AnimalsY','AnimalsN','AnimalsNotChecked','AnimalsInfo',
        'Connection_LitterFeel','Connection_LitterAmount','Connection_Action',
        'Connection_ConnectionY','Connection_ConnectionN','Connection_ConnectionSame',
        'Connection_Unsure','Connection_NewPeopleY','Connection_NewPeopleN',
        'Connection_NewPeopleAlone','Connection_NewPeopleKnewAlready','Connection_ActivityAfterY',
        'Connection_ActivityAfterN','Connection_TakePartBeforeY','Connection_TakePartBeforeN',
        'Connection_TakePartBeforeUnsure','Connection_TakePartBeforeHowMany']

    #rename columns
    df.columns=cols
    #remove row with extra column names that aren't now needed
    df3 = df.drop(index=0)
    
    #prepare columns with year and month data to be able to extract monthly or yearly data 
    m = []
    y = []
    dates = df3['Date_TrailClean'].values
    for d in dates:
        split = d.split('/')
        month = split[1]
        year = split[2]
        if len(month) == 1:
            new = '0' + month
            m.append(new)
            y.append(year)
        else:
            m.append(month)
            y.append(year)
        
    df3['month'] = m
    df3['year'] = y
                  
    #exporting the cleaned monthly data 
    df3.to_csv(TFTout + 'CS_survey.csv', index=False)
    
   
    
def citizen_science_count_clean_data(TFTin, TFTout):
    """
    A function which takes TFT citizen science raw count data and prepares it for analyses
    
    Parameters
    ----------
             
    TFTin: string
            path to folder with input csv file with new data  
             
            
    TFTout: string
            path to folder to save file with clean data
    """

    #read csv file
    df = pd.read_csv(TFTin + 'CScount.csv')
    
    #remove unneeded columns
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
    cols = ['Date_Count','People','postcode', 'TrailName','ActivityBike',
        'ActivityRun','ActivityWalk','ActivityCombo','ActivityOther','TFTmethods_Y',
        'TFTmethods_N','TFTmethods_NotSure','Record_Y', 'Record_N','Komoot_link',
        'Time_hours','Total_distance(m)','100m_transect',
        '1km_transect','other_transect','Transect100m','Transect200m','Transect300m',
        'Transect400m','Transect500m','Transect600m','Transect700m','Transect800m',
        'Transect900m','Transect1km','Transect1.1km','Transect1.2km','Transect1.3km',
        'Transect1.4km','Transect1.5km','Transect1.6km','Transect1.7km',
        'Transect1.8km','Transect1.9km','Transect2.0km','Transect2.1km',
        'Transect2.1km','Transect2.2km','Transect2.3km','Transect2.4km','Transect2.5km',
        '1kTransect1','1kTransect2','1kTransect3','1kTransect4','1kTransect5',
        '1kTransect6','1kTransect7','1kTransect8','1kTransect9','1kTransect10',
        '1kTransect11','1kTransect12','1kTransect13','1kTransect14','1kTransect15',
        '1kTransect16','1kTransect17','1kTransect18','1kTransect19','1kTransect20',
        'TotItems','TypeMrkdTrails','TypeRoW','TypeMtnSummitTrail','TypeUpliftAccessed',
        'TypeUnofficial','TypePump','TypeUrban','TypeOtherTrails','TypeAccess','TypeCar',
        'TypeAquatic','TypeOther','ZonesCarpark','ZonesVisitorInfrastructure',
        'ZonesTrailMaps','ZonesTrailhead','ZonesDogPoo','ZonesShakedown',
        'ZonesBottomDescent','ZonesTopClimb','ZonesView','ZonesJumps',
        'ZonesUplift(Un)load','ZonesViewPause','ZonesPicnic','ZonesPuncture','ZonesAlmostHome',
        'ZonesSummit','ZonesRoadCrossing','ZonesSwimspot','ZonesCamp','ZonesToilet',
        'ZonesSkiLift','ZonesOther','MostZonesCarpark','MostZonesVisitorInfrastructure',
        'MostZonesTrailMaps','MostZonesTrailhead','MostZonesDogPoo','MostZonesShakedown',
        'MostZonesBottomDescent','MostZonesTopClimb','MostZonesView','MostZonesJumps',
        'MostZonesUplift','MostZonesPause','MostZonesPicnic','MostZonesPuncture',
        'MostZonesRoadCrossing','MostZonesAlmostHome','MostZonesSummit','MostZonesRoadCrossing','MostZonesSwimspot',
        'MostZonesCamp','MostZonesToilet','MostZonesSkiLift','MostZonesOther',
        'Amount_DRS','Amount_Vapes','AmountGels','MostSUPItem','MostBrand',
        'Connect_SUP_amount','Connect_Impact-ve','Connect_Impact+ve',
        'Connect_ImpactNone','Connect_ImpactNotSure','Connect_Feel','AIY','AIN',
        'AIDidntLook','AINotSure','ThisTrailBeforeY','ThisTrailBeforeN',
        'ThisTrailBeforeValue','UnnaturalY','UnnaturalN','UnnaturalNotSure'] 
    
    #rename columns
    df.columns=cols
    #remove row with extra column names that aren't now needed
    df3 = df.drop(index=0)
    
    #prepare columns with year and month data to be able to extract monthly or yearly data 
    m = []
    y = []
    dates = df3['Date_Count'].values
    for d in dates:
        split = d.split('/')
        month = split[1]
        year = split[2]
        if len(month) == 1:
            new = '0' + month
            m.append(new)
            y.append(year)
        else:
            m.append(month)
            y.append(year)
        
    df3['month'] = m
    df3['year'] = y 
                  
    #exporting the cleaned monthly data 
    df3.to_csv(TFTout + 'CS_count.csv', index=False)
    
def add_to_existing_data(monthin, year_folder):
    """
    A function which takes the prepared monthly TFT data and adds it to the 
    correct yearly file
    
    Parameters
    ----------
    
    monthin: string
            path to folder with input csv files with cleaned raw monthly data
            
    yearin: string
            path to folder with input csv files with cleaned raw yearly data and
            for output files 
             
    """

    forms = ['count', 'survey', 'CS_count', 'CS_survey', 'lite']
    #read csv file
    for file in forms:
        df_month = pd.read_csv(monthin + file + '.csv')   
        df_year = pd.read_csv(year_folder + file + '/' + file + '_2025.csv')
        dfs = (df_month, df_year)
        df_final = pd.concat(dfs, ignore_index = True) 
        df_final.to_csv(year_folder + file + '/' + file + '_2025.csv', index=False)    
        
    

def TFR_clean_data(TFTin, TFTout):
    """
    A function which takes new raw TFR survey data and prepares it for analyses
    
    Parameters
    ----------
             
    TFTin: string
            path to folder with input csv file with new data  
             
            
    TFTout: string
            path to folder to save file with clean data
    """
    #read csv file
    df = pd.read_csv(TFTin + 'Trash Free Races.csv' )
    
    #remove unneeded columns
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
    cols = ['Start_Date', 'End_Date','postcode','EventName','ActivityMTB',
        'ActivityGravel','ActivityRun','ActivityTriathlon','ActivityHike',
        'ActivityFestival','ActivityOther', 'Attendees',
        'Conversations','Newsletters','Merch_teeS','Merch_teeS', 'Merch_teeM'
        'Merch_teeL', 'Merch_teeXL', 'Merch_tee_5-6', 'Merch_tee_7-8',
        'Merch_tee_9-11', 'Merch_hoodyS', 'Merch_hoodyM', 'Merch_hoodyL', 
        'Merch_hoodyXL', 'Mech_glasscoffee', 'Merch_KBCcoffee', 'Merch_Hydroflask',
        'Merch_Stanleyflask', 'Merch_Patch_TFTlogo', 'Merch_Patch_PAlogo', 
        'Merch_Patch_PAwhitesquare', 'Merch_Patch_Trashmob', 'Merch_woodmarker',
        'Merch_steelmarker', 'Full Dog Poo Bags',
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
        'Nappies','Single-Use Period products','Rubber/nitrile gloves', 'Single-Use Covid Masks',
        'Outdoor event (eg Festival)','Camping','Halloween & Fireworks','Seasonal (Christmas and/or Easter)',
        'Normal balloons','Helium balloons','MTB related (e.g. inner tubes, water bottles etc)',
        'Running','Roaming and other outdoor related (e.g. climbing, kayaking)',
        'Textiles','Clothes & Footwear',
        'Plastic milk bottles', 'Glass milk bottles','Plastic food containers',
        'Cardboard food containers',
        'Cleaning products containers','Miscellaneous','Too small/dirty to ID',
        'Weird/Retro', 'Plastic cups', 'Event info leaflets', 'Giveaways',
        'Race tape', 'Food tokens', 'Receipts', 'Paper napkins', 'Reusable bottle',
        'B1_Lucozade','B1_Coke','B1_RedBull','B1_Monster','B1_Cadbury',
        'B1_McDonalds','B1_Walkers','B1_Mars','B1_StellaArtois','B1_Strongbow','B1_Costa',
        'B1_Budweiser','B1_Haribo','B1_SIS','B1_Carling','B1_Fosters','B1_Thatchers',
        'B1_Pepsi','B1_Nestle','B1_Subway','B1_Other','B2_Lucozade','B2_Coke','B2_RedBull',
        'B2_Monster','B2_Cadbury','B2_McDonalds','B2_Walkers','B2_Mars','B2_StellaArtois',
        'B2_Strongbow','B2_Costa','B2_Budweiser','B2_Haribo','B2_SIS','B2_Carling',
        'B2_Fosters','B2_Thatchers','B2_Pepsi','B2_Nestle','B2_Subway','B2_Other',
        'B3_Lucozade','B3_Coke','B3_RedBull','B3_Monster','B3_Cadbury','B3_McDonalds',
        'B3_Walkers','B3_Mars','B3_StellaArtois','B3_Strongbow','B3_Costa','B3_Budweiser',
        'B3_Haribo','B3_SIS','B3_Carling','B3_Fosters','B3_Thatchers','B3_Pepsi',
        'B3_Nestle','B3_Subway','B3_Other','AnimalsY','AnimalsN','AnimalsNotChecked',
        'AnimalsInfo']


    #rename columns
    df.columns=cols
    #remove row with extra column names that aren't now needed
    df_clean = df.drop(index=0)
          
    #exporting the cleaned monthly data 
    df_clean.to_csv(TFTout + 'TFR.csv', index=False)
    
    
    
    
