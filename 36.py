'''
Question:
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
'''
d = []
def pr_d(start, end):
	for x in range(start,end+1):
		d.append(x*x)
pr_d(1,20)
for each_i in d:
	print each_i