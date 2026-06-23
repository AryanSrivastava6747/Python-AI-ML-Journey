"""
Python me Input ke liye input() function ka use hota hai.
Ye function user se input lene ke liye use kiya jata hai.
-->Input — input()
⚠️Remember:
input() always returns a string. If you need a number, convert it manually with int() or float().
name = input("What is your name? ")
age  = int(input("How old are you? "))

print(f"Hello {name}, you are {age} years old!")

"""
name = input("what is your name?") # yahan par hamne input() function ka use kiya hai jisme hamne user se name input lene ke liye prompt diya hai
age = int(input("what is your age?")) # yahan par hamne input() function ka use kiya hai jisme hamne user se age input lene ke liye prompt diya hai aur usse int() function ke through integer me convert kiya hai

print (f"Hello {name}, you are {age} years old!") # yaha par hamne f-string ka use kiya hai jisme hamne variable name aur age ko string ke sath print kiya hai
# Output = Hello Aryan, you are 25 years old!)