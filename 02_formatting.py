"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
# makes a variable for the correct password
password = "rama123"
# the user enters their own password
user_password = input("Enter your password: ")
# checks if the password user put is not case sensitive
if user_password.lower() == password.lower(): 
    print("granted") 
else: 
    print("not granted")


"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
# User Inputs the string that they want 
user_input = input("Enter a string: ")
# If statement for if string empty
if user_input == " ":
    print("Invalid")
# If the string is not empty 
else: 
    print("valid") 

"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
# Gives the variable animal to cat
animal = "cat"
#Using the replace function to change the variable into dog 
new_animal = animal.replace("cat", "dog")
# prints the new output
print(new_animal) 


"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
# User inputs both the age and the name 
age = input("What is your age: ")
name = input("What is your name: ")
# creates the sentence with the inputs
print(f"my name is {name} and I am {age} years old. ")


"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""
# Inputs both of the float values

number1_input = input("Enter a float 1: ")
number1_float = float(number1_input)
number2_input = input("Enter a float 2: ")
number2_float = input(number2_input)
# gets the quotient
quotient = number1_input//number2_input 
print(quotient)
# prints the results rounded to the nearest tenths 
rounded_quotient = (quotient,1)
txt = f"results: {quotient:.1f}" 
print(txt) 