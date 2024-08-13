from class_author import Author
from add_records import add_authors
from retrieve_data import fetch_all_authors

authors = []

def author_operations():
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Return to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            add_new_author()
        elif choice == '2':
            view_author_details()
        elif choice == '3':
            display_all_authors()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_new_author():
    id = input("Enter author ID: ")
    name = input("Enter author name: ")
    biography = input("Enter author biography: ")
    add_authors(id, name, biography)  
    print(f"Author '{name}' added successfully.")

def view_author_details():
    name = input("Enter author name: ")
    authors = fetch_all_authors()  
    for author in authors:
        if author[1] == name:  
            print(f"Author found: Name: {author[1]}, Biography: {author[2]}")
            return
    print("Author not found.")

def display_all_authors():
    authors = fetch_all_authors()
    if authors:
        for author in authors:
            print(f"ID: {author[0]}, Name: {author[1]}, Biography: {author[2]}")
    else:
        print("No authors found in the database.")
