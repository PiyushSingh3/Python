#python list are container to store a set of values of any type
#Unlike strings , strings are mutable , meaning you can change their content without changing their identity
# Lists are defined by square brackets []
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)  # ➡️ Output: [1, 2, 3, 4, 5]

#sorting a list
new_list = [2,5,4,7,1,3]
new_list.sort()
print("Sorted List:", new_list)  # ➡️ Output: [1, 2, 3, 4, 5, 7]
print("Reversed List1:", new_list[::-1])  # ➡️ Output: [7, 5, 4, 3, 2, 1]
new_list.reverse()
print("Reversed List2:", new_list)  # ➡️ Output: [7, 5, 4, 3, 2, 1]

popped_item = new_list.pop() #removes last item by default
print("After Pop:", new_list)  # ➡️ Output: [7, 5, 4, 3, 2]
print("Popped Item:", popped_item)  # ➡️ Output: 1

popped_item = new_list.pop(2)
print("After Pop:", new_list)  # ➡️ Output: [7, 5, 3, 2, 1]
print("Popped Item:", popped_item)  # ➡️ Output: 4

# Accessing elements
print("First Element:", my_list[0])  # ➡️ Output: 1
print("Last Element:", my_list[-1])  # ➡️ Output: 5

# Slicing
print("Sliced List (1 to 3):", my_list[1:4])  # ➡️ Output: [2, 3, 4]

# Adding elements
my_list.append(6)
print("After Append:", my_list)  # ➡️ Output: [1, 2, 3, 4, 5, 6]
my_list.insert(0, 0)
print("After Insert at Beginning:", my_list)  # ➡️ Output: [0   , 1, 2, 3, 4, 5, 6]

# Removing elements
my_list.remove(3)
print("After Remove 3:", my_list)  # ➡️ Output: [0, 1, 2, 4, 5, 6]
popped_item = my_list.pop()
print("After Pop:", my_list)  # ➡️ Output: [0, 1, 2, 4, 5]
print("Popped Item:", popped_item)  # ➡️ Output: 6

# List length
print("List Length:", len(my_list))  # ➡️ Output: 5

# Looping through a list
for item in my_list:
    print("List Item:", item)
# ➡️ Output: 0 1 2 4 5
# ✅ Done! You now know the basics of Python lists. 🎉

