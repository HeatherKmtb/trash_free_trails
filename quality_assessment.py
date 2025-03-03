#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 09:47:05 2025

@author: heatherkay
"""

import pandas as pd


def survey_QA(TFTin, folderout):
    """
    A function which takes clean monthly TFT survey data and does a quality assessment
    
    Parameters
    ----------
    
    TFTin: string
             path to input csv file with monthly TFT data
            
    dataout: string
           path to save results
    """
    
    df = pd.read_csv(TFTin)
    
    #check tot items v surveyed items
    col_list = ['Value Full Dog Poo Bags','Value Unused Dog Poo Bags',
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
    
    df3 = df[df['TotItems']>0]
    df4 = df3[df3['MoreInfoY'].notna()]
    
    for index,i in df4.iterrows():
        sum_items = i[col_list].sum()
        tot_items = i['TotItems']
        next_step = sum_items + tot_items
        mean = next_step/2   
        variance = tot_items - mean 
        qa_step1 = abs(variance)/tot_items
        qa = qa_step1 *100
        #qa = qa_step2.astype(float)
        #pd.to_numeric(qa)
        
    df4.insert(loc=31, column = 'VarianceTotItems', value=variance)
    df4.insert(loc=32, column = 'QATotItems', value=qa)
    
    df4.to_csv('/Users/heatherkay/Documents/TrashFreeTrails/Data/Testing_code/qa_2024.csv')

    results = pd.DataFrame(columns = ['tot_items','reported_SUP_%','reported_SUP_no',
            'rep_SUP_no_from_surveyed','SUP_from_surveyed','variance','QA'])
                                      
    #check SUP percentage
    col_list_SUP = ['Value Full Dog Poo Bags','Value Unused Dog Poo Bags',
     #'Value Toys (eg., tennis balls)','Value Other Pet Related Stuff',
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
    'Value Food on the go (eg.salad boxes)',
    #'Value Homemade lunch (eg., aluminium foil, cling film)', 'Value Fruit peel & cores',
    'Value Cigarette Butts','Value Smoking related',
    'Value Disposable vapes','Value Vaping / E-Cigarette Paraphernalia','Value Drugs related',
    #'Value Farming',
    'Value Salt/mineral lick buckets','Value Silage wrap',
    #'Value Forestry',
    'Value Tree guards',
    #'Value Industrial',
    'Value Cable ties',
    'Value Industrial plastic wrap','Value Toilet tissue','Value Face/ baby wipes',
    'Value Nappies','Value Single-Use Period products','Value Single-Use Covid Masks',
    'Value Rubber/nitrile gloves','Value Outdoor event (eg Festival)',
    #'Value Camping',
    'Value Halloween & Fireworks','Value Seasonal (Christmas and/or Easter)',
    'Value Normal balloons','Value Helium balloons',
    #'Value MTB related (e.g. inner tubes, water bottles etc)',
    #'Value Running','Value Roaming and other outdoor related (e.g. climbing, kayaking)',
    'Value Outdoor sports event related (e.g.race)',
    #'Value Textiles','Value Clothes & Footwear',
    'Value Plastic milk bottles','Value Plastic food containers','Value Cardboard food containers',
    'Value Cleaning products containers',
    #'Value Miscellaneous','Value Too small/dirty to ID',
    #'Value Weird/Retro'
    ]
    
    col_list_maybe_SUP = ['Value Toys (eg., tennis balls)','Value Other Pet Related Stuff',
                          'Value Homemade lunch (eg., aluminium foil, cling film)', 
                          'Value Fruit peel & cores','Value Farming','Value Industrial','Value Camping',
                          'Value MTB related (e.g. inner tubes, water bottles etc)','Value Running',
                          'Value Roaming and other outdoor related (e.g. climbing, kayaking)',
                          'Value Miscellaneous','Value Too small/dirty to ID','Value Weird/Retro']
    
    #remove cols where calcs aren't possible
    #df2 = df[df['Perc_SU'].notna()]

    df5 = df4[df4['Perc_SU']>0]

    for index,i in df5.iterrows():
        sum_items = i[col_list].sum()
        SUP_items = i[col_list_SUP].sum()
        pot_SUP_items = i[col_list_maybe_SUP].sum()
        perc_SUP = i['Perc_SU']
        tot_items = i['TotItems']
        estimated_SUP = (perc_SUP*tot_items)/100
        
        next_step = SUP_items + abs(estimated_SUP)
        mean = next_step/2   
        variance = abs(estimated_SUP) - mean 
        qa_step1 = abs(variance)/estimated_SUP
        qa = qa_step1 *100

        #pd.to_numeric(qa)
        
        perSUP = i['Perc_SU']
        percSUP = float(perSUP)
        totitems = i['TotItems']
        result = percSUP/100 * totitems
        other = percSUP/100 * sum_items

        results = results.append({'tot_items':tot_items, 'reported_SUP_%':perSUP,
                              'reported_SUP_no':result, 'rep_SUP_no_from_surveyed':other,
                              'SUP_from_surveyed':SUP_items,
                              'pot_SUP_from_surveyed':pot_SUP_items,
                              'variance':variance,'QA':qa, 'sum_surveyed_items':sum_items}, ignore_index=True)

    results.to_csv('/Users/heatherkay/Documents/TrashFreeTrails/Data/Testing_code/qa.csv')
    
    import matplotlib.pyplot as plt

    import numpy as np        
      
    
 #plots for % SUP
    x = results['reported_SUP_no'].astype(float)
    y = results['SUP_from_surveyed'].astype(float)
    
    #plot the result
    fig = plt.figure(); ax = fig.add_subplot(1,1,1)
    plt.rcParams.update({'font.size':12})
    #plots H_100 on x with I_CD on y
    ax.scatter(x,y,marker='.')
    #sets title and axis labels
    ax.set_title('Comparisons of SUP reported')
    ax.set_ylabel('Amount of SUP from count of surveyed items')
    ax.set_xlabel('Amount of SUP from % of total items reported')
    ax.set_xlim([0, 2500])
    ax.set_ylim([0,2500])  
    ax.set_aspect('equal', adjustable='box')
    #obtain m (slope) and b(intercept) of linear regression line
    #m, b = np.polyfit(x,y, 1)
    #add linear regression line to scatterplot 
    #plt.plot(x, m*x+b)
    plt.close
     
    
    #alt plot with reduced axes
    fig = plt.figure(); ax = fig.add_subplot(1,1,1)
    plt.rcParams.update({'font.size':12})
    #plots H_100 on x with I_CD on y
    ax.scatter(x,y,marker='.')
    #sets title and axis labels
    ax.set_title('Comparisons of SUP reported')
    ax.set_ylabel('Amount of SUP from count of surveyed items')
    ax.set_xlabel('Amount of SUP from % of total items reported')
    ax.set_xlim([0, 500])
    ax.set_ylim([0,500])  
    ax.set_aspect('equal', adjustable='box')
    #obtain m (slope) and b(intercept) of linear regression line
    #m, b = np.polyfit(x,y, 1)
    #add linear regression line to scatterplot 
    #plt.plot(x, m*x+b)
    plt.close    

 #plots for total items v surveyed items    
    x = results['sum_surveyed_items'].astype(float)
    y = results['tot_items'].astype(float)
    

    fig = plt.figure(); ax = fig.add_subplot(1,1,1)
    plt.rcParams.update({'font.size':12})
    #plots H_100 on x with I_CD on y
    ax.scatter(x,y,marker='.')
    #sets title and axis labels
    ax.set_title('Comparisons of SUP reported')
    ax.set_ylabel('total items reported')
    ax.set_xlabel('total items from count of surveyed items')
    ax.set_xlim([0, 2500])
    ax.set_ylim([0,2500])  
    ax.set_aspect('equal', adjustable='box')
    #obtain m (slope) and b(intercept) of linear regression line
    #m, b = np.polyfit(x,y, 1)
    #add linear regression line to scatterplot 
    #plt.plot(x, m*x+b)
    plt.close    
    
    #alt plot with reduced axes
    fig = plt.figure(); ax = fig.add_subplot(1,1,1)
    plt.rcParams.update({'font.size':12})
    #plots H_100 on x with I_CD on y
    ax.scatter(x,y,marker='.')
    #sets title and axis labels
    ax.set_title('Comparisons of SUP reported')
    ax.set_ylabel('total items reported')
    ax.set_xlabel('total items from count of surveyed items')
    ax.set_xlim([0, 200])
    ax.set_ylim([0,200])  
    ax.set_aspect('equal', adjustable='box')
    #obtain m (slope) and b(intercept) of linear regression line
    #m, b = np.polyfit(x,y, 1)
    #add linear regression line to scatterplot 
    #plt.plot(x, m*x+b)
    plt.close        
    
    
 #plot histogram of variance  
    x = results['QA'] 
    counts, bins = np.histogram(x)
    plt.stairs(counts, bins)
    
    
    
def count_QA(TFTin, TFTout):
    """
    A function which takes clean monthly TFT survey data and does a quality assessment
    
    Parameters
    ----------
    
    TFTin: string
             path to input csv file with monthly TFT data
            
    dataout: string
           path to save results
    """    
    
    df = pd.read_csv(TFTin)
    
    col_list = ['Transect1','Transect2','Transect3','Transect4','Transect5','Transect6',
    'Transect7','Transect8','Transect9','Transect10']
    
    df[['TotItems']] = df[['TotItems']].apply(pd.to_numeric)
    df[col_list] = df[col_list].apply(pd.to_numeric)
    df4 = df[df['TotItems']>0]
    
    var=[]
    qas=[]
    for index,i in df4.iterrows():
        sum_items = i[col_list].sum()
        tot_items = i['TotItems']
        next_step = sum_items + tot_items
        mean = next_step/2   
        variance = tot_items - mean 
        qa_step1 = abs(variance)/tot_items
        qa = qa_step1 *100
        var.append(variance)
        qas.append(qa)
        
    df4.insert(loc=67, column = 'VarianceTotItems', value=var)
    df4.insert(loc=68, column = 'QATotItems', value=qas)
    
    df4.to_csv(TFTout)
    
    df100m = df[df['100m_transect'].notna()]
    df1km = df[df['1km_transect'].notna()]
    
    #100m
    check = []
    for index,i  in df100m.iterrows():
        #distance = i['Total_distance']
        no_transects = []
        for col in col_list:
            trans = i[col]
            if pd.isna(trans):
                no_transects.append(0)
            else:
                no_transects.append(1)
        check1 = sum(no_transects)
        check2 = check1 * 100
        check.append(check2)
        
    df100m.insert(loc=14, column = 'Check_Distance', value = check)    
      
    #1km
    check = []
    for index,i  in df1km.iterrows():
        #distance = i['Total_distance']
        no_transects = []
        for col in col_list:
            trans = i[col]
            if pd.isna(trans):
                no_transects.append(0)
            else:
                no_transects.append(1)
        check1 = sum(no_transects)
        check2 = check1 * 1000
        check.append(check2)
        
    df1km.insert(loc=14, column = 'Check_Distance', value = check)    
        
                     
                

    
    
