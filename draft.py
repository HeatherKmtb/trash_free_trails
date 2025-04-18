#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 10:45:15 2025

@author: heatherkay
"""
months = ['4','5','6','7','8','9','10','11','12']
years = ['2024','2025']

   
     year = '2024'
     survey_results = pd.DataFrame(columns = ['month','survey_submisssions', 'total items removed', 
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
     
     #create df for results - or could read in and append to overall stats sheet
     results = pd.DataFrame(columns = ['month','total_submisssions', 'total_survey',
                                       'no_people','duration_hours', 'connected'
                                       ])
     
     count_results = pd.DataFrame(columns = ['month','count_submisssions', 'prevalence', 'hotspots',
                                       'worst_zone'])

     
     for month in months:
     
         survey = pd.read_csv(folderin + 'survey_' + month + '_' + year + '.csv')
         lite = pd.read_csv(folderin + 'lite_' + month + '_' + year + '.csv')
         count = pd.read_csv(folderin + 'count_' + month + '_' + year + '.csv')
         CSsurvey = pd.read_csv(folderin + 'CS_survey_' + month + '_' + year + '.csv')
         CScount = pd.read_csv(folderin + 'CS_count_' + month + '_' + year + '.csv')
         bag_res_lite = pd.read_csv(folderin + 'bag_res_lite_' + month + '_' + year + '.csv')
     
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
             people = []
             hours = []
             for index,i in df.iterrows():
                 peeps = i['People']
                 hour = i['Time_hours']
         #km = df['Distance_km'].sum()
         #items = df['TotItems'].sum()
                 tot_hours = peeps * hour
                 people.append(peeps)
                 hours.append(tot_hours)

             
             
         tot_peeps = sum(people)
         all_hours = sum(hours)
         tot_people.append(tot_peeps)
         tot_time.append(all_hours)
         #tot_km.append(km)
         #tot_items.append(items)
     
     #add to total people the number of lite and count submissions
         lite_people = count_lite * 3.08
         tot_people.append(lite_people)
         tot_people.append(count_count)
  
 #volunteers
         total_people = sum(tot_people)
     
     #method to estimate time spent on count
         count_time = count_count * 1.38
         lite_time = count_lite * 1.64
         tot_time.append(count_time)
         tot_time.append(lite_time)
 #time 
         total_time = sum(tot_time) 
         
         #ONLY NEED TO WORRY ABOUT THOSE THAT SAID YES
        
                 
         connect_survey = survey[survey['Connection_ConnectionY'] == 'Yes']['People'].tolist()
         connect_count = count[count['Connect_ConnectY'] == 'Yes']['People'].tolist()
         connect_CSsurvey = CSsurvey[CSsurvey['Connection_ConnectionY'] == 'Yes']['People'].tolist()
         connect_lite = lite['Increased Nature Connection - Yes'].sum()
         
         connect = connect_survey + connect_count + connect_CSsurvey
         connect1 = sum(connect)
         connected = connect1 + connect_lite
         
             
   
         results = results.append({'total_submisssions':total_CS, 'total_count':total_count,
                               'total_survey':total_survey,'no_people':total_people, 
                               'duration_hours':total_time, 'connected':connected}, ignore_index=True)                                         
     
         results.to_csv(folderout + '/overview.csv',index=False)    
    