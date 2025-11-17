#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 19:26:10 2025

@author: anneyece isabel castro ramos and yolina bakhos :<
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/isabel/Desktop/Crime_Data_from_2020_to_Present.csv")

# =============================================================================
# 
# =============================================================================  


                #LIA deliverable 2: Visualizing your dataset
"""
date_occured = df["DATE OCC"]
area = df["AREA NAME"]
time_occ = df['TIME OCC']

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

"""
# =============================================================================
# 
# =============================================================================

                #LIA deliverable 3: Exploratory Data Analysis




# 1. Preliminary steps

#a) Initial data inspection:
print(" ")
print("Overview of the Data Structure:") # Title for organization
print(" ")

print(df.head()) # .head(): provides summery of the dataset, with the columns and rows and whats found in those cells
print(" ")
print(df.info()) # .info(): provides the amount of not empty (non-null) cells within each column (listing each one) and total columns in the dataset
print(" ")
print(df.describe()) # .describe(): does statistical test on the data in the dataset


#b) Handle duplicate entries:
print(" ")
print("Identifying Duplicates:") # Title for organization
print(" ")

print(df.duplicated()) # .duplicated(): lists the rows and determines if duplicates are or arent found inside by outputting "True" or "False"


#c) Identify missing values:
  
print(" ")
print("Identifying Missing Values:") # Title for organization
print(" ")

print(df.isnull()) # .insull(): crosstab of columns and rows and determines if a cell is empty (nul) by outputting "True" or "False"

#c) Managing missing values:

    #option 1 - fill categorical missing values with some string of your choice. Justify your decision.

#organizing the column more (explained on the report)
df["Vict Sex"] = df["Vict Sex"].map({"X": "U", "H": "U","-": "U", "F": "F","M": "M"}) # .map(): applies what is stated to the dataset, so the changes we wanted for the variables in the cells for that column are applied



filled_vict = {"Vict Sex":"U"} #stating the target column and what will be used to fill

new_df = df.fillna(filled_vict) #.fillna(): filling NA, NA as in empty (null) cell with what is stated 


#d) Correct data types and formats

# correcting format
new_df["Month"] = new_df["DATE OCC"].str[:2] # new column that is only the first 2 variable of the "DATE OCC" column, which is the month the crime occured

Seasons = [] # List that is currently empty

for s in new_df["Month"]: # "For" loop that goes throught the "Month" column, applies months to the conditions --> filters it accordingly 
  if s in ["12", "01", "02"]: # <CONDITION> if the months corespond to those listed...
      Seasons.append("Winter") # adding to the list 'Seasons', the season "Winter" that correspond to months listed
  elif s in ["03", "04", "05"]: # <CONDITION> if the months corespond to those listed
      Seasons.append("Spring") # adding to the list 'Seasons', the season "Spring" that correspond to months listed
  elif s in ["06", "07", "08"]: # <CONDITION> if the months corespond to those listed
      Seasons.append("Summer") # adding to the list 'Seasons', the season "Summer" that correspond to months listed
  else:                         # <CONDITION> if none correspond, whats left
      Seasons.append("Fall") # adding to the list 'Seasons', the season "Fall" that correspond to months listed

new_df["Seasons"] = Seasons #turn list "Seasons" as a new column based off what is a above


#c) Managing missing values:

    #option 2 - drop rows with missing values
   
new_df_isolate_vict_age = new_df.drop(new_df[new_df["Vict Age"] == 0].index) #.drop(): deletes rows where "0" is found within the column stated



# 2. Univariate non-graphical EDA

# Numerical Value

# 1 only - Vict Age

print(" ")
print("Descriptive Statistics of Victim Age:") # Title for organization
print(" ")

print(new_df_isolate_vict_age["Vict Age"].describe()) # .describe(): does statistical test on the values in column stated
print("median :",new_df_isolate_vict_age["Vict Age"].median()) # .median(): calculates the median on the values in column stated
print("skewness :",new_df_isolate_vict_age["Vict Age"].skew()) # .skew(): calculates the skewness on the values in column stated
print("kurtosis :",new_df_isolate_vict_age["Vict Age"].kurtosis()) # .kurtosis(): calculates for the kurtosis on the values in column stated



