#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 14:43:26 2020

@author: tzuyili
"""
# Define class
class smoke:
    def __init__(self, year, state, value):
        self.year = year
        self.state = state
        self.value = value

# import csv file
import csv
f = open("smokers.csv")
rows = csv.reader(f)
next(rows)

data = []
for row in rows:
    s = smoke(int(row[0]),row[1], float(row[2]))
    data.append(s)

#Step 1:​ Read file and display the number of rows in the data.
print("\nStep 1")
print("======")
#Count number of surveys
records = len(list(map(lambda x: x, data)))
print("# of Surveys: ",records)

# Step 2:​ Find and display the average number of surveys conducted per state.
print("\nStep 2")
print("======")

states = list(set(map(lambda x: x.state, data)))
# Find Number of states
print("# of States: ", len(states))
# use number of records / number of states
print("Average # of Surveys per State: ", records/len(states))

# Step 3:​ Among the surveys in the data-set, display the minimum and maximum smoking rate.
print("\nStep 3")
print("======")

min_value = min(data, key = lambda x: x.value)
print("Minimum:")
print(min_value.year, min_value.state, min_value.value)

max_value = max(data, key = lambda x: x.value)
print("Maximum:")
print(max_value.year, max_value.state, max_value.value)


print("\nStep 4")
print("======")

def average(lst):
    return sum(lst)/len(lst)

avg_dic = {}
for state in states:
    st = filter(lambda x: x.state == state, data)
    values = list(map(lambda x: x.value, st))
    avg = average(values)
    if state not in avg_dic:
        avg_dic[state] = {}
    avg_dic[state] = avg

# sort the average value from high to low
sort_avg_dic = sorted(avg_dic.items(),key=lambda item:item[1],reverse=True)

print("Min:", sort_avg_dic[len(sort_avg_dic)-1][0], sort_avg_dic[len(sort_avg_dic)-1][1])
print("Max:", sort_avg_dic[0][0], sort_avg_dic[0][1])

# Step 5:​ Same as Step 4 but display the top 10 states instead of min and max.
print("\nStep 5")
print("======")
# Get top 10 records from the previous sorted dictionary
for i in range(10):
    print(sort_avg_dic[i][0], sort_avg_dic[i][1])

# Step 6: ​Get state and year from user and display the surveys for that state for that year.
print("\nStep 6")
print("======")

state_year_v = {}
state_years = list(set(map(lambda x: str(x.year) + " " + x.state, data)))
for sy in state_years:
    styr = filter(lambda x: str(x.year) + " " + x.state == sy, data)
    yr = list(map(lambda x: x.year, styr))
    styr = filter(lambda x: str(x.year) + " " + x.state == sy, data)
    values = list(map(lambda x: x.value, styr))
    state_name = sy.split()[1]
    if state_name not in state_year_v:
        state_year_v[state_name] = {}
    state_year_v[state_name][yr[0]] = values


# User inputs State and Year
find_state = str(input("State: "))
find_year = int(input("Year: "))

print("\nFound ",len(state_year_v[find_state][find_year]), " Surveys")

for i in range(len(state_year_v[find_state][find_year])):
    print(find_year,  find_state, state_year_v[find_state][find_year][i])

# Step 7 
# (1)Get state from user as input (using input()) and display the average smoker rate year by year. 
# (2)By looking at the most recent 2 years, display if the cigarette use is on decline or rise.
print("\nStep 7")
print("======")

input_state = ''
while input_state.lower().strip() != 'exit':
    input_state = input('State: ')
    if input_state in states:

        x = []
        y = []
        for year, values in sorted(state_year_v[input_state].items(),key=lambda item:item[0],reverse=False):
            x.append(year)
            y.append(average(values))

        import matplotlib.pyplot as plt
        plt.plot(x, y)
        plt.show()
        
        #Compare the most recent 2 years, and display if the cigarette use is on decline or rise.
        
        if y[-1] > y[-2]:
            print("Cigarette use is on rise in ", input_state)
        elif y[-1] < y[-2]:
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
