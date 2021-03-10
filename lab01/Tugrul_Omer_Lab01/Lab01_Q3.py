#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 13:52:38 2021

@author: omertugrul
"""
p1 = 0
p2 = 0

set1 = int(input("Enter sets1 :"))
set2 = int(input("Enter sets2 :"))

if set1 == 3 and set2 <= 2:
    if set2 == 2:
        p1 += 2
        p2 += 1
    elif set2 < 2:
        p1 += 3
    
elif set1 == 2 and set2 == 3:
    p1 += 1
    p2 += 2
     
elif set1 < 2 and set2 == 3:
    p2 += 3

else:
    print("Wrong score")

print("p1 = {0:1d} p2 = {1:1d}".format(p1,p2))
    
    
    
