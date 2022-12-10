"""
Author: Heidi Dye
Date: 
Version: 
Purpose: 
"""

import pandas as pd
from matplotlib import pyplot as plt


#data = pd.read_csv('plot_data_run_3', usecols=[0, 7, 8], index_col=0)
data = pd.read_csv('plot_data_run_3', usecols=[0, 12], index_col=0)
data.cumsum()
print(data)

data.plot(title='Coverage per Time')