text = "Hello, world, my name is"
count = 0
# Space with quotation insures that it is counting the spaces in the sentence
for char in text:
    if char == " ":
       count += 1

print(count) 


print("give me a number")
# function insures only integer are being inputed for this value
n = int(input())  


for num in range(1, n):  
# If divided by 2 and nothing remains it makes it even or else odd
    if num % 2 == 0: 
        print(num, "is even.")
    else:        
        print(num, "is odd.")



num = int(input("Enter an integer: "))
# Makes sure no negative number is being added 
if num < 0:
  print("No negative numbers.")
else:
  result = 1
# Add num + 1 since we wanna include the number that we input
  for i in range(1, num+1):
    result *= i   
# Can only print as a string so adding the str function helps it print
  print("Factorial of " + str(num) + "is"  + str(result)) 



  attempts = 0
correct_password = "secret"

while True:
    password = input("Enter your password: ")
    attempts += 1

    if password == correct_password:
        print("Correct password!")
    # break makes the condition stop running in a loop
        break 

    else:
        print("Incorrect password")
# Minium password allowed to input is 3
    if attempts >= 3:  
        print("Too many attempts")
        break

