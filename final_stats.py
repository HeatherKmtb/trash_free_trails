#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:29:33 2025

@author: heatherkay
"""

import pandas as pd

def overview_stats(folderin, folderout):
    """
    A function which takes clean monthly TFT survey data and produces monthly stats
    
    Parameters
    ----------
    
    folderin: string
             path to input folder with csv files with monthly TFT data
            
    folderout: string
           path for folder to save results in
    """

    
    #create df for results - or could read in and append to overall stats sheet
    results = pd.DataFrame(columns = ['total_submisssions', 'total_count', 
                                      'total_survey', 'total_lite', 'trash_watch',
                                      'no_people','area_km2','distance_km','duration_hours', 
                                      'items_removed','items_surveyed', 'total_items',
                                      'total_kg','total_cokecans','Adjusted Total Items'])
    
      
    survey = pd.read_csv(folderin + 'survey.csv')
    lite = pd.read_csv(folderin + 'lite.csv')
    count = pd.read_csv(folderin + 'count.csv')
    CSsurvey = pd.read_csv(folderin + 'CS_survey.csv')
    CScount = pd.read_csv(folderin + 'CS_count.csv')
    bag_res_lite = pd.read_csv(folderin + 'bag_res_lite.csv')
    tfr = pd.read_csv(folderin + 'TFR.csv')
    
    dfs = [survey, CSsurvey, CScount]
    
    #total submmissions before any filtering
    count_survey = len(survey.index)    
    count_lite = len(lite.index)
    count_count = len(count.index)
    count_CSsurvey = len(CSsurvey.index)
    count_CScount = len(CScount.index)
    
    #Overview Stats - submitted data

    CS = [count_survey, count_lite, count_count, count_CSsurvey,
                            count_CScount]
#Total combined data sets submitted
    total_CS = sum(CS)
    cnt = [count_count, count_CScount]
#Total Count Datasets
    total_count = sum(cnt)
    srvy = [count_survey, count_CSsurvey]
#Total survey dasets
    total_survey = sum(srvy)
#Total lite datasets calculated as count_lite
    
    
    #Overview - volunteers, distance, hours, items
    mins = survey['Time_min']
    hours = []
    for m in mins:
        hour = m/60
        hours.append(hour)
        
    survey['Time_hours'] = hours    
    
    tot_people = []
    tot_time = []

    for df in dfs: #survey, CSsurvey & CS count
        people = df['People'].sum()
        hours = df['Time_hours'].sum()
        #km = df['Distance_km'].sum()
        #items = df['TotItems'].sum()
        tot_people.append(people)
        tot_time.append(hours)
        #tot_km.append(km)
        #tot_items.append(items)
    
    #add to total people the number of lite and count submissions
    lite_people = count_lite * 3.08
    tot_people.append(lite_people)
    tot_people.append(count_count)
 
#volunteers
    total_people = sum(tot_people)
    
    survey_km = survey['Distance_km'].sum()
    count_m = count['Total_distance(m)'].sum()
    count_km = count_m / 1000
    CScount_m = CScount['Total_distance(m)'].sum()
    CScount_km = CScount_m / 1000
    lite_km = count_lite * 6.77
    
    survey_area = survey_km * 0.006
    lite_area = lite_km * 0.006
    CSsurvey_area = CSsurvey['Area_km2'].sum()
    
    areas = [survey_area, CSsurvey_area, lite_area]
#area cleaned / surveyed
    area = sum(areas)   
    
    CSsurvey_km = CSsurvey_area / 0.006
    kms = [survey_km, count_km, CScount_km, lite_km]
#distance cleaned / surveyed 
    km = sum(kms)
        
    #method to estimate time spent on count
    count_time = count_count * 1.38
    lite_time = count_lite * 1.64
    tot_time.append(count_time)
    tot_time.append(lite_time)
#time 
    total_time = sum(tot_time) 

    all_items = ['Value Full Dog Poo Bags','Value Unused Dog Poo Bags',
    'Value Toys (eg., tennis balls)','Value Other Pet Related Stuff',
    'Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
    'Value Aluminium soft drink cans','Value Plastic bottle, top','Value Glass soft drink bottles',
    'Value Plastic energy drink bottles','Value Aluminium energy drink can',
    'Value Plastic energy gel sachet','Value Plastic energy gel end','Value Aluminium alcoholic drink cans',
    'Value Glass alcoholic bottles','Value Glass bottle tops','Value Hot drinks cups',
    'Value Hot drinks tops and stirrers','Value Drinks cups (eg., McDonalds drinks)',
    'Value Drinks tops (eg., McDonalds drinks)','Value Cartons','Value Plastic straws',
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
    
    
    # Apply conversion to both DataFrames individually
    for df in [survey, CSsurvey]:
        df[all_items] = df[all_items].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

    # Now they both have clean numeric columns
    combined = pd.concat([survey, CSsurvey], ignore_index=True)

    # Summation works the same
    reported_items = combined[all_items].sum(axis=0).to_list()
    
    '''
    combined = pd.concat([survey, CSsurvey], ignore_index=True)

    # Convert to numeric, replace errors with NaN, then fill with 0 and cast to int
    combined[all_items] = combined[all_items].apply(lambda col: pd.to_numeric(col, errors='coerce')).fillna(0).astype(int)

    reported_items = combined[all_items].sum(axis=0).to_list()
    '''
    total_reported_items = sum(reported_items)
    
    srvy_items = []
    rmv_items = []       
        
    survey_items = survey['TotItems'].sum()   
    srvy_items.append(survey_items)
    rmv_items.append(survey_items)
    
    CSsurvey_items = CSsurvey['TotItems'].sum()   
    srvy_items.append(CSsurvey_items)
    rmv_items.append(CSsurvey_items)
    
    lite_items = bag_res_lite['TotItems'].sum() 
    rmv_items.append(lite_items)
    
    count_items = count['TotItems'].sum() 
    srvy_items.append(count_items)
    
    CScount_items = CScount['TotItems'].sum() 
    srvy_items.append(CScount_items)
    
    tfr_items = tfr['TotItems'].sum()
    srvy_items.append(tfr_items)
    rmv_items.append(tfr_items)
    
    removed_items = sum(rmv_items)
    surveyed_items = sum(srvy_items)   
#total removed items (reported)
    total_items = surveyed_items + lite_items

#weight removed items
    total_kg = removed_items / 57  
#volume of removed items as number of coke cans
    total_cokecans = removed_items / 1.04
    
    ATI_srvy = survey['AdjTotItems']
    ATI_srvy_correct_itms = [x for x in ATI_srvy if str(x) != '#DIV/0!']
    ATI_srvy_correct = [float(i) for i in ATI_srvy_correct_itms]
    ATI_survey = sum(ATI_srvy_correct)
    
    ATIs = []
    for index, i in CSsurvey.iterrows():
        TotItems = i['TotItems']#.astype(float)
        people = i['People']#.astype(float)
        hours = i['Time_hours']#.astype(float)
        time = hours*60
        area = i['Area_km2']#.astype(float)
        dist = area / 0.006
        #calculate ATI
        denominator = (people*time)*dist
        if denominator == 0:
            continue
        AdjTotItems = TotItems/denominator 
        if AdjTotItems > 0:
            ATIs.append(AdjTotItems)
        
        
    for index, i in count.iterrows():
        TotItems = i['TotItems']#.astype(float)
        people = i['People']#.astype(float)
        time = 1.38
        m = i['Total_distance(m)']#.astype(float)
        kmc = m / 1000
        #calculate ATI
        denominator = (people*time)*kmc
        if denominator == 0:
            continue
        AdjTotItems = TotItems/denominator     
        if AdjTotItems > 0:
            ATIs.append(AdjTotItems)

    for index, i in CScount.iterrows():
        TotItems = i['TotItems']#.astype(float)
        people = i['People']#.astype(float)
        hours = i['Time_hours']#.astype(float)
        time = hours*60
        m = i['Total_distance(m)']#.astype(float)
        kmcs = m / 1000
        #calculate ATI
        denominator = (people*time)*kmcs
        if denominator == 0:
            continue
        AdjTotItems = TotItems/denominator     
        if AdjTotItems > 0:
            ATIs.append(AdjTotItems) 
              
    
    lite_denom = (lite_people*lite_time)*lite_km
    if lite_denom == 0.0:
        ATI_lite = 0.0
    else:
        ATI_lite = lite_items/lite_denom
    
    ATI_next = sum(ATIs)
#Adjusted total items    
    ATI = ATI_next + ATI_lite + ATI_survey
    
    new_row = pd.DataFrame([{'total_submisssions':total_CS, 'total_count':total_count,
                              'total_survey':total_survey, 'total_lite': count_lite,
                              'no_people':total_people, 
                              'area_km2':area, 'distance_km':km,
                              'duration_hours':total_time, 'items_removed':removed_items,
                              'items_surveyed':surveyed_items, 'total_items':total_items,
                              'total_kg':total_kg,'total_cokecans':total_cokecans,
                              'Adjusted Total Items':ATI}])
    results= pd.concat([results, new_row], ignore_index=True) 
                                        
    
    results.to_csv(folderout + '/overview.csv',index=False)    
    
    count = count.rename(columns={'ZMostonesAlmostHome':'MostZonesAlmostHome'})
    count = count.rename(columns={'MostZonesLunch':'MostZonesPicnic'})
    
    

    count_results = pd.DataFrame(columns = ['count_submisssions', 'prevalence', 'hotspots',
                                      'worst_zone'])
    
    #this will only work once dfs are the same 
    #dfs = (count, CScount) 
    #df = pd.concat(dfs, ignore_index = True) 
    #km = df['Distance_km'].sum()
    #items = df['TotItems'].sum()  
    #prevalence = items/km
    count_df1 = count[count['TotItems'].notna()]
    count_df2 = count_df1[count_df1['Total_distance(m)'].notna()]
    CScount_df1 = CScount[CScount['TotItems'].notna()]
    CScount_df2 = CScount_df1[CScount_df1['Total_distance(m)'].notna()]   
    count_ms = count_df2['Total_distance(m)'].sum()
    count_kms = count_ms / 1000
    CScount_ms = CScount_df2['Total_distance(m)'].sum()
    CScount_kms = CScount_ms / 1000
    count_itms = count_df2['TotItems'].sum()
    CScount_itms = CScount_df2['TotItems'].sum()
    
    
    distance = CScount_kms + count_kms
    items = CScount_itms + count_itms
#how much is out there per km
    prevalence = items/distance
    
#hot spots????
    

    mostzonesindy = ['MostZonesCarpark','MostZonesVisitorInfrastructure','MostZonesTrailMaps',
    'MostZonesTrailhead','MostZonesDogPoo','MostZonesShakedown','MostZonesTopClimb',
    'MostZonesView','MostZonesPicnic','MostZonesRoadCrossing','MostZonesSwimspot',
    'MostZonesBottomDescent','MostZonesJumps','MostZonesPause','MostZonesAlmostHome',
    'MostZonesLake','MostZonesRiver','MostZonesBeach','MostZonesSanddunes']
    
    mostzonesCS = ['MostZonesCarpark','MostZonesVisitorInfrastructure',
    'MostZonesTrailMaps','MostZonesTrailhead','MostZonesDogPoo','MostZonesShakedown',
    'MostZonesBottomDescent','MostZonesTopClimb','MostZonesView','MostZonesJumps',
    'MostZonesUplift','MostZonesPause','MostZonesPicnic','MostZonesPuncture',
    'MostZonesRoadCrossing','MostZonesAlmostHome','MostZonesSummit','MostZonesRoadCrossing',
    'MostZonesSwimspot','MostZonesCamp','MostZonesToilet','MostZonesSkiLift','MostZonesOther']

    zonecounts = []
    for z in mostzonesindy:
        df = count[count[z].notna()]
        for index,i in df.iterrows():
            zonecounts.append(z)
        
    for z in mostzonesCS:
        df = CScount[CScount[z].notna()]

        for index,i in df.iterrows():
            zonecounts.append(z)        

#mostpolluted trail zone
    topzone = max(set(zonecounts), key=zonecounts.count)

    new_row = pd.DataFrame([{'count_submisssions':total_count, 
                'prevalence':prevalence,
                'worst_zone':topzone}])
    count_results = pd.concat([count_results, new_row], ignore_index=True) 
 

    count_results.to_csv(folderout + '/count.csv',index=False)  
    
    survey_results = pd.DataFrame(columns = ['survey_submisssions', 'total items removed', 
                'weight removed', 'volume removed', 'distance_kms', 'area kms2',
                'most common material', 'SUP reported','SUP calculated','most common category',
                'DRS reported','DRS total items','DRS total glass','DRS % of total items',
                'glass DRS % of DRS items','glass DRS % of total items','vapes reported',
                'vapes total items','vapes % of total items','vapes % of smoking related items',
                'gel ends reported','gel ends total items','gel ends % of total items',
                'gels reported','gels total items','gels % of total items',
                'poo bags reported','poo bags total items','poo bags % of total items',
                'outdoor gear reported','outdoor gear total items',
                'outdoor gear % of total items','brand 1','brand 2',
                'brand 3'])


#Survey stats
    
#first ones currently covered in overvies
    values = [total_survey, count_lite]
    total_all_survey = sum(values)
    
    kms_survey = [survey_km, CSsurvey_km, lite_km] 
#distance covered    
    km_survey = sum(kms_survey)
    
    areas_survey = [survey_area,  CSsurvey_area, lite_area]
#area directly protected - excludes Lite
    area_survey = sum(areas_survey)   
    
    plastic = ['Value Full Dog Poo Bags',
            'Value Unused Dog Poo Bags','Value Toys (eg., tennis balls)','Value Other Pet Related Stuff',
            'Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
            'Value Plastic bottle, top','Value Plastic energy drink bottles',
            'Value Plastic energy gel sachet','Value Plastic energy gel end', 'Value Plastic straws',
            'Value Hot drinks tops and stirrers','Value Drinks tops (eg., McDonalds drinks)',
            'Value Plastic carrier bags','Value Plastic bin bags',
            'Value Plastic fast food, takeaway and / or on the go food packaging, cups, cutlery etc',
            'Value Confectionary/sweet wrappers',
            'Value Wrapper "corners" / tear-offs','Value Other confectionary (eg., Lollipop Sticks)',
            'Value Crisps Packets','Value Disposable vapes','Value Salt/mineral lick buckets','Value Silage wrap',
            'Value Tree guards','Value Cable ties','Value Industrial plastic wrap','Value Rubber/nitrile gloves',
            'Value Normal balloons','Value Helium balloons','Value Plastic milk bottles',
            'Value Plastic food containers','Value Cleaning products containers']
            
            
    potentially_plastic = ['Value Hot drinks cups','Value Drinks cups (eg., McDonalds drinks)',
                           'Value Food on the go (eg.salad boxes)']        
            
    metal = ['Value Aluminium soft drink cans','Value Aluminium energy drink can',
             'Value Aluminium alcoholic drink cans','Value Glass bottle tops',
             'Value Disposable BBQs and / or BBQ related items','Value BBQs and / or BBQ related items',]   

    glass = ['Value Glass soft drink bottles','Value Glass alcoholic bottles',]     
    
    cardboard_paper_wood = ['Value Cartons','Value Paper straws',
            'Value Other fast food, takeaway and / or on the go food packaging, cups, cutlery (eg., cardboard)',
            'Value Vaping / E-Cigarette Paraphernalia','Value Toilet tissue','Value Cardboard food containers',]
    
    other = ['Value Used Chewing Gum','Value Fruit peel & cores','Value Cigarette Butts','Value Smoking related',
             'Value Drugs related','Value Farming',
             'Value Forestry','Value Industrial','Value Homemade lunch (eg., aluminium foil, cling film)',
             'Value Face/ baby wipes',
             'Value Nappies','Value Single-Use Period products','Value Single-Use Covid Masks',
             'Value Outdoor event (eg Festival)','Value Camping','Value Halloween & Fireworks','Value Seasonal (Christmas and/or Easter)',
             'Value MTB related (e.g. inner tubes, water bottles etc)',
             'Value Running','Value Roaming and other outdoor related (e.g. climbing, kayaking)',
             'Value Outdoor sports event related (e.g.race)','Value Textiles','Value Clothes & Footwear',
             'Value Miscellaneous','Value Too small/dirty to ID','Value Weird/Retro']
    
    
    plastics = combined[plastic].sum(axis=0).to_list()
    metals = combined[metal].sum(axis=0).to_list()
    glasses = combined[glass].sum(axis=0).to_list()
    papers = combined[cardboard_paper_wood].sum(axis=0).to_list()       
    potentially_plastics = combined[potentially_plastic].sum(axis=0).to_list()
    others = combined[other].sum(axis=0).to_list()     
    
    totpl = sum(plastics)
    totme = sum(metals)
    totgl = sum(glasses)
    totpa = sum(papers)    
    totppl = sum(potentially_plastics)
    tototh = sum(others)

    typedf = pd.DataFrame({'type': ['plastic','metal','glass','paper', 'potentially_plastic','other'],
                           'quantity':[totpl, totme, totgl, totpa, totppl, tototh]})

    t = typedf.loc[typedf['quantity'].idxmax()]
#Most common material    
    most_type = t['type']  

    SUP=[]
    df2 = survey[survey['Perc_SU'].notna()]
    for index,i in df2.iterrows():
        perSUP = i['Perc_SU']
        percSUP = float(perSUP)
        totitems = i['TotItems']
        result = percSUP/100 * totitems
        SUP.append(result) 

    df3 = CSsurvey[CSsurvey['Perc_SU'].notna()]
    for index,i in df3.iterrows():
        perSUP = i['Perc_SU']
        percSUP = float(perSUP)
        totitems = i['TotItems']
        result = percSUP/100 * totitems
        SUP.append(result) 

    srvy_tot = df2['TotItems'].sum()
    CSsrvy_tot = df3['TotItems'].sum()
    tot_items_surveys = srvy_tot + CSsrvy_tot
    tot_SUP = sum(SUP) 
    #calcualte percentage
#SUP proportion % reported    
    tot_percSUP = tot_SUP/tot_items_surveys *100   
    
    #check SUP percentage
    col_list_SUP = ['Value Full Dog Poo Bags','Value Unused Dog Poo Bags',
    'Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
    'Value Aluminium soft drink cans','Value Plastic bottle, top','Value Glass soft drink bottles',
    'Value Plastic energy drink bottles','Value Aluminium energy drink can',
    'Value Plastic energy gel sachet','Value Plastic energy gel end','Value Aluminium alcoholic drink cans',
    'Value Glass alcoholic bottles','Value Glass bottle tops','Value Hot drinks cups',
    'Value Hot drinks tops and stirrers','Value Drinks cups (eg., McDonalds drinks)',
    'Value Drinks tops (eg., McDonalds drinks)','Value Cartons','Value Plastic straws',
    'Value Paper straws','Value Plastic carrier bags','Value Plastic bin bags',
    'Value Confectionary/sweet wrappers','Value Wrapper "corners" / tear-offs',
    'Value Other confectionary (eg., Lollipop Sticks)','Value Crisps Packets',
    'Value Used Chewing Gum','Value Plastic fast food, takeaway and / or on the go food packaging, cups, cutlery etc',
    'Value Other fast food, takeaway and / or on the go food packaging, cups, cutlery (eg., cardboard)',
    'Value Disposable BBQs and / or BBQ related items',
    'Value Food on the go (eg.salad boxes)','Value Cigarette Butts','Value Smoking related',
    'Value Disposable vapes','Value Vaping / E-Cigarette Paraphernalia','Value Drugs related',
    'Value Salt/mineral lick buckets','Value Silage wrap','Value Tree guards',
    'Value Cable ties','Value Industrial plastic wrap','Value Toilet tissue',
    'Value Face/ baby wipes','Value Nappies','Value Single-Use Period products',
    'Value Single-Use Covid Masks','Value Rubber/nitrile gloves','Value Halloween & Fireworks',
    'Value Seasonal (Christmas and/or Easter)','Value Normal balloons','Value Helium balloons',
    'Value Outdoor sports event related (e.g.race)','Value Plastic milk bottles',
    'Value Plastic food containers','Value Cardboard food containers',
    'Value Cleaning products containers']
     
    calc_perc_SUP = []
    df2 = survey[survey['MoreInfoY'].notna()]
    for index, i in df2.iterrows():
        SUP_items = i[col_list_SUP].sum()   
        tot_items = i[all_items].sum()
        if tot_items == 0:
            continue
        calculated_SUP = (SUP_items/tot_items)*100
        calc_perc_SUP.append(calculated_SUP)
        
    df3 = CSsurvey       
    for index, i in df3.iterrows():
        SUP_items = i[col_list_SUP].sum()   
        tot_items = i[all_items].sum()
        if tot_items == 0:
            continue
        calculated_SUP = (SUP_items/tot_items)*100
        calc_perc_SUP.append(calculated_SUP)        
    SUPs = sum(calc_perc_SUP)     
#SUP proportion % calculated          
    tot_calc_SUP = SUPs/len(calc_perc_SUP)     
    
    pet_stuff = ['Value Full Dog Poo Bags','Value Unused Dog Poo Bags',
    'Value Toys (eg., tennis balls)','Value Other Pet Related Stuff']
    
    drinks_containers = ['Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
    'Value Aluminium soft drink cans','Value Plastic bottle, top','Value Glass soft drink bottles',
    'Value Plastic energy drink bottles','Value Aluminium energy drink can',
    'Value Plastic energy gel sachet','Value Plastic energy gel end','Value Aluminium alcoholic drink cans',
    'Value Glass alcoholic bottles','Value Glass bottle tops','Value Hot drinks cups',
    'Value Hot drinks tops and stirrers','Value Drinks cups (eg., McDonalds drinks)',
    'Value Drinks tops (eg., McDonalds drinks)','Value Cartons','Value Plastic straws',
    'Value Paper straws']
    
    snack = ['Value Plastic carrier bags','Value Plastic bin bags',
    'Value Confectionary/sweet wrappers','Value Wrapper "corners" / tear-offs',
    'Value Other confectionary (eg., Lollipop Sticks)','Value Crisps Packets',
    'Value Used Chewing Gum','Value Plastic fast food, takeaway and / or on the go food packaging, cups, cutlery etc',
    'Value Other fast food, takeaway and / or on the go food packaging, cups, cutlery (eg., cardboard)',
    'Value Disposable BBQs and / or BBQ related items','Value BBQs and / or BBQ related items',
    'Value Food on the go (eg.salad boxes)','Value Homemade lunch (eg., aluminium foil, cling film)',
    'Value Fruit peel & cores']
    
    smoking = ['Value Cigarette Butts','Value Smoking related',
    'Value Disposable vapes','Value Vaping / E-Cigarette Paraphernalia','Value Drugs related']
    
    agro_ind = ['Value Farming','Value Salt/mineral lick buckets','Value Silage wrap',
    'Value Forestry','Value Tree guards','Value Industrial','Value Cable ties',
    'Value Industrial plastic wrap']
    
    hygiene = ['Value Toilet tissue','Value Face/ baby wipes',
    'Value Nappies','Value Single-Use Period products','Value Single-Use Covid Masks',
    'Value Rubber/nitrile gloves']
    
    recreation = ['Value Outdoor event (eg Festival)','Value Camping',
    'Value Halloween & Fireworks','Value Seasonal (Christmas and/or Easter)',
    'Value Normal balloons','Value Helium balloons']
    
    sports = ['Value MTB related (e.g. inner tubes, water bottles etc)',
    'Value Running','Value Roaming and other outdoor related (e.g. climbing, kayaking)',
    'Value Outdoor sports event related (e.g.race)']
    
    textiles = ['Value Textiles','Value Clothes & Footwear']
    
    house = ['Value Plastic milk bottles','Value Plastic food containers','Value Cardboard food containers',
    'Value Cleaning products containers']
    
    misc = ['Value Miscellaneous','Value Too small/dirty to ID',
    'Value Weird/Retro']

    pets = combined[pet_stuff].sum(axis=0).to_list()
    drinks = combined[drinks_containers].sum(axis=0).to_list()
    snacks = combined[snack].sum(axis=0).to_list()
    smokes = combined[smoking].sum(axis=0).to_list()
    agros = combined[agro_ind].sum(axis=0).to_list()
    hyg = combined[hygiene].sum(axis=0).to_list()
    recre = combined[recreation].sum(axis=0).to_list()
    sport = combined[sports].sum(axis=0).to_list()
    text = combined[textiles].sum(axis=0).to_list()
    home = combined[house].sum(axis=0).to_list()
    miscs = combined[misc].sum(axis=0).to_list()

    totpet = sum(pets)
    totdrs = sum(drinks)
    totsn = sum(snacks)
    totsm = sum(smokes)
    totag = sum(agros)
    tothy = sum(hyg)
    totrec = sum(recre)
    totsp = sum(sport)      
    tottx = sum(text)
    totho = sum(home)
    totmis = sum(miscs)
 

    catdf = pd.DataFrame({'type': ['pet stuff','drinks','snacks','smoking', 'agro_ind',
                                   'hygiene','recreational','sports','textiles',
                                   'household','miscellaneous'],
                           'quantity':[totpet, totdrs, totsn, totsm, totag, tothy,
                                       totrec, totsp, tottx, totho, totmis]})
    
    c = catdf.loc[catdf['quantity'].idxmax()]
#Most common category of SUP    
    most_cat = c['type']    

    sub_DRS =   ['Plastic Water Bottles','Plastic Soft Drink Bottles',
    'Aluminium soft drink cans','Glass soft drink bottles',
    'Plastic energy drink bottles','Aluminium energy drink can',
    'Aluminium alcoholic drink cans','Glass alcoholic bottles']
    
    DRS = ['Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
    'Value Aluminium soft drink cans', 'Value Glass soft drink bottles',
    'Value Plastic energy drink bottles','Value Aluminium energy drink can',
    'Value Aluminium alcoholic drink cans','Value Glass alcoholic bottles']
    
    DRS_glass = ['Value Glass soft drink bottles','Value Glass alcoholic bottles']
    
    df_DRS_subs = survey[sub_DRS]    
    subs_indy = df_DRS_subs.any(axis=1).sum()
    df_CSDRS_subs = CSsurvey[DRS]
    subs_CS = df_CSDRS_subs.any(axis=1).sum()
        
    DRS_items = combined[DRS].sum(axis=0).to_list()   
    glass_DRS_items = combined[DRS_glass].sum(axis=0).to_list()  


    lite_DRS = []
    for index,i in lite.iterrows():
        if i['Categories - Drinks Containers']==True:
            lite_DRS.append(1)
            
    DRS_lite = sum(lite_DRS)
    tot_DRS_subs = subs_indy + subs_CS + DRS_lite   
      
    subs_for_DRS = [count_survey, count_CSsurvey, count_lite]
    subs = sum(subs_for_DRS)
        
    
#% Submissions reporting DRS                
    DRS_reported = (tot_DRS_subs/subs)*100
#DRS total items
    DRS_tot_items = sum(DRS_items)
#DRS total glass items
    DRS_tot_glass = sum(glass_DRS_items)
    
#% of total items that are DRS - from those reporting breakdown
    DRS_proportion = (DRS_tot_items/total_reported_items)*100
#%of DRS items that are glass    
    glass_DRS_proportion = (DRS_tot_glass/DRS_tot_items)*100
#% of total items that are glass DRS
    glass_proportion = (DRS_tot_glass/total_reported_items)*100 
    
    
    vapes_indy = ['Disposable vapes','Value Disposable vapes']   
    survey['Disposable vapes'] = pd.to_numeric(survey['Disposable vapes'], errors='coerce').fillna(0).astype(int)
    vape_items_indy = survey[vapes_indy].sum(axis=0).to_list()
               
    vapes_subs_indy = vape_items_indy[0]
    
    all_vapes_CS = CSsurvey['Value Disposable vapes'].to_list()
    vapes_CS = [x for x in all_vapes_CS if str(x) != 'nan']
    
    vapes_subs_CS = len(vapes_CS)
    vapes_subs = vapes_subs_indy + vapes_subs_CS
    vapes_tt_indy = vape_items_indy[1]
    vapes_tt_CS = sum(vapes_CS)
        
#% submissions reporting vapes    
    vapes_reported = (vapes_subs/total_survey)*100
#vapes_total_items    
    vapes_total = vapes_tt_CS + vapes_tt_indy
#% of total items that are vapes
    vapes_proportion = (vapes_total/total_reported_items)*100
#% of smoking items that are vapes    
    vapes_in_smoke = (vapes_total/totsm)*100
     
    gel_end_subs_indy = []
    no_gelends_indy = []
    for index, i in survey.iterrows():
        gelend = i['Plastic energy gel end']
        no_gelends = i['Value Plastic energy gel end']
        gel_end_subs_indy.append(gelend)
        no_gelends_indy.append(no_gelends)
    gelends_subs_indy = [x for x in gel_end_subs_indy if str(x) != 'nan']    
    gelend_subs_indy = len(gelends_subs_indy)  
    gelends_indy = [x for x in no_gelends_indy if str(x) != 'nan']

   
    all_gelends_CS = CSsurvey['Value Plastic energy gel end'].to_list()
    gelends_CS = [x for x in all_gelends_CS if str(x) != 'nan']
    
    gelends_subs_CS = len(gelends_CS)
    gelend_subs = gelend_subs_indy + gelends_subs_CS
    gelends_tt_indy = sum(gelends_indy)
    gelends_tt_CS = sum(gelends_CS)
      
#% submissions reporting gel ends    
    gelends_reported = (gelend_subs/total_survey)*100
#gel ends_total_items    
    gelends_total = gelends_tt_indy + gelends_tt_CS
#% of total items that are gel ends
    gelends_proportion = (gelends_total/total_reported_items)*100 

    gel_subs_indy = []
    no_gels_indy = []
    for index, i in survey.iterrows():
        gel = i['Plastic energy gel sachet']
        no_gels = i['Value Plastic energy gel sachet']
        gel_subs_indy.append(gel)
        no_gels_indy.append(no_gels)
        
    gels_subs_ind = [x for x in gel_subs_indy if str(x) != 'nan']    
    gels_subs_indy = len(gels_subs_ind)  

    gels_indy = [x for x in no_gels_indy if str(x) != 'nan']

   
    all_gels_CS = CSsurvey['Value Plastic energy gel sachet'].to_list()
    gels_CS = [x for x in all_gels_CS if str(x) != 'nan']
    
    gels_subs_CS = len(gels_CS)
    gel_subs = gels_subs_indy + gels_subs_CS
    gels_tt_indy = sum(gels_indy)
    gels_tt_CS = sum(gels_CS)        
#% submissions reporting gel ends    
    gels_reported = (gel_subs/total_survey)*100
#gel ends_total_items    
    gels_total = gels_tt_indy + gels_tt_CS
#% of total items that are gel ends
    gels_proportion = (gels_total/total_reported_items)*100 
       
        
    poo = []
    bag = []
    for index, i in survey.iterrows():
        full_bags = i['Value Full Dog Poo Bags']
        bags = i['Value Unused Dog Poo Bags']
        if full_bags > 0:
            poo.append(full_bags)
            bag.append(1)
            if bags > 0:
                poo.append(bags)  
        else:
            if bags > 0:
                poo.append(bags)
                bag.append(1)
                
    for index, i in CSsurvey.iterrows():
        full_bags = i['Value Full Dog Poo Bags']
        bags = i['Value Unused Dog Poo Bags']
        if full_bags > 0:
            poo.append(full_bags)
            bag.append(1)
            if bags > 0:
                poo.append(bags)  
        else:
            if bags > 0:
                poo.append(bags)
                bag.append(1)                
            
    all_bags = len(bag)
#% submissions reporting poo bags   
    bags_reported = (all_bags/total_survey)*100
#poo bags_total_items    
    bags_total = sum(poo)   
#% of total items that are poo bags
    bags_proportion = (bags_total/total_reported_items)*100


    outdoor = ['Value Outdoor event (eg Festival)','Value Camping','Value MTB related (e.g. inner tubes, water bottles etc)',
    'Value Running','Value Roaming and other outdoor related (e.g. climbing, kayaking)',
    'Value Outdoor sports event related (e.g.race)']
    
    out = []
    out_subs = []
    out_df = survey[outdoor]
    outCS_df = CSsurvey[outdoor]
    for index, i in out_df.iterrows():
        outs = i.sum()
        if outs > 0:
            out_subs.append(1)
        out.append(outs)  
        
    for index, i in outCS_df.iterrows():
        outs = i.sum()
        if outs > 0:
            out_subs.append(1)
        out.append(outs)      
    
    tot_subs = len(out_subs)
    
    lite_outs = []
    for index,i in lite.iterrows():
        if i['Categories - Outdoor Sports & Recreation']==True:
            lite_outs.append(1)
            
    out_lite = sum(lite_outs)
    tot_out_subs = tot_subs + out_lite 
#% submissions reporting outdoor gear    
    outs_reported = (tot_out_subs/subs)*100
#outdoor gear_total_items    
    outs_total = sum(out)   
#% of total items that are outdoor gear
    outs_proportion = (outs_total/total_reported_items)*100        
        
        
    

    #calculate brands
    brands = ['Lucozade','Coke','RedBull','Monster','Cadbury','McDonalds','Walkers','Mars','StellaArtois','Strongbow',
              'Costa','Budweiser','Haribo','SIS','Carling','Fosters','Thatchers','Pepsi','Nestle','Subway','Other']
    

    brand_res = pd.DataFrame(columns=['brand', 'weighted_count'])

    # Weight mapping
    weights = {'B1': 3, 'B2': 2, 'B3': 1}

    for b in brands:
        total_weighted = 0
    
        for col_prefix, weight in weights.items():
            # Count non-null for survey
            col_name = f"{col_prefix}_{b}"
            count_survey = survey[col_name].notna().sum()
            # Count non-null for CSsurvey
            count_cs = CSsurvey[col_name].notna().sum()
        
            # Add weighted contribution
            total_weighted += (count_survey + count_cs) * weight
        
        new_row = pd.DataFrame([{'brand': b, 'weighted_count': total_weighted}])
        brand_res = pd.concat([brand_res, new_row], ignore_index=True) 

    # Sort by weighted count
    brand_res = brand_res.sort_values(by='weighted_count', ascending=False)
    #brands 1, 2 and 3    
    brand1 = brand_res.iloc[0]['brand']
    brand2 = brand_res.iloc[1]['brand']
    brand3 = brand_res.iloc[2]['brand']
    
    brand_res.to_csv(folderout + 'brands.csv')
    
    new_row = pd.DataFrame([{'survey_submisssions':total_all_survey,
                'total items removed':removed_items, 'weight removed':total_kg, 
                'volume removed':total_cokecans, 'distance_kms':km_survey, 
                'area kms2':area_survey,'most common material':most_type, 
                'SUP reported':tot_percSUP,'SUP calculated':tot_calc_SUP,
                'most common category':most_cat,'DRS reported':DRS_reported,
                'DRS total items':DRS_tot_items,'DRS total glass':DRS_tot_glass,
                'DRS % of total items':DRS_proportion,'glass DRS % of DRS items':glass_DRS_proportion,
                'glass DRS % of total items':glass_proportion,
                'vapes reported':vapes_reported,'vapes total items':vapes_total,
                'vapes % of total items':vapes_proportion,
                'vapes % of smoking related items':vapes_in_smoke,
                'gel ends reported':gelends_reported,'gel ends total items':gelends_total,
                'gel ends % of total items':gelends_proportion,'gels reported':gels_reported,
                'gels total items':gels_total,'gels % of total items':gels_proportion,
                'poo bags reported':bags_reported,'poo bags total items':bags_total,
                'poo bags % of total items':bags_proportion,
                'outdoor gear reported':outs_reported,'outdoor gear total items':outs_total,
                'outdoor gear % of total items':outs_proportion,
                'brand 1':brand1,'brand 2':brand2,'brand 3':brand3}])
    survey_results = pd.concat([survey_results, new_row], ignore_index=True) 

    survey_results.to_csv(folderout + '/survey.csv', index=False)  
    
    impacts_results = pd.DataFrame(columns = ['Fauna Interaction', 'Fauna Death',
                    'First Time', 'Repeat volunteers','Felt proud',
                    'Felt more connected','met someone inspiring', 'went out after',
                    'Would do again','provided contact info'])
    
    #animal interaction - how many (%) answered the question and checked
    CSsurv_AIcols = ['AnimalsY','AnimalsN','AnimalsInfo']
    CScount_AIcols = ['AIY','AIN','AINotSure']
    survey_AIcols = ['AnimalsY','AnimalsN','AnimalsInfo']
    lite_AIcols = ['Animal Interaction - No',
               'Animal Interaction - Chew Marks','Animal Interaction - Death']
    
    AI_survey = survey[survey_AIcols].notna().any(axis=1).sum()
    AI_CSsurvey = CSsurvey[CSsurv_AIcols].notna().any(axis=1).sum()
    AI_CScount = CScount[CScount_AIcols].notna().any(axis=1).sum()
    AI_lite = lite[lite_AIcols].any(axis=1).sum()
    
    AI_subs = [AI_survey, AI_CSsurvey, AI_CScount, AI_lite]
    subs_tot = sum(AI_subs)
    survey_AI = survey['AnimalsY'].value_counts().get('Yes', 0)
    CSsurvey_AI = CSsurvey['AnimalsY'].value_counts().get('Yes', 0)
    CScount_AI = CScount['AIY'].value_counts().get('Yes', 0)
    lite_AI = (lite['Animal Interaction - Chew Marks'] | lite['Animal Interaction - Death']).sum()
    AI_yes = [survey_AI, CSsurvey_AI, CScount_AI, lite_AI]
    AI_tot = sum(AI_yes)
    
#percent submissions reporting AI observed
    perc_AI = (AI_tot/subs_tot)*100
    
    dfs = [CSsurvey, survey]
    deaths = []
    for df in dfs:
        if 'AnimalsInfo' in df.columns and df['AnimalsInfo'].notna().any():
            death = df['AnimalsInfo'].astype(str).str.contains(r'\b(death|dead)\b', case=False, na=False).sum()
        else:
            death = 0
        deaths.append(death)


    lite_death = lite['Animal Interaction - Death'].sum()
    deaths.append(lite_death)
    
    tot_deaths = sum(deaths)
    subs_for_death = [AI_survey, AI_lite, AI_CSsurvey]
    death_subs_tot = sum(subs_for_death)
#percent submissions reporting death of those reporting they checked for AI  
    perc_death = (tot_deaths/death_subs_tot)*100
    
    survey_1st = survey['First time'].value_counts().get('This is my first time!', 0)
    CSsurvey_1st = CSsurvey['Connection_TakePartBeforeN'].value_counts().get('No', 0)
    if count['First_time'].isna().all:
        count_1st = 0
    else:
        count_1st = count['First_time'].value_counts().get('This is my first time!', 0)

    subs_for_1st = [survey_1st, CSsurvey_1st, count_1st]
#number submitting for first time - not lite    
    no_1st = sum(subs_for_1st)
    
    multiple_cols = ['Volunteer','A-Team','Community Hub']
    dfs = [count, survey]
    befores = []
    for df in dfs:
        before = df[multiple_cols].notna().sum()
        before_tot = sum(before)
        befores.append(before_tot)
     
#number submitting again - not including CS or lite        
    beforers = sum(befores)    
    
    p_survey4 = survey['Connection_Action'].value_counts().get(4, 0)
    p_CSsurvey4 = CSsurvey['Connection_Action'].value_counts().get(4, 0)
    p_CScount4 = CScount['Connect_Feel'].value_counts().get(4, 0)
    p_survey5 = survey['Connection_Action'].value_counts().get(5, 0)
    p_CSsurvey5 = CSsurvey['Connection_Action'].value_counts().get(5, 0)
    p_CScount5 = CScount['Connect_Feel'].value_counts().get(5, 0)
    proud = [p_survey4, p_CSsurvey4, p_CScount4, p_survey5, p_CSsurvey5, p_CScount5]     
    prouds = sum(proud)
    na_survey = survey['Connection_Action'].notna().sum()
    na_CSsurvey = CSsurvey['Connection_Action'].notna().sum()
    na_CScount = CScount['Connect_Feel'].notna().sum()
    nas = [na_survey, na_CSsurvey, na_CScount]
    count_nas = sum(nas)
#percent feeling proud after taking action 
    perc_proud = (prouds/count_nas) * 100

    dfs = [survey, count, CSsurvey]
    connection = []
    counts_connect = []
    for df in dfs:
        more_connected = df['Connection_ConnectionY'].value_counts().get('Yes', 0) 
        connection.append(more_connected)
        columns_of_interest = ['Connection_ConnectionY', 'Connection_ConnectionN', 
                               'Connection_ConnectionSame', 'Connection_Unsure'] #won't work for count until redo columns
        count_connect = df[columns_of_interest].notnull().any(axis=1).sum()
        counts_connect.append(count_connect)
    
    lite_connects = lite['Increased Nature Connection - Yes'].sum()
    connection.append(lite_connects)
    counts_connect.append(count_lite)
    
    total_answer_connect = sum(counts_connect)
    connects = sum(connection)
#percent feeling more connected    
    perc_more_connected = (connects/total_answer_connect) *100
    
    dfs = [survey, CSsurvey] 
    people = []
    answered_p = []
    activity = []
    answered_a = []
    people_cols = ['Connection_NewPeopleY', 'Connection_NewPeopleN']
    activity_cols = ['Connection_ActivityAfterY', 'Connection_ActivityAfterN']
    for df in dfs:
        new_people = df['Connection_NewPeopleY'].value_counts().get('Yes', 0)
        answered_people = df[people_cols].notnull().any(axis=1).sum()
        activity_after = df['Connection_ActivityAfterY'].value_counts().get('Yes', 0)
        answered_activity = df[activity_cols].notnull().any(axis=1).sum()
        people.append(new_people)
        answered_p.append(answered_people)
        activity.append(activity_after)
        answered_a.append(answered_activity)
    
    new_people = sum(people)
    ans_people = sum(answered_p)
#percentage meeting inspiring/new people    
    perc_new_peeps = (new_people/ans_people) *100
    
    active_after = sum(activity)
    ans_act = sum(answered_a)
#percentage doing an activity after
    perc_active = (active_after/ans_act) * 100
    
    again = survey['Connection_TakePartAgainY'].value_counts().get('Yes', 0)
    again_cols = ['Connection_TakePartAgainY', 'Connection_TakePartAgainN', 'Connection_TakePartAgainUnsure']
    answered_again = survey[again_cols].notnull().any(axis=1).sum()
#percentage who would participate again
    perc_participate_again = (again/answered_again)*100

    dfs = [count, survey, lite]
    contacts = []
    for df in dfs:
        contact = df['Email'].notnull().sum()
        contacts.append(contact)
    
    no_subs = [count_count, count_survey, count_lite]
    contact_deets = sum(contacts)
    subs_contact = sum(no_subs)
#percent leaving contact details    
    perc_contacts = (contact_deets/subs_contact)*100

    new_row = pd.DataFrame([{'Fauna Interaction':perc_AI, 
                    'Fauna Death':perc_death,'First Time':no_1st, 
                    'Repeat volunteers':beforers,'Felt proud':perc_proud,
                       'Felt more connected':perc_more_connected,
                       'met someone inspiring':perc_new_peeps, 
                       'went out after':perc_active,
                       'Would do again':perc_participate_again,
                       'provided contact info':perc_contacts}])
    impacts_results = pd.concat([impacts_results, new_row], ignore_index=True)    
    
    impacts_results.to_csv(folderout + '/impacts.csv', index=False) 
           
            
            
            
            
            
            
    
    
                                      

    
    


    
    
    
        
        
        
    
    
    
    
    
    