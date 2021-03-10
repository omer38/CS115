#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 14:41:57 2021

@author: omertugrul
"""


def printMultiples(n,m):
    """
    Receives two integers(n,m), prints first m multiples of n
     Parameters:
     (n,m), (int,int): will print first m multiples of n 

     Returns:
     String: string

    """
    string=""
    for i in range(1,m+1):     
        string+=str(n*i)
        string+=", "
           
    string=string[0:len(string)-2]
    return string
    
first_int = int(input("Enter first integer: ")) 
second_int = int(input("Enter second integer: "))
    
while first_int>0 and second_int>0:
    print(printMultiples(first_int, second_int))
    first_int = int(input("Enter first integer: ")) 
    second_int = int(input("Enter second integer: "))