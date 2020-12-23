#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 13:17:59 2020

@author: tzuyili
"""

# while True would make the sytem keep running
#I set anothoer variable "check_again" in the end of each choice, and it would break if the user don't want to continue.
while True:
    # use 4 variables to define the answers to 4 symptoms
    short_breath = input("Do you have shortness of breath (y/n)? ")
    cough = input("Do you cough (y/n)? ")
    sore_n_nose = input("Do you have sore throat/runny nose (y/n)? ")
    vomit = input("Do you have diarrhea, nausea and vomiting (y/n)? ")
    
    # Step 1 - 1:
    # If a user says no to all 4 questions, 
    # inform the user that there are no symptoms 
    # and hence they should wait to see if any symptom will develop.
    if short_breath == "n" and cough == "n" and sore_n_nose == "n" and vomit == "n":
        print("You should wait to see if you will develop any symptoms.")
        check_again = input("Would you like to check again (y/n)? ")
        if check_again == "y":
            continue
        else:
            print("Good bye!")
            break
    # Step 1 - 2:
    # If a user says yes to shortness of breath and coughing, 
    # and no to sore-throat and nausea, 
    # then we need to check fever (see Step 2).
    elif short_breath == "y" and cough == "y" and sore_n_nose == "n" and vomit == "n":
        print("You may have COVID-19, let's continue...")
        # Step 2:
        # we ask the user to enter the most recent 5 temperature readings
        print("Enter 5 most recent temperature readings: ")
        temp = []
        temp1 = int(input("Temp 1: "))
        temp2 = int(input("Temp 2: "))
        temp3 = int(input("Temp 3: "))
        temp4 = int(input("Temp 4: "))
        temp5 = int(input("Temp 5: "))
        # zero values should be ignored and not taken into account for average calculation
        # I use "if" to solve the problem.
        # if user enters 0, the value would not be added to the list.
        if temp1 != 0:
            temp.append(temp1)
        if temp2 != 0:
            temp.append(temp2)
        if temp3 != 0:
            temp.append(temp3)
        if temp4 != 0:
            temp.append(temp4)
        if temp5 != 0:
            temp.append(temp5)
        # I create a new list to store the sorted values in the original list.
        sort_temp = sorted(temp)
        # print(sort_temp)
        Max_temp = sort_temp[len(temp) - 1]
        # (temp1 + temp2 + temp3 + temp4 + temp5) queals to the sum function
        # I use len(temp) to see how many numbers in the list.
        # In the list, I have excluded the value of 0.
        avg_temp = (temp1 + temp2 + temp3 + temp4 + temp5) / len(temp)
        print("Your max. temp. was ", Max_temp, ".")
        print("Your avg. temp. was ", avg_temp, ".")
        if Max_temp  >= 104 and avg_temp >= 100:
            print("Please seek medical attention now!")
        elif avg_temp >= 99:
            print("You should monitor your condition and check back with the app.")
        else:
            print("You likely have the cold or influenza virus.")
        check_again = input("Would you like to check again (y/n)? ")
        if check_again == "y":
            continue
        else:
            print("Good bye!")
            break
    else:
        print("You likely have the influenza virus.")
        check_again = input("Would you like to check again (y/n)? ")
        if check_again == "y":
            continue
        else:
            print("Good bye!")
            break
    
