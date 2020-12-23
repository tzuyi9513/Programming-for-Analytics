#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 19:06:47 2020

@author: tzuyili
"""


import matplotlib.pyplot as plt


# Read csv
airport_records = []
f = open("airline_delays.csv")
content = f.read()

f.close()

# split rows with \n
rows = content.split("\n")

for i in range(len(rows)):
    if i > 0 and rows[i] != "":  # skip header
        values = rows[i].split(",")

        if values[0] != "" and values[2] != "" and values[4] != "":
            airport_records.append([values[0],float(values[2]),float(values[4])])

#Step 1  Calculate the performance of a specific airport
print("Step 1")

# Create a dictionary: key is "airport", values are "delay", "distance"
airport_dict = {}

for record in airport_records:
    airport = record[0]
    delay = record[1]
    distance = record[2]
    
    if airport not in airport_dict:
    	airport_dict[airport] = { 'delays': [], 'distances': [], 'num_of_delay': 0, 'num_of_on_time': 0}

    airport_dict[airport]['delays'].append(delay)
    airport_dict[airport]['distances'].append(distance)

    if delay > 0:
        airport_dict[airport]['num_of_delay'] += 1
    else:
        airport_dict[airport]['num_of_on_time'] += 1

#print(airport_dict)
for airport in airport_dict:
    num_of_on_time = airport_dict[airport]['num_of_on_time']
    num_of_delay = airport_dict[airport]['num_of_delay']
    airport_dict[airport]['performance'] = num_of_on_time / (num_of_delay + num_of_on_time)

# # Get the target airport from user's input
target_airport = input('Origin Airport: ')

num_of_on_time = airport_dict[target_airport]['num_of_on_time']
num_of_delay = airport_dict[target_airport]['num_of_delay']
performance = airport_dict[target_airport]['performance']
print("Flight from ", target_airport, "was on time ", num_of_on_time, " times.")
print("Flight from ", target_airport, "was delayed ", num_of_delay, " times.")
print("The performance of airport_records from ", target_airport, " is ", performance, ".")


# # Step 2
print()
print("Step 2")
# # Count the performance of each airport
best_performance = 0
worst_performance = float('inf')

for airport in airport_dict:
    performance = airport_dict[airport]['performance']

    print("The performance of airport_records from ", airport, " is ", performance, ".")

    # find the best airport with best performance
    if performance > best_performance:
      best_performance = performance
      best_airport = airport

    # find the worst airport with worst performance
    if performance < worst_performance:
      worst_performance = performance
      worst_airport = airport

print('Best airport is ' + best_airport + ' with perf ' + str(best_performance) + '.')
print('Worst airport is ' + worst_airport + ' with perf ' + str(worst_performance) + '.')


# Step 3: Put distance into 6 groups, calculate the on-time rate in each group, and draw a line chart
# Create a dicytionary: key is distance; value is delay

print(" ")
print("Step 3")
distance_dict = {}

for airport in airport_dict:

  distances = airport_dict[airport]['distances']
  delays = airport_dict[airport]['delays']

  for i in range(len(distances)):
    distance = distances[i]
    delay = delays[i]

    normalized_distance = (distance + 1) // 400

    if normalized_distance not in distance_dict:
    	distance_dict[normalized_distance] = []

    distance_dict[normalized_distance].append(delay)
# print(distance_dict)
# calculate the on-time
# x = [0, 1, 2, 3, 4, 5, 6]
# y = [0.12, 0.23, 0.34, 0.45, 0.56, 0.67. 0.78]

x_values = sorted(distance_dict.keys())
y_values = []

for x_value in x_values:
    num_of_on_time = distance_dict[x_value].count(0)
    total_num_of_flight = len(distance_dict[x_value])
    performance = num_of_on_time / total_num_of_flight
    y_values.append(performance)

# draw the plot
#
plt.plot(x_values, y_values)
plt.title('distance and on-time correlation')
plt.xlabel('distance group')
plt.ylabel('on-time percentage')
plt.show(block=False)
plt.pause(10)
plt.close()
