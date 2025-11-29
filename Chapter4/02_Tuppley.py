#Tupples are similar to lists but they are immutable , meaning once created their content cannot be changed
#Tuples are defined by parentheses () 
a=()
b=(1)
c=(1,)
print(type(a))  # ➡️ Output: <class 'tuple'>
print(type(b))  # ➡️ Output: <class 'int'> 
print(type(c))  # ➡️ Output: <class 'tuple'>

my_tuple = (1, 2, 3, 4, 5)
print("Original Tuple:", my_tuple)  # ➡️ Output: (1, 2, 3, 4, 5)
# Accessing elements
print("First Element of Tuple:", my_tuple[0])  # ➡️ Output: 1
print("Last Element of Tuple:", my_tuple[-1])  # ➡️ Output: 5
# Slicing
print("Sliced Tuple (1 to 3):", my_tuple[1:4])  # ➡️ Output: (2, 3, 4)
# Tuple length 
print("Tuple Length:", len(my_tuple))  # ➡️ Output: 5
# Looping through a tuple
for item in my_tuple:
    print("Tuple Item:", item)
# ➡️ Output: 1 2 3 4 5
# ✅ Done! You now know the basics of Python tuples.   🎉