from .models import Author, Book, Library, Librarian

def sample_queries():
    # Query all books by a specific author
    author = Author.objects.first()
    books_by_author = Book.objects.filter(author=author)

    # List all books in a library
    library = Library.objects.first()
    books_in_library = library.books.all() if library else []

    # Retrieve the librarian for a library
    librarian = Librarian.objects.filter(library=library).first() if library else None

    return books_by_author, books_in_library, librarian
