# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 11:48:35 2017

@author: julia_001
"""

def sum_of_squares(num, squareTracker = 0):
    squareTracker = squareTracker + num**2
    print(squareTracker)
    print(type(squareTracker))
    if num < 10:
        sum_of_squares(num + 1)
    else:
        return squareTracker
    
def square_of_sums(num, sumTracker = 0):
    sumTracker = sumTracker + num
    print(sumTracker)
    print(type(sumTracker))
    if num < 10:
        square_of_sums(num + 1)
    else:
        sumTracker = sumTracker**2
        print(sumTracker)
        print(type(sumTracker))
        return sumTracker

square_of_sums(1)
'''
finalResult = (int(square_of_sums(1)) - int(sum_of_squares(1)))
print(finalResult) 
'''