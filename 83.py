'''
Question:
Please write a program to generate all sentences where 
subject is in ["I", "You"] and verb is in 
["Play", "Love"] and the object is 
in ["Hockey","Football"].
Hints:
Use list[index] notation to get a element from a list.
'''
a = ["I", "You"]
b = ["Play", "Love"]
c = ["Hockey","Football"]

for each_a in a:
    for each_b in b:
        for each_c in c:
            print each_a+" "+each_b+" "+each_c