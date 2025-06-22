# library_system.py

class Book:
    """Base class representing a book."""
    def __init__(self, title, author):
        """Initialize a book with title and author.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
    
    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""
    def __init__(self, title, author, file_size):
        """Initialize an ebook with title, author, and file size.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            file_size (int): The file size in KB.
        """
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """Return a string representation of the ebook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a physical printed book."""
    def __init__(self, title, author, page_count):
        """Initialize a print book with title, author, and page count.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            page_count (int): The number of pages in the book.
        """
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """Return a string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class representing a library that manages a collection of books."""
    def __init__(self):
        """Initialize a library with an empty list of books."""
        self.books = []
    
    def add_book(self, book):
        """Add a book to the library's collection.
        
        Args:
            book (Book): A Book, EBook, or PrintBook instance to add.
        """
        self.books.append(book)
    
    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)

            