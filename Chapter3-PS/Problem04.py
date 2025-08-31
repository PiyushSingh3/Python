#replace double space form poeblem 3 with single space and print the modified string.
string = input("Enter a string: ")
if " " in string:
    print("The string contains double spaces.")
else:
    print("The string does not contain double spaces.")

#replacing double space with single space
modified_string = string.replace("  ", " ")