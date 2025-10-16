#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 11:59:31 2025

@author: heatherkay
"""

import os
import pandas as pd


years = ['2019','2020','2021','2022','2023','2024', '2025']

months = months = ['01','02','03','04','05','06','07','08','09','10','11','12']

folderin = '/Users/heatherkay/Documents/TrashFreeTrails/Data/Monthly_stats/'
folderout = '/Users/heatherkay/Documents/TrashFreeTrails/Data/Misc_data_requests/SoOT_2025/'


all_dfs = []

for year in years:
    for month in months:
        # try version with "2020_" prefix first
        filepath = f"{folderin}{year}/output_10_25/2020_{month}_brands_all.csv"
        
        if not os.path.exists(filepath):
            # fall back to version without prefix
            filepath = f"{folderin}{year}/output_10_25/{month}_brands_all.csv"
        
        if os.path.exists(filepath):
            df = pd.read_csv(filepath)
            print(f"Loaded: {filepath}")
            
            # --- Clean brand names ---
            df['brand'] = (
                df['brand']
                .astype(str)           # make sure it’s string
                .str.lower()           # lowercase
                .str.replace(r'[\s\-]+', '', regex=True)  # remove spaces and dashes
            )
        
            all_dfs.append(df)
        else:
            print(f"Skipped missing: {filepath}")
            continue

# --- Combine and aggregate ---
if all_dfs:
    combined_df = pd.concat(all_dfs, ignore_index=True)
    
    # Group by brand, summing count and score
    summary_df = combined_df.groupby('brand', as_index=False)[['count', 'score']].sum()

else:
    print("No files found.")
    
    




    
            