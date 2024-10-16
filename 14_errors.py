"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""
num1 = int(input("enter a number: "))
num2 = int(input("enter a second number: "))



def divide_numbers(num1, num2):
    try:
        # Error was that division cannot be by 0
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Please provide numbers.")
        return None

    print("Result:", result)

# Example usage
divide_numbers(num1, num2)  # Using user inputs



# Example usage:
divide_numbers(10, 0)


"""
Example 2: Opening Files
"""

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
        print(f"Error: The file  was not found.")
    except PermissionError:       
        print(f"Error: You do not have permission to read the file.")
    except Exception as e:   
        print(f"An unexpected error occurred")

# Example usage
read_file("example.txt")  # Replace with the actual filename you want to read
 
   

# Example usage:
read_file("nonexistent.txt")

"""
Example 3: List Items
"""
my_list = [1,2,3]

def get_item(lst, index):
    try:
        item = lst[index]
        print("Item:", item)
    except IndexError: 
        print("the index is out of range")
    except TypeError: 
        print("provide a valid number")
    except Exception:
        print("an unexpected error has occured")

# Example usage:
my_list = [1, 2, 3]
get_item(my_list, 5)


"""
Example 4: Dictionaries
"""

def get_value(dictionary, key):
    try:
          value = dictionary[key]
          print("Value:", value)
# there is a key error it will excute this print statement 
    except KeyError: 
        print("Eror: Put in the proper key") 
    except ValueError: 
        print("Error: the values are incorrect") 
    # what happens as a backup for the others 
    except Exception: 
        print("Error: an unexpected error has occured")

# Example usage:
my_dict = {"a": 1, "b": 2}
get_value(my_dict, "c")


"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
        print("Error: File not found.")
    # this will print this if there is no error 
    else:
        print("File processed successfully.")
    # last output that will happen 
    finally:
        print("Finished attempting to process the file.")

# Example usage
process_file('example.txt')
