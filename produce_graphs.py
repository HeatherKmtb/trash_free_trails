#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 15:22:31 2024

@author: heatherkay
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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

