import json
from pathlib import Path

CONTACTS_FILE = Path("contacts.json")


def load_contacts():
    """Load contacts from JSON. Return an empty list if missing or invalid."""
    try:
        with CONTACTS_FILE.open("r", encoding="utf-8") as file:
            contacts = json.load(file)

        if not isinstance(contacts, list):
            return []

        # Keep only valid contact records.
        return [
            contact for contact in contacts
            if isinstance(contact, dict)
            and isinstance(contact.get("name"), str)
            and isinstance(contact.get("phone"), str)
            and isinstance(contact.get("email", ""), str)
        ]

    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return []


def save_contacts(contacts):
    """Save contacts to JSON."""
    try:
        with CONTACTS_FILE.open("w", encoding="utf-8") as file:
            json.dump(contacts, file, indent=4, ensure_ascii=False)
        return True
    except OSError as error:
        print(f"Error saving contacts: {error}")
        return False


def add_contact(contacts):
    """Add a new contact."""
    print("\n--- Add Contact ---")
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)

    if save_contacts(contacts):
        print("Contact added successfully!")
    else:
        contacts.pop()


def list_contacts(contacts):
    """Display all saved contacts."""
    print("\n--- Contact List ---")

    if not contacts:
        print("No contacts found.")
        return

    for index, contact in enumerate(contacts, start=1):
        print(f"\nContact {index}")
        print(f"Name:  {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact.get('email', '')}")


def search_contacts(contacts):
    """Search for contacts using part of a name."""
    query = input("\nEnter a name to search: ").strip().casefold()

    if not query:
        print("Search term cannot be empty.")
        return

    matches = [
        contact for contact in contacts
        if query in contact["name"].casefold()
    ]

    if not matches:
        print("No matching contacts found.")
        return

    print("\n--- Search Results ---")
    for contact in matches:
        print(f"Name:  {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact.get('email', '')}")
        print("-" * 25)


def edit_contact(contacts):
    """Edit a contact selected by its list number."""
    list_contacts(contacts)

    if not contacts:
        return

    try:
        index = int(input("\nEnter contact number to edit: ")) - 1
    except ValueError:
        print("Please enter a valid number.")
        return

    if not 0 <= index < len(contacts):
        print("Invalid contact number.")
        return

    contact = contacts[index]

    print("Press Enter to keep the current value.")

    name = input(f"Name [{contact['name']}]: ").strip()
    phone = input(f"Phone [{contact['phone']}]: ").strip()
    email = input(
        f"Email [{contact.get('email', '')}]: "
    ).strip()

    updated_contact = {
        "name": name or contact["name"],
        "phone": phone or contact["phone"],
        "email": email or contact.get("email", "")
    }

    if not updated_contact["name"]:
        print("Name cannot be empty.")
        return

    contacts[index] = updated_contact

    if save_contacts(contacts):
        print("Contact updated successfully!")
    else:
        contacts[index] = contact


def delete_contact(contacts):
    """Delete a contact after confirmation."""
    list_contacts(contacts)

    if not contacts:
        return

    try:
        index = int(input("\nEnter contact number to delete: ")) - 1
    except ValueError:
        print("Please enter a valid number.")
        return

    if not 0 <= index < len(contacts):
        print("Invalid contact number.")
        return

    contact = contacts[index]
    confirm = input(
        f"Delete {contact['name']}? (y/n): "
    ).strip().lower()

    if confirm == "y":
        contacts.pop(index)

        if save_contacts(contacts):
            print("Contact deleted successfully!")
        else:
            contacts.insert(index, contact)
    else:
        print("Deletion cancelled.")


def main():
    contacts = load_contacts()

    actions = {
        "1": add_contact,
        "2": list_contacts,
        "3": search_contacts,
        "4": edit_contact,
        "5": delete_contact
    }

    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add contact")
        print("2. List contacts")
        print("3. Search contacts")
        print("4. Edit contact")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice in actions:
            actions[choice](contacts)
        elif choice == "6":
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()
