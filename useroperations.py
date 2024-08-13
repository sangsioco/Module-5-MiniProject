from class_user import User
from add_records import add_users

users = []

def user_operations():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Return to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            add_new_user()
        elif choice == '2':
            view_user_details()
        elif choice == '3':
            display_all_users()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_new_user():
    id = input("Enter user ID: ")
    name = input("Enter user name: ")
    library_id = input("Enter user library ID: ")
    add_users(id, name, library_id)
    new_user = User(name, library_id)
    users.append(new_user)
    print(f"User '{name}' added successfully.")

def view_user_details():
    library_id = input("Enter user library ID: ")
    for user in users:
        if user.get_library_id() == library_id:
            print(f"User found: {user.get_name()}, Library ID: {user.get_library_id()}, Borrowed Books: {', '.join(user.get_borrowed_books())}")
            return
    print("User not found.")

def display_all_users():
    if not users:
        print("No users available.")
    for user in users:
        print(f"Name: {user.get_name()}, Library ID: {user.get_library_id()}, Borrowed Books: {', '.join(user.get_borrowed_books())}")
