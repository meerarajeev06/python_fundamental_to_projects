import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    """Reads data from JSON file safely if it exists."""
    if not os.path.exists(FILE_NAME):
        return [] # Return empty list if file doesn't exist yet
    
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_contacts(contacts):
    """Saves the updated list back into the JSON file."""
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)
    print("✅ Contacts saved successfully!\n")

def add_contact():
    name = input("Enter Name: ")
    role = input("Enter Role/Component (e.g. Lab Partner, Resistor): ")
    
    contacts = load_contacts()
    contacts.append({"name": name, "role": role})
    save_contacts(contacts)

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("\n📭 No contacts found.\n")
        return
    clear
    print("\n--- Saved Entries ---")
    for idx, c in enumerate(contacts, 1):
        print(f"{idx}. {c['name']} - {c['role']}")
    print("---------------------\n")

def main():
    while True:
        print("=== DAY 2: DATA MANAGER ===")
        print("1. View Saved Entries")
        print("2. Add New Entry")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")
        
        if choice == "1":
            view_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()  