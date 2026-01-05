#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  5 09:30:01 2026

@author: heatherkay
"""

import pandas as pd

df = pd.read_csv('/Users/heatherkay/Documents/TrashFreeTrails/Data/Data_per_year/TFR/TFR_surevys_2025_round_up_just items.csv')

df.columns = df.columns.str.replace('Value ', '', regex=False)



import matplotlib.pyplot as plt

#overall big shitters bar graph

cols = ['Confectionary/sweet wrappers','Toilet tissue', 
        'Food on the go (eg.salad boxes)', 'Outdoor sports event related (e.g.race)',
        'Cable ties','Wrapper "corners" / tear-offs',
        'Hot drinks cups', 'Cigarette Butts',
        'Aluminium energy drink can','Plastic Water Bottles']

# cols = list of column names you want
totals = df[cols].sum()

label_map = {'Confectionary/sweet wrappers':'confectionary',
             'Toilet tissue':'tissue', 
             'Food on the go (eg.salad boxes)':'food on the go',
             'Outdoor sports event related (e.g.race)':'event related',
             'Cable ties':'cable ties',
             'Wrapper "corners" / tear-offs':'tear-offs',
             'Hot drinks cups': 'coffee cups', 
             'Cigarette Butts': 'cigarette butts',
             'Aluminium energy drink can':'energy cans',
             'Plastic Water Bottles':'water bottles'}

short_labels = [label_map.get(c, c) for c in totals.index]

plt.figure()
plt.bar(short_labels, totals.values)
plt.xlabel("Big (S)hitter")
plt.ylabel("Total number of items")
plt.title("Overall Big (S)hitters")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('/Users/heatherkay/Documents/TrashFreeTrails/Data/Data_requests/TFR/2025_round_up/overall_shitters.svg')

plt.show()





#stacked big shitters graph
cols = ['Confectionary/sweet wrappers','Toilet tissue', 
        'Food on the go (eg.salad boxes)', 'Outdoor sports event related (e.g.race)',
        'Cable ties','Wrapper "corners" / tear-offs',
        'Hot drinks cups', 'Cigarette Butts',
        'Aluminium energy drink can','Plastic Water Bottles']


label_map = {'Confectionary/sweet wrappers':'confectionary',
             'Toilet tissue':'tissue', 
             'Food on the go (eg.salad boxes)':'food on the go',
             'Outdoor sports event related (e.g.race)':'event related',
             'Cable ties':'cable ties',
             'Wrapper "corners" / tear-offs':'tear-offs',
             'Hot drinks cups': 'coffee cups', 
             'Cigarette Butts': 'cigarette butts',
             'Aluminium energy drink can':'energy cans',
             'Plastic Water Bottles':'water bottles'}

df_plot = df.set_index('TrailName')[cols]

# Transpose so columns become x-axis
df_plot = df_plot.T

# Apply label_map to x-axis labels
df_plot.index = [label_map.get(c, c) for c in df_plot.index]

# Plot stacked bars
ax = df_plot.plot(kind='bar', stacked=True, figsize=(10,6))

# Rotate x labels
plt.xticks(rotation=45, ha='right')
plt.ylabel("Total number of items")
plt.xlabel("Big (S)hitter")
plt.title("Overall Big (S)hitters by event")
plt.tight_layout()
plt.savefig('/Users/heatherkay/Documents/TrashFreeTrails/Data/Data_requests/TFR/2025_round_up/event_shitters.svg')
plt.show()






#event type big shitters

cols = ['Confectionary/sweet wrappers','Toilet tissue', 
        'Food on the go (eg.salad boxes)', 'Outdoor sports event related (e.g.race)',
        'Cable ties','Wrapper "corners" / tear-offs',
        'Hot drinks cups', 'Cigarette Butts',
        'Aluminium energy drink can','Plastic Water Bottles']

df_grouped = df.groupby('Event')[cols].mean()

# Transpose so columns become x-axis
df_plot = df_grouped.T

# Apply label_map to x-axis labels
df_plot.index = [label_map.get(c, c) for c in df_plot.index]

# Plot stacked bars
ax = df_plot.plot(kind='bar', stacked=True, figsize=(10,6))

# Rotate x labels
plt.xticks(rotation=45, ha='right')
plt.ylabel("Total number of items")
plt.xlabel("Big (S)hitter")
plt.title("Overall Big (S)hitters by event")
plt.tight_layout()
plt.savefig('/Users/heatherkay/Documents/TrashFreeTrails/Data/Data_requests/TFR/2025_round_up/event_type_shitters.svg')
plt.savefig('/Users/heatherkay/Documents/TrashFreeTrails/Data/Data_requests/TFR/2025_round_up/event_type_shitters.png')
plt.show()



#event type big shitters without selecting type...
#df_grouped = df.groupby('Event').mean()
numeric_cols = df.select_dtypes(include='number').columns
df_grouped = df.groupby('Event')[numeric_cols].mean()



top_cols_per_event = {}

for event in df_grouped.index:
    # Sort columns by value descending and take top 5
    top_cols = df_grouped.loc[event].sort_values(ascending=False).head(5).index.tolist()
    top_cols_per_event[event] = top_cols
    
top_cols_all = list({col for cols in top_cols_per_event.values() for col in cols})

df_plot = df.groupby('Event')[top_cols_all].mean().T 

ax = df_plot.plot(kind='bar', stacked=True, figsize=(10,6))
plt.xticks(rotation=45, ha='right')
plt.ylabel("Average number of items per trail")
plt.xlabel("Big (S)hitter")
plt.title("Top 5 Big (S)hitters per Event Type")
plt.tight_layout()
ax.figure.savefig('/Users/heatherkay/Documents/TrashFreeTrails/Data/Data_requests/TFR/2025_round_up/top5_event_shitters.svg')
ax.figure.savefig('/Users/heatherkay/Documents/TrashFreeTrails/Data/Data_requests/TFR/2025_round_up/top5_event_shitters.png')
plt.show()
