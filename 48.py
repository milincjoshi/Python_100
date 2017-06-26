'''
Question:
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

Hints:

Use map() to generate a list.
Use lambda to define anonymous functions.
'''

print map(lambda x : x**2, [x for x in range(1,21)])