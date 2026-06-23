"""
🔴 High: Customer Account Number Formatter
Problem Statement: A bank stores account numbers as a continuous string:

987654321234

Write a Python program that:

1. Takes the account number as a string.
2. Prints:
        First 4 digits
        Middle 4 digits
        Last 4 digits
3. Creates a masked account number in this format: 9876-****-1234
4. Converts the account number to an integer.
5. Adds 500 to the account number.
6. Displays the new account number.

Sample Input:
Enter Account Number: 987654321234

Sample Output:
First Part   : 9876
Middle Part  : 5432
Last Part    : 1234
Masked Number: 9876-****-1234
Updated Number: 987654321734

🎯 Bonus Challenge (Optional)
Without using loops or built-in reverse methods, print the account number in reverse.

Example:

Input:
987654321234

Output:
432123456789

Hint: Think about how slicing works with a negative step.
"""

# My Approach
# Takes the Account Number as a string
account_number  = input ("Enter Account Number: ")

# First 4 digits of Account Number
first_part = account_number [:4]

# Middle 4 digits of Account Number
middle_part = account_number [4:8]

# Last 4 digits of Account Number
last_part = account_number [8:]

# Creates a masked account number in this format: 9876-****-1234
masked_account_number = first_part + ("-****-") + last_part

# Account number in Reverse
reverse_account_number = account_number [::-1]

# Adds 500 to the account number
account_number = int (account_number)
updated_number = account_number + 500

# Display result
print("\n========== ACCOUNT DETAILS ==========")
print(f"First Part              : {first_part}")
print(f"Middle Part             : {middle_part}")
print(f"Last Part               : {last_part}")
print(f"Masked Account Number   : {masked_account_number}")
print(f"Updated Number          : {updated_number}")
print(f"Reverse Account Number  : {reverse_account_number}")
print("=====================================")


"""
🐍 Pythonic Improvements
1. Don't Reuse Variables for Different Types

You wrote:
account_number = int(account_number)

This works.
However, before this line:

account_number
is a string.

After this line:
account_number
is an integer.

Changing a variable's type midway can make code harder to follow.

A cleaner approach:
account_number_int = int(account_number)
updated_number = account_number_int + 500

Now it's obvious which variable is a string and which is an integer.

2. Cleaner String Concatenation

You wrote:
masked_account_number = first_part + ("-****-") + last_part
Correct.

More Pythonic:

masked_account_number = f"{first_part}-****-{last_part}"
This becomes very useful when formatting larger strings.

3. Output Formatting

Current:
print(f"Masked Account Number   : {masked_account_number}")

Already good.
The alignment throughout the output is consistent, which improves readability.

Time Complexity: O(n)
where n is the account number length.
Perfectly acceptable.

Space Complexity: O(n)
because slicing creates new strings.
Again, completely fine.
"""

# Professional Version
# ==========================================
# Customer Account Number Formatter
# Topic: String Slicing & Type Conversion
# ==========================================

# Take account number as input
account_number = input("Enter Account Number: ")

# Extract different parts
first_part = account_number[:4]
middle_part = account_number[4:8]
last_part = account_number[8:]

# Create masked account number
masked_account_number = f"{first_part}-****-{last_part}"

# Reverse account number
reverse_account_number = account_number[::-1]

# Convert to integer and add 500
account_number_int = int(account_number)
updated_number = account_number_int + 500

# Display result
print("\n========== ACCOUNT DETAILS ==========")
print(f"First Part             : {first_part}")
print(f"Middle Part            : {middle_part}")
print(f"Last Part              : {last_part}")
print(f"Masked Number          : {masked_account_number}")
print(f"Updated Number         : {updated_number}")
print(f"Reverse Account Number : {reverse_account_number}")
print("=====================================")