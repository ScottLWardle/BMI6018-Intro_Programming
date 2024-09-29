# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 14:23:10 2024

@author: scott
"""

def filter_list(input_list, filter_point):
    # will use a list comprehension to filter out the elements greater than the filter point
    return [input_list[i] for i in range(len(input_list)) if i <= filter_point]

my_list = [1,2,[3,4,5],6,[[7,8]],9,10]
threshold = 4
filtered_list=filter_list(my_list,threshold)
print(f'Filtered list my_list > {threshold} and got {filtered_list}')