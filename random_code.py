#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 08:55:07 2025

@author: heatherkay
"""

import pandas as pd

months = ['5','6','8','9','10','11','12']
folder = '/Users/heatherkay/Documents/TrashFreeTrails/Data/Monthly stats/2024/input/'

for month in months:
    df = pd.read_csv(folder + 'CS_count_' + month + '.csv' )
    df = df.rename(columns={'Time(hours)':'Time_hours'})
    df.to_csv(folder + 'CS_count_' + month + '.csv' , index=False)
    
def join_survey_clean_data(oldin, newin, cleanout):
    """
    A function which takes new cleaned monthly TFT survey data and joins it with
    existing data
    
    Parameters
    ----------
    
    TFTin: string
            path to input csv file with original TFT data
             
    newin: string
            path to input csv file with new data  
             
    monthout: string
            path to save the clean data just for the month you are processing
            
    rawout:  string        
            path to save file with raw data
            
    TFTout: string
            path to save file with clean data
    """    

    #read in 'old' data and 'new' data
    orig_data = pd.read_csv(oldin)   
    new_data = pd.read_csv(newin)
    cols2 = list(orig_data) # only needed if using column names from 'old' data or to check columns

    #check column headers - not needed unless df_final has more columns than orig_data
    c = []
    for val in cols:
        if val not in cols2:
            c.append(val)
            
    d = []
    for val in cols2:
        if val not in cols:
            d.append(val)  

      
    #add new cleaned data to top of original data
    dfs = (new_data, orig_data)
    
    #stage above may be changed so data is added to the appropriate yearly/monhtly dataset
    
    df_final = pd.concat(dfs, ignore_index = True) 
    
    df_final.to_csv(cleanout)    

#SUP / m checks
count = pd.read_csv('/Users/heatherkay/Documents/TrashFreeTrails/Data/Data_per_year/Count/2024.csv')    

ms = count['Total_distance(m)']
itms = count['TotItems']
items = [x for x in itms if str(x) != 'nan'] 
m = [x for x in ms if str(x) != 'nan']

prevs = []
for index, i in count.iterrows():
    item = i['TotItems']
    distance = i['Total_distance(m)']
    if item == 0:
        continue
    if distance == 0:
        continue
    prev = item/distance
    prevs.append(prev)


prv = [x for x in prevs if str(x) != 'nan']    
denom = len(prv)
nom = sum(prv)  
new_prevalence = nom/denom  
sum_items = sum(items)
sum_m = sum(m)
prevalence_notna = sum_items/sum_m



#
years = [2024, 2025]
months = [1,2,3,4,5,6,8,9,10,11,12]

csv = '/Users/heatherkay/Documents/TrashFreeTrails/Data/Misc_data_requests/to_end2024_countries/survey/cymru2025.csv'
folderout = '/Users/heatherkay/Documents/TrashFreeTrails/Data/Misc_data_requests/to_end2024_countries/months_cymru/'

df = pd.read_csv(csv)

for year in years:
        #extract data for one year
        new=df.loc[df['year']==year]
        
        
        #extract data for each month
        for month in months:
            data=new.loc[new['month']==month]
            if data.empty:
                continue
            #write df with monthly data
            data.to_csv(folderout + 'survey_{}_{}.csv'.format(month,year))
            del data
            
 
    


folderin = '/Users/heatherkay/Documents/TrashFreeTrails/Data/Monthly stats/2025/'
months = ['2025_01','2025_02','2025_03']
data = ['count.csv','CS_count.csv','CS_survey.csv','lite.csv','survey.csv']
folderout = '/Users/heatherkay/Documents/TrashFreeTrails/Data/Misc_data_requests/to_end2024_countries/2025/'

for d in data:
    dfs = []
    for month in months:
       df = pd.read_csv(folderin + month + '/input/' + d)
       dfs.append(df)
    new = pd.concat(dfs, ignore_index=True)
    new.to_csv(folderout + d)
    
       
       
    