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
    results = pd.DataFrame(columns = ['total_submisssions', 'total_count', 'total_survey',
                                      'no_people', 'area_km2', 'distance_km','duration_hours', 
                                      'items_removed','items_surveyed', 'total_items',
                                      'total_kg','total_cokecans'])
    
      
    survey = pd.read_csv(folderin + 'survey.csv')
    lite = pd.read_csv(folderin + 'lite.csv')
    count = pd.read_csv(folderin + 'count.csv')
    CSsurvey = pd.read_csv(folderin + 'CS_survey.csv')
    CScount = pd.read_csv(folderin + 'CS_count.csv')
    bag_res_lite = pd.read_csv(folderin + 'bag_res_lite.csv')
    
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
    tot_people.append(count_lite)
    tot_people.append(count_count)
 
#volunteers
    total_people = sum(tot_people)
    
    survey_km = survey['Distance_km'].sum()
    count_m = count['Total_distance_m'].sum()
    count_km = count_m / 1000
    CScount_m = CScount['Total_distance_m'].sum()
    CScount_km = CScount_m / 1000
    
    survey_area = survey_km * 0.006
    count_area = count_km * 0.006
    CScount_area = CScount_km * 0.006
    CSsurvey_area = CSsurvey['Area_km2'].sum()
    
    areas = [survey_area, count_area, CScount_area, CSsurvey_area]
#area cleaned / surveyed - excludes Lite
    area = areas.sum()   
    
    CSsurvey_km = CSsurvey_area / 0.006
    kms = [survey_km, count_km, CSsurvey_km, CScount_km]
#distance cleaned / surveyed - excludes Lite
    km = kms.sum()
        
    #method to estimate time spent on count
    count_time = count_count * 1.52
    tot_time.apppend(count_time)
#time - excludes Lite
    total_time = sum(tot_time) #doesn't include lite - no data

    
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
    
    removed_items = sum(rmv_items)
    surveyed_items = sum(srvy_items)    
    tot_items = surveyed_items
    tot_items.append(lite_items)
#total items
    total_items = sum(tot_items)
#weight removed items
    total_kg = removed_items / 57  
#volume of removed items as number of coke cans
    total_cokecans = removed_items / 1.04
    
    results = results.append({'total_submisssions':total_CS, 'total_count':total_count,
                              'total_survey':total_survey,'no_people':total_people, 
                              'area_km2':area, 'distance_km':km,
                              'duration_hours':total_time, 'items_removed':removed_items,
                              'items_surveyed':surveyed_items, 'total_items':total_items,
                              'total_kg':total_kg,'total_cokecans':total_cokecans}, ignore_index=True)                                         
    
    results.to_csv(folderout + '/overview.csv')    
    
    

    count_results = pd.DataFrame(columns = ['count_submisssions', 'prevalence', 'hotspots',
                                      'worst_zone'])
    
    #this will only work once dfs are the same 
    #dfs = (count, CScount) 
    #df = pd.concat(dfs, ignore_index = True) 
    #km = df['Distance_km'].sum()
    #items = df['TotItems'].sum()  
    #prevalence = items/km
    
    distance = CScount_km + count_km
    items = CScount_items + count_items
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

    count_results = count_results.append({'count_submisssions':total_count, 
                'prevalence':prevalence,
                'worst_zone':topzone}, ignore_index=True)  

    count_results.to_csv(folderout + '/count.csv')  
    
    survey_results = pd.DataFrame(columns = ['survey_submisssions', 'total items removed', 
                'weight removed', 'volume removed', 'distance_kms', 'area kms2',
                'most common material', 'SUP reported','SUP calculated','most common category',
                'DRS reported','DRS total items','DRS total glass','vapes reported',
                'vapes total items','gel ends reported','gel ends total items',
                'poo bags reported','poo bags total items','brand 1','brand 2',
                'brand 3'])


#Survey stats
    
#first ones currently covered in overvies
    values = [total_survey, count_lite]
    total_all_survey = sum(values)
    
    kms_survey = [survey_km, CSsurvey_km] 
#distance covered - doesn't include Lite    
    km_survey = kms_survey.sum()
    
    areas_survey = [survey_area,  CSsurvey_area]
