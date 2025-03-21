#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 13:32:46 2025

@author: heatherkay
"""


import pandas as pd

postcodes = pd.read_csv('/Users/heatherkay/Documents/TrashFreeTrails/Data/Postcode_locations.csv')

df = pd.read_csv('/Users/heatherkay/Documents/TrashFreeTrails/Data/Data_per_year/Survey/ALL_toend2024_extratimecolumnandpostcodes.csv')
Scotland = []   
Wales = []
England = []
for index,i in postcodes.iterrows():
    if i['Country'] == 'Scotland':
        postcode = i['Prefix']
        Scotland.append(postcode)
    elif i['Country'] == 'Wales':
        postcode = i['Prefix']
        Wales.append(postcode)  
    else:
        postcode = i['Prefix']
        England.append(postcode)         
        
scots = pd.DataFrame()        
for p in Scotland:
    new = df.loc[df['postcode_start']==p]
    scots = scots.append(new)
    
cymru = pd.DataFrame()        
for p in Wales:
    new = df.loc[df['postcode_start']==p]
    cymru = cymru.append(new)  
    
eng = pd.DataFrame()        
for p in England:
    new = df.loc[df['postcode_start']==p]
    eng = eng.append(new)      
    
folderout = '/Users/heatherkay/Documents/TrashFreeTrails/Data/Data_per_year/Survey/to_end2024_countries/'

eng.to_csv(folderout + 'england.csv')
scots.to_csv(folderout + 'alba.csv')
cymru.to_csv(folderout + 'cymru.csv')


results = pd.DataFrame(columns=['country', '% submissions reporting DRS',
                              'total DRS (including glass)','total glass DRS items',
                              'amount of DRS items per km of trail',
                              '% of items surveyed which are DRS (including glass)',
                              '% of DRS items that are glass',
                              'total_items'])

DRS = ['Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
    'Value Aluminium soft drink cans','Value Plastic bottle, top','Value Glass soft drink bottles',
    'Value Plastic energy drink bottles','Value Aluminium energy drink can',
    'Value Aluminium alcoholic drink cans','Value Glass alcoholic bottles']
    
DRS_glass = ['Value Glass soft drink bottles','Value Glass alcoholic bottles']



survey = eng
      
DRS_submissions = []
DRS_glass_ttl = []
df2 = survey[survey['MoreInfoY'].notna()] 
for index, i in df2.iterrows():
        DRS_items = i[DRS].sum() 
        glass_itms = i[DRS_glass].sum()
        if DRS_items > 0:
            DRS_submissions.append(DRS_items)
        DRS_glass_ttl.append(glass_itms)
        
DRS_subs = len(DRS_submissions)
    
subs = len(df2.index)

    
#% Submissions reporting DRS                
DRS_reported = (DRS_subs/subs)*100
#DRS total items
DRS_tot_items = sum(DRS_submissions)
#DRS total glass items
DRS_tot_glass = sum(DRS_glass_ttl)
tot_items = df2['TotItems'].sum()
survey_km = df2['Distance_km'].sum()
DRS_prevalence = DRS_tot_items/survey_km
DRS_proportion = DRS_tot_items/tot_items
glass_proportion = DRS_tot_glass/DRS_tot_items
country = 'England'

   
results = results.append({'country':country, '% submissions reporting DRS':DRS_reported,
                              'total DRS (including glass)':DRS_tot_items,'total glass DRS items':DRS_tot_glass,
                              'amount of DRS items per km of trail':DRS_prevalence,
                              '% of items surveyed which are DRS (including glass)':DRS_proportion,
                              '% of DRS items that are glass':glass_proportion,
                              'total_items':tot_items}, ignore_index=True) 
    

