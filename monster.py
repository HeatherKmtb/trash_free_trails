#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 10:01:49 2026

@author: heatherkay
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os


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
    df = df.drop('Unnamed: 295', axis=1)



    #provide correct column names - could read from existing once wierd columns are sorted
    cols = ['Ethics','Date_TrailClean','People','postcode','TrailName','FamiliarRegular',
        'FamiliarFewTimes','FamiliarFirst','ActivityBike', 'ActivityRun',
        'ActivityWalk','ActivityCombo','ActivityOther','WeatherSunny',
        'WeatherOvercast','WeatherLightRain','WeatherHeavyRain','WeatherSnow',
        'WeatherWinds','WeatherExtremes','HabitatCanal','HabitatCoastal',
        'HabitatFarm','HabitatForest','HabitatMarsh','HabitatMoor','HabitatMountain',
        'HabitatRiver','HabitatUrban','TypeMrkdTrails','TypeRoW','TypeUnofficial',
        'TypePump','TypeUrban','TypeOtherTrails','TypeAccess','TypeCar','TypeOther',
        'MostTypeTrails','MostTypeFootpaths','MostTypeUnofficial','MostTypePump',
        'MostTypeUrban','MostTypeOtherTrails','MostTypeAccess','MostTypeCar',
        'MostTypeOther','Time_min','Distance_km','TotItems','Handful','Pocketful',
        'Bread bag', 'Carrier bag', 'Bin bag', 'Multiple Bin Bags', 
        'Full Dog Poo Bags','Unused Dog Poo Bags','Other Pet Related Stuff',
        'Plastic Water Bottles','Plastic Soft Drink Bottles','Aluminium soft drink cans',
        'Glass soft drink bottles','Milkshake bottle or carton','Plastic energy drink bottles',
        'Aluminium energy drink can','Plastic energy gel sachet','Plastic energy gel end',
        'Protein drink bottle or carton', 'Aluminium alcoholic drink cans',
        'Glass alcoholic bottles','Hot drinks cups','Hot drinks tops and stirrers',
        'Cold drinks cups and tops','Cartons','Plastic straws','Paper straws',
        'Plastic bottle, top', 'Glass bottle tops', 'Ring pull', 'Plastic bottle sleeve',
        'Reusable drinks container','Other drink related','Confectionary/sweet wrappers',
        'Wrapper "corners" / tear-offs','Other confectionary (eg., Lollipop Sticks)',
        'Crisps Packets','Used Chewing Gum','Homemade lunch (eg., aluminium foil, cling film)',
        'BBQ related','Fruit peel & cores','Branded single-use carrier bags',
        'Unbranded single-use carrier bags', 'Branded bag for life','Unbranded bag for life', 
        'Branded plastic fast / takeaway food packaging / utensils',
        'Unbranded plastic fast / takeaway food packaging / utensils',
        'Branded card or wood fast / takeaway food packaging / utensils',
        'Unbranded card or wood fast / takeaway food packaging / utensils',
        'Branded condiments packaging','Unbranded condiments packaging',
        'Branded food on the go','Unbranded food on the go','Branded other food related',
        'Unbranded other food related','Clothes & Footwear','Textiles',
        'Plastic milk bottles','Glass milk bottles','Plastic food containers',
        'Cardboard food containers','Cleaning products containers',
        'Cosmetics / deodorants', 'Other household','Cigarette Butts','Nicotine pouches',
        'Disposable vapes',
        'Nicotine related packaging','Other nicotine related','Unbagged dog poo',
        'Needles / syringes','Other drug related','broken glass or pottery',
        'Toilet tissue','Face/ baby wipes','Nappies','Period products',
        'Covid Masks','First Aid & medcal waste','batteries and electronics',
        'Other hazardous', 'Camping','Fireworks','Seasonal (Christmas and/or Easter)',
        'Rubber balloons','Foil balloons','Outdoor event related (e.g.race)',
        'Biking specific','Hiking specific','Other outdoor related',
        'Farming','Forestry','Industrial','Cable ties','Miscellaneous hard plastic',
        'Miscellaneous soft plastic','Miscellaneous card or wood','Miscellaneous metal',
        'Too small/dirty to ID','Other Miscellaneous','MoreInfoY','MoreInfoN',
        'Value Full Dog Poo Bags',
        'Value Unused Dog Poo Bags','Value Other Pet Related Stuff',
        'Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
        'Value Aluminium soft drink cans',
        'Value Glass soft drink bottles','Value Milkshake bottle or carton',
        'Value Plastic energy drink bottles',
        'Value Aluminium energy drink can','Value Plastic energy gel sachet',
        'Value Plastic energy gel end',
        'Value Protein drink bottle or carton', 'Value Aluminium alcoholic drink cans',
        'Value Glass alcoholic bottles','Value Hot drinks cups',
        'Value Hot drinks tops and stirrers',
        'Value Cold drinks cups and tops','Value Cartons','Value Plastic straws',
        'Value Paper straws',
        'Value Plastic bottle, top', 'Value Glass bottle tops', 'Value Ring pull', 
        'Value Plastic bottle sleeve',
        'Value Reusable drinks container','Value Other drink related',
        'Value Confectionary/sweet wrappers','Value Wrapper "corners" / tear-offs',
        'Value Other confectionary (eg., Lollipop Sticks)',
        'Value Crisps Packets','Value Used Chewing Gum','Value Homemade lunch (eg., aluminium foil, cling film)',
        'Value BBQ related','Value Fruit peel & cores','Value Branded single-use carrier bags',
        'Value Unbranded single-use carrier bags', 'Value Branded bag for life',
        'Value Unbranded bag for life', 
        'Value Branded plastic fast / takeaway food packaging / utensils',
        'Value Unbranded plastic fast / takeaway food packaging / utensils',
        'Value Branded card or wood fast / takeaway food packaging / utensils',
        'Value Unbranded card or wood fast / takeaway food packaging / utensils',
        'Value Branded condiments packaging','Value Unbranded condiments packaging',
        'Value Branded food on the go','Value Unbranded food on the go',
        'Value Branded other food related','Value Unbranded other food related',
        'Value Clothes & Footwear','Value Textiles','Value Plastic milk bottles',
        'Value Glass milk bottles',
        'Value Plastic food containers','Value Cardboard food containers',
        'Value Cleaning products containers',
        'Value Cosmetics / deodorants', 'Value Other household',
        'Value Cigarette Butts','Value Nicotine pouches','Value Disposable vapes',
        'Value Nicotine related packaging','Value Other nicotine related',
        'Value Unbagged dog poo',
        'Value Needles / syringes','Value Other drug related','Value Broken glass or pottery',
        'Value Toilet tissue','Value Face/ baby wipes','Value Nappies','Value Period products',
        'Value Covid Masks','Value First Aid & medcal waste','Value Batteries and electronics',
        'Value Other hazardous', 'Value Camping','Value Fireworks','Value Seasonal (Christmas and/or Easter)',
        'Value Rubber balloons','Value Foil balloons','Value Outdoor event related (e.g.race)',
        'Value Biking specific','Value Hiking specific','Value Other outdoor related',
        'Value Farming','Value Forestry','Value Industrial','Value Cable ties',
        'Value Miscellaneous hard plastic','Value Miscellaneous soft plastic',
        'Value Miscellaneous card or wood','Value Miscellaneous metal',
        'Value Too small/dirty to ID','Value Other Miscellaneous','Perc_SU',
        'Lucozade', 'Ribena','RedBull','Monster','High5','SIS','Danone','Highland Spring',
        'Coke','Costa','Pepsi','Walkers','Barrs','Britvic','Mars','Nestle',
        'Mondelez','Cadbury','Magnum','Haribo','AB InBev','Corona','Molson Corrs',
        'Thatchers','Heineken','Fosters','Bulmers','Carlsberg','Burger King',
        'Greggs','KFC','McDonalds','Subway','Aldi','Co-op','Euro Shopper','LiDL',
        'M&S','Tesco','Other','AnimalsY','AnimalsN','AnimalsNotChecked','Rando Q',
        'AIDeath','AIChew','AINesting','AIOther','AItype','ExperienceY','ExperienceN',
        'Experience_Feeling1', 'Experience_Feeling2','Experience_Feeling3',
        'Experience_+veFeeling0','Experience_+veFeeling1','Experience_+veFeeling2',
        'Experience_+veFeeling3','Experience_+veFeeling4','Experience_+veFeeling5',
        'Experience_+veFeeling6','Experience_+veFeeling7','Experience_+veFeeling8',
        'Experience_+veFeeling9','Experience_+veFeeling10','Experience_Engagement0',
        'Experience_Engagement1','Experience_Engagement2','Experience_Engagement3',
        'Experience_Engagement4','Experience_Engagement5','Experience_Engagement6',
        'Experience_Engagement7','Experience_Engagement8','Experience_Engagement9',
        'Experience_Engagement10','Experience_Relationships0',
        'Experience_Relationships1','Experience_Relationships2',
        'Experience_Relationships3','Experience_Relationships4',
        'Experience_Relationships5','Experience_Relationships6',
        'Experience_Relationships7','Experience_Relationships8',
        'Experience_Relationships9','Experience_Relationships10',
        'Experience_Meaning0','Experience_Meaning1','Experience_Meaning2',
        'Experience_Meaning3','Experience_Meaning4','Experience_Meaning5',
        'Experience_Meaning6','Experience_Meaning7','Experience_Meaning8',
        'Experience_Meaning9','Experience_Meaning10','Experience_Accomplishment0',
        'Experience_Accomplishment1','Experience_Accomplishment2',
        'Experience_Accomplishment3','Experience_Accomplishment4',
        'Experience_Accomplishment5','Experience_Accomplishment6',
        'Experience_Accomplishment7','Experience_Accomplishment8',
        'Experience_Accomplishment9','Experience_Accomplishment10',
        'Experience_Health0','Experience_Health1','Experience_Health2',
        'Experience_Health3','Experience_Health4','Experience_Health5',
        'Experience_Health6','Experience_Health7','Experience_Health8',
        'Experience_Health9','Experience_Health10','Experience_NatureConnect0',
        'Experience_NatureConnect1','Experience_NatureConnect2',
        'Experience_NatureConnect3','Experience_NatureConnect4',
        'Experience_NatureConnect5','Experience_NatureConnect6',
        'Experience_NatureConnect7','Experience_NatureConnect8',
        'Experience_NatureConnect9','Experience_NatureConnect10',
        'Experience_Place0','Experience_Place1','Experience_Place2',
        'Experience_Place3','Experience_Place4','Experience_Place5',
        'Experience_Place6','Experience_Place7','Experience_Place8',
        'Experience_Place9','Experience_Place10','Experience_Knowledge0',
        'Experience_Knowledge1','Experience_Knowledge2','Experience_Knowledge3',
        'Experience_Knowledge4','Experience_Knowledge5','Experience_Knowledge6',
        'Experience_Knowledge7','Experience_Knowledge8','Experience_Knowledge9',
        'Experience_Knowledge10',
        'Connection_RewardY','Connection_RewardN','Connection_RewardUnsure',
        'Connection_TakePartAgainY','Connection_TakePartAgainN',
        'Connection_TakePartAgainUnsure','First time','Volunteer','A-Team',
        'HQ','Community Hub','VolunteerWeeks',
        'VolunteerMonths','VolunteerYears','WhySubmit','Name','Surname','Email',
        'Receive emailY','Receive emailN','Receive email_alreadyin',
        'DemographicsY','DemographicsN',
        'AgeU18','Age18-14','Age25-34','Age35-44','Age45-54','Age55-64','Age65+',
        'GenderFemale','GenderMale','GenderNon-binary','GenderTransgender',
        'GenderPreferNot','GenderOther','HomePostcode','EthnicAfrican','EthnicArab',
        'EthnicAsian','EthinicLatino','EthnicCaucasian','EthinicPreferNot',
        'EthnicOther','IllnessY','IllnessN','IllnessPreferNot'
        ]


    #rename columns
    df.columns=cols
    #remove row with extra column names that aren't now needed
    df_clean = df.drop(index=0)
    
    df_clean = df_clean.drop('Rando Q', axis=1)
    df_clean.insert(58, 'Binbags', np.nan)
    
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
    df_clean.insert(loc=50, column = 'AdjTotItems', value=AdjTotItems)
    

    exp_cols = ['Experience_+veFeeling0','Experience_+veFeeling1','Experience_+veFeeling2',
    'Experience_+veFeeling3','Experience_+veFeeling4','Experience_+veFeeling5',
    'Experience_+veFeeling6','Experience_+veFeeling7','Experience_+veFeeling8',
    'Experience_+veFeeling9','Experience_+veFeeling10','Experience_Engagement0',
    'Experience_Engagement1','Experience_Engagement2','Experience_Engagement3',
    'Experience_Engagement4','Experience_Engagement5','Experience_Engagement6',
    'Experience_Engagement7','Experience_Engagement8','Experience_Engagement9',
    'Experience_Engagement10','Experience_Relationships0',
    'Experience_Relationships1','Experience_Relationships2',
    'Experience_Relationships3','Experience_Relationships4',
    'Experience_Relationships5','Experience_Relationships6',
    'Experience_Relationships7','Experience_Relationships8',
    'Experience_Relationships9','Experience_Relationships10',
    'Experience_Meaning0','Experience_Meaning1','Experience_Meaning2',
    'Experience_Meaning3','Experience_Meaning4','Experience_Meaning5',
    'Experience_Meaning6','Experience_Meaning7','Experience_Meaning8',
    'Experience_Meaning9','Experience_Meaning10','Experience_Accomplishment0',
    'Experience_Accomplishment1','Experience_Accomplishment2',
    'Experience_Accomplishment3','Experience_Accomplishment4',
    'Experience_Accomplishment5','Experience_Accomplishment6',
    'Experience_Accomplishment7','Experience_Accomplishment8',
    'Experience_Accomplishment9','Experience_Accomplishment10',
    'Experience_Health0','Experience_Health1','Experience_Health2',
    'Experience_Health3','Experience_Health4','Experience_Health5',
    'Experience_Health6','Experience_Health7','Experience_Health8',
    'Experience_Health9','Experience_Health10','Experience_NatureConnect0',
    'Experience_NatureConnect1','Experience_NatureConnect2',
    'Experience_NatureConnect3','Experience_NatureConnect4',
    'Experience_NatureConnect5','Experience_NatureConnect6',
    'Experience_NatureConnect7','Experience_NatureConnect8',
    'Experience_NatureConnect9','Experience_NatureConnect10',
    'Experience_Place0','Experience_Place1','Experience_Place2',
    'Experience_Place3','Experience_Place4','Experience_Place5',
    'Experience_Place6','Experience_Place7','Experience_Place8',
    'Experience_Place9','Experience_Place10','Experience_Knowledge0',
    'Experience_Knowledge1','Experience_Knowledge2','Experience_Knowledge3',
    'Experience_Knowledge4','Experience_Knowledge5','Experience_Knowledge6',
    'Experience_Knowledge7','Experience_Knowledge8','Experience_Knowledge9',
    'Experience_Knowledge10'
    ]
  
    df_clean[exp_cols] = df_clean[exp_cols].apply(pd.to_numeric, errors='coerce')

    df_clean[exp_cols] = df_clean[exp_cols].replace({
        '0 - Not at all': 0,
        '10 - Completely': 10
        }, regex=False)
    
    for i in range(0, len(exp_cols), 11):
        group = exp_cols[i : i + 11]
        
        
        new_col_name = group[0][:-1] 
        max_col = df_clean[group].idxmax(axis=1) 
        df_clean[new_col_name] = max_col.str.extract(r'(\d+)$').astype(float)
        df_clean.drop(columns=group, inplace=True)
    
    perma_cols = ['Experience_+veFeeling','Experience_Engagement',
        'Experience_Relationships','Experience_Meaning','Experience_Accomplishment',
        'Experience_Health'
        ]
    
    df_clean['perma_score'] = df_clean[perma_cols].mean(axis=1)
        
    #remove sensitive data for U18s
    cols_to_clear = ['Experience_Feeling1', 'Experience_Feeling2',
        'Experience_Feeling3','Experience_+veFeeling','Experience_Engagement',
        'Experience_Relationships','Experience_Meaning','Experience_Accomplishment',
        'Experience_Health','Experience_NatureConnect','Experience_Knowledge',
        'GenderFemale','GenderMale','GenderNon-binary','GenderTransgender',
        'GenderPreferNot','GenderOther','HomePostcode','EthnicAfrican',
        'EthnicArab','EthnicAsian','EthinicLatino','EthnicCaucasian','EthinicPreferNot',
        'EthnicOther','IllnessY','IllnessN','IllnessPreferNot'
        ]

    df_clean.loc[df_clean['AgeU18'].notna(), cols_to_clear] = None
        

    
    #change data in presence(composition) data to TRUE
    change_cols = ['Handful','Pocketful','Bread bag',
            'Carrier bag', 'Bin bag', 'Full Dog Poo Bags','Unused Dog Poo Bags',
            'Other Pet Related Stuff',
            'Plastic Water Bottles','Plastic Soft Drink Bottles',
            'Aluminium soft drink cans',
            'Glass soft drink bottles','Milkshake bottle or carton',
            'Plastic energy drink bottles',
            'Aluminium energy drink can','Plastic energy gel sachet',
            'Plastic energy gel end',
            'Protein drink bottle or carton', 'Aluminium alcoholic drink cans',
            'Glass alcoholic bottles','Hot drinks cups','Hot drinks tops and stirrers',
            'Cold drinks cups and tops','Cartons','Plastic straws','Paper straws',
            'Plastic bottle, top', 'Glass bottle tops', 'Ring pull', 
            'Plastic bottle sleeve',
            'Reusable drinks container','Other drink related',
            'Confectionary/sweet wrappers',
            'Wrapper "corners" / tear-offs',
            'Other confectionary (eg., Lollipop Sticks)',
            'Crisps Packets','Used Chewing Gum',
            'Homemade lunch (eg., aluminium foil, cling film)',
            'BBQ related','Fruit peel & cores','Branded single-use carrier bags',
            'Unbranded single-use carrier bags', 'Branded bag for life',
            'Unbranded bag for life', 
            'Branded plastic fast / takeaway food packaging / utensils',
            'Unbranded plastic fast / takeaway food packaging / utensils',
            'Branded card or wood fast / takeaway food packaging / utensils',
            'Unbranded card or wood fast / takeaway food packaging / utensils',
            'Branded condiments packaging','Unbranded condiments packaging',
            'Branded food on the go','Unbranded food on the go',
            'Branded other food related',
            'Unbranded other food related','Clothes & Footwear','Textiles',
            'Plastic milk bottles','Glass milk bottles','Plastic food containers',
            'Cardboard food containers','Cleaning products containers',
            'Cosmetics / deodorants', 'Other household','Cigarette Butts',
            'Nicotine pouches','Disposable vapes',
            'Nicotine related packaging','Other nicotine related','Unbagged dog poo',
            'Needles / syringes','Other drug related','broken glass or pottery',
            'Toilet tissue','Face/ baby wipes','Nappies','Period products',
            'Covid Masks','First Aid & medcal waste','batteries and electronics',
            'Other hazardous', 'Camping','Fireworks','Seasonal (Christmas and/or Easter)',
            'Rubber balloons','Foil balloons','Outdoor event related (e.g.race)',
            'Biking specific','Hiking specific','Other outdoor related',
            'Farming','Forestry','Industrial','Cable ties','Miscellaneous hard plastic',
            'Miscellaneous soft plastic','Miscellaneous card or wood','Miscellaneous metal',
            'Too small/dirty to ID','Other Miscellaneous'
            ]

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
    
    #reorder so experience cols are together
    cols = list(range(df3.shape[1]))
    target_block = cols[348:357]
    remaining_cols = [c for c in cols if c not in target_block]
    new_order = remaining_cols[:302] + target_block + remaining_cols[302:]
    df3 = df3.iloc[:, new_order]
             
    #exporting the cleaned monthly data 
    df3.to_csv(TFTout + 'survey.csv', index=False)
     
    
