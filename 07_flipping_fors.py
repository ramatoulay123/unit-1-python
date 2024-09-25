"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
animal = ["tiger", "lion", "bear"]
# Prints out the strings in the list
# x created a new variable
for x in animal: 
     print(x)

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
numbers = [1,2,3,4,5] 
# Set variable to make the number start at 0
total_numbers = 0  
# For each string it will add the numbers
for x in numbers: 
     total_numbers += x 
     print("The sum of the list is", total_numbers) 
      


"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
a = "cat are cute"
# Split makes the words in the sentence space out
words = a.split(" ") 
for x in words: 
     
# Len is used to measure the lenght of the word
     print(f"The word '{x}' has {len(words)} characters.")


"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result
"""

colorofrainbow = {
  "color1": "red",
  "color2": "yellow",
  "color3": "green",
  "color4": "blue" 
} 
#item is used to iterate the dictionairy
for key, value in colorofrainbow.items():
    print(f"{key}: {value}") 
      
     
"""
In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
# I notice that the output is the same as what was on the dictionairy. I did expect this since it is a dictionairy and remains the same and cant be changed such as the other elements.
