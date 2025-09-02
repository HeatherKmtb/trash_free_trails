#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 13:25:53 2025

@author: heatherkay
"""

import pandas as pd
import functools
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy import stats

def overview_stats(folderin, figout):
    """
    A function which takes clean monthly TFT survey data and produces monthly stats
    
    Parameters
    ----------
    
    folderin: string
             path to input folder with csv files with monthly TFT data
            
    folderout: string
           path for folder to save results in
    """
    

    
    df_2019 = pd.read_csv(folderin + 'output/2019_overview_csv')
    df_2020 = pd.read_csv(folderin + 'output/2020_overview_csv')
    df_2021 = pd.read_csv(folderin + 'output/2021_overview_csv')
    df_2022 = pd.read_csv(folderin + 'output/2022_overview_csv')
    df_2023 = pd.read_csv(folderin + 'output/2023_overview_csv')
    df_2024 = pd.read_csv(folderin + 'output/2024_overview_csv')
    
    years = [df_2019, df_2020, df_2021, df_2022, df_2023, df_2024]
    years = ['2019', '2020', '2021', '2022', '2023', '2024']
    dfs=[]
    for year in years:
        df = pd.read_csv(folderin + year + '/output/' + year + '_overview.csv')
        df['year'] = year
        dfs.append(df)
    
    df = pd.concat(dfs, ignore_index=True)
    
    dates = []
    for index, i in df.iterrows():
        day = 1
        month = i['month']
        year_str = i['year']
        year = int(year_str)
        date = datetime.date(year,month,day)
        dates.append(date)
    
    df['date'] = dates
    
    x = df['date']
    # corresponding y axis values
    y = df['total_submisssions']

    fig, ax = plt.subplots(figsize=(10, 6))
    # plotting the points 
    ax.plot(x, y, color='blue', marker='o', label='Adjusted Total Items')
    #ax.set_xlim()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  # e.g., Jan 2025, Jul 2025

    plt.xticks(rotation=45)
    
    plt.savefig(figout)


def bottle_tops(TFTin, folderout):
    """
    A function which takes full TFT survey stats and produces some graphs
   
    
    Parameters
    ----------
    
    TFTin: string
             path to input csv file with all TFT data
            
    folderout: string
           path to save all figures
    """            
            
    df1 = pd.read_csv(TFTin)

    
    #need to get monthly bottle top values
    years = df1['year'].unique()
    months = df1['month'].unique()
    
    df = pd.DataFrame(columns=['month', 'year', 'tops', 'distance_km'])
    
    for y in years:
        dfy = df1[df1['year']==y]
        for m in months: 
            dfmy = dfy[dfy['month']==m]
            if dfmy.empty:
                tops = 0
                dist = 0
            dfmy.loc[:, 'Value Plastic bottle, top'] = dfmy['Value Plastic bottle, top'].fillna(0)
            dfmy.loc[:, 'Distance_km'] = dfmy['Distance_km'].fillna(0)
            tops = sum(dfmy['Value Plastic bottle, top'])
            dist = sum(dfmy['Distance_km'])
            
            new_row = pd.DataFrame([{'month':m, 'year':y, 'tops':tops, 'distance_km':dist}])
            df = pd.concat([df, new_row], ignore_index=True)
            
            
    df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))         
    
    df['tops_per_km'] = df['tops'] / df['distance_km']
    
    date = df['date']
    #reported_poo = df['poo bags reported']
    #amount_poo = df['poo bags total items']
    #perc_poo = df['poo bags % of total items']
    total_tops = df['tops_per_km']
    
    #plot the result
    fig = plt.figure(); ax = fig.add_subplot(1,1,1)
    plt.rcParams.update({'font.size':12})
    #plots H_100 on x with I_CD on y
    ax.scatter(date,total_tops,marker='.')
    #sets title and axis labels
    ax.set_title('Number of plastic bottle tops reported per kilometer')
    ax.set_ylabel('Number of tops per km')
    ax.set_xlabel('Date')
    #ax.set_xlim([0, 600])
    #ax.set_ylim([0,6])  
    #obtain m (slope) and b(intercept) of linear regression line
    x = date.map(pd.Timestamp.toordinal)
    m, b = np.polyfit(x, total_tops, 1)
    #add linear regression line to scatterplot 
    plt.plot(date, m * x + b, color='red')
    plt.close    
    
    
    