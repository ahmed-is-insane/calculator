
print (" TASK NUMBER 4 \n \n ")


import os

# Initialize an empty dictionary for contacts 
contacts = {}

# A Function to add a new contact
def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")
    contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
    print(f"{name} added to contacts.")

# Function to view all contacts
def view_contacts():
    print("\nContacts:")
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {info['Phone']}")
        print(f"Email: {info['Email']}")
        print(f"Address: {info['Address']}\n")

# Function to search for a contact by name or phone number
def search_contact():
    search_term = input("Enter the name of the individual to search: ")
    found = False
    for name, info in contacts.items():
        if search_term in name or search_term == info['Phone']:
            print(f"\nName: {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print(f"Address: {info['Address']}\n")
            found = True
    if not found:
        print("Contact not found.")

# Function to update contact details
def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    if name in contacts:
        print("Current Contact Information:")
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['Email']}")
        print(f"Address: {contacts[name]['Address']}")
        
        contacts[name]['Phone'] = input("Enter new phone number: ")
        contacts[name]['Email'] = input("Enter new email: ")
        contacts[name]['Address'] = input("Enter new address: ")
        
        print(f"Contact {name} updated successfully.")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found.")

# Main program loop
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please enter a valid option.")