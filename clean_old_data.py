#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:53:12 2024

@author: heatherkay
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def clean_old_data(TFTin, folderout):
    """
    A function which takes clean monthly TFT survey data and produces monthly stats
    
    Parameters
    ----------
    
    TFTin: string
             path to input csv file with monthly TFT data
            
    folderout: string
           path to save all new montly and yearly files
    """
    
    df = pd.read_csv(TFTin)
    
    #clean dataset - remove rows with no value in Total Items column
    df2 = df.dropna(subset=['TotItems'])

    #provide correct column names 
    cols = ['Date_TrailClean','People','postcode','TrailName','ActivityBike',
        'ActivityRun','ActivityWalk','ActivityCombo','ActivityOther',
        'ZonesTrails','ZonesFootpaths','ZonesUnofficial','ZonesPump','ZonesUrban',
        'ZonesOtherTrails','ZonesAccess','ZonesCar','ZonesOther','MostZonesTrails',
        'MostZonesFootpaths','MostZonesUnofficial','MostZonesPump','MostZonesUrban',
        'MostZonesOtherTrails','MostZonesAccess','MostZonesCar','MostZonesOther',
        'Time_min','Distance_km','TotItems','AdjTotItems',
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
        'Weird/Retro','Perc_SU','RecycleY','RecycleN','RecyclePerc','MoreInfoY',
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
        'Value Weird/Retro','B1_Lucozade','B1_Coke','B1_RedBull','B1_Monster','B1_Cadbury',
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
        'Community Hub','Name','Surname','Email ','Phone','Receive email','Receive SMS ']

    df2.columns=cols 
    #getting all the dates into the same format
    dates = df2['Date_TrailClean'].values
    newdates = []
    check=[]
    for d in dates:
        if d.find('/') >=0:
            split = d.split('/')
            year = split[2]
            month = split[1]
            day = split[0]
            newdate = day+'-'+month+'-'+year
            newdates.append(newdate)
        else:
            if d.find('-') >=0:
                split = d.split('-')
                year = split[0]
                month = split[1]
                day = split[2]
                newdate = day+'-'+month+'-'+year
                newdates.append(newdate)
                check.append(newdate)

    #adding the clean dates to the df        
    df2['New_TCdate'] = newdates
    
    del dates, newdates, year, month, day, newdate, split

    #prepare columns with year and month data to be able to extract monthly data 
    m = []
    y = []
    dates = df2['New_TCdate'].values
    for d in dates:
        split = d.split('-')
        month = split[1]
        year = split[2]
        if len(month) == 1:
            new = '0' + month
            m.append(new)
            y.append(year)
        else:
            m.append(month)
            y.append(year)
        
    df2['month'] = m
    df2['year'] = y
    
    del dates, year, month, split
    #get list of years and months
    years = list(np.unique(df2['year']))
    months = list(np.unique(df2['month']))
    
    for year in years:
        #extract data for one year
        new=df2.loc[df2['year']==year]
        #extract data for each month
        for month in months:
            data=new.loc[new['month']==month]
            if data.empty:
                continue
            #write df with monthly data
            data.to_csv(folderout + '{}_{}.csv'.format(year,month))
            del data
            
            
def get_some_graphics(TFTin, folderout)
    """
    A function which takes full clean TFT survey data and produces some graphs
    to analyse benefit of keeping or losing data columns in surveys
    
    Parameters
    ----------
    
    TFTin: string
             path to input csv file with all TFT data
            
    folderout: string
           path to save all figures
    """            
            
    df = pd.read_csv(TFTin)
    
    items = df['AdjTotItems']
    feel = df['Connection_LitterFeel']
    
    #plot the result
    fig = plt.figure(); ax = fig.add_subplot(1,1,1)
    plt.rcParams.update({'font.size':12})
    #plots H_100 on x with I_CD on y
    ax.scatter(items,feel,marker='.')
    #sets title and axis labels
    ax.set_title('Feelings about amount of litter depending on litter amount')
    ax.set_ylabel('Feelings about litter')
    ax.set_xlabel('Amount of litter per person, per km')
    ax.set_xlim([0, 600])
    ax.set_ylim([0,5])  
    #obtain m (slope) and b(intercept) of linear regression line
    m, b = np.polyfit(items, feel, 1)
    #add linear regression line to scatterplot 
    plt.plot(items, m*items+b)
    plt.close
        
    
        
    
    
    
    
        
    
    