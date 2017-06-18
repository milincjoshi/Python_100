'''
Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

sentence = raw_input()
chars = list(sentence)
upper = 0
lower = 0
for each_char in chars:
	if each_char.isalpha() and each_char.isupper():
		upper+=1
	if each_char.isalpha() and each_char.islower():
		lower+=1
print upper
print lower