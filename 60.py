'''
Question:
Print a unicode string "hello world".
Hints:
Use u'strings' format to define unicode string.
'''

y = "hello world"
x = y.decode("utf-8")
print x
print type(x)