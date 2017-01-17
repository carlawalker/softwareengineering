#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 11:55:46 2017
@author: carlawalker
"""


# Import sklearn, matplotlib and numpy with the usual conventions
# sklearn and matplotlib are important for our regression and the ploting 
# numpy is required for the calculation of the coefficents 
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np


# Import dataset from the Datamanagement Module
from datamanagement import dataset


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
