'''
Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints:

Use try/except to catch exceptions.
'''
def div(a,b):
    try:
        if(b == 0):
            raise ZeroDivisionError()
        print a/b
    except ZeroDivisionError:
        print "Cannot divide by 0"
div(5,0)