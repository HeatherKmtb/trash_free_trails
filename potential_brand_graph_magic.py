#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 15:35:23 2026

@author: heatherkay
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image

# ... your existing data setup ...
brands = ['Lucozade', 'Ribena','RedBull','Monster','High5','SIS','Danone',
          'Highland Spring','Coke','Costa','Pepsi','Walkers','Barrs',
          'Britvic','Mars','Nestle','Mondelez','Cadbury','Magnum','Haribo',
          'AB InBev','Corona','Molson Corrs','Thatchers','Heineken',
          'Fosters','Bulmers','Carlsberg','Burger King','Greggs','KFC',
          'McDonalds','Subway','Aldi','Co-op','Euro Shopper','LiDL',
          'M&S','Tesco']  

brand_totals = df[brands].apply(pd.to_numeric, errors='coerce').sum()
brand_totals = brand_totals.sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(14, 8)) # Slightly larger to fit 39 logos nicely

# 1. Plot the bars normally
bars = ax.bar(brand_totals.index, brand_totals.values, color='#00945C', edgecolor='black')

# Path to the folder where your logos are saved
logo_folder = './logos/' 

# 2. Loop through each bar and place the logo at the top
for bar, brand_name in zip(bars, brand_totals.index):
    y_val = bar.get_height()
    x_val = bar.get_x() + bar.get_width() / 2.0
    
    img_path = os.path.join(logo_folder, f"{brand_name}.png")
    
    # Check if the logo image exists before trying to load it
    if os.path.exists(img_path):
        img = Image.open(img_path)
        
        # Adjust zoom to scale your images down to fit nicely above the bars
        # (e.g., 0.05 to 0.15 depending on your original image resolution)
        imagebox = OffsetImage(img, zoom=0.08) 
        
        # Position the logo slightly above the top of the bar (xybox adjusts the offset in pixels)
        ab = AnnotationBbox(imagebox, (x_val, y_val),
                            xybox=(0, 12), 
                            xycoords='data',
                            boxcoords="offset points",
                            frameon=False) # No border around the image
        ax.add_artist(ab)

# 3. Dynamic Y-axis limits
# Since logos take up vertical space, pad the top of the graph so they don't get cut off
ax.set_ylim(0, brand_totals.max() * 1.15)

ax.set_xlabel('Brands', **afont)
ax.set_ylabel('Total', **afont)
ax.set_title('Total Sum per Brand', **tfont, pad=15)

plt.xticks(rotation=45, ha='right')

plt.savefig(folderout + '/brands.png', bbox_inches='tight')
plt.close() # Note: Fixed your missing parenthesis here!