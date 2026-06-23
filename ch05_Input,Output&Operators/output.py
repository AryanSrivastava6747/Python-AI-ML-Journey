"""
Python me output ke liye print() function ka use hota hai. 
Ye function kisi bhi value ko console par display karne ke liye use kiya jata hai.
-->Output — print()
e.g.
name = "Akarsh"
age  = 20

print("Hello!")                         # basic
print(f"My name is {name}")              # f-string ka use ham tab karte hai jab hame variable ko string ke sath print karna ho
print("Name:", name, "Age:", age)      # multiple values ka use ham tab karte hai jab hame multiple values ko print karna ho
"""

name = "Aryan"
age = "25"

print(name,age) # basic yahan par hamne variable name aur age ko print kiya hai
print(f"My name is {name} and my age is {age}") # yaha par hamne f-string ka use kiya hai
#jisme hamne variable name aur age ko string ke sath print kiya hai
# Output = My name is Aryan and my age is 25

print("My name is",name,"and my age is",age) # yaha par hamne multiple values ka use kiya hai
#jisme hamne variable name aur age ko print kiya hai
# Output = My name is Aryan and my age is 25