#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:03:57 2026

@author: heatherkay
"""

import pandas as pd
import matplotlib.pyplot as plt

'''
colour codes:
DIO gold BCA25D
Trail Clean Green 3D6A2C
Emergence green 00945C
SoOT green 859150
NC blue 70ADA3
TMA red BA3F0F
AT/CH blue 508591
PA orange E3761C

TFR '#e5582e', '#f4a71c', '#072340', '#faf9ef'

'''


def loughrigg_stats_and_graphs(TFTin, folderout):
    """
    A function which takes clean monthly TFT survey data and produces monthly stats
    
    Parameters
    ----------
    
    TFTin: string
             path to input csv of Loughrigg data
            
    folderout: string
           path for folder to save results in
    """

    
    #create df for results - or could read in and append to overall stats sheet
    results = pd.DataFrame(columns = ['no_people','distance_km','duration_hours', 
                                      'total_items'
                                      ])
        
    survey = pd.read_csv(TFTin)
        
    #Overview - volunteers, distance, hours, items
    mins = survey['Time_min']
    hours = []
    for m in mins:
        hour = m/60
        hours.append(hour)
        
    survey['Time_hours'] = hours    
    
    total_people = survey['People'].sum()
    total_time = (survey['People'] * survey['Time_hours']).sum()
    km = survey['Distance_km'].sum()

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

    total_items = survey['TotItems'].sum()   
   
    new_row = pd.DataFrame([{'no_people':total_people, 'distance_km':km,
                              'duration_hours':total_time, 'total_items':total_items
                              }])
    
    results= pd.concat([results, new_row], ignore_index=True) 
                                        
    
    results.to_csv(folderout + '/overview.csv',index=False)  

    df = survey 
    
    items = df['TotItems']
    people = df['People']
    df['items pp'] = items/people
    #plot items, people, items per person

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12), sharex=True)
    
    afont = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 18}
    
    tfont = {'family' : 'sans-serif',
        'weight' : 'bold',
        'size'   : 18}

    ax1.plot(df['Date_TrailClean'], df['TotItems'], color='black', marker='o', linestyle='-')
    ax1.set_ylabel('Total Items', **afont)
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.set_title('Number of items and volunteers per clean', **tfont, pad=15)

    ax2.plot(df['Date_TrailClean'], df['People'], color='#3D6A2C', marker='s', linestyle='-')
    ax2.set_ylabel('Number of People', **afont)
    ax2.grid(True, linestyle='--', alpha=0.5)

    ax3.plot(df['Date_TrailClean'], df['items pp'], color='#BCA25D', marker='^', linestyle='-')
    ax3.set_ylabel('Items per person', **afont)
    ax3.set_xlabel('Date', **afont)
    ax3.grid(True, linestyle='--', alpha=0.5)
    

    plt.tight_layout()
    plt.savefig(folderout + '/stats.png', bbox_inches='tight')
    plt.close


    #plot DRS, EPR and poo items
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
    
    
    df['DRS_sum'] = df[DRS].sum(axis=1)
    df['EPR_sum'] = df[EPR].sum(axis=1)
    df['poo'] = df[poo].sum(axis=1)

    df_sorted = df

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar(df_sorted['Date_TrailClean'], df_sorted['TotItems'], color='#223B18', label='Other Items')
    ax.bar(df_sorted['Date_TrailClean'], df_sorted['DRS_sum'] + df_sorted['EPR_sum'] + df_sorted['poo'], color='#3D6A2C', label='dog poo')
    ax.bar(df_sorted['Date_TrailClean'], df_sorted['DRS_sum'] + df_sorted['EPR_sum'], color='#599B40', label='pEPR Items')
    ax.bar(df_sorted['Date_TrailClean'], df_sorted['DRS_sum'], color='#84C26C', label='DRS Items')
    
    afont = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 12}
    
    tfont = {'family' : 'sans-serif',
        'weight' : 'bold',
        'size'   : 18}


    ax.set_xlabel('Date', **afont)
    ax.set_ylabel('Total Items', **afont)
    ax.set_title('Items per Trail Clean Breakdown', **tfont, pad=15)
    ax.legend()

    # Rotate x-axis labels to prevent overlapping
    plt.xticks(rotation=45, ha='right')

    plt.savefig(folderout + '/total_items.png', bbox_inches='tight')
    plt.close
    

def comparison_graphs(TFTin, TFTout):
    """
    A function which takes prepared TFT survey data for different regions
    and produces graphs for BBC
    
    Parameters
    ----------
    
    TFTin: string
             path to input folder with prepped csvs
            
    folderout: string
           path for folder to save results in
    """
    
    loughrigg = pd.read_csv(TFTin + 'survey.csv')
    lakes = pd.read_csv(TFTin + 'lakes.csv')
    england = pd.read_csv(TFTin + 'england.csv')
    gb = pd.read_csv(TFTin + 'GB.csv')

    df_titles = ["Loughrigg Fell and Rydal caves", "Lake District", "England", "Great Britain"]
    dataframes = [loughrigg, lakes, england, gb]
    
    
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
       
    
    bg_color = '#1A1A1A'
  
    for i, df in enumerate(dataframes):
        #Resolve nan issues
        df[all_items] = df[all_items].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

        # Select the current subplot position (1 to 4)
        ax = plt.subplot(2, 2, i + 1)
        ax.set_facecolor(bg_color)

        drs_sum = df[DRS].sum().sum()
        epr_sum = df[EPR].sum().sum()
        poo_sum = df[poo].sum().sum()
        tot_sum = df[all_items].sum().sum()
    
        
        other_sum = tot_sum - (drs_sum + epr_sum + poo_sum)
    
        # Define initial labels and values
        labels = ['DRS', 'EPR', 'Dog poo','Other']
        values = [drs_sum, epr_sum, poo_sum, other_sum]
        
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
        
        colors = ['#223B18','#3D6A2C','#599B40','#84C26C']
        
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

        plt.title(f"{df_titles[i]}\nTotal Items: {tot_sum}", fontdict = tfont)
        
    plt.tight_layout()
    plt.gcf().set_facecolor(bg_color)

    plt.savefig(TFTout + 'SUP_composition.png', dpi=300, facecolor = bg_color, edgecolor='none')
    plt.close()
 
    
    #Animal interaction comparison
    for i,df in enumerate(dataframes):
        survey_AIcols = ['AnimalsY','AnimalsN']

        subs_tot = df[survey_AIcols].notna().any(axis=1).sum()

        AI_tot = df['AnimalsY'].value_counts().get('Yes', 0)
    
        #percent submissions reporting AI observed
        perc_AI = (AI_tot/subs_tot)*100
    
        ai_death_clean = df['AIDeath'].replace(['X', 'x'], 1)
        ai_death_numerical = pd.to_numeric(ai_death_clean, errors='coerce')
    
        tot_deaths = ai_death_numerical.sum()

        #percent submissions reporting death of those reporting they checked for AI  
        perc_death = (tot_deaths/subs_tot)*100
        
        #preparing for the pie chart
        not_AI = 100 - perc_AI
        AI_remaining = perc_AI - perc_death
        AI_death = perc_death
    
        raw_values = [not_AI, AI_remaining, AI_death]
        raw_labels = ['No observed animal interaction', 'Animal Interaction', 'Evidence of Death']
        raw_colors = ['#223B18', '#3D6A2C', '#3D6A2C']
        
        # Build values dynamically: Skip AI_death if it equals 0
        values = []
        labels = []
        colors = []
        death_wedge_idx = None # Keeps track of where the death wedge lands
        
        
        for idx, (val, label, col) in enumerate(zip(raw_values, raw_labels, raw_colors)):
            if idx == 2 and val == 0:
                continue # Skip adding the 'Evidence of Death' slice completely
            
            values.append(val)
            labels.append(label)
            colors.append(col)
            
            if idx == 2:
                # If we added the death slice, mark its new index position
                death_wedge_idx = len(values) - 1
        
        afont = {'family' : 'sans-serif',
            'weight' : 'normal',
            'size'   : 4,
            'color'  : '#FFFFFF'
            }
        ax = plt.subplot(2, 2, i + 1)
        ax.set_facecolor(bg_color)
        
        wedges, texts, autotexts = ax.pie(
            values,
            labels=labels,
            colors=colors,
            autopct='%1.1f%%',
            startangle=140,
            counterclock=False,
            textprops=dict(**afont)
            )
        
        if death_wedge_idx is not None:
            wedges[2].set_hatch('////') 

        
        for autotext in autotexts:
            autotext.set_color('white')           #text inside wedges     
            autotext.set_weight('bold')             

        plt.title(f"{df_titles[i]}\nTotal Items: {tot_sum}", fontdict = tfont)


    plt.tight_layout()
    plt.gcf().set_facecolor(bg_color)

    plt.savefig(TFTout + 'Animal Interaction.png', dpi=300, facecolor = bg_color, edgecolor='none')
  