#area directly protected - excludes Lite
    area_survey = areas_survey.sum()   
    
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
             'Value utdoor event (eg Festival)','Value Camping','Value Halloween & Fireworks','Value Seasonal (Christmas and/or Easter)',
             'Value MTB related (e.g. inner tubes, water bottles etc)',
             'Value Running','Value Roaming and other outdoor related (e.g. climbing, kayaking)',
             'Value Outdoor sports event related (e.g.race)','Value Textiles','Value Clothes & Footwear',
             'Value Miscellaneous','Value Too small/dirty to ID','Value Weird/Retro']
    
    
    plastics = []
    metals = []
    glasses = []
    papers = []
    for p in plastic:
        item = survey[p].sum()
        CSitem = CSsurvey[p].sum()
        total = item + CSitem
        plastics.append(total)
        
    for p in metal:
        item = survey[p].sum()
        CSitem = CSsurvey[p].sum()
        total = item + CSitem
        metals.append(total)

    for p in glass:
        item = survey[p].sum()
        CSitem = CSsurvey[p].sum()
        total = item + CSitem
        glasses.append(total)

    for p in cardboard_paper_wood:
        item = survey[p].sum()
        CSitem = CSsurvey[p].sum()
        total = item + CSitem
        papers.append(total)
    
    totpl = sum(plastics)
    totme = sum(metals)
    totgl = sum(glasses)
    totpa = sum(papers)    

    typedf = pd.DataFrame({'type': ['plastic','metal','glass','paper'],
                           'quantity':[totpl, totme, totgl,totpa]})
    
  

    s = typedf.max()
#Most common material    
    most_type = s['type']  

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
    for index, i in df2.iterrows():
        SUP_items = i[col_list_SUP].sum()   
        tot_items = i['TotItems']
        calculated_SUP = (SUP_items/tot_items)*100
        calc_perc_SUP.append(calculated_SUP)
        
    for index, i in df3.iterrows():
        SUP_items = i[col_list_SUP].sum()   
        tot_items = i['TotItems']
        calculated_SUP = (SUP_items/tot_items)*100
        calc_perc_SUP.append(calculated_SUP)        
        
#SUP proportion % calculated          
    tot_calc_SUP = calc_perc_SUP.sum()      
    
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

    pets = []
    drinks = []
    snacks = []
    smokes = []
    agros = []
    hyg = []
    recre = []
    sport = []
    text = []
    home = []
    miscs = []
    for p in pet_stuff:
        item = survey[p].sum()
        CSitem = CSsurvey[p].sum()
        total = item + CSitem
        pets.append(total)
        
    for p in drinks_containers:
        item = survey[p].sum()
        CSitem = CSsurvey[p].sum()
        total = item + CSitem
        drinks.append(total)

    for p in snack:
        item = survey[p].sum()
        CSitem = CSsurvey[p].sum()
        total = item + CSitem
        snacks.append(total)

    for p in smoking:
        item = survey[p].sum()
        CSitem = CSsurvey[p].sum()
        total = item + CSitem
        smokes.append(total)
        
    for p in agro_ind:
        item = survey[p].sum()
        CSitem = CSsurvey[p].sum()
        total = item + CSitem
        agros.append(total)

    for p in hygiene:
        item = survey[p].sum()
        CSitem = CSsurvey[p].sum()
        total = item + CSitem
        hyg.append(total)

    for p in recreation:
        item = survey[p].sum()
        CSitem = CSsurvey[p].sum()
        total = item + CSitem
        recre.append(total)

    for p in sports:
        item = survey[p].sum()
        CSitem = CSsurvey[p].sum()
        total = item + CSitem
        smokes.append(total)

    for p in textiles:
        item = survey[p].sum()
        CSitem = CSsurvey[p].sum()
        total = item + CSitem
        text.append(total)

    for p in house:
        item = survey[p].sum()
        CSitem = CSsurvey[p].sum()
        total = item + CSitem
        home.append(total)

    for p in misc:
        item = survey[p].sum()
        CSitem = CSsurvey[p].sum()
        total = item + CSitem
        miscs.append(total)        
    
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
    
    c = catdf.max()
