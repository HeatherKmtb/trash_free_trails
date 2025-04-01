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

def overview_stats(folderin, folderout):
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

    #dates need to be numeric for trendline

    #Dates = Wilsarno['Date_TrailClean'].apply(datetime.date.toordinal)

    #calculate equation for trendline
    #slope, y0, r, p, stderr = stats.linregress(Dates, Wilsarno['AdjTotItems'])
    
    
    
    