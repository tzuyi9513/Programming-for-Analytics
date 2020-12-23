#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 23:12:16 2020

@author: tzuyili
"""

import pandas as pd
import numpy as np

print("\nStep 0")
print("========================")
df =pd.read_csv("athlete_events.csv")
print("There are",len(df), "records in the data-set.")


print("\nStep 1")
print("========================")
# Clean the data by filling na with 'None'
df['Medal'].fillna('None', inplace=True)
print("There are",len(df[df['Medal'] != 'None']), "records in the data-set with medals.")

print("\nStep 2")
print("========================")
# calculate average
gf = df.groupby("Sport").mean()

print("\nTallest:")
for i in range(3):
    print(gf.sort_values("Height", ascending = False)["Height"].index[i],gf.sort_values("Height", ascending = False)["Height"][i])

print("\nShortest:")
for i in range(3):
    print(gf.sort_values("Height", ascending = True)["Height"].index[i],gf.sort_values("Height", ascending = True)["Height"][i])

print("\nHeaviest:")
for i in range(3):
    print(gf.sort_values("Weight", ascending = False)["Weight"].index[i],gf.sort_values("Weight", ascending = False)["Weight"][i])

print("\nLightest:")
for i in range(3):
    print(gf.sort_values("Weight", ascending = True)["Weight"].index[i], gf.sort_values("Weight", ascending = True)["Weight"][i])


print("\nStep 3")
print("========================")

# filter Winter data only
df_winter = df[df["Season"] == "Winter"]
# generate a new column called "Winter_Gold". 
# If season was winter and medal was gold, the column would be 1, and else should be 0.

df_winter.loc[(df['Medal'] == 'Gold'), 'Winter_Gold'] = 1  
df_winter.loc[(df['Medal'] != 'Gold'), 'Winter_Gold'] = 0

# Calculate the gold medal numbers using sum of the 'Winter_Gold'
df_wg = df_winter.groupby(["Year","Team"]).sum()

# Sort the dataframe
df_wg_sort = df_wg.sort_values('Winter_Gold', ascending = False).groupby(level = 0).head(1)
# Get index of the groupby & sort result

Max_Team = df_wg_sort.sort_values('Year').index
for index in Max_Team:
    print(index[0],index[1])

print("\nStep 4")
print("========================")

# generate a new column called 'Medal_number'
# if Medal not None, then 1; else should be 0
df.loc[(df['Medal'] != 'None'),'Medal_number'] = 1
df.loc[(df['Medal'] == 'None'),'Medal_number'] = 0

# sum up 'Medal_number'
df_sport = df3 = df.groupby(['Sport','Team']).sum()

# rank the result from high to low
df_sport_sort = df_sport.sort_values(["Medal_number"], ascending = False).groupby(level = 0).head(1)
Max_Team_Sport = df_sport_sort.sort_values('Sport')

for i in range(len(Max_Team_Sport['Medal_number'])):
    print(Max_Team_Sport['Medal_number'].index.to_flat_index()[i][0], ":",Max_Team_Sport['Medal_number'].index.to_flat_index()[i][1], " with ", Max_Team_Sport['Medal_number'][i], 'medals.')

print("\nStep 5")
print("========================")

# generate a new column called 'Female'
# If it's female, then 1; else should be 0
df['Female'] = df.Sex.apply(lambda x: 1 if 'F' in x else 0)
# generate a new column called 'all'
# If it's female or male, then 1; else should be 0
df['all'] = df.Sex.apply(lambda x: 1 if 'F' or 'M' in x else 0)

# Groupby Year
dfall = df.groupby("Year").sum()
# Generate a new column by diving Female & all
dfall['FemaleRate'] =  dfall['Female']/dfall['all']

import matplotlib.pyplot as plt
plt.plot(dfall.index, dfall['FemaleRate'])
plt.show()

print("\nStep 6")
print("========================")
# Group by Year and calculate the average age
dfage = df.groupby("Year").mean()["Age"]
print(dfage)
import matplotlib.pyplot as plt

plt.plot(dfage)
plt.show()

print("\nStep 7")
print("========================")
# want only data in 2016
df_2016 = df[df["Year"] == 2016]
df_compete = df_2016.groupby('Sport').agg({'Medal_number':np.sum, 'all': np.size})
# generate a new column ratio by comparing the medal number and participants
df_compete['ratio'] = df_compete['Medal_number'] / df_compete['all']

df_compete_sort = df_compete.sort_values('ratio',ascending= False)

print("We recommend:")
for i in range(3):
    print(df_compete_sort.index[i])
