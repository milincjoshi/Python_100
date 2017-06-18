'''
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

'''

'''
note

always remember that each method/function in a class has first parameter self in order to make it a member of class it resides in
'''

class S(object):
	def __init__(self):
		self.s = ""

	def getString(self):
		self.s = raw_input()
	def printString(self):
		print self.s.upper()

s = S()
s.getString()
s.printString()