def lite_clean_data(TFTin, TFTout, year_folder):
    """
    Cleans TFT lite data and calculates total items per bag type using
    imported average item counts per bag.

    Parameters
    ----------
    TFTin : str
        Path to folder with input CSV file 'lite.csv'.
    TFTout : str
        Path to folder to save cleaned data and results.
    averages_path : str
        Path to CSV containing average items per bag type (columns: 'bag', 'avg_items').
    """
    
    df = pd.read_csv(os.path.join(TFTin, 'lite.csv'))
    averages = pd.read_csv(year_folder + 'bag_averages_calc.csv')

    avg_map = dict(zip(averages['bag'], averages['avg_items']))

    # Define mapping between readable names and DataFrame column names
    bag_column_map = {'handful': 'Quantity - Handful',
        'pocketful': 'Quantity - Pocketful',
        'breadbag': 'Quantity - Bread Bag',
        'carrierbag': 'Quantity - Carrier Bag',
        'binbag': 'Quantity - Generic Bin Bag',
        'multiplebinbags': 'Quantity - Multiple Bin Bags'}

    # --- 2. Extract year/month from Created Date ---
    df[['year', 'month']] = df['Created Date'].str.split('-', n=2, expand=True)[[0, 1]]

    # --- 3. Remove rows with more than one TRUE ---
    trash_cols = list(bag_column_map.values())
    df = df[df[trash_cols].sum(axis=1) == 1]

    # --- 3a. Add TotItems column ---
    def get_tot_items(row):
        if pd.notna(row['How many items?']):
            return row['How many items?']
        
        for bag, col in bag_column_map.items():
            if row[col] == True:
                avg_items = avg_map.get(bag, 0)
                num_bags = row['How many bags?'] if (bag == 'multiplebinbags' and not pd.isna(row['How many bags?'])) else 1
                return num_bags * avg_items
        return 0

    df['TotItems'] = df.apply(get_tot_items, axis=1)
    
    df['LIVE I felt connected to nature during the trail clean'] = df['LIVE I felt connected to nature during the trail clean'].str.strip('[]"')
    df['OLD I felt connected to nature during the trail clean'] = df['OLD I felt connected to nature during the trail clean'].replace(6, np.nan)    
            
    NC_cols = ['LIVE I felt connected to nature during the trail clean',
               'OLD I felt connected to nature during the trail clean',
               'Increased Nature Connection - No',
               'Increased Nature Connection - No Change',
               'Increased Nature Connection - Not Sure',
               'Increased Nature Connection - Yes'
               ]
    # Combine the two into a single new column
    df['nature_connection'] = df['LIVE I felt connected to nature during the trail clean'].combine_first(df['OLD I felt connected to nature during the trail clean'])
    df = df.drop(columns=NC_cols)
    
    # Save cleaned version with TotItems and email_id
    df.to_csv(os.path.join(TFTout, 'lite.csv'), index=False)
    
    
