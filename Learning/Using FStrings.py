# Using Fstrings
name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))
if age < 18:
    print(f"{name} is {age} years old so, not eligible to vote. ")
else:
    print(f"{name} is {age} years old so, {name} is eligible to vote. ")