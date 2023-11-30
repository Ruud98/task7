# Code that displays a logical error

name_1 = input("Please enter your first name: ")
name_2 = input("Please enter your last name: ")
name_3 = input("please enter any middle names if you have them: ")
age = input("Please enter your age: ")

print(f"Hello {name_1} {name_2} {name_3}, you are {age} years old.")

# Logical error in the order of the names when printed 
# Easily overlooked due to the unclear variable names
