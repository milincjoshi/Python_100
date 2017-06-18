'''
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

#range_xy = raw_input().split(',')
low = 1000
high = 3000
ans= []
for x in range(low,high+1 ):
	iseven = True
	for y in list(str(x)):
		if int(y)%2 !=0:
			iseven = False
	if iseven:
		ans.append(str(x))
print (',').join(ans)