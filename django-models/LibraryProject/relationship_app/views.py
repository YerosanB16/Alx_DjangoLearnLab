from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.views.generic import DetailView
from .models import Book, Library, UserProfile
from .forms import RegisterForm


# Task 1: Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Task 1: Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# Task 2: Authentication
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = RegisterForm()
    return render(request, "relationship_app/register.html", {"form": form})


# Task 3: Role-based access control
def check_role(role):
    def predicate(user):
        return user.userprofile.role == role
    return predicate

@user_passes_test(check_role("Admin"))
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(check_role("Librarian"))
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(check_role("Member"))
def member_view(request):
    return render(request, "relationship_app/member_view.html")


# Task 4: Custom permissions
@permission_required("relationship_app.can_add_book")
def add_book_view(request):
    return render(request, "relationship_app/secure_action.html", {"action": "Add Book"})

@permission_required("relationship_app.can_change_book")
def edit_book_view(request):
    return render(request, "relationship_app/secure_action.html", {"action": "Edit Book"})

@permission_required("relationship_app.can_delete_book")
def delete_book_view(request):
    return render(request, "relationship_app/secure_action.html", {"action": "Delete Book"})
