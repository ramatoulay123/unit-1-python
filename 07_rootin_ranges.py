

"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
# starts at 1 ends at 10
for x in range(1,11):
    print(x) 

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
#starts at 900 counting by 90s until 1000
for x in range(900,1001,90):
    print(x) 
"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
# Makes it start at 1 and ends at 100 adding 9 each time
for x in range(1,101,9):
    print(x) 

"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
total_numbers = 0
# makes it from 1 to 10
for x in range(1,11): 
#adds each of the x in the list
   total_numbers += x 
   print(total_numbers) 


"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""
# The output of the code is the small star and each line it adds one more then the other until it reaches 5
# First the code makes row equal 5 so that means the range is 5. 
# then they make another range which adds one to the already existing range this is the inner loop
# the print statement gives the stars and the end makes sure that it is spaced out without moving to the next line

rows = 5
for i in range(rows):
    for j in range(i + 1):
        print('*', end=' ')
    print()  