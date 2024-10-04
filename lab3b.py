#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
# Author ID: 140729229

def sum_numbers(number1, number2):
    return number1 + number2
    

def subtract_numbers(number1, number2):
    return number1 - number2

def multiply_numbers(number1, number2):
    return number1 * number2

if __name__ == '__main__':
    print(sum_numbers(10, 5))
    print(subtract_numbers(10, 5))
    print(multiply_numbers(10, 5))

import lab3b

lab3b.sum_numbers(10, 5)
# Will return 15
lab3b.sum_numbers(25, 25)
# Will return 50
lab3b.subtract_numbers(10, 5)
# Will return 5
lab3b.subtract_numbers(5, 10)
# Will return -5
lab3b.multiply_numbers(10, 5)
# Will return 50
lab3b.multiply_numbers(10, 2)
# Will return 20

