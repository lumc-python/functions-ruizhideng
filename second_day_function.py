# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:58:07 2019

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:40:57 2019

@author: Administrator
"""
# Assignment Functions
# 1. Write a Python function that returns the maximum of two numbers.
def max_number_two(x,y):
    """returns the maximum of two numbers"""
    return max(x,y)
print(max_number_two(2,3))

# 2. returns the maximum of three numbers
def max_number_three(x,y,z):
    """returns the maximum of three numbers"""
    return max(max_number_two(x,y),z)
print(max_number_three(2,3,4))
# 3. positive and negative numbers
def judge_ne_po():
    """ positive and negative numbers"""
    input_number = int(input('please input a number:'))
    if type(input_number) != int :
        raise TypeError
    else:
        if input_number > 0:
            print('{} is a positive number'.format(input_number))
        elif input_number == 0:
            print('{} is == 0'.format(input_number))
        else:
            print('{} is a negative number'.format(input_number))
        
judge_ne_po()

#Practice Funcitons
# 1. Multiplication
def multiplication_pos_number(x):
    """multiply all the positive numbers in a list"""
    result = 1
    for i in x:
        if i > 0:
            result = result * i
    return result
                    
x = [-1,11,3,-1,3]
print(multiplication_pos_number(x))

# 2. Function updates
def transform_pos(x):
    """transforms all the positive numbers from a list"""
    for i in x:
        if i > 0:
            return True
x = [-1,11,3,-1,3]
print(transform_pos(x))

# 3. Palindrome
def palindrom(x):
    if x[:] == x[::-1]:
        return True
    else:
        return False
print('{} is palindrom'. format(palindrom('90.09')))

# 4. k-mer counting 
# (1/2)
def suffixes(dna_string,k):
    """Print all the sufixes"""    
    for i in range(0, len(dna_string) + 1):
        print(dna_string[i:])
        
    """Print all length 3 substrings"""     
    for i in range(0, len(dna_string) - k + 1):
        print(dna_string[i:i+k])

    """Print all unique substrings of length 3."""
    unique_words = set()
    for i in range(0, len(dna_string) - k + 1):
        unique_words.add(dna_string[i:i+k])
    print(unique_words)

string_test = "ACGT" * 3 + "TTATT" * 5
suffixes(string_test,k=4)

# (2/2)
def suffixes(dna_string,k):    
    """Print substrings""" 
    list_keys = []
    list_values = []
    for i in range(0, len(dna_string) - k + 1):
        list_keys.append(dna_string[i:i+k])
        list_values.append(k)
    print(dict(zip(list_keys,list_values)))

string_test = "ACGT" * 3 + "TTATT" * 5
suffixes(string_test,k=4)
    
    