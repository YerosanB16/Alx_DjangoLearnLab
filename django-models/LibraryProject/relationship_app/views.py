from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Author, Book, Library, Librarian

# --------------------
# General Views
# --------------------
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
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"

# --------------------
# User registration
# --------------------
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully!")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# --------------------
# Role-based access helpers
# --------------------
def is_admin(user):
    return user.is_superuser

def is_librarian(user):
    return hasattr(user, "profile") and hasattr(user.profile, "library")  # Example check

def is_member(user):
    return not (user.is_superuser or hasattr(user, "profile") and hasattr(user.profile, "library"))

# --------------------
# Role-based views
# --------------------
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")

# --------------------
# Book management views
# --------------------
@login_required
@user_passes_test(is_librarian)
def add_book_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        publication_year = request.POST.get("publication_year")
        author_id = request.POST.get("author")
        author = get_object_or_404(Author, id=author_id)
        Book.objects.create(title=title, publication_year=publication_year, author=author)
        messages.success(request, "Book added successfully!")
        return redirect("list_books")
    authors = Author.objects.all()
    return render(request, "relationship_app/add_book.html", {"authors": authors})

@login_required
@user_passes_test(is_librarian)
def edit_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.publication_year = request.POST.get("publication_year")
        author_id = request.POST.get("author")
        book.author = get_object_or_404(Author, id=author_id)
        book.save()
        messages.success(request, "Book updated successfully!")
        return redirect("list_books")
    authors = Author.objects.all()
    return render(request, "relationship_app/edit_book.html", {"book": book, "authors": authors})

@login_required
@user_passes_test(is_librarian)
def delete_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted successfully!")
        return redirect("list_books")
    return render(request, "relationship_app/delete_book.html", {"book": book})
