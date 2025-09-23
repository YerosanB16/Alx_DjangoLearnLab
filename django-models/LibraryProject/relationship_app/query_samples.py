from .models import Author, Book, Library

# All books by a specific author
author = Author.objects.first()
books_by_author = Book.objects.filter(author=author)

# All books in a library
library = Library.objects.first()
library_books = library.books.all()

# Librarian for a library
librarian = library.librarian
