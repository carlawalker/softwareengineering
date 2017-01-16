#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 11:55:46 2017

@author: carlawalker
"""


#Import pandas and glob with the usual conventions.
import pandas as pd
import glob
from sklearn import linear_model
import matplotlib.pyplot as plt

#Using glob to create a list with all the Research Variables (RV) files in the Data folder.  
glob.glob("../softwareengineering/Data/RV*.xlsx")


#Creation of the data frame. This technique appends all the different rows according to the same year in column.  
dataset = pd.DataFrame()
for f in glob.glob("../softwareengineering/Data/RV*.xlsx"):
    df = pd.read_excel(f)
    dataset = dataset.append(df, ignore_index=True)

    
#Transposition of the resulting table. Year (common row) is used as index while transposed. This way we obtain the end result as described above.
dataset = dataset.set_index("year").T


#Option to save the table as csv for visualization. For some reason "year" does not appear. Can be corrected. 
dataset.to_csv("final_dataset.csv")
print (dataset)

#dataset['travels_private'].plot()
travels_x = dataset['exchange_rate'].values
exchange_y = dataset['travels_private'].values
# tbd:  change dataset x,y for fit function

# split the data into training/testing sets 
travels_x_train = travels_x
travels_x_test = travels_x

exchange_y_train = exchange_y
exchange_y_test = exchange_y

# identifying the parameters
travels_x_train = [[2008,2009,2016],[1.59,1.51,1.09]]
exchange_y_train = [[2008,2009,2016],[17873.64, 15932.37,18820.7]]
regr = linear_model.LinearRegression()
regr.fit(travels_x_train, exchange_y_train)

#adjusting and plotting regression model
plt.scatter(travels_x_test,exchange_y_test, color='black')
plt.plot(travels_x_train, regr.predict(exchange_y_test), color='blue')

plt.axis([1, 1.6, 15000, 19000 ])
plt.show()
