from connect_mysql import connect_database

def get_genre_id(genre_name):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT id FROM genres WHERE name = %s"
            cursor.execute(query, (genre_name,))
            result = cursor.fetchone()
            if result:
                return result[0]  # Return the genre_id
            else:
                return None
        except Exception as e:
            print(f"Error fetching genre ID: {e}")
            return None
        finally:
            cursor.close()
            conn.close()

def add_genres(id, name, description, category):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO genres (id, name, description, category) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (id, name, description, category))
            conn.commit()  
            print(f"Genre '{name}' added successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

def add_users(id, name, library_id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO users (id, name, library_id) VALUES (%s, %s, %s)"
            cursor.execute(query, (id, name, library_id))
            conn.commit()
            print(f"User '{name}' added successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

def get_author_id(author_name):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT id FROM authors WHERE name = %s"
            cursor.execute(query, (author_name,))
            result = cursor.fetchone()
            if result:
                return result[0] 
            else:
                return None
        except Exception as e:
            print(f"Error fetching author ID: {e}")
            return None
        finally:
            cursor.close()
            conn.close()

def add_authors(id, name, biography):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO authors (id, name, biography) VALUES (%s, %s, %s)"
            cursor.execute(query, (id, name, biography))
            conn.commit()
            print(f"Author '{name}' added successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

def add_book(id, title, isbn, publication_date, availability, author_name, genre_name):
    # Get or add author
    author_id = get_author_id(author_name)
    if author_id is None:
        print(f"Author '{author_name}' not found. Adding the author.")
        author_id = add_authors(author_name)
        if author_id is None:
            print(f"Failed to add author '{author_name}'. Book not added.")
            return
    
    # Get or add genre
    genre_id = get_genre_id(genre_name)
    if genre_id is None:
        print(f"Genre '{genre_name}' not found. Adding the genre.")
        genre_id = add_genres(genre_name)
        if genre_id is None:
            print(f"Failed to add genre '{genre_name}'. Book not added.")
            return

    # Add the book
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO book (id, title, isbn, publication_date, availability, author_id, genre_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (id, title, isbn, publication_date, availability, author_id, genre_id))
            conn.commit()
            print(f"Book '{title}' added successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
