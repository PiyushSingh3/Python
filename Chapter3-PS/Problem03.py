#Write a program to detect double spaces in a string.
string = input("Enter a string: ")
if "  " in string:
    print("The string contains double spaces.")
else:
    print("The string does not contain double spaces.")

#or using find function
print(string.find( "  "))  # it will return -1 if not found otherwise index of first occurence of double space