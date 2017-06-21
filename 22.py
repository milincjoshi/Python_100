'''
Question:
Write a program to compute the frequency of the words from the input. 
The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

Hints
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

sentence = raw_input().split()
counter = {}
for each_word in sentence:
	if each_word in counter:
		counter[each_word] = counter[each_word]+1
	else:
		counter[each_word] = 1
sorted_map = sorted(counter.items())
for each_word, each_value in sorted_map:
#	print each_word+":"+sorted_map[each_word]
	print each_word+":"+str(each_value)