#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 15:42:35 2026

@author: heatherkay
"""


import pandas as pd
import numpy as np

def sorting_dfs(TFTin, TFTout):
    """
    A function which takes the pre-2026 survey data and adjust the columns to
    match the 2026 updated data
    
    Parameters
    ----------
             
    TFTin: string
            path to input csv file with original TFT data 
             
            
    TFTout: string
            path to output file with updated TFT data
    """

    df = pd.read_csv(TFTin)

    # Booleans
    pet_cols = ['Toys (eg., tennis balls)', 'Other Pet Related Stuff']
    pet_combined = df[pet_cols].any(axis=1).replace(False, np.nan)

    drink_cols = ['Drinks cups (eg., McDonalds drinks)', 'Drinks tops (eg., McDonalds drinks)']
    drink_combined = df[drink_cols].any(axis=1).replace(False, np.nan)

    bbq_cols = ['Disposable BBQs and / or BBQ related items', 'BBQs and / or BBQ related items']
    bbq_combined = df[bbq_cols].any(axis=1).replace(False, np.nan)

    smoke_cols = ['Smoking related', 'Vaping / E-Cigarette Paraphernalia']
    smoke_combined = df[smoke_cols].any(axis=1).replace(False, np.nan)

    farm_cols = ['Farming','Salt/mineral lick buckets','Silage wrap']
    farm_combined = df[farm_cols].any(axis=1).replace(False, np.nan)
    
    woods_cols = ['Forestry','Tree guards']
    woods_combined = df[woods_cols].any(axis=1).replace(False, np.nan)

    ind_cols = ['Industrial','Industrial plastic wrap']
    ind_combined = df[ind_cols].any(axis=1).replace(False, np.nan)

    out_cols = ['Running','Roaming and other outdoor related (e.g. climbing, kayaking)']
    out_combined = df[out_cols].any(axis=1).replace(False, np.nan)

    event_cols = ['Outdoor event (eg Festival)','Outdoor sports event related (e.g.race)']
    event_combined = df[event_cols].any(axis=1).replace(False, np.nan)
    
    misc_cols = ['Miscellaneous','Weird/Retro']
    misc_combined = df[misc_cols].any(axis=1).replace(False, np.nan)
  
    
  
    # Summing cols
    pet_val_cols = ['Value Toys (eg., tennis balls)', 'Value Other Pet Related Stuff']
    pet_sum = df[pet_val_cols].sum(axis=1)

    drink_val_cols = ['Value Drinks cups (eg., McDonalds drinks)', 'Value Drinks tops (eg., McDonalds drinks)']
    drink_sum = df[drink_val_cols].sum(axis=1)
    
    bbq_val_cols = ['Value Disposable BBQs and / or BBQ related items', 'Value BBQs and / or BBQ related items']
    bbq_sum = df[bbq_val_cols].sum(axis=1)

    smoke_val_cols = ['Value Smoking related', 'Value Vaping / E-Cigarette Paraphernalia']
    smoke_sum = df[smoke_val_cols].sum(axis=1)

    farm_val_cols = ['Value Farming','Value Salt/mineral lick buckets','Value Silage wrap']
    farm_sum = df[farm_val_cols].sum(axis=1)

    woods_val_cols = ['Value Forestry','Value Tree guards']
    woods_sum = df[woods_val_cols].sum(axis=1)
    
    ind_val_cols = ['Value Industrial','Value Industrial plastic wrap']
    ind_sum = df[ind_val_cols].sum(axis=1)

    out_val_cols = ['Value Running','Value Roaming and other outdoor related (e.g. climbing, kayaking)']
    out_sum = df[out_val_cols].sum(axis=1)
    
    event_val_cols = ['Value Outdoor event (eg Festival)','Value Outdoor sports event related (e.g.race)']
    event_sum = df[event_val_cols].sum(axis=1)

    misc_val_cols = ['Value Miscellaneous','Value Weird/Retro']
    misc_sum = df[misc_val_cols].sum(axis=1)   
    
 
    
    #brand colum reshifting
    brand_cols = [c for c in df.columns if c.startswith(('B1_', 'B2_', 'B3_'))]
    unique_brands = set(c.split('_', 1)[1] for c in brand_cols)

    for brand in unique_brands:
        df[brand] = pd.Series(dtype='object')

        for i in [1, 2, 3]:
            col_name = f'B{i}_{brand}'
            if col_name in df.columns:
                mask = df[col_name].notna()
                if brand == 'Other':
                    df.loc[mask, brand] = df.loc[mask, col_name]
                else:
                    df.loc[mask, brand] = f'x{i}'

    df = df.drop(columns=brand_cols)
    
 
    
    #place connection reshifting
    conditions = [df['Connection_ConnectionY'].notna(), 
                  df['Connection_ConnectionN'].notna(),
                  df['Connection_ConnectionSame'].notna()
                  ]

    choices = [10, 0, 5]

    df['Experience_Place'] = np.select(conditions, choices, default=np.nan)



    #Renaming cols
    mapping = {'Plastic carrier bags': 'Branded single-use carrier bags', 
               'Value Plastic carrier bags': 'Value Branded single-use carrier bags',
               'Plastic fast food, takeaway and / or on the go food packaging, cups, cutlery etc':'Branded plastic fast / takeaway food packaging / utensils',
               'Value Plastic fast food, takeaway and / or on the go food packaging, cups, cutlery etc':'Value Branded plastic fast / takeaway food packaging / utensils',
               'Other fast food, takeaway and / or on the go food packaging, cups, cutlery (eg., cardboard)':'Branded card or wood fast / takeaway food packaging / utensils',
               'Value Other fast food, takeaway and / or on the go food packaging, cups, cutlery (eg., cardboard)':'Value Branded card or wood fast / takeaway food packaging / utensils',
               'Food on the go (eg.salad boxes)':'Branded food on the go',
               'Value Food on the go (eg.salad boxes)':'Value Branded food on the go',
               'Drugs related':'Other drug related',
               'Value Drugs related':'Value Other drug related',
               'Single-Use Period products':'Period products',
               'Single-Use Covid Masks':'Covid Masks',
               'Value Single-Use Period products':'Value Period products',
               'Value Single-Use Covid Masks':'Value Covid masks',
               'Rubber/nitrile gloves':'First Aid & medcal waste',
               'Value Rubber/nitrile gloves':'Value First Aid & medcal waste',
               'Halloween & Fireworks':'Fireworks',
               'Value Halloween & Fireworks':'Value Fireworks',
               'Seasonal (Christmas and/or Easter)':'Seasonal (Christmas and/or Easter)',
               'Value Seasonal (Christmas and/or Easter)':'Value Seasonal (Christmas and/or Easter)',
               'Normal balloons':'Rubber balloons',
               'Helium balloons':'Foil balloons',
               'Value Normal balloons':'Value Rubber balloons',
               'Value Helium balloons':'Value Foil balloons',
               'MTB related (e.g. inner tubes, water bottles etc)':'Biking specific',
               'Roaming and other outdoor related (e.g. climbing, kayaking)':'Hiking specific',
               'Value MTB related (e.g. inner tubes, water bottles etc)':'Value Biking specific',
               'Value Roaming and other outdoor related (e.g. climbing, kayaking)':'Value Hiking specific',
               'AnimalsInfo':'AIOther'
               }

    df = df.rename(columns=mapping)
 
    
 
    #Add all the new empty columns
    new_empty_cols = [
        'Ethics', 'FamiliarRegular', 'FamiliarFewTimes', 'FamiliarFirst',
        'WeatherSunny', 'WeatherOvercast', 'WeatherLightRain', 'WeatherHeavyRain',
        'WeatherSnow', 'WeatherWinds', 'WeatherExtremes', 'HabitatCanal',
        'HabitatCoastal', 'HabitatFarm', 'HabitatForest', 'HabitatMarsh',
        'HabitatMoor', 'HabitatMountain', 'HabitatRiver', 'HabitatUrban',
        'Milkshake bottle or carton','Protein drink bottle or carton',
        'Ring pull', 'Plastic bottle sleeve',
        'Reusable drinks container','Other drink related',
        'Unbranded single-use carrier bags', 'Branded bag for life',
        'Unbranded bag for life', 
        'Unbranded plastic fast / takeaway food packaging / utensils',
        'Unbranded card or wood fast / takeaway food packaging / utensils',
        'Branded condiments packaging','Unbranded condiments packaging',
        'Unbranded food on the go','Branded other food related',
        'Unbranded other food related','Cosmetics / deodorants', 'Other household',
        'Nicotine pouches','Nicotine related packaging','Unbagged dog poo',
        'Needles / syringes','broken glass or pottery',
        'batteries and electronics',
        'Other hazardous', 'Other outdoor related','Miscellaneous hard plastic',
        'Miscellaneous soft plastic','Miscellaneous card or wood',
        'Miscellaneous metal','Value Milkshake bottle or carton',
        'Value Protein drink bottle or carton',
        'Value Ring pull', 'Value Plastic bottle sleeve',
        'Value Reusable drinks container','Value Other drink related',
        'Value Unbranded single-use carrier bags', 'Value Branded bag for life',
        'Value Unbranded bag for life', 
        'Value Unbranded plastic fast / takeaway food packaging / utensils',
        'Value Unbranded card or wood fast / takeaway food packaging / utensils',
        'Value Branded condiments packaging','Value Unbranded condiments packaging',
        'Value Unbranded food on the go','Value Branded other food related',
        'Value Unbranded other food related','Value Cosmetics / deodorants',
        'Value Other household','Value Nicotine pouches',
        'Value Nicotine related packaging','Value Unbagged dog poo',
        'Value Needles / syringes','Value broken glass or pottery',
        'Value batteries and electronics',
        'Value Other hazardous', 'Value Other outdoor related',
        'Value Miscellaneous hard plastic',
        'Value Miscellaneous soft plastic','Value Miscellaneous card or wood',
        'Value Miscellaneous metal','Glass milk bottles','Value Glass milk bottles', 
        'Value Broken glass or pottery', 
        'Value Covid Masks', 'Value Batteries and electronics', 
        'Ribena','Danone', 'Highland Spring', 
        'Barrs', 'Britvic','Mondelez', 'High5',
        'Magnum', 'AB InBev', 'Corona', 'Molson Corrs', 
        'Heineken','Bulmers', 'Carlsberg', 'Burger King', 'Greggs',
        'KFC', 'Aldi', 'Co-op', 'Euro Shopper', 'LiDL', 
        'M&S', 'Tesco','AnimalsNotChecked', 'AIDeath', 'AIChew', 
        'AINesting','AItype', 'ExperienceY', 'ExperienceN', 
        'Experience_Feeling1', 'Experience_Feeling2', 'Experience_Feeling3', 
        'Experience_+veFeeling', 'Experience_Engagement', 
        'Experience_Relationships', 'Experience_Meaning', 
        'Experience_Accomplishment', 'Experience_Health', 
        'Experience_NatureConnect', 'Experience_Knowledge', 
        'Connection_RewardY', 'Connection_RewardN', 'Connection_RewardUnsure', 
        'HQ', 'VolunteerWeeks', 'VolunteerMonths', 'VolunteerYears', 
        'WhySubmit', 'Receive emailY', 'Receive emailN', 
        'Receive email_alreadyin', 'DemographicsY', 'DemographicsN', 
        'AgeU18', 'Age18-14', 'Age25-34', 'Age35-44', 'Age45-54', 'Age55-64', 
        'Age65+', 'GenderFemale', 'GenderMale', 'GenderNon-binary', 'GenderTransgender', 
        'GenderPreferNot', 'GenderOther', 'HomePostcode', 'EthnicAfrican', 
        'EthnicArab', 'EthnicAsian', 'EthinicLatino', 'EthnicCaucasian', 
        'EthinicPreferNot', 'EthnicOther', 'IllnessY', 'IllnessN', 'IllnessPreferNot'
        ]
    
    new_df_piece = pd.DataFrame(np.nan, index=df.index, columns=new_empty_cols)
    df = pd.concat([df, new_df_piece], axis=1)




    # Add the calculated columns
    df['Other Pet Related Stuff'] = pet_combined
    df['Value Other Pet Related Stuff'] = pet_sum
    df['Cold drinks cups and tops'] = drink_combined
    df['Value Cold drinks cups and tops'] = drink_sum
    df['BBQ related'] = bbq_combined
    df['Value BBQ related'] = bbq_sum
    df['Other nicotine related'] = smoke_combined
    df['Value Other nicotine related'] = smoke_sum
    df['Farming'] = farm_combined
    df['Value Farming'] = farm_sum
    df['Forestry'] = woods_combined
    df['Value Forestry'] = woods_sum
    df['Industrial'] = ind_combined
    df['Value Industrial'] = ind_sum
    df['Other outdoor related'] = out_combined
    df['Value Other outdoor related'] = out_sum
    df['Outdoor event related (e.g.race)'] = event_combined
    df['Value Outdoor event related (e.g.race)'] = event_sum
    df['Other Miscellaneous'] = misc_combined
    df['Value Other Miscellaneous'] = misc_sum




    # Sort out the order
    desired_order = ['Ethics','Date_TrailClean','People','postcode','TrailName','FamiliarRegular',
        'FamiliarFewTimes','FamiliarFirst','ActivityBike', 'ActivityRun',
        'ActivityWalk','ActivityCombo','ActivityOther','WeatherSunny',
        'WeatherOvercast','WeatherLightRain','WeatherHeavyRain','WeatherSnow',
        'WeatherWinds','WeatherExtremes','HabitatCanal','HabitatCoastal',
        'HabitatFarm','HabitatForest','HabitatMarsh','HabitatMoor','HabitatMountain',
        'HabitatRiver','HabitatUrban','TypeMrkdTrails','TypeRoW','TypeUnofficial',
        'TypePump','TypeUrban','TypeOtherTrails','TypeAccess','TypeCar','TypeOther',
        'MostTypeTrails','MostTypeFootpaths','MostTypeUnofficial','MostTypePump',
        'MostTypeUrban','MostTypeOtherTrails','MostTypeAccess','MostTypeCar',
        'MostTypeOther','Time_min','Distance_km','TotItems','AdjTotItems',
        'Handful','Pocketful',
        'Bread bag', 'Carrier bag', 'Bin bag', 'Multiple Bin Bags', 'Binbags',
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
        'Unbranded single-use carrier bags', 'Branded bag for life',
        'Unbranded bag for life', 
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
        'M&S','Tesco','Other','AnimalsY','AnimalsN','AnimalsNotChecked',
        'AIDeath','AIChew','AINesting','AIOther','AItype','ExperienceY','ExperienceN',
        'Experience_Feeling1', 'Experience_Feeling2','Experience_Feeling3',
        'Experience_+veFeeling','Experience_Engagement',
        'Experience_Relationships','Experience_Meaning','Experience_Accomplishment',
        'Experience_Health','Experience_NatureConnect','Experience_Place',
        'Experience_Knowledge',
        'Connection_RewardY','Connection_RewardN','Connection_RewardUnsure',
        'Connection_TakePartAgainY','Connection_TakePartAgainN',
        'Connection_TakePartAgainUnsure','First time','Volunteer','A-Team',
        'HQ','Community Hub','VolunteerWeeks',
        'VolunteerMonths','VolunteerYears','WhySubmit','Name','Surname',
        'Receive emailY','Receive emailN','Receive email_alreadyin',
        'DemographicsY','DemographicsN',
        'AgeU18','Age18-14','Age25-34','Age35-44','Age45-54','Age55-64','Age65+',
        'GenderFemale','GenderMale','GenderNon-binary','GenderTransgender',
        'GenderPreferNot','GenderOther','HomePostcode','EthnicAfrican','EthnicArab',
        'EthnicAsian','EthinicLatino','EthnicCaucasian','EthinicPreferNot',
        'EthnicOther','IllnessY','IllnessN','IllnessPreferNot','month','year',
        'email_id','community','name'
        ]
    
    df = df[desired_order]
    
    df.to_csv(TFTout)
