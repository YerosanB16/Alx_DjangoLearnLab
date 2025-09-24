from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Author, Book, Library, Librarian

# Function-based views
def home(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    libraries = Library.objects.all()
    return render(request, "relationship_app/home.html", {
        "authors": authors,
        "books": books,
        "libraries": libraries,
    })

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for a specific library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add books in this library to the context
        context['books'] = self.object.books.all()
        return context

# Placeholder authentication and role views (implement as needed)
def register_view(request):
    pass

def admin_view(request):
    pass

def librarian_view(request):
    pass

def member_view(request):
    pass

def add_book_view(request):
    pass

def edit_book_view(request):
    pass

def delete_book_view(request):
    pass
