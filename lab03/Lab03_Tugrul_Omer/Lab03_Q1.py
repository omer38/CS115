#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 13:37:14 2021

@author: omertugrul
"""

def is_ordered(string):
    """
    This function is for checking whether the string is in alphabetic order or not
     Parameters:
     string (str):The word that will be checked if it is in alphabetic order

     Returns:
     Boolean: True or False
     """ 
    prev=""
    for char in string:        
       if prev=="":
           prev=char
       else:
           if prev>char:
               return False
           prev=char
    return True           

word = input("Enter a string: ") 

if is_ordered(word.lower()):
    print("Letters of '{}' are in alphabetical order".format(word))
           
            
            
        
            
        
        
        
        
        
    
    
    
    
    