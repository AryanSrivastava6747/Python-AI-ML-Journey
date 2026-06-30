"""
-->String Indexing
Every character in a string has a position number called an index. 
Positive indexes count from the left (starting at 0), negative from the right (starting at -1).

a = "Hello"
#   H  e  l  l  o
#   0  1  2  3  4   ← positive (starting from 0 and left to right)
#  -5 -4 -3 -2 -1   ← negative (starting from -1 and right to left)

print(a[0])   # H
print(a[-1])  # o

small bracket () is used for function calls, 
square bracket [] is used for indexing and slicing, and 
curly bracket {} is used for dictionaries and sets.
"""
name = "ARYAN"
print("This is the positive indexing of the string name:")
print(name[0])   # A
print(name[1])   # R
print(name[2])   # Y
print(name[3])   # A
print(name[4])   # N

print("This is the negative indexing of the string name:")
print(name[-1])  # N
print(name[-2])  # A
print(name[-3])  # Y
print(name[-4])  # R
print(name[-5])  # A
