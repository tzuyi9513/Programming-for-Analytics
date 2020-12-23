#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 12:30:09 2020

@author: tzuyili
"""

# Step 0:
# Define CLass
# Create a class representing a County containing the properties 
class County:
    name = ""
    state = ""
    commute = 0
    home = 0 
    income = 0
    population = 0
    education = 0
    happy = 0

import csv
f = open("county_facts.csv")
rows = csv.reader(f)

# add what we need in a list
data = []
next(rows)

for cols in rows:
    if cols[2] != "" : 
        c = County()
        c.name = cols[1]
        c.state = cols[2]
        c.commute = float(cols[25])
        c.home =float(cols[27])
        c.income = float(cols[33])
        c.population = float(cols[6])
        c.education = float(cols[23])
        c.happy = (c.home * c.income)/c.commute
        data.append(c)


# Step 1: Display the least and most populous counties.
print("Q1: Counties with least and most population")
print("===========================================")
largest_pop  = max(data, key=lambda x: x.population)
least_pop = min(data, key=lambda x: x.population)
print(least_pop.name,"(", least_pop.state,"):", least_pop.population)
print(largest_pop.name,"(", largest_pop.state,"):", largest_pop.population)


# Step 2: Display the states with least and most population.
print("\nQ2: States with least and most population")
print("===========================================")

# create a dictionary to store states(key) and total population(value)
st_pop_dic = {}
for d in data:
    if d.state in st_pop_dic:
        # when the state has been in the dictionary, add the populaiton to original population
        # after each loop, the population in the dictionary will be a running total
        st_pop_dic[d.state] = st_pop_dic[d.state] + d.population
    else:
        # when the state not in dictinary, 
        # add state in the dictionary, and append the population of its first record.
        st_pop_dic[d.state] = d.population

min_pop = float('inf')
max_pop = 0
min_state = ""
max_state = ""

for key, value in st_pop_dic.items():
    if float(value) > max_pop:
        max_state = key
        max_pop = value
    if float(value) < min_pop:
        min_state = key
        min_pop = value

print(min_state, ":", min_pop)
print(max_state, ":", max_pop)

# Step 3: if there is a correlation between happiness and the rate of higher education in counties.
print("\nQ3: Happiness vs Higher Education Rate")
print("===========================================")

# define a function to calculate average value
def avg(lst):
    ret = sum(lst) / len(lst)
    return ret 

# Go beack to class to define happiness
# extract happiness
happiness = list(map(lambda x: x.happy, data))
avg_happy = avg(happiness)

# segment 2 groups by below/over average happiness
groups = [{"start":0, "end":avg_happy}, {"start":avg_happy, "end":float('inf')}]

# Based on the 2 groups, I add the education into the 2 groups
# and then calculated the average education in each groups
happy_edu = []
for grp in groups:
    withinRange = filter(lambda x: grp["start"] <= x.happy <= grp["end"], data)
    edu = list(map(lambda x: x.education, withinRange))    
    happy_edu.append(avg(edu))

print("Happy Counties College Edu Rate  : ", happy_edu[1], "%")
print("Unhappy Counties College Edu Rate: ", happy_edu[0], "%")
Diff = happy_edu[1]-happy_edu[0]
print("Difference is ", Diff, "%")

if Diff > 20:
    print("Happy counties have significantly more college graduates.")
elif (-Diff) >20:
    print("Happy counties have significantly less college graduates.")
elif Diff > 5:
    print("Happy counties have slightly more college graduates.")
elif (-Diff) < 5:
    print("Happy counties have slightly less college graduates.")
else:
    print("Could not find any significant correlation.")
    

# Step 4: Find and report all counties that are similar.
print("\nQ4: Similar Counties (2%)")
print("===========================================")
# Define a function to see if absolute value of difference is within 2%
def sim(x, y):
    return abs(x / y - 1) < 0.02

result = set()
for c in data:
    # Let county + state become a whole identity
    # The whole identity cannot compare its own. Only compare with other county+state.
    selfrem = filter(lambda x: (x.name + x.state) != (c.name + c.state), data)
    # find those that are similar in terms of population, education, commute, home, income
    similar = filter(lambda x: sim(x.population, c.population) and sim(x.education, c.education)
                     and sim(x.commute, c.commute) and sim(x.home, c.home) and sim(x.income, c.income),                
                     selfrem)
    # transform similar counties to [names]
    names = list(map(lambda x: x.name + " (" + x.state + ")", similar))
    # let county_name has the same format as names list, so we can compare whether it's the same
    county_name = c.name + " (" + c.state + ")"


    # when the names list is not blank (when there is at least one similar county)
    if len(names) > 0: 
        # put county_name we has found into the result set
        result.add(county_name)
        for n in names:
            if n not in result:
                # put n in names list to result set
                # by doing so, the order of similarity is not important
                # a & b are similar = b & a are similar
                result.add(n)
                print(county_name, "and ", n, " are similar.")
        


# Step 5: Create a graph displaying correlation between population and income.
print("\nQ5: Population vs Income Rate")
print("===========================================")

# divide the range into 3 so we can see the distance of each group
rg = (largest_pop.population - least_pop.population) / 3
groups_q5 = [{"start":least_pop.population, "end":least_pop.population + rg}, {"start":least_pop.population + rg, "end":least_pop.population + 2 * rg}, {"start":least_pop.population + 2 * rg, "end":largest_pop.population}]

income_pop = []
for grp5 in groups_q5:
    withinRange5 = filter(lambda x: grp5["start"] <= x.population <= grp5["end"], data)
    inc = list(map(lambda x: x.income, withinRange5))    
    income_pop.append(avg(inc))

import matplotlib.pyplot as plt


r1 = least_pop.population
r2 = least_pop.population + rg
r3 = least_pop.population + 2 *rg
r4 = largest_pop.population

# set the name of x range
r1_r2 = '{}~{}'.format(r1, r2)
r2_r3 = '{}~{}'.format(r2, r3)
r3_r4 = '{}~{}'.format(r3, r4)

x_range = [r1_r2, r2_r3, r3_r4]

plt.plot(x_range, income_pop, color = 'blue')
# let the beginning and ending in the left and right
plt.xlim(left = 0, right = 2)
# set the beginning and ending numbers in y axis
plt.ylim([44000, 56000])

plt.show()
