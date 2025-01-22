# library_system.py

class Book:
    """Base class representing a general book."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Class representing an e-book, inheriting from Book."""
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size  # in kilobytes (KB)

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Class representing a printed book, inheriting from Book."""
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class representing a library, demonstrating composition."""
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        """Adds a book (Book, EBook, or PrintBook) to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        """Lists all books in the library."""
        if not self.books:
            print("The library has no books.")
        else:
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. {book}")
