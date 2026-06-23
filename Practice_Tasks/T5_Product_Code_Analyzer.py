"""
🟡 Medium: Product Code Analyzer
Problem Statement: An e-commerce platform uses product codes in the format:

ABC12345

Where:

First 3 characters = Category Code
Remaining characters = Product Number

Write a program that:

1. Takes a product code as input.
2. Extracts the category code using slicing.
3. Extracts the product number using slicing.
4. Converts the product number to an integer.
5. Adds 1000 to the product number.
6. Displays all values neatly.

Sample Input:
Enter Product Code: MOB12345

Sample Output:
Category Code : MOB
Product Number: 12345
Updated Number: 13345
"""
# My Approach
# Takes Product details as input
product_code = input ("Enter Product Code: ")

# -------- String Indexing --------

# First character of the product
first_character = product_code[0]

# Last character of the product
last_character = product_code[-1]

# -------- String Slicing --------

# Category Code of the product
category_code= product_code [:3]

# Product Number of the product
product_number = int (product_code [3:])


# -------- Calculations --------
# Updated Number of the product
updated_number = product_number + 1000 

# -------- Display Result --------

print("\n========== Product Code Preview =======")
print(f"Category Code   : {category_code}")
print(f"Product Number  : {product_number}")
print(f"Updated Number  : {updated_number}")
print("=======================================")

"""
⚠️ Unnecessary Variables

You created:

first_character = product_code[0]
last_character = product_code[-1]

but never used them.
Since the problem doesn't ask for them, they should be removed.
Professional programmers try to avoid unused variables because they can confuse future readers.


🐍 Pythonic Improvements
Good
category_code = product_code[:3]
This is the preferred Python style.

Good
product_number = int(product_code[3:])
You combined slicing and type conversion in one line.
That's efficient and readable.

⚡ Efficiency

Time Complexity: O(n)

Why?
Because slicing creates a new string.

product_code[:3]
product_code[3:]

Both operations depend on the string length.

Space Complexity: O(n)
because new sliced strings are created.

For this problem, that's completely acceptable.
"""

# Professional Version
# ==========================================
# Product Code Analyzer
# Topic: String Slicing & Type Conversion
# ==========================================

# Take product code as input
product_code = input("Enter Product Code: ")

# Extract category code (first 3 characters)
category_code = product_code[:3]

# Extract product number and convert to integer
product_number = int(product_code[3:])

# Add 1000 to the product number
updated_number = product_number + 1000

# Display result
print("\n========== PRODUCT DETAILS ==========")
print(f"Category Code : {category_code}")
print(f"Product Number: {product_number}")
print(f"Updated Number: {updated_number}")
print("=====================================")