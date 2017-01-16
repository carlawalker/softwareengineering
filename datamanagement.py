# -*- coding: utf-8 -*-
"""
Data Management Module. 
Objective: parse multiple xlsx files, combine the data and clean it up.
End Result: a table with a column for each excel file, each row corresponding to a given year.  
"""


#Import pandas and glob with the usual conventions.


import pandas as pd
import glob


#Using glob to create a list with all the Research Variables (RV) files in the Data folder.  


glob.glob("../softwareengineering/Data/RV*.xlsx")


#Creation of the data frame. This technique appends all the different rows according to the same year in column.  


dataset = pd.DataFrame()
for f in glob.glob("../softwareengineering/Data/RV*.xlsx"):
    df = pd.read_excel(f)
    dataset = dataset.append(df, ignore_index=True)

    
#Transposition of the resulting table. Year (common row) is used as index while transposed. This way we obtain the end result as described above.
    

dataset = dataset.set_index("year").T

dataset


#Option to save the table as csv for visualization. For some reason "year" does not appear. Can be corrected. 


dataset.to_csv("final_dataset.csv")