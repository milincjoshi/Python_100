'''
Question:
Please write a program which count and print the numbers of each character in a string input by console.
Example:
If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:
a,2
c,2
b,2
e,1
d,1
g,1
f,1
Hints:
Use dict to store key/value pairs.
Use dict.get() method to lookup a key with default value.
'''

d = {}
s = raw_input()
for each_char in s:
    d[each_char] = d.get(each_char,0)+1
print d