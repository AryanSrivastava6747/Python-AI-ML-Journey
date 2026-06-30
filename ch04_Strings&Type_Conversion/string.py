"""
String is a sequence of characters. It is a data type in python that is used to represent text. 
Strings are enclosed in either single quotes (' ') or double quotes (" ").
Strings are immutable, which means that once a string is created, it cannot be changed.
Strings can be concatenated using the + operator and repeated using the * operator.

--> How Strings Work Internally
Each character in a string is stored with its own Unicode number. That's why strings use more memory than integers.

ord("A")   # → 65  (Unicode of A)
chr(65)   # → "A" (Character from Unicode)

Unicode is a standard for representing text in different writing systems. 
Each character is assigned a unique number, called a code point, which can be used to represent that character in a computer system.
"""



b = "A"
print (ord(b))  # → 65  (Unicode of A)

c = " "
print (ord(c)) # → 32  (Unicode of space)

a = "1"
print (ord(a))   # → 49  (Unicode of 1)
print (type(a))  # → <class 'str'> (Type of a is string)
print (chr(49))  # → "1" (Character from Unicode)