"""
🟢 Easy Problem: Grocery Bill Calculator
Problem Statement: A local grocery shop wants a simple program to calculate the total cost of a customer's purchase.

Write a Python program that:

1. Takes the customer's name.
2. Takes the name of a product.
3. Takes the price of one product.
4. Takes the quantity purchased.
5. Calculates the total bill.
6. Displays a formatted bill.

Input:
Customer Name (String)
Product Name (String)
Product Price (Float)
Quantity (Integer)

Sample Input:
Enter customer name: Aryan
Enter product name: Apple
Enter price: 45.5
Enter quantity: 4

Sample Output:
----- BILL -----
Customer : Aryan
Product  : Apple
Price    : ₹45.5
Quantity : 4
----------------
Total Bill = ₹182.0
"""
# My Approach
# cust_name = input ("Enter Customer Name:") # Customer Name
# product_name = input ("Enter Product Name:") # Product Name
# price = float(input("Enter  Price(in Rs.):")) # Price
# quantity = int(input("Enter  Quantity:")) # Quantity of items purchase

# bill = (price * quantity)
# print (bill)

"""
This problem only requires basic input and one calculation.

Time Complexity: O(1)

Space Complexity: O(1)

This is optimal.
"""

# Improved Version
cust_name = input("Enter Customer Name: ")
product_name = input("Enter Product Name: ")
price = float(input("Enter Price (Rs.): "))
quantity = int(input("Enter Quantity: "))

bill = price * quantity 

print("\n----- BILL -----")
print("Customer :", cust_name)
print("Product  :", product_name)
print("Price    : ₹", price)
print("Quantity :", quantity)
print("----------------")
print("Total Bill = ₹", bill)