#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 13:14:39 2020

@author: tzuyili
"""
import pandas as pd
import matplotlib.pyplot as plt

print("\nStep 1: Reading file...")
df =pd.read_csv("nyc_parking_tickets.csv")
print(len(df), "records were read from file.")

print("\nStep 2: Cleaning up...")

df_clean = df[(df["Registration_State"] != '99') & (df["Plate_Type"] != '999') & (df["Vehicle_Make"] != "") & (df["Vehicle_Year"] != 0)  & (df["Vehicle_Year"] < 2018) & (df["Issuer_Code"] != 0)]
print(len(df_clean), "records left after cleanup...")


print("\nStep3: # of tickets by vehicle year...")
# Generate a new column 'Ticket'
df_clean.loc[df_clean.Vehicle_Year != None, 'Ticket'] = 1
df_year = df_clean.groupby('Vehicle_Year').count()['Ticket']

plt.plot(df_year)
plt.show

print("\nStep 4: Top 5 Vehicle-makes with most tickets...")
# Use 'Vehicle_Make' to groupby
df_vm = df_clean.groupby('Vehicle_Make').count()['Plate_ID']
df_vm_sort = df_vm.sort_values(ascending = False)
print(df_vm_sort.head())

print("\nStep 5: The street where commercial vehicles got the most ticket:")
df_com = df_clean[df_clean.Plate_Type == "COM"]
df_str = df_com.groupby('Street_Name').count()['Plate_ID']
df_str_sort = df_str.sort_values(ascending = False)
print(df_str_sort.head(1))

print("\nStep 6.1: The state with newest vehicles")
# Use 'Registration_State' to groupby and get the average 'Vehicle_Year'
df_st = df_clean.groupby('Registration_State').mean()['Vehicle_Year']
df_st_sort = df_st.sort_values(ascending = False)
print(df_st_sort.head(1))


print("\nStep 6.2: The state with oldest vehicles")
print(df_st_sort.tail(1))
