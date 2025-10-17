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

# Seasons on a plot (Bar)
plt.bar(['Winter','Spring', 'Summer','Fall'],[Winter, Spring, Summer, Fall]) # The individual listed strings of each season represented the x values and the Variable names of the seasons allowed access to the number of crimes committed per those seasons and was therefore the values in our Y axis. 
plt.xlabel('Seasons') # Title of X axis
plt.ylabel('Total number of crimes') # Title of Y axis
plt.title('Total number of crimes committed per Season') # Title of Graph 

# Areas on a plot (Bar)
plt.bar(Are.keys(),Are.values()) # First line of code represents our x and y axes that we chose for the following bar graph being accessed from a dictionnary Keys, the areas for the x values and the values as in the number of crimes being the y values
plt.xticks(rotation=90) # This rotates the x values (areas) so that it does not overlap and can easily be read 
plt.tight_layout() # Makes sure that the names do not for sure overlap 
plt.xlabel('LA Disctricts') # title of X axis 
plt.ylabel('Number of Crimes') # Title of Y axis
plt.title('Crimes committed in different LA Districts') # Title of Graph 

# Area on a plot (Pie)
plt.pie(Are.values(), labels = Are.keys(), autopct='%1.1f%%') # First line of code represents our x and y axes that we chose for the following pie graph accessed from dictionnary and the autopct dosplays the percentage of each slice of pie allowing for more precision
plt.tight_layout() # Makes sure that the names do not for sure overlap 
plt.title('Percentage of Crimes committed in different LA Regions') # Title of the Graph since axis do not represnt correctly due to the form of a pie graph that is why we did not include them 

# The next 15 lines of code would be the code used to create the subplot graph, that in our case, would combine a line graph and a bar graph together.However, we are only two as i mentioned previously in the mios and we spent the entire weekend  and free time figuring out how to do it and we did our best, we created 5 out of the 7 graphs , I hope you can understand, this was the compromise that we were forced into since we did not get a reply from your part.
# Seasons and Months on a plot (Bar + Line)
# Average amount Seasons Bar plot code
plt.bar(['Winter','Spring', 'Summer','Fall'],[Average_Winter, Average_Spring, Average_Summer, Average_Fall]) 
plt.xlabel('Seasons') # Title of X axis
plt.ylabel('Average number of crimes') # Title of Y axis
plt.title('Avergae number of crimes committed per Season')

# Months Line plot code

plt.plot(fre.keys(),fre.values())
plt.xticks(rotation=90) 

#COMMENT: This was the 6th graph intended to plot however, was not included as explained. In this graph, we were planning on displaying one singular graph which would be the result of two subplots being in our case, a bar graph represneting the (Average crimes per Seasons) and a line graph represneting (Crimes per Months) hoping that this combination would create a graph displaying the two as one.




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
plt.bar(time_of_crime.keys(), time_of_crime.values(), width=1) #First line of code represents our x and y axes that we chose for the following bar graph. We originally attempted to us the histogram function but since we already had maniplulated the data, it was no longer a raw set but it was linked to crimes, it did not work and we needed to use the bar function instead making it resemble a typical histogram by using width= 1 to thicken and closen the bars up
plt.xlabel('Hours within a day') # title of X axis 
plt.ylabel('Number of crimes') # title of Y axis 
plt.title('Crimes committed depending on the time of day') # Title of Graph 

#Time on a plot (Scatter)
plt.scatter(time_of_crime.keys(), time_of_crime.values()) # First line of code represents our x and y axes that we chose for the following scatter graph being accessed from a dictionnary Keys, X values being the different times/ hours of the day and the Y values being the Crimes committed per those times.
plt.xlabel('Hours within a day') # Title of X axis
plt.ylabel('Number of crimes') # Title of Y axis
plt.title('Crimes committed depending on the time of day') # Title of Graph 

#Time on a plot (Scatter + Grid)

plt.scatter(time_of_crime.keys(), time_of_crime.values()) # First line of code represents our x and y axes that we chose for the following scatter graph being accessed from a dictionnary Keys, X values being the different times/ hours of the day and the Y values being the Crimes committed per those times.
plt.grid() # Add a grid
plt.xlabel('Hours within a day') # Title of X axis
plt.ylabel('Number of crimes') # Title of Y axis
plt.title('Crimes committed depending on the time of day') # Title of Graph 

plt.show() # Displays the graph(s)











