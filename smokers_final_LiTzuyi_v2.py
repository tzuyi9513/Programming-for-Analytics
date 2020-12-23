#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 20:25:27 2020

@author: tzuyili
"""

import pandas as pd
import matplotlib.pyplot as plt

df =pd.read_csv("smokers.csv")

print("\nStep 1")
print("======")

print("# of Surveys: ",len(df))

print("\nStep 2")
print("======")
# Find distinct states
states_num = len(df['State'].unique())
print("# of states: ", states_num)
print("Average # of Surveys per State: ",len(df)/states_num)

print("\nStep 3")
print("======")
# Sort all values in the dataset without groupby from low to high
df_sort = df.sort_values('Value')

print("\nMinimum Recorded Cigarette Use:")
print(df_sort.T[0])

print("\nMaximum Recorded Cigarette Use:")
print(df_sort.T[len(df_sort)-1])

print("\nStep 4")
print("======")
# Calculate average Year and Value by states
df_st = df.groupby('State').mean()
# Sort the groupby state result by Value from high to low, and only show Value
df_st_sort = df_st.sort_values("Value", ascending = False)["Value"]

print("\nLeast Cigarette Use State:")
print(df_st_sort.index[-1],df_st_sort[-1])
print("\nMost Cigarette Use State:")
print(df_st_sort.index[0],df_st_sort[0])

print("\nStep 5")
print("======")
print("\nTop 10 Most Cigarette Use States:")
# In the screenshot there is average year, but it's not meaningful so I didn't include average year.

print(df_st_sort.head(10))

print("\nStep 6")
print("======")

st = input("State: ")
yr = int(input("Enter Year: "))
# Filter data by condition of state and year
df_filter = df[(df["Year"] == yr) & (df["State"] == st)]
print("Found ",len(df_filter)," Surveys.")
print(df_filter)

print("\nStep 7")
print("======")
# Use state and Year to groupby the data
df_gp = df.groupby(['State','Year']).mean()
# Use reset_index to make it a dataframe, and will use df_gp to further filter the state we need
df_gp = df_gp.reset_index()

input_state = ''
while input_state.lower().strip() != 'exit':
    input_state = input('State: ')
    if input_state in df['State'].unique():
        df_plot = df_gp[df_gp["State"] == input_state]
        plt.plot(df_plot['Year'], df_plot['Value'])
        plt.show()
        
        if df_plot['Value'].iloc[len(df_plot)-1] > df_plot['Value'].iloc[len(df_plot)-2]:
            print("Cigarette use is on rise in ", input_state)
        elif df_plot['Value'].iloc[len(df_plot)-1] < df_plot['Value'].iloc[len(df_plot)-2]:
            print("Cigarette use is on decline in ", input_state)
        else:
            print("Not enough years!")
        print("Compute for another state or enter 'Exit' to exit.")
    elif input_state.lower().strip() == 'exit':
        print("bye bye!")
    else:
        print("hmmm... cannot find that state.")
        print("Compute for another state or enter 'Exit' to exit.")
    print()
    