'''
Question:
Define a function that can accept two strings as input and print the string with maximum length in console.
If two strings have the same length, then the function should print al l strings line by line.

Hints:

Use len() function to get the length of a string
'''

def print_max(a,b):
	if len(a)>len(b):
		print a
	if len(b)>len(a):
		print b
	if len(a)==len(b):
		print a
		print b
print_max("Milin","Joshi")
		