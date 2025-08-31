# 📘 Python String Functions - Most Commonly Used

# 🔹 1. len() - Get the length of a string
s = "hello"
print("🔹 len():", len(s))  # ➡️ Output: 5

# 🔹 2. lower() - Convert to lowercase
s = "HELLO"
print("🔹 lower():", s.lower())  # ➡️ Output: "hello"

# 🔹 3. upper() - Convert to uppercase
s = "hello"
print("🔹 upper():", s.upper())  # ➡️ Output: "HELLO"

# 🔹 4. strip() - Remove leading/trailing whitespace
s = "   hello   "
print("🔹 strip():", s.strip())  # ➡️ Output: "hello"

# 🔹 5. replace() - Replace part of a string
s = "hello world"
print("🔹 replace():", s.replace("world", "Python"))  # ➡️ Output: "hello Python"

# 🔹 6. split() - Split string into list
s = "a,b,c"
print("🔹 split():", s.split(","))  # ➡️ Output: ['a', 'b', 'c']

# 🔹 7. join() - Join list into string
words = ["hello", "world"]
print("🔹 join():", " ".join(words))  # ➡️ Output: "hello world"

# 🔹 8. find() - Find position of substring
s = "hello"
print("🔹 find():", s.find("e"))  # ➡️ Output: 1

# 🔹 9. startswith() and endswith() - Check string prefix/suffix
s = "hello"
print("🔹 startswith():", s.startswith("he"))  # ➡️ Output: True
print("🔹 endswith():", s.endswith("lo"))      # ➡️ Output: True

# 🔹 10. isdigit(), isalpha(), isalnum() - Check content type
print("🔹 isdigit():", "123".isdigit())    # ➡️ Output: True
print("🔹 isalpha():", "abc".isalpha())    # ➡️ Output: True
print("🔹 isalnum():", "abc123".isalnum()) # ➡️ Output: True

# ✅ Done! You now know the essential string methods in Python. 🎉
