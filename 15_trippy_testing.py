"""
Exercise 1: Divide
"""
def divide(a, b):
  """Divides two numbers, handling potential division by zero.
  Args:
    a: The numerator.
    b: The denominator.

  Returns:
    The quotient, or None if b is zero.
  """
  

  if b == 0:
    return None
  else:
    return a / b
# Checks to make sure that anything divided by 0 is equal to nothing 
assert divide(10,0) == None
# checks if you divide other numbers you get an output 
assert divide(10,5) == 2  

"""
Exercise 2: Factorial
"""
def factorial(n):
  """Calculates the factorial of a non-negative integer.

  Args:
    n: A non-negative integer.

  Returns:
    The factorial of n.
  """

  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
# checks to make sure when the factorial is 0 the value is 1 
assert factorial(0) == 1
# checks to see that the factorial of 4 is 24 
assert factorial(4) == 24

"""
Exercise 3: String Reverse
"""
def reverse_string(string):
  """Reverses a given string.

  Args:
    string: A string to be reversed.

  Returns:
    The reversed string.
  """

  reversed_string = ""
  for char in string:
    reversed_string = char + reversed_string
  return reversed_string
# checks to see if these conditions will come out as this 
assert reverse_string("") == "" 
# checks to see if hello will be outputed backwards 
assert reverse_string("hello") == "olleh" 

"""
Exercise 4: Fibonacci
"""
def fibonacci(n):
  """Generates the nth Fibonacci number.

  Args:
    n: The index of the Fibonacci number to calculate.

  Returns:
    The nth Fibonacci number.
  """

  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
# tracks the first condition statement to see wheter it equals 0 
assert fibonacci(0) == 0 
# checks the second conditional statement 
assert fibonacci(1) == 1
# checks the third conditional statement 
assert fibonacci(5) == 5

"""
Exercise 5: Email Validation
"""

import re

def is_valid_email(email):
  """Determines whether email is valid or not

  Args:
    email: The email to validate

  Returns:
    Boolean value if email is valid
  """
  email_regex = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+"
  return re.match(email_regex, email) is not None
# This checks the email and in this case its true
assert is_valid_email("test@example.com") == True
# this is wrong since the output will be false so this stops my code from going further 
assert is_valid_email("@missingusername.com") == True
