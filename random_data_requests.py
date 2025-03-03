#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:21:47 2024

@author: heatherkay
"""
import pandas as pd
import numpy as np
import statistics
import glob
from os import path


def get_data_quantity_per_month(datain, dataout):
    """
    A function which takes full survey data and gets overall and yearly mean submissions per month
    
    Parameters
    ----------
    
    datain: string
             path to input csv file with all TFT survey data
            
    dataout: string
           path to save results
    """


    df2 = pd.read_csv(datain)
    #get list of years and months
    years = list(np.unique(df2['year']))
    months = list(np.unique(df2['month']))
    
    count = []
    
    for year in years:
        #extract data for one year
        new=df2.loc[df2['year']==year]
        #extract data for each month
        for month in months:
            data=new.loc[new['month']==month]
            if data.empty:
                continue
            submissions = len(data.index)
            count.append(submissions)
            
    monthly_mean = statistics.mean(count)
    
    results = pd.DataFrame(columns = ['year', 'submissions'])

    for year in years:
        count = []
        #extract data for one year
        new=df2.loc[df2['year']==year]
        #extract data for each month
        for month in months:
            data=new.loc[new['month']==month]
            if data.empty:
                continue
            submissions = len(data.index)
            count.append(submissions)
        monthly_mean = statistics.mean(count)    
        
        results = results.append({'year':year, 'mean':monthly_mean}, ignore_index = True)
        
        results.to_csv(dataout)
        
def average_hours_per_person(datain):
    """
    A function which takes full survey data and gets average volunteer hours per person
    
    Parameters
    ----------
    
    datain: string
             path to input csv file with all TFT survey data

    """
    df2 = pd.read_csv(datain)
    
    total = []
    for index, i in df2.iterrows():
        mins = i['Time_min']
        people = i['People']
        hours = mins/60
        tot = people * hours
        total.append(tot)
        
    total_hours = sum(total)
    people = df2['People']
    total_people = sum(people)
    average = total_hours / total_people
            

            
            