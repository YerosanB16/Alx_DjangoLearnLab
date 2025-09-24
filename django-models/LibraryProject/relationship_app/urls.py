from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    list_books, LibraryDetailView,
    register_view, admin_view, librarian_view, member_view,
    add_book_view, edit_book_view, delete_book_view
)

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Authentication
    path("login/", auth_views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", register_view, name="register"),

    # Role-based access
    path("admin-view/", admin_view, name="admin_view"),
    path("librarian-view/", librarian_view, name="librarian_view"),
    path("member-view/", member_view, name="member_view"),

    # Permissions
    path("add-book/", add_book_view, name="add_book"),
    path("edit-book/", edit_book_view, name="edit_book"),
    path("delete-book/", delete_book_view, name="delete_book"),
]
