"""
3. Logical Operators: These operators are used to combine conditional statements.
    - and (Logical AND) it returns True if both operands are true, otherwise it returns False.
    - or (Logical OR) it returns True if at least one of the operands is true, otherwise it returns False.
    - not (Logical NOT) it returns True if the operand is false, and it returns False if the operand is true.
"""

# print (12 > 10 and 20 == 20) # Output: True
# print (12 > 10 and 20 == 20 and 10 >20) # Output: False

# print (10 > 20 or 20 < 10) # Output: False
# print (10 > 20 or 20 < 10 or 10 == 10) # Output: True

# print (not 12 == 34) #Output: True
# print (not 12 <= 34) #Output: False

print((5 > 3 and 10 == 10) or (4 != 4 and 2 < 1)) # Output: True
print((10 == 10 and 23 != 23) or (34 == 12 and bool("hello"))) # Output: False
print(not (5 == 5 and 3 != 4) or (10 > 20)) # Output: False