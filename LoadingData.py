#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 19:26:10 2025

@author: anneyece isabel castro ramos and yolina bakhos :<
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/isabel/Desktop/Crime_Data_from_2020_to_Present.csv")

date_occured = df["DATE OCC"]
area = df["AREA NAME"]
time_occ = df['TIME OCC']

# =============================================================================
# 
# =============================================================================  

                #LIA deliverable 2: Visualizing your dataset


# Months
fre = { } # Dictionary that is currently empty

for date in date_occured: # "For" loop that goes throught the different dates when the crime occured (that specific data column in our dataset)
    month = date[:2] # new variable name called "month" that looks at only the first 2 digits, which from our dataset is the month it occured (01 = Jan, 02 = Feb...)

    if month in fre.keys(): # <Condition> that if "month" (01 = Jan, 02 = Feb...) appears inside the dictionaries' keys...
        fre[month] = fre[month] + 1 # add a value of 1 so the .values for that "month" increases by 1 every time the loop is applied as it goes through the data
    else: #if this isn't possible, which it isnt initially because nothing is written in the dictionary...
        fre[month] = 1 # when a "month" (01 = Jan, 02 = Feb...) appears for the first time, give it a value of 1 and consider it a .key in the dictionnary the loop is creating/building (adds keys as new ones apear and tallies it up)

sorted_months = sorted(fre.keys()) # sorts the keys in numerical order/ascending order

# Seasons
Winter = fre['12'] + fre['01'] +  fre['02'] # variable name "Winter" that amounts to the combined amount of crimes committed from the months in winter
Spring = fre['03'] + fre['04'] +  fre['05'] # variable name "Spring" that amounts to the combined amount of crimes committed from the months in spring
Summer = fre['06'] + fre['07'] +  fre['08'] # variable name "Summer" that amounts to the combined amount of crimes committed from the months in summer
Fall = fre['09'] + fre['10'] +  fre['11'] # variable name "Fall" that amounts to the combined amount of crimes committed from the months in fall

# Seasons on a plot (Bar)
plt.bar(['Winter','Spring', 'Summer','Fall'],[Winter, Spring, Summer, Fall]) # Creating bar graph, x values = list of different Seasons, y values = number of crimes commited per variable name

plt.xlabel('Seasons') # Title of X axis
plt.ylabel('Total number of crimes committed') # Title of Y axis
plt.title('Crime Trends per Seasons (2020-2024)') # Title of Graph 
plt.show() # Displays the graph


# Months per year
fre2 = { } # Dictionary that is currently empty

for date_year in date_occured: # "For" loop that goes throught the different dates when the crime occured (that specific data column in our dataset)
    months_year = date_year[:2]+'-'+date_year[6:10] # new variable name called "months_year" that looks at only the first 2 digits and the 6th to the 9th digit, which from our dataset is the month and year it occured (01 = Jan, 02 = Feb... as well as 2020, 2021...)
    
    if months_year in fre2.keys(): # <Condition> that if "month_year" (01 2020, 02 2020,...) appears inside the dictionaries' keys...
        fre2[months_year]=fre2[months_year] + 1 # add a value of 1 so the .values for that "month_year" increases by 1 every time the loop is applied as it goes through the data
    else: #if this isn't possible, which it isnt initially because nothing is written in the dictionary...
        fre2[months_year] = 1 # when a "month_year" (01 2020, 02 2020,...) appears for the first time, give it a value of 1 and consider it a .key in the dictionnary the loop is creating/building (adds keys as new ones apear and tallies it up)
    

months = ['01','02','03','04','05','06','07','08','09','10','11','12'] # list of the different months

#2020
y20 = [] # List that is currently empty
for i in months: # "For" loop that goes throught the different months
    year_key = i+'-2020' # adding to each month the year -2020 ('01' -> '01-2020')
    y20.append(fre2[year_key]) # adding to the list 'y20', the number of crimes that correspond to 'year_key'

#2021
y21 = [] # List that is currently empty
for i in months: # "For" loop that goes throught the different months
    year_key = i+ '-2021' # adding to each month the year -2021 ('01' -> '01-2021')
    y21.append(fre2[year_key]) # adding to the list 'y21', the number of crimes that correspond to 'year_key'

#2022
y22 = [] # List that is currently empty
for i in months: # "For" loop that goes throught the different months
    year_key = i+ '-2022' # adding to each month the year -2022 ('01' -> '01-2022')
    y22.append(fre2[year_key]) # adding to the list 'y22', the number of crimes that correspond to 'year_key'
     
#2023
y23 = [] # List that is currently empty
for i in months: # "For" loop that goes throught the different months
    year_key = i+ '-2023' # adding to each month the year -2023 ('01' -> '01-2023')
    y23.append(fre2[year_key]) # adding to the list 'y23', the number of crimes that correspond to 'year_key'

