class User:
    def __init__(self, name, library_id):
        self._name = name
        self._library_id = library_id
        self._borrowed_books = []

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_library_id(self):
        return self._library_id

    def set_library_id(self, library_id):
        self._library_id = library_id

    def get_borrowed_books(self):
        return self._borrowed_books

    def borrow_book(self, book_title):
        self._borrowed_books.append(book_title)

    def return_book(self, book_title):
        self._borrowed_books.remove(book_title)

