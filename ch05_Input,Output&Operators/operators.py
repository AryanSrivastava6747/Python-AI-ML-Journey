"""
Operators are special symbols that perform specific operations on one or more operands. In Python, there are several types of operators, including:
1. Arithmetic Operators: These operators perform basic mathematical operations like addition, subtraction, multiplication, division, etc.
   - + (Addition) 
   - - (Subtraction)
   - * (Multiplication)
   - / (Division)
   - % (Modulus)
   - ** (Exponentiation)
   - // (Floor Division)

2. Comparison Operators: These operators compare two values and return a boolean result (True or False).
   - == (Equal to)
   - != (Not equal to)
   - > (Greater than)
   - < (Less than)
   - >= (Greater than or equal to)
   - <= (Less than or equal to)

3. Logical Operators: These operators are used to combine conditional statements.
   - and (Logical AND) it returns True if both operands are true, otherwise it returns False.
   - or (Logical OR) it returns True if at least one of the operands is true, otherwise it returns False.
   - not (Logical NOT) it returns True if the operand is false, and it returns False if the operand is true.

4. Assignment Operators: These operators are used to assign values to variables.
   - = (Assignment)
   - += (Add and assign)
   - -= (Subtract and assign)
   - *= (Multiply and assign)
   - /= (Divide and assign)
   - %= (Modulus and assign)
   - **= (Exponentiation and assign)
   - //= (Floor division and assign)

5. Bitwise Operators: These operators perform bit-level operations on binary numbers.
   - & (Bitwise AND)
   - | (Bitwise OR)
   - ^ (Bitwise XOR)
   - ~ (Bitwise NOT)
   - << (Left shift)
   - >> (Right shift)

6. Identity Operators: These operators compare the memory locations of two objects.
   - is (Returns True if both operands refer to the same object)
   - is not (Returns True if both operands do not refer to the same object)

7. Membership Operators: These operators test for membership in a sequence (like lists, tuples, strings).
   - in (Returns True if a value is found in the sequence)
   - not in (Returns True if a value is not found in the sequence)

In Python, operators follow a specific order of precedence, which determines the order in which operations are evaluated. 
The precedence can be remembered using the following hierarchy:
   1. Parentheses ( )
   2. Exponentiation (**)
   3. Unary plus and minus (+x, -x)
   4. Multiplication, Division, Modulus, Floor Division (*, /, %,//)
   5. Addition and Subtraction (+, -)
   6. Bitwise Shift Operators (<<, >>)
   7. Bitwise AND (&)
   8. Bitwise XOR (^)
   9. Bitwise OR (|)
   10. Comparison Operators (==, !=, >, <, >=, <=)
   11. Identity Operators (is, is not)
   12. Membership Operators (in, not in)
   13. Logical Operators (and, or, not)
   Understanding operators and their precedence is crucial for writing correct and efficient code in Python.
   """

# Arithmetic Operators (+, -, *, /, //, %, **)
a = 10
b = 3
print ("1. Addition:", a+b) # Output = 13
print ("2.Subtraction:", a-b) # Output = 7
print ("3.Multiplication:", a*b) # Output = 30
print ("4. Division:", a/b) # Output = 3.33333.... Data Type is float
print ("5. Floor Division:", a//b) # Output = 3 Data Type is integer
print ("6. Modulus:", a%b) # Output = 1 Modulus me jo remainder hota hai vo result me aata hai
print ("7. Exponentiation:", a**b) # Output = 1000 It ss a power operator i.e. 10^3

print (3 + 4 * 2) # Output 11
print (15 // 4 + 15 % 4) # Output 6
print (3 + 2 ** 2 * 5 - 1) # Output 22

