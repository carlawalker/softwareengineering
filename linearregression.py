#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 11:55:46 2017

@author: carlawalker
"""


# Import pandas, glob, sklearn, matplotlib and numpy with the usual conventions
# pandas is for easy to use data structures and data analysis
# glob is for the data import 
# sklearn and matplotlib are important for our regression and the ploting 
# numpy is required for the calculation of the coefficents 
import pandas as pd
import glob
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

# set directory of data import files
# @var curr = files directory
curr = "./Desktop/Software Engineering/python/clone_repository/softwareengineering/Data/RV*.xlsx"

#Using glob to create a list with all the Research Variables (RV) files in the Data folder.  
glob.glob(curr)

#Creation of the data frame. This technique appends all the different rows according to the same year in column.  
dataset = pd.DataFrame()


# dataset import function
# @param f = current file in directory
for f in glob.glob(curr):
    df = pd.read_excel(f)
    dataset = dataset.append(df, ignore_index=True)
    
#Transposition of the resulting table. Year (common row) is used as index while transposed. This way we obtain the end result as described above.
dataset = dataset.set_index("year").T

#Option to save the table as csv for visualization
dataset.to_csv("final_dataset.csv")
print (dataset)

# Plot the two variables against each other, x remains the same, y can be changed  
# @var x_df = DataFrame column for base "exchange_rate"
# @var y_df = DataFrame column variable y-value
x_df = dataset.loc[:,["exchange_rate"]]
y_df = dataset.loc[:,["swiss_travels"]]

# Create linear regression object
regr = linear_model.LinearRegression()
regr.fit(x_df, y_df)

# Plot outputs and show the graph 
plt.scatter(x_df, y_df, color='black')
plt.plot(x_df, regr.predict(x_df), color='blue', linewidth=3)
plt.show()

# Calculate coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % np.mean((regr.predict(x_df) - y_df) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(x_df, y_df))
