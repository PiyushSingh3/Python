# write a program to accept marks of 6 students and display them in a list

Marks = []

m1 = int (input("Enter the masrks of 1st student : "))
Marks.append(m1)
m2 = int (input("Enter the masrks of 2nd student : "))  
Marks.append(m2)
m3 = int (input("Enter the masrks of 3rd student : "))
Marks.append(m3)
m4 = int (input("Enter the masrks of 4th student : "))
Marks.append(m4)
m5 = int (input("Enter the masrks of 5th student : "))
Marks.append(m5)
m6 = int (input("Enter the masrks of 6th student : "))
Marks.append(m6)

Marks.sort()

print("The marks of the students are:", Marks)   