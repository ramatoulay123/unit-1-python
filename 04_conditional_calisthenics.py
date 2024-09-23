'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''

def check_number(num):
    return num > 10 and num % 2 == 0

# you input the number
number_input = int(input("Enter an integer: "))
result = check_number(number_input)
#returns true or false
print(result)


    




'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
#Input functions 
age_input = int(input("What is your age: ")) 
student_input = input("are you a student: ") 
# conditional statements to check what the price is
if age_input < 18: 
   print("Price is 10 dollars")
elif student_input == "yes":
    print("price is 10 dollars")
else: 
    print("price is 20 dollars") 



'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
fruits = ["banana","orange","strawberry"]
fruit_input = input("Name a fruit: ")   
# makes sure when you type you get this print if its on the list
if fruit_input in fruits: 
    print("yes that fruit is on the list")    

# if the fruit is not in this happens
else:
    print("no the fruit is not on the list")


'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
# Checks if it is a leap year 
def is_century_leap_year(year):
    
    if year % 100 == 0:
       
        return year % 400 == 0
    return False

# creates the output 
year_input = int(input("Enter a year: "))
result = is_century_leap_year(year_input)
print(result)


'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
# Makes sure if the weight is less than 0 then there is an error 
def calculate_shipping_cost(weight, zone):
    if weight < 0:
        return "Error: Weight cannot be negative."
# Makes zone a and b equal their kilograms 
    if zone == 'A':
        cost_per_kg = 5
    elif zone == 'B':
        cost_per_kg = 7
# If not equal to any of these its false
    else:
        return "Error: Invalid zone."

    shipping_cost = weight * cost_per_kg
    return f"The shipping cost is ${shipping_cost:.2f}."

# Example usage:
order_weight = float(input("Enter the order weight in kg: "))
destination_zone = input("Enter the destination zone (A or B): ").upper()

result = calculate_shipping_cost(order_weight, destination_zone)
print(result)



'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''

lenghts_input = int(input("enter side lenghts: "))
# each of these triangles have certain side lenghts 
if lenghts_input == 3:
    print("equilateral and scalene")
elif lenghts_input == 2:
    print("isoceles") 
# None of the numbers entered had those side lenghts 
else: 
    print("not a triangle")