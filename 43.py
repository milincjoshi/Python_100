'''
Question:
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 

Hints:

Use if statement to judge condition.
'''

def print_yes(str):
	if str == "yes" or str == "YES" or str == "Yes":
		print "Yes"
	else:
		print "No"
		
print_yes(raw_input())