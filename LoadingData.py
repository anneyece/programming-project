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
time_occ = df['TIME OCC']

fre = { }

# Months
for date in date_occured:
    month = date[:2]


    if month in fre.keys():  
        fre[month] = fre[month] + 1 # adding up      
    else:
        fre[month] = 1 # giving a value of 1 to the month

# Seasons
Winter = fre['12'] + fre['01'] +  fre['02']
Spring = fre['03'] + fre['04'] +  fre['05']
Summer = fre['06'] + fre['07'] +  fre['08']
Fall = fre['09'] + fre['10'] +  fre['11']

print(Winter)
print(Spring)
print(Summer)
print(Fall)

# Area Names
Are = { }

for place in area :
    
    if place in Are.keys():
        Are[place] = Are[place] + 1 # adding up 
    else:
        Are[place] = 1 # giving a value of 1 to the place


# Sir, when you do run our code, make sure that you run each plot code seperately or else the graphs will be combined into 1
# Areas on a plot (Bar)
"plt.bar(Are.keys(),Are.values())"
"plt.xticks(rotation=90)"
"plt.tight_layout()"
"plt.xlabel('LA Disctricts')"
"plt.ylabel('Number of Crimes')"
"plt.title('Crimes committed in different LA Districts')"

# Area on a plot (Pie)
"plt.pie(Are.values(), labels = Are.keys(), autopct='%1.1f%%')"
"plt.title('Percentage of Crimes committed in different LA Regions')"



# Seasons and Area on a plot (Bar + Line)

# Seasons Bar plot code
plt.bar(['Winter','Spring', 'Summer','Fall'],[Winter, Spring, Summer, Fall])
plt.xlabel('Seasons')
plt.ylabel('Number of crimes')
plt.title('Crimes committed per Season')


# Areas Line plot code
plt.plot(Are.keys(),Are.values())
plt.xticks(rotation=90)


# Time
time_of_crime = { }

for t in time_occ:
    hour_crime = str(t).zfill(4)
    hour = hour_crime[:2]

    if hour in time_of_crime :
        time_of_crime[hour] = time_of_crime[hour] + 1 # adding up
    else:
        time_of_crime[hour] = 1 # giving a value of 1 to the time

time_of_crime = dict(sorted(time_of_crime.items()))

#Time on a plot (Histogram)
"plt.bar(time_of_crime.keys(), time_of_crime.values(), width=1)"
"plt.xlabel('Hours within a day')"
"plt.ylabel('Number of crimes')"
"plt.title('Crimes committed depending on the time of day')"

#Time on a plot (Scatter)
"plt.scatter(time_of_crime.keys(), time_of_crime.values())"
"plt.xlabel('Hours within a day')"
"plt.ylabel('Number of crimes')"
"plt.title('Crimes committed depending on the time of day')"

#Time on a plot (Scatter + Grid)
"plt.scatter(time_of_crime.keys(), time_of_crime.values())"
"plt.grid()"
"plt.xlabel('Hours within a day')"
"plt.ylabel('Number of crimes')"
"plt.title('Crimes committed depending on the time of day')"

plt.show()











