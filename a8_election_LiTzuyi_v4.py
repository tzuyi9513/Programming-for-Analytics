#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 14:32:20 2020

@author: tzuyili
"""

# Define CLass

class Contribution:
    candidate = ""
    Fname = ""
    Lname = ""
    sex = ""
    age = 0
    donation = 0

import csv
f = open("contributions.csv")
rows = csv.reader(f)

# add what we need in a list
data = []
next(rows)

for cols in rows:
    if cols[0] != "" : 
        c = Contribution()
        c.candidate = cols[0]
        c.Fname = cols[1]
        c.Lname = cols [2]
        if cols[3] == "male" or cols[3] == "female":
            c.sex = str.capitalize(cols[3])
        else:
            c.sex = "Female"
        c.age = float(cols[4])
        c.donation = float(cols[5])
        data.append(c)

f.close()
        
def average(lst):
    lst = list(lst)
    return sum(lst) / len(lst)

# Step 0: Write a function that will take a list of donation objects as input argument and 
# print out 
# 1. the number of donations in the list, 
# 2. the total amount of those donations and 
# 3. the average donation amount.
def ct_ttl_avg(lst):
    count = len(lst)
    total = sum(lst)
    avg = average(lst)
    return print("   There are ", count, " donations. \n   Total amount is $",total,". \n   Average contribution was $", avg, ".")

# Step 1: how many candidates are running
print("\nStep 1")
candidate_set = list(set(map(lambda x: x.candidate, data)))

print("In this election, ", len(candidate_set), " candidates are running:")
for i in range(len(candidate_set)):
    print("   Candidate", i+1, ": ", candidate_set[i])

# Step 2: report # of contributions, total amount of contributions and average contribution
print("\nStep 2")
for c in candidate_set:
    cand = filter(lambda x: x.candidate == c, data)
    don = list(map(lambda x: x.donation, cand))
    print("For Candidate ", c, ":")
    ct_ttl_avg(don)

# Step 3: Check if there are donors younger than the age of 21 
print("\nStep 3")

for d in data:
    underage = filter(lambda x: x.age < 21, data)
    amt = list(map(lambda x: x.donation, underage))

print("Donation from underage doners: ")
ct_ttl_avg(amt)

# Step 4: No individual can contribute more than $1600 in an election.
print("\nStep 4")
donors = set(map(lambda x: x.Fname +" "+  x.Lname, data))

print("Following donors exceeded amount limit per election:")

for donor in donors:
    donor_names = filter(lambda x: (x.Fname +" "+ x.Lname) == donor, data)
    amounts = list(map(lambda x: x.donation, donor_names))
    if sum(amounts) > 1600:
        print("   ", donor, "contributed $", sum(amounts), ".")
        
# Step 5: For each candidate report the donation count, total amount and average per gender.
print("\nStep 5")

candidates_gender = set(map(lambda x: x.sex + "s for candidate " + x.candidate, data))
for c in candidates_gender:
    cand = filter(lambda x: x.sex + "s for candidate " + x.candidate == c, data)
    don = list(map(lambda x: x.donation, cand))
    print(c,":")
    ct_ttl_avg(don)