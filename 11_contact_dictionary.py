contact_book = {}

def add_contact():
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    contact_book[name] = number
    print(f"Contact {name} added.")

def delete_contact():
    name = input("Enter the contact name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")

def list_contacts():
    if contact_book:
        print("Your contacts:")
        for name, number in contact_book.:
            print(f"{name}: {number}")
    else:
        print("No contacts found.")

while True:
    print("""
    1: Add contact
    2: Delete contact
    3: List contacts
    4: Exit
    """)
    
    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        delete_contact()
    elif choice == "3":
        list_contacts()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid option. Please choose again.")


  
 

