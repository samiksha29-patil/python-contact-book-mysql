from contact import Contact
from contact_book import ContactBook

def display_menu():
    print("\n" + "="*30)
    print("Contact Book Menu")
    print("="*30)
    print("1. Add Contact")
    print("2. Display All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact_ui(contact_book):
    print("\n-- Add New Contact --")
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    contact= Contact(name, phone, email)
    contact_book.add_contact(contact)
    print("Contact added successfully!")

def search_contact_ui(contact_book):
    name = input("Enter name to search: ").strip()
    contact=contact_book.search_contact(name)
    if contact:
        print("\nConatact found:")
        contact.display_contact()
    else:
        print("Contact not found.")

def update_contact_ui(contact_book):
    name = input("Enter name of contact to update: ").strip()
    new_name=input("Enter new name(or press Enter to keep current): ").strip()
    new_phone=input("Enter new phone number (or press Enter to keep current): ").strip()
    new_email=input("Enter new email (or press enter to keep current): ").strip()

    contact_book.update_contact(
        name,
        new_name if new_name else None,
        new_phone if new_phone else None,
        new_email if new_email else None 
    )

def delete_contact_ui(contact_book):
    name=input("Enter name of contact to delete: ").strip()
    contact_book.delete_contact(name)

def main():
    contact_book=ContactBook()
    while True:
        display_menu()
        choice=input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_contact_ui(contact_book)
        elif choice == '2':
            print("\nAll Contacts:")
            contact_book.display_all_contacts()
        elif choice == '3':
            search_contact_ui(contact_book)
        elif choice == '4':
            update_contact_ui(contact_book)
        elif choice == '5':
            delete_contact_ui(contact_book)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

main()