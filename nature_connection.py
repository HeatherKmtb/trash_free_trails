#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 09:20:37 2026

@author: heatherkay
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/Users/heatherkay/Documents/TrashFreeTrails/Data/Data_per_year/survey/all_survey.csv')
df['NC'] = df[['Connection_ConnectionY', 'Connection_ConnectionN', 
               'Connection_ConnectionSame', 'Connection_Unsure']].bfill(axis=1).iloc[:, 0]
df = df.dropna(subset=['TotItems'])

sns.boxplot(x='NC', y='TotItems', data=df)
plt.xlabel('Nature Connection')
plt.ylabel('Number of items')
#plt.ylim(0, 1000) 
plt.title('Influence of total items on NC')
plt.show()


#optional extra
sns.stripplot(x='NC', y='TotItems', data=df, color='black', alpha=0.4)

#summary stats
df.groupby('NC')['TotItems'].describe()

#anova
from scipy.stats import f_oneway

groups = [g['TotItems'].values for _, g in df.groupby('NC')]
f_oneway(*groups)
#or non-parametric
from scipy.stats import kruskal
kruskal(*groups)




#feel about amount
ct = pd.crosstab(df['NC'], df['Connection_LitterFeel'])

sns.heatmap(ct, annot=True, fmt='d', cmap='Greens')
plt.xlabel('Connection_LitterFeel')
plt.ylabel('Nature Connection')
plt.title('How did you feel about the amount of litter you saw (4=disappointed)')
plt.show()

#more or less
mapping = {'More!': 4, 'About the same.': 2, 'Less :)': 0, 'About the same':2}

df['Connection_LitterAmount'] = (
    df['Connection_LitterAmount']
    .replace(mapping)
    .pipe(pd.to_numeric, errors='coerce')
    .astype('Int64'))

#df = df[~df['Connection_LitterAmount'].isin([3, 1])]

ct = pd.crosstab(df['NC'], df['Connection_LitterAmount'])

sns.heatmap(ct, annot=True, fmt='d', cmap='Greens')
plt.xlabel('Connection_LitterAmount')
plt.ylabel('Nature Connection')
plt.title('Did you find more or less SUP than expected (4=more)')
plt.show()

#after taking action
ct = pd.crosstab(df['NC'], df['Connection_Action'])

sns.heatmap(ct, annot=True, fmt='d', cmap='Greens')
plt.xlabel('Connection_Action (4=proud)')
plt.ylabel('Nature Connection')
plt.title('How did you feel after taking action')
plt.show()


#taking action v more or less
ct = pd.crosstab(df['Connection_Action'], df['Connection_LitterAmount'])

sns.heatmap(ct, annot=True, fmt='d', cmap='Greens')
plt.xlabel('Connection_LitterAmount (4=more)')
plt.ylabel('Connection_Action (4=proud)')
plt.title('Did you find more or less SUP than expected')
plt.show()

#taking action v feel about amount
ct = pd.crosstab(df['Connection_Action'], df['Connection_LitterFeel'])

sns.heatmap(ct, annot=True, fmt='d', cmap='Greens')
plt.xlabel('Connection_LitterFeel (4=disappointed)')
plt.ylabel('Connection_LitterAmount (4=more)')
plt.title('How did you feel about the amount of litter you saw (4=disappointed)')
plt.show()