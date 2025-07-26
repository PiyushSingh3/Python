# 🧮 1. Arithmetic Operators
# Used for basic math.

# +   # Addition
# -   # Subtraction
# *   # Multiplication
# /   # Division (float result)
# //  # Floor division (whole number result)
# %   # Modulus (remainder)
# **  # Exponentiation (power)

a = 5
b = 2
print(a + b)   # 7
print(a / b)   # 2.5
print(a // b)  # 2
print(a % b)   # 1
print(a ** b)  # 25


# 🔁 2. Assignment Operators
# Used to assign values to variables.

# =     # Assign
# +=    # Add and assign
# -=    # Subtract and assign
# *=    # Multiply and assign
# /=    # Divide and assign
# //=   # Floor divide and assign
# %=    # Modulo and assign
# **=   # Power and assign

x = 10
x += 5    # x = x + 5 → 15
x *= 2    # x = x * 2 → 30
print(x)


# 🔍 3. Comparison Operators
# Used to compare values — returns True or False.

# ==   # Equal to
# !=   # Not equal to
# >    # Greater than
# <    # Less than
# >=   # Greater than or equal to
# <=   # Less than or equal to

a = 10
b = 20
print(a == b)   # False
print(a < b)    # True


# ✅ 4. Logical Operators
# Used to combine conditional statements.

# and   # True if both are True
# or    # True if at least one is True
# not   # Inverts the result

x = 5
print(x > 2 and x < 10)   # True
print(not(x > 10))        # True


# 🧠 5. Identity Operators
# Used to check if two variables refer to the same object in memory.

# is       # True if same object
# is not   # True if not same object

a = [1, 2]
b = a
c = [1, 2]
print(a is b)      # True
print(a is c)      # False (same content, different objects)


# 📦 6. Membership Operators
# Check for presence in sequences like lists, strings, etc.

# in       # True if found
# not in   # True if not found

colors = ['red', 'blue']
print('red' in colors)        # True
print('green' not in colors)  # True


# 🧱 7. Bitwise Operators (Advanced)
# Operate on binary bits.

# &   # AND
# |   # OR
# ^   # XOR
# ~   # NOT (inverts all bits)
# <<  # Shift left
# >>  # Shift right

a = 5     # 0101
b = 3     # 0011
print(a & b)  # 1 (0001)
