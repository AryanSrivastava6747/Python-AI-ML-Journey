"""
What are Data Types?
Every value in Python has a type that tells Python what kind of data it is and
what you can do with it. You don't need to declare types — Python figures it out automatically.

The Main Data Types are:
int: Whole numbers like 1, 42, -7

float: Decimal numbers like 3.14, -0.5 or fractions like 1/2, 12/3

complex: Real + imaginary numbers like 3+4j or 5-2j. Here, j is the imaginary unit.

str: Text in quotes: "hello 123 !@#$$#". It is not only letters, but can also include numbers and symbols.

bool: Only two values, True or False

NoneType: Represents nothing: None. The NoneType is used to represent the absence of a value or a null value.

"""

# Examples of different data types in Python
a = 10          # int
b = 3.14        # float
b1 = 1/2         # float
c = 2 + 3j      # complex
d = "Hello, Not Your College by Sheryians!"  # str
e = True        # bool
f = None        # NoneType

# To check the type of a variable, you can use the built-in type() function. 
# type() returns the type of the object passed to it. For example:

print(type(a))  # Output: <class 'int'>
print(type(b)) # Output: <class 'float'>
print(type(b1)) # Output: <class 'float'>
print(type(c))  # Output: <class 'complex'>
print(type(d))  # Output: <class 'str'>
print(type(e))  # Output: <class 'bool'>
print(type(f))  # Output: <class 'NoneType'>

# You  can also use type() to check the type of a literal value directly, like this:
print(type(42))         # Output: <class 'int'>
print(type(3.14))       # Output: <class 'float'>