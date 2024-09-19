"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
# creating the list 
tvshows = ["supernatural", "originals","you","tvd"]
# prints the list
print(tvshows)

"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""

# adds the new show victorious to the list 
tvshows.append("victorious") 
print(tvshows)

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
# del removes the index 1 from the list 
del tvshows[1]
print(tvshows)

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
#This function adds these new items to the already existing list 
tvshows.append("The Umbrella Academy") 
tvshows.append("Emily in Paris")
tvshows.append("lost")
print(tvshows) 

"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
# removes the thing on the 4th index 
del tvshows [4]
print(tvshows)

"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
# creates a variable for the first 2 values 
newshows = "supernatural", "you"
# prints both of the tv shows
print( newshows[0:2])

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
# Creates a variable for the additional shows 
additional_shows = "breaking bad", "stranger things"
# adds both ot the list together
new_variable = newshows + additional_shows

print(new_variable)
