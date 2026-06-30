"""
Type conversion is the process of converting a value from one data type to another. 
In Python, you can use built-in functions to perform type conversion. 
Type conversion is useful when you want to perform operations that require specific data types or when you want to display values in a certain format.

Here are some common type conversion functions:
- int(): Converts a value to an integer.
- float(): Converts a value to a floating-point number.
- str(): Converts a value to a string.
- bool(): Converts a value to a boolean (True or False).
- list(): Converts a value to a list.
- tuple(): Converts a value to a tuple.
- set(): Converts a value to a set.
- dict(): Converts a value to a dictionary.

Type conversion can be implicit (automatically done by Python) or 
a = 12
print(a / 2)  # 6.0
# int ÷ int → float!
explicit (done by the programmer using type conversion functions).
a = 12
a = str(a)
print(a)  # "12"

The Falsy Values in Python: Everything converts to True with bool() — except these values which become False:
1. False
2. None
3. 0 (zero of any numeric type)
4. 0.0 (zero of float type)
5. 0j (zero of complex type)
6. "" (empty string)
7. [] (empty list)
8. () (empty tuple)
9. {} (empty dictionary)
10. set() (empty set)
All other values are considered Truthy.
"""

a = "12"
print(a) # "12"
print(type(a))  # <class 'str'> (Type of a is string) before type conversion

a = int(a)  # Type conversion from string to integer
print(a)  # 12
print(type(a))  # <class 'int'> (Type of a is integer) after type conversion


c = "3.14"
print(c)  # "3.14"
print(type(c))  # <class 'str'> (Type of c is string) before type conversion

c = float(c)  # Type conversion from string to float
print(c)  # 3.14
print(type(c))  # <class 'float'> (Type of c is float) after type conversion

#Note: ham sabhi variables ko string me convert kar sakte hai, 
#lekin har cheez ko integer ya float me convert nahi kar sakte hai. 
#Agar aap aise string ko integer ya float me convert karne ki koshish karenge jisme numbers nahi hai, to aapko error milega.
#Jaise yaha par c ko integer me convert karne ki koshish karte hai, to error milega, kyunki c me decimal point hai, jo integer me convert nahi ho sakta.
# c = int(c)  # Type conversion from float to integer (This will give an error)

d = "22"
print(d)  # "22"
print(type(d))  # <class 'str'> (Type of d is string) before type conversion

d = float(d)  # Type conversion from string to float
print(d)  # 22.0
print(type(d))  # <class 'float'> (Type of d is float) after type conversion

p = 25 # integer
q = 5.05 # float
r = "Python" # string
s = True # boolean
t = 1+2j # complex

print(str(p))  # "25" (Type conversion from integer to string)
print(type(str(p)))  # <class 'str'> (Type of str(p) is string after type conversion)

print(str(q))  # "5.05" (Type conversion from float to string)
print(type(str(q)))  # <class 'str'> (Type of str(q) is string after type conversion)

print(str(r))  # "Python" (Type conversion from string to string)
print(type(str(r)))  # <class 'str'> (Type of str(r) is string after type conversion)

print(str(s))  # "True" (Type conversion from boolean to string)
print(type(str(s)))  # <class 'str'> (Type of str(s) is string after type conversion)

print(str(t))  # "1+2j" (Type conversion from complex to string)
print(type(str(t)))  # <class 'str'> (Type of str(t) is string after type conversion)


a = 12 # integer
b = 3.14 # float
c = 0 # integer
d = 0.0 # float
e = "" # empty string
f = "hello" # string
g = [] # empty list
h = [1, 2, 3] # list
i = () # empty tuple
j = (1, 2, 3) # tuple
k = {} # empty dictionary
l = {"name": "Alice", "age": 30} # dictionary
m = set() # empty set
n = {1, 2, 3} # set

print(bool(a))  # True (Type conversion from integer to boolean)
print(bool(b))  # True (Type conversion from float to boolean)
print(bool(c))  # False (Type conversion from integer to boolean)
print(bool(d))  # False (Type conversion from float to boolean)
print(bool(e))  # False (Type conversion from string to boolean)
print(bool(f))  # True (Type conversion from string to boolean)
print(bool(g))  # False (Type conversion from list to boolean)
print(bool(h))  # True (Type conversion from list to boolean)
print(bool(i))  # False (Type conversion from tuple to boolean)
print(bool(j))  # True (Type conversion from tuple to boolean)
print(bool(k))  # False (Type conversion from dictionary to boolean)
print(bool(l))  # True (Type conversion from dictionary to boolean)
print(bool(m))  # False (Type conversion from set to boolean)
print(bool(n))  # True (Type conversion from set to boolean)

# Example of implicit type conversion (type coercion)
x = 5 # integer
y = 2.5 # float

result = x + y # integer + float → float
print(result)  # 7.5

result = x/y # integer ÷ float → float
print(result)  # 2.0