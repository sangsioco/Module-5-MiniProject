from connect_mysql import connect_database
from datetime import date

user_id = 3
book_id = 5

def borrow_book(user_id, book_id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            borrow_query = """
                INSERT INTO borrowed_books (user_id, book_id, borrowed_date)
                VALUES (%s, %s, %s)
            """
            today_date = date.today().isoformat()
            cursor.execute(borrow_query, (user_id, book_id, today_date))

            update_query = """
                UPDATE book
                SET availability = 0  # Assuming 0 means not available
                WHERE id = %s
            """
            cursor.execute(update_query, (book_id,))

            conn.commit()
            print("Book borrowed successfully.")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

