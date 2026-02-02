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
plt.ylim(0, 1000) 
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