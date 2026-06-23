"""
🔴 High Problem: Employee Salary Slip Generator
Problem Statement: A company wants to automatically generate an employee's salary slip.

Write a Python program that:

1. Takes:
    Employee Name
    Employee ID
    Basic Salary
2. Calculates:
    HRA = 20% of Basic Salary
    DA = 10% of Basic Salary
    PF = 12% of Basic Salary
3. Calculates:
    Gross Salary = Basic + HRA + DA
    Net Salary = Gross Salary − PF
4. Prints a professional salary slip.

Input
Employee Name (String)
Employee ID (String)
Basic Salary (Float)

Sample Input:
Enter employee name: Aryan
Enter employee ID: EMP101
Enter basic salary: 50000

Sample Output:
----------- SALARY SLIP -----------

Employee Name : Aryan
Employee ID   : EMP101

Basic Salary  : ₹50000.0
HRA (20%)     : ₹10000.0
DA (10%)      : ₹5000.0
PF (12%)      : ₹6000.0

Gross Salary  : ₹65000.0
Net Salary    : ₹59000.0

📌 Rules: Do not use loops, functions, lists, dictionaries, or classes.
Use only:
Variables
Basic data types (int, float, str, bool)
User input (input())
Type conversion
Arithmetic operators
print()
Keep the output clean and readable.
"""

# My Approach
# Takes Employee Details
emp_name = input ("Enter Employee Name: ")
emp_id = input ("Enter Employee ID: ")
base_salary = float (input ("Enter basic salary: "))

# Calculations
hra = 20 / 100 * base_salary # 20% of Basic Salary
da = 10 / 100 * base_salary # 10% of Basic Salary
pf = 12 / 100 * base_salary # 12% of Basic Salary
gross_salary = base_salary + hra + da
net_salary = gross_salary - pf

# Display Result
print("\n----- SALARY SLIP -----")
print(f"Employee Name   : {emp_name}")
print(f"Employee ID     : {emp_id}")
print(f"\nBasic Salary    : {base_salary}")
print(f"HRA (20%)       : {hra}")
print(f"DA (10%)        : {da}")
print(f"PF (12%)        : {pf}")
print(f"\nGross Salary    : {gross_salary}")
print(f"Net Salary      : {net_salary}")
print("------------------")


"""
Time Complexity: O(1)

Space Complexity: O(1)
"""

"""
💡 Pythonic Improvements
1. Use Decimal Formatting

Currently:
Basic Salary : 50000.0

A professional salary slip usually shows two decimal places:
Basic Salary : ₹50000.00

Example:
print(f"Basic Salary : ₹{base_salary:.2f}")

2. Define Percentage Constants

Instead of writing:
hra = 20 / 100 * base_salary

you could write:

HRA_RATE = 0.20
DA_RATE = 0.10
PF_RATE = 0.12

hra = base_salary * HRA_RATE
da = base_salary * DA_RATE
pf = base_salary * PF_RATE

Benefits:
Easier to update if rates change.
Improves readability.

3. Display Currency Symbol

Instead of:

print(f"Net Salary : {net_salary}")

Use:

print(f"Net Salary : ₹{net_salary:.2f}")
This makes the output look more like a real salary slip.

4. Consistent Divider Length

Instead of:

------------------

Match the heading width:

---------------------------

It looks cleaner.
"""

# Professional Version
emp_name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
base_salary = float(input("Enter Basic Salary: "))

HRA_RATE = 0.20
DA_RATE = 0.10
PF_RATE = 0.12

hra = base_salary * HRA_RATE
da = base_salary * DA_RATE
pf = base_salary * PF_RATE

gross_salary = base_salary + hra + da
net_salary = gross_salary - pf

print("\n----------- SALARY SLIP -----------")
print(f"Employee Name : {emp_name}")
print(f"Employee ID   : {emp_id}")

print(f"\nBasic Salary  : ₹{base_salary:.2f}")
print(f"HRA (20%)     : ₹{hra:.2f}")
print(f"DA (10%)      : ₹{da:.2f}")
print(f"PF (12%)      : ₹{pf:.2f}")

print(f"\nGross Salary  : ₹{gross_salary:.2f}")
print(f"Net Salary    : ₹{net_salary:.2f}")
print("-----------------------------------")