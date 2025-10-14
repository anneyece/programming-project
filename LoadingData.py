#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 19:26:10 2025

@author: anneyece isabel castro ramos and yolina bakhos
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/isabel/Desktop/Crime_Data_from_2020_to_Present.csv")

date_reported = df["Date Rptd"]
date_occured = df["DATE OCC"]
area = df["AREA NAME"]


fre = { }

# Months

for date in date_occured:
    month = date[:2]


    if month in fre.keys():  
        fre[month] = fre[month] + 1 # adding up      
    else:
        fre[month] = 1 # giving a value of 1 to the month


fre = dict(sorted(fre.items()))
print(fre)

# Seasons

Winter = fre['12'] + fre['01'] +  fre['02']
Spring = fre['03'] + fre['04'] +  fre['05']
Summer = fre['06'] + fre['07'] +  fre['08']
Fall = fre['09'] + fre['10'] +  fre['11']

print(Winter)
print(Spring)
print(Summer)
print(Fall)


# seasons on a plot
plt.bar(['Winter','Spring', 'Summer','Fall'],[Winter, Spring, Summer, Fall])


plt.show()

