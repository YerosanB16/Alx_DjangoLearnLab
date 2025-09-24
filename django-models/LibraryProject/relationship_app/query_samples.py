from .models import Author, Book, Library, Librarian

# -------------------------------
# 1. List all books in a library
# -------------------------------
def list_books_in_library(library_name):
    """
    Returns all books in a given library by name.
    """
    library = Library.objects.get(name=library_name)
    return library.books.all()

# -------------------------------
# 2. Query all books by a specific author
# -------------------------------
def list_books_by_author(author_name):
    """
    Returns all books written by a specific author.
    """
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)  # Use objects.filter(author=author)

# -------------------------------
# 3. Retrieve the librarian for a library
# -------------------------------
def get_librarian_for_library(library_name):
    """
    Returns the librarian assigned to a specific library.
    """
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)  # Use objects.get(library=library)
