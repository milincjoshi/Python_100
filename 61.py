'''
Write a program to read an ASCII string
 and to convert it to a unicode string encoded by utf-8.
Hints:
Use unicode() function to convert.
'''

x = raw_input()
x = unicode(x,"utf-8")
print x
print type(x)