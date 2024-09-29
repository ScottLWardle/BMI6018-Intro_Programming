# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:38:57 2024

@author: scott

"""

def find_deepest_list(input_list):
    # Start with an initial list and its depth as a 2 element tuple
    beg_list = [(input_list, 0)]
    deepest_list = input_list
    max_depth = 0
    
    print(f'Initial list: {beg_list}')
    
    # While there are still some lists to process, create a currebt list and depth
    while beg_list:
        current_list, depth = beg_list.pop()
        print(f'Popped from beginning list -- current list = {current_list}, depth = {depth}')
        
        # See if there is a deeper list, update the deepest list and depth
        if depth > max_depth:
            max_depth = depth
            deepest_list = current_list
            print(f'New deepest list was found -- {deepest_list} at {max_depth} depth')
        
        # Going through the current list and add any imbedded list into the beg_list, adding depth
        for x in current_list:
            if isinstance(x, list):
                beg_list.append((x, depth + 1))
                print(f'I found a nested list -- {x}, add it to beg_list with {depth + 1} depth')
        
        print(f'Current beg_list: {beg_list}')
        
    # Finbally lets add 1 to each element of the deepest list
    for i in range(len(deepest_list)):
        if isinstance(deepest_list[i], int):
            deepest_list[i] += 1

    print(f'Final deepest list after increment - {deepest_list} at max {max_depth} depth')
    return deepest_list

# Example usage:
example_list = [1, 2, [3, 4], [[5, 6], [7, [8, 9]]]]
deepest = find_deepest_list(example_list)
print('Deepest nested list (plus 1)--', deepest)





  
        
        