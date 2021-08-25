
# compresses by ignoring values of same mean and variance
# consider the "harmonic mean" in adwin
# anomalies are defined as:
# same 

import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Global Variables

t_min = 4     # minimum time steps to differentiate between a blip and a drift
mu_1 = 0      # original mean of 1st concept
mu_2 = 1      # mean of the 2nd concept, after a drift
var_1 = 0     # variance at current time step
var_2 = 0     # variance at the next time step
w = 100       # width of window in time steps
EPSILON = 0.2 # % variation before 


directory = r'data/'

def readfiles(directory):
  data_files = []
  for filename in os.listdir(directory):
    temp = pd.read_csv(os.path.join(directory, filename), sep=",", header=None)
    if filename.startswith("abrupt"): temp['label'] = 0
        
    data_files.append(temp)
    data = pd.concat(data_files, axis=0, ignore_index=True)
    
  return data

data = readfiles(directory)
print(data.shape)

plt.plot(data.iloc[:,-1])