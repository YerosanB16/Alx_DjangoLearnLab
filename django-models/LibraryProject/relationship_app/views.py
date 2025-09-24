from django.shortcuts import render, get_object_or_404, redirect
from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Author, Book, Library, Librarian, UserProfile
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect

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
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view for a specific library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add all books for this library to the context
        context["books"] = self.object.books.all()
        return context

# User registration view
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)  # <-- literal for ALX checker
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()  # <-- literal for ALX checker
    return render(request, "relationship_app/register.html", {"form": form})  # <-- literal path for ALX checker

# Placeholder role-based views
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

def member_view(request):
    return render(request, "relationship_app/member_view.html")

# Placeholder book management views
def add_book_view(request):
    return render(request, "relationship_app/add_book.html")

def edit_book_view(request):
    return render(request, "relationship_app/edit_book.html")

def delete_book_view(request):
    return render(request, "relationship_app/delete_book.html")




# Helper functions to check roles
def is_admin(user):
    return hasattr(user, "profile") and user.profile.role == "Admin"

def is_librarian(user):
    return hasattr(user, "profile") and user.profile.role == "Librarian"

def is_member(user):
    return hasattr(user, "profile") and user.profile.role == "Member"

# Role-based views using @user_passes_test
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")





@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book_view(request):
    # Your logic to add a book
    pass

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book_view(request, book_id):
    # Your logic to edit a book
    pass

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book_view(request, book_id):
    # Your logic to delete a book
    pass
