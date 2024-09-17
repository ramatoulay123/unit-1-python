# task 1 
#making float variable



"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
# making float variable
number = 0.9 
print(number)
# turned the number into am integer
number2 = int(number) 

print(number2) 

"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
# input your number
number3 = int(input("Please write a number: "))
# If statements 
if number3 > 0: 
    print("its positive")
# makes sure if the input is 0 it will print
elif number3 == 0: 
    print("its zero")
# if the number matches none of these conditionals then this outputs
else: 
    print("your number is negative")




"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
# input an integer 
number4 = int(input("write a number: "))
# input a float number
number5 = float(input("write a float: "))
#adds the value
addition = number4 + number5  
# subtracts the values
subtraction = number4 - number5 
# multiplies the values
multiplication = number4 * number5

division = number4 // number5 
# prints the answer as a list
print( addition , subtraction, multiplication, division)



"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
# creates the dictionary 
fruits = { 
    "banana": 10,
    "apple": 7, 
     "mango": 9, 
     "oranges": 8,
}
fruitsbasket = "banana"
# to check wheter the quantity is in the dictonary
if fruitsbasket in fruits: 
    print("there quantity of banana is 10 ") 
else: 
    print("banana is not in the dictionary")


"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
# created the list of strings 
string_number = "10, 20, 30, 40, 50"
print(string_number)

#converts the string to a list first
my_list = string_number.split(",") 
print(my_list)
#prints the tuple
my_list2 = tuple(my_list)
print(my_list2)