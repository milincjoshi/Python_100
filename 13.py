'''
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

sentence = raw_input()
letters = 0
numbers = 0
for each_char in list(sentence):
	if each_char.isalpha():
		letters+=1
	if each_char.isdigit():
		numbers+=1
print "LETTERS "+str(letters)
print "DIGITS "+str(numbers)