#2024
y24 = [] # List that is currently empty
for i in months: # "For" loop that goes throught the different months
    year_key = i+ '-2024' # adding to each month the year -2024 ('01' -> '01-2024')
    y24.append(fre2[year_key]) # adding to the list 'y24', the number of crimes that correspond to 'year_key'

# Plot with data from more than one array using different colours
plt.scatter(months,y20,label='2020') # Creating scatter graph, x values = list of different Months, y values = number of crimes commited per the year 2020

plt.scatter(months,y21,label='2021') # Creating scatter graph, x values = list of different Months, y values = number of crimes commited per the year 2021

plt.scatter(months,y22,label='2022') # Creating scatter graph, x values = list of different Months, y values = number of crimes commited per the year 2022

plt.scatter(months,y23,label='2023') # Creating scatter graph, x values = list of different Months, y values = number of crimes commited per the year 2023

plt.scatter(months,y24,label='2024') # Creating scatter graph, x values = list of different Months, y values = number of crimes commited per the year 2024


plt.xlabel('Months') # title of X axis 
plt.ylabel('Total number of crimes commited') # title of Y axis 
plt.title('Monthly Crime Trends by Year (2020-2024)') # Title of Graph 
plt.legend(bbox_to_anchor=(1.05, 1),loc='upper left', borderaxespad=0.) #adds legend and places it outside to the right
plt.tight_layout() # Makes sure titles dont overlap

plt.show() # Displays the graph  
     

# Area Names
Are = { } # Dictionary that is currently empty

for place in area : # "For" loop that goes throught the different districts where each crime occured (that specific data column in our dataset)
    
    if place in Are.keys(): # <Condition> that if "place" (LA Districts) appears inside the dictionaries' keys...
        Are[place] = Are[place] + 1 # add a value of 1 so the .values for that "place" increases by 1 every time the loop is applied as it goes through the data
    else: #if this isn't possible, which it isnt initially because nothing is written in the dictionary...
        Are[place] = 1 # when a "place" (LA Districts) appears for the first time, give it a value of 1 and consider it a .key in the dictionnary the loop is creating/building (adds keys as new ones apear and tallies it up)
        

# Areas on a plot (Bar)
plt.bar(Are.keys(),Are.values()) #creating bar graph, x values = keys which are the different districts, y values = number of crimes commited 
plt.xticks(rotation=90) # This rotates the x values (districts) so that it does not overlap and can easily be read 

plt.xlabel('LA Disctricts') # Title of X axis 
plt.ylabel('Number of Crimes Committed') # Title of Y axis
plt.title('Crimes Trends per LA Districts (2020-2024)') # Title of Graph 
plt.show() # Displays the graph

# Area on a plot (Pie)
plt.pie(Are.values(), labels = Are.keys(), autopct='%1.1f%%') # Creating pie graph, y values = values which are number of crimes commited, x values = keys which are the different LA Districts, displaying the percentage

plt.title('Percentage of Crimes committed in different LA Districts (2020-2024)') # Title of the Graph since axis do not represnt correctly due to the form of a pie graph that is why we did not include them 
plt.tight_layout() # Makes sure that the names do not for sure overlap 
plt.show() # Displays the graph


#Subplot

# Average per Seasons plot (Line)
plt.subplot(1,2,1) # Intention to make subplot with 1 row and 2 columns, focusing on the first plot
plt.plot(['Winter','Spring', 'Summer','Fall'],[Winter, Spring, Summer, Fall]) # Creating linear graph, x values = list of different Seasons, y values = number of crimes commited 


# Months plot (Line)
plt.subplot(1,2,2) # Intention to make subplot with 1 row and 2 columns, focusing on the second plot
plt.plot(sorted_months ,fre.values()) # Creating linear graph, x values = list of different months (sorted), y values = number of crimes commited 

plt.title('Crime Trends per Seasons and Months (2020-2024)') # Title of Graph
plt.tight_layout() # Makes sure titles dont overlap
plt.show() # Displays the graph

# Time
time_of_crime = { } # Dictionary that is currently empty

for t in time_occ: # "For" loop that goes throught the different times when the crime occured (that specific data column in our dataset)
    hour_crime = str(t).zfill(4) # new variable name "hour_crime" that makes entire dataset 4 digits by adding a 0 in front if needed (as if data is 3 digits)
    hour = hour_crime[:2] # new variable name called "hour" that looks at only the first 2 digits in "hour_crime" the newly adjusted time, which from our dataset is the hour it occured (01 = 1am, 12 = 12 pm, 14 = 2pm)

    if hour in time_of_crime: # <Condition> that if "hour" (01 = 1am, 12 = 12 pm, 14 = 2pm) appears inside the dictionaries' keys...
        time_of_crime[hour] = time_of_crime[hour] + 1 # add a value of 1 so the .values for that "hour" increases by 1 every time the loop is applied as it goes through the data
    else: #if this isn't possible, which it isnt initially because nothing is written in the dictionary...
        time_of_crime[hour] = 1 # when a "hour" (01 = 1am, 12 = 12 pm, 14 = 2pm) appears for the first time, give it a value of 1 and consider it a .key in the dictionnary the loop is creating/building (adds keys as new ones apear and tallies it up)

