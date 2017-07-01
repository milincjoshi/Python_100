'''
Please write a program to print the list 
after removing delete even numbers in [5,6,77,45,22,12,24].

Hints:
Use list comprehension to delete a bunch of element from a list.
'''

l = [5,6,77,45,22,12,24]
x = [l[s] for s in range(0,len(l)) if l[s]%2!=0]
print x