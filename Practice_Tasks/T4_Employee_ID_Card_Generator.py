"""
🟢 Easy: Employee ID Card Generator
Problem Statement: A company wants to generate a simple employee ID preview.

Write a Python program that:

1. Takes the employee's full name as input.
2. Takes the employee's age as input.
3. Prints:
    First character of the name
    Last character of the name
    First 3 characters of the name
    Last 3 characters of the name
    Age after converting it to an integer
    Age after 5 years

Sample Input:
Enter Name: Aryan
Enter Age: 21

Sample Output:
First Character : A
Last Character  : n
First 3 Letters : Ary
Last 3 Letters  : yan
Current Age     : 21
Age After 5 Yrs : 26
Last 3 Letters from end  : nay
"""

# My Approach 
# Takes Employee Details
employee_name = input ("Enter name: ")
employee_age = int (input ("Enter age: "))

# Calculations
first_character = employee_name[0]
last_character = employee_name[-1]
first_3_letters = employee_name[0:3]
last_3_letters = employee_name[-3:]
last_3_letters_from_end = employee_name[-1:-4:-1]
age_after_5_years = employee_age + 5

# Display result
print (f"\nFirst Character          : {first_character}")
print (f"Last Character             : {last_character}")
print (f"First 3 Letters            : {first_3_letters}")
print (f"Last 3 Letters            : {last_3_letters}")
print (f"Last 3 Letters from End    : {last_3_letters_from_end}")
print (f"Current Age                : {employee_age}")
print (f"Age after 5 years          : {age_after_5_years}")

"""
🐍 Pythonic Suggestions
1. Cleaner Slicing

Instead of:
first_3_letters = employee_name[0:3]

You can write:
first_3_letters = employee_name[:3]

Python assumes the start index is 0 when omitted.

2. Display Age with an f-string

Instead of:
print(f"Current Age : {employee_age}")

you're already doing the modern approach, which is great.

3. Keep Variable Names Consistent

You used:

employee_name
employee_age

These are descriptive and follow snake_case, which matches Python's style guide. Nicely done.

⚠️ Edge Case

What if the user enters:

Al

Then:

employee_name[:3]

returns "Al" without an error, which is good.

But your code assumes the name is non-empty.

If the user presses Enter without typing anything:

employee_name = ""

then:

employee_name[0]

raises an IndexError.

We'll learn how to handle that safely once we cover conditionals (if) and exception handling.
"""

# ==========================================
# Employee ID Preview
# Topic: String Indexing, String Slicing,
#        and Type Conversion
# ==========================================

# Take employee details as input
employee_name = input("Enter Employee Name: ")
employee_age = int(input("Enter Employee Age: "))

# -------- String Indexing --------

# First character of the name
first_character = employee_name[0]

# Last character of the name
last_character = employee_name[-1]

# -------- String Slicing --------

# First three letters of the name
first_3_letters = employee_name[:3]

# Last three letters of the name
last_3_letters = employee_name[-3:]

# Last three letters in reverse order (Bonus)
last_3_letters_from_end = employee_name[-1:-4:-1]

# -------- Calculations --------

# Calculate employee's age after 5 years
age_after_5_years = employee_age + 5

# -------- Display Result --------

print("\n========== EMPLOYEE ID PREVIEW ==========")
print(f"First Character          : {first_character}")
print(f"Last Character           : {last_character}")
print(f"First 3 Letters          : {first_3_letters}")
print(f"Last 3 Letters           : {last_3_letters}")
print(f"Last 3 Letters (Reverse) : {last_3_letters_from_end}")
print(f"Current Age              : {employee_age}")
print(f"Age After 5 Years        : {age_after_5_years}")
print("=========================================")
