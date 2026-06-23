#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:16:01 2026

@author: heatherfriendship
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('/Users/heatherfriendship/Documents/TrashFreeTrails/Data/Data_requests/Citizen_Science/Leighs_school/input/survey.csv')


#SUP composition comparison
DRS = ['Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
'Value Aluminium soft drink cans', 'Value Glass soft drink bottles',
'Value Plastic energy drink bottles','Value Aluminium energy drink can',
'Value Aluminium alcoholic drink cans','Value Glass alcoholic bottles',
'Value Glass soft drink bottles','Value Glass alcoholic bottles'
] 
EPR = ['Value Milkshake bottle or carton','Value Plastic energy gel sachet',
'Value Plastic energy gel end','Value Protein drink bottle or carton',
'Value Hot drinks cups','Value Hot drinks tops and stirrers',
'Value Cold drinks cups and tops','Value Cartons','Value Plastic straws',
'Value Paper straws',
'Value Plastic bottle, top', 'Value Glass bottle tops', 'Value Ring pull', 
'Value Plastic bottle sleeve','Value Confectionary/sweet wrappers',
'Value Wrapper "corners" / tear-offs','Value Other confectionary (eg., Lollipop Sticks)',
'Value Crisps Packets','Value Branded single-use carrier bags',
'Value Unbranded single-use carrier bags', 'Value Branded bag for life',
'Value Unbranded bag for life', 
'Value Branded plastic fast / takeaway food packaging / utensils',
'Value Unbranded plastic fast / takeaway food packaging / utensils',
'Value Branded card or wood fast / takeaway food packaging / utensils',
'Value Unbranded card or wood fast / takeaway food packaging / utensils',
'Value Branded condiments packaging','Value Unbranded condiments packaging',
'Value Branded food on the go','Value Unbranded food on the go',
'Value Plastic milk bottles','Value Glass milk bottles',
'Value Plastic food containers','Value Cardboard food containers',
'Value Cleaning products containers','Value Cosmetics / deodorants', 
'Value Nicotine related packaging'
]

poo = ['Value Full Dog Poo Bags','Value Unused Dog Poo Bags',
       'Value Unbagged dog poo'
       ]

all_items = ['Value Full Dog Poo Bags',
'Value Unused Dog Poo Bags','Value Other Pet Related Stuff',
'Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
'Value Aluminium soft drink cans',
'Value Glass soft drink bottles','Value Milkshake bottle or carton',
'Value Plastic energy drink bottles',
'Value Aluminium energy drink can','Value Plastic energy gel sachet',
'Value Plastic energy gel end',
'Value Protein drink bottle or carton', 'Value Aluminium alcoholic drink cans',
'Value Glass alcoholic bottles','Value Hot drinks cups',
'Value Hot drinks tops and stirrers',
'Value Cold drinks cups and tops','Value Cartons','Value Plastic straws',
'Value Paper straws',
'Value Plastic bottle, top', 'Value Glass bottle tops', 'Value Ring pull', 
'Value Plastic bottle sleeve',
'Value Reusable drinks container','Value Other drink related',
'Value Confectionary/sweet wrappers','Value Wrapper "corners" / tear-offs',
'Value Other confectionary (eg., Lollipop Sticks)',
'Value Crisps Packets','Value Used Chewing Gum','Value Homemade lunch (eg., aluminium foil, cling film)',
'Value BBQ related','Value Fruit peel & cores','Value Branded single-use carrier bags',
'Value Unbranded single-use carrier bags', 'Value Branded bag for life',
'Value Unbranded bag for life', 
'Value Branded plastic fast / takeaway food packaging / utensils',
'Value Unbranded plastic fast / takeaway food packaging / utensils',
'Value Branded card or wood fast / takeaway food packaging / utensils',
'Value Unbranded card or wood fast / takeaway food packaging / utensils',
'Value Branded condiments packaging','Value Unbranded condiments packaging',
'Value Branded food on the go','Value Unbranded food on the go',
'Value Branded other food related','Value Unbranded other food related',
'Value Clothes & Footwear','Value Textiles','Value Plastic milk bottles',
'Value Glass milk bottles',
'Value Plastic food containers','Value Cardboard food containers',
'Value Cleaning products containers',
'Value Cosmetics / deodorants', 'Value Other household',
'Value Cigarette Butts','Value Nicotine pouches','Value Disposable vapes',
'Value Nicotine related packaging','Value Other nicotine related',
'Value Unbagged dog poo',
'Value Needles / syringes','Value Other drug related','Value Broken glass or pottery',
'Value Toilet tissue','Value Face/ baby wipes','Value Nappies','Value Period products',
'Value Covid Masks','Value First Aid & medcal waste','Value Batteries and electronics',
'Value Other hazardous', 'Value Camping','Value Fireworks','Value Seasonal (Christmas and/or Easter)',
'Value Rubber balloons','Value Foil balloons','Value Outdoor event related (e.g.race)',
'Value Biking specific','Value Hiking specific','Value Other outdoor related',
'Value Farming','Value Forestry','Value Industrial','Value Cable ties',
'Value Miscellaneous hard plastic','Value Miscellaneous soft plastic',
'Value Miscellaneous card or wood','Value Miscellaneous metal',
'Value Too small/dirty to ID','Value Other Miscellaneous']

nicotine = ['Value Cigarette Butts','Value Nicotine pouches','Value Disposable vapes',
            'Value Nicotine related packaging','Value Other nicotine related'
            ]
   

bg_color = '#312e30'

fig, ax = plt.subplots(figsize=(6, 6), facecolor = bg_color)


df[all_items] = df[all_items].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

# Select the current subplot position (1 to 4)

ax.set_facecolor(bg_color)

drs_sum = df[DRS].sum().sum()
epr_sum = df[EPR].sum().sum()
poo_sum = df[poo].sum().sum()
nico_sum = df[nicotine].sum().sum()
tot_sum = df[all_items].sum().sum()



other_sum = tot_sum - (drs_sum + epr_sum + poo_sum + nico_sum)

# Define initial labels and values
labels = ['DRS', 'EPR', 'Dog poo', 'Nicotine related','Other']
values = [drs_sum, epr_sum, poo_sum, nico_sum, other_sum]

afont = {'family' : 'sans-serif',
    'weight' : 'normal',
    'size'   : 8,
    'color'  : '#FFFFFF'
    }

tfont = {'family' : 'sans-serif',
    'weight' : 'bold',
    'size'   : 12,
    'color'  : '#FFFFFF'
    }

colors = ['#223B18','#3D6A2C','#599B40','#84C26C', '#A7E191']



wedges, texts, autotexts = ax.pie(
    values,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    counterclock=False,
    textprops=dict(**afont)
    )

for autotext in autotexts:
    autotext.set_color('white')           #text inside wedges    
    autotext.set_weight('bold')             

plt.title("Overview of the compostion of SUP", fontdict = tfont)
plt.savefig(folderout + '/composition.png', bbox_inches='tight',
            facecolor = bg_color, edgecolor='none')
plt.close