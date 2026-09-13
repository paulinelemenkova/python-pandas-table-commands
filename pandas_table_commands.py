#!/usr/bin/env python
# coding: utf-8
"""Pandas DataFrame Table Commands with Python

Author:  Polina Lemenkova
ORCID:   https://orcid.org/0000-0002-5759-1089
Archive: https://doi.org/10.13140/RG.2.2.20867.35366
License: MIT

See README.md for details.
"""
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import ListedColormap
# libraries
from mpl_toolkits.mplot3d import Axes3D

# In[201]:


os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Dataset
df = pd.read_csv("Tab-Bathy.csv")

X = df.iloc[0:516, 1:13]
X

B = df.loc[12]
B

data = pd.read_csv("Tab-Morph.csv")

strong = data['slope_class'] == 8
strong

profile_15 = data.loc[data['profile'] == 15, ['sedim_thick', 'slope_angle', 'igneous_volc']]
profile_15

# What is the maximal bathymetric depth ?
data['Min'].min()

# What is the maximal sediment thickness ?
data['sedim_thick'].max()

data['slope_angle'].max()

# How many data belong to each of the slope class?
data['slope_class'].value_counts()

# Summary displaying statistics for the selected variable: Mariana tectonic plate
data['sedim_thick'].describe()

# Splitting the data into different groups bya variable
data.groupby(['slope_class']).groups.keys()

# data.groupby('slope_class')['profile'].sum() # produces Pandas Series
data.groupby('slope_class', as_index=False)[['profile']].sum()  # produces Pandas DF

# print(df.head)
print(type(data))
# df
# data

data.shape
df.shape
data.ndim
df.ndim
data.head()
df.tail()
data.dtypes
df['profile13'].describe()

data.sedim_thick
data['sedim_thick']
data.loc[:, 'sedim_thick']
data.iloc[:, [1, 2, 3, 4]]
data.iloc[0:5, :]  # selecting 5 first rows

df['profile23'].plot(kind='hist', bins=100)
plt.xlabel('profiles')
plt.ylabel('depths')

myplot = data['Min']

myplot
myplot.sort_values().plot(kind='bar', color=sns.color_palette('Spectral'))