time_of_crime = dict(sorted(time_of_crime.items())) # sorts the keys in numerical order/ascending order

# Time on a plot (Histogram)
plt.bar(time_of_crime.keys(), time_of_crime.values(), width=1) # Creating bar graph, x values = keys which are the different hours, y values = values which are number of crimes commited 

plt.xlabel('Hours within a day') # title of X axis 
plt.ylabel('Number of crimes') # title of Y axis 
plt.title('Crimes committed depending on the time of day (2020-2024)') # Title of Graph 
plt.show() # Displays the graph

# Time on a plot (Scatter)
plt.scatter(time_of_crime.keys(), time_of_crime.values()) # Creating scatter graph, x values = keys which are the different hours within a day, y values = values which are number of crimes committed

plt.xlabel('Hours within a day') # Title of X axis
plt.ylabel('Number of Crimes Committed') # Title of Y axis
plt.title('Crimes committed depending on the time of day (2020-2024)') # Title of Graph 
plt.show() # Displays the graph

# Time on a plot (Scatter + Grid)

plt.scatter(time_of_crime.keys(), time_of_crime.values()) # Creating scatter graph, x values = keys which are the different hours, y values = values which are number of crimes commited 

plt.grid() # Add a grid
plt.xlabel('Hours within a day') # Title of X axis
plt.ylabel('Number of crimes') # Title of Y axis
plt.title('Crimes committed depending on the time of day (2020-2024)') # Title of Graph 
plt.show() # Displays the graph


# =============================================================================
# 
# =============================================================================

                #LIA deliverable 3: Exploratory Data Analysis


# 1. Preliminary steps

#a) Initial data inspection:
print(" ")
print("Overview of the data structure:")
print(" ")

print(df.head())
print(" ")
print(df.info())
print(" ")
print(df.describe())


#b) Handle duplicate entries:
print(" ")
print("Identifying duplicates:")
print(" ")

print(df.duplicated())

    #ANSWER --> There are duplicates. Even if there were any we would not remove


#c) Identify and manage missing values:

    #(c) fill categorical missing values with some string of your choice. Justify your decision.

#looking at .info, "Vict Age" and "Vict Sex" has nulls


filled_vict = {"Vict Sex":"U"}

new_df = df.fillna(filled_vict) 


#d) Correct data types and formats:

# ---> not needed





# 2. Univariate non-graphical EDA

# Numerical Value

# 1 - Vict Age

print(df["Vict Age"].describe())
print("median :",df["Vict Age"].median())
print("skewness :",df["Vict Age"].skew())
print("kurtosis :",df["Vict Age"].kurtosis())

# Categorical Value

# 1 - Vict Sex

print(df["Vict Sex"].value_counts())

# 2 - Date Occured (date_occured)

# 3 - LA Disctrict (area)

# 4 - Time Occured (time_occ)


# 3. Univariate graphical EDA

#a) Custom and appropriate number of bins

#b) Conditioning on other variables

#c) Stacked histogram

#d) Dodge bars

#e) Normalized histogram statistics

#f) Kernel density estimation (choosing the smoothing bandwidth)

#g) Empirical cumulative distributions


# 4. Multivariate non-graphical EDA

#a) Make use of this approach at least 3 times with different variables from your dataset.

#b) Now use proportions or percentages rather than raw counts (use the “normalize” parameter from crosstab())

#c) Generate at least one three-way frequency table (3 or more variables, by giving a list of variables to crosstab() rather than single variables)


# 5. Multivariate graphical EDA (18 plots)

# statistical relationships (5 plots):
#a) plot using Faceting feature (col parameter in the relplot() function)

#b) plot representing 5 variables at once (x, y, hue, size, col)

#c) plot using line instead of points (find a variable that makes sense emphasizing continuity and explain why)

#d) plot illustrating standard deviation

#e) plot including a linear regression


# categorical data (10 plots):
#a) categorical scatter plot with jitter enabled

#b) categorical scatter plot with jitter disabled (explain your choice of variable for this one)

#c) “beeswarm” plot representing 3 variables

#d) box plot representing 3 variables

#e) box plot showing the shape of the distribution (boxenplot())

#f) split violin plot representing 3 variables with bandwidth adjusted for better visualization

#g) violin plot with scatter points inside the violin shapes

#h) bar plot representing 3 variables showing 97% confidence intervals

#i) point plot representing 3 variables showing 90% confidence intervals and lines in dashed style

#j) bar plot showing the number of observations in each category


# bivariate distributions (3 plots):
#a) “heatmap” plot representing 2 variables with color intensity bar and adjusted bin width.

#b) distribution plot with 2 variables making use of bivariate density contours with amount of curves and its lowest level adjusted (use a kernel density estimation displot()).

#c) “heatmap” plot representing 3 variables, again of kind kde.








