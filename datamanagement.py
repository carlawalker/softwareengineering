# -*- coding: utf-8 -*-
"""
Data Management Module. 
Objective: parse multiple xlsx files, combine the data and clean it up.
"""

import pandas as pd
import numpy as np
import glob


glob.glob("../softwareengineering/Data/RV*.xlsx")

dataset = pd.DataFrame()
for f in glob.glob("../softwareengineering/Data/RV*.xlsx"):
    df = pd.read_excel(f)
    dataset = dataset.append(df,ignore_index=True)
    
dataset.describe()