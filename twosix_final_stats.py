#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 13:46:36 2026

@author: heatherkay
"""

import numpy as np
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
                                      'no_people','distance_km','duration_hours', 
                                      'items_removed','items_surveyed', 'total_items',
                                      'total_kg','total_cokecans','Adjusted Total Items'])
    
    lite_dt = pd.read_csv(folderin + 'other_averages_calc.csv',
                          index_col=0).iloc[:, 0]
    lite_dict = lite_dt.to_dict()  
    
    survey = pd.read_csv(folderin + 'survey.csv')
    lite = pd.read_csv(folderin + 'lite.csv')
    count = pd.read_csv(folderin + 'count.csv')
    #CSsurvey = pd.read_csv(folderin + 'CS_survey.csv')
    #CScount = pd.read_csv(folderin + 'CS_count.csv')
    #bag_res_lite = pd.read_csv(folderin + 'bag_res_lite.csv')
    tfr = pd.read_csv(folderin + 'TFR.csv')
    
    
    #total submmissions before any filtering
    count_survey = len(survey.index)    
    count_lite = len(lite.index)
    count_count = len(count.index)
    
    #Overview Stats - submitted data

    CS = [count_survey, count_lite, count_count]
#Total combined data sets submitted
    total_CS = sum(CS)

        
    #Overview - volunteers, distance, hours, items
    mins = survey['Time_min']
    hours = []
    for m in mins:
        hour = m/60
        hours.append(hour)
        
    survey['Time_hours'] = hours    
    
    tot_people = []
    tot_time = []
    
    minutes = lite_dict['Time_min']
    time = minutes/60

    survey['Time_hours'] = survey['Time_hours'].replace(0, time).fillna(time)
    survey['People'] = survey['People'].replace(0, lite_dict['People']).fillna(lite_dict['People'])
    
    people = survey['People'].sum()
    hours = (survey['People'] * survey['Time_hours']).sum()

    tot_people.append(people)
    tot_time.append(hours)

    #add to total people the number of lite and count submissions
    lite_people = count_lite * lite_dict['People']
    tot_people.append(lite_people)
    count_people = count['People'].sum()
    tot_people.append(count_people)
 
#volunteers
    total_people = sum(tot_people)
    
    #removing empty rows before next steps so prevalance calc is correct
    count_df1 = count[count['TotItems'].notna()]
    count_df2 = count_df1[count_df1['Total_distance(m)'].notna()]
    count = count_df2
    
    survey_km = survey['Distance_km'].sum()
    count_m = count['Total_distance(m)'].sum()
    count_km = count_m / 1000
    lite_km = count_lite * lite_dict['Distance_km']
      
    kms = [survey_km, count_km, lite_km]
#distance cleaned / surveyed 
    km = sum(kms)
        
    #method to estimate time spent on count

    count_time = count_count * time
    lite_time = count_lite * time
    tot_time.append(count_time)
    tot_time.append(lite_time)
#time 
    total_time = sum(tot_time) 

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
    
    all_presence = ['Full Dog Poo Bags','Unused Dog Poo Bags','Other Pet Related Stuff',
    'Plastic Water Bottles','Plastic Soft Drink Bottles','Aluminium soft drink cans',
    'Glass soft drink bottles','Milkshake bottle or carton','Plastic energy drink bottles',
    'Aluminium energy drink can','Plastic energy gel sachet','Plastic energy gel end',
    'Protein drink bottle or carton', 'Aluminium alcoholic drink cans',
    'Glass alcoholic bottles','Hot drinks cups','Hot drinks tops and stirrers',
    'Cold drinks cups and tops','Cartons','Plastic straws','Paper straws',
    'Plastic bottle, top', 'Glass bottle tops', 'Ring pull', 'Plastic bottle sleeve',
    'Reusable drinks container','Other drink related','Confectionary/sweet wrappers',
    'Wrapper "corners" / tear-offs','Other confectionary (eg., Lollipop Sticks)',
    'Crisps Packets','Used Chewing Gum','Homemade lunch (eg., aluminium foil, cling film)',
    'BBQ related','Fruit peel & cores','Branded single-use carrier bags',
    'Unbranded single-use carrier bags', 'Branded bag for life','Unbranded bag for life', 
    'Branded plastic fast / takeaway food packaging / utensils',
    'Unbranded plastic fast / takeaway food packaging / utensils',
    'Branded card or wood fast / takeaway food packaging / utensils',
    'Unbranded card or wood fast / takeaway food packaging / utensils',
    'Branded condiments packaging','Unbranded condiments packaging',
    'Branded food on the go','Unbranded food on the go','Branded other food related',
    'Unbranded other food related','Clothes & Footwear','Textiles',
    'Plastic milk bottles','Glass milk bottles',
    'Plastic food containers','Cardboard food containers','Cleaning products containers',
    'Cosmetics / deodorants', 'Other household','Cigarette Butts','Nicotine pouches',
    'Disposable vapes',
    'Nicotine related packaging','Other nicotine related','Unbagged dog poo',
    'Needles / syringes','Other drug related','broken glass or pottery',
    'Toilet tissue','Face/ baby wipes','Nappies','Period products',
    'Covid Masks','First Aid & medcal waste','batteries and electronics',
    'Other hazardous', 'Camping','Fireworks','Seasonal (Christmas and/or Easter)',
    'Rubber balloons','Foil balloons','Outdoor event related (e.g.race)',
    'Biking specific','Hiking specific','Other outdoor related',
    'Farming','Forestry','Industrial','Cable ties','Miscellaneous hard plastic',
    'Miscellaneous soft plastic','Miscellaneous card or wood','Miscellaneous metal',
    'Too small/dirty to ID','Other Miscellaneous']
    
    #Resolve nan issues
    survey[all_items] = survey[all_items].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

    # Summation works the same
    reported_items = survey[all_items].sum(axis=0).to_list()
    total_reported_items = sum(reported_items)
    
    srvy_items = []
    rmv_items = [] 
    cnt_items = []
    full_srvy_items = []
        
    survey_items = survey['TotItems'].sum()   
    srvy_items.append(survey_items)
    rmv_items.append(survey_items)
    full_srvy_items.append(survey_items)
    
    lite_items = lite['TotItems'].sum() 
    rmv_items.append(lite_items)
    
    count_items = count['TotItems'].sum() 
    srvy_items.append(count_items)
    cnt_items.append(count_items)
    
    tfr_items = tfr['TotItems'].sum()
    srvy_items.append(tfr_items)
    rmv_items.append(tfr_items)
    
    removed_items = sum(rmv_items)
    surveyed_items = sum(srvy_items) 
    tot_count_items = sum(cnt_items)
    fully_surveyed_items = sum(full_srvy_items)
    
#total removed items (reported)
    total_items = surveyed_items + lite_items

#weight removed items
    total_kg = removed_items / 57  
#volume of removed items as number of coke cans
    total_cokecans = removed_items / 1.04

    new_row = pd.DataFrame([{'total_submisssions':total_CS, 'total_count':count_count,
                              'total_survey':count_survey, 'total_lite': count_lite,
                              'no_people':total_people, 
                              'distance_km':km,
                              'duration_hours':total_time, 'items_removed':removed_items,
                              'items_surveyed':surveyed_items, 'total_items':total_items,
                              'total_kg':total_kg,'total_cokecans':total_cokecans}])
    
    results= pd.concat([results, new_row], ignore_index=True) 
                                        
    
    results.to_csv(folderout + '/overview.csv',index=False)    
    
    count = count.rename(columns={'ZMostonesAlmostHome':'MostZonesAlmostHome'})
    count = count.rename(columns={'MostZonesLunch':'MostZonesPicnic'})
    
    

    count_results = pd.DataFrame(columns = ['count_submisssions', 'count_items',
                                            'count_kms','prevalence', 'hotspots',
                                            'worst_zone'])
    
    distance = count_km

#how much is out there per km
    if distance == 0:
        prevalence = 0
    else:
        prevalence = tot_count_items/distance
    
#hot spots????
    

    mostzonesindy = ['MostZonesCarpark','MostZonesVisitorInfrastructure','MostZonesTrailMaps',
    'MostZonesTrailhead','MostZonesDogPoo','MostZonesShakedown','MostZonesTopClimb',
    'MostZonesView','MostZonesPicnic','MostZonesRoadCrossing','MostZonesSwimspot',
    'MostZonesBottomDescent','MostZonesJumps','MostZonesPause','MostZonesAlmostHome',
    'MostZonesLake','MostZonesRiver','MostZonesBeach','MostZonesSanddunes']

    zonecounts = []
    for z in mostzonesindy:
        df = count[count[z].notna()]
        for index,i in df.iterrows():
            zonecounts.append(z)

        for index,i in df.iterrows():
            zonecounts.append(z)        

#mostpolluted trail zone
    if len(zonecounts) == 0:
        topzone = 'none'
    else:
        topzone = max(set(zonecounts), key=zonecounts.count)

    new_row = pd.DataFrame([{'count_submisssions':count_count, 
                'count_items':tot_count_items,
                'count_kms':distance,
                'prevalence':prevalence,
                'worst_zone':topzone}])
    count_results = pd.concat([count_results, new_row], ignore_index=True) 
 

    count_results.to_csv(folderout + '/count.csv',index=False)  
    
    survey_results = pd.DataFrame(columns = ['survey_submisssions', 'total items surveyed', 
                'total composition items','weight removed', 'volume removed', 'distance_kms', 'area kms2',
                'most common material', 'SUP reported','SUP calculated','most common category',
                'DRS reported','DRS total items','DRS total glass','DRS % of total items',
                'glass DRS % of DRS items','glass DRS % of total items','EPR reported',
                'EPR total items','EPR % of total items','vapes reported',
                'vapes total items','vapes % of total items','vapes % of smoking related items',
                'gel ends reported','gel ends total items','gel ends % of total items',
                'gels reported','gels total items','gels % of total items',
                'poo bags reported','poo bags total items','poo bags % of total items',
                'outdoor gear reported','outdoor gear total items',
                'outdoor gear % of total items','brand 1','brand 2',
                'brand 3'])


#Survey stats
    
#first ones currently covered in overviews
    
    kms_survey = [survey_km] 
#distance covered    
    km_survey = sum(kms_survey)

    plastic = ['Value Full Dog Poo Bags',
            'Value Unused Dog Poo Bags',
            'Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
            'Value Plastic bottle, top','Value Plastic energy drink bottles',
            'Value Plastic energy gel sachet','Value Plastic energy gel end', 'Value Plastic straws',
            'Value Plastic bottle sleeve',
            'Value Hot drinks tops and stirrers','Value Cold drinks cups and tops',
            'Value Branded single-use carrier bags',
            'Value Unbranded single-use carrier bags', 
            'Value Branded bag for life',
            'Value Unbranded bag for life', 
            'Value Branded plastic fast / takeaway food packaging / utensils',
            'Value Unbranded plastic fast / takeaway food packaging / utensils',
            'Value Confectionary/sweet wrappers',
            'Value Wrapper "corners" / tear-offs','Value Other confectionary (eg., Lollipop Sticks)',
            'Value Crisps Packets','Value Disposable vapes','Value Cable ties',
            'Value Face/ baby wipes',
            'Value Rubber balloons','Value Foil balloons','Value Plastic milk bottles',
            'Value Plastic food containers','Value Cleaning products containers',
            'Value Miscellaneous hard plastic','Value Miscellaneous soft plastic']
            
            
    potentially_plastic = ['Value Hot drinks cups','Value Unbranded food on the go',
                           'Value Branded food on the go','Value Branded condiments packaging',
                           'Value Unbranded condiments packaging','Value Other Pet Related Stuff',
                           'Value Farming','Value Forestry','Value Industrial',
                           'Value Milkshake bottle or carton',
                           'Value Protein drink bottle or carton','Value Nicotine related packaging']        
            
    metal = ['Value Aluminium soft drink cans','Value Aluminium energy drink can',
             'Value Aluminium alcoholic drink cans','Value Glass bottle tops',
             'Value Ring pull','Value Cosmetics / deodorants','Value Batteries and electronics',
             'Value Miscellaneous metal']   

    glass = ['Value Glass soft drink bottles','Value Glass alcoholic bottles',
             'Value Glass milk bottles','Value Broken glass or pottery']     
    
    cardboard_paper_wood = ['Value Cartons','Value Paper straws',
            'Value Branded card or wood fast / takeaway food packaging / utensils',
            'Value Unbranded card or wood fast / takeaway food packaging / utensils',
            'Value Toilet tissue','Value Cardboard food containers',
            'Value Miscellaneous card or wood']
    
    other = ['Value Reusable drinks container',
    'Value Other drink related',
    'Value Used Chewing Gum','Value Homemade lunch (eg., aluminium foil, cling film)',
    'Value BBQ related','Value Fruit peel & cores','Value Branded other food related',
    'Value Unbranded other food related','Value Clothes & Footwear',
    'Value Textiles','Value Other household',
    'Value Cigarette Butts','Value Nicotine pouches', 'Value Other nicotine related',
    'Value Unbagged dog poo','Value Needles / syringes','Value Other drug related',
    'Value Nappies', 'Value Period products','Value Covid Masks',
    'Value First Aid & medcal waste','Value Other hazardous', 'Value Camping',
    'Value Fireworks','Value Seasonal (Christmas and/or Easter)',
    'Value Outdoor event related (e.g.race)',
    'Value Biking specific','Value Hiking specific','Value Other outdoor related',
    'Value Too small/dirty to ID','Value Other Miscellaneous']
    
    
    plastics = survey[plastic].sum(axis=0).to_list()
    metals = survey[metal].sum(axis=0).to_list()
    glasses = survey[glass].sum(axis=0).to_list()
    papers = survey[cardboard_paper_wood].sum(axis=0).to_list()       
    potentially_plastics = survey[potentially_plastic].sum(axis=0).to_list()
    others = survey[other].sum(axis=0).to_list()     
    
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

    tot_items_surveys = df2['TotItems'].sum()
    sup = [x for x in SUP if pd.notna(x)]
    
    tot_SUP = sum(sup)  
    #calcualte percentage
#SUP proportion % reported    
    tot_percSUP = tot_SUP/tot_items_surveys *100   
    
    #check SUP percentage
    col_list_SUP = ['Value Full Dog Poo Bags','Value Unused Dog Poo Bags',
    'Value Plastic Water Bottles', 'Value Plastic Soft Drink Bottles',
    'Value Aluminium soft drink cans','Value Glass soft drink bottles',
    'Value Milkshake bottle or carton', 'Value Plastic energy drink bottles',
    'Value Aluminium energy drink can','Value Plastic energy gel sachet',
    'Value Plastic energy gel end','Value Protein drink bottle or carton', 
    'Value Aluminium alcoholic drink cans','Value Glass alcoholic bottles',
    'Value Hot drinks cups','Value Hot drinks tops and stirrers',
    'Value Cold drinks cups and tops','Value Cartons','Value Plastic straws',
    'Value Paper straws','Value Plastic bottle, top', 'Value Glass bottle tops', 
    'Value Ring pull', 'Value Plastic bottle sleeve',  
    'Value Other drink related', 'Value Confectionary/sweet wrappers',
    'Value Wrapper "corners" / tear-offs',
    'Value Other confectionary (eg., Lollipop Sticks)',
    'Value Crisps Packets', 'Value Used Chewing Gum',
    'Value BBQ related',
    'Value Branded single-use carrier bags',
    'Value Unbranded single-use carrier bags', 
    'Value Branded plastic fast / takeaway food packaging / utensils',
    'Value Unbranded plastic fast / takeaway food packaging / utensils',
    'Value Branded card or wood fast / takeaway food packaging / utensils',
    'Value Unbranded card or wood fast / takeaway food packaging / utensils',
    'Value Branded condiments packaging','Value Unbranded condiments packaging',
    'Value Branded food on the go','Value Unbranded food on the go',
    'Value Branded other food related','Value Unbranded other food related',
    'Value Plastic milk bottles',
    'Value Plastic food containers','Value Cardboard food containers',
    'Value Cigarette Butts','Value Nicotine pouches',
    'Value Disposable vapes', 'Value Nicotine related packaging',
    'Value Needles / syringes', 'Value Other drug related',
    'Value Toilet tissue','Value Face/ baby wipes',
    'Value Nappies', 'Value Period products', 'Value Covid Masks',
    'Value First Aid & medcal waste', 'Value Fireworks',
    'Value Seasonal (Christmas and/or Easter)', 'Value Rubber balloons',
    'Value Foil balloons','Value Cable ties',
    'Value Miscellaneous soft plastic',
    'Value Too small/dirty to ID',
    'Value Other Miscellaneous']
     
    calc_perc_SUP = []
    df_new = survey[all_items]
    df2 = df_new[df_new.any(axis=1)]
    for index, i in df2.iterrows():
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
    'Value Other Pet Related Stuff']
    
    drinks_related = ['Value Plastic Water Bottles',
    'Value Plastic Soft Drink Bottles','Value Aluminium soft drink cans',
    'Value Glass soft drink bottles','Value Milkshake bottle or carton',
    'Value Plastic energy drink bottles','Value Aluminium energy drink can',
    'Value Plastic energy gel sachet','Value Plastic energy gel end',
    'Value Protein drink bottle or carton', 'Value Aluminium alcoholic drink cans',
    'Value Glass alcoholic bottles','Value Hot drinks cups',
    'Value Hot drinks tops and stirrers','Value Cold drinks cups and tops',
    'Value Cartons','Value Plastic straws','Value Paper straws',
    'Value Plastic bottle, top', 'Value Glass bottle tops', 'Value Ring pull', 
    'Value Plastic bottle sleeve','Value Reusable drinks container',
    'Value Other drink related',]
    
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

    pets = survey[pet_stuff].sum(axis=0).to_list()
    drinks = survey[drinks_related].sum(axis=0).to_list()
    snacks = survey[snack].sum(axis=0).to_list()
    smokes = survey[nicotine].sum(axis=0).to_list()
    agros = survey[agro_ind].sum(axis=0).to_list()
    hyg = survey[hygiene].sum(axis=0).to_list()
    recre = survey[recreation].sum(axis=0).to_list()
    home = survey[house].sum(axis=0).to_list()
    miscs = survey[misc].sum(axis=0).to_list()

    totpet = sum(pets)
    totdrs = sum(drinks)
    totsn = sum(snacks)
    totsm = sum(smokes)
    totag = sum(agros)
    tothy = sum(hyg)
    totrec = sum(recre)
    totho = sum(home)
    totmis = sum(miscs)
 

    catdf = pd.DataFrame({'type': ['pet stuff','drinks','snacks','smoking', 'agro_ind',
                                   'hygiene','recreational','household','miscellaneous'],
                           'quantity':[totpet, totdrs, totsn, totsm, totag, tothy,
                                       totrec, totho, totmis]})
    
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
        
    DRS_items = survey[DRS].sum(axis=0).to_list()   
    glass_DRS_items = survey[DRS_glass].sum(axis=0).to_list()  


    lite_DRS = []
    for index,i in lite.iterrows():
        if i['Categories - Drinks Containers']==True:
            lite_DRS.append(1)
            
    DRS_lite = sum(lite_DRS)
    tot_DRS_subs = subs_indy + DRS_lite   
      
    subs_presence = survey[all_presence]
    s_subs_report_presence = subs_presence.any(axis=1).sum()
    subs_reporting_presence_withLITE = [s_subs_report_presence, count_lite]
    subs_for_presence = s_subs_report_presence.sum()
    subs_for_presence_wLITE = sum(subs_reporting_presence_withLITE)

    
#% Submissions reporting DRS                
    DRS_reported = (tot_DRS_subs/subs_for_presence_wLITE)*100
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
    
    sub_EPR =   ['Plastic energy gel sachet','Plastic energy gel end', 
    'Protein drink bottle or carton','Milkshake bottle or carton',
    'Hot drinks cups','Hot drinks tops and stirrers',
    'Cold drinks cups and tops','Cartons','Plastic straws','Paper straws',
    'Plastic bottle, top','Glass bottle tops', 'Ring pull', 
    'Plastic bottle sleeve','Confectionary/sweet wrappers',
    'Wrapper "corners" / tear-offs',
    'Other confectionary (eg., Lollipop Sticks)',
    'Crisps Packets','Branded single-use carrier bags',
    'Unbranded single-use carrier bags', 
    'Branded bag for life','Unbranded bag for life', 
    'Branded plastic fast / takeaway food packaging / utensils',
    'Unbranded plastic fast / takeaway food packaging / utensils',
    'Branded card or wood fast / takeaway food packaging / utensils',
    'Unbranded card or wood fast / takeaway food packaging / utensils',
    'Branded condiments packaging','Unbranded condiments packaging',
    'Branded food on the go','Unbranded food on the go',
    'Plastic milk bottles','Glass milk bottles',
    'Plastic food containers','Cardboard food containers',
    'Cleaning products containers','Cosmetics / deodorants', 
    'Nicotine related packaging']
    
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
    'Value Nicotine related packaging']
     
    df_EPR_subs = survey[sub_EPR]    
    subs_EPR_indy = df_EPR_subs.any(axis=1).sum()

    EPR_items = survey[EPR].sum(axis=0).to_list()   
  
    tot_EPR_subs = subs_EPR_indy 
              
#% Submissions reporting EPR                
    EPR_reported = (tot_EPR_subs/subs_for_presence)*100
#EPR total items
    EPR_tot_items = sum(EPR_items)
    
#% of total items that are EPR - from those reporting breakdown
    EPR_proportion = (EPR_tot_items/total_reported_items)*100
    
    
    vapes_indy = ['Disposable vapes','Value Disposable vapes']   
    survey['Disposable vapes'] = pd.to_numeric(survey['Disposable vapes'], errors='coerce').fillna(0).astype(int)
    vape_items_indy = survey[vapes_indy].sum(axis=0).to_list()
               
    vapes_subs = vape_items_indy[0]
#vapes_total_items   
    vapes_total = vape_items_indy[1]
       
#% submissions reporting vapes    
    vapes_reported = (vapes_subs/count_survey)*100
    
#% of total items that are vapes
    vapes_proportion = (vapes_total/total_reported_items)*100
#% of smoking items that are vapes    
    if totsm == 0:
        vapes_in_smoke = 0
    else:
        vapes_in_smoke = (vapes_total/totsm)*100
     
    gel_end_subs_indy = []
    no_gelends_indy = []
    for index, i in survey.iterrows():
        gelend = i['Plastic energy gel end']
        no_gelends = i['Value Plastic energy gel end']
        gel_end_subs_indy.append(gelend)
        no_gelends_indy.append(no_gelends)
    gelends_subs_indy = [x for x in gel_end_subs_indy if str(x) != 'nan']    
    gelend_subs = len(gelends_subs_indy)  
    gelends_indy = [x for x in no_gelends_indy if str(x) != 'nan']
#gel ends_total_items
    gelends_total = sum(gelends_indy)     
#% submissions reporting gel ends    
    gelends_reported = (gelend_subs/count_survey)*100
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
    gel_subs = len(gels_subs_ind)  

    gels_indy = [x for x in no_gels_indy if str(x) != 'nan']
#gel ends_total_items    
    gels_total = sum(gels_indy)     
#% submissions reporting gel ends    
    gels_reported = (gel_subs/count_survey)*100

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
                
    all_bags = len(bag)
#% submissions reporting poo bags   
    bags_reported = (all_bags/count_survey)*100
#poo bags_total_items    
    bags_total = sum(poo)   
#% of total items that are poo bags
    bags_proportion = (bags_total/total_reported_items)*100


    outdoor = ['Value Camping','Value Biking specific','Value Hiking specific',
               'Value Other outdoor related']
    
    out = []
    out_subs = []
    out_df = survey[outdoor]

    for index, i in out_df.iterrows():
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
    outs_reported = (tot_out_subs/subs_for_presence)*100
#outdoor gear_total_items    
    outs_total = sum(out)   
#% of total items that are outdoor gear
    outs_proportion = (outs_total/total_reported_items)*100        
        


    #calculate brands

    brands = ['Lucozade', 'Ribena','RedBull','Monster','High5','SIS','Danone',
    'Highland Spring','Coke','Costa','Pepsi','Walkers','Barrs','Britvic',
    'Mars','Nestle','Mondelez','Cadbury','Magnum','Haribo','AB InBev','Corona',
    'Molson Corrs','Thatchers','Heineken','Fosters','Bulmers','Carlsberg',
    'Burger King','Greggs','KFC','McDonalds','Subway','Aldi','Co-op',
    'Euro Shopper','LiDL','M&S','Tesco','Other']
    
  
    survey[brands] = survey[brands].replace('x', 1).apply(pd.to_numeric, errors='coerce')
    
    brands_sum = survey[brands].sum().reset_index()
    brands_sum.columns = ['brand', 'Total']

    # Sort by prevalence
    brands_sum = brands_sum.sort_values(by='Total', ascending=False)
    #brands 1, 2 and 3    
    brand1 = brands_sum.iloc[0]['brand']
    brand2 = brands_sum.iloc[1]['brand']
    brand3 = brands_sum.iloc[2]['brand']
                             
    brands_sum.to_csv(folderout + 'brands.csv', index=False)
    
    #maybe work out something here to deal with other brands once you see what inputs you get...
    #it may need to be something like the animal info from pre-2026
    #ALSO have lost data from TFR and CS survey
    #can also add in here if we get tiered data! But keep an eye for now
    
    new_row = pd.DataFrame([{'survey_submisssions':count_survey,
                'total items surveyed':fully_surveyed_items, 
                'total composition items':total_reported_items, 
                'weight removed':total_kg, 
                'volume removed':total_cokecans, 'distance_kms':km_survey, 
                'most common material':most_type, 
                'SUP reported':tot_percSUP,'SUP calculated':tot_calc_SUP,
                'most common category':most_cat,'DRS reported':DRS_reported,
                'DRS total items':DRS_tot_items,'DRS total glass':DRS_tot_glass,
                'DRS % of total items':DRS_proportion,'glass DRS % of DRS items':glass_DRS_proportion,
                'glass DRS % of total items':glass_proportion,'EPR reported':EPR_reported,
                'EPR total items':EPR_tot_items,'EPR % of total items':EPR_proportion,
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
    survey_AIcols = ['AnimalsY','AnimalsN']
    lite_AIcols = ['Animal Interaction - No',
               'Animal Interaction - Chew Marks','Animal Interaction - Death']
    
    AI_survey = survey[survey_AIcols].notna().any(axis=1).sum()
    AI_lite = lite[lite_AIcols].any(axis=1).sum()
    
    AI_subs = [AI_survey, AI_lite]
    subs_tot = sum(AI_subs)
    survey_AI = survey['AnimalsY'].value_counts().get('Yes', 0)
    lite_AI = (lite['Animal Interaction - Chew Marks'] | lite['Animal Interaction - Death']).sum()
    AI_yes = [survey_AI, lite_AI]
    AI_tot = sum(AI_yes)
    
#percent submissions reporting AI observed

    perc_AI = (AI_tot/subs_tot)*100
    
    survey['AIDeath'] = survey['AIDeath'].replace(['X', 'x'], 1)
    survey['AIDeath'] = pd.to_numeric(survey['AIDeath'], errors='coerce')
    
    deaths = []
    death_survey = survey['AIDeath'].sum()
    deaths.append(death_survey)

    lite_death = lite['Animal Interaction - Death'].sum()
    deaths.append(lite_death)
    
    tot_deaths = sum(deaths)
    subs_for_death = [AI_survey, AI_lite]
    death_subs_tot = sum(subs_for_death)
#percent submissions reporting death of those reporting they checked for AI  
    perc_death = (tot_deaths/death_subs_tot)*100
    
    survey_1st = survey['First time'].value_counts().get('This is my first time!', 0)
    if count['First_time'].isna().all:
        count_1st = 0
    else:
        count_1st = count['First_time'].value_counts().get('This is my first time!', 0)

    subs_for_1st = [survey_1st, count_1st]
#number submitting for first time - not lite    
    no_1st = sum(subs_for_1st)
    
    if 'Community Hub' not in count.columns:
        count.rename(columns={'CH': 'Community Hub'}, inplace=True)    
    
    dfs = [count, survey]
    
    befores = []
    for df in dfs:        
        if 'A-Team' not in survey.columns:
            survey.rename(columns={'A-Team ': 'A-Team'}, inplace=True)
            
        multiple_cols = ['Volunteer','A-Team','Community Hub']
        before = df[multiple_cols].notna().sum()
        before_tot = sum(before)
        befores.append(before_tot)
     
#number submitting again - not including CS or lite        
    beforers = sum(befores)    
    
    #count is place connection, new survey is place and nature, lite is nature 
    if 'Connection_ConnectionY' not in count.columns:
        count.rename(columns={'Connect_ConnectY': 'Connection_ConnectionY'}, inplace=True) 
        count.rename(columns={'Connect_ConnectN': 'Connection_ConnectionN'}, inplace=True)
        count.rename(columns={'Connect_ConnectSame': 'Connection_ConnectionSame'}, inplace=True)
        count.rename(columns={'Connect_ConnectNotSure': 'Connection_Unsure'}, inplace=True)
    
    place_connection = []
    ncounts_connect = []
    pcounts_connect = []
    nature_connection = []

    #count df
    place_connected = count['Connection_ConnectionY'].value_counts().get('Yes', 0) 
    place_connection.append(place_connected)
    columns_of_interest = ['Connection_ConnectionY', 'Connection_ConnectionN', 
                               'Connection_ConnectionSame', 'Connection_Unsure'] 
    count_connect = count[columns_of_interest].notnull().any(axis=1).sum()
    pcounts_connect.append(count_connect)
    
    #lite df
    lite_connects = lite['nature_connection'] >= 6
    lite_connect = (lite_connects == True).sum()  
    nature_connection.append(lite_connect)

    count_rows = lite['nature_connection'].notna().sum()
    ncounts_connect.append(count_rows)

    #survey df
    survey_nature = survey['Experience_NatureConnect'] >= 6
    s_nature = (survey_nature == True).sum()
    nature_connection.append(s_nature)
    
    survey_place = survey['Experience_Place'] >= 6
    s_place = (survey_place == True).sum()
    place_connection.append(s_place)
                            
    sn_rows = survey['Experience_NatureConnect'].notna().sum()
    ncounts_connect.append(sn_rows)

    sp_rows = survey['Experience_Place'].notna().sum()
    pcounts_connect.append(sp_rows)                        
                            
    
    total_answer_connect_n = sum(ncounts_connect)
    total_answer_connect_p = sum(pcounts_connect)
    nature_connects = sum(nature_connection)
    place_connects = sum(place_connection)
#percent feeling more connected    
    perc_more_nconnected = (nature_connects/total_answer_connect_n) *100
    perc_more_pconnected = (place_connects/total_answer_connect_p) *100

    perma_count = survey['perma_score'].notna().sum()
    perma_wb = survey['perma_score'] >= 6
    no_perma_wb = (perma_wb == True).sum()
    
    perc_inc_wb = (no_perma_wb/perma_count) *100
    
    again = survey['Connection_TakePartAgainY'].value_counts().get('Yes', 0)
    again_cols = ['Connection_TakePartAgainY', 'Connection_TakePartAgainN', 'Connection_TakePartAgainUnsure']
    answered_again = survey[again_cols].notnull().any(axis=1).sum()
#percentage who would participate again
    perc_participate_again = (again/answered_again)*100

    dfs = [count, survey, lite]
    if 'Email' not in count.columns:
        count.rename(columns={'email': 'Email'}, inplace=True)     
        
    contacts = []
    for df in dfs:
        contact = df['email_id'].notnull().sum()
        contacts.append(contact)
    
    no_subs = [count_count, count_survey, count_lite]
    contact_deets = sum(contacts)
    subs_contact = sum(no_subs)
#percent leaving contact details    
    perc_contacts = (contact_deets/subs_contact)*100

    new_row = pd.DataFrame([{'Fauna Interaction':perc_AI, 
                    'Fauna Death':perc_death,'First Time':no_1st, 
                    'Repeat volunteers':beforers,#'Felt proud':perc_proud,
                       'Felt more connected to nature':perc_more_nconnected,
                       'Felt more connected to place':perc_more_pconnected,
                       'Percent with positive well-being':perc_inc_wb,
                       'Would do again':perc_participate_again,
                       'provided contact info':perc_contacts}])
    impacts_results = pd.concat([impacts_results, new_row], ignore_index=True)    
    
    impacts_results.to_csv(folderout + '/impacts.csv', index=False) 
           
            
            
            
            
            
            
    
    
                                      

    
    


    
    
    
        
        
        
    
    
    
    
    
    