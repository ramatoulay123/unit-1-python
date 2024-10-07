"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
# Brings the datetime function to the whole code
from datetime import datetime 
# Allows it to print the current date 
my_date = datetime.now()
print(my_date) 

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""

my_date = datetime.now() 
# changes the format to print the date in this way 
date = my_date.strftime("%m/%d/%Y") 
print(date) 

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
date_string1 = "09/25/2024" 
date_string2 = "07/25/2007" 


date_format = "%m/%d/%Y"
# Allows each of the strings format to change to the date format 
date1 = datetime.strptime(date_string1, date_format)  
date2 = datetime.strptime(date_string2, date_format)

# Subtracts both of the dates 
date_difference = date1 - date2


print("Difference in days:", date_difference.days)




"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
# User inputs 
birthday_input = input("what is the date of your birthday: ")
# changes the input into a date function 
birthdate = datetime.strptime(birthday_input, "%m/%d/%Y") 
# includes the date today 
date_today = datetime.now() 
# Subtracts both the birthdate with the date today year 
age = date_today.year - birthdate.year 
# conditional statement 
if (date_today.month, date_today.day) < (birthdate.month, birthdate.day):
    age -= 1

print(age) 
