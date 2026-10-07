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
            'per km': total_reported_items/km,
            'per person': total_reported_items/people,
            'per km, per person':(total_reported_items/(km*people))*100
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
    labels = ['per km','per person','per km, per person']
    
    for col, c in zip(labels, colors):
        ax.plot(results.index, results[col], marker='o', color=c, label=col)
        
    ax.tick_params(colors='white', which='both')
    for spine in ax.spines.values():
        spine.set_color('white')

    ax.set_xlabel('Year', **afont)
    ax.set_ylabel('Number of items', **afont)
    ax.set_title('Total items recorded per km and per person', **tfont)
    ax.set_xticks(results.index)
    ax.legend(facecolor=bg_color, edgecolor='white', labelcolor='white')
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    fig.savefig(f'{folderout}/per_things.png', dpi=300)
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
        
def create_various_items_per(filein, folderout):
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
    
    pet_stuff = ['Value Full Dog Poo Bags','Value Unused Dog Poo Bags',
    'Value Other Pet Related Stuff']
    
    snack = ['Value Confectionary/sweet wrappers','Value Wrapper "corners" / tear-offs',
    'Value Other confectionary (eg., Lollipop Sticks)','Value Crisps Packets',
    'Value Used Chewing Gum','Value Homemade lunch (eg., aluminium foil, cling film)',
    'Value BBQ related','Value Fruit peel & cores','Value Branded single-use carrier bags',
    'Value Unbranded single-use carrier bags','Value Branded bag for life',
    'Value Unbranded bag for life', 
    'Value Branded plastic fast / takeaway food packaging / utensils',
    'Value Unbranded plastic fast / takeaway food packaging / utensils',
    'Value Branded card or wood fast / takeaway food packaging / utensils',
    'Value Unbranded card or wood fast / takeaway food packaging / utensils',
    'Value Branded condiments packaging','Value Unbranded condiments packaging',
    'Value Branded food on the go','Value Unbranded food on the go',
    'Value Branded other food related','Value Unbranded other food related']
    
    house = ['Value Clothes & Footwear','Value Textiles','Value Plastic milk bottles',
    'Value Glass milk bottles','Value Plastic food containers','Value Cardboard food containers',
    'Value Cleaning products containers','Value Cosmetics / deodorants', 
    'Value Other household']
    
    nicotine = ['Value Cigarette Butts','Value Nicotine pouches',
    'Value Disposable vapes','Value Nicotine related packaging',
    'Value Other nicotine related']
    
    hygiene = ['Value Unbagged dog poo','Value Needles / syringes',
    'Value Other drug related','Value Broken glass or pottery',
    'Value Toilet tissue','Value Face/ baby wipes','Value Nappies',
    'Value Period products','Value Covid Masks','Value First Aid & medcal waste',
    'Value Batteries and electronics','Value Other hazardous']
    
    recreation = ['Value Camping','Value Fireworks','Value Seasonal (Christmas and/or Easter)',
    'Value Rubber balloons','Value Foil balloons','Value Outdoor event related (e.g.race)',
    'Value Biking specific','Value Hiking specific','Value Other outdoor related']
    
    agro_ind = ['Value Farming','Value Forestry', 'Value Industrial',
    'Value Cable ties'] 

    misc = ['Value Miscellaneous hard plastic','Value Miscellaneous soft plastic',
    'Value Miscellaneous card or wood','Value Miscellaneous metal',
    'Value Too small/dirty to ID','Value Other Miscellaneous']
    
    years = sorted(survey['year'].unique())
    
    records = []
    
    for year in years:
        df = survey[survey['year'] == year]

        total_reported_items = df[all_items].sum().sum()
        sum_DRS = df[DRS].sum().sum()
        perc_DRS = sum_DRS / total_reported_items
        sum_pet = df[pet_stuff].sum().sum()
        perc_pet = sum_pet / total_reported_items
        sum_snack = df[snack].sum().sum()
        perc_snack = sum_snack / total_reported_items
        sum_house = df[house].sum().sum()
        perc_house = sum_house / total_reported_items
        sum_nicotine = df[nicotine].sum().sum()
        perc_nicotine = sum_nicotine / total_reported_items
        sum_hygiene = df[hygiene].sum().sum()
        perc_hygiene = sum_hygiene / total_reported_items
        sum_recreation = df[recreation].sum().sum()
        perc_recreation = sum_recreation / total_reported_items
        sum_agro_ind = df[agro_ind].sum().sum()
        perc_agro_ind = sum_agro_ind / total_reported_items
        sum_misc = df[misc].sum().sum()
        perc_misc = sum_misc / total_reported_items
        
 
        km = df['Distance_km'].sum()
        
        records.append({
            'year':int(year),
            'per km': total_reported_items/km,
            '% DRS': total_reported_items/km * perc_DRS,
            '% pet stuff': total_reported_items/km * perc_pet,
            '% food related': total_reported_items/km * perc_snack,
            '% household': total_reported_items/km * perc_house,
            '% nicotine related': total_reported_items/km * perc_nicotine,
            '% hygiene': total_reported_items/km * perc_hygiene,
            '% recreation': total_reported_items/km * perc_recreation,
            '% agro-industrial': total_reported_items/km * perc_agro_ind,
            '% miscellaneous': total_reported_items/km * perc_misc
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
    
    colors = ['#BCA25D','#3D6A2C','#00945C', '#859150', '#70ADA3', '#BA3F0F', 
              '#508591', '#E3761C', '#F7F6EC', '#84C26C']
    labels = ['per km','% DRS', '% pet stuff','% food related','% household',
              '% nicotine related','% hygiene','% recreation','% agro-industrial',
              '% miscellaneous']
    
    for col, c in zip(labels, colors):
        ax.plot(results.index, results[col], marker='o', color=c, label=col)
        
    ax.tick_params(colors='white', which='both')
    for spine in ax.spines.values():
        spine.set_color('white')

    ax.set_xlabel('Year', **afont)
    ax.set_ylabel('Number of items', **afont)
    ax.set_title('Percentages of types of SUP per km through time', **tfont)
    ax.set_xticks(results.index)
    ax.legend(facecolor=bg_color, edgecolor='white', labelcolor='white')
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    fig.savefig(f'{folderout}/item_split.png', dpi=300)
    plt.show()

    return results    



def create_clean_type_viz(filein, folderout):
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

    # Resolve nan issues
    survey[all_items] = survey[all_items].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

    years = sorted(survey['year'].unique())
    clean_types = sorted(survey['CleanType'].dropna().unique())

    records = []

    for year in years:
        df = survey[survey['year'] == year]

        total_reported_items = df[all_items].sum().sum()
        km = df['Distance_km'].sum()

        row = {'year': int(year)}

        # Overall total per km
        row['Total per km'] = total_reported_items / km

        # Per CleanType per km
        for ct in clean_types:
            df_ct = df[df['CleanType'] == ct]
            items_ct = df_ct[all_items].sum().sum()
            row[f'{ct} per km'] = items_ct / km if km else 0

        records.append(row)

    results = pd.DataFrame(records).set_index('year')

    # ---- Plotting ----
    bg_color = '#312e30'
    fig, ax = plt.subplots(figsize=(9, 5), facecolor=bg_color)
    ax.set_facecolor(bg_color)

    afont = {'family': 'sans-serif', 'weight': 'normal', 'size': 8, 'color': '#FFFFFF'}
    tfont = {'family': 'sans-serif', 'weight': 'bold', 'size': 12, 'color': '#FFFFFF'}

    # Generate a distinct color for each line
    n_lines = 1 + len(clean_types)  # 1 overall + 1 per CleanType
    cmap = plt.cm.get_cmap('tab20')
    colors = [cmap(i / n_lines) for i in range(n_lines)]

    # First line: overall total
    ax.plot(results.index, results['Total per km'],
            marker='o', color=colors[0], linewidth=2, label='Total per km')

    # Then each CleanType line
    for i, ct in enumerate(clean_types):
        ax.plot(results.index, results[f'{ct} per km'],
                marker='o', color=colors[i + 1], linewidth=1.5, label=f'{ct} per km')

    ax.tick_params(colors='white', which='both')
    for spine in ax.spines.values():
        spine.set_color('white')

    ax.set_xlabel('Year', **afont)
    ax.set_ylabel('Number of items', **afont)
    ax.set_title('Total items recorded per km by CleanType', **tfont)
    ax.set_xticks(results.index)

    # Legend: total first, then CleanTypes
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, facecolor=bg_color, edgecolor='white', labelcolor='white',
              fontsize=7, loc='upper left')

    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    fig.savefig(f'{folderout}/clean_types.png', dpi=300)
    plt.show()
    
def create_trail_type_viz(filein, folderout):
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

    # Resolve nan issues
    survey[all_items] = survey[all_items].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

    DRS = ['Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
    'Value Aluminium soft drink cans', 'Value Glass soft drink bottles',
    'Value Plastic energy drink bottles','Value Aluminium energy drink can',
    'Value Aluminium alcoholic drink cans','Value Glass alcoholic bottles']
    
    years = sorted(survey['year'].unique())
    group = ['TypeMrkdTrails','TypeRoW','TypeUnofficial',
    'TypePump','TypeUrban','TypeOtherTrails','TypeAccess','TypeCar','TypeOther']
    
    df_clean = survey
   
    non_null_count = df_clean[group].notna().sum(axis=1)
    single_active = non_null_count == 1

    if single_active.any():
    # For each row, find which column has the non-null value
        def get_active_col(row):
            return row[row.notna()].index[0]
    
        df_clean.loc[single_active, 'Trail_Type'] = df_clean.loc[single_active, group].apply(get_active_col, axis=1)
    
        multi_active = non_null_count > 1
        df_clean = df_clean[~multi_active]

    df_clean.drop(columns=group, inplace=True)

    trail_types = sorted(df_clean['Trail_Type'].dropna().unique())
    records = []

    for year in years:
        df = df_clean[df_clean['year'] == year]

        total_reported_items = df[DRS].sum().sum()
        km = df['Distance_km'].sum()

        row = {'year': int(year)}

        # Overall total per km
        row['Total DRS per km'] = total_reported_items / km

        # Per CleanType per km
        for ct in trail_types:
            df_ct = df[df['Trail_Type'] == ct]
            items_ct = df_ct[DRS].sum().sum()
            row[f'{ct} per km'] = items_ct / km if km else 0

        records.append(row)

    results = pd.DataFrame(records).set_index('year')

    # ---- Plotting ----
    bg_color = '#312e30'
    fig, ax = plt.subplots(figsize=(9, 5), facecolor=bg_color)
    ax.set_facecolor(bg_color)

    afont = {'family': 'sans-serif', 'weight': 'normal', 'size': 8, 'color': '#FFFFFF'}
    tfont = {'family': 'sans-serif', 'weight': 'bold', 'size': 12, 'color': '#FFFFFF'}

    # Generate a distinct color for each line
    n_lines = 1 + len(trail_types)  # 1 overall + 1 per CleanType
    cmap = plt.cm.get_cmap('tab20')
    colors = [cmap(i / n_lines) for i in range(n_lines)]

    # First line: overall total
    ax.plot(results.index, results['Total DRS per km'],
            marker='o', color=colors[0], linewidth=2, label='Total DRS per km')

    # Then each CleanType line
    for i, ct in enumerate(trail_types):
        ax.plot(results.index, results[f'{ct} per km'],
                marker='o', color=colors[i + 1], linewidth=1.5, label=f'{ct} per km')

    ax.tick_params(colors='white', which='both')
    for spine in ax.spines.values():
        spine.set_color('white')

    ax.set_xlabel('Year', **afont)
    ax.set_ylabel('Number of items', **afont)
    ax.set_title('DRS items recorded per km by trail type', **tfont)
    ax.set_xticks(results.index)

    # Legend: total first, then CleanTypes
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, facecolor=bg_color, edgecolor='white', labelcolor='white',
              fontsize=7, loc='upper left')

    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    fig.savefig(f'{folderout}/trail_types_DRS.png', dpi=300)
    plt.show()
    
