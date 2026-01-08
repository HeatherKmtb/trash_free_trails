#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 12:42:27 2026

@author: heatherkay
"""

import pandas as pd    
    
ateam = ['alistair hair', 'andy lund', 'chloe parker', 'dan jarvis', 
             'dom barry', 'ed roberts', 'emma johnson', 'gill houlsby', 
             'hannah lowther', 'hari milburn', 'harry wood', 'ian white', 
             'ian lean', 'jake rainford', 'james mackeddie', 'jane chisholm', 
             'jay schreiber', 'jo shwe', 'john bellis', 'kyle harvey', 
             'lauren munro-bennet', 'leon rosser', 'mario presi', 'mark wilson', 
             'marv davies', 'matt kennelly', 'monet adams', 'neil hudson', 
             'nush lee', 'pete scullion', 'ram gurung', 'rosie holdsworth', 
             'ross lambie', 'sam piper', 'tom laws', 'will atkinson', 
             'victoria herbert', 'ollie cain', 'laurance ward', 'tim bowden', 
             'kristina vackova', 'helen wilson', 'lauren cattell']
    
    
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

ch_email = ['info@thebikingexplorers.co.uk', 'info@cycleisletrax.co.uk', 
            'info@cycleworksyorkshire.co.uk', 'sara.radford@gmail.com', 
            'hello@drosibikes.org', 'enquiries@ponnekrunning.co.uk', 
            'dyfiadventurecampsite@gmail.com', 'joe@energisecycles.co.uk', 
            'bangor@evolution-bikes.co.uk', 'stuart@grvl.cc', 
            'noodfoodzerowaste@gmail.com', 'sally.outsidelives@gmail.com', 
            'bobby.mcnicol@rapha.cc', 'scoopandscales@gmail.com', 
            'ailsa@thegreenhousesuffolk.co.uk', 'ciara@thesportsroom.ie', 
            'zhelliot-jones1@sheffield.ac.uk', 'siop@ytygwyrdd.cymru',
            'prb007peterbowen@aim.com', 'info@pobladocoffi.co.uk', 'matt@runcomm.co.uk', 
            'kate@aban.scot', 'jane@adaptiveriderscollective.org.uk', 
            'clairecopeman@adventuretoursuk.com', 'alythcycles@gmail.com', 
            'barrysidingscafe@gmail.com', 'enquiries@beartrax.co.uk', 
            'Biketek100@gmail.com', 'joanne.ellis@wildelements.org.uk', 
            'foh@caban-cyf.org', 'Nia.Davies@cyfoethnaturiolcymru.gov.uk', 
            'william@comriecroft.com', 'craig@cyclewise.co.uk', 
            'ben.herbert@forestryengland.uk', 'stu@dalesbikecentre.co.uk', 
            'rob.hulme@hotmail.co.uk', 'scott.welland@nationaltrust.org.uk', 
            't.halliday@haeckels.co.uk', 'helensburghcycles@yahoo.co.uk', 
            'marketingteam@hfholidays.co.uk', 'oliver.rogers@forestryengland.uk',
            'hazel.lyon@yahoo.co.uk', 'elaine.russell@johnlewis.co.uk', 
            'elaine.russell@johnlewis.co.uk', 'monica@kickbackcoffee.co.uk', 
            'lightno@hotmail.com', 'Anthony@mountainviewbikepark.co.uk', 
            'mtbtrailguides@outlook.com', 'solene@onebiketz.com', 
            'matthew@oneplanetadventure.com', 'lee@otec.bike', 
            'tyler@theoutrunners.co.uk', 'store.bristol@patagonia.com', 
            'jonmclements@gmail.com', 'info@pedalprogression.com', 
            'liz.beverley@pyb.co.uk', 'info@rateofrisecoffee.co.uk', 
            'cumuluskiteboarding@hotmail.com', 'jen@ridebikes.co.uk', 
            'skirrto@btinternet.com', 'janephillips5882@googlemail.com', 
            'keith.wraight@roundhousebirmingham.org.uk', 'jonmclements@gmail.com', 
            'ridekirklees@hotmail.com', 'stompinggroundcoffee@outlook.com', 
            'tarlandtrails@gmail.com', 'hello@thebikescollege.org', 
            'chagfordbikefixer@yahoo.co.uk', 'thelodgestaylittle@gmail.com', 
            'info@oystercatcheranglesey.co.uk', 'contact@thesurfcafe.co.uk', 
            'robbie@thewoodscyclery.co.uk', 'sales@thetrailhead.co.uk', 
            'swansea@tredz.co.uk', 'bath@trekbikes.com', 'german_tortarolo@trekbikes.com', 
            'paul_hitchcock@trekbikes.com', 'manchester@trekbikes.com', 
            'jonathan_stone@trekbikes.com', 'nathaniel_harrop@trekbikes.com', 
            'conor_j_bailey@trekbikes.com', 'connor_flood@trekbikes.com', 
            'tyredncranky@gmail.com', 'velosurmer@gmail.com', 'phil@venturefield.com', 
            'info@wadebridgebikeshop.co.uk', 'Kevin.Mannion@youngglos.org.uk', 
            'rikkibarrattmtb@gmail.com', 'robtrashfreetrails@gmail.com', 
            'bikechallengechannel@gmail.com', 'matt@wondercross.com.au', 
            'domingocozzani@gmail.com', 'hello@bikehikeandpaddle.co.uk', 
            'ncamedia9@gmail.com', 'gill.erskine@wildstrong.co', 'Pete@cyclistsfc.org.uk', 
            'contact@trailskills.co.uk', 'hello@unboundco.com', 'ben@misspentsummers.com', 
            'tom@tomhutton.net', 'info@mtb23.com', 'info@ochilbiketech.com', 
            'howardswanwick@googlemail.com', 'info@finalborgoofficinerunning.com', 
            'ljgriffiths@yahoo.com', 'hannah@opentrail.co.uk', 'gareth@hadfer.com', 
            'tom.elsworth@hotmail.co.uk', 'Anna.Harrison1@nationaltrust.org.uk', 
            'robertbobbyglover@gmail.com', 'ruth@onarecce.com', 'nbc@merciacycles.com', 
            'nicolas.bulois@gmail.com', 'workshop@bikegarage.co.uk', 
            'jonathon.lee@denbighshire.gov.uk', 'adventure@femaleexplorers.co.uk']

ch_name = ['Biosphere', 'Coffi', 'TraX', 'Yorkshire', 'Dean','Drosi',
           'Dusty','Dyfi','Energise','Evolution','GRVL','Nood',
           'Outside','Rapha','Scoop','Stif','Swinley','Green',
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


survey = pd.read_csv('/Users/heatherkay/Documents/TrashFreeTrails/Data/Data_per_year/survey/all_survey.csv')
lite = pd.read_csv('/Users/heatherkay/Documents/TrashFreeTrails/Data/Data_per_year/lite/all_lite.csv')

import re

# --- normalize columns ---
email_col   = survey['Email'].str.strip().str.lower().fillna('')
surname_col = survey['Surname'].str.lower().fillna('')
hub_col     = survey['Community Hub'].str.lower().fillna('')
trail_col   = survey['TrailName'].str.lower().fillna('')

# --- normalize lists ---
emails_lower   = [e.strip().lower() for e in ch_email]
names_lower    = [n.lower() for n in ch_name]
contacts_lower = [c.lower() for c in ch_contact]

# --- build regex patterns for names/contacts ---
name_pattern    = '|'.join(re.escape(n) for n in names_lower)
contact_pattern = '|'.join(re.escape(c) for c in contacts_lower)

# --- combine filters ---
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

# --- normalize columns ---
lite_col = lite['Title'].str.strip().str.lower().fillna('')

filtered_lite = lite[
    lite_col.str.contains(name_pattern)
    | lite_col.str.contains(contact_pattern)
    ]