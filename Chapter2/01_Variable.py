'''A variavle is a name given to a memory loaction in an program'''
a= 5 # Integer Datatype
b=2 # Integer Datatype
c=7.12 #Floting point number Datatype
d= True #Boolean Datatype
e="Hello World" #Sting Datatype
print(a+b)

# Variable = container for storing data values
# Variables are created when you assign a value to them 

# Keywords are reserved words in Python that cannot be used as variable names
# Examples of keywords: False, None, True, and, or, not, if,

# Identifiers are names given to entities in Python like variables, functions, classes, etc.
# An identifier can be a combination of letters, digits, and underscores
# but cannot start with a digit. Identifiers are case-sensitive.



# ✅ Variable Naming Rules in Python

# 1. Variable names must start with a letter (a–z, A–Z) or an underscore (_)
# Example:
name = "Alice"
_age = 30

# 2. Variable names cannot start with a number
# ❌ Invalid:
# 1name = "Bob"   ← This will cause a SyntaxError

# 3. Variable names can include letters, numbers, and underscores
# Example:
user_1_score = 100

# 4. Variable names are case-sensitive
# These are different variables:
city = "Paris"
City = "London"

# 5. Avoid using Python reserved keywords (like if, for, class, etc.)
# ❌ Invalid:
# for = 10        ← This will cause a SyntaxError

# 6. Use descriptive names that explain what the variable stores
# 👍 Good:
temperature_celsius = 36.6
# 👎 Bad:
x = 36.6

# 7. Snake_case is the recommended naming style for variables
# Example:
total_price = 199.99

# 8. Constants (values you don't plan to change) are written in ALL_CAPS by convention
# Example:
PI = 3.14159

# 9. No special characters allowed (like @, $, %, etc.)
# ❌ Invalid:
# user@name = "John"

# 10. Avoid using built-in function names as variables (like list, str, id, etc.)
# ❌ Risky:
# list = [1, 2, 3]   ← This will override the built-in list() function
