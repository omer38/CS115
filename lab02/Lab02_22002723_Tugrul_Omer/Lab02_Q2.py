#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:59:20 2021

@author: omertugrul
"""
a = int(input("Enter a: "))

b = int(input("Enter b: "))

summ = 0

if a >= b:
    print("{0:0d} is not < {1:0d}".format(a,b))
else:
    for i in range(a,b+1):
        if i%2==0:
            summ+=i  
    print("Sum = {0:0d}".format(summ))   
        
