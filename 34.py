'''
Question:
Define a function which can generate a dictionary 
where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
 The function should just print the values only.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.
'''

d = {}
def pr_d(start, end):
	for x in range(start,end+1):
		d[x] = x*x
pr_d(1,20)
for each_i in d:
	print d[each_i]