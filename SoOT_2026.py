#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:39:07 2026

@author: heatherfriendship
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def create_annual_DRS_viz(filein, folderout):
    survey = pd.read_csv(filein)
    
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
    
    #Resolve nan issues
    survey[all_items] = survey[all_items].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

    
    DRS = ['Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
    'Value Aluminium soft drink cans', 'Value Glass soft drink bottles',
    'Value Plastic energy drink bottles','Value Aluminium energy drink can',
    'Value Aluminium alcoholic drink cans','Value Glass alcoholic bottles']
    
    DRS_glass = ['Value Glass soft drink bottles','Value Glass alcoholic bottles']
    
    DRS_metal = ['Value Aluminium soft drink cans','Value Aluminium energy drink can',
    'Value Aluminium alcoholic drink cans',]
    
    DRS_plastic = ['Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
    'Value Plastic energy drink bottles']
    
    years = sorted(survey['year'].unique())

    records = []
    
    for year in years:
        df = survey[survey['year'] == year]

        total_reported_items = df[all_items].sum().sum()
 
        sum_DRS = df[DRS].sum().sum()
        sum_metal = df[DRS_metal].sum().sum()
        sum_plastic = df[DRS_plastic].sum().sum()
        sum_glass = df[DRS_glass].sum().sum()
        
        records.append({
            'year':int(year),
            'DRS_total': sum_DRS / total_reported_items * 100,
            'metal': sum_metal / total_reported_items * 100,
            'plastic': sum_plastic / total_reported_items * 100,
            'glass': sum_glass/ total_reported_items * 100,
            })
        
    results = pd.DataFrame(records).set_index('year')

    # Line graph
    bg_color = '#312e30'
    fig, ax = plt.subplots(figsize=(9, 5), facecolor = bg_color)
    ax.set_facecolor(bg_color)
    
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
    
    colors = ['#5C9E4E','#3D6A2C','#599B40','#84C26C']
    labels = ['DRS_total','plastic',  'metal', 'glass']
    
    for col, c in zip(labels, colors):
        ax.plot(results.index, results[col], marker='o', color=c, label=col)
        
    ax.tick_params(colors='white', which='both')
    for spine in ax.spines.values():
        spine.set_color('white')

    ax.set_xlabel('Year', **afont)
    ax.set_ylabel('Share of reported items (%)', **afont)
    ax.set_title('DRS items as a percentage of all reported litter items', **tfont)
    ax.set_xticks(results.index)
    ax.legend(facecolor=bg_color, edgecolor='white', labelcolor='white')
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    fig.savefig(f'{folderout}/annual_DRS.png', dpi=300)
    plt.show()

    return results

def create_items_per(filein, folderout):
    survey = pd.read_csv(filein)
    
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
    
    #Resolve nan issues
    survey[all_items] = survey[all_items].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

    DRS = ['Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
    'Value Aluminium soft drink cans', 'Value Glass soft drink bottles',
    'Value Plastic energy drink bottles','Value Aluminium energy drink can',
    'Value Aluminium alcoholic drink cans','Value Glass alcoholic bottles']
    
    years = sorted(survey['year'].unique())
    
    records = []
    
    for year in years:
        df = survey[survey['year'] == year]

        total_reported_items = df[all_items].sum().sum()
        sum_DRS = df[DRS].sum().sum()
        perc_DRS = sum_DRS / total_reported_items
 
        km = df['Distance_km'].sum()
        people = df['People'].sum()
        
        records.append({
            'year':int(year),
            'items': total_reported_items/km,
            'people': total_reported_items/people,
            '% DRS': total_reported_items/km * perc_DRS
            })
        
    results = pd.DataFrame(records).set_index('year')

    bg_color = '#312e30'
    fig, ax = plt.subplots(figsize=(9, 5), facecolor = bg_color)
    ax.set_facecolor(bg_color)
    
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
    
    colors = ['#5C9E4E','#3D6A2C','#84C26C']
    labels = ['items','people','% DRS']
    
    for col, c in zip(labels, colors):
        ax.plot(results.index, results[col], marker='o', color=c, label=col)
        
    ax.tick_params(colors='white', which='both')
    for spine in ax.spines.values():
        spine.set_color('white')

    ax.set_xlabel('Year', **afont)
    ax.set_ylabel('Number of items', **afont)
    ax.set_title('Total items recorded per km and per person, plus % DRS per km', **tfont)
    ax.set_xticks(results.index)
    ax.legend(facecolor=bg_color, edgecolor='white', labelcolor='white')
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    fig.savefig(f'{folderout}/items_DRS.png', dpi=300)
    plt.show()

    return results
        
def create_DRS_type_viz(filein, folderout):
    survey = pd.read_csv(filein)
    
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
    
    #Resolve nan issues
    survey[all_items] = survey[all_items].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

    
    DRS = ['Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
    'Value Aluminium soft drink cans', 'Value Glass soft drink bottles',
    'Value Plastic energy drink bottles','Value Aluminium energy drink can',
    'Value Aluminium alcoholic drink cans','Value Glass alcoholic bottles']
    
    DRS_soft = ['Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
                'Value Glass soft drink bottles', 'Value Aluminium soft drink cans']
    
    DRS_energy = ['Value Plastic energy drink bottles','Value Aluminium energy drink can']
    
    DRS_alcohol = ['Value Aluminium alcoholic drink cans','Value Glass alcoholic bottles']
    
    years = sorted(survey['year'].unique())

    records = []
    
    for year in years:
        df = survey[survey['year'] == year]

        total_reported_items = df[all_items].sum().sum()
 
        sum_DRS = df[DRS].sum().sum()
        sum_soft = df[DRS_soft].sum().sum()
        sum_energy = df[DRS_energy].sum().sum()
        sum_alcohol = df[DRS_alcohol].sum().sum()
        
        records.append({
            'year':int(year),
            'DRS_total': sum_DRS / total_reported_items * 100,
            'soft': sum_soft / total_reported_items * 100,
            'energy': sum_energy / total_reported_items * 100,
            'alcohol': sum_alcohol/ total_reported_items * 100,
            })
        
    results = pd.DataFrame(records).set_index('year')

    # Line graph
    bg_color = '#312e30'
    fig, ax = plt.subplots(figsize=(9, 5), facecolor = bg_color)
    ax.set_facecolor(bg_color)
    
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
    
    colors = ['#5C9E4E','#3D6A2C','#599B40','#84C26C']
    labels = ['DRS_total','soft',  'energy', 'alcohol']
    
    for col, c in zip(labels, colors):
        ax.plot(results.index, results[col], marker='o', color=c, label=col)
        
    ax.tick_params(colors='white', which='both')
    for spine in ax.spines.values():
        spine.set_color('white')

    ax.set_xlabel('Year', **afont)
    ax.set_ylabel('Share of reported items (%)', **afont)
    ax.set_title('DRS items as a percentage of all reported litter items', **tfont)
    ax.set_xticks(results.index)
    ax.legend(facecolor=bg_color, edgecolor='white', labelcolor='white')
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    fig.savefig(f'{folderout}/DRS_type.png', dpi=300)
    plt.show()

    return results        
        
        
