# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 18:43:26 2024

@author: scott
"""

"""Question 1 (15 Points)
Compute the euclidean distance between series (points) p and q, without using a packaged formula.
Input"""
import pandas as pd
import numpy as np
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

e_distance = np.sqrt(np.sum((p - q) ** 2))

"""Question 2 (15 Points)
Change the order of columns of a dataframe. Interchange columns 'a' and 'c'.
Input"""
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
df
q2_df = df[['c','b','a','d','e']]
q2_df

"""Question 3 (15 Points)
Change the order of columns of a dataframe.  Create a generic function to interchange two columns, without hardcoding column names.
Input"""
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))

def change_cols(df, col1, col2):
    #copy the df so it doesnt change original
    df = df.copy()
    df[col1], df[col2] = df[col2], df[col1]
    return df

print("Original Data Frame:")
print(df)
q3_new_df=change_cols(df, 'a', 'c')
print("New Data Frame")
print(q3_new_df)

"""Question 4 (15 Points)
Format or suppress scientific notations in a pandas dataframe. Suppress scientific notations like ‘e-03’ in df and print upto 4 numbers after decimal.
Input"""
df = pd.DataFrame(np.random.random(4)**10, columns=['random'])
df
q4_df_round = df.round(4)
q4_df_round

"""Question 5 (15 Points)
Create a new column that contains the row number of nearest column by euclidean distance. Create a new column such that, each row contains the row number of nearest row-record by euclidean distance.
Input"""
df_q5 = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1), columns=list('pqrs'), index=list('abcdefghij'))
df_q5
#create function to compute distance between 2 rows
def euc_dist(row1, row2):
    return np.sqrt(np.sum((row1 - row2)**2))

#compute distance between each row -testing out on row 0 and 1
dist=euc_dist(df.iloc[0], df.iloc[1])
print(f'Euclidean distance between row 0 and 1 is {dist}')

#Import a tool to help iterate over all possible combinations
from itertools import combinations

# Function to compute distance matrix
def compute_distance_matrix(df):
    # Create DataFrame to store the distances
    distance_matrix = pd.DataFrame(index=df.index, columns=df.index)
    #lets see what this bad boy looks like to start
    print(distance_matrix)
    
    # Iterate over all combinations of rows - the index is iterable, the 2 is the pairwise argument
    for i, j in combinations(df.index, 2):
        distance = euc_dist(df.loc[i], df.loc[j])
        distance_matrix.at[i, j] = distance
        distance_matrix.at[j, i] = distance  # Distance is symetric
    
    # Fill diagonal with zeros since those all 0
    np.fill_diagonal(distance_matrix.values, 0)
    
    return distance_matrix

# Compute the distance matrix
distance_matrix = compute_distance_matrix(df_q5)
print(distance_matrix)

#Now find the column with the smallest non-zero distance for each row
def find_smallest_nonzero(df):
    #create empty dictionary
    smallest_nonzero = {}
    #iterate over each row and index
    for index, row in df.iterrows():
        #elements that are not zero (the diagonal)
        non_zero_values = row[row != 0]
        #for all the ones that are not empty
        if not non_zero_values.empty:
            #find the index and value for the minimum value
            min_index = non_zero_values.idxmin()
            min_value = non_zero_values[min_index]
            #fill up the dictionary with the min values
            smallest_nonzero[index] = (min_index, min_value)
        else:
            # replace zeros with NaN
            smallest_nonzero[index] = (np.nan, np.nan)  
    # return the min values as a dataframe
    return pd.DataFrame(smallest_nonzero, index=['Nearest Row', 'Distance']).T

# Compute the distance matrix
distance_matrix = compute_distance_matrix(df_q5)

# Find the index and value of the smallest non-zero value in each row
q5_smallest_nonzero_df = find_smallest_nonzero(distance_matrix)
print(q5_smallest_nonzero_df)

"""Question 6 (15 Points)
Correlation is a statistical technique that shows how two variables are related. Pandas dataframe.corr() method is
used for creating the correlation matrix. It is used to find the pairwise correlation of all columns in the dataframe.
Any na values are automatically excluded. For any non-numeric data type columns in the dataframe it is ignored.
Input"""

data = {'A': [45, 37, 0, 42, 50],
'B': [38, 31, 1, 26, 90],
'C': [10, 15, -10, 17, 100],
'D': [60, 99, 15, 23, 56],
'E': [76, 98, -0.03, 78, 90]}

print(type(data))

q6_corr = pd.DataFrame(data)
print(isinstance(q6_corr, pd.DataFrame))
corr_matrix = df.corr()
print(corr_matrix)