# Categorical Value
# 5 different - Vict Sex - DATE OCC - AREA NAME - TIME OCC

print(" ")
print("Descriptive Statistics of the Different Categorical Variables:") # Title for organization
print(" ")

crime_data_categorical = ["Vict Sex", "DATE OCC", "AREA NAME", "TIME OCC", "Month", "Seasons"] #list of the column names desired

for i in crime_data_categorical: # "For" loop that goes throught the desired name of the columns in our data within a list, applies them to the each (variable in that specific column) to whats within the "For" loop
    print("Frequency of", i, ":") # Title for organization
    print(new_df[i].value_counts()) # .value_counts(): calculates frequency, the amount the variable appears
    print(" ")
    print("Proportion of", i, ":") # Title for organization
    print(new_df[i].value_counts(normalize=True)) #.value_counts(): calculates proportion, the amount the variable appears in decimal form (percentage)
    print(" ")
    print("Mode of", i, ":") # Title for organization
    print(new_df[i].mode()) #.mode(): calculates for the mode, which list the most frequent variable
    print(" ")



# 3. Univariate graphical EDA

    #We ony have one numerical variable (sorry sir Tiago) --> Victim Age (Vict Age)

#b) Conditioning on other variables
sns.displot(new_df_isolate_vict_age, x="Vict Age", binwidth=2, hue="Vict Sex", element="step") # seaborn plot --> step hisotgram, overlap shown

#c) Stacked histogram
sns.displot(new_df_isolate_vict_age, x="Vict Age", binwidth=2, hue="Vict Sex", multiple="stack") # seaborn plot --> stack hisotgram, no overlap shown

#d) Dodge bars
sns.displot(new_df_isolate_vict_age, x="Vict Age", binwidth=6, hue="Vict Sex", multiple="dodge") # seaborn plot --> dodge hisotgram, moves bars horizontally

#e) Normalized histogram statistics
sns.displot(new_df_isolate_vict_age, x="Vict Age", binwidth=5, hue="Vict Sex", stat="density", common_norm=False) # seaborn plot --> normalized histogram statistics, normalizes isolated variables among histogram to better compare

#f) Kernel density estimation (choosing the smoothing bandwidth)
sns.displot(new_df_isolate_vict_age, x="Vict Age", kind="kde", bw_adjust=.50) # seaborn plot --> kernel density estimation distribution plot, continuous density estimate with smoothness determined by us

#g) Empirical cumulative distributions
sns.displot(new_df_isolate_vict_age, x="Vict Age", kind="ecdf")  # seaborn plot --> empirical cumulative distribution plot, draws curve that represents the proportion 




# 4. Multivariate non-graphical EDA

crosstab_variables = ["AREA NAME", "Month", "Seasons" ] #list of the column names desired

for i in crosstab_variables: # "For" loop that goes throught the desired name of the columns in our data within a list, applies them to the each (variable in that specific column) to whats within the "For" loop
    print("CrossTab Relationships between", i, "and Time Occurred:") # Title for organization
    print(pd.crosstab(new_df[i],new_df["TIME OCC"])) # .crosstab(): makes a cross tabulation of the two columns listed, displaying the frequency of that crossover
    print("CrossTab Relationships between", i, "and Time Occurred (Proportion):") # Title for organization
    print(pd.crosstab(new_df[i], new_df["TIME OCC"], normalize="all")) # .crosstab(..., normalize="all"): makes a cross tabulation of the two columns listed, displaying the frequency of that crossover --> normalizing over all the values, decimal it represents from all values
    print(pd.crosstab(new_df[i], new_df["TIME OCC"], normalize="index")) # .crosstab(..., normalize="index"): makes a cross tabulation of the two columns listed, displaying the frequency of that crossover --> normalizing over each row the values, decimal it represents from each row values
    print(pd.crosstab(new_df[i], new_df["TIME OCC"], normalize="columns")) # .crosstab(.., normalize="columns"): makes a cross tabulation of the two columns listed, displaying the frequency of that crossover --> normalizing over each column the values, decimal it represents from each column values


#c) Generate at least one three-way frequency table (3 or more variables, by giving a list of variables to crosstab() rather than single variables)

