from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from .models import Book, Library

# --------------------
# Function-Based View
# List all books
# --------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# --------------------
# Class-Based View
# Display Library details
# --------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# --------------------
# Authentication Views
# --------------------
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')


# --------------------
# Role-Based Views
# --------------------
def is_admin(user):
    return user.userprofile.role == "Admin"

def is_librarian(user):
    return user.userprofile.role == "Librarian"

def is_member(user):
    return user.userprofile.role == "Member"

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
