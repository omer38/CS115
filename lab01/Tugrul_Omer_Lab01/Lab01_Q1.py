#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 13:25:26 2021

@author: omertugrul
"""

v = float(input("Enter initial velocity (m/s): "))

h = float(input("Enter initial height (m): "))

t = float(input("Enter number of seconds: "))

height = (-16*(t**2)+(v*t)+h)

print("The height after {0:.1f} seconds is {1:.1f} meters".format(t,height))