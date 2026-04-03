#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 14:15:04 2026

@author: heatherkay
"""

import pandas as pd
import re
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
        'EthnicOther','IllnessY','IllnessN','IllnessPreferNot']


    #rename columns
    df.columns=cols
    #remove row with extra column names that aren't now needed
    df_clean = df.drop(index=0)
    
    df = df.drop('Rando Q', axis=1)
    
    
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
    'Experience_Knowledge10']
  
    df_clean[exp_cols] = df_clean[exp_cols].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)
    for i in range(0, len(exp_cols), 11):
        group = exp_cols[i : i + 11]
        new_col_name = group[0][:-1] 
        df_clean[new_col_name] = df_clean[group].idxmax(axis=1).str.extract(r'(\d+)$').astype(int)
        df_clean.drop(columns=group, inplace=True) 
    
    
    #remove sensitive data for U18s
    cols_to_clear = ['Experience_Feeling1', 'Experience_Feeling2',
        'Experience_Feeling3','Experience_+veFeeling','Experience_Engagement',
        'Experience_Relationships','Experience_Meaning','Experience_Accomplishment',
        'Experience_Health','Experience_NatureConnect','Experience_Knowledge',
        'GenderFemale','GenderMale','GenderNon-binary','GenderTransgender',
        'GenderPreferNot','GenderOther','HomePostcode','EthnicAfrican',
        'EthnicArab','EthnicAsian','EthinicLatino','EthnicCaucasian','EthinicPreferNot',
        'EthnicOther','IllnessY','IllnessN','IllnessPreferNot']

    df_clean.loc[df_clean['AgeU18'].notna(), cols_to_clear] = None
        

    
    #change data in presence(composition) data to TRUE
    change_cols = ['Handful','Pocketful','Bread bag',
            'Carrier bag', 'Bin bag', 'Full Dog Poo Bags','Unused Dog Poo Bags',
            'Other Pet Related Stuff',
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
            'Branded food on the go','Unbranded food on the go',
            'Branded other food related','Unbranded other food related',
            'Clothes & Footwear','Textiles','Plastic milk bottles','Glass milk bottles',
            'Plastic food containers','Cardboard food containers','Cleaning products containers',
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
            'Too small/dirty to ID','Other Miscellaneous']

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
    
    email_ref_df = pd.read_csv(TFTin + 'email_reference.csv', encoding='cp1252')  
    
    df3['Email'] = (df3['Email'].str.strip().str.lower())
    new_emails = df3[~df3['Email'].isin(email_ref_df['email'])]['Email'].dropna().unique()
    
    if len(new_emails) > 0:
        current_max_id = email_ref_df['email_id'].max()
    
        new_rows = pd.DataFrame({
            'email': new_emails,
            'email_id': range(current_max_id + 1, current_max_id + 1 + len(new_emails))
            })

        email_ref_df = pd.concat([email_ref_df, new_rows], ignore_index=True)
    
        email_ref_df.to_csv(TFTin + 'email_reference.csv', index=False)
        
    df3 = df3.merge(email_ref_df, left_on='Email', right_on='email', how='left')
    
    df3.drop(columns=['Email'], inplace=True)
    df3.drop(columns=['email'], inplace=True)
    
    #reorder so experience cols are together
    cols = list(range(df3.shape[1]))
    target_block = cols[348:357]
    remaining_cols = [c for c in cols if c not in target_block]
    new_order = remaining_cols[:302] + target_block + remaining_cols[302:]
    df3 = df3.iloc[:, new_order]
             
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
        'FirstName','LastName','Email','phone','Receive_email','SMS']
    
    
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
    
    email_ref_df = pd.read_csv(TFTin + 'email_reference.csv')  
    
    df3['Email'] = (df3['Email'].str.strip().str.lower())
    new_emails = df3[~df3['Email'].isin(email_ref_df['email'])]['Email'].dropna().unique()
    
    if len(new_emails) > 0:
        current_max_id = email_ref_df['email_id'].max()
    
        new_rows = pd.DataFrame({
            'email': new_emails,
            'email_id': range(current_max_id + 1, current_max_id + 1 + len(new_emails))
            })

        email_ref_df = pd.concat([email_ref_df, new_rows], ignore_index=True)
    
        email_ref_df.to_csv(TFTin + 'email_reference.csv', index=False)
        
    df3 = df3.merge(email_ref_df, left_on='Email', right_on='email', how='left')
    
    df3.drop(columns=['Email'], inplace=True)
    df3.drop(columns=['email'], inplace=True)
    df3.drop(columns=['phone'], inplace=True)
            
    df3.to_csv(TFTout + 'count.csv', index=False)
    
def update_lite_averages(year_folder, TFTout):
    """
    A function which takes the bag averages data and the survey data, it uses the 
    survey data to update the averages (whilst ignoring outliers) and then writes out 
    an averages .csv to read into lite_clean_data and an updated averages.csv
    
    Parameters
    ----------
    
    TFTout: string
            path to folder with input csv files with cleaned raw monthly data
            
    yearin: string
            path to folder with input csv files with cleaned raw yearly data and
            for output files 
             
    """
    
    bag_df = pd.read_csv(year_folder + 'bag_averages_raw.csv')
    survey = pd.read_csv(TFTout + 'survey.csv')


    bag_types = ['Handful', 'Pocketful', 'Bread bag', 'Carrier bag', 'Bin bag']

    # make a copy so we don't modify df directly
    df_updated = bag_df.copy()

    for _, row in survey.iterrows():
        # Identify which column is filled
        for col in ['Handful', 'Pocketful', 'Bread bag', 'Carrier bag', 'Bin bag', 'Multiple Bin Bags']:
            val = row[col]
            if pd.notna(val) and (val is True or isinstance(val, (int, float))):
                
                # Determine bag type and items per bag
                if col == 'Multiple Bin Bags':
                    bag_type = 'Bin bag'
                    tot_per_bag = row['TotItems'] / val  # divide by number of bags
                else:
                    bag_type = col
                    tot_per_bag = row['TotItems']

                # Get outlier limits using IQR
                series = df_updated[bag_type].dropna()
                if len(series) >= 4:  # need enough data to get quartiles
                    Q1 = series.quantile(0.25)
                    Q3 = series.quantile(0.75)
                    IQR = Q3 - Q1
                    lower = Q1 - 1.5 * IQR
                    upper = Q3 + 1.5 * IQR
                else:
                    # if too few data points, skip outlier filtering
                    lower, upper = -float("inf"), float("inf")

                # Append if within range
                if lower <= tot_per_bag <= upper:
                    # Append to df (add a new row with only that column filled)
                    new_row = {c: None for c in bag_types}
                    new_row[bag_type] = tot_per_bag
                    df_updated = pd.concat([df_updated, pd.DataFrame([new_row])], ignore_index=True)
                break  # only one type per row

    for col in bag_types:
        df_updated[col] = pd.to_numeric(df_updated[col], errors='coerce')

    # Now compute numeric mean
    averages = df_updated.mean(numeric_only=True)
    averages_df = averages.reset_index()
    averages_df.columns = ['bag', 'avg_items']

    # Clean bag names if needed
    averages_df['bag'] = averages_df['bag'].str.lower().str.replace(' ', '')
    
    binbag_avg = averages_df.loc[averages_df['bag'] == 'binbag', 'avg_items'].values[0]
    averages_df = pd.concat([averages_df, pd.DataFrame([{'bag': 'multiplebinbags', 
                'avg_items': binbag_avg}])], ignore_index=True)

    averages_df.to_csv(year_folder + 'bag_averages_calc.csv', index=False)
    df_updated.to_csv(year_folder + 'bag_averages_raw.csv', index=False)

    #now for people, distance and time
    other_df = pd.read_csv(year_folder + 'other_averages_raw.csv') 
    av_df = survey[['People', 'Time_min', 'Distance_km']].copy()
    av_df = av_df[av_df['People'] < 7]
    
    dfs=[other_df, av_df]
    new_averages_df = pd.concat(dfs, ignore_index=True)
    
    av = new_averages_df.mean(numeric_only=True)
    av.to_csv(year_folder + 'other_averages_calc.csv')
    new_averages_df.to_csv(year_folder + 'other_averages_raw.csv')
    
    av.to_csv(TFTout + 'other_averages_calc.csv')
    averages_df.to_csv(TFTout + 'bag_averages_calc.csv', index=False)
    
        
    
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
        for bag, col in bag_column_map.items():
            if row[col] == True:
                avg_items = avg_map.get(bag, 0)
                num_bags = row['How many bags?'] if (bag == 'multiplebinbags' and not pd.isna(row['How many bags?'])) else 1
                return num_bags * avg_items
        return 0

    df['TotItems'] = df.apply(get_tot_items, axis=1)

    email_ref_df = pd.read_csv(TFTin + 'email_reference.csv')  
    
    df['Email'] = (df['Email'].str.strip().str.lower())
    new_emails = df[~df['Email'].isin(email_ref_df['email'])]['Email'].dropna().unique()
    
    if len(new_emails) > 0:
        current_max_id = email_ref_df['email_id'].max()
    
        new_rows = pd.DataFrame({
            'email': new_emails,
            'email_id': range(current_max_id + 1, current_max_id + 1 + len(new_emails))
            })

        email_ref_df = pd.concat([email_ref_df, new_rows], ignore_index=True)
    
        email_ref_df.to_csv(TFTin + 'email_reference.csv', index=False)
        
    df = df.merge(email_ref_df, left_on='Email', right_on='email', how='left')
    
    df.drop(columns=['Email'], inplace=True)
    df.drop(columns=['email'], inplace=True)

    
    # Save cleaned version with TotItems and email_id
    df.to_csv(os.path.join(TFTout, 'lite.csv'), index=False)

    # --- 4. Compute totals using TotItems ---
    results = []
    for bag, col in bag_column_map.items():
        df_subset = df[df[col] == True]
        tot_items = df_subset['TotItems'].sum()
        tot_bags = df_subset['How many bags?'].fillna(1).sum() if bag == 'multiplebinbags' else len(df_subset)
    
        results.append({'bag': bag, 'TotItems': tot_items, 'no. of bags': tot_bags})

    # --- 5. Save results ---
    results_df = pd.DataFrame(results)
    results_df.to_csv(os.path.join(TFTout, 'bag_res_lite.csv'), index=False)

    
    
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
    


def TFRaces_clean_data_v1(TFTin, TFTout):
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
        'Merch_steelmarker', 'Merch_NCcards + tin', 'Merch_NCcards no tin',
        'survey', 'count', 'TotItems', 'include_Y', 'include_N',
        'include_some', 'Item1', 'Item2', 'Item3', 'Item4', 'Item5', 'Item1_Quantity', 
        'Item2_Quantity', 'Item3_Quantity', 'Item4_Quantity', 'Item5_Quantity', 
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
    

    
def add_to_existing_data(TFTout, year_folder):
    """
    A function which takes the prepared monthly TFT data and adds it to the 
    correct yearly file
    
    Parameters
    ----------
    
    TFTout: string
            path to folder with input csv files with cleaned raw monthly data
            
    yearin: string
            path to folder with input csv files with cleaned raw yearly data and
            for output files 
             
    """

    forms = ['count', 'survey', 'CS_count', 'CS_survey', 'lite', 'TFR']
    #read csv file
    for file in forms:
        df_month = pd.read_csv(TFTout + file + '.csv')   
        df_year = pd.read_csv(year_folder + file + '/' + file + '_2026.csv')
        df_all_time = pd.read_csv(year_folder + file + '/all_' + file + '.csv')
        dfs = (df_month, df_year)
        alltime = (df_month, df_all_time)
        df_final = pd.concat(dfs, ignore_index = True) 
        df_alltime = pd.concat(alltime, ignore_index = True) 
        df_final.to_csv(year_folder + file + '/' + file + '_2026.csv', index=False) 
        df_alltime.to_csv(year_folder + file + '/all_' + file + '.csv', index=False)
        
    bag_res = pd.read_csv(TFTout + 'bag_res_lite.csv') 
    y_bag_res = pd.read_csv(year_folder + 'lite/bag_res_lite_2026.csv')
    all_bagres = pd.read_csv(year_folder + 'lite/all_bag_res_lite.csv')
    dfs = [bag_res, y_bag_res]
    alltime = [bag_res, all_bagres]
    bag_res_dfy = pd.concat(dfs, ignore_index = True) 
    df_alltime = pd.concat(alltime, ignore_index = True) 
    bag_res_dfy.to_csv(year_folder + 'lite/bag_res_lite_2026.csv', index=False) 
    df_alltime.to_csv(year_folder + 'lite/all_bag_res_lite.csv', index=False)
    
        
        
        
    
