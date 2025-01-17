
# Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is available."""
        return not self._is_checked_out

# Library class
class Library:
    def __init__(self):
        self._books = []  # Private list to store books

    def add_book(self, book):
        """Adds a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title if available."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out: {book.title} by {book.author}")
                else:
                    print(f"The book '{title}' is already checked out.")
                return
        print(f"The book '{title}' is not available in the library.")

    def return_book(self, title):
        """Returns a book by title if it was checked out."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned: {book.title} by {book.author}")
                else:
                    print(f"The book '{title}' was not checked out.")
                return
        print(f"The book '{title}' is not available in the library.")

    def list_available_books(self):
        """Lists all books that are currently available in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are available at the moment.")
