'''
Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield
'''

class X(object):
	def divisible_by_7(self,n):
		i = 0
		while(i<n):
			if i%7 ==0:
				yield i
x = X()
print x.divisible_by_7(80)