def experience_clean_data(TFTin, TFTout):
    """
    A function which takes new raw wellbeing data and prepares it for analyses
    
    Parameters
    ----------
             
    TFTin: string
            path to folder with input csv file with new data  
             
            
    TFTout: string
            path to folder to save file with clean data
    """
    #read csv file
    df = pd.read_csv(TFTin + 'experience.csv' )
    
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
    cols = ['EthicsY','EthicsN','Location','Date_TrailClean','Type_Hosted',
            'Type_Self_organised','Type_NotSure','Type_Other','FamiliarRegular',
            'FamiliarFewTimes','FamiliarFirst','Experience_Feeling1', 
            'Experience_Feeling2','Experience_Feeling3',
            'Experience_+veFeeling0','Experience_+veFeeling1','Experience_+veFeeling2',
            'Experience_+veFeeling3','Experience_+veFeeling4','Experience_+veFeeling5',
            'Experience_+veFeeling6','Experience_+veFeeling7','Experience_+veFeeling8',
            'Experience_+veFeeling9','Experience_+veFeeling10','Experience_Engagement0',
            'Experience_Engagement1','Experience_Engagement2','Experience_Engagement3',
            'Experience_Engagement4','Experience_Engagement5','Experience_Engagement6',
            'Experience_Engagement7','Experience_Engagement8','Experience_Engagement9',
            'Experience_Engagement10','Experience_Relationships0',
            'Experience_Relationships1','Experience_Relationships2',
            'Experience_Relationships3','Experience_Relationships4',
            'Experience_Relationships5','Experience_Relationships6',
            'Experience_Relationships7','Experience_Relationships8',
            'Experience_Relationships9','Experience_Relationships10',
            'Experience_Meaning0','Experience_Meaning1','Experience_Meaning2',
            'Experience_Meaning3','Experience_Meaning4','Experience_Meaning5',
            'Experience_Meaning6','Experience_Meaning7','Experience_Meaning8',
            'Experience_Meaning9','Experience_Meaning10','Experience_Accomplishment0',
            'Experience_Accomplishment1','Experience_Accomplishment2',
            'Experience_Accomplishment3','Experience_Accomplishment4',
            'Experience_Accomplishment5','Experience_Accomplishment6',
            'Experience_Accomplishment7','Experience_Accomplishment8',
            'Experience_Accomplishment9','Experience_Accomplishment10',
            'Experience_Health0','Experience_Health1','Experience_Health2',
            'Experience_Health3','Experience_Health4','Experience_Health5',
            'Experience_Health6','Experience_Health7','Experience_Health8',
            'Experience_Health9','Experience_Health10','Experience_NatureConnect0',
            'Experience_NatureConnect1','Experience_NatureConnect2',
            'Experience_NatureConnect3','Experience_NatureConnect4',
            'Experience_NatureConnect5','Experience_NatureConnect6',
            'Experience_NatureConnect7','Experience_NatureConnect8',
            'Experience_NatureConnect9','Experience_NatureConnect10',
            'Experience_Place0','Experience_Place1','Experience_Place2',
            'Experience_Place3','Experience_Place4','Experience_Place5',
            'Experience_Place6','Experience_Place7','Experience_Place8',
            'Experience_Place9','Experience_Place10','Experience_Knowledge0',
            'Experience_Knowledge1','Experience_Knowledge2','Experience_Knowledge3',
            'Experience_Knowledge4','Experience_Knowledge5','Experience_Knowledge6',
            'Experience_Knowledge7','Experience_Knowledge8','Experience_Knowledge9',
            'Experience_Knowledge10','TakePartAgainY','TakePartAgainN',
            'TakePartAgainUnsure','First time','Volunteer','A-Team',
            'HQ','Community Hub', 'Clean_Hosting','Clean_Supporting',
            'Clean_Attending','VolunteerWeeks','VolunteerMonths','VolunteerYears',
            'Anything else','Name','Surname','Email','Receive emailY',
            'Receive emailN','Receive email_alreadyin','DemographicsY','DemographicsN',
            'AgeU18','Age18-14','Age25-34','Age35-44','Age45-54','Age55-64','Age65+',
            'GenderFemale','GenderMale','GenderNon-binary','GenderTransgender',
            'GenderPreferNot','GenderOther','HomePostcode','EthnicAfrican','EthnicArab',
            'EthnicAsian','EthinicLatino','EthnicCaucasian','EthinicPreferNot',
            'EthnicOther','IllnessY','IllnessN','IllnessPreferNot'
            ]
    
    #rename columns
    df.columns=cols
    #remove row with extra column names that aren't now needed
    df_clean = df.drop(index=0)
    
    exp_cols = ['Experience_+veFeeling0','Experience_+veFeeling1','Experience_+veFeeling2',
    'Experience_+veFeeling3','Experience_+veFeeling4','Experience_+veFeeling5',
    'Experience_+veFeeling6','Experience_+veFeeling7','Experience_+veFeeling8',
    'Experience_+veFeeling9','Experience_+veFeeling10','Experience_Engagement0',
    'Experience_Engagement1','Experience_Engagement2','Experience_Engagement3',
    'Experience_Engagement4','Experience_Engagement5','Experience_Engagement6',
    'Experience_Engagement7','Experience_Engagement8','Experience_Engagement9',
    'Experience_Engagement10','Experience_Relationships0',
    'Experience_Relationships1','Experience_Relationships2',
    'Experience_Relationships3','Experience_Relationships4',
    'Experience_Relationships5','Experience_Relationships6',
    'Experience_Relationships7','Experience_Relationships8',
    'Experience_Relationships9','Experience_Relationships10',
    'Experience_Meaning0','Experience_Meaning1','Experience_Meaning2',
    'Experience_Meaning3','Experience_Meaning4','Experience_Meaning5',
    'Experience_Meaning6','Experience_Meaning7','Experience_Meaning8',
    'Experience_Meaning9','Experience_Meaning10','Experience_Accomplishment0',
    'Experience_Accomplishment1','Experience_Accomplishment2',
    'Experience_Accomplishment3','Experience_Accomplishment4',
    'Experience_Accomplishment5','Experience_Accomplishment6',
    'Experience_Accomplishment7','Experience_Accomplishment8',
    'Experience_Accomplishment9','Experience_Accomplishment10',
    'Experience_Health0','Experience_Health1','Experience_Health2',
    'Experience_Health3','Experience_Health4','Experience_Health5',
    'Experience_Health6','Experience_Health7','Experience_Health8',
    'Experience_Health9','Experience_Health10','Experience_NatureConnect0',
    'Experience_NatureConnect1','Experience_NatureConnect2',
    'Experience_NatureConnect3','Experience_NatureConnect4',
    'Experience_NatureConnect5','Experience_NatureConnect6',
    'Experience_NatureConnect7','Experience_NatureConnect8',
    'Experience_NatureConnect9','Experience_NatureConnect10',
    'Experience_Place0','Experience_Place1','Experience_Place2',
    'Experience_Place3','Experience_Place4','Experience_Place5',
    'Experience_Place6','Experience_Place7','Experience_Place8',
    'Experience_Place9','Experience_Place10','Experience_Knowledge0',
    'Experience_Knowledge1','Experience_Knowledge2','Experience_Knowledge3',
    'Experience_Knowledge4','Experience_Knowledge5','Experience_Knowledge6',
    'Experience_Knowledge7','Experience_Knowledge8','Experience_Knowledge9',
    'Experience_Knowledge10'
    ]
  
    df_clean[exp_cols] = df_clean[exp_cols].apply(pd.to_numeric, errors='coerce')

    df_clean[exp_cols] = df_clean[exp_cols].replace({
        '0 - Not at all': 0,
        '10 - Completely': 10
        }, regex=False)
    
    for i in range(0, len(exp_cols), 11):
        group = exp_cols[i : i + 11]
        
        
        new_col_name = group[0][:-1] 
        max_col = df_clean[group].idxmax(axis=1) 
        df_clean[new_col_name] = max_col.str.extract(r'(\d+)$').astype(float)
        df_clean.drop(columns=group, inplace=True)
    
    perma_cols = ['Experience_+veFeeling','Experience_Engagement',
        'Experience_Relationships','Experience_Meaning','Experience_Accomplishment',
        'Experience_Health'
        ]
    
    df_clean['perma_score'] = df_clean[perma_cols].mean(axis=1)
        
    #remove sensitive data for U18s
    cols_to_clear = ['Experience_Feeling1', 'Experience_Feeling2',
        'Experience_Feeling3','Experience_+veFeeling','Experience_Engagement',
        'Experience_Relationships','Experience_Meaning','Experience_Accomplishment',
        'Experience_Health','Experience_NatureConnect','Experience_Knowledge',
        'GenderFemale','GenderMale','GenderNon-binary','GenderTransgender',
        'GenderPreferNot','GenderOther','HomePostcode','EthnicAfrican',
        'EthnicArab','EthnicAsian','EthinicLatino','EthnicCaucasian','EthinicPreferNot',
        'EthnicOther','IllnessY','IllnessN','IllnessPreferNot'
        ]
 
    before = len(df_clean.index)
    df_clean.loc[df_clean['AgeU18'].notna(), cols_to_clear] = None
    after = len(df_clean.index)
    U18s_int = before - after
    U18s = str(U18s_int)
    
    
    df3 = df_clean[df_clean['Date_TrailClean'].notna()]
    
    
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
    df3.to_csv(TFTout + 'experience.csv', index=False)
    
    print('Number of Under 18s submissions = ' + U18s)
    


