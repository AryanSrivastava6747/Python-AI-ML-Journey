"""
🟡 Medium Problem: Student Percentage Calculator
Problem Statement: A school wants a program that generates a student's result.

Write a Python program that:

1. Takes the student's name.
2. Takes marks for five subjects.
3. Calculates:
    a. Total Marks
    b. Percentage
4. Displays all the information neatly.
Assume each subject is out of 100 marks.

Input:
Student Name (String)
Five integer marks

Sample Input:
Enter name: Aryan

Math: 95
Science: 90
English: 88
Computer: 97
Physics: 91

Sample Output:
------ RESULT ------
Student    : Aryan
Total      : 461
Percentage : 92.2%

Bonus Challenge (Optional)
Also display: Average Marks: 92.2
"""
# My Approach
st_name = input ("Enter name: ") # Enter Student name

#Enter Subject marks out of 100
maths = int (input ("Math: "))
science = int (input ("Science: "))
english = int (input ("English: "))
computer = int (input ("Computer: "))
physics = int (input ("Physics: "))

# Calculate Result
total_marks = maths + science + english + computer + physics
percentage = (total_marks / 500) * 100
avg = total_marks / 5

# Display Result
print("\n----- RESULT -----")
print("Student :", st_name)
print("Total  :", total_marks)
print("Percentage    :", percentage,)
print("Average Marks :", avg)
print("----------------")

"""
Time Complexity:O(1)

Space Complexity:O(1)
"""

"""
💡 What Can Be Improved?
1. Improve Output Formatting

Current output:

Percentage    : 92.2
A cleaner output would be:

Percentage : 92.20%
You can do this with f-strings:

print(f"Percentage : {percentage:.2f}%")

:.2f means "display exactly two digits after the decimal point."

2. Use Consistent Alignment

Instead of:
print("Student :", st_name)
print("Total  :", total_marks)

Use consistent spacing:

print("Student       :", st_name)
print("Total Marks   :", total_marks)
print("Percentage    :", f"{percentage:.2f}%")
print("Average Marks :", f"{avg:.2f}")

This improves readability.

3. Use Descriptive Variable Names

Current:
avg

Better:
average_marks

Why?
Someone reading your code immediately understands what the variable represents.

4. Use f-Strings

Instead of:
print("Student :", st_name)

Modern Python style is:

print(f"Student : {st_name}")

Advantages:

Cleaner syntax
Easier to combine text and variables
Preferred in modern Python
"""

# Improved Version
st_name = input("Enter Student Name: ")

maths = int(input("Math: "))
science = int(input("Science: "))
english = int(input("English: "))
computer = int(input("Computer: "))
physics = int(input("Physics: "))

total_marks = maths + science + english + computer + physics
percentage = (total_marks / 500) * 100
average_marks = total_marks / 5

print("\n----- RESULT -----")
print(f"Student       : {st_name}")
print(f"Total Marks   : {total_marks}")
print(f"Percentage    : {percentage:.2f}%") # .2f means "display exactly two digits after the decimal point."
print(f"Average Marks : {average_marks:.2f}")
print("------------------")