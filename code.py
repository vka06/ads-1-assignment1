# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 12:49:11 2023

@author: vasantha kavya
"""


"""
importing libraries
pandas, matplotlib, seaborn
to plot graphs with our data
"""

import pandas as pd # giving pandas functions to pd
import matplotlib.pyplot as plt # giving matplotlib.pyplot functions to plt
import seaborn as sns # giving seaborn functions to sns

"""
reading the csv file using pandas

"""

data_file = pd.read_csv(r"C:\Users\karan\Desktop\assignment\data.csv.csv")

print(data_file.head()) # printing the data for our use

#converting it into date time format
data_file['Pivotable date'] = pd.to_datetime(data_file['Pivotable date']) 

data_file.set_index('Pivotable date', inplace = True) # setting it as index

"""
storing data we are using in variables

"""

detached_houses = data_file['Percentage change (yearly) Detached houses']

semi_detached_houses = data_file["Percentage change (yearly) Semi-detached houses"]

terraced_houses = data_file['Percentage change (yearly) Terraced houses']


"""
line plot graph

"""
def lineplt():
        plt.figure(figsize = (10, 6)) # size of figure 

        plt.plot(detached_houses.index, detached_houses, label = 'Detached houses', 
         alpha = 0.8, marker = 'o')

        plt.plot(semi_detached_houses.index, semi_detached_houses, 
         label = 'Semi-detached houses', alpha = 0.8, marker = 'v')

        plt.plot(terraced_houses.index, terraced_houses, label = 'Terraced houses', 
         alpha = 0.8,  marker = '*')

        plt.grid(visible = True, color = 'black', alpha = 0.3, linestyle = '-.', 
         linewidth = 2) # for hor & vert lines



        """
        plot's title, x axis label, y axis label and legend
 
        """

        plt.title('Yearly percentage change in house prices')

        plt.xlabel('Year')

        plt.ylabel('Percentage change')

        plt.legend()


        # Show's the plot
        plt.show()




"""
Pie chart graph

"""

def pieplot():
    # data for pie chart to plot
    pie_data = [data_file['Average price Detached houses'].sum(), 
            data_file['Average price Semi-detached houses'].sum(), 
            data_file['Average price Terraced houses'].sum(), 
            data_file['Average price Flats and maisonettes'].sum()]

    # Extracting variables to create the pie chart
    labels = ['Detached', 'Semi-Detached', 'Terraced', 'Flat']

    # ploting the pie chart
    fig, ax = plt.subplots(figsize = (10, 10)) # size of pie chart

    ax.pie(pie_data, labels = labels, autopct = '%1.1f%%', startangle = 90)

    ax.axis('equal')

    # title for pie chart
    plt.title('Distribution of Property Types within the year of 2020-22')
    plt.legend(labels,loc = "best")

    # displaying the pie plot
    plt.show()


"""
Bar plot graph

"""


sns.set_style("whitegrid") # background

sns.set(font_scale=1.2) # fontsize

fig, ax = plt.subplots(figsize=(26, 18)) # figure size

"""
plotting bar graph

"""
def barplot():
    sns.barplot(x="Percentage change (yearly) All property types", 
            y="Sales volume", data=data_file,ci = None )
    
    plt.grid(visible = True, color = 'black', alpha = 0.3, linestyle = '-.', 
             linewidth = 2) # for hor & vert lines

    plt.show()
    
    
lineplt()
pieplot()
barplot()
