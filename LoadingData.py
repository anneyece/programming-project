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

# Seasons Average
Average_Winter = Winter / 3
Average_Spring = Spring / 3
Average_Summer = Summer / 3
Average_Fall = Fall / 3

print(Average_Winter)
print(Average_Spring)
print(Average_Summer)
print(Average_Fall)

# Area Names
Are = { }

for place in area :
    
    if place in Are.keys():
        Are[place] = Are[place] + 1 # adding up 
    else:
        Are[place] = 1 # giving a value of 1 to the place


# Sir, when you do run our code, make sure that you run each plot code seperately or else the graphs will be combined into 1
# Areas on a plot (Bar)

# plt.bar(Are.keys(),Are.values())
# plt.xticks(rotation=90)
# plt.tight_layout()
# plt.xlabel('LA Disctricts')
# plt.ylabel('Number of Crimes')
# plt.title('Crimes committed in different LA Districts')

# Area on a plot (Pie)

# plt.pie(Are.values(), labels = Are.keys(), autopct='%1.1f%%')
# plt.title('Percentage of Crimes committed in different LA Regions')



# The next 15 lines of code would be the code used to create the subplot graph, that in our case, would combine a line graph and a bar graph together.However, we are only two as i mentioned previously in the mios and we spent the entire weekend  and free time figuring out how to do it and we did our best, we created 5 out of the 7 graphs , I hope you can understand, this was the compromise that we were forced into since we did not get a reply from your part.
# Seasons and Months on a plot (Bar + Line)
# Average amount Seasons Bar plot code

# plt.bar(['Winter','Spring', 'Summer','Fall'],[Average_Winter, Average_Spring, Average_Summer, Average_Fall])
# plt.xlabel('Seasons')
# plt.ylabel('Average number of crimes')
# plt.title('Avergae number of crimes committed per Season')

# Months Line plot code

# plt.plot(fre.keys(),fre.values())
# plt.xticks(rotation=90) 





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

# plt.bar(time_of_crime.keys(), time_of_crime.values(), width=1)
# plt.xlabel('Hours within a day')
# plt.ylabel('Number of crimes')
# plt.title('Crimes committed depending on the time of day')

#Time on a plot (Scatter)

# plt.scatter(time_of_crime.keys(), time_of_crime.values())
# plt.xlabel('Hours within a day')
# plt.ylabel('Number of crimes')
# plt.title('Crimes committed depending on the time of day')

#Time on a plot (Scatter + Grid)

plt.scatter(time_of_crime.keys(), time_of_crime.values())
plt.grid()
plt.xlabel('Hours within a day')
plt.ylabel('Number of crimes')
plt.title('Crimes committed depending on the time of day')

plt.show()











