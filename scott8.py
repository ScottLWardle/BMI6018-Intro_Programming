# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 20:34:15 2024

@author: scott
"""

#q1
import numpy as np

#q2
q2=np.arange(10)
q2

#q3 - import pandas and read in csv file from the url

import pandas as pd
q3=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',sep=',',header=None)
q3

#q4 Find the position of the first occurrence of a value greater than 1.0 in petalwidth 4th column of iris dataset.
print(q3.shape)
#get the 4th column of the array and put into col4 
q4_mask_gt1 = q3.iloc[:,3] > 1
q4_mask_gt1
#get position of first element meeting condition
first_pos = q4_mask_gt1.idxmax()
print("First occurance position:", first_pos)

#Q5 From the array a, replace all values greater than 30 to 30 and less than 10 to 10.
np.random.seed(100)
a = np.random.uniform(1,50, 20)
a

# Creating an empty list
filter_a = []

# go through each element in a
for element in a:
    if element > 30:
        filter_a.append(30.)
    elif element < 10:
        filter_a.append(10.)
    else:
        filter_a.append(element)

q5 = np.array(filter_a)

print(q5)