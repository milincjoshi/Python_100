'''
Question:

Define a class Person and its two child classes: Male and Female. 
All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

Hints:
Use Subclass(Parentclass) to define a child class.
'''

class Person():
    def getGender(self):
        return "None"
class Male(Person):
    def getGender(self):
        return "Male"
class Female(Person):
    def getGender(self):
        return "Female"

print Male().getGender()
print Female().getGender()