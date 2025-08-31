#write a program to fill in a letter template given below with name and date.
#letter = '''Dear <|NAME|>,
#You are selected!
#Date : <|DATE|>'''
#Replace <|NAME|> with name and <|DATE|> with date (Use string functions)
letter = '''Dear <|NAME|>,
You are selected!
Date : <|DATE|>'''
name = input("Enter Your Name : ")
date = input("Enter Date : ")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)

#or using chainged replace function

print(letter.replace("<|NAME|>", "Piyush").replace("<|DATE|>", "12/10/2023"))