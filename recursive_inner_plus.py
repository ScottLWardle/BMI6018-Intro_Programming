# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:59:09 2024

@author: scott
"""

def find_depest_recur_list(input_list, depth=0):
    # Start with traxking deepest list and depth
    deepest_list = input_list
    max_depth = depth
    
    print(f'Current list: {deepest_list}')
    
    # while there are still some lists to process
    for item in input_list:
        if isinstance(item, list):
            print(f'looking to see if {item} is a list')
            #do recursive here to find deepest list
            try_list, curr_depth = find_depest_recur_list(item, depth +1)
            
            #update if found deeper list
            if curr_depth > max_depth:
                deepest_list = try_list
                max_depth = curr_depth
                
    return deepest_list, max_depth


def addto_deepest_list(input_list):
    deepest_list, depth = find_depest_recur_list(input_list)
    print(f'Deepest list found -- {deepest_list} at {depth} depth')
    
    #now add 1 to each element in deepest list
    for i in range(len(deepest_list)):
        if isinstance(deepest_list[i], int):
            deepest_list[i] += 1
    
    return deepest_list # Will deepest list modified            


example_list = [1, 2, [3, 4], [[5, 6], [7, [8, 9]]]]
updated_list = addto_deepest_list(example_list)
print('Updated list (plus 1)--', updated_list)
    