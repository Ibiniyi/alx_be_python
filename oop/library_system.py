# library_system.py

class Book:
    """Base class representing a general book."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def __str__(self):
        return f"'{self.title}' by {self.author} (EBook, {self.file_size}MB)"


class PrintBook(Book):
    """Derived class representing a printed book."""
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"'{self.title}' by {self.author} (PrintBook, {self.page_count} pages)"


class Library:
    """Class demonstrating composition — manages a collection of Book objects."""
    def __init__(self):
        self.books = []  # List to hold book objects

    def add_book(self, book: Book):
        """Add a Book, EBook, or PrintBook to the library."""
        self.books.append(book)
        print(f"Added {book.title} to the library.")

    def list_books(self):
        """List all books currently in the library."""
        print("\nBooks available in the library:")
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

