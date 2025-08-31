a = "Piyush is Good boy.\nHe is very Smart." # \n is used to print in new line.
print(a)

# 📘 Python Escape Sequences Cheat Sheet

# Escape sequences are used to insert special characters into strings.

# 🔹 \n - Newline
print("🔹 Newline (\\n):")
print("Hello\nWorld")  # ➡️ Output: Hello (newline) World
print("-" * 30)

# 🔹 \t - Horizontal Tab
print("🔹 Tab (\\t):")
print("Name\t:\tJohn")  # ➡️ Output: Name    :   John
print("-" * 30)

# 🔹 \\ - Backslash
print("🔹 Backslash (\\\\):")
print("This is a backslash: \\")  # ➡️ Output: This is a backslash: \
print("-" * 30)

# 🔹 \' - Single Quote
print("🔹 Single Quote (\\'):")
print('It\'s a beautiful day!')  # ➡️ Output: It's a beautiful day!
print("-" * 30)

# 🔹 \" - Double Quote
print("🔹 Double Quote (\\\"):")
print("He said, \"Hello!\"")  # ➡️ Output: He said, "Hello!"
print("-" * 30)

# 🔹 \r - Carriage Return (moves cursor to start of line)
print("🔹 Carriage Return (\\r):")
print("12345\rABC")  # ➡️ Output: ABC45 (overwrites beginning)
print("-" * 30)

# 🔹 \b - Backspace (removes previous character)
print("🔹 Backspace (\\b):")
print("Oops\b!")  # ➡️ Output: Oop!
print("-" * 30)

# 🔹 \f - Form Feed (rarely used; used for page breaks in old printers)
print("🔹 Form Feed (\\f):")
print("Line1\fLine2")  # ➡️ Output: Line1␌Line2 (behavior depends on console)
print("-" * 30)

# 🔹 \a - Bell/Alert (may trigger a beep sound)
print("🔹 Bell (\\a):")
print("Beep!\a")  # May cause beep in some terminals
print("-" * 30)

# 🔹 \ooo - Octal value
print("🔹 Octal (\\ooo):")
print("\101\102\103")  # ➡️ Output: ABC
print("-" * 30)

# 🔹 \xhh - Hex value
print("🔹 Hex (\\xhh):")
print("\x48\x49")  # ➡️ Output: HI
print("-" * 30)

# ✅ Done! These are Python's most used escape sequences 🎉
