# -*- coding: utf-8 -*-
"""
#%% the humble print statement

1.a
Using the print() function only, get the wrong_add_function to print out where
it is making a mistake, given the expected output for ex, "we are making an error 
in the loop", which you would put near the loop. 
Structure the print() statement to show what the expected output ought to be
via f-strings: ie "The correct answer is supposed to be: [...]".
1.b
Then, changing as little as possible, modify the function, using the same 
general structure to output the correct answer. Call this new function 
correct_add_function() 
"""

 """
 The function takes in two lists of integers, then it adds
 all of arg2 to each item of arg1.

 Example:
    > wrong_add_function([1,2,3],[1,1,1])
    > [6,9,12]

 whereas the expected correct answer is, [2,3,4]

 Parameters
 ----------
 arg1 : list
    list of integers.
 arg2 : list
    list of integers.

 Returns
 -------
 arg1 : list
    Elements of arg1, with each element having had the contents of 
    arg2 added to it.

 """  

#1a - adding print statements function   
def wrong_add_function(arg1,arg2):

   arg1_index=0
   while arg1_index < len(arg1):
      arg_2_sum = 0
      for arg2_elements in arg2:
         arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
         print(f"We are making an error in the loop: = {arg_2_sum}")
         print(f"The correct answer should be {arg1[arg1_index]} + {arg2[0]} = {arg1[arg1_index] + arg2[0]}")
      arg1[arg1_index]=arg_2_sum  
      arg1_index+=1
   return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]

wrong_add_function(arg1, arg2)

#1b - modify the function to produce correct output
def correct_add_function(arg1,arg2):

   arg1_index=0
   while arg1_index < len(arg1):
       #doing addition on the respective elements of each parameter
       arg1[arg1_index] = arg1[arg1_index] + arg2[arg1_index]
       arg1_index+=1
   return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]

correct_add_function(arg1, arg2)


#%% try, except
"""
2.a
Update the numeric section of the function with your changes from 1 for both 
2.b and 2.c

2.b
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
returns an error message to the user, in case users give invalid inputs,
(for example an input of ["5","2", 5])
: "Your input argument [1 or 2] at element [n]
is not of the expected type. Please change this and rerun. Name this function 
exception_add_function()

2.c
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
gets it to process via the string section. IE, do not, outside the function,
change the values of arg_str_1 or arg_str_2. Name this function 
correction_add_function(), i.e you will not be updating the wrong_add_function,
you will simply handle the error of wrong inputs in a seperate function, you want
the wrong_add_function to output its current result you are only bolstering the 
function for edge cases .
"""

   """
   The function takes in two lists of integers, then it adds
   all of arg2 to each item of arg1.
   
   Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [4,5,6]
   
   If the lists are lists of strings, concatenate them
   Example:
      > wrong_add_function(['1','2','3'],['1','1','1'])
      > ['1111','2111','3111']
   Parameters
   ----------
   arg1 : list
      list of integers.
   arg2 : list
      list of integers.

   Returns
   -------
   arg1 : list
      Elements of arg1, with each element having had the contents of 
      arg2 added to it.

   """
def wrong_add_function(arg1,arg2):

   #2a - updated numeric section with changes from 1
   #numeric section
   if sum([type(i)==int for i in arg1])==len(arg1) and \
      sum([type(i)==int for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
             arg1[arg1_index] = arg1[arg1_index] + arg2[arg1_index]
             arg1_index+=1
         return arg1
   #string section
   elif sum([type(i)==str for i in arg1])==len(arg1) and \
      sum([type(i)==str for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
               arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
         return arg1
arg_str_1=['1','2','3']
arg_str_2=['1','1', 1]

def exception_add_function(arg1, arg2):
    """function will evaluate the inputs to check (try) that all elements in arg1 /
    and arg2 are all ints or all strings.  if not, will raise custom type error message
    """
    try:
        #observe the variable type of first argument if int then make that the expected type
        if isinstance(arg1[0], int):
            expected_type = int
        else:
            expected_type = str
            
        #make sure all elements in arg1 and arg 2 match expected type
        for index, element in enumerate(arg1):
            if not isinstance(element, expected_type):
                raise TypeError(f"Sorry the element for [arg1] at position [{index}] is not of the expected type [{expected_type}]")
                
        for index, element in enumerate(arg2):
            if not isinstance(element, expected_type):
                raise TypeError(f"Sorry the element for [arg2] at position [{index}] is not of the expected type [{expected_type}]")
                
        #if all is fine, return the call to the main function
        return wrong_add_function(arg1, arg2)
    
    except TypeError as whatelse:
        return str(whatelse)

arg1 = ['1','2','3']
arg2 = ['1','1', 1]    
result=exception_add_function(arg1, arg2)
print(result)

def correction_add_function(arg1,arg2):
    """function will evaluate inputs and try all elements in arg1 /
    and arg2 are all ints or all strings. If not it will correct the inputs /
    converting them to the expected type based on first one found
    """
    try:
        #observe the variable type of first argument if int then make that the expected type
        if isinstance(arg1[0], int):
            expected_type = int
        else:
            expected_type = str
            
        #correct any elements in arg1 and arg 2 that dont match expected type
        if expected_type == str:
            arg1 = [str(element) if isinstance(element, int) else element for element in arg1]
            arg2 = [str(element) if isinstance(element, int) else element for element in arg2]
        elif expected_type == int:
            arg1 = [int(element) if isinstance(element, str) else element for element in arg1]
            arg2 = [int(element) if isinstance(element, str) else element for element in arg2]
            
        return wrong_add_function(arg1, arg2)
    
    except TypeError as whatelse:
        return str(whatelse)
    
arg1 = ['1','2','3']
arg2 = ['1','1', 1]    
result=correction_add_function(arg1, arg2)
print(result)
                    
