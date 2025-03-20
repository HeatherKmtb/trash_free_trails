#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 14:39:55 2025

@author: heatherkay
"""
import pandas as pd

def building_averages(TFTin, dataout):
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
    
    vols = []
    kms = []
    mins = []
    df2 = df[df['People'].notna()]
    for index,i in df2.iterrows():
        vol = i['People']
        vols.append(vol)
    
    df2 = df[df['Distance_km'].notna()]
    for index,i in df2.iterrows():
        km = i['Distance_km']
        kms.append(km)
        
    df2 = df[df['Time_min'].notna()]
    for index,i in df2.iterrows():
        time = i['Time_min']
        mins.append(time)        

    stat = ['People','Distance_km','Time_min']
    cats = [vols, kms, mins]
    averages = []
    for c in cats:
        length = len(c)
        total = sum(c)
        average = total/length
        averages.append(average)
        
    dict = {'stat':stat, 'average':averages}    
    results = pd.DataFrame(dict) 
    results.to_csv(dataout)
        