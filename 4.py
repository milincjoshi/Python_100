'''
Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which
contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple
'''

list_input = raw_input()
list_input = list_input.split(',')
tuple_input = tuple(list_input)

print list_input
print tuple_input