#!/usr/bin/env python3.6
try: # code we want to try to run goes under the try
    print('Enter a numerator: ')
    numerator = int(input())
    print('Eenter a denominator: ')
    denominator = int(input())
    print(numerator / denominator)
except ZeroDivisionError: # Only catches div by zero errors
    print('**Not a legal entry**\nEenter a numerator: ')
    numerator = int(input())
    print('Eenter a denominator: ')
    denominator = int(input())
    print(numerator / denominator)
except ValueError: # Only catches value error
    print('Need a integer number.\nEnter a numerator: ')
    numerator = int(input())
    print('Enter a denominator: ')
    denominator = int(input())
    print(numerator / denominator)
except: # this statement catches all other errors
    print('You caused an error, just not a ZeroDivisonError')