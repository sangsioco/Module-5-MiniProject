class Book:
    def __init__(self, title, author, ISBN, publication_date, availability_status=True):
        self._title = title
        self._author = author
        self._ISBN = ISBN
        self._publication_date = publication_date
        self._availability_status = availability_status

    # Getters and setters
    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    def get_ISBN(self):
        return self._ISBN

    def set_ISBN(self, ISBN):
        self._ISBN = ISBN

    def get_publication_date(self):
        return self._publication_date

    def set_publication_date(self, publication_date):
        self._publication_date = publication_date

    def is_available(self):
        return self._availability_status

    def borrow_book(self):
        if self._availability_status:
            self._availability_status = False
            return True
        return False

    def return_book(self):
        self._availability_status = True

