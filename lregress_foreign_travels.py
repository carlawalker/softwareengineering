#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Regressions Module | Travels for foreign countries. 
Objective: find the coefficients between the exchange rate and varible "foreign_travels".
End Result: graph plot and main indicators.
"""


#Import pandas and glob with the usual conventions.
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

#import dataset from the datamanagement module


from datamanagement import dataset 

dataset

#dataset['travels_private'].plot()
# @var x_df = DataFrame column for base "exchange_rate"
# @var y_df = DataFrame column variable y-value
x_df = dataset.loc[:,["exchange_rate"]]
y_df = dataset.loc[:,["foreign_travels"]]

# identifying the parameters
regr = linear_model.LinearRegression()
regr.fit(x_df, y_df)

# Plot outputs adjusting and plotting regression model
plt.scatter(x_df, y_df, color='black')
plt.plot(x_df, regr.predict(x_df), color='blue', linewidth=3)
plt.show()

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % np.mean((regr.predict(x_df) - y_df) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(x_df, y_df))
