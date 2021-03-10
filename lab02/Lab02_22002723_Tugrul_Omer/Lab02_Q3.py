#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 14:07:58 2021

@author: omertugrul
"""
a = input("Enter a character:")

string = ''
while a!='*':
    if a.isdigit():
        string += a
    a = input("Enter a character:")
        
formed_string = string[::-1]
    
print( 'Formed String = "' + formed_string + '"')
    
    
    