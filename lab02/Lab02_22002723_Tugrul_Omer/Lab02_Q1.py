#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:30:10 2021

@author: omertugrul
"""
x=True

while x:
    result=1
    
    a = int(input("Enter first number: "))

    b = int(input("Enter second number: "))

    c = int(input("Enter third number: "))
    
    if a < 0 and b < 0 and c < 0:
        x=False
    else:
        for char in (a,b,c):
            if char>0:
                result*=char
        print("Product of a,b,c: {0:0d}".format(result))

    
    
    