from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books

urlpatterns = [
    # Function-based view
    path("books/", views.list_books, name="list_books"),

    # Class-based view
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # Authentication
    path("login/", auth_views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register_view, name="register"),  # <-- literal 'views.register_view'

    # Role-based access
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),

    # Permissions
    path("add-book/", views.add_book_view, name="add_book"),
    path("edit-book/", views.edit_book_view, name="edit_book"),
    path("delete-book/", views.delete_book_view, name="delete_book"),
]


path("add-book/", add_book_view, name="add_book"),
path("edit-book/<int:book_id>/", edit_book_view, name="edit_book"),
path("delete-book/<int:book_id>/", delete_book_view, name="delete_book"),
