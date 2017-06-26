'''
Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield
'''

class X(object):
	def divisible_by_7(self,n):
		i = 0
		while(i<=n):
			if i%7 ==0:
				yield i
			i+=1
obj_x = X()
gen_7 = obj_x.divisible_by_7(70)
for each_item in gen_7:
	print each_item
'''
print next(gen_7)
print next(gen_7)
print next(gen_7)
'''