def monster_stats_and_graphs(folderin, folderout):
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
    results = pd.DataFrame(columns = ['no_people','distance_km','duration_hours', 
                                      'total_items'
                                      ])
    
    lite_dt = pd.read_csv(folderin + 'other_averages_calc.csv',
                          index_col=0).iloc[:, 0]
    lite_dict = lite_dt.to_dict()  
    
    survey = pd.read_csv(folderin + 'survey.csv')
    lite = pd.read_csv(folderin + 'lite.csv')
    experience = pd.read_csv(folderin + 'experience.csv')
  
    count_lite = len(lite.index)

        
    #Overview - volunteers, distance, hours, items
    mins = survey['Time_min']
    hours = []
    for m in mins:
        hour = m/60
        hours.append(hour)
        
    survey['Time_hours'] = hours    
    
    tot_people = []
    tot_time = []
    
    minutes = lite_dict['Time_min']
    time = minutes/60

    survey['Time_hours'] = survey['Time_hours'].replace(0, time).fillna(time)
    survey['People'] = survey['People'].replace(0, lite_dict['People']).fillna(lite_dict['People'])
    
    people = survey['People'].sum()
    hours = (survey['People'] * survey['Time_hours']).sum()

    tot_people.append(people)
    tot_time.append(hours)

    #add to total people the number of lite and count submissions
    lite_people = count_lite * lite_dict['People']
    tot_people.append(lite_people)

 
