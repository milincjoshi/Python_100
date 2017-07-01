'''
Question:
Please write a program to print the running time of execution of "1+1" for 100 times.
Hints:
Use timeit() function to measure the running time.
'''
from timeit import Timer
def func():
    for i in range(0,100):
        1+1
t = Timer(func)
print t.timeit()