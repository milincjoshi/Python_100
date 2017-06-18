'''
Question:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''


list_input = raw_input()
val = [x for x in list_input.split(',') if int(x)%2!=0] # list comprehension is a way of creating list in a simple manner (used in mathematics)
print (',').join(val)