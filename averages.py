#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 14:39:55 2025

@author: heatherkay
"""
import pandas as pd

def building_averages(TFTin, dataout):
    """
    A function which takes any TFT survey data and obtains averages
    
    Parameters
    ----------
    
    TFTin: string
             path to input csv file with TFT data
            
    dataout: string
           path to save results
    """
    
    df = pd.read_csv(TFTin)
    
    #creating empty lists to add data into
    vols = []
    kms = []
    mins = []
    #making dataframe which only has submissions which report the numer of people
    df2 = df[df['People'].notna()]
    #for each of these submissions extracting the number of people and adding to the list
    for index,i in df2.iterrows():
        vol = i['People']
        vols.append(vol)
    
    #repeating steps above for distance
    df2 = df[df['Distance_km'].notna()]
    for index,i in df2.iterrows():
        km = i['Distance_km']
        kms.append(km)
        
    #repeating steps above for time    
    df2 = df[df['Time_min'].notna()]
    for index,i in df2.iterrows():
        time = i['Time_min']
        mins.append(time)        

    #preparing list for the reults
    stat = ['People','Distance_km','Time_min']
    #defining the data for the loop below
    cats = [vols, kms, mins]
    #creating empty list for the reults
    averages = []
    
    for c in cats:
        #getting the length of the data = number of submissions
        length = len(c)
        #getting the sum of the data
        total = sum(c)
        #calculating the average per submission
        average = total/length
        averages.append(average)
        
    #preparing the results    
    dict = {'stat':stat, 'average':averages}  
    #writing the reults to a dataframe
    results = pd.DataFrame(dict) 
    results.to_csv(dataout)
        