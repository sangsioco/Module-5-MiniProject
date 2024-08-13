from class_genre import Genre
from retrieve_data import fetch_all_genres
from add_records import add_genres

def genre_operations():
    while True:
        print("\nGenre Operations:")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")
        print("4. Return to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            add_new_genre()
        elif choice == '2':
            view_genre_details()
        elif choice == '3':
            display_all_genres()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_new_genre():
    id = input("Enter genre ID: ")
    name = input("Enter genre name: ")
    description = input("Enter genre description: ")
    category = input("Enter genre category: ")
    add_genres(id, name, description, category) 

def view_genre_details():
    name = input("Enter genre name: ")
    genres = fetch_all_genres()  
    for genre in genres:
        if genre[1] == name:  
            print(f"Genre found: Name: {genre[1]}, Description: {genre[2]}, Category: {genre[3]}")
            return
    print("Genre not found.")

def display_all_genres():
    genres = fetch_all_genres()
    if genres:
        for genre in genres:
            print(f"ID: {genre[0]}, Name: {genre[1]}, Description: {genre[2]}, Category: {genre[3]}")
    else:
        print("No genres found in the database.")
