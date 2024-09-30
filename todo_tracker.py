
todos = ["get cash", "spend cash", "cry"]
# it oprns the file and reads it line by line
with open("todo_tracker.txt") as file:
    todos = file.readlines()

# creates the while loop so the functions repeat themselves over and over again 
while True:  
    print("\nYour current todos are:")
    for x in todos:
    # makes the list of the things to do more ordered 
        print(x)

    newtodos = str(input("Would you like to add, remove, or exit?: ")).strip().lower()


    # the add makes use the append which would add the new thing the user input in the code
    if newtodos == "add": 
        newtodos1 = input("What is your new todo? ").strip()
        todos.append(newtodos1 + "\n")
        print("Todo added!")
    elif newtodos == "exit":
           # Save all todos to the file before exiting

           with open("todo_tracker.txt","w") as file: 
             todos = file.writelines(todos)   
        # Makes sure the code does not repeat itself over and over
           break   
    elif newtodos == "remove":     
    
    # 
        if not todos:
            print("No todos to remove.")
        # continue ends the current iteration and creates a new one 
        
                        
        
            
           
        
       
        # The del function deletes any new todos by the number minus 1 
        print(newtodos)
        newtodos3 = int(input("Which # would you like to remove: ")) 
        del todos[newtodos3 - 1]  

    

   
   

