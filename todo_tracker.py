
todos = ["get cash", "spend cash", "cry"]
# creates the while loop so the functions repeat themselves over and over again 
while True:  
    print("\nYour current todos are:")
    for x in todos:
    # makes the list of the things to do more ordered 
        print(x)

    newtodos = input("Would you like to add or remove a todo?: ").strip().lower()

    # the add makes use the append which would add the new thing the user input in the code
    if newtodos == "add": 
        newtodos1 = input("What is your new todo? ").strip()
        todos.append(newtodos1)
        print("Todo added!")
    elif newtodos == "remove":
    # 
        if not todos:
            print("No todos to remove.")
        # continue ends the current iteration and creates a new one 
            continue
        
       
        # The del function deletes any new todos by the number minus 1 
        print(newtodos)
        newtodos3 = int(input("Which # would you like to remove: ")) 
        del todos[newtodos3 - 1]  

    

   
   

