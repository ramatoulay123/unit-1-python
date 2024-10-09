"""
Task 1: Greeting
Write a function that takes a name as a 
parameter and prints a greeting message like "Hello, [name]!".
"""
# Name is the parameter 
def my_function(name): 
    print("Hello," + name)
# assigns name of the variable as rama
my_function("rama")

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
def square_number(a,b):
# returns the number as a square
    return a ** b 
# Gives the parameters values to replace a and b
x = square_number(7,2) 
# prints output of the square 
print(x)

    


"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""
a = int(input("Write a number: ")) 
# Function allows for if the number is even it will return true or false
def number(a): 
    if a % 2 == 0:
        return True
    else:
        return False
# tells wheter it is true or false 
print(number(a)) 




"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
l = int(input("What is the lenght of the rectangle: "))
w = int(input("What is the width of the rectangle: ")) 
# The lenght and width will be replaced by the value the user puts on their input
def area(l,w):
# will return the area by multiplying
    return l * w
# will print the output
print(area(l,w)) 


"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
c = int(input("enter the teampuature in celcius: ")) 

def teamputure(c): 
# This is the equation to convert celcius to farenheit 
    return (c * 1.8) + 32
# prints the out in farenheight 
print(teamputure(c)) 


"""
Task 6: Average of Numbers
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers
"""
# Imported so I can find the mean of the numbers 
import statistics

def list_of_numbers(a, b, c, d):
# Created the values as list so the mean function can work 
    return statistics.mean([a, b, c, d])  
# Puts these values as the filler
c = list_of_numbers(1, 2, 3, 4)
# prints output
print(c)


"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, and returns the total.
Your function should also optionally accept a 3rd argument for discount, and return the discounted if provided.
"""
# this parameter set the discount at 0 
def sell(price,quantity, discount =0): 
# to find the total
    total = price * quantity

    if discount:
        total -= total * (discount/100)
    return total
# gives the parameters in the function the values 
y = sell(100,2, 50) 
print(y) 
