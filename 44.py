
'''
Question:
Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

Hints:

Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.
'''

'''
understanding filter
def filter_func(n):
    if n<10:
        return n

n = 20
#list_of_nums = [x for x in l]
#print list_of_nums
g = lambda x : x**2
print g(9)
#list comprehensions
list_of_nums = [x for x in range(1,n)]
print list_of_nums

#list comprehensions, need square brackets
even_nums = [x for x in range(1,10) if x % 2 == 0]
print even_nums

#filter example
filtered_list = filter(filter_func, list_of_nums)
print filtered_list
'''

list_numbers = [x for x in range(1,11)]
print list_numbers

def filter_even_nums(n):
    if n%2 == 0:
        return n
print "ans"
#ans = filter(filter_even_nums,  list_numbers)
#ans = filter(filter_even_nums,  [x for x in range(1,11)])
ans = filter( lambda x : x%2 == 0,  [x for x in range(1,11)])

print ans