#volunteers
    total_people = sum(tot_people)
    
    survey_km = survey['Distance_km'].sum()
    lite_km = count_lite * lite_dict['Distance_km']
      
    kms = [survey_km, lite_km]
#distance cleaned / surveyed 
    km = sum(kms)
        
    #method to estimate time spent on count
    lite_time = count_lite * time
    tot_time.append(lite_time)
#time 
    total_time = sum(tot_time) 

    all_items = ['Value Full Dog Poo Bags',
    'Value Unused Dog Poo Bags','Value Other Pet Related Stuff',
    'Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
    'Value Aluminium soft drink cans',
    'Value Glass soft drink bottles','Value Milkshake bottle or carton',
    'Value Plastic energy drink bottles',
    'Value Aluminium energy drink can','Value Plastic energy gel sachet',
    'Value Plastic energy gel end',
    'Value Protein drink bottle or carton', 'Value Aluminium alcoholic drink cans',
    'Value Glass alcoholic bottles','Value Hot drinks cups',
    'Value Hot drinks tops and stirrers',
    'Value Cold drinks cups and tops','Value Cartons','Value Plastic straws',
    'Value Paper straws',
    'Value Plastic bottle, top', 'Value Glass bottle tops', 'Value Ring pull', 
    'Value Plastic bottle sleeve',
    'Value Reusable drinks container','Value Other drink related',
    'Value Confectionary/sweet wrappers','Value Wrapper "corners" / tear-offs',
    'Value Other confectionary (eg., Lollipop Sticks)',
    'Value Crisps Packets','Value Used Chewing Gum','Value Homemade lunch (eg., aluminium foil, cling film)',
    'Value BBQ related','Value Fruit peel & cores','Value Branded single-use carrier bags',
    'Value Unbranded single-use carrier bags', 'Value Branded bag for life',
    'Value Unbranded bag for life', 
    'Value Branded plastic fast / takeaway food packaging / utensils',
    'Value Unbranded plastic fast / takeaway food packaging / utensils',
    'Value Branded card or wood fast / takeaway food packaging / utensils',
    'Value Unbranded card or wood fast / takeaway food packaging / utensils',
    'Value Branded condiments packaging','Value Unbranded condiments packaging',
    'Value Branded food on the go','Value Unbranded food on the go',
    'Value Branded other food related','Value Unbranded other food related',
    'Value Clothes & Footwear','Value Textiles','Value Plastic milk bottles',
    'Value Glass milk bottles',
    'Value Plastic food containers','Value Cardboard food containers',
    'Value Cleaning products containers',
    'Value Cosmetics / deodorants', 'Value Other household',
    'Value Cigarette Butts','Value Nicotine pouches','Value Disposable vapes',
    'Value Nicotine related packaging','Value Other nicotine related',
    'Value Unbagged dog poo',
    'Value Needles / syringes','Value Other drug related','Value Broken glass or pottery',
    'Value Toilet tissue','Value Face/ baby wipes','Value Nappies','Value Period products',
    'Value Covid Masks','Value First Aid & medcal waste','Value Batteries and electronics',
    'Value Other hazardous', 'Value Camping','Value Fireworks','Value Seasonal (Christmas and/or Easter)',
    'Value Rubber balloons','Value Foil balloons','Value Outdoor event related (e.g.race)',
    'Value Biking specific','Value Hiking specific','Value Other outdoor related',
    'Value Farming','Value Forestry','Value Industrial','Value Cable ties',
    'Value Miscellaneous hard plastic','Value Miscellaneous soft plastic',
    'Value Miscellaneous card or wood','Value Miscellaneous metal',
    'Value Too small/dirty to ID','Value Other Miscellaneous']
    
    #Resolve nan issues
    survey[all_items] = survey[all_items].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

    rmv_items = [] 

    survey_items = survey['TotItems'].sum()   
    rmv_items.append(survey_items)

    lite_items = lite['TotItems'].sum() 
    rmv_items.append(lite_items)
      
    total_items = sum(rmv_items)
    
    new_row = pd.DataFrame([{'no_people':total_people, 'distance_km':km,
                              'duration_hours':total_time, 'total_items':total_items
                              }])
    
    results= pd.concat([results, new_row], ignore_index=True) 
                                        
    
    results.to_csv(folderout + '/overview.csv',index=False)  

    #plot DRS items
    DRS = ['Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
    'Value Aluminium soft drink cans', 'Value Glass soft drink bottles',
    'Value Plastic energy drink bottles','Value Aluminium energy drink can',
    'Value Aluminium alcoholic drink cans','Value Glass alcoholic bottles',
    'Value Glass soft drink bottles','Value Glass alcoholic bottles'
    ] 

    df = survey 
    
    df['DRS_sum'] = df[DRS].sum(axis=1)

    df_sorted = df.sort_values(by='TotItems', ascending=False)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar(df_sorted['TrailName'], df_sorted['TotItems'], color='#80DCB5', label='Other Items')
    ax.bar(df_sorted['TrailName'], df_sorted['DRS_sum'], color='#00945C', label='DRS Items')
    
    afont = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 12}
    
    tfont = {'family' : 'sans-serif',
        'weight' : 'bold',
        'size'   : 18}


    ax.set_xlabel('Location', **afont)
    ax.set_ylabel('Total Items', **afont)
    ax.set_title('Items per Trail Breakdown', **tfont, pad=15)
    ax.legend()

    # Rotate x-axis labels to prevent overlapping
    plt.xticks(rotation=45, ha='right')

    plt.savefig(folderout + '/total_items.png', bbox_inches='tight')
    plt.close
    
    #plot brands
    brands = ['Lucozade', 'Ribena','RedBull','Monster','High5','SIS','Danone',
              'Highland Spring','Coke','Costa','Pepsi','Walkers','Barrs',
              'Britvic','Mars','Nestle','Mondelez','Cadbury','Magnum','Haribo',
              'AB InBev','Corona','Molson Corrs','Thatchers','Heineken',
              'Fosters','Bulmers','Carlsberg','Burger King','Greggs','KFC',
              'McDonalds','Subway','Aldi','Co-op','Euro Shopper','LiDL',
              'M&S','Tesco']  

    brand_totals = df[brands].apply(pd.to_numeric, errors='coerce').sum()
    brand_totals = brand_totals.sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar(brand_totals.index, brand_totals.values, color='#00945C', edgecolor='black')

    ax.set_xlabel('Brands', **afont)
    ax.set_ylabel('Total', **afont)
    ax.set_title('Total Sum per Brand', **tfont, pad=15)

    plt.xticks(rotation=45, ha='right')

    plt.savefig(folderout + '/brands.png', bbox_inches='tight')
    plt.close
    
    #plot animal interaction
    #animal interaction - how many (%) answered the question and checked
    survey_AIcols = ['AnimalsY','AnimalsN']
    lite_AIcols = ['Animal Interaction - No',
               'Animal Interaction - Chew Marks','Animal Interaction - Death']
    
    AI_survey = survey[survey_AIcols].notna().any(axis=1).sum()
    AI_lite = lite[lite_AIcols].any(axis=1).sum()
    
    AI_subs = [AI_survey, AI_lite]
    subs_tot = sum(AI_subs)
    survey_AI = survey['AnimalsY'].value_counts().get('Yes', 0)
    lite_AI = (lite['Animal Interaction - Chew Marks'] | lite['Animal Interaction - Death']).sum()
    AI_yes = [survey_AI, lite_AI]
    AI_tot = sum(AI_yes)
    
