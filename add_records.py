from connect_mysql import connect_database

def add_genres(id, name, description, category):
    query = "INSERT INTO genres (id, name, description, category) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (id, name, description, category))

def add_users(id, name, library_id):
    query = "INSERT INTO users (id, name, library_id) VALUES (%s, %s, %s)"
    cursor.execute(query, (id, name, library_id))

def add_authors(id, name, biography):
    query = "INSERT INTO authors (id, name, biography) VALUES (%s, %s, %s)"
    cursor.execute(query, (id, name, biography))

def add_book(id, title, isbn, publication_date, availability, author_id, genre_id):
    query = "INSERT INTO book (id, title, isbn, publication_date, availability, author_id, genre_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (id, title, isbn, publication_date, availability, author_id, genre_id))

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        add_genres(2, "Paranormal", "Paranomal romance, Mystery, Adventure", "Fiction")

        add_users(3, "Mary Sue", "10")  # Assuming library_id is a string

        add_authors(120, "Charlaine Harris", "American author who specialize in mystery")
        
        # Use valid author_id and genre_id that exist in their respective tables
        add_book(5, "Dead Until Dark", "9780441018253", "2009-07-09", True, 120, 2)

        conn.commit()
        print("All information added successfully.")
    
    except Exception as e:
        print(f"Error {e}")
    
    finally:
        cursor.close()
        conn.close()
