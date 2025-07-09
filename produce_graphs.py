a#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 15:22:31 2024

@author: heatherkay
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker


def monthly_histogram(TFTin, fileout):
    """
    A function which takes a year of clean TFT survey data and produces a histogram
    of monthly submissions
    
    Parameters
    ----------
    
    TFTin: string
             path to input csv file with all TFT data
            
    fileout: string
           path to save the figure
    """     
    df = pd.read_csv(TFTin)
    



def get_some_graphics(TFTin, folderout):
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
    ax.set_ylim([0,6])  
    #obtain m (slope) and b(intercept) of linear regression line
    m, b = np.polyfit(items, feel, 1)
    #add linear regression line to scatterplot 
    plt.plot(items, m*items+b)
    plt.close

def mach_power_hour(figout):
    """
    A function you put your own data into and plot abarchart
    
    Parameters
    ----------
    figout: string
           path to save figure
    """            
       
    x = [2021, 2022, 2023, 2024]
    y = [1400, 876, 604, 579]


    #plt.style.use('ggplot')

    # Set up figure
    fig, ax = plt.subplots(figsize=(8, 5), dpi=100, facecolor='white')
    ax.set_facecolor('white')

    # Assign unique hexcolors 
    hex_colors = ['#e5582e', '#f4a71c', '#072340', '#faf9ef']


    # Plot bars
    bars = ax.bar(x, y, color=hex_colors, edgecolor='black', linewidth=0.8, width = 0.6)

    # Format x-axis: integer years only
    ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))

    # Add labels above bars
    ax.bar_label(bars, fmt='%.0f')  # <-- No decimals :contentReference[oaicite:1]{index=1}

    # Clean up spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)


    # Add axis labels and title, tweak fonts
    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('Items', fontsize=12, fontweight='bold')
    ax.set_title('Items found at Machynlleth Pump Track per year', fontsize=14, fontweight='bold')

    # Optional: horizontal grid for readability
    #ax.yaxis.grid(True, linestyle='--', color='black', alpha=0.7)
    #ax.set_axisbelow(True)

    plt.tight_layout()
    plt.show()
    fig.savefig(figout, dpi=300, bbox_inches='tight', transparent=False)