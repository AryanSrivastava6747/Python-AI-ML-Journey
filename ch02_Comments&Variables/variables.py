#-->Variables
#Think of a variable as a labelled box — you put a value inside and refer to it by the label whenever you need it.

#-->Variable Names
#Variable names can contain letters, numbers, and underscores. 
# They must start with a letter or an underscore. 
# Variable names are case-sensitive, meaning that "myVariable" and "myvariable" would be considered two different variables.

name = "Aryan Srivastava"  # This is a string variable
age = 20  # This is an integer variable
weight = 70.5  # This is a float variable

print(name) # Output: Aryan Srivastava
print(age) # Output: 20
print(weight) # Output: 70.5

""" This is a multi-line comment explaining the rules for variable names:
🚫Rules — these will cause errors:

❌  1name = "x"  → can't start with a number
❌  my name = "x"  → no spaces allowed
❌  my-name = "x"  → no special characters (except underscore)
✅  name1 = "x"  → valid

-->Naming Conventions of Variables 
camelCase  → myVariableName 
PascalCase → MyVariableName
snake_case → my_variable_name  # ✅ Python prefers this
constant_case → MY_VARIABLE_NAME  # ✅ Python prefers this for constants
"""