#Most common category of SUP    
    most_cat = c['type']    

      
    DRS = ['Value Plastic Water Bottles','Value Plastic Soft Drink Bottles',
    'Value Aluminium soft drink cans','Value Plastic bottle, top','Value Glass soft drink bottles',
    'Value Plastic energy drink bottles','Value Aluminium energy drink can',
    'Value Aluminium alcoholic drink cans','Value Glass alcoholic bottles']
    
    DRS_glass = ['Value Glass soft drink bottles','Value Glass alcoholic bottles']
    
    DRS_submissions = []
    DRS_glass_ttl = []
    for index, i in survey.iterrows():
        DRS_items = i[DRS].sum() 
        glass_itms = i[DRS_glass].sum()
        if DRS_items > 0:
            DRS_submissions.append(DRS_items)
        DRS_glass_ttl.append(glass_itms)
        
    for index, i in CSsurvey.iterrows():
        DRS_items = i[DRS].sum() 
        glass_itms = i[DRS_glass].sum()
        if DRS_items > 0:
            DRS_submissions.append(DRS_items)
        DRS_glass_ttl.append(glass_itms)
        
    DRS_subs = len(DRS_submissions)
    
    lite_DRS = []
    for index,i in lite.iterrows():
        if i['Categories - Drinks Containers']=='TRUE':
            lite_DRS.append(1)
            
    DRS_lite = sum(lite_DRS)
    tot_DRS_subs = DRS_subs + DRS_lite   
    subs_for_DRS = [count_survey, count_CSsurvey, count_lite]
    subs = sum(subs_for_DRS)
    
#% Submissions reporting DRS                
    DRS_reported = (tot_DRS_subs/subs)*100
#DRS total items
    DRS_tot_items = sum(DRS_submissions)
#DRS total glass items
    DRS_tot_glass = sum(DRS_glass_ttl)
    
    vaping = []
    for index, i in survey.iterrows():
        vapes = i['Value Disposable vapes']
        if vapes > 0:
            vaping.append(vapes)
            
    vapes_subs = len(vaping)
#% submissions reporting vapes    
    vapes_reported = (vapes_subs/total_survey)*100
#vapes_total_items    
    vapes_total = sum(vaping)
    
    gel_ends = []
    for index, i in survey.iterrows():
        ends = i['Value Plastic energy gel end']
        if ends > 0:
            gel_ends.append(ends)
            
    gel_subs = len(gel_ends)
#% submissions reporting gel ends    
    gels_reported = (gel_subs/total_survey)*100
#gel ends_total_items    
    gels_total = sum(gel_ends)
    
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
#% submissions reporting gel ends    
    bags_reported = (all_bags/total_survey)*100
#gel ends_total_items    
    bags_total = sum(poo)    

    #calculate brands
    brands = ['Lucozade','Coke','RedBull','Monster','Cadbury','McDonalds','Walkers','Mars','StellaArtois','Strongbow',
              'Costa','Budweiser','Haribo','SIS','Carling','Fosters','Thatchers','Pepsi','Nestle','Subway','Other']
    
    brand_res = pd.DataFrame(columns = ['brand','count'])
                             
    for b in brands:
        b1 = survey[survey['B1_' + b].notna()]
        b2 = survey[survey['B2_' + b].notna()]
        b3 = survey[survey['B3_' + b].notna()]
        b1CS = CSsurvey[CSsurvey['B1_' + b].notna()]
        b2CS = CSsurvey[CSsurvey['B2_' + b].notna()]
        b3CS = CSsurvey[CSsurvey['B3_' + b].notna()]        
        dfs = (b1, b2, b3, b1CS, b2CS, b3CS)
        brand = pd.concat(dfs, ignore_index = True)
        count = len(brand.index)
        brand_res = brand_res.append({'brand':b, 'count':count}, ignore_index=True)
    
    test = brand_res.sort_values(by = ['count'], ascending=False)
#brands 1, 2 and 3    
    brand1 = test.iloc[0]['brand']
    brand2 = test.iloc[1]['brand']
    brand3 = test.iloc[2]['brand']
    
    test.to_csv(folderout + 'brands.csv')
    
    survey_results = survey_results.append({'survey_submisssions':total_all_survey,
                'total items removed':removed_items, 'weight removed':total_kg, 
                'volume removed':total_cokecans, 'distance_kms':km_survey, 
                'area kms2':area_survey,'most common material':most_type, 
                'SUP reported':tot_percSUP,'SUP calculated':tot_calc_SUP,
                'most common category':most_cat,'DRS reported':DRS_reported,
                'DRS total items':DRS_tot_items,'DRS total glass':DRS_tot_glass,
                'vapes reported':vapes_reported,'vapes total items':vapes_total,
                'gel ends reported':gels_reported,'gel ends total items':gels_total,
                'poo bags reported':bags_reported,'poo bags total items':bags_total,
                'brand 1':brand1,'brand 2':brand2,'brand 3':brand3}, ignore_index=True)  

    survey_results.to_csv(folderout + '/survey.csv')  
    
    

    
    
    
    
            
            
    

    
    
                          
           
            
            
            
            
            
            
    
    
                                      

    
    
#COMPARE ORIG & CS DATA

    
    
    
        
        
        
    
    
    
    
    
    