#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 13:32:46 2025

@author: heatherkay
"""


import pandas as pd
import re

#direct from chatgpt after some in depth discussions so may need refining
def count_animal_deaths(df, column="AnimalsInfo", keywords=None):

    if keywords is None:
        keywords = [
            "death", "dead", "meth", "drown",
            "smell", "remain", "entrapment"
        ]

    kw = r"(?:%s)" % "|".join(keywords)
    text = df[column].astype(str).str.lower()
    total = 0

    for cell in text:
        # Count explicit numbers before keywords (e.g. "10 death")
        nums_before = re.findall(rf"(\d+)\s*{kw}", cell)
        total += sum(map(int, nums_before))

        # Count multipliers (e.g. "remains x2")
        multipliers = re.findall(rf"{kw}.*?x\s*(\d+)", cell)
        total += sum(map(int, multipliers))

        # Remove counted patterns to avoid double counting
        cleaned = re.sub(rf"(\d+)\s*{kw}", "", cell)
        cleaned = re.sub(rf"{kw}.*?x\s*\d+", "", cleaned)

        # Count remaining keyword mentions as 1 each
        total += len(re.findall(kw, cleaned))

    return total

def get_country_data(postcodesin, TFTin, folderout):
    """
    A function which takes clean monthly TFT survey data and produces monthly stats
    
    Parameters
    ----------
    
    postcodesin: string
             path to input csv file with postcode, countrywise data    
    
    TFTin: string
             path to input csv file with TFT data
            
    folderout: string
           path to save results
    """
    postcodes_df = pd.read_csv(postcodesin)

    df = pd.read_csv(TFTin)

    df['postcode'] = df['postcode'].astype(str)

    postcodes = []
    for index,i in df.iterrows():
         postcode = i['postcode']
 
         first = postcode.upper()
         new = first.replace(" ","")
         start = new[:4]
         letters = ''.join(x for x in start if x.isalpha())
         postcodes.append(letters)
         
    df['postcode_start'] = postcodes  

    Scotland = []   
    Wales = []
    England = []
    for index,i in postcodes_df.iterrows():
        if i['Country'] == 'Scotland':
            postcode = i['Prefix']
            Scotland.append(postcode)
        elif i['Country'] == 'Wales':
            postcode = i['Prefix']
            Wales.append(postcode)  
        else:
            postcode = i['Prefix']
            England.append(postcode)         

    scots = df[df['postcode_start'].isin(Scotland)].copy()
    cymru = df[df['postcode_start'].isin(Wales)].copy()
    eng = df[df['postcode_start'].isin(England)].copy()


    eng.to_csv(folderout + 'england.csv')
    scots.to_csv(folderout + 'alba.csv')
    cymru.to_csv(folderout + 'cymru.csv')

def get_DRS_data_per_country(TFTin, folderout):
    """
    A function which takes clean monthly TFT survey data and produces monthly stats
    
    Parameters
    ----------
    
    postcodesin: string
             path to input csv file with postcode, countrywise data    
    
    TFTin: string
             path to input csv file with TFT data
            
    folderout: string
           path to save results
    """
    
    from country_data_prep import count_animal_deaths
    
    

    
    results = pd.DataFrame(columns=['country', '% submissions reporting DRS',
                              'total DRS (including glass)','total glass DRS items',
                              'total metal DRS items','total plastic DRS items',
                              'amount of DRS items per km of trail',
                              '% of items surveyed which are DRS (including glass)',
                              '% of DRS items that are glass','% of DRS items that are metal',
                              '% of DRS items that are plastic','total_items',
                              'death','death subs'])
    
    presults = pd.DataFrame(columns=['country', 'region', 'DRS', 'tot_items',
                                     'perc_DRS', 'DRS_subs'])
    
    tresults = pd.DataFrame(columns=['country', 'trail type', 'DRS', 'tot_items',
                                     'perc_DRS', 'DRS_subs'])

    DRS = ['Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
    'Value Aluminium soft drink cans','Value Plastic bottle, top',
    'Value Glass soft drink bottles',
    'Value Plastic energy drink bottles','Value Aluminium energy drink can',
    'Value Aluminium alcoholic drink cans','Value Glass alcoholic bottles']

    DRS_metal = ['Value Aluminium soft drink cans','Value Aluminium energy drink can',
             'Value Aluminium alcoholic drink cans']

    DRS_plastic = ['Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
               'Value Plastic bottle, top','Value Plastic energy drink bottles',]
    
    DRS_glass = ['Value Glass soft drink bottles','Value Glass alcoholic bottles']

    all_items = ['Value Full Dog Poo Bags','Value Unused Dog Poo Bags',
    'Value Toys (eg., tennis balls)','Value Other Pet Related Stuff',
    'Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
    'Value Aluminium soft drink cans','Value Plastic bottle, top','Value Glass soft drink bottles',
    'Value Plastic energy drink bottles','Value Aluminium energy drink can',
    'Value Plastic energy gel sachet','Value Plastic energy gel end',
    'Value Aluminium alcoholic drink cans',
    'Value Glass alcoholic bottles','Value Glass bottle tops',
    'Value Hot drinks cups',
    'Value Hot drinks tops and stirrers',
    'Value Drinks cups (eg., McDonalds drinks)',
    'Value Drinks tops (eg., McDonalds drinks)','Value Cartons',
    'Value Plastic straws',
    'Value Paper straws','Value Plastic carrier bags','Value Plastic bin bags',
    'Value Confectionary/sweet wrappers','Value Wrapper "corners" / tear-offs',
    'Value Other confectionary (eg., Lollipop Sticks)','Value Crisps Packets',
    'Value Used Chewing Gum','Value Plastic fast food, takeaway and / or on the go food packaging, cups, cutlery etc',
    'Value Other fast food, takeaway and / or on the go food packaging, cups, cutlery (eg., cardboard)',
    'Value Disposable BBQs and / or BBQ related items','Value BBQs and / or BBQ related items',
    'Value Food on the go (eg.salad boxes)','Value Homemade lunch (eg., aluminium foil, cling film)',
    'Value Fruit peel & cores','Value Cigarette Butts','Value Smoking related',
    'Value Disposable vapes','Value Vaping / E-Cigarette Paraphernalia','Value Drugs related',
    'Value Farming','Value Salt/mineral lick buckets','Value Silage wrap',
    'Value Forestry','Value Tree guards','Value Industrial','Value Cable ties',
    'Value Industrial plastic wrap','Value Toilet tissue','Value Face/ baby wipes',
    'Value Nappies','Value Single-Use Period products','Value Single-Use Covid Masks',
    'Value Rubber/nitrile gloves','Value Outdoor event (eg Festival)','Value Camping',
    'Value Halloween & Fireworks','Value Seasonal (Christmas and/or Easter)',
    'Value Normal balloons','Value Helium balloons','Value MTB related (e.g. inner tubes, water bottles etc)',
    'Value Running','Value Roaming and other outdoor related (e.g. climbing, kayaking)',
    'Value Outdoor sports event related (e.g.race)','Value Textiles','Value Clothes & Footwear',
    'Value Plastic milk bottles','Value Plastic food containers','Value Cardboard food containers',
    'Value Cleaning products containers','Value Miscellaneous','Value Too small/dirty to ID',
    'Value Weird/Retro']
    
    trail_types = ['TypeMrkdTrails','TypeRoW','TypeUnofficial','TypePump','TypeUrban',
    'TypeOtherTrails','TypeAccess','TypeCar','TypeOther']
    
    trail_zones = ['ZonesTrails','ZonesFootpaths','ZonesUnofficial','ZonesPump',
    'ZonesUrban','ZonesOtherTrails','ZonesAccess','ZonesCar','ZonesOther']
    
    dfs = ['england', 'alba', 'cymru']    

        
    for x in dfs:
        survey = pd.read_csv(TFTin + x + '.csv')
        
        #survey[trail_types] = survey[trail_types].combine_first(survey[trail_zones])
        trail_types_exist = [c for c in trail_types if c in survey.columns]
        trail_zones_exist = [c for c in trail_zones if c in survey.columns]

# double-check lengths match
        assert len(trail_types_exist) == len(trail_zones_exist), "Column lists must be same length and exist in df"

# combine
        for a, b in zip(trail_types_exist, trail_zones_exist):
            survey[a] = survey[a].combine_first(survey[b])

        DRS_submissions = []
        DRS_glass_ttl = []
        df2 = survey
        #df2 = survey[survey['MoreInfoY'].notna()] 
        #subs = len(df2.index)
        for index, i in df2.iterrows():
            DRS_items = i[DRS].sum() 
            glass_itms = i[DRS_glass].sum()
            if DRS_items > 0:
                DRS_submissions.append(DRS_items)
            DRS_glass_ttl.append(glass_itms)
        df_DRS = df2.reindex(columns = DRS)
        DRS_items = df_DRS.sum(axis=1).to_list()     
        DRS_subs_list = [x for x in DRS_items if x != 0.0]
        DRS_subs = len(DRS_subs_list)

        df_DRS_glass = df2.reindex(columns = DRS_glass)
        DRS_items_glass = df_DRS_glass.sum(axis=1).to_list()     
        DRS_subs_glass = [x for x in DRS_items_glass if x != 0.0]

        df_DRS_metal = df2.reindex(columns = DRS_metal)
        DRS_items_metal = df_DRS_metal.sum(axis=1).to_list()     
        DRS_subs_metal = [x for x in DRS_items_metal if x != 0.0]

        df_DRS_plas = df2.reindex(columns = DRS_plastic)
        DRS_items_plas = df_DRS_plas.sum(axis=1).to_list()     
        DRS_subs_plas = [x for x in DRS_items_plas if x != 0.0]

        df2[all_items] = df2[all_items].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)
        reported_items = df2[all_items].sum(axis=0).to_list()
        total_reported_items = sum(reported_items)
    
#% Submissions reporting DRS                
       # DRS_reported = (DRS_subs/subs)*100
#DRS total items
        DRS_tot_items = sum(DRS_subs_list)
#DRS total glass, metal and plastic items
        DRS_tot_glass = sum(DRS_subs_glass)
        DRS_tot_metal = sum(DRS_subs_metal)
        DRS_tot_plas = sum(DRS_subs_plas)

    
    
        survey_km = df2['Distance_km'].sum()

#% of total items that are DRS - from those reporting breakdown
        DRS_proportion = (DRS_tot_items/total_reported_items)*100
#%of DRS items that are glass, metal, plastic    
        glass_DRS_proportion = (DRS_tot_glass/DRS_tot_items)*100
        metal_DRS_proportion = (DRS_tot_metal/DRS_tot_items)*100
        plastic_DRS_proportion = (DRS_tot_plas/DRS_tot_items)*100
#% of total items that are glass DRS
        glass_proportion = (DRS_tot_glass/total_reported_items)*100 
        DRS_prevalence = DRS_tot_items/survey_km
        DRS_proportion = DRS_tot_items/total_reported_items
        
        
        survey_AIcols = ['AnimalsY','AnimalsN','AnimalsInfo']
        '''
        if 'AnimalsInfo' in survey.columns and survey['AnimalsInfo'].notna().any():
            regex = r'(?:death|dead|meth|drown|smell|remains|entrapment)'
            survey['death_count'] = (survey['AnimalsInfo'].astype(str).str.lower().str.count(regex))
        
        else:
            death = 0
        '''   
        AI_survey = survey[survey_AIcols].notna().any(axis=1).sum()
        deaths = []
        
        df = survey
        death = count_animal_deaths(df, column="AnimalsInfo")
        deaths.append(death)  
            
        tot_deaths = sum(deaths)
        
        postcodes = df['postcode_start'].unique()
        for p in postcodes:
            mask = df['postcode_start'] == p
            pDRS = df.loc[mask, DRS].sum().sum()
            count = mask.sum()    
            pall_items = df.loc[mask, all_items].sum().sum() 
            percent_DRS = pDRS/pall_items*100
            
            
            
            pnew_row = pd.DataFrame([{'country':x, 'region':p, 
                            'DRS':pDRS, 'tot_items':pall_items,
                            'perc_DRS':percent_DRS, 'DRS_subs':count}])
            
            presults = pd.concat([presults, pnew_row],  ignore_index = True)

        dft = df[df[trail_types].notna().sum(axis=1) == 1]
        for t in trail_types:
            tmask = dft[t].notna()
            tDRS = dft.loc[tmask, DRS].sum().sum()
            tcount = tmask.sum()    
            tall_items = dft.loc[tmask, all_items].sum().sum() 
            tpercent_DRS = tDRS/tall_items*100
            
            tnew_row = pd.DataFrame([{'country':x, 'trail type':t, 
                            'DRS':tDRS, 'tot_items':tall_items,
                            'perc_DRS':tpercent_DRS, 'DRS_subs':tcount}])
            
            tresults = pd.concat([tresults, tnew_row],  ignore_index = True)


        new_row = pd.DataFrame([{'country':x, #'% submissions reporting DRS':DRS_reported,
                              'total DRS (including glass)':DRS_tot_items,'total glass DRS items':DRS_tot_glass,
                              'total metal DRS items':DRS_tot_metal,'total plastic DRS items':DRS_tot_plas,
                              'amount of DRS items per km of trail':DRS_prevalence,
                              '% of items surveyed which are DRS (including glass)':DRS_proportion,
                              '% of DRS items that are glass':glass_DRS_proportion,
                              '% of DRS items that are metal':metal_DRS_proportion,
                              '% of DRS items that are plastic':plastic_DRS_proportion,
                              'total_items':total_reported_items, 'death':tot_deaths,
                              'death subs':AI_survey}]) 
        
        results = pd.concat([results, new_row], ignore_index = True)
    
    results.to_csv(folderout + 'DRS.csv',index=False)
    presults.to_csv(folderout + 'regions_DRS.csv',index=False)
    tresults.to_csv(folderout + 'trail_DRS.csv',index=False)
    
    
    

        
        
        

