from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        query = """SELECT b.id, b.title, b.author_id, b.genre_id, b.isbn, b.publication_date, b.availability
                   FROM Book b, Authors a
                   WHERE b.author_id = a.id"""

        cursor.execute(query)

        for book in cursor.fetchall():
            print(book)
    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()