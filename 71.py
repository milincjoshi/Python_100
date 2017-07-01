'''
Question:
Please write a binary search function which 
searches an item in a sorted list. 
The function should return the index of element to be searched in the list.
Hints:
Use if/elif to deal with conditions.
'''
l = [1,2,3,4,5,6,7,8,9,10]
def binary_search(x, start, stop, l):
    if(start<=stop):
        mid = (start+stop)/2
        if l[mid] == x:
            return mid
        if l[mid]<x:
            return binary_search(x, mid+1, stop, l)
        if l[mid]>x:
            return binary_search(x, start, mid-1, l)
print binary_search(1, 0, len(l)-1, l)
