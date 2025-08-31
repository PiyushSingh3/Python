#Sequence of charter enclose in quotes is called string.

name = 'Piyush' #Single line string
name = "Piyush" #Single line string
name = '''Piyush''' #Multi line string
name = """Piyush""" #Multi line string

#String can be created using single quotes, double quotes or triple quotes.

#String can be created using str() function also.
name = str('Piyush')

#String can be printed using print() function.
print(name)

#String can be concatenated using + operator.
first_name = 'Piyush'   
last_name = 'Singh'
full_name = first_name + ' ' + last_name
print(full_name)

#String can be repeated using * operator.
greeting = 'Hello! '
print(greeting * 3)  # This will print 'Hello! Hello! Hello! '

#Sting is immutable, i.e, it cannot be changed.

#String can be accessed using indexing.
first_char = full_name[0]  # This will get the first character 'P'
last_char = full_name[-1]  # This will get the last character 'h'
print(first_char)
print(last_char)

#String can be sliced using slicing operator.
substring = full_name[0:6]  # This will get the substring 'Piyush', Start index is inclusive (0) and end index is exclusive(6)
print(substring)
substring = full_name[7:]  # This will get the substring 'Singh'
print(substring)
substring = full_name[:5]  # This will get the substring 'Piyus'
print(substring)
substring = full_name[:]  # This will get the whole string 'Piyush Singh'
print(substring)    
substring = full_name[-5:]  # This will get the substring 'Singh'
print(substring)

#Sicing with skip value
substring = full_name[0:10:2]  # This will get the substring 'Pyh ig', Start index is inclusive (0), end index is exclusive(10) and skip value is 2
print(substring)   
substring = full_name[::3]  # This will get the substring 'Phn', Start index is inclusive (0), end index is exclusive(len(full_name)) and skip value is 3
print(substring)

#String functions
print(len(full_name))  # This will print the length of the string 'Piyush Singh' which is 12
print(full_name.lower())  # This will print the string in lowercase 'piyush singh'
print(full_name.upper())  # This will print the string in uppercase 'PIYUSH SINGH'
print(full_name.title())  # This will print the string in title case 'Piyush Singh'
print(full_name.count('i'))  # This will print the count of 'i' in the string which is 2
print(full_name.find('Singh'))  # This will print the starting index of substring 'Singh' which is 7
print(full_name.replace('Piyush', 'Ravi'))  # This will replace 'Piyush' with 'Ravi' and print 'Ravi Singh'
print(full_name.split(' '))  # This will split the string at space and print ['Piyush', 'Singh']
print(full_name.strip())  # This will remove any leading or trailing whitespace (if any)    and print 'Piyush Singh'
print(full_name.isalpha())  # This will check if all characters in the string are alphabetic and print False (because of space)
print(full_name.isalnum())  # This will check if all characters in the string are alphanumeric and print False (because of space)
print(full_name.startswith('Piyush'))  # This will check if the string starts with 'Piyush' and print True
print(full_name.endswith('Singh'))  # This will check if the string ends with 'Singh' and print True
print(full_name.index('Singh'))  # This will print the starting index of substring 'Singh' which is 7
print(full_name.capitalize())  # This will capitalize the first character of the string and print 'Piyush singh'
print(full_name.center(20, '*'))  # This will center the string in a field  of width 20 and fill with '*' and print '****Piyush Singh*****'
print(full_name.encode())  # This will encode the string to bytes and print b'Piyush Singh'
print(full_name.islower())  # This will check if all characters in the string are lowercase and print False
print(full_name.isupper())  # This will check if all characters in the string are uppercase and print False
print(full_name.isspace())  # This will check if all characters in the string are whitespace and print False
print(full_name.zfill(15))  # This will pad the string with zeros on the left to make it of width 15 and print '0000Piyush Singh'
print(full_name.swapcase())  # This will swap the case of all characters in the string and print 'pIYUSH sINGH'
print(full_name.partition(' '))  # This will partition the string at the first occurrence of space and print ('Piyush', ' ', 'Singh')
print(full_name.rpartition(' '))  # This will partition the string at the last occurrence of space and print ('Piyush', ' ', 'Singh')
print(full_name.rsplit(' '))  # This will split the string at space from the right and print ['Piyush', 'Singh']
print(full_name.rfind('i'))  # This will print the last index of 'i' in the string which is 8
print(full_name.lstrip())  # This will remove any leading whitespace (if any) and   print 'Piyush Singh'
print(full_name.rstrip())  # This will remove any trailing whitespace (if any) and print 'Piyush Singh'
print(full_name.expandtabs())  # This will replace all tab characters with spaces (if any) and print 'Piyush Singh'
print(full_name.isdecimal())  # This will check if all characters in the string are decimal and print False
print(full_name.isdigit())  # This will check if all characters in the string are digits and print False
print(full_name.isnumeric())  # This will check if all characters in the string are numeric and print False