print(" ")
print("Three-way CrossTab Relationships between LA District, Time Occurred and Months:") # Title for organization
print(" ")

print(pd.crosstab(index=[new_df["AREA NAME"],new_df["TIME OCC"]], columns=new_df["Month"])) # .crosstab(): makes a cross tabulation of the three columns listed

    


# 5. Multivariate graphical EDA (18 plots)

#what the code whould have looked like :<
#THIS CODE does not run please dont attempt '-', just wanted to show that we knew how to execute what you wanted for this deliverable (sorry again sir Tiago)

"""

# statistical relationships (5 plots):
#a) plot using Faceting feature (col parameter in the relplot() function)

sns.displot(df, x='a numerical variable', y='a numerical variable', col='a categorical variable')


#b) plot representing 5 variables at once (x, y, hue, size, col)

sns.displot(df, x='a numerical variable', y='a numerical variable', hue='a categorical variable', size='another categorical variable', col='another categorical variable')


#c) plot using line instead of points (find a variable that makes sense emphasizing continuity and explain why)

sns.relplot(df, x='a numerical variable', y='a numerical variable', kind="line")


#d) plot illustrating standard deviation

sns.relplot(df, x='a numerical variable', y='a numerical variable', errorbar="sd", kind="line")


#e) plot including a linear regression

sns.lmplot(df, x='a numerical variable', y='a numerical variable', col="Vict Sex", hue="AREA NAME")

"""



"""
# categorical data (10 plots):
#a) categorical scatter plot with jitter enabled

sns.catplot(new_df, x='a categorical variable', y='a numerical variable')
plt.show()


#b) categorical scatter plot with jitter disabled (explain your choice of variable for this one)

sns.catplot(new_df, x='a categorical variable', y='a numerical variable', jitter=False)
plt.show()


#c) “beeswarm” plot representing 3 variables

sns.catplot(new_df, x='a categorical variable', y='a numerical variable', hue='another categorical variable', kind="swarm")
plt.show()


#d) box plot representing 3 variables

sns.catplot(new_df, x='a categorical variable', y='a numerical variable', hue='another categorical variable', kind="box")
plt.show()


#e) box plot showing the shape of the distribution (boxenplot())

sns.catplot(new_df, x='a categorical variable', y='a numerical variable', kind="boxen")
plt.show()


#f) split violin plot representing 3 variables with bandwidth adjusted for better visualization

sns.catplot(new_df, x='a categorical variable', y='a numerical variable', hue="Vict Sex", kind="violin", bw_adjust=4 )
plt.show()


#g) violin plot with scatter points inside the violin shapes

v = sns.catplot(new_df, x='a categorical variable', y='a numerical variable', kind="violin", inner=None)
sns.swarmplot(new_df, x='a categorical variable', y="Vict Age",ax=v.ax)
plt.show()


#h) bar plot representing 3 variables showing 97% confidence intervals

sns.catplot(new_df, x='a categorical variable', y='a numerical variable', hue='another categorical variable', kind="bar", errorbar=("pi", 97))
plt.show()
 
           
#i) point plot representing 3 variables showing 90% confidence intervals and lines in dashed style

sns.catplot(new_df, x='a categorical variable', y='a numerical variable', hue='another categorical variable', kind="point", linestyles=["-", "- -"], errorbar=("pi", 90))
plt.show()


#j) bar plot showing the number of observations in each category

sns.catplot(new_df, x='a categorical variable', y='a numerical variable', hue='another categorical variable', kind="bar")


# bivariate distributions (3 plots):
#a) “heatmap” plot representing 2 variables with color intensity bar and adjusted bin width.

sns.displot(new_df, x='a numerical variable', y='a numerical variable', binwidth=(2, .5), cbar=True)


#b) distribution plot with 2 variables making use of bivariate density contours with amount of curves and its lowest level adjusted (use a kernel density estimation displot()).

sns.displot(new_df, x='a numerical variable', y='a numerical variable', levels=0.2, thresh=0.1 )


#c) “heatmap” plot representing 3 variables, again of kind kde.

sns.displot(new_df, x='a numerical variable', y='a numerical variable', hue='another categorical variable', kind="kde")

"""


