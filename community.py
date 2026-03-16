#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 12:42:27 2026

@author: heatherkay
"""

import pandas as pd 
import re   
    
def get_CH_data(TFTin, TFTout, rawin):
    """
    A function which extracts (as best possible) Community Hub submissions
    from the different data streams. Based on presence of the surname of the 
    contact person, the contact email address or a key word from the hub name
    being present in the data.
    
    It saves these filtered submissions to .csv and also extracts date, name of CH,
    how many people, items and kms were on the submission and saves this to 
    another .csv

    Parameters
    ----------
    TFTin : string
             path to input folder with TFT data you want to search
            
    TFTout : string
           path for folder to save filtered .csvs in

    """
    
    ch_contact = ['Berry', 'Scholfield', 'Gwynedd', 'Munroe', 'Radford', 
              'Downing', 'Fielding', 'McKnight', 'McNicol', 'MacDonald', 
              'Kavanagh', 'Elliot-Jones', "O'Brien", 'Wilkinson', 'Copeman',
              'Caddy', 'Davies', 'Holloway', 'Greaves', 'Scott', 'Herbert',
              'Price', 'Hulme', 'Welland', 'Flight', 'Wright', 'Cox', 'Flynn',
              'Cairns', 'Smith', 'Pita', 'Deards', 'Mitchell',
              'Shackell', 'Fowler', 'Halpin', 'Luck', 'Martin', 'Swain',
              'Marshall', 'Wade', 'Herbert', 'Sweetman', 'Parsons',
              'Manning', 'Halliday', 'Hutcheson', 'Rogers', 'Lyon', 'Russell',
              'Dew', "O'Boyle", 'Whittick', 'Patterson', 'Neate', 'Chew', 
              'Jones', 'Hodgson', 'Sheppard', 'Burke', 'Mcwilliam', 
              'Bount', 'Rousell', 'Prebost', 'Evans', 'Nivan',
              'Williams-Green', 'Clements', 'Beverley', 'Cossey', 'Gilbert',
              'Nuttall', 'Skirrow', 'Phillips', 'Clements', 'Ashford', 
              'Redmond', 'Williams', 'Stasiw', 'Sherwood', 'Plenty', 
              'Tortarolo', 'Lima de Campos Castro', 'Jacklin', 'Hitchcock', 
              'Stone', 'Harrop', 'Bailey', 'Flood', 'Banfield', 'Stockton', 
              'Mannion', 'Barratt', 'Hirst', 'Giordo', 'Osborne', 'Cozzani', 
              'Phillips', 'Cooper-Abs', 'Erskine', 'Johnson', 'Peacock', 
              'Finlayson', 'Winder', 'Hutton', 'McCann', 'Swanwick', 
              'Griffiths', 'Escott', 'Elsworth', 'Harrison', 'Glover', 'Finney', 
              'Burke', 'Bulois', 'Irwin', 'Lee', 'Maturin-Bird']    
    
    #rewrite to import from reference .csv
    email_ref_df = email_ref_df = pd.read_csv(rawin + 'email_reference.csv')
    ch_email = email_ref_df.loc[email_ref_df['community'].isin(['CH', 'both']), 'email_id'].astype(str).tolist()

    ch_name = ['Biosphere', 'Coffi', 'TraX', 'Works', 'Dean','Drosi',
           'Dusty','Dyfi','Energise','Evolution','GRVL','Nood',
           'Outside','Rapha','Scoop','Stif','Swinley','Green House',
           'Room','Sheffield','Gwyrdd','Bethel','Poblado','RunCyB',
           'Àban','Adaptive','Tours','Alyth','Sidings','Bear','Tek',
           'Boat', 'Caban', 'Brenin', 'Comrie', 'Whinlatter', 'Dalby', 
           'Dales','Dreigiau','Filcombe','Thorpe', 'Ape', 'Heackels', 'Helensburgh',
           'Holidays','Thetford','Idris','Lewis', 'Kickback','Leisure',
           'View', 'Cannock Chase', 'Blickling', 'Dudmaston', 'Kinder',
           'Wray', 'Ormesby', 'Clumber', 'Fyne', 'Broomfield', 'Knoll', 
           'Tanzania', 'Planet', 'OTEC', 'Outrunners', 'Patagonia',
           'Pau', 'Progression', 'Plas', 'Rise', 'Sky', 'Ride', 
           'Northampton', 'Riverside', 'Roundhouse', 'Laces', 
           'Stanedge', 'Stomping', 'Tarland', 'College', 'Fixer', 
           'Lodge', 'Oyster', 'Surf', 'Cyclery', 'Trailhead', 'Tredz', 'Trek' 
           'Tyred', 'Domestique', 'Venturefield', 'Wadebridge',
           'YG', 'Rikki', 'Dee', 'Challenge', 'Wonder', 'Liguianna', 
           'Paddle', 'Fort', 'Wild', 'Charity', 'Skills', 'Unbound',
           'Misspent', 'Manly', 'MTB23', 'Ochil', 'Mendips', 'Finalborgo',
           'Brick', 'Burlish', 'Hadfer', 'RoundUp219', 'Killerton', 
           'Calderdale', 'Recce', 'Mercia', 'Windmill', 'Garage', 
           'Denbighshire', 'Explorers']


    survey = pd.read_csv(TFTin + 'survey.csv')
    lite = pd.read_csv(TFTin + 'lite.csv')
    count = pd.read_csv(TFTin + 'count.csv')


    #survey - normalize cols
    survey['email_id'] = survey['email_id'].astype(str)
    email_col   = survey['email_id'].str.strip().str.lower().fillna('')
    surname_col = survey['Surname'].str.lower().fillna('')
    hub_col     = survey['Community Hub'].str.lower().fillna('')
    trail_col   = survey['TrailName'].str.lower().fillna('')

    #lite normalize cols
    lite_col = lite['Title'].str.strip().str.lower().fillna('')
    

    #normalize lists
    emails_lower   = [e.strip().lower() for e in ch_email]
    names_lower    = [n.lower() for n in ch_name]
    contacts_lower = [c.lower() for c in ch_contact]

    #build regex patterns for names/contacts
    name_pattern    = '|'.join(re.escape(n) for n in names_lower)
    contact_pattern = '|'.join(re.escape(c) for c in contacts_lower)

    #survey combine filters
    filtered_survey = survey[
        # email exact match
        email_col.isin(emails_lower)
        # OR name appears in email, hub, or trail
        | email_col.str.contains(name_pattern)
        | hub_col.str.contains(name_pattern)
        | trail_col.str.contains(name_pattern)
        # OR contact appears in email or surname
        | email_col.str.contains(contact_pattern)
        | surname_col.str.contains(contact_pattern)
        ]

    #lite combine filters
    filtered_lite = lite[
        lite_col.str.contains(name_pattern)
        | lite_col.str.contains(contact_pattern)
        ]

    #count - normalize cols
    count['email_id'] = count['email_id'].astype(str)
    count['Community Hub'] = count['Community Hub'].astype(str)
    email_col   = count['email_id'].str.strip().str.lower().fillna('')
    surname_col = count['LastName'].str.lower().fillna('')
    hub_col     = count['Community Hub'].str.lower().fillna('')
    trail_col   = count['TrailName'].str.lower().fillna('')
    
    #count combine filters
    filtered_count = count[
        # email exact match
        email_col.isin(emails_lower)
        # OR name appears in email, hub, or trail
        | email_col.str.contains(name_pattern)
        | hub_col.str.contains(name_pattern)
        | trail_col.str.contains(name_pattern)
        # OR contact appears in email or surname
        | email_col.str.contains(contact_pattern)
        | surname_col.str.contains(contact_pattern)
        ]
    filtered_survey['email_id'] = pd.to_numeric(filtered_survey['email_id'], errors='coerce').astype('Int64')
    filtered_count['email_id'] = pd.to_numeric(filtered_count['email_id'], errors='coerce').astype('Int64')
    filtered_lite['email_id'] = pd.to_numeric(filtered_lite['email_id'], errors='coerce').astype('Int64')
    
    filtered_lite.to_csv(TFTout + 'CH_lite.csv', index=False)
    filtered_survey.to_csv(TFTout + 'CH_survey.csv', index=False)
    filtered_count.to_csv(TFTout + 'CH_count.csv', index=False)
    
    results = pd.DataFrame(columns = ['Date', 'Community Hub', 'no_people',
                                      'distance_km', 'total_items',
                                      'Submission Type'])
    
    email_ref_df['email_id'] = email_ref_df['email_id'].astype(str)
    hub_map = email_ref_df.set_index('email_id')['name'].to_dict()
    filtered_survey['email_id'] = filtered_survey['email_id'].astype(str)
    filtered_count['email_id'] = filtered_count['email_id'].astype(str)
    filtered_lite['email_id'] = filtered_lite['email_id'].astype(str)

    # --- 1. Process Survey Data ---
    df_survey = pd.DataFrame({
    'Date': pd.to_datetime(filtered_survey['Date_TrailClean']).dt.strftime('%Y-%m-%d'),
    'Community Hub': filtered_survey['email_id'].map(hub_map).fillna(filtered_survey['Surname']),
    'no_people': filtered_survey['People'],
    'distance_km': filtered_survey['Distance_km'],
    'total_items': filtered_survey['TotItems'],
    'Submission Type': 'Survey'})

    # --- 2. Process Count Data ---
    df_count = pd.DataFrame({
    'Date': pd.to_datetime(filtered_count['Date_Count']).dt.strftime('%Y-%m-%d'),
    'Community Hub': filtered_count['email_id'].map(hub_map).fillna(filtered_count['LastName']),
    'no_people': filtered_count['People'],
    'distance_km': filtered_count['Total_distance(m)'] / 1000, 
    'total_items': filtered_count['TotItems'],
    'Submission Type': 'Count'})

    # --- 3. Process Lite Data ---
    # Load the dictionary for constants
    lite_dt = pd.read_csv(TFTin + 'other_averages_calc.csv', index_col=0).iloc[:, 0]
    lite_dict = lite_dt.to_dict()
    
    df_lite = pd.DataFrame({
    'Date': pd.to_datetime(filtered_lite['Created Date']).dt.strftime('%Y-%m-%d'),
    'Community Hub': filtered_lite['email_id'].map(hub_map).fillna(filtered_lite['Title']), # Lookup Name
    'no_people': lite_dict['People'], 
    'distance_km': lite_dict['Distance_km'], 
    'total_items': filtered_lite['TotItems'],
    'Submission Type': 'Lite'})

    
    # Combine all three
    results = pd.concat([df_survey, df_count, df_lite], ignore_index=True)

    # Ensure the final order matches your requirement
    results = results[['Date', 'Community Hub', 'no_people', 'distance_km', 
                       'total_items', 'Submission Type']]
    
    results.to_csv(TFTout + 'Community Hubs.csv')
    
    
def get_ATeam_data(TFTin, TFTout, rawin):
    """
    A function which extracts (as best possible) A-Team submissions
    from the different data streams. Based on presence of the surname, 
    or the contact email address being present in the data.
    
    It saves these filtered submissions to .csv and also extracts date, 
    name of A-Teamer, plus how many people, items and kms were on the submission 
    and saves this to another .csv

    Parameters
    ----------
    TFTin : string
             path to input folder with TFT data you want to search
            
    TFTout : string
           path for folder to save filtered .csvs in

    """ 
    
    email_ref_df = email_ref_df = pd.read_csv(rawin + 'email_reference.csv', encoding='cp1252')
    ch_email = email_ref_df.loc[email_ref_df['community'].isin(['AT', 'both']), 'email_id'].astype(str).tolist()

    ch_name = ['Wilson','Munro','Ward','Lush','Herbert','Lambie','Chisholm',
               'Barry','Schreiber','Davies','Lund','Laws','Hair','Kenelly',
               'Presi','Parker','Jarvis','Roberts','Johnson','Houlsby',
               'Lowther','Wood','Lean','Rainford','Mackeddie','Shwe',
               'Bellis','Harvey','Rosser','Adams','Hudson','Lee','Scullion',
               'Holdsworth','Piper','Cain','Bowden','Vackova','Cattell',
               'Heath','Ewart','Fabien','Whittaker','Harvey','Atkinson',
               'Finney']


    survey = pd.read_csv(TFTin + 'survey.csv')
    lite = pd.read_csv(TFTin + 'lite.csv')
    count = pd.read_csv(TFTin + 'count.csv')


    #survey - normalize cols
    survey['email_id'] = survey['email_id'].astype(str)
    survey['A-Team'] = survey['A-Team'].astype(str)
    email_col   = survey['email_id'].str.strip().str.lower().fillna('')
    surname_col = survey['Surname'].str.lower().fillna('')
    hub_col     = survey['A-Team'].str.lower().fillna('')

    #lite normalize cols
    lite_col = lite['Title'].str.strip().str.lower().fillna('')
    

    #normalize lists
    emails_lower   = [e.strip().lower() for e in ch_email]
    names_lower    = [n.lower() for n in ch_name]

    #build regex patterns for names/contacts
    name_pattern    = '|'.join(re.escape(n) for n in names_lower)


    #survey combine filters
    filtered_survey = survey[
        # email exact match
        email_col.isin(emails_lower)
        # OR name appears in email, hub, or trail
        | email_col.str.contains(name_pattern)
        | hub_col.str.contains('teamer')
        | surname_col.str.contains(name_pattern)
        ]

    #lite combine filters
    filtered_lite = lite[
        lite_col.str.contains(name_pattern)
        ]

    #count - normalize cols
    count['email_id'] = count['email_id'].astype(str)
    count['A-Team'] = count['A-Team'].astype(str)
    email_col   = count['email_id'].str.strip().str.lower().fillna('')
    surname_col = count['LastName'].str.lower().fillna('')
    hub_col     = count['A-Team'].str.lower().fillna('')

    
    #count combine filters
    filtered_count = count[
        # email exact match
        email_col.isin(emails_lower)
        # OR name appears in email, hub, or trail
        | email_col.str.contains(name_pattern)
        | hub_col.str.contains('teamer')
        | surname_col.str.contains(name_pattern)
        ]
    
    filtered_survey['email_id'] = pd.to_numeric(filtered_survey['email_id'], errors='coerce').astype('Int64')
    filtered_count['email_id'] = pd.to_numeric(filtered_count['email_id'], errors='coerce').astype('Int64')
    filtered_lite['email_id'] = pd.to_numeric(filtered_lite['email_id'], errors='coerce').astype('Int64')
    
    filtered_lite.to_csv(TFTout + 'AT_lite.csv', index=False)
    filtered_survey.to_csv(TFTout + 'AT_survey.csv', index=False)
    filtered_count.to_csv(TFTout + 'AT_count.csv', index=False)
    
    results = pd.DataFrame(columns = ['Date', 'A-Teamer', 'no_people',
                                      'distance_km', 'total_items',
                                      'Submission Type'])
    
    email_ref_df['email_id'] = email_ref_df['email_id'].astype(str)
    hub_map = email_ref_df.set_index('email_id')['name'].to_dict()
    filtered_survey['email_id'] = filtered_survey['email_id'].astype(str)
    filtered_count['email_id'] = filtered_count['email_id'].astype(str)
    filtered_lite['email_id'] = filtered_lite['email_id'].astype(str)

    # --- 1. Process Survey Data ---
    df_survey = pd.DataFrame({
    'Date': pd.to_datetime(filtered_survey['Date_TrailClean'], dayfirst=True).dt.strftime('%Y-%m-%d'),
    'A-Teamer': filtered_survey['email_id'].map(hub_map).fillna(filtered_survey['Surname']),
    'no_people': filtered_survey['People'],
    'distance_km': filtered_survey['Distance_km'],
    'total_items': filtered_survey['TotItems'],
    'Submission Type': 'Survey'})

    # --- 2. Process Count Data ---
    df_count = pd.DataFrame({
    'Date': pd.to_datetime(filtered_count['Date_Count'], dayfirst=True).dt.strftime('%Y-%m-%d'),
    'A-Teamer': filtered_count['email_id'].map(hub_map).fillna(filtered_count['LastName']),
    'no_people': filtered_count['People'],
    'distance_km': filtered_count['Total_distance(m)'] / 1000, 
    'total_items': filtered_count['TotItems'],
    'Submission Type': 'Count'})

    # --- 3. Process Lite Data ---
    # Load the dictionary for constants
    lite_dt = pd.read_csv(TFTin + 'other_averages_calc.csv', index_col=0).iloc[:, 0]
    lite_dict = lite_dt.to_dict()
    
    df_lite = pd.DataFrame({
    'Date': pd.to_datetime(filtered_lite['Created Date']).dt.strftime('%Y-%m-%d'),
    'A-Teamer': filtered_lite['email_id'].map(hub_map).fillna(filtered_lite['Title']), # Lookup Name
    'no_people': lite_dict['People'], 
    'distance_km': lite_dict['Distance_km'], 
    'total_items': filtered_lite['TotItems'],
    'Submission Type': 'Lite'})

    
    # Combine all three
    results = pd.concat([df_survey, df_count, df_lite], ignore_index=True)

    # Ensure the final order matches your requirement
    results = results[['Date', 'A-Teamer', 'no_people', 'distance_km', 
                       'total_items', 'Submission Type']]
    
    results.to_csv(TFTout + 'A-Team.csv', index=False)
    

def original_email_extraction():

    df3 = pd.read_csv('/Users/heatherkay/Downloads/TFTCommunityHubs_Contacts - Community Hubs.csv')

    email_ref_df = pd.read_csv('/Users/heatherkay/Downloads/email_reference2.csv')

    df3['Email'] = (df3['Email'].str.strip().str.lower())
    new_emails = df3[~df3['Email'].isin(email_ref_df['email'])]['Email'].dropna().unique()
    
    if len(new_emails) > 0:
        current_max_id = email_ref_df['email_id'].max()
    
        new_rows = pd.DataFrame({
            'email': new_emails,
            'email_id': range(current_max_id + 1, current_max_id + 1 + len(new_emails))
            })

        email_ref_df = pd.concat([email_ref_df, new_rows], ignore_index=True)


    import numpy as np


    email_ref_df['community'] = np.where(email_ref_df['email'].isin(df3['Email']), 'CH', '')
        
    email_ref_df.to_csv('/Users/heatherkay/Downloads/email_reference2.csv', index=False)
        

    #A-TEAM

    df3 = pd.read_csv('/Users/heatherkay/Downloads/at_email.csv')
    email_ref_df = pd.read_csv('/Users/heatherkay/Downloads/email_reference2.csv')

    df3['Email'] = (df3['Email'].str.strip().str.lower())
    new_emails = df3[~df3['Email'].isin(email_ref_df['email'])]['Email'].dropna().unique()
    
    if len(new_emails) > 0:
        current_max_id = email_ref_df['email_id'].max()
    
        new_rows = pd.DataFrame({
            'email': new_emails,
            'email_id': range(current_max_id + 1, current_max_id + 1 + len(new_emails))
            })

        email_ref_df = pd.concat([email_ref_df, new_rows], ignore_index=True)


    email_ref_df.loc[email_ref_df['email'].isin(df3['Email']), 'community'] = 'AT'
        
    email_ref_df.to_csv('/Users/heatherkay/Downloads/email_reference3.csv', index=False)


