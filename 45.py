'''
Question:
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

Hints:

Use map() to generate a list.
Use lambda to define anonymous functions.
'''

#print map([x for x in range(1,11)], lambda x : x**2)
print map( lambda x : x**2,[x for x in range(1,11)])