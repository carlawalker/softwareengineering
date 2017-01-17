# -*- coding: utf-8 -*-
"""
Data Management Module. 
Objective: parse multiple xlsx files, combine the data and clean it up.
End Result: a table with a column for each excel file, each row corresponding to a given year.  
"""


#Import pandas and glob with the usual conventions.


import pandas as pd
import glob


#set directory of data import files
# @var curr = files directory
curr = "../softwareengineering/Data/RV*.xlsx"


#Using glob to create a list with all the Research Variables (RV) files in the Data folder.  


glob.glob(curr)


#Creation of the data frame. This technique appends all the different rows according to the same year in column.  


dataset = pd.DataFrame()


# dataset import function
# @param f = current file in directory


for f in glob.glob(curr):
    df = pd.read_excel(f)
    dataset = dataset.append(df, ignore_index=True)

dataset    
#Transposition of the resulting table. Year (common row) is used as index while transposed. This way we obtain the end result as described above.
    

dataset = dataset.set_index("year").T


#Correction to "year" column. For some reason the code won't identify it, this correction enables to make the code consider the denomination "year" again.


dataset = dataset.reset_index().rename(columns={"index" : "year"})
dataset.columns.name = None


#Redefining year as index.

dataset.set_index("year", inplace = True)


#Remove rows with any "NaN" value


dataset = dataset.dropna()


#output


print (dataset)

