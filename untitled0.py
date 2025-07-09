#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 14:57:04 2025

@author: heatherkay
"""

#Investigating ATI numbers for differnt survey types

    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    
    #create df for results - or could read in and append to overall stats sheet
    results = pd.DataFrame(columns = ['month','ATI_survey_orig', 'ATI_CSsurvey',
                                      'ATI_count', 'ATI_CScount', 'ATI_survey_new',
                                      'ATI_lite'])

    
    for month in months:
    
        survey = pd.read_csv(folderin + 'survey_' + month + '.csv')
        lite = pd.read_csv(folderin + 'lite_' + month + '.csv')
        count = pd.read_csv(folderin + 'count_' + month + '.csv')
        CSsurvey = pd.read_csv(folderin + 'CS_survey_' + month + '.csv')
        CScount = pd.read_csv(folderin + 'CS_count_' + month + '.csv')
        bag_res_lite = pd.read_csv(folderin + 'bag_res_lite_' + month + '.csv')
     
        count_survey = len(survey.index)    
        count_lite = len(lite.index)
        count_count = len(count.index)
        count_CSsurvey = len(CSsurvey.index)
        count_CScount = len(CScount.index)

        ATI_srvy = survey['AdjTotItems']
        ATI_srvy_correct_itms = [x for x in ATI_srvy if str(x) != '#DIV/0!']
        ATI_srvy_correct = [float(i) for i in ATI_srvy_correct_itms]
        ATI_survey = sum(ATI_srvy_correct) / count_survey
           
        ATI_CSS = []
        for index, i in CSsurvey.iterrows():
            TotItems = i['TotItems']#.astype(float)
            people = i['People']#.astype(float)
            hours = i['Time_hours']#.astype(float)
            time = hours*60
            area = i['Area_km2']#.astype(float)
            km = area / 0.006
            #calculate ATI
            denominator = (people*time)*km
            if denominator == 0:
                continue
            AdjTotItems = TotItems/denominator 
            if AdjTotItems > 0:
                ATI_CSS.append(AdjTotItems)
        
        if CSsurvey.empty:
            continue
        else:
            Tot_CSS = sum(ATI_CSS) / count_CSsurvey    
        
        ATI_C = []
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
                ATI_C.append(AdjTotItems)
      
        if count.empty:
            continue
        else:                
            Tot_C = sum(ATI_C) / count_count   

        ATI_CSC = []
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
                ATI_CSC.append(AdjTotItems) 
                
        if CScount.empty:
            continue
        else:              
            Tot_CSC = sum(ATI_CSC) / count_CScount 
        
        
        lite_denom = (lite_people*lite_time)*lite_km
        if lite_denom == 0.0:
            ATI_lite = 0.0
        else:
            ATI_lite = lite_items/lite_denom

        ATI_S = []
        for index, i in survey.iterrows():
            TotItems = i['TotItems']#.astype(float)
            people = i['People']#.astype(float)
            time = i['Time_min']#.astype(float)
       
            #area = i['Area_km2']#.astype(float)
            km = i['Distance_km']
            #calculate ATI
            denominator = (people*time)*km
            if denominator == 0:
                continue
            AdjTotItems = TotItems/denominator 
            if AdjTotItems > 0:
                ATI_S.append(AdjTotItems)               

        ATI_S = sum(ATI_S) / count_survey
        
        
        results = results.append({'month':month, 'ATI_survey_orig':ATI_survey, 
                                  'ATI_CSsurvey':ATI_CSS,'ATI_count':ATI_C, 
                                  'ATI_CScount':ATI_CSC, 'ATI_survey_new':ATI_S,
                                  'ATI_lite':ATI_lite}, ignore_index=True)                                         
    
        results.to_csv(folderout + '/overview.csv',index=False)    
        
   
#finding patterns

    df = pd.read_csv(TFTin)
    
    items = df['AdjTotItems']
    tot_items = df['Distance_km']
    
    #plot the result
    fig = plt.figure(); ax = fig.add_subplot(1,1,1)
    plt.rcParams.update({'font.size':12})
    #plots H_100 on x with I_CD on y
    ax.scatter(items,tot_items,marker='.')
    #sets title and axis labels
    ax.set_title('Distance v ATI')
    ax.set_ylabel('Distance')
    ax.set_xlabel('Adjusted total items')
    #ax.set_xlim([0, 600])
    #ax.set_ylim([0,500])  
    #obtain m (slope) and b(intercept) of linear regression line
    m, b = np.polyfit(items, tot_items, 1)
    #add linear regression line to scatterplot 
    plt.plot(items, m*items+b)
    plt.close        
        