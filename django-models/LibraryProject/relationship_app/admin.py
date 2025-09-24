from django.contrib import admin
from .models import Author, Book, Library, Librarian, UserProfile

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "birth_year")
    search_fields = ("name",)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "publication_year", "author")
    list_filter = ("publication_year",)
    search_fields = ("title",)

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    filter_horizontal = ("books",)

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ("name", "library")

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "bio")
