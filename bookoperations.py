from class_book import Book
import re
from add_records import add_book
from borrow_data import borrow_book
from retrieve_data import fetch_all_books

books = []

def book_operations():
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Return to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            add_new_book()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            search_book()
        elif choice == '5':
            display_all_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def add_new_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    genre = input("Enter genre: ")
    
    while True:
        ISBN = input("Enter book ISBN (13-digit format): ")
        if re.match(r'^\d{13}$', ISBN):
            break
        else:
            print("Invalid ISBN. Please enter a 13-digit number.")
    
    publication_date = input("Enter publication date (YYYY-MM-DD): ")
    availability = True  
    
    id = None

    add_book(id, title, ISBN, publication_date, availability, author, genre)
    print(f"Book '{title}' added successfully.")


def borrow_book():
    title = input("Enter the title of the book to borrow: ")
    author = input("Enter the author of the book to borrow: ")
    books = fetch_all_books()

    found_books = []
    for book in books:
        if isinstance(book, tuple) and len(book) >= 7:
            if book[1].lower() == title.lower() and book[2].lower() == author.lower():
                found_books.append(book)
    
    if not found_books:
        print(f"No book found with title '{title}' and author '{author}'.")
        return

    if len(found_books) > 1:
        print("Multiple books found with the same title and author. Please select one:")
        for index, book in enumerate(found_books, start=1):
            print(f"{index}. Title: {book[1]}, Author: {book[2]}")
        choice = input("Enter the number corresponding to the book you want to borrow: ")
        try:
            index = int(choice) - 1
            selected_book = found_books[index]
            borrow_selected_book(selected_book)
        except (ValueError, IndexError):
            print("Invalid choice. Returning to main menu.")
    else:
        selected_book = found_books[0]
        borrow_selected_book(selected_book)


def borrow_selected_book(book):
    book_id, title, author_name, genre_name, isbn, publication_date, availability = book
    if availability: 
        print(f"You have borrowed '{title}' by {author_name} with ISBN {isbn}.")
    else:
        print(f"The book '{title}' by {author_name} is not available.")

def return_book():
    ISBN = input("Enter the ISBN of the book to return: ")
    books = fetch_all_books()
    
    for book in books:
        if book[3] == ISBN: 
            print(f"You have returned '{book[1]}' by '{book[2]}'.")
            return
    print("Book not found.")
def search_book():
    title = input("Enter the title of the book to search: ")
    books = fetch_all_books()
    
    for book in books:
        if book[1] == title:  
            print(f"Book found: Title: {book[1]}, Author: {book[2]}, ISBN: {book[3]}, Availability: {'Available' if book[4] else 'Borrowed'}")
            return
    print("Book not found.")

def display_all_books():
    books = fetch_all_books()
    if not books:
        print("No books available.")
    else:
        for book in books:
            book_id, title, author_name, genre_name, isbn, publication_date, availability = book
            availability_status = 'Available' if availability else 'Borrowed'
            print(f"ID: {book_id}, Title: {title}, Author: {author_name}, Genre: {genre_name}, ISBN: {isbn}, Publication Date: {publication_date}, Availability: {availability_status}")