def create_DRS_per_both(filein, folderout):
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
 
        km = df['Distance_km'].sum()
        people = df['People'].sum()
        
        records.append({
            'year':int(year),
            'total items': (total_reported_items/(km*people))*100,
            'DRS': (sum_DRS/(km*people))*100
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
    
    colors = ['#5C9E4E','#3D6A2C']
    labels = ['total items','DRS']
    
    for col, c in zip(labels, colors):
        ax.plot(results.index, results[col], marker='o', color=c, label=col)
        
    ax.tick_params(colors='white', which='both')
    for spine in ax.spines.values():
        spine.set_color('white')

    ax.set_xlabel('Year', **afont)
    ax.set_ylabel('Number of items', **afont)
    ax.set_title('Total items and DRS items recorded per km and per person', **tfont)
    ax.set_xticks(results.index)
    ax.legend(facecolor=bg_color, edgecolor='white', labelcolor='white')
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    fig.savefig(f'{folderout}/DRS_per_person_km.png', dpi=300)
    plt.show()

    return results

def create_DRS_per_km_only(filein, folderout):
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
 
        km = df['Distance_km'].sum()
        people = df['People'].sum()
        
        records.append({
            'year':int(year),
            'total items': total_reported_items/km,
            'DRS': sum_DRS/km
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
    
    colors = ['#5C9E4E','#3D6A2C']
    labels = ['total items','DRS']
    
    for col, c in zip(labels, colors):
        ax.plot(results.index, results[col], marker='o', color=c, label=col)
        
    ax.tick_params(colors='white', which='both')
    for spine in ax.spines.values():
        spine.set_color('white')

    ax.set_xlabel('Year', **afont)
    ax.set_ylabel('Number of items', **afont)
    ax.set_title('Total items and DRS items recorded per km', **tfont)
    ax.set_xticks(results.index)
    ax.legend(facecolor=bg_color, edgecolor='white', labelcolor='white')
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    fig.savefig(f'{folderout}/DRS_per_km.png', dpi=300)
    plt.show()

    return results

def create_DRS_per_person_only(filein, folderout):
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
 
        people = df['People'].sum()
        
        records.append({
            'year':int(year),
            'total items': total_reported_items/people,
            'DRS': sum_DRS/people
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
    
    colors = ['#5C9E4E','#3D6A2C']
    labels = ['total items','DRS']
    
    for col, c in zip(labels, colors):
        ax.plot(results.index, results[col], marker='o', color=c, label=col)
        
    ax.tick_params(colors='white', which='both')
    for spine in ax.spines.values():
        spine.set_color('white')

    ax.set_xlabel('Year', **afont)
    ax.set_ylabel('Number of items', **afont)
    ax.set_title('Total items and DRS items recorded per person', **tfont)
    ax.set_xticks(results.index)
    ax.legend(facecolor=bg_color, edgecolor='white', labelcolor='white')
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    fig.savefig(f'{folderout}/DRS_per_person.png', dpi=300)
    plt.show()

    return results

def create_DRS_per_hour_only(filein, folderout):
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
    
    mins = survey['Time_min']
    hours = []
    for m in mins:
        hour = m/60
        hours.append(hour)
        
    survey['Time_hours'] = hours
    
    years = sorted(survey['year'].unique())
    
    records = []
    
    for year in years:
        df = survey[survey['year'] == year]

        total_reported_items = df[all_items].sum().sum()
        sum_DRS = df[DRS].sum().sum()
 
        hours = df['Time_hours'].sum()
        
        records.append({
            'year':int(year),
            'total items': total_reported_items/hours,
            'DRS': sum_DRS/hours
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
    
    colors = ['#5C9E4E','#3D6A2C']
    labels = ['total items','DRS']
    
    for col, c in zip(labels, colors):
        ax.plot(results.index, results[col], marker='o', color=c, label=col)
        
    ax.tick_params(colors='white', which='both')
    for spine in ax.spines.values():
        spine.set_color('white')

    ax.set_xlabel('Year', **afont)
    ax.set_ylabel('Number of items', **afont)
    ax.set_title('Total items and DRS items recorded per hour', **tfont)
    ax.set_xticks(results.index)
    ax.legend(facecolor=bg_color, edgecolor='white', labelcolor='white')
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    fig.savefig(f'{folderout}/DRS_per_hour.png', dpi=300)
    plt.show()

    return results
