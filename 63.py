'''
Question:
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
'''

x = int(raw_input())
ans = 0.0
for x in range(1,x+1):
    ans+=(float(x)/(x+1))
print ans