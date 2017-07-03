'''
Question:

Please write a program which accepts a string from console and print it in reverse order.

Example:
If the following string is given as input to the program:

rise to vote sir

Then, the output of the program should be:

ris etov ot esir

Hints:
Use list[::-1] to iterate a list in a reverse order.
'''
from __future__ import print_function
x = "rise to vote sir"
for y in range(len(x)-1,-1,-1):
    print(x[y],end="")