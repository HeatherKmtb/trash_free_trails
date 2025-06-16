#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 14:27:59 2025

@author: heatherkay
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy import stats
from datetime import date

def sort_postcodes (TFTin, TFTout, CHs, folderout):
    """
    A function which takes clean TFT survey data and converts postcodes to capitals
    
    Parameters
    ----------
    
    TFTin: string
             path to input csv file with monthly TFT data
            
    TFTout: string
           path to save new csv file
    """        
    
    df = pd.read_csv(TFTin)
    
    df['postcode'] = df['postcode'].astype(str)
    
    postcodes = []
    for index,i in df.iterrows():
         postcode = i['postcode']
 
         first = postcode.upper()
         new = first.replace(" ","")
         start = new[:4]
         postcodes.append(start)
         
    df['postcode_start'] = postcodes     
         
    df.to_csv(TFTout)
    
    df2 = pd.read_csv(CHs)
    df2['Postcode'] = df2['Postcode'].astype(str)
    #df2['Postcode'] = df2['Postcode'].replace(" ","")

    postcode_list = []    
    for index,i in df2.iterrows():
         postcode = i['Postcode']
         new = postcode.replace(" ","")
         test = new[:4] 
         postcode_list.append(test)
         
    for location in postcode_list:
        new_df = df.loc[df['postcode_start']==location] 
        if new_df.empty:
            continue
        else:
            new_df.to_csv(folderout + '/{}.csv'.format(location))    
            
    #Wilsarno = df.loc[df['postcode_start']=="LL17"]        
        

def plot_data_and_trend (datain, figout):
    """
    A function which takes clean TFT survey data and converts postcodes to capitals
    
    Parameters
    ----------
    
    TFTin: string
             path to input csv file with monthly TFT data
            
    TFTout: string
           path to save new csv file
    """    

    Wilsarno = pd.read_csv(datain)

Dates = Wilsarno['Date_TrailClean'].apply(lambda d: d.toordinal())
Wilsarno['Adj_Date'] = Dates

# Convert ordinal back to datetime.date for plotting
Wilsarno['Plot_Date'] = Wilsarno['Adj_Date'].apply(date.fromordinal)

# Sort by date for plotting
Wilsarno = Wilsarno.sort_values(by='Plot_Date')

# x and y values
x = Wilsarno['Plot_Date']
y = Wilsarno['AdjTotItems']

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, color='blue', marker='o', label='Adjusted Total Items')

# Format x-axis as dates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

    #dates need to be numeric for trendline



    #calculate equation for trendline
    slope, y0, r, p, stderr = stats.linregress(Dates, Wilsarno['AdjTotItems'])


    # x co-ordinates for the start and end of the line
    #x_endpoints = pd.DataFrame([Dates[0], Dates[-1]])

    # Compute predicted values from linear regression
    y_endpoints = y0 + slope * Dates
    # Overlay the line
    ax.plot(Dates, y_endpoints, c='green')


    ax.set_xlabel('Date')
    ax.set_ylabel(r'Adjusted Total Items')
    ax.set_title('Adjusted Total Items Over Time')


    # function to show the plot
    #plt.show()
    plt.savefig(figout)

    y2 = Wilsarno['Distance_km']
    y4 = Wilsarno['TotItems']
    y3 = y4/y2
    
    y = y3
