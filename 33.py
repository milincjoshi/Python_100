'''
Question:
Define a function which can print a dictionary where the keys are 
numbers between 1 and 20 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
'''
d = {}
def pr_d(start, end):
	for x in range(start,end+1):
		d[x] = x*x
pr_d(1,20)
print d