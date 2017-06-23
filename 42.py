'''
Question:
Write a program to generate and print another tuple whose values are even numbers 
in the given tuple (1,2,3,4,5,6,7,8,9,10). 

Hints:

Use "for" to iterate the tuple
Use tuple() to generate a tuple from a list.
'''

t =(1,2,3,4,5,6,7,8,9,10)
even_l = []
odd_l = []

for x in t:
	if x%2 == 0:
		even_l.append(x)
	else:
		odd_l.append(x)
even_t = tuple(even_l)
odd_t = tuple(odd_l)

print even_t
print odd_t