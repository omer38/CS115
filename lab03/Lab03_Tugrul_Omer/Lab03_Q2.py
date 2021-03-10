#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 13:46:19 2021

@author: omertugrul
"""

def countDigits(num):
    """
    Counts how many digits the number that was entered.
     Parameters:
     num (int): The number, which will be checked.

     Returns:
     String,Integer: "","negative",count

    """
    count=0
    if num > 0 :
        while num>=10:
            num=num//10
            count+=1
        count+=1
        return count
        
    elif num==0:
        return ""
    else:
        return "negative"
        
while True:    
    number = int(input("Enter an integer (0 to stop): ")) 
    
    if countDigits(number)=="negative":
        print("Value must be Positive")
        
    elif countDigits(number)=="":
        break
    else:
        print("{0:0d} has {1:0d} digits".format(number,countDigits(number)))
        