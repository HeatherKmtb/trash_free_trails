#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:16:01 2026

@author: heatherfriendship
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def create_single_composition_pie_DRS_EPR_poo_cigs(filein, folderout, title):
    df = pd.read_csv(filein)

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
    'Value Too small/dirty to ID','Value Other Miscellaneous'
    ]

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
    
    plt.title(title, fontdict = tfont)
    plt.savefig(folderout + '/composition.png', bbox_inches='tight',
                facecolor = bg_color, edgecolor='none')
    plt.close
    
def four_comparison_composition_pies_one_df(TFTin, toptitle, TFTout):
    """
    A function which takes prepared TFT survey data of 4 different groups or locations
    and produces a visualisation with 4 different pie charts
    
    Parameters
    ----------
    
    df01-df04: strings
             path to input prepped csvs
             
    toptitle: string
            title for top of visualisation
            
    title1-title4: strings
            titles for each specific group or region
            
    TFTout: string
           path for folder to save results in
    """
    
#figure this out
    df = pd.read_csv(TFTin)
 
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
    
    #poo = ['Value Outdoor event related (e.g.race)',
    #'Value Biking specific','Value Hiking specific','Value Other outdoor related','Value Cable ties']
    
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
    'Value Too small/dirty to ID','Value Other Miscellaneous'
    ]
       
    nicotine = ['Value Cigarette Butts','Value Nicotine pouches','Value Disposable vapes',
            'Value Nicotine related packaging','Value Other nicotine related'
            ]
    
    bg_color = '#312e30'
    
    fig = plt.figure(figsize=(8, 8))
    fig.patch.set_facecolor(bg_color)
    
    fig.suptitle(
        toptitle,
        fontsize=16,
        fontweight='bold',
        color='white'
    )
    
    df[all_items] = df[all_items].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)
    
    for i in range(4):
        #Resolve nan issues
        row = df.iloc[i]
        row_title = row['postcode']

        # Select the current subplot position (1 to 4)
        ax = plt.subplot(2, 2, i + 1)
        ax.set_facecolor(bg_color)

        drs_sum = row[DRS].sum()
        epr_sum = row[EPR].sum()
        poo_sum = row[poo].sum()
        tot_sum = row[all_items].sum()
        nico_sum = row[nicotine].sum()
        
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

        plt.title(f"{row_title}\nTotal Surveyed Items: {(tot_sum):,}", fontdict = tfont)
        
      
    #vertical line    
    fig.add_artist(
        plt.Line2D(
            [0.5, 0.5], [0.05, 0.85],
            transform=fig.transFigure,
            color='#A0AEC0',
            linewidth=1,
            linestyle='-'))

    #horizontal line
    fig.add_artist(
        plt.Line2D(
            [0.05, 0.95], [0.45, 0.45],
            transform=fig.transFigure,
            color='#A0AEC0',
            linewidth=1,
            linestyle='-'))

    # Leave room for suptitle
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.gcf().set_facecolor(bg_color)

    plt.savefig(TFTout + 'SUP_composition_comparison.png', dpi=300, facecolor = bg_color, edgecolor='none')
    plt.close()
    
def single_nature_connection_pie(df01, df02, df03, df04, toptitle, title1, title2, title3,
                                     title4, TFTout):
    """
    A function which takes prepared TFT survey data of 4 different groups or locations
    and produces a visualisation with 4 different pie charts
    
    Parameters
    ----------
    
    df01-df04: strings
             path to input prepped csvs
             
    toptitle: string
            title for top of visualisation
            
    title1-title4: strings
            titles for each specific group or region
            
    TFTout: string
           path for folder to save results in
    """
    

    df1 = pd.read_csv(df01)
    df2 = pd.read_csv(df02)
    df3 = pd.read_csv(df03)
    df4 = pd.read_csv(df04)

    df_titles = [title1, title2, title3, title4]
    dataframes = [df1, df2, df3, df4]
    
    bg_color = '#312e30'
        
    #Place connection comparison
    
    fig = plt.figure(figsize=(8, 8))
    fig.patch.set_facecolor(bg_color)
    
    fig.suptitle(
        'Comparison of feelings of connection across regions',
        fontsize=16,
        fontweight='bold',
        color='white'
        )
    
    for i,df in enumerate(dataframes):
        survey_place = df['Experience_Nature'] >= 6
        s_place = (survey_place == True).sum()
        
        equal_place = df['Experience_Nature'] == 5
        e_place = (equal_place == True).sum()
        
        less_place = df['Experience_Nature'] <= 4
        l_place = (less_place == True).sum()
        
        sp_rows = df['Experience_Nature'].notna().sum()
        
        #perc_more_pconnected = (s_place/sp_rows) *100
        
        raw_labels = ['% feeling more connected', '% not feeling equally connected',
                  '% feeling less connected']
        raw_values = [s_place, e_place, l_place]
        
        raw_colors = ['#223B18','#3D6A2C','#599B40']
        
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
        
        labels = []
        values = []
        colors = []
        
        for label, val, color in zip(raw_labels, raw_values, raw_colors):
            if val > 0 and pd.notna(val):  # Ensures it's greater than 0 and not empty
                labels.append(label)
                values.append(val)
                colors.append(color)
        
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
        
        for autotext in autotexts:
            autotext.set_color('white')           #text inside wedges    
            autotext.set_weight('bold')             

        plt.title(f"{df_titles[i]}\nNumber of submissions: {(sp_rows):,}", fontdict = tfont)
        
      
    #vertical line    
    fig.add_artist(
        plt.Line2D(
            [0.5, 0.5], [0.05, 0.85],
            transform=fig.transFigure,
            color='#A0AEC0',
            linewidth=1,
            linestyle='-'))

    #horizontal line
    fig.add_artist(
        plt.Line2D(
            [0.05, 0.95], [0.45, 0.45],
            transform=fig.transFigure,
            color='#A0AEC0',
            linewidth=1,
            linestyle='-'))

    # Leave room for suptitle
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.gcf().set_facecolor(bg_color)

    plt.savefig(TFTout + 'Nature_connection.png', dpi=300, facecolor = bg_color, edgecolor='none')
    plt.close()
    

def before_and_after_experience(TFTin, folderout):
    df = pd.read_csv(TFTin + 'experience.csv')
    
    experience_cols = [col for col in df.columns if col.startswith('AExperience_') or col.startswith('BExperience_')]

    # Convert all identified columns to standard integers
    for col in experience_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64')
       
    # 2. Dynamically extract the 10 unique 'xxx' options from column names
    xxx_options = set()
    for col in df.columns:
        if col.startswith('AExperience_'):
            xxx_options.add(col.replace('AExperience_', ''))
        elif col.startswith('BExperience_'):
            xxx_options.add(col.replace('BExperience_', ''))
    
    categories = sorted(list(xxx_options))
    print(f"Detected categories: {categories}")
    
    # 3. GRAPH 1: Line Graph for Average Scores
    a_means = [df[f'AExperience_{cat}'].mean() for cat in categories]
    b_means = [df[f'BExperience_{cat}'].mean() for cat in categories]
    
    # Build line chart
    bg_color = '#312e30'
    fig, ax = plt.subplots(figsize=(12, 6), facecolor=bg_color)
    
    ax.set_facecolor(bg_color)
    
    ax.plot(categories, a_means, marker='o', linewidth=4, color='#78B062', label='After')
    ax.plot(categories, b_means, marker='s', linewidth=4, color='#3D6A2C', label='Before')
    
    afont = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 12,
        'color' : 'white'
        }
    
    tfont = {'family' : 'sans-serif',
        'weight' : 'bold',
        'size'   : 18,
        'color' : 'white'
        }
    
    ax.set_xlabel('Experience Categories', **afont)
    ax.set_ylabel('Average Score', **afont)
    ax.set_title('Comparison of Average Experience Scores: Before vs After', **tfont, pad=15)
    ax.set_ylim(0, 10)  # Scores are between 0 and 7
    #ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(facecolor=bg_color, edgecolor='white', labelcolor='white')
    
    ax.tick_params(colors='white', which='both')
    
    for spine in ax.spines.values():
        spine.set_color('white')
    
    plt.tight_layout()
    plt.savefig(folderout + 'average_scores_line_graph.png', bbox_inches='tight', 
                facecolor = bg_color, edgecolor='none', dpi=300)
    plt.close()
    
    
    # 4. GRAPHS 2-4: Side-by-side Pie Charts for Place, Nature, and Others
    pie_categories = ['Place', 'Nature', 'Others']
    
    # Create a consistent color palette for choices 0 through 7
    colors = plt.cm.tab20(np.linspace(0, 1, 8)) 
    
    for cat in pie_categories:
        # Ensure the columns exist before plotting
        a_col = f'AExperience_{cat}'
        b_col = f'BExperience_{cat}'
        
        if a_col in df.columns and b_col in df.columns:
            # Reindex to range(8) ensures scores 0-7 are consistently aligned, filling missing values with 0
            a_counts = df[a_col].value_counts().reindex(range(8), fill_value=0)
            b_counts = df[b_col].value_counts().reindex(range(8), fill_value=0)
            
            # Setup side-by-side layout (1 row, 2 columns)
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
            labels = [f'Score {i}' for i in range(8)]
            
            # Plot A Pie Chart
            ax1.pie(a_counts, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, 
                    textprops={'fontsize': 10})
            ax1.set_title(f'A Experience: {cat}', fontsize=12, weight='bold')
            
            # Plot B Pie Chart
            ax2.pie(b_counts, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, 
                    textprops={'fontsize': 10})
            ax2.set_title(f'B Experience: {cat}', fontsize=12, weight='bold')
            
            # Main title for the shared graph
            plt.suptitle(f'Score Distribution Comparison (0-7) for "{cat}"', fontsize=16, weight='bold', y=0.98)
            plt.tight_layout()
            plt.savefig(folderout + f'pie_charts_{cat.lower()}.png', dpi=300)
            plt.close()
        else:
            print(f"Warning: Columns for '{cat}' were not found in the dataset.")
    
    print("All charts generated and saved successfully!")

 
    