#percent submissions reporting AI observed
    perc_AI = (AI_tot/subs_tot)*100
    
    survey['AIDeath'] = survey['AIDeath'].replace(['X', 'x'], 1)
    survey['AIDeath'] = pd.to_numeric(survey['AIDeath'], errors='coerce')
    
    deaths = []
    death_survey = survey['AIDeath'].sum()
    deaths.append(death_survey)

    lite_death = lite['Animal Interaction - Death'].sum()
    deaths.append(lite_death)
    
    tot_deaths = sum(deaths)
    subs_for_death = [AI_survey, AI_lite]
    death_subs_tot = sum(subs_for_death)
#percent submissions reporting death of those reporting they checked for AI  
    perc_death = (tot_deaths/death_subs_tot)*100
        
    #preparing for the pie chart
    not_AI = 100 - perc_AI
    AI_remaining = perc_AI - perc_death
    AI_death = perc_death

    sizes = [not_AI, AI_remaining, AI_death]
    labels = ['No observed animal interaction', 'Animal Interaction', 'Evidence of Death']

    colors = ['#80DCB5', '#00945C', '#00945C']
    
    afont = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 10}


    fig, ax = plt.subplots(figsize=(6, 6))

    wedges, texts, autotexts = ax.pie(
        sizes, 
        labels=labels, 
        colors=colors, 
        autopct='%1.1f%%', 
        startangle=90, 
        counterclock=False,
        textprops=dict(color='#80DCB5', **afont),
        wedgeprops=dict(edgecolor='white', linewidth=2) 
        )


    wedges[2].set_hatch('////') 

    autotexts[1].set_text(f"{perc_AI:.1f}%")
    autotexts[0].set_color('#1A202C') #paler
    autotexts[1].set_color('black')    # Main AI total text
    autotexts[1].set_fontweight('bold')
    autotexts[2].set_color('black')    # Death subset text
    autotexts[2].set_fontweight('bold')


    ax.set_title("Animal Interaction with Single-use Pollution", fontsize=15, fontweight='bold', color='#1A202C', pad=20)

    plt.tight_layout()
    plt.savefig(folderout + 'AI_pie_chart.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close
    
    #plot nature connection and perma score
    df = experience
    counts = df['Experience_NatureConnect'].value_counts().sort_index()

    color_0 = "#508591"    # A-Team blue (0 - All the other color)
    color_5 = "#F1F5F9"    # Pale Slate/Gray (5 - Neutral/Pale center)
    color_10 = "#00945C"   # Emergence Green (10 - All Green)

    # Create two smooth gradients meeting perfectly at 5
    cmap_low = mcolors.LinearSegmentedColormap.from_list("low", [color_0, color_5])
    cmap_high = mcolors.LinearSegmentedColormap.from_list("high", [color_5, color_10])

 
    colors = []
    for i in range(11):
        if i <= 5:
            colors.append(cmap_low(i / 5.0))       # Maps 0 -> 5
        else:
            colors.append(cmap_high((i - 5) / 5.0)) # Maps 5 -> 10

    #counts_filtered = counts[counts > 0]
    colors_filtered = [colors[int(i)] for i in counts.index]
    labels = [f"Score {int(i)}" for i in counts.index]

    #Plot the pie chart
    fig, ax = plt.subplots(figsize=(8, 8))

    wedges, texts, autotexts = ax.pie(
        counts,
        labels=labels,
        colors=colors_filtered,
        autopct='%1.1f%%',
        startangle=140,
        counterclock=False,
        textprops=dict(color='#4A5568', **afont),
        wedgeprops=dict(edgecolor='white', linewidth=2)  # Sharp white borders between slices
        )

# 5. Dynamically adjust text color inside slices for contrast/readability
    for i, autotext in enumerate(autotexts):
        score_value = counts.index[i]
    # Use white text for the very dark slices (0, 1, 10), dark text for pale slices
        if score_value <= 1 or score_value == 10:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        else:
            autotext.set_color('#1E293B')

# Title styling
    ax.set_title("Nature Connection Scores", **tfont, pad=20)

    plt.tight_layout()
    plt.savefig(folderout + 'nature_connection.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close
    
    
    
    #perma_score
    df = df.dropna(subset=['perma_score'])
    df['perma_score'] = df['perma_score'].round(0).astype(int)
    counts = df['perma_score'].value_counts().sort_index()

    color_0 = "#508591"    # A-Team blue (0 - All the other color)
    color_5 = "#F1F5F9"    # Pale Slate/Gray (5 - Neutral/Pale center)
    color_10 = "#00945C"   # Emergence Green (10 - All Green)

    # Create two smooth gradients meeting perfectly at 5
    cmap_low = mcolors.LinearSegmentedColormap.from_list("low", [color_0, color_5])
    cmap_high = mcolors.LinearSegmentedColormap.from_list("high", [color_5, color_10])

 
    colors = []
    for i in range(11):
        if i <= 5:
            colors.append(cmap_low(i / 5.0))       # Maps 0 -> 5
        else:
            colors.append(cmap_high((i - 5) / 5.0)) # Maps 5 -> 10

    #counts_filtered = counts[counts > 0]
    colors_filtered = [colors[int(i)] for i in counts.index]
    labels = [f"Score {int(i)}" for i in counts.index]

    #Plot the pie chart
    fig, ax = plt.subplots(figsize=(8, 8))

    wedges, texts, autotexts = ax.pie(
        counts,
        labels=labels,
        colors=colors_filtered,
        autopct='%1.1f%%',
        startangle=140,
        counterclock=False,
        textprops=dict(color='#4A5568', **afont),
        wedgeprops=dict(edgecolor='white', linewidth=2)  # Sharp white borders between slices
        )

# 5. Dynamically adjust text color inside slices for contrast/readability
    for i, autotext in enumerate(autotexts):
        score_value = counts.index[i]
    # Use white text for the very dark slices (0, 1, 10), dark text for pale slices
        if score_value <= 1 or score_value == 10:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        else:
            autotext.set_color('#1E293B')

# Title styling
    ax.set_title("Well-being Scores \n Called a PERMA score, calculated from 5 of the experience responses \n ranking from 0 - lowest score to 10 - highest score", **tfont, pad=20)

    bg_color = '#00945C' 

    fig.patch.set_facecolor(bg_color)  # Changes the whole image background
    ax.set_facecolor(bg_color)   # Changes the background behind the pie chart
    
    plt.tight_layout()
    plt.savefig(folderout + 'well_being2.png', 
                dpi=300, 
                bbox_inches='tight', 
                facecolor=fig.get_facecolor(), 
                edgecolor='none'
                )
    
def TFT_stats_and_graphs(folderin, folderout):
    """
    A function which takes all time TFT data and produces graphs to match Monster graphics
    
    Parameters
    ----------
    
    folderin: string
             path to input folder with csv files with monthly TFT data
            
    folderout: string
           path for folder to save results in
    """

    
    #create df for results - or could read in and append to overall stats sheet
    results = pd.DataFrame(columns = ['no_people','distance_km','duration_hours', 
                                      'total_items'
                                      ])
    
    lite_dt = pd.read_csv(folderin + 'other_averages_calc.csv',
                          index_col=0).iloc[:, 0]
    lite_dict = lite_dt.to_dict()  
    
    survey = pd.read_csv(folderin + 'survey/all_survey.csv')
    lite = pd.read_csv(folderin + 'lite/all_lite.csv')
    experience = pd.read_csv(folderin + 'experience/all_experience.csv')
  
    count_lite = len(lite.index)

        
    #Overview - volunteers, distance, hours, items
    mins = survey['Time_min']
    hours = []
    for m in mins:
        hour = m/60
        hours.append(hour)
        
    survey['Time_hours'] = hours    
    
    tot_people = []
    tot_time = []
    
    minutes = lite_dict['Time_min']
    time = minutes/60

    survey['Time_hours'] = survey['Time_hours'].replace(0, time).fillna(time)
    survey['People'] = survey['People'].replace(0, lite_dict['People']).fillna(lite_dict['People'])
    
    people = survey['People'].sum()
    hours = (survey['People'] * survey['Time_hours']).sum()

    tot_people.append(people)
    tot_time.append(hours)

    #add to total people the number of lite and count submissions
    lite_people = count_lite * lite_dict['People']
    tot_people.append(lite_people)

     
    #volunteers
    total_people = sum(tot_people)
    
    survey_km = survey['Distance_km'].sum()
    lite_km = count_lite * lite_dict['Distance_km']
      
    kms = [survey_km, lite_km]
    #distance cleaned / surveyed 
    km = sum(kms)
        
    #method to estimate time spent on count
    lite_time = count_lite * time
    tot_time.append(lite_time)
    #time 
    total_time = sum(tot_time) 

    all_items = ['Value Full Dog Poo Bags',
    'Value Unused Dog Poo Bags','Value Other Pet Related Stuff',
    'Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
    'Value Aluminium soft drink cans',
    'Value Glass soft drink bottles','Value Milkshake bottle or carton',
    'Value Plastic energy drink bottles',
    'Value Aluminium energy drink can','Value Plastic energy gel sachet',
    'Value Plastic energy gel end',
    'Value Protein drink bottle or carton', 'Value Aluminium alcoholic drink cans',
    'Value Glass alcoholic bottles','Value Hot drinks cups',
    'Value Hot drinks tops and stirrers',
    'Value Cold drinks cups and tops','Value Cartons','Value Plastic straws',
    'Value Paper straws',
    'Value Plastic bottle, top', 'Value Glass bottle tops', 'Value Ring pull', 
    'Value Plastic bottle sleeve',
    'Value Reusable drinks container','Value Other drink related',
    'Value Confectionary/sweet wrappers','Value Wrapper "corners" / tear-offs',
    'Value Other confectionary (eg., Lollipop Sticks)',
    'Value Crisps Packets','Value Used Chewing Gum','Value Homemade lunch (eg., aluminium foil, cling film)',
    'Value BBQ related','Value Fruit peel & cores','Value Branded single-use carrier bags',
    'Value Unbranded single-use carrier bags', 'Value Branded bag for life',
    'Value Unbranded bag for life', 
    'Value Branded plastic fast / takeaway food packaging / utensils',
    'Value Unbranded plastic fast / takeaway food packaging / utensils',
    'Value Branded card or wood fast / takeaway food packaging / utensils',
    'Value Unbranded card or wood fast / takeaway food packaging / utensils',
    'Value Branded condiments packaging','Value Unbranded condiments packaging',
    'Value Branded food on the go','Value Unbranded food on the go',
    'Value Branded other food related','Value Unbranded other food related',
    'Value Clothes & Footwear','Value Textiles','Value Plastic milk bottles',
    'Value Glass milk bottles',
    'Value Plastic food containers','Value Cardboard food containers',
    'Value Cleaning products containers',
    'Value Cosmetics / deodorants', 'Value Other household',
    'Value Cigarette Butts','Value Nicotine pouches','Value Disposable vapes',
    'Value Nicotine related packaging','Value Other nicotine related',
    'Value Unbagged dog poo',
    'Value Needles / syringes','Value Other drug related','Value Broken glass or pottery',
    'Value Toilet tissue','Value Face/ baby wipes','Value Nappies','Value Period products',
    'Value Covid Masks','Value First Aid & medcal waste','Value Batteries and electronics',
    'Value Other hazardous', 'Value Camping','Value Fireworks','Value Seasonal (Christmas and/or Easter)',
    'Value Rubber balloons','Value Foil balloons','Value Outdoor event related (e.g.race)',
    'Value Biking specific','Value Hiking specific','Value Other outdoor related',
    'Value Farming','Value Forestry','Value Industrial','Value Cable ties',
    'Value Miscellaneous hard plastic','Value Miscellaneous soft plastic',
    'Value Miscellaneous card or wood','Value Miscellaneous metal',
    'Value Too small/dirty to ID','Value Other Miscellaneous']
    
    #Resolve nan issues
    survey[all_items] = survey[all_items].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

    rmv_items = [] 

    survey_items = survey['TotItems'].sum()   
    rmv_items.append(survey_items)

    lite_items = lite['TotItems'].sum() 
    rmv_items.append(lite_items)
      
    total_items = sum(rmv_items)
    
    new_row = pd.DataFrame([{'no_people':total_people, 'distance_km':km,
                              'duration_hours':total_time, 'total_items':total_items
                              }])
    
    results= pd.concat([results, new_row], ignore_index=True) 
                                        
    
    results.to_csv(folderout + '/overview.csv',index=False)  

    #plot DRS items
    DRS = ['Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
    'Value Aluminium soft drink cans', 'Value Glass soft drink bottles',
    'Value Plastic energy drink bottles','Value Aluminium energy drink can',
    'Value Aluminium alcoholic drink cans','Value Glass alcoholic bottles',
    'Value Glass soft drink bottles','Value Glass alcoholic bottles'
    ] 

    df = survey 
    
    df['DRS_sum'] = df[DRS].sum(axis=1)

    #df_sorted = df.sort_values(by='TotItems', ascending=False)

    #fig, ax = plt.subplots(figsize=(10, 6))

    #ax.bar(df_sorted['TrailName'], df_sorted['TotItems'], color='#80DCB5', label='Other Items')
    #ax.bar(df_sorted['TrailName'], df_sorted['DRS_sum'], color='#00945C', label='DRS Items')
  
    
    afont = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 12}
    
    tfont = {'family' : 'sans-serif',
        'weight' : 'bold',
        'size'   : 18}

    #ax.set_ylabel('Total Items', **afont)
    #ax.set_xlabel('Location', **afont)
    #ax.set_title('Items per Trail Breakdown', **tfont, pad=15)
    #ax.legend()

    # Rotate x-axis labels to prevent overlapping
    plt.xticks(rotation=45, ha='right')

    plt.savefig(folderout + '/total_items.png', bbox_inches='tight')
    plt.close
  
    #plot brands
    brands = ['Lucozade', 'Ribena','RedBull','Monster','High5','SIS','Danone',
              'Highland Spring','Coke','Costa','Pepsi','Walkers','Barrs',
              'Britvic','Mars','Nestle','Mondelez','Cadbury','Magnum','Haribo',
              'AB InBev','Corona','Molson Corrs','Thatchers','Heineken',
              'Fosters','Bulmers','Carlsberg','Burger King','Greggs','KFC',
              'McDonalds','Subway','Aldi','Co-op','Euro Shopper','LiDL',
              'M&S','Tesco']  

    brand_totals = df[brands].apply(pd.to_numeric, errors='coerce').sum()
    brand_totals = brand_totals.sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar(brand_totals.index, brand_totals.values, color='#00945C', edgecolor='black')

    ax.set_xlabel('Brands', **afont)
    ax.set_ylabel('Total', **afont)
    ax.set_title('Total Sum per Brand', **tfont, pad=15)

    plt.xticks(rotation=45, ha='right')

    plt.savefig(folderout + '/brands.png', bbox_inches='tight')
    plt.close
    
    #plot animal interaction
    #animal interaction - how many (%) answered the question and checked
    survey_AIcols = ['AnimalsY','AnimalsN']
    lite_AIcols = ['Animal Interaction - No',
               'Animal Interaction - Chew Marks','Animal Interaction - Death']
    
    AI_survey = survey[survey_AIcols].notna().any(axis=1).sum()
    AI_lite = lite[lite_AIcols].any(axis=1).sum()
    
    AI_subs = [AI_survey, AI_lite]
    subs_tot = sum(AI_subs)
    survey_AI = survey['AnimalsY'].value_counts().get('Yes', 0)
    lite_AI = (lite['Animal Interaction - Chew Marks'] | lite['Animal Interaction - Death']).sum()
    AI_yes = [survey_AI, lite_AI]
    AI_tot = sum(AI_yes)
    
    #percent submissions reporting AI observed
    perc_AI = (AI_tot/subs_tot)*100
    
    survey['AIDeath'] = survey['AIDeath'].replace(['X', 'x'], 1)
    survey['AIDeath'] = pd.to_numeric(survey['AIDeath'], errors='coerce')
    
    deaths = []
    death_survey = survey['AIDeath'].sum()
    deaths.append(death_survey)
    
    lite_death = lite['Animal Interaction - Death'].sum()
    deaths.append(lite_death)
    
    tot_deaths = sum(deaths)
    subs_for_death = [AI_survey, AI_lite]
    death_subs_tot = sum(subs_for_death)
    #percent submissions reporting death of those reporting they checked for AI  
    perc_death = (tot_deaths/death_subs_tot)*100
        
    #preparing for the pie chart
    not_AI = 100 - perc_AI
    AI_remaining = perc_AI - perc_death
    AI_death = perc_death
    
    sizes = [not_AI, AI_remaining, AI_death]
    labels = ['No observed animal interaction', 'Animal Interaction', 'Evidence of Death']
    
    colors = ['#80DCB5', '#00945C', '#00945C']
    
    afont = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 10}
    
    
    fig, ax = plt.subplots(figsize=(6, 6))
    
    wedges, texts, autotexts = ax.pie(
        sizes, 
        labels=labels, 
        colors=colors, 
        autopct='%1.1f%%', 
        startangle=90, 
        counterclock=False,
        textprops=dict(color='#80DCB5', **afont),
        wedgeprops=dict(edgecolor='white', linewidth=2) 
        )
    
    
    wedges[2].set_hatch('////') 
    
    autotexts[1].set_text(f"{perc_AI:.1f}%")
    autotexts[0].set_color('#1A202C') #paler
    autotexts[1].set_color('black')    # Main AI total text
    autotexts[1].set_fontweight('bold')
    autotexts[2].set_color('black')    # Death subset text
    autotexts[2].set_fontweight('bold')
    
    
    ax.set_title("Animal Interaction with Single-use Pollution", fontsize=15, fontweight='bold', color='#1A202C', pad=20)
    
    plt.tight_layout()
    plt.savefig(folderout + 'AI_pie_chart.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close
    
    #plot nature connection and perma score
    df = experience
    counts = df['Experience_NatureConnect'].value_counts().sort_index()
    
    color_0 = "#508591"    # A-Team blue (0 - All the other color)
    color_5 = "#F1F5F9"    # Pale Slate/Gray (5 - Neutral/Pale center)
    color_10 = "#00945C"   # Emergence Green (10 - All Green)
    
    # Create two smooth gradients meeting perfectly at 5
    cmap_low = mcolors.LinearSegmentedColormap.from_list("low", [color_0, color_5])
    cmap_high = mcolors.LinearSegmentedColormap.from_list("high", [color_5, color_10])
    
     
    colors = []
    for i in range(11):
        if i <= 5:
            colors.append(cmap_low(i / 5.0))       # Maps 0 -> 5
        else:
            colors.append(cmap_high((i - 5) / 5.0)) # Maps 5 -> 10
    
    #counts_filtered = counts[counts > 0]
    colors_filtered = [colors[int(i)] for i in counts.index]
    labels = [f"Score {int(i)}" for i in counts.index]
    
    #Plot the pie chart
    fig, ax = plt.subplots(figsize=(8, 8))
    
    wedges, texts, autotexts = ax.pie(
        counts,
        labels=labels,
        colors=colors_filtered,
        autopct='%1.1f%%',
        startangle=140,
        counterclock=False,
        textprops=dict(color='#4A5568', **afont),
        wedgeprops=dict(edgecolor='white', linewidth=2)  # Sharp white borders between slices
        )
    
    # 5. Dynamically adjust text color inside slices for contrast/readability
    for i, autotext in enumerate(autotexts):
        score_value = counts.index[i]
    # Use white text for the very dark slices (0, 1, 10), dark text for pale slices
        if score_value <= 1 or score_value == 10:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        else:
            autotext.set_color('#1E293B')
    
    # Title styling
    ax.set_title("Nature Connection Scores", **tfont, pad=20)
    
    plt.tight_layout()
    plt.savefig(folderout + 'nature_connection.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close
    
    
    
    #perma_score
    df = df.dropna(subset=['perma_score'])
    df['perma_score2'] = df['perma_score'].round(0).astype(int)
    counts = df['perma_score'].value_counts().sort_index()
    
    color_0 = "#508591"    # A-Team blue (0 - All the other color)
    color_5 = "#F1F5F9"    # Pale Slate/Gray (5 - Neutral/Pale center)
    color_10 = "#00945C"   # Emergence Green (10 - All Green)
    
    # Create two smooth gradients meeting perfectly at 5
    cmap_low = mcolors.LinearSegmentedColormap.from_list("low", [color_0, color_5])
    cmap_high = mcolors.LinearSegmentedColormap.from_list("high", [color_5, color_10])
    
     
    colors = []
    for i in range(11):
        if i <= 5:
            colors.append(cmap_low(i / 5.0))       # Maps 0 -> 5
        else:
            colors.append(cmap_high((i - 5) / 5.0)) # Maps 5 -> 10
    
    #counts_filtered = counts[counts > 0]
    colors_filtered = [colors[int(i)] for i in counts.index]
    labels = [f"Score {int(i)}" for i in counts.index]
    
    #Plot the pie chart
    fig, ax = plt.subplots(figsize=(8, 8))
    
    wedges, texts, autotexts = ax.pie(
        counts,
        labels=labels,
        colors=colors_filtered,
        autopct='%1.1f%%',
        startangle=140,
        counterclock=False,
        textprops=dict(color='#4A5568', **afont),
        wedgeprops=dict(edgecolor='white', linewidth=2)  # Sharp white borders between slices
        )
    
    # 5. Dynamically adjust text color inside slices for contrast/readability
    for i, autotext in enumerate(autotexts):
        score_value = counts.index[i]
    # Use white text for the very dark slices (0, 1, 10), dark text for pale slices
        if score_value <= 1 or score_value == 10:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        else:
            autotext.set_color('#1E293B')
    
    # Title styling
    ax.set_title("Well-being Scores \n Called a PERMA score, calculated from 5 of the experience responses \n ranking from 0 - lowest score to 10 - highest score", **tfont, pad=20)
    
    bg_color = '#00945C' 
    
    fig.patch.set_facecolor(bg_color)  # Changes the whole image background
    ax.set_facecolor(bg_color)   # Changes the background behind the pie chart
    
    plt.tight_layout()
    plt.savefig(folderout + 'well_being2.png', 
                dpi=300, 
                bbox_inches='tight', 
                facecolor=fig.get_facecolor(), 
                edgecolor='none'
                )
    
    
    
    




























    
