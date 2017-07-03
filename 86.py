'''
Question:

By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

Hints:
Use list comprehension to make an array.

'''

l = [[[0 for z in range(0,8)] for y in range(0,5)] for x in range(0,3)]
print l