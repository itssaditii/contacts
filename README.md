Task 03 — Contact Book

A menu-driven contact management application built with Python. It allows users to add, list, search, edit, and delete contacts, with data stored persistently in a JSON file.

Features
Add contacts with a name, phone number, and email address.
Display all saved contacts.
Search contacts by partial name, without case sensitivity.
Edit existing contact details.
Delete contacts with confirmation.
Automatically save changes to contacts.json.
Start with an empty contact list if the file is missing or contains invalid JSON.
Requirements
Python 3.8 or newer
No external libraries required
How to Run
Clone or download this repository.
Open a terminal in the project directory.
Run:
python main.py


Alternatively, run python3 main.py if required by your system.

Menu Options
Add contact
List contacts
Search contacts
Edit contact
Delete contact
Exit
Data Storage

Contacts are stored in contacts.json as a list of dictionaries. Each contact contains a name, phone number, and email address.

The application loads contacts when it starts and saves changes after each successful addition, edit, or deletion.

If the JSON file is missing, unreadable, or malformed, the application starts with an empty list.

Implementation Notes
Each major operation has its own function.
Partial-name searches are case-insensitive.
Phone numbers are stored as strings.
Pressing Enter during editing keeps the existing value.
Deletion requires confirmation.
Author

Created as part of Task 03 — Contact Book.



Aditi Lodhi
