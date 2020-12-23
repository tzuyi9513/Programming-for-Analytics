#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 13:27:03 2020

@author: tzuyili
"""

# Read csv

f = open("medicaid.csv")
content = f.read()

f.close()

rows = content.split("\n")


# Step 1
# Create a list to store XXXX and 0
emp_or_xxxx = []
# Create a list to store values other than XXXX and 0
med_records_no_emp = []

for i in range(len(rows)):
    values = rows[i].split(",")
    if values[0] == "0" or values[0] == "XXXX":
        emp_or_xxxx.append([values[0]])


for i in range(len(rows)):
    values = rows[i].split(",")
    if values[0] != "0" and values[0] != "XXXX":
        med_records_no_emp.append(float(values[0]))

print("Step 1")        
# Calculate how many records in these lists
print("Read ",len(med_records_no_emp), "records.")
print("Skipped ", len(emp_or_xxxx), "records.")



# Step 2
print("Step 2")
# Create a new list to store the sorted value (High to Low)
sorted_medrec_HtoL = sorted(med_records_no_emp,reverse=True)

# max will be the first record in the sorted list (H to L)
max_rec = sorted_medrec_HtoL[0]
# min will be the last record in the sorted list (L to H), and the location will be len - 1
min_rec = sorted_medrec_HtoL[len(sorted_medrec_HtoL)-1]
print("Min. Expense is ", min_rec, ".")
print("Max. Expense is", max_rec, ".")


# Step 3
print("Step 3")
# Create a new list to store data larger than 100K and not equal to 0 or XXXX
larger_hundk = []
for i in range(len(rows)):
    values = rows[i].split(",")
    if values[0] != "0" and values[0] != "XXXX" and float(values[0]) > 100000:
        larger_hundk.append(float(values[0]))
#print(larger_hundk)

# calulate the sum in larger_hundk using for loop
ttl = 0
for item in larger_hundk:
    ttl += item
# average = sum / how many records
avg_if_larger = ttl / len(larger_hundk)
print("Average is ", avg_if_larger)

# Step 4
print("Step 4")
# For users to input upper and lower bound
Lower = int(input("Lower: "))
Upper = int(input("Upper: "))
# Count how many records within the range
ct = 0
for v in med_records_no_emp:
    
    if v >= Lower and v <= Upper:
        ct += 1
print("There are ", ct, "records.")

# Step 5
print("Step 5")     

for i in range(10):
    print(i+1, "-", sorted_medrec_HtoL[i])

# Step 6    
print("Step 6")
# if len is even: avg(r1, r2); if len is odd: median is in the middle
if len(sorted_medrec_HtoL) % 2 == 0:
    r1 = sorted_medrec_HtoL[len(sorted_medrec_HtoL)/2 - 1]
    r2 = sorted_medrec_HtoL[len(sorted_medrec_HtoL)/2]
    median_rec = (r1 + r2) / 2
else:
    median_rec = sorted_medrec_HtoL[int(len(sorted_medrec_HtoL)/2)]
print(median_rec)
