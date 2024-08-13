from connect_mysql import connect_database

def fetch_all_books():
    conn = connect_database()
    books = []
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = """SELECT 
                    b.id, 
                    b.title, 
                    a.name AS author_name, 
                    g.name AS genre_name, 
                    b.isbn, 
                    b.publication_date, 
                    b.availability
                FROM 
                    book b
                JOIN 
                    authors a ON b.author_id = a.id
                JOIN 
                    genres g ON b.genre_id = g.id"""

            cursor.execute(query)
            books = cursor.fetchall()

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

    return books

def fetch_all_authors():
    conn = connect_database()
    authors = []
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = """SELECT id, name, biography FROM authors"""

            cursor.execute(query)
            authors = cursor.fetchall()

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

    return authors

def fetch_all_genres():
    conn = connect_database()
    genres = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = """SELECT id, name, description, category FROM genres"""
            cursor.execute(query)
            genres = cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
    return genres