#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 13:43:25 2021

@author: omertugrul
"""

first_suit = float(input("Enter the cost of the first suit: "))

second_suit = float(input("Enter the cost of the second suit: "))

if first_suit > second_suit:
    lower = second_suit
    higher = first_suit
else:
    lower = first_suit
    higher = second_suit
    
new_lower = lower/2

total = new_lower + higher

if total > 1000:
    new_total = total*(9/10)
    print("Over 1000TL discount applied!")
else:
    new_total = total

print("The total cost of your purchase is {0:.2f}TL".format